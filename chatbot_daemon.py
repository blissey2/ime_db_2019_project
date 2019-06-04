import sys
import ChatBotModel

def proc_rolling(bot, update):
    gang.sendMessage('데구르르..')
    sound = firecracker()
    gang.sendMessage(sound)
    gang.sendMessage('르르..')

def proc_stop(bot, update):
    gang.sendMessage('종료합니다.')
    gang.stop()

def category_region(bot, update):
    gang.sendMessage(chat_id = chat_id, text='수상레저_GIGU004')
    map=folium.Map(location=['37.5191333','127.007916'],zoom_start=13)
    gang.sendMessage(chat_id, map)

def firecracker():
    return '팡팡!'

gang = ChatBotModel.HangangBot()
gang.add_handler('rolling', proc_rolling)
gang.add_handler('stop', proc_stop)
gang.start()
