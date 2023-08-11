# main.py
from telegram.ext import Updater
from handlers import command_handlers
from config import config

def main():
    updater = Updater(token=config.API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(command_handlers.start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
