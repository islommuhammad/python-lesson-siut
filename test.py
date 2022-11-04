import telegram.ext
import os 

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PORT = int(os.environ.get('PORT', '8443'))


def start(update, context):
    update.message.reply_text('Hi!')

def echo(update, context):
    update.message.reply_text(update.message.text)


def main():

    TOKEN = '5604141585:AAFXID3BI7DdaHupDQQhzUF-GBuqe1KxK0U'
    APP_NAME = 'https://pythonsiut.herokuapp.com/'

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path = TOKEN, webhook_url=APP_NAME+ TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()