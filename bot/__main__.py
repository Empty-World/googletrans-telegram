from re import I
from bot import BOT_TOKEN
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
    updater.start_polling()
    updater.idle()