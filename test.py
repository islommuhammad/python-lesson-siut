import os 

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PORT = int(os.environ.get('PORT', '8443'))


def start(update, context):
    update.message.reply_text('Hi!')

def echo(update, context):
    update.message.reply_text(update.message.text)


def main():

    TOKEN = os.environ.get("TOKEN")
    APP_NAME = 'https://pythonsiut.herokuapp.com/'

    updater = Updater(TOKEN, use_context=True)
    updater.bot.send_message(chat_id =-321996347,  text="Salom testing")
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text, echo))

    # updater.start_webhook(listen="0.0.0.0", port=PORT, url_path = TOKEN, webhook_url=APP_NAME+ TOKEN)
    # updater.idle()
    # updater.start_polling()
    # updater.idle()

if __name__ == '__main__':
    main()