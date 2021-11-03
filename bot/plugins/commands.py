from telegram import Update, ForceReply
from telegram.parsemode import ParseMode
from ..utils import google_tr
from googletrans import LANGUAGES
from bot import START_MESSAGE


def start_msg(update: Update, _) -> None:
    """
    Send a message when the command /start is issued.
    """
    user = update.effective_user
    update.message.reply_text(
        f'*Hello* {user.mention_markdown()}, {START_MESSAGE}',
        ParseMode.MARKDOWN
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


def help_msg(update: Update, _) -> None:
    lang_codes_list = "\n".join(LANGUAGES)
    update.message.reply_text(f'`{lang_codes_list}`', ParseMode.MARKDOWN)
