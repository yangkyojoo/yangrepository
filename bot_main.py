from telegram.ext import Updater, MessageHandler, Filters
from emoji import emojize
from datetime import datetime
import random
from selenium import webdriver
import time
import bot_start
import os


updater = Updater(token='1355479720:AAEDivIOsnAaE0y1H-kN10K1aVIWMvTBc2Q')
dispatcher = updater.dispatcher

botA = bot_start.BotChii()
botA.start()
updater.start_polling()

def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id

    
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
    elif '얼마야' in text:
        driver = webdriver.Chrome("./chromedriver")
        driver.get("https://finance.daum.net/quotes/A045300")
        
        for n in range(1, 20):
            time.sleep(1)
            stores = driver.find_elements_by_css_selector("span.numB")
            how = stores[0].find_element_by_css_selector("strong").text
            bot.send_message(chat_id=chat_id, text=str(how))
    elif '로또' in text:
        bot.send_message(chat_id=chat_id, text=str(random.randrange(1,46))+','+str(random.randrange(1,46))+','+str(random.randrange(1,46))+','+str(random.randrange(1,46))+','+str(random.randrange(1,46))+','+str(random.randrange(1,46)))
    elif '사진' in text:
        bot.send_photo(chat_id=chat_id, photo=open('img/'+str(random.randrange(1,17))+'.jpg', 'rb'))
    elif '잘자' in text:
        bot.send_message(chat_id=chat_id, text='다음에 뵙죠!!')
        os._exit(1)
    else:
        bot.send_message(chat_id=chat_id, text='몰라')





echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
