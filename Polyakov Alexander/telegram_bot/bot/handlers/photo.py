from telegram.ext import CallbackContext
from telegram import Update

# Ваш обработчик фотографий
async def handle_photo(update: Update, context: CallbackContext) -> None:
    last_button = context.user_data.get('last_button_pressed')
    
    if last_button:
      await update.message.reply_text(
          f"Вы нажали на кнопку {last_button}",
          reply_to_message_id=update.message.message_id
      )
    
      # достаем файл изображения из сообщения
      file = await update.message.photo[-1].get_file()
      
      # сохраняем изображение на диск
      await file.download_to_drive("image.jpg")
      await update.message.reply_text('Фото сохранено.')

      context.user_data['expected_reply'] = False
