from telegram.ext import CallbackContext
from telegram import Update, InputFile

async def send_instruction_and_photo(update: Update, context: CallbackContext, message: str, photo_path: str) -> None:
    query = update.callback_query
    chat_id = query.message.chat_id

    # Редактирование текста сообщения и установка ожидаемого ответа
    context.user_data['expected_reply'] = True
    await query.edit_message_text(message)

    # Отправка примера фото
    with open(photo_path, "rb") as photo_file:
        await context.bot.send_photo(chat_id=chat_id, photo=photo_file)

async def handle_buttons(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    context.user_data['last_button_pressed'] = query.data

    switch_dict = {
        "1": (
              "Для определения материала оправы, пожалуйста, пришлите фотографию очков.", 
              "img/frame.jpg"
            ),
        "2": (
              "В разработке!!",
              "img/tag.jpg"
            )
        # "2": (
        #       "В разработке!! Чтобы найти оправу по метке, пришлите фото метки как можно отчетливее и крупнее.",
        #       "img/tag.jpg"
        #     )
    }

    message, photo_path = switch_dict.get(query.data, (None, None))

    if message and photo_path:
        await send_instruction_and_photo(
                update, 
                context,
                message, 
                photo_path
            )