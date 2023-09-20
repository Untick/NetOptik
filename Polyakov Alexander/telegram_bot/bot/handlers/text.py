from telegram.ext import CallbackContext
from telegram import Update

from keyboard import start_keyboard
from config import pm

async def handle_text(update: Update, context: CallbackContext) -> None:
    if not context.user_data.get('expected_reply'):
        # Кнопки для любого текстового сообщения
        reply_markup = await start_keyboard()
        await update.message.reply_text(
            pm.t('what_to_do'), 
            reply_markup=reply_markup
        )
