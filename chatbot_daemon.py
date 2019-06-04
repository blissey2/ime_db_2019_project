import sys
import ChatBotModel

def proc_rolling(bot, update):
    gang.sendMessage('데구르르..')
    sound = firecracker()
    gang.sendMessage(sound)
    gang.sendMessage('르르..')

def proc_stop(bot, update):
    gang.sendMessage('치이 봇이 잠듭니다.')
    gang.stop()

def firecracker():
    return '팡팡!'

gang = ChatBotModel.HangangBot()
gang.add_handler('rolling', proc_rolling)
gang.add_handler('stop', proc_stop)
gang.start()