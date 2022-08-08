import telebot
from telebot import types

bot = telebot.TeleBot('5348803276:AAH8610B53HBOTOuxM4IqTd62OjNyJlLBTA')

# По идее, первая кнопка (единственная), но выходят сразу все кнопки, что есть в коде
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Да")

markup.add(item1)

# Текст примерный, сразу говорю, написан чисто для теста предложения вариантов ботом

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>. Я твой наставник по шахматам в виде бота. Я буду давать тебе шахматные задачи, готов начать?'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
    


# Кнопки, которые должны выходить с сообщением выше, после того, как пользователь нажимает на "Да"
markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item2 = types.KeyboardButton("Мат в 1 ход")
item3 = types.KeyboardButton("Мат в 2 хода")
item4 = types.KeyboardButton("Мат в 3 хода")

markup.add(item2, item3, item4)


@bot.message_handler(content_types=['text'])
def да(message):
    if message.chat.type == 'private':
        if message.text == 'Да':
            bot.send_message(message.chat.id, 'Отлично, тогда, для начала, выбери подходящий уровень сложности', reply_markup=markup2, parse_mode='html')


@bot.message_handler(content_types=['text'])
def да(message):
    if message.chat.type == 'private':
        if message.text == 'Мат в 1 ход':
            bot.send_message(message.chat.id, '1', parse_mode='html')
        elif message.text == 'Мат в 2 хода':
            bot.send_message(message.chat.id, '2', parse_mode='html')
        elif message.text == 'Мат в 3 хода':
            bot.send_message(message.chat.id, '3', parse_mode='html')


bot.polling(none_stop=True)
