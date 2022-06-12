from . import filters
from .loader import bot

__all__ = [
    'before_message',
    'after_callback_query',
    'before_command',
]


def before_message(
        user_id: int | list[int] = None,
        chat_type: str | list[str] = None,
        state: str = None,
):
    fs = [
        filters.Message(),
        filters.State(state),
    ]

    if user_id:
        fs.append(filters.UserId(user_id))

    if chat_type:
        fs.append(filters.ChatType(chat_type))

    def _(func):
        bot.add_pre_middleware(func, fs)
        return func

    return _


def after_callback_query(
        user_id: int | list[int] = None,
        chat_type: str | list[str] = None,
        state: str = None,
):
    fs = [
        filters.CallbackQuery(),
        filters.State(state),
    ]

    if user_id:
        fs.append(filters.UserId(user_id))

    if chat_type:
        fs.append(filters.ChatType(chat_type))

    def _(func):
        bot.add_post_middleware(func, fs)
        return func

    return _


def before_command(
        value: str = None,
        user_id: int | list[int] = None,
        chat_type: str | list[str] = None,
        state: str = None,
):
    fs = [
        filters.Command(value),
        filters.State(state),
    ]

    if user_id:
        fs.append(filters.UserId(user_id))

    if chat_type:
        fs.append(filters.ChatType(chat_type))

    def _(func):
        bot.add_pre_middleware(func, fs)
        return func

    return _
