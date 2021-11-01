from telegram import Update
from ..utils import google_tr
from googletrans import LANGUAGES


def start_msg(update: Update, _) -> None:
    """
    Replies to /start command  
    """
    print(update.message)
    update.message.reply_text("**Hello World**",)


def tr_command(update: Update, _) -> None:
    lang_code = update.message.text.split(" ")[-1]
    if lang_code in LANGUAGES:
        result = google_tr(update.message.reply_to_message.text, lang_code)
        update.message.reply_text(result)
    else:
        update.message.reply_text('Language not supported')
