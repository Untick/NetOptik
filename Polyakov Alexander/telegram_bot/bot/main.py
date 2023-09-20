from telegram.ext import (Application, CommandHandler, MessageHandler,
                           CallbackQueryHandler, filters)

from dotenv import load_dotenv
import os

# Импортируем хендлеры 
from handlers.start import handle_start
from handlers.text import handle_text
from handlers.buttons import handle_buttons
from handlers.media import handle_media

load_dotenv()
TOKEN = os.environ.get("TELEGRAM_API_TOKEN")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Обработчики
    application.add_handler(CommandHandler("start", handle_start))
    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, lambda u, c: handle_media(u, c, 'photo')))
    application.add_handler(MessageHandler(filters.Document.IMAGE & ~filters.COMMAND, lambda u, c: handle_media(u, c, 'document')))
    application.add_handler(MessageHandler(filters.TEXT, handle_text))
    # Обработчик нажатия Inline кнопок
    application.add_handler(CallbackQueryHandler(handle_buttons))
    
    application.run_polling()

if __name__ == "__main__":
    main()
