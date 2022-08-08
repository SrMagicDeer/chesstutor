import telebot
from telebot import types

bot = telebot.TeleBot('5348803276:AAH8610B53HBOTOuxM4IqTd62OjNyJlLBTA')


# Текст примерный, сразу говорю, написан чисто для теста предложения вариантов ботом

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    markup.add(btn1)
    mess = f'Привет, <b>{message.from_user.first_name}</b>. Я твой наставник по шахматам в виде бота. Я буду давать тебе шахматные задачи, готов начать?'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


# Не работает нихуя, второе сообщение тупо не появляется после нажатия на кнопку "Да"

@bot.message_handler(content_types=['level'])
def level(message):
    if message.text == "Да":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Начинающий")
        btn3 = types.KeyboardButton("Продвинутый")
        btn4 = types.KeyboardButton("Мастер спорта")
        markup.add(btn2, btn3, btn4)
        mess = f'Тогда, для начала, выбери <b>уровень сложности</b>, который тебе подходит'
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

    elif message.text == "Начинающий":
        bot.send_message(message.chat.id, "Начинающий")

    elif message.text == "Продвинутый":
        bot.send.message(message.chat.id, "Продвинутый")

    elif message.text == "Мастер спорта":
        bot.send_message(message.chat.id, "Мастер спорта")


bot.polling(none_stop=True)
