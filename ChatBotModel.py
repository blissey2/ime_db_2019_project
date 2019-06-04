import telegram
from telegram.ext import Updater, CommandHandler

from sql_model import *

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = secrets['admin_id']
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class HangangBot(TelegramBot):
    def __init__(self):
        self.token = secrets['telegram_access_token']
        TelegramBot.__init__(self, '텔레그램', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('안녕하세요')
        self.updater.start_polling()
        self.updater.idle()