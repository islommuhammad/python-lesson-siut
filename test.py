import os 
import schedule
import time
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



PORT = int(os.environ.get('PORT', '8443'))


def start(update, context):
    update.message.reply_text('Hi!')

def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    #TOKEN = "5604141585:AAFXID3BI7DdaHupDQQhzUF-GBuqe1KxK0U"
    TOKEN = os.environ.get("TOKEN")

    now = datetime.now()
    strNow = now.strftime("%d/%m/%Y %H:%M:%S")
    updater = Updater(TOKEN, use_context=True)
    updater.bot.send_message(chat_id =-321996347,  text="Salom testing hozir "+strNow)
    dp = updater.dispatcher
    
    #dp.add_handler(CommandHandler("start", start))

    #dp.add_handler(MessageHandler(Filters.text, echo))

    # updater.start_webhook(listen="0.0.0.0", port=PORT, url_path = TOKEN, webhook_url=APP_NAME+ TOKEN)
    # updater.idle()
    # updater.start_polling()
    # updater.idle()
schedule.every(1).minutes.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    main()