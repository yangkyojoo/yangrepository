import sys
import ChatBotModel

def proc_rolling(bot, update):
    chii.sendMessage('데구르르..')
    sound = firecracker()
    chii.sendMessage(sound)
    chii.sendMessage('르르..')

def proc_stop(bot, update):
    chii.sendMessage('치이 봇이 잠듭니다.')
    chii.stop()

def proc_a(bot, update):
    chii.sendMessage('a로 시작하는 말은 apple')
    chii.sendMessage('다른 명령을 해주세요')

def firecracker():
    return '팡팡!'

chii = ChatBotModel.BotChii()
chii.add_handler('rolling', proc_rolling)
chii.add_handler('stop', proc_stop)
chii.add_handler('a', proc_a)
chii.start()