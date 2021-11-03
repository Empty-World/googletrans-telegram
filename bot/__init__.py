import logging
from logging.handlers import RotatingFileHandler
from .env import get_env


__version__ = "0.1.1"
__author__ = "Abhijith N T"

BOT_TOKEN = get_env('BOT_TOKEN')


START_MESSAGE = "*It is the telegram bot that uses to translate messages.*"


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            'tr_bot_log.txt',
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("telegram").setLevel(logging.WARNING)


def logger(logs: str) -> logging.Logger:
    """
    logger function  
    """
    return logging.getLogger(logs)
