import telegram

api_key = '1355479720:AAEDivIOsnAaE0y1H-kN10K1aVIWMvTBc2Q'

bot = telegram.Bot(token=api_key)

# chat_id = bot.get_updates()[-1].message.chat_id
chat_id = 20294994

bot.sendMessage(chat_id=chat_id, text='빵형, 안녕?')