from telegram.ext import Updater, MessageHandler, Filters
from emoji import emojize
from datetime import datetime
import random

updater = Updater(token='1355479720:AAEDivIOsnAaE0y1H-kN10K1aVIWMvTBc2Q')
dispatcher = updater.dispatcher
updater.start_polling()

def handler(bot, update):
  text = update.message.text
  chat_id = update.message.chat_id
  intWeekday = datetime.today().weekday()
  strWeekday = '일요일'

  if intWeekday == 0:
    strWeekday = '월요일'
  else:
    if intWeekday == 1:
      strWeekday = '화요일'
    else:
      if intWeekday == 2:
        strWeekday = '수요일'
      else:
        if intWeekday == 3:
          strWeekday = '목요일'
        else:
          if intWeekday == 4:
            strWeekday = '금요일'
          else:
            if intWeekday == 5:
              strWeekday = '토요일'
            else:
              strWeekday = '일요일'
    
  
  if '모해' in text:
    bot.send_message(chat_id=chat_id, text='오빠 생각 ㅎㅎ')
  elif '몇시' in text:
    bot.send_message(chat_id=chat_id, text= datetime.today().strftime("%Y/%m/%d %H:%M:%S"))
  elif '오늘 몇일이야?' in text:
    bot.send_message(chat_id=chat_id, text= str(datetime.today().day)+'일'   )
  elif '무슨요일?' in text:
    bot.send_message(chat_id=chat_id, text= strWeekday   )
  elif '아잉' in text:
    bot.send_message(chat_id=chat_id, text=emojize('아잉:heart_eyes:', use_aliases=True))
  elif '몇시에' in text:
    bot.send_message(chat_id=chat_id, text='7시에 보자')
  elif '로또' in text:
    bot.send_message(chat_id=chat_id, text=str(random.randrange(1,46))+','+str(random.randrange(1,46))+','+str(random.randrange(1,46))+','+str(random.randrange(1,46))+','+str(random.randrange(1,46))+','+str(random.randrange(1,46)))
  elif '사진' in text:
    bot.send_photo(chat_id=chat_id, photo=open('img/'+str(random.randrange(1,17))+'.jpg', 'rb'))
  else:
    bot.send_message(chat_id=chat_id, text='몰라')

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)