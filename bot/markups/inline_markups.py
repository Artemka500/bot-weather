from telebot import types
import random


def weather(city):
    smail = ['🌄', '🏡', '📬', '📨', '🌖', '🌦', '☃', '🍉', '🥩', '🍽', '⚽', '🥇', '🏛', '💻', '🌊']
    y = 0
    markup = types.InlineKeyboardMarkup(row_width=2)
    for citys in city:
        smails = random.choice(smail)
        y = y + 1
        if y == 1:
            button1 = types.InlineKeyboardButton(text=f'{citys}', callback_data=f'weather:{citys}')
        if y == 2:
            y = y + 1
            button2 = types.InlineKeyboardButton(text=f'{citys}', callback_data=f'weather:{citys}')
        if y == 3:
            y = 0
            markup.add(button1, button2)
    button_end = types.InlineKeyboardButton(text=f'🌦 Другой город', callback_data=f'weather:end')
    markup.add(button_end)
    return markup


def back():
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='⬅ Назад', callback_data=f'weather:back')
    markup.add(button)
    return markup