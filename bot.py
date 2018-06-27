import telebot
from telebot import types
import config
import translator as tr
import database as db

bot = telebot.TeleBot(config.telegram_token)

@bot.message_handler(commands=['start'])
def start_bot(message):
    if db.user_exist(message.chat.id):
        bot.send_message(message.chat.id, 'Ви вже розпочинали бесіду з цим ботом.\n'
                                          'Для перегляду списку усіх команд скористайтеся '
                                          'командою - /help.')
    else:
        user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                one_time_keyboard=True)
        sorted_langs = sorted(db.top_langs.items(), key=lambda kv: kv[1])
        for lang in sorted_langs:
            user_markup.row(lang[1])
        msg = bot.send_message(message.chat.id,
                         'Доброї пори доби! \nЦе бот-перекладач, який '
                         'побудований на Yandex-перекладачі та підтримує понад '
                         '90 мов світу. \nЗараз Вам '
                         'необхідно вказати мову на яку перекладатиметься текст. '
                         '\nЗмінити мову перекладу можна за допомогою команди '
                         '/langs (всі мови) та /top_langs (найпопулярніші мови). '
                         '\nМова вхідного тексту визначається автоматично. '
                         '\nСписок усіх команд Ви можете переглянути у меню команд, '
                         'що знаходиться біля клавіші відправки повідомлення.', reply_markup=user_markup)

        def add_user(msg):
            usr_lang = msg.text
            db.add_user(msg.chat.id, usr_lang)
            hide_markup = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Чудово!', reply_markup=hide_markup)


        bot.register_next_step_handler(msg, add_user)

@bot.message_handler(commands=['langs'])
def change_langs(message):
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
    sorted_langs = sorted(db.langs.items(), key=lambda kv: kv[1])
    for lang in sorted_langs:
        user_markup.row(lang[1])
    msg = bot.send_message(message.chat.id,
                           'Будь ласка, оберіть нову мову для перекладу:',
                           reply_markup=user_markup)
    def change(msg):
        usr_lang = msg.text
        db.change_langs(msg.chat.id, usr_lang)
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Мову успішно змінено!',
                         reply_markup=hide_markup)

    bot.register_next_step_handler(msg, change)

@bot.message_handler(commands=['top_langs'])
def change_langs(message):
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
    sorted_langs = sorted(db.top_langs.items(), key=lambda kv: kv[1])
    for lang in sorted_langs:
        user_markup.row(lang[1])
    msg = bot.send_message(message.chat.id,
                           'Будь ласка, оберіть нову мову для перекладу:',
                           reply_markup=user_markup)

    def change(msg):
        usr_lang = msg.text
        db.change_top_langs(msg.chat.id, usr_lang)
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Мову успішно змінено!',
                         reply_markup=hide_markup)

    bot.register_next_step_handler(msg, change)

@bot.message_handler(commands=['about'])
def about(message):
    bot.send_message(message.chat.id, 'Мене звати Остап. '
                                      '\nЯ - Junior Python Developer. '
                                      '\nTelegram - @Victoria1807 '
                                      '\nGitHub - https://github.com/Victoria1807 '
                                      '\nGmail - flamaster1807@gmail.com')

@bot.message_handler(content_types=['text'])
def translate_text(message):
    usr_lang = db.users_data[str(message.chat.id)]
    if len(message.text) >= 4050:
        bot.send_message(message.chat.id,
                         'Довжина тексту не повинна перевищувати 4050 символів.')
    else:
        try:
            transl_response = tr.translate(usr_lang, message.text)
            bot.send_message(message.chat.id, transl_response)
        except:
            bot.send_message(message.chat.id,
                             'Довжина тексту занадто велика.')

if __name__ == '__main__':
    bot.polling(none_stop=True)