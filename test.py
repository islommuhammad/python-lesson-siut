import os 
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PORT = int(os.environ.get('PORT', '8443'))
now = datetime.now()
strNow = now.strftime("%d/%m/%Y %H:%M:%S")

def start(update, context):
    update.message.reply_text('Hi!')

def echo(update, context):
    update.message.reply_text(update.message.text)


def main():

    TOKEN = os.environ.get("TOKEN")

    updater = Updater(TOKEN, use_context=True)
    updater.bot.send_message(chat_id =-321996347,  text="Salom testing hozir "+strNow)
    dp = updater.dispatcher
    
    #dp.add_handler(CommandHandler("start", start))

    #dp.add_handler(MessageHandler(Filters.text, echo))

    # updater.start_webhook(listen="0.0.0.0", port=PORT, url_path = TOKEN, webhook_url=APP_NAME+ TOKEN)
    # updater.idle()
    # updater.start_polling()
    # updater.idle()

if __name__ == '__main__':
    main()