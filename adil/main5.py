# 7337205665:AAENC7Ta24lz6UiMCEMZSNU6WA5P3gxDmGc

import telebot
import random
from telebot import types
# import speech_recognition as sr
# from pydub import AudioSegment
# import os


API_TOKEN = '7337205665:AAENC7Ta24lz6UiMCEMZSNU6WA5P3gxDmGc'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

# обработка команды старт
@bot.message_handler(commands=['start'])
def send_welcom(message):
    # создание клавиатуры
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/rad')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Добро пожаловать! Это бот "tetris_adil13_bot" v0.1', reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    help_txt = (
        "<b>Доступные команды:</b>\n"
        "/start - Начать взаимодействие с ботом\n"
        "/rand - отправка случайной картинки\n"
        "/help - информация о доступных командах\n"
    )
    bot.reply_to(message, help_txt)


@bot.message_handler(commands=['rand'])
def rand_ing(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Кнопка 1', url="https://www.youtube.com/")
    markup.add(btn1)

    btn2 = types.InlineKeyboardButton('Кнопка 2', url="https://www.youtube.com/")
    btn3 = types.InlineKeyboardButton('Кнопка 3', url="https://www.youtube.com/")
    markup.row(btn2, btn3)

    try:
        random_index = random.randint(0,2)
        image_path = f"./img/image{random_index}.jpg"
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file, reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка {e}")


# @bot.message_handler(content_types=['voice'])
# def handle_voice(message):
#     try:
#         file_info = bot.get_file(message.voice.file_id)
#         downloaded_file = bot.download_file(file_info.file_path)

#         voice_ogg_path = "voice.ogg"
#         voice_wav_path = "voice.wav"

#         with open(voice_ogg_path, 'wb') as new_file:
#             new_file.write(downloaded_file)

#         audio = AudioSegment.from_ogg(voice_ogg_path)
#         audio.export(voice_wav_path, format="wav")

#         recognizer = sr.Recognizer()
#         with sr.Audiofile(voice_wav_path) as source:
#             audio_data = recognizer.record(source)
#             text = recognizer.recognize_google(audio_data, language="ru-Ru")
#             bot.reply_to(message, f"Вы сказали: {text}")



# обработка типов photo, video, sticker
@bot.message_handler(content_types=['photo', 'video', 'sticker'])
def reaction_message(message):
    choice = random.choice(['😃', '👋', '🤬', '🤔'])
    bot.reply_to(message, choice)




# обработка остальных сообщений
@bot.message_handler()
def handle_unknown_command(message):
    bot.reply_to(message, "<b>Научись писать!!!</b>")


bot.polling()



