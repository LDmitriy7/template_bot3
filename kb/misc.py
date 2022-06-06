from core import *


class Test(InlineKeyboardMarkup):
    GREETING = InlineKeyboardButton(text='Привет, я {user_name}', callback_data='test:say_hello:{user_name}')
    DEVELOPER_LINK = InlineKeyboardButton(text='Разработчик шаблона', url='https://t.me/Dmitriy7244')

    # def __init__(self, user_name: str):
    #     super().__init__(row_width=1)
    #
    #     self.add(
    #         self.GREETING.format(user_name=user_name),
    #         self.DEVELOPER_LINK,
    #     )
