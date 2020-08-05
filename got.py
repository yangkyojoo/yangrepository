from telegram.ext import Updater, MessageHandler, Filters  # import modules

my_token = '1355479720:AAEDivIOsnAaE0y1H-kN10K1aVIWMvTBc2Q'

print('start telegram chat bot')

# message reply function
def get_message(bot, update) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)
    

updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()