from typing import Any

from .new_objects import *
from .tg_objects import *
from ..bot import bot
from ..context import ctx


def _get_alt(value, default):
    """Get alternatives"""
    if value is None:
        return default
    return value


def _get_translation(t: Translations):
    return t.get(ctx.lang)


def send_message(
        text: str | Translations,
        chat_id: int | str = None,
        parse_mode: str = None,
        entities: list[MessageEntity] = None,
        disable_web_page_preview: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None,
) -> Message:
    if isinstance(text, Translations):
        text = _get_translation(text)

    chat_id = _get_alt(chat_id, ctx.chat_id)
    parse_mode = _get_alt(parse_mode, ctx.parse_mode)
    disable_web_page_preview = _get_alt(disable_web_page_preview, ctx.disable_web_page_preview)
    disable_notification = _get_alt(disable_notification, ctx.disable_notification)
    protect_content = _get_alt(protect_content, ctx.protect_content)

    result: dict = bot.request('sendMessage', locals())
    return Message.from_dict(result)


# ===

SimpleTypes = int | bool | str | list | dict


def prepare_request_params(params: dict[str, Any], **alternatives) -> dict[str, SimpleTypes]:
    return {'1': object}

    # if isinstance(text, Translation):
    #     text = _get_translation(text)


def get_translation(t: str | Translations) -> str:
    return ...


def _send_message(
        text: str | Translations,
        reply_markup: ReplyKeyboardMarkup | InlineKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None,

        chat_id: int | str = None,
        parse_mode: str = None,
        disable_web_page_preview: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,

        reply_to_message_id: int = None,
        entities: list[MessageEntity] = None,
        allow_sending_without_reply: bool = None,

) -> Message:
    params = prepare_request_params(
        locals(),
        chat_id=ctx.chat_id,
        parse_mode=ctx.parse_mode,
        disable_web_page_preview=ctx.disable_web_page_preview,
        disable_notification=ctx.disable_notification,
        protect_content=ctx.protect_content,
    )

    result: dict = bot.request('sendMessage', params)
    return Message.from_dict(result)


# ===

def get_updates(
        offset: int = None,
        limit: int = None,
        timeout: int = None,
        allowed_updates: list[str] = None
) -> list[Update]:
    result = bot.request('GetUpdates', locals())
    return [Update.from_dict(i) for i in result]


def get_chat_member(
        chat_id: int | str = None,
        user_id: int = None,
) -> ChatMember:
    chat_id = _get_alt(chat_id, ctx.chat_id)
    user_id = _get_alt(user_id, ctx.user_id)

    result: dict = bot.request('getChatMember', locals())

    def cast(chat_member: dict) -> ChatMember:
        _Type = {
            'creator': ChatMemberOwner,
            'administrator': ChatMemberAdministrator,
            'member': ChatMemberMember,
            'restricted': ChatMemberRestricted,
            'left': ChatMemberLeft,
            'kicked': ChatMemberBanned,
        }[chat_member['status']]
        return _Type.from_dict(chat_member)

    return cast(result)


def get_my_commands(
        scope: BotCommandScope = None,
        language_code: str = None
) -> list[BotCommand]:
    result: list = bot.request('getMyCommands', locals())
    return [BotCommand.from_dict(i) for (i) in result]


def set_my_commands(
        commands: list[BotCommand],
        scope: BotCommandScope = None,
        language_code: str = None,
) -> bool:
    result: bool = bot.request('setMyCommands', locals())
    return result


def answer_callback_query(
        text: str | Translations = None,
        callback_query_id: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
) -> bool:
    if isinstance(text, Translations):
        text = _get_translation(text)

    callback_query_id = _get_alt(callback_query_id, ctx.callback_query_id)

    result: bool = bot.request('AnswerCallbackQuery', locals())
    return result


def create_chat_invite_link(
        chat_id: int | str = None,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
) -> ChatInviteLink:
    chat_id = _get_alt(chat_id, ctx.chat_id)

    result: dict = bot.request('CreateChatInviteLink', locals())
    return ChatInviteLink.from_dict(result)


def copy_message(
        chat_id: int | str,
        from_chat_id: int | str = None,
        message_id: int = None,
        caption: str = None,
        parse_mode: str = None,
        caption_entities: list[MessageEntity] = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply = None,
) -> MessageId:
    from_chat_id = _get_alt(from_chat_id, ctx.chat_id)
    message_id = _get_alt(message_id, ctx.message_id)
    parse_mode = _get_alt(parse_mode, ctx.parse_mode)
    disable_notification = _get_alt(disable_notification, ctx.disable_notification)
    protect_content = _get_alt(protect_content, ctx.protect_content)

    result = bot.request('CopyMessage', locals())
    return MessageId.from_dict(result)


def edit_message_text(
        text: str | Translations,
        chat_id: int | str = None,
        message_id: int = None,
        inline_message_id: str = None,
        parse_mode: str = None,
        entities: list[MessageEntity] = None,
        disable_web_page_preview: bool = None,
        reply_markup: InlineKeyboardMarkup = None,
):
    if isinstance(text, Translations):
        text = _get_translation(text)

    chat_id = _get_alt(chat_id, ctx.chat_id)
    parse_mode = _get_alt(parse_mode, ctx.parse_mode)
    disable_web_page_preview = _get_alt(disable_web_page_preview, ctx.disable_web_page_preview)
    message_id = _get_alt(message_id, ctx.message_id)

    result = bot.request('EditMessageText', locals())
    if result is True:
        return result
    return Message.from_dict(result)
