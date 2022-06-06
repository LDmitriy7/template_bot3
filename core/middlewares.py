from . import filters
from .loader import bot

__all__ = [
    'before_message',
]


def before_message(
        user_id: int | list[int] = None,
        chat_type: str | list[str] = None,
        state: str = None,
):
    fs = [filters.Message()]

    if user_id:
        fs.append(filters.UserId(user_id))

    if chat_type:
        fs.append(filters.ChatType(chat_type))

    fs.append(filters.State(state))

    def _(func):
        bot.add_pre_middleware(func, fs)
        return func

    return _
