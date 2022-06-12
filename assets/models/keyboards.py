from itertools import chain

from core import *
from .. import config as cfg


class MainMenu(InlineKeyboardMarkup):
    create_ad = CallbackButton('📝 Создать объявление')
    my_ads = CallbackButton('📁 Мои объявления')
    tech_support = UrlButton('👨‍💻 Техподдержка', 'https://t.me/LFeedbackBot')
    our_site = UrlButton('🌐 Наш сайт', 'https://horeca-job.com.ua/')
    change_lang = CallbackButton('{flag} Сменить язык')

    def __init__(self):
        super().__init__()

        self.add_row(self.create_ad(), self.my_ads())
        self.add_row(self.tech_support(), self.our_site())

        flag = {c.RU: '🇷🇺', c.UA: '🇺🇦'}.get(ctx.lang, '🇷🇺')
        self.add_row(self.change_lang(flag=flag))


class RegionalCities(ReplyKeyboardMarkup):
    buttons = list(cfg.CITIES.keys())

    def __init__(self):
        super().__init__(resize_keyboard=True)

        self.add_row(*self.buttons)


class Cities(ReplyKeyboardMarkup):
    buttons = list(chain(*cfg.CITIES.values()))

    def __init__(self, regional_city: str):
        super().__init__(resize_keyboard=True)

        self.add_row(*cfg.CITIES[regional_city])
