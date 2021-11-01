from telegram import Update
from ..utils import google_tr
from googletrans import LANGUAGES


def income_text_handler(update: Update, _) -> None:
    """
    Provides translating text for the user
    """
    if update.message.text in LANGUAGES:
        result = google_tr(update.message.reply_to_message.text,
                           update.message.text)
        update.message.reply_text(result)
    else:
        update.message.reply_text('Language not supported')
