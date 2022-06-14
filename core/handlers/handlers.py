from .. import filters
from ..bot import bot
from ..models.new_objects import *

__all__ = [
    'on_text',
    'on_command',
    'on_callback_query',
    'on_message',
    'on_button',
]


def on_text(
        value: str = None,
        user_id: int | list[int] = None,
        chat_type: str | list[str] = None,
        state: str = None,
):
    fs = [
        filters.Text(value),
        filters.State(state),
    ]

    if user_id:
        fs.append(filters.UserId(user_id))

    if chat_type:
        fs.append(filters.ChatType(chat_type))

    def _(func):
        bot.add_handler(func, fs)
        return func

    return _


def on_command(
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
        bot.add_handler(func, fs)
        return func

    return _


def on_callback_query(
        value: str = None,
        user_id: int | list[int] = None,
        chat_type: str | list[str] = None,
        state: str = None,
):
    fs = [
        filters.QueryData(value),
        filters.State(state),
    ]

    if user_id:
        fs.append(filters.UserId(user_id))

    if chat_type:
        fs.append(filters.ChatType(chat_type))

    def _(func):
        bot.add_handler(func, fs)
        return func

    return _


def on_message(
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
        bot.add_handler(func, fs)
        return func

    return _


def on_button(
        value: CallbackButton | list[str],
        user_id: int | list[int] = None,
        chat_type: str | list[str] = None,
        state: str = None,
):
    fs = [
        filters.Button(value),
        filters.State(state),
    ]

    if user_id:
        fs.append(filters.UserId(user_id))

    if chat_type:
        fs.append(filters.ChatType(chat_type))

    def _(func):
        bot.add_handler(func, fs)
        return func

    return _
