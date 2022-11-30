import telebot
from bot.data import config
from bot.markups import inline_markups

bot = telebot.TeleBot(config.API_TOKEN_BOT)


def start_func(message, city):
    bot.send_message(message.chat.id, f'🤗 <b>Приветствуем вас в нашем Боте</b>\n\n💼 <b>Данный Бот создан для портфолио</b>\n\n⛅ <i>Выберите город в котором вам надо показать погоду</i>',
                     parse_mode='html', reply_markup=inline_markups.weather(city=city))
def start_func_edit(message, city):
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=f'🤗 <b>Приветствуем вас в нашем Боте</b>\n\n💼 <b>Данный Бот создан для портфолио</b>\n\n⛅ <i>Выберите город в котором вам надо показать погоду</i>',
        parse_mode='html', reply_markup=inline_markups.weather(city=city))
def help_func(message):
    bot.send_message(chat_id=message.chat.id, text=f'⁉ <b>О Боте:</b>\n\n<code>/start</code> - <i>Стартовая команда Бота которая открывает меню с городами для определения погоды</i>\n<code>/help</code> - <i>Вспомогательное меню с оформацией о Боте</i>\n\n<b>Данный Бот является портфолиом пользователя GitHub <a href="https://github.com/Artemka500">@Artemka500</a></b>', parse_mode='html')