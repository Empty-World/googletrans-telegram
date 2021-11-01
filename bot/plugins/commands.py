from telegram import Update

def start_msg(update: Update, _) ->None:
    """
    Replies to /start command  
    """
    update.message.reply_text("**Hello World**",)