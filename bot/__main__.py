from re import I
from bot import BOT_TOKEN
from .plugins import income_text_handler, tr_command
from .plugins import start_msg
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)


if __name__ == '__main__':
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_msg))
    # tr
    dispatcher.add_handler(
        CommandHandler("tr", tr_command,
                       Filters.text & Filters.reply & Filters.group)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command & Filters.reply,
                       income_text_handler)
    )
    updater.start_polling()
    updater.idle()
