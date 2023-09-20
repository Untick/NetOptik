from telegram.ext import CallbackContext
from telegram import Update
from config import pm

async def handle_buttons(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    chat_id = query.message.chat_id

    context.user_data['last_button_pressed'] = query.data

    # Редактирование текста сообщения и установка ожидаемого ответа
    context.user_data['expected_reply'] = True
    await query.edit_message_text(pm.t(f'buttons.{query.data}'))

    # Отправка примера фото
    with open(pm.t(f'buttons.{query.data}_img_path'), "rb") as photo_file:
        await context.bot.send_photo(chat_id=chat_id, photo=photo_file)
