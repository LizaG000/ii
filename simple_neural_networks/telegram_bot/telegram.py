import telebot
bot = telebot.TeleBot("8391809243:AAGi-OMZxGl3PnAuMeIW-xDi0UntJEes-vM")

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! 👋 Добро пожаловать в мебельный магазин <b>«Future»</b>.\nЗарегистрируйтесь — и мы сохраним ваши любимые товары и предложим персональные скидки!\nЧтобы зарегистрироваться введите \\registrate', parse_mode='html')

@bot.message_handler(commands=['registrate', 'регистрация'])
def main(message):
    bot.register_next_step_handler(message.chat.id, 'Введите ваше имя.')

bot.polling(non_stop=True)