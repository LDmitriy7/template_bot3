from core import filters
from core.bot import bot

__all__ = [
    'after_callback_query',
]


def after_callback_query(
        value: str | None = None,
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
        bot.add_post_middleware(func, fs)
        return func

    return _