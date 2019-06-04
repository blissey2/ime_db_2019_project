import sys
import ChatBotModel

def proc_rolling(bot, update):
    bot.sendMessage('데구르르..')
    sound = firecracker()
    bot.sendMessage(sound)
    bot.sendMessage('르르..')

def proc_study(bot, update):
    bot.sendMessage('공부를 해라!!!')
    print(update)

def proc_stop(bot, update):
    bot.sendMessage('봇이 잠듭니다.')
    bot.stop()

# def proc_start(bot, update):
#     bot.sendMessage('안녕하세요.')
#     bot.start()

def firecracker():
    return '팡팡!'

bot = ChatBotModel.HangangBot()
bot.add_handler('rolling', proc_rolling)
bot.add_handler('study', proc_study)
bot.add_handler('stop', proc_stop)
bot.send_location(chat_id: '', latitude: '', longitude: '')
# bot.add_handler('start', proc_start)
bot.start()