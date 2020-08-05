from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  # import modules
import os

my_token = '1355479720:AAEDivIOsnAaE0y1H-kN10K1aVIWMvTBc2Q'

print('start telegram chat bot')

dir_now = os.path.dirname(os.path.abspath(__file__))  # real path to dirname


# message reply function
def get_message(bot, update) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)


# help reply function
def help_command(bot, update) :
    update.message.reply_text("무엇을 도와드릴까요?")


# photo reply function
def get_photo(bot, update) :
    file_path = os.path.join(dir_now, 'from_telegram.png')
    photo_id = update.message.photo[-1].file_id  # photo 번호가 높을수록 화질이 좋음
    photo_file = bot.getFile(photo_id)
    photo_file.download(file_path)
    update.message.reply_text('photo saved')


updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler('help', help_command)
updater.dispatcher.add_handler(help_handler)

photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()