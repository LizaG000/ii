import telebot
bot = telebot.TeleBot("8391809243:AAGi-OMZxGl3PnAuMeIW-xDi0UntJEes-vM")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'HI')
    print(message)

bot.polling(non_stop=True)