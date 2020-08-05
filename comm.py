from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  # import modules

my_token = '1355479720:AAEDivIOsnAaE0y1H-kN10K1aVIWMvTBc2Q'

print('start telegram chat bot')


# message reply function
def get_message(bot, update) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)


# help reply function
def help_command(bot, update) :
    update.message.reply_text("무엇을 도와드릴까요?")


updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler('help', help_command)
updater.dispatcher.add_handler(help_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()