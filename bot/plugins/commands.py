from telegram import Update, ForceReply
from ..utils import google_tr
from googletrans import LANGUAGES


def start_msg(update: Update, _) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}!\n',
        reply_markup=ForceReply(selective=True),
    )


def tr_command(update: Update, _) -> None:
    """
    Sends a message when the /tr command is entered.
    """
    lang_code = update.message.text.split(" ")[-1]
    if lang_code in LANGUAGES:
        result = google_tr(update.message.reply_to_message.text, lang_code)
        update.message.reply_text(result)
    else:
        update.message.reply_text('Language not supported')
