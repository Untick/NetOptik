from telegram.ext import CallbackContext
from telegram import Update
from predict.predictor import Predictor
from config import pm

async def handle_media(update: Update, context: CallbackContext, get_file_method: str) -> None:
    last_button = context.user_data.get('last_button_pressed')

    if not last_button:
        return

    await update.message.reply_text(
        pm.t('predict.started'),
        reply_to_message_id=update.message.message_id
    )

    if get_file_method == 'document':
        imageurl = await update.message.document.get_file()
    elif get_file_method == 'photo':
        imageurl = await update.message.photo[-1].get_file()
    else:
        raise ValueError(f"Unknown get_file_method: {get_file_method}")

    predictor = Predictor(imageurl['file_path'], last_button)
    message = await predictor.predict()
    await update.message.reply_text(message)

    context.user_data['expected_reply'] = False
