from telegram.ext import CallbackContext
from telegram import Update
from processing.recognize_api import RecognizeApi

# Ваш обработчик фотографий
async def handle_photo(update: Update, context: CallbackContext) -> None:
    last_button = context.user_data.get('last_button_pressed')
    
    if last_button:
        await update.message.reply_text(
            f"Изображение в очереди",
            reply_to_message_id=update.message.message_id
        )

        imageurl = await update.message.photo[-1].get_file()

        recognizer = RecognizeApi()

        if last_button == "1":
            res = await recognizer.fetch_material(imageurl['file_path'])
            result = res.get('result', 'unknown')
    
            if result == 'plastic':
                message = "Я думаю, что это пластик."
            elif result == 'metall':
                message = "Я думаю, что это металл."
            else:
                message = "Не могу определить материал."

        elif last_button == "2":
            # res = await recognizer.fetch_tag(imageurl['file_path'])
            message = "В разработке. Скоро будет."

        await update.message.reply_text(message)

        context.user_data['expected_reply'] = False
