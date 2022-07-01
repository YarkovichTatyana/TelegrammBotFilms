import random

import telebot
from  telebot import types

bot = telebot.TeleBot('5586371619:AAE3bivTGfHBOJAj6D5184zZgwTdkyjdnqw')

films = [" 1+1 (Неприкасаемые)", "Миссия невыполнима", "Достучаться до небес", "Карты, деньги, два ствола!",
         "Гарри Поттер и узник Азкабана", "Один дома", "Маска", "Большой куш", "День сурка", "Евротур",
         "Форсаж", " Адреналин", "Дом Франкенштейна", "Без лица", "Доктор Хаус", "Побег из Нью‑Йорка", "Ронин",
         "Люди в чёрном","Игра престолов", "Дневники вампира", "Сверхъестественное", "Теория большого взрыва",
         "Друзья","Остаться в живых","Как я встретил вашу маму", "Властелин колец 3: Возвращение Короля ",
         "Зеленая миля ","Пираты Карибского моря: Проклятие Черной жемчужины ", "Судья Дредд 3D", "Фантазм 2",
         "Звездные войны: Эпизод 5 - Империя наносит ответный удар", "Престиж"]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    greeting=['привет', 'хай', 'ку', 'здоров', 'здравствуйте', 'доброго дня суток', 'доброе утро', 'добрый вечер']
    if str(message.text).lower() in greeting:
        bot.send_message(message.chat.id, 'Приветствую')
        keyboard = types.InlineKeyboardMarkup()
        key_films = types.InlineKeyboardButton(text='Фильм', callback_data='film')
        keyboard.add(key_films)

        bot.send_message(message.from_user.id, text='Выбери свой фильм', reply_markup=keyboard)

    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Я тебе помогу, напиши Привет')
    else:
        bot.send_message(message.chat.id, 'Я не понимаю, напиши /help')

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "film":
        msg = random.randint(0,(len(films)))
        bot.send_message(call.message.chat.id, films[msg])
        print(films[msg])



bot.polling(none_stop=True, interval=0)


