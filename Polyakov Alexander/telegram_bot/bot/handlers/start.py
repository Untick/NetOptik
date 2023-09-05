from telegram.ext import CallbackContext
from telegram import Update
from keyboard import start_keyboard

async def handle_start(update: Update, context: CallbackContext) -> None:
    reply_markup = await start_keyboard()  
    await update.message.reply_text(
        "Привет!\n\n"
        "Это AI Optic Bot.\n\n"
        "Что я могу для вас сделать?\n\n\n"
        "Для повторного вызова меню отправьте любое сообщение.",
        reply_markup=reply_markup
    )





