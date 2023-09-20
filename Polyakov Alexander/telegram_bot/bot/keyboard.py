from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import pm

async def start_keyboard():
    keyboard = [[InlineKeyboardButton(pm.t('keyboard.material'), callback_data="material"),
                 InlineKeyboardButton(pm.t('keyboard.type'), callback_data="type"),
                 InlineKeyboardButton(pm.t('keyboard.tag'), callback_data="tag")]]

    return InlineKeyboardMarkup(keyboard)
 