from telegram.ext import (Application, CommandHandler, MessageHandler,
                          CallbackContext, CallbackQueryHandler, filters)
from telegram import Update
from dotenv import load_dotenv
import os

# Импортируем функции из других файлов
from handlers.start import handle_start
from handlers.text import handle_text
from handlers.buttons import handle_buttons
from handlers.photo import handle_photo


load_dotenv()
TOKEN = os.environ.get("TELEGRAM_API_TOKEN")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Обработчики
    application.add_handler(CommandHandler("start", handle_start))
    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, handle_photo))
    application.add_handler(MessageHandler(filters.TEXT, handle_text))
    # Обработчик нажатия Inline кнопок
    application.add_handler(CallbackQueryHandler(handle_buttons))
    
    application.run_polling()

if __name__ == "__main__":
    main()
