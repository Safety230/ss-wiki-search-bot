
from telegram.update import Update
from telegram.ext import Updater, CommandHandler, CallbackContext



updater = Updater(token='5241365514:AAHO0jN87V92rLAQvtQEvDxA5vBKFAAOfaA')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Salom!')


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()

