
from telegram.update import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import settings

updater = Updater(settings.BOT_TOKEN)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Salom!')


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()

