import telebot
bot = telebot.TeleBot("8391809243:AAGi-OMZxGl3PnAuMeIW-xDi0UntJEes-vM")

@bot.message_handler(command=['start'])
def main(message):
    bot.send_message(message.chat.id)