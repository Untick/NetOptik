from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image
import numpy as np
import os
import numpy as np
from PIL import Image

IMG_WIDTH = 256
IMG_HEIGHT = 512
CLASS_COUNT = 2
IMG_WIDTH_AUTOENCODER = 64
IMG_HEIGHT_AUTOENCODER = 128
THRESHOLD_ERR = 0.01
FILE_MODEL_AUTOENCODER = 'autocoder_best_model_v64x128.h5'  # Модель автокодировщика для распознавания очков на картинке
FILE_BEST_WEIGHTS = 'material_best_model_w.h5'      # Веса модели для определения материала оправы


# ====== Модель определения материала оправ и загрузка весов (были только веса и не было сохраненной модели)=====================================
def load_model_material():
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization
    from keras.applications import VGG16

    model_vgg16_trained = VGG16(weights='imagenet',
                            include_top=False,
                            input_shape=(IMG_WIDTH, IMG_HEIGHT, 3))

    model_vgg16_trained.trainable = False
    model = Sequential()
    model.add(model_vgg16_trained)
    model.add(Flatten(name='Class_1'))
    model.add(Dense(256, activation='relu', name='Class_2'))
    model.add(Dropout(0.3))
    model.add(Dense(CLASS_COUNT, activation='softmax', name='Class_3'))

    model.load_weights(FILE_BEST_WEIGHTS)
    return model


# Модель для определения подходит ли изображение для предсказания (можно ли определить очки) на основе автокодировщика
def load_model_ae():
    from tensorflow.keras.models import load_model
    model_ae = load_model(FILE_MODEL_AUTOENCODER)
    return model_ae


# функция преобразования изображения в массив для автокодировщика
def image_to_array_ae(image):
    img_ae = Image.open(BytesIO(image)).resize((IMG_HEIGHT_AUTOENCODER, IMG_WIDTH_AUTOENCODER)).convert('L')
    data_images_ae = []
    data_images_ae.append(np.array(img_ae))
    x_data_ae = np.array(data_images_ae)
    x_data_ae_ = x_data_ae.reshape(-1, x_data_ae.shape[1], x_data_ae.shape[2], 1)
    x_data_ae = x_data_ae_.astype('float32') / 255.
    return x_data_ae


# функция преобразования изображения в массив для распознавания материала оправы
def image_to_array_material(image):
    img = Image.open(BytesIO(image)).resize((IMG_HEIGHT, IMG_WIDTH))
    data_images = []
    data_images.append(np.array(img))
    x_data = np.array(data_images)
    return x_data


# Функция определения очки или нет по порогу среднеквадратической ошибки
def img_error(x_data, pred):
    from sklearn.metrics import mean_squared_error
    image_size = x_data.shape[1] * x_data.shape[2]  # Расчет количества пикселей изображения
    err_pred = mean_squared_error(x_data.reshape(-1, image_size).T,
                                     pred.reshape(-1, image_size).T,
                                     multioutput='raw_values')
    return err_pred.mean()


model_ae = load_model_ae()
model_material = load_model_material()


#====== Запуск бота =======================================================================================
# возьмем переменные окружения из .env
load_dotenv()

# загружаем токен бота
TOKEN = os.environ.get("TOKEN")

# функция команды /start
async def start(update, context):
    await update.message.reply_text('Привет! Отправь этому боту фотографию оправы для распознавания материала.')


# функция обработки изображений
async def material(update, context):
    await update.message.reply_text('Мы получили от тебя фотографию. Идет распознавание материала...')

    file = await update.message.document.get_file()
    # извлекаем изображение в формате bytearray
    file = await update.message.document.get_file()
    image = await file.download_as_bytearray()

    x_data_ae = image_to_array_ae(image)
    pred_ae = model_ae.predict(x_data_ae)                   # предсказание очки или нет на картинке
    error_in_glass_definition = img_error(x_data_ae, pred_ae)
    print("Среднеквадратичная ошибка=", error_in_glass_definition)
    if error_in_glass_definition > THRESHOLD_ERR:
        await update.message.reply_text("Очки на фото не распознаны. Попробуйте другую фотографию")
    else:
        x_data = image_to_array_material(image)
        pred_material = model_material.predict(x_data)      # предсказание материала очков
        if np.argmax(pred_material) == 0:
            frame_material = "Оправа металлическая"
        else:
            frame_material = "Оправа пластиковая"

        # возвращаем результат обратно пользователю
        await update.message.reply_text(frame_material)


def main():
    # точка входа в приложение
    application = Application.builder().token(TOKEN).build()
    print('Бот запущен...')

    # добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # добавляем обработчик фото
    application.add_handler(MessageHandler(filters.Document.IMAGE, material))

    # запуск приложения (для остановки нужно нажать Ctrl-C)
    application.run_polling()


if __name__ == "__main__":
    main()