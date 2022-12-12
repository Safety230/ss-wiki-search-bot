
from telegram.update import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import settings

updater = Updater(token=settings.BOT_TOKEN)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Assalomu alaykum! Wikipedia saytidan ma'lumotlarni qidiruvchi BOTga hush kelibsiz! "
        "Biror ma'lumot izlash uchun /search va undan so'ng so'rovingizni yozing. "
        "Misol uchun, /search O'zbekiston")


def search(update: Update, context: CallbackContext):
    args = context.args
    search_text = ' '.join(args)
    response = requests.get('https://uz.wikipedia.org/w/api.php', {
        'action': 'opensearch',
        'search':  search_text,
        'limit': 1,
        'namespace': 0,
        'format': 'json',
    })
    result = response.json()
    link = result[3]
    if link:
        update.message.reply_text("Sizning so'rovingiz bo'yicha ma'lumotlar: " + link[0])
    else:
        update.message.reply_text("Sizning so'rovingiz bo'yicha ma'lumotlar topilmadi!")

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))

updater.start_polling()
updater.idle()

