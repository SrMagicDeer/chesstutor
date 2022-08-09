import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_start = types.KeyboardButton("Погнали")
    markup.add(btn_start)

    mess = f'Привет, <b>{message.from_user.first_name}</b>. Я твой наставник по шахматам в виде бота. Я буду давать тебе шахматные задачи, готов начать?'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def tasks(message):
    if message.text == "Погнали":

        markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_accept = types.KeyboardButton("Я все понял, давай к делу")
        markup_menu.add(btn_accept)

        mess = f'Отлично, рад слышать! Моя база данных задач обновляется каждый день, <b>ныняшняя версия: 0.1</b> Задачи усложняются по ходу решения. Ты можешь пропустить задачу, вернуться к предыдущей, попросить подсказку или вернуться в это меню и начать все заново. Чтобы ответить на задачу необходимо написать ответ в формате "e2-e4" (пример) и просто отправить мне. Я скажу, если тыответил правильно или допустил ошибку. Приятного время препровождения!'
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup_menu)

    elif message.text == "Я все понял, давай к делу":

        keyboard_1 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Кнопка1", callback_data="knopka1")
        keyboard_1.add(callback_button_1)

        task_1 = 'https://skr.sh/sFLDGEHa3XV?a'
        bot.send_photo(message.chat.id, task_1, 'Задача #1', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, tasks)

    elif message.text == "a2-a1":
        task_1_done = 'https://skr.sh/sFLdRFxiDgV'
        bot.send_photo(message.chat.id, task_1_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!')

    else:
        task_1 = 'https://skr.sh/sFLDGEHa3XV?a'
        bot.send_photo(message.chat.id, task_1, 'Ты допустил ошибку, попробуй еще раз или пропусти задачу')


bot.polling(none_stop=True)
