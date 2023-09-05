from telegram.ext import CallbackContext
from telegram import Update

from keyboard import start_keyboard

async def handle_text(update: Update, context: CallbackContext) -> None:
    if not context.user_data.get('expected_reply'):
        # Кнопки для любого текстового сообщения
        reply_markup = await start_keyboard()
        await update.message.reply_text(
            'Что сделать?', 
            reply_markup=reply_markup
        )
