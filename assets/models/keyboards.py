from core import *


class PayOptions(InlineKeyboard):
    option = CallbackButton('{amount} RUB')

    def __init__(self):
        self.inline_keyboard = [
            [self.option(amount=a)] for a in [79, 149, 299, 499]
        ]
