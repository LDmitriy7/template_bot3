from core import *


class PayOptions(InlineKeyboardMarkup):
    option = CallbackButton('{amount} RUB', 'PayOptions.option')

    def __init__(self):
        super().__init__()

        for a in [79, 149, 299, 499]:
            self.add_row(self.option(amount=a))
