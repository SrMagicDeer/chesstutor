import telebot
import config
from telebot import types

bot = telebot.TeleBot('5348803276:AAH8610B53HBOTOuxM4IqTd62OjNyJlLBTA')


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

        mess = f'Отлично, рад слышать! Моя база данных задач обновляется каждый день, <b>ныняшняя версия: 0.1</b> ' \
               f'Задачи усложняются по ходу решения. Ты можешь пропустить задачу, вернуться к предыдущей или ' \
               f'вернуться в это меню и начать все заново. Чтобы ответить на задачу необходимо написать ответ в ' \
               f'формате "e2-e4" (пример) и просто отправить мне. Я скажу, если ты ответил правильно или допустил ' \
               f'ошибку. Приятного время препровождения! '
        bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup_menu)

    elif message.text == "Я все понял, давай к делу" or "Я отдохнул, готов решать":

        keyboard_1 = types.InlineKeyboardMarkup()
        callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
        keyboard_1.add(callback_button_1)

        task_1 = 'https://skr.sh/sFLDGEHa3XV?a'
        bot.send_photo(message.chat.id, task_1, 'Задача #1 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_tasks)


def answer_tasks(message):
    if message.text == "a2-a1":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Следующая')
        next_one.add(button_next)

        task_1_done = 'https://skr.sh/sFLdRFxiDgV'
        bot.send_photo(message.chat.id, task_1_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task2)

    elif message.text != "a2-a1":
        task_1 = 'https://skr.sh/sFLDGEHa3XV?a'
        bot.send_photo(message.chat.id, task_1,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_tasks)


def task2(message):
    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Следующая":
        task_2 = 'https://skr.sh/sFN16tp1Jth'
        bot.send_photo(message.chat.id, task_2, 'Задача #2 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_task_2)


def answer_task_2(message):
    if message.text == "h4-h8":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Следующая')
        next_one.add(button_next)

        task_2_done = 'https://skr.sh/sFNK9csE1A3'
        bot.send_photo(message.chat.id, task_2_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task3)

    elif message.text != "h4-h8":
        task_2 = 'https://skr.sh/sFN16tp1Jth'
        bot.send_photo(message.chat.id, task_2,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_task_2)


def task3(message):
    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Следующая":
        task_2 = 'https://skr.sh/sFNC0qJ3tpf'
        bot.send_photo(message.chat.id, task_2, 'Задача #3 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_task_3)


def answer_task_3(message):
    if message.text == "d4-e6":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Следующая')
        next_one.add(button_next)

        task_3_done = 'https://skr.sh/sFNgunnjrYI?a'
        bot.send_photo(message.chat.id, task_3_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task4)

    elif message.text != "d4-e6":
        task_3 = 'https://skr.sh/sFNC0qJ3tpf'
        bot.send_photo(message.chat.id, task_3,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_task_3)


def task4(message):
    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Следующая":
        task_4 = 'https://skr.sh/sFNp0vpnUg4'
        bot.send_photo(message.chat.id, task_4, 'Задача #4 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_task_4)


def answer_task_4(message):
    if message.text == "h7-f5":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Следующая')
        next_one.add(button_next)

        task_4_done = 'https://skr.sh/sFNcgKWIuP7'
        bot.send_photo(message.chat.id, task_4_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task5)

    elif message.text != "h7-f5":
        task_4 = 'https://skr.sh/sFNp0vpnUg4'
        bot.send_photo(message.chat.id, task_4,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_task_4)


def task5(message):
    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Следующая":
        task_5 = 'https://skr.sh/sFNpa2H723F'
        bot.send_photo(message.chat.id, task_5, 'Задача #5 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_task_5)


def answer_task_5(message):
    if message.text == "a3-d3":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Следующая')
        next_one.add(button_next)

        task_5_done = 'https://skr.sh/sFNozemjDhl'
        bot.send_photo(message.chat.id, task_5_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task6)

    elif message.text != "a3-d3":
        task_5 = 'https://skr.sh/sFNpa2H723F'
        bot.send_photo(message.chat.id, task_5,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_task_5)


def task6(message):
    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Следующая":
        task_6 = 'https://skr.sh/sFNqPzQ2D0k?a'
        bot.send_photo(message.chat.id, task_6, 'Задача #6 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_task_6)


def answer_task_6(message):
    if message.text == "e3-e1":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Следующая')
        next_one.add(button_next)

        task_6_done = 'https://skr.sh/sFNGjy2Wmpl'
        bot.send_photo(message.chat.id, task_6_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task7)

    elif message.text != "e3-e1":
        task_6 = 'https://skr.sh/sFNqPzQ2D0k?a'
        bot.send_photo(message.chat.id, task_6,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_task_6)


def task7(message):
    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Следующая":
        task_7 = 'https://skr.sh/sFN2srKczjs'
        bot.send_photo(message.chat.id, task_7, 'Задача #7 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_task_7)


def answer_task_7(message):
    if message.text == "b8-h2":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Следующая')
        next_one.add(button_next)

        task_7_done = 'https://skr.sh/sFNiLyUXJoU'
        bot.send_photo(message.chat.id, task_7_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task8)

    elif message.text != "b8-h2":
        task_7 = 'https://skr.sh/sFN2srKczjs'
        bot.send_photo(message.chat.id, task_7,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_task_7)


def task8(message):
    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Следующая":
        task_8 = 'https://skr.sh/sFNp3qeqc39'
        bot.send_photo(message.chat.id, task_8, 'Задача #8 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_task_8)


def answer_task_8(message):
    if message.text == "e5-e1":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Следующая')
        next_one.add(button_next)

        task_8_done = 'https://skr.sh/sFNg7Z5lCOn'
        bot.send_photo(message.chat.id, task_8_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task9)

    elif message.text != "e5-e1":
        task_8 = 'https://skr.sh/sFNp3qeqc39'
        bot.send_photo(message.chat.id, task_8,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_task_8)


def task9(message):
    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Следующая":
        task_9 = 'https://skr.sh/sFNWi3wIJ8z?a'
        bot.send_photo(message.chat.id, task_9, 'Задача #9 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_task_9)


def answer_task_9(message):
    if message.text == "b2-h8":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Следующая')
        next_one.add(button_next)

        task_9_done = 'https://skr.sh/sFNI5HpCcbu'
        bot.send_photo(message.chat.id, task_9_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task10)

    elif message.text != "b2-h8":
        task_9 = 'https://skr.sh/sFNWi3wIJ8z?a'
        bot.send_photo(message.chat.id, task_9,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_task_9)


def task10(message):
    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Следующая":
        task_10 = 'https://skr.sh/sFN1Me3OnLP'
        bot.send_photo(message.chat.id, task_10, 'Задача #10 | Напиши ответ в формате "e2-e4"', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_task_10)


def answer_task_10(message):
    if message.text == "f7-e6":

        next_one = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_next = types.KeyboardButton('Завершить')
        next_one.add(button_next)

        task_10_done = 'https://skr.sh/sFNH5B9dKri'
        bot.send_photo(message.chat.id, task_10_done, 'Отлично! Ты правильно решил задачу, переходи к следующей!',
                       reply_markup=next_one)
        bot.register_next_step_handler(message, task_complete)

    elif message.text != "f7-e6":
        task_10 = 'https://skr.sh/sFN1Me3OnLP'
        bot.send_photo(message.chat.id, task_10,
                       'Ты допустил ошибку или отправил ответ в неправильном формате. Попробуй еще раз.')
        bot.register_next_step_handler(message, answer_task_10)


def task_complete(message):

    keyboard_1 = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Вернуться в меню", callback_data="mainmenu")
    keyboard_1.add(callback_button_1)

    if message.text == "Завершить":
        bot.send_message(message.chat.id, 'Молодец! Ты решил все задачи на сегодня. Подожди, пока не обновиться база данных задач и возвращайся снова!:)', reply_markup=keyboard_1)
        bot.register_next_step_handler(message, answer_tasks)


@bot.callback_query_handler(func=lambda call: True)
def menu(callback):
    if callback.data == "mainmenu":
        markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_accept = types.KeyboardButton("Я отдохнул, готов решать")
        markup_menu.add(btn_accept)

        mess = f'<b>Ты вернулся в меню.</b> Моя база данных задач обновляется каждый день, <b>ныняшняя версия: 0.1</b> ' \
               f'Задачи усложняются по ходу решения. Ты можешь пропустить задачу, вернуться к предыдущей или ' \
               f'вернуться в это меню и начать все заново. Чтобы ответить на задачу необходимо написать ответ в ' \
               f'формате "e2-e4" (пример) и просто отправить мне. Я скажу, если ты ответил правильно или допустил ' \
               f'ошибку. Приятного время препровождения! '
        msg = bot.send_message(callback.message.chat.id, mess, parse_mode='html', reply_markup=markup_menu)
        bot.register_next_step_handler(msg, answer_tasks)
        bot.clear_step_handler_by_chat_id(chat_id=callback.message.chat.id)


bot.polling(none_stop=True)
