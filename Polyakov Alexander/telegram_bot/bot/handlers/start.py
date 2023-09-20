from telegram.ext import CallbackContext
from telegram import Update
from keyboard import start_keyboard
from config import pm

async def handle_start(update: Update, context: CallbackContext) -> None:
    reply_markup = await start_keyboard()  
    await update.message.reply_text(pm.t('greeting'), reply_markup=reply_markup)
