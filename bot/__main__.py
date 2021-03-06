from bot import logger, BOT_TOKEN, __version__
from .plugins import income_text_handler, tr_command, help_msg
from .plugins import start_msg
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)


if __name__ == '__main__':
    LOGGER = logger(__name__)
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler(
        "start", start_msg, Filters.chat_type.private))
    dispatcher.add_handler(CommandHandler(
        "help", help_msg, Filters.chat_type.private))
    # tr
    dispatcher.add_handler(
        CommandHandler("tr", tr_command,
                       Filters.text)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command & Filters.reply & Filters.chat_type.private,
                       income_text_handler)
    )
    updater.start_polling()
    LOGGER.info(f'Bot is Online - Version {__version__}')
    updater.idle()
    LOGGER.info(f'Bot is Offline')
