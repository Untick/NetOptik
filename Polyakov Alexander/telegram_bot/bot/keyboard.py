from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def start_keyboard():
    keyboard = [[InlineKeyboardButton("Определить материал", callback_data="1"),
                 InlineKeyboardButton("Найти оправу по метке", callback_data="2")]]

    return InlineKeyboardMarkup(keyboard)