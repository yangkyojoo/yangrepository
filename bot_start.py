import telegram

class BotChii():
    def start(self):
        self.api_key = '1355479720:AAEDivIOsnAaE0y1H-kN10K1aVIWMvTBc2Q'
        bot = telegram.Bot(token=self.api_key)
        self.chat_id = 20294994
        bot.sendMessage(chat_id=self.chat_id, text='저 일어났어요...')