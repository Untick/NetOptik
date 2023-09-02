from telegram.ext import CallbackContext
from telegram import Update

from keyboard import start_keyboard

async def handle_start(update: Update, context: CallbackContext) -> None:
    reply_markup = await start_keyboard()  
    await update.message.reply_text('Привет! Это AI Optic Bot.', reply_markup=reply_markup)
