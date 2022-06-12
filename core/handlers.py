from . import filters
from .loader import bot
from .my_types import *


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


def on_data(
        value: str = None,
        user_id: int | list[int] = None,
        chat_type: str | list[str] = None,
        state: str = None,
):
    fs = [
        filters.Data(value),
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
