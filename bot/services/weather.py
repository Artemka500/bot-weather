import telebot
import requests

from bs4 import BeautifulSoup as BS
from bot.data import config
from bot.handlers import user_start


def get_weather_t_min(city):

    r = requests.get(f'https://sinoptik.ua/погода-{city}')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        try:
            t_min = el.select('.temperature .min')[0].text
            t_min = t_min.replace('мин.', '')
            return t_min
        except:
            pass


def get_weather_t_max(city):

    r = requests.get(f'https://sinoptik.ua/погода-{city}')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        try:
            t_max = el.select('.temperature .max')[0].text
            t_max = t_max.replace('макс.', '')
            return t_max
        except:
            pass


def get_weather_description(city):

    r = requests.get(f'https://sinoptik.ua/погода-{city}')
    html = BS(r.content, 'html.parser')

    for el in html.select('#content'):
        try:
            description = el.select('.wDescription .description')[0].text
            return description
        except:
            pass