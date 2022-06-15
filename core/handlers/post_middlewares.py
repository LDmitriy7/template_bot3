from core import filters
from core.bot import bot


def after_callback_query(
        value: str | None = None,
        user_id: int | list[int] = None,
        chat_type: str | list[str] = None,
        state: str = None,
):
    _filters  =[
        filters.QueryData(value),
        filters.State(state),
    ]

    if user_id:
        _filters.append(filters.UserId(user_id))

    if chat_type:
        _filters.append(filters.ChatType(chat_type))

    def _(func):
        bot.add_post_middleware(func, _filters)
        return func

    return _
