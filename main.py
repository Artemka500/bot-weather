import telebot
import requests

from bs4 import BeautifulSoup as BS
from bot.data import config
from bot.handlers import user_start
from bot.services import weather
from bot.markups import inline_markups


bot = telebot.TeleBot(config.API_TOKEN_BOT)

city = ['Москва', 'Краснодар', 'Санкт-Петербург', 'Екатеринбург', 'Калининград', 'Ярославль', 'Питер', 'Владивосток', 'Сочи', 'Домодедово']


@bot.message_handler(commands=['start'])
def start(message):
    user_start.start_func(message, city)


@bot.message_handler(commands=['help'])
def start(message):
    user_start.help_func(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_function(call):
    if call.data:
        for get in city:
            if call.data == f'weather:{get}':
                t_min = weather.get_weather_t_min(get)
                t_max = weather.get_weather_t_max(get)
                description = weather.get_weather_description(get)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'⛅ <b>Вот что мне удалось найти по вашему запросу:</b>\n\n🌦 Погода в городе <b>{get}:</b>\n\n🥵 <b>Максимальная температура:</b> {t_max}\n🥶 <b>Минимальная температу:</b> {t_min}\n\n<i>🌘 {description}</i>', parse_mode='html', reply_markup=inline_markups.back())
        if call.data == 'weather:back':
            user_start.start_func_edit(call.message, city)
        if call.data == 'weather:end':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'⛅ Введите название нужного города:', parse_mode='html', reply_markup=inline_markups.back())
            bot.register_next_step_handler(call.message, input_city)
def input_city(message):
    city = message.text

    t_min = weather.get_weather_t_min(city)
    t_max = weather.get_weather_t_max(city)
    description = weather.get_weather_description(city)
    if t_min == None:
        bot.send_message(chat_id=message.chat.id, text=f'😔 <b>Данный город не найден\n\nПроверьте что ваш запрос:</b>\n<i>1. В именительном падеже\n2. Город реален</i>', parse_mode='html', reply_markup=inline_markups.back())
    else:
        bot.send_message(chat_id=message.chat.id, text=f'⛅ <b>Вот что мне удалось найти по вашему запросу:</b>\n\n🌦 Погода в городе <b>{city}:</b>\n\n🥵 <b>Максимальная температура:</b> {t_max}\n🥶 <b>Минимальная температу:</b> {t_min}\n\n<i>🌘 {description}</i>', parse_mode='html', reply_markup=inline_markups.back())


@bot.message_handler(content_types=['text', 'audio', 'photo', 'file'])
def handler(message):
    bot.send_message(message.chat.id, f'⛅ <b>Я вас не понимаю</b>\n\n<i>Напишите</i> <code>/help</code>', parse_mode='html', reply_markup=inline_markups.back())


if __name__ == '__main__':
    bot.polling(none_stop=True)