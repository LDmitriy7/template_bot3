from typing import Any

from .new_objects import *
from .tg_objects import *
from ..bot import bot
from ..context import ctx

SimpleTypes = int | float | bool | str | list | dict


def _get_translation(t: Translations):
    return t.get(ctx.lang)


# TODO
def _prepare_request_params(params: dict[str, Any], **alternatives) -> dict[str, SimpleTypes]:
    new_params = {}

    for p, v in params.items():
        if v is None:
            v = alternatives.get(p)
        if isinstance(v, Translations):
            v = _get_translation(v)
        new_params[p] = v

    return new_params


def send_message(
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
    params = _prepare_request_params(
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
    params = _prepare_request_params(locals())

    result = bot.request('GetUpdates', params)
    return [Update.from_dict(i) for i in result]


def get_chat_member(
        chat_id: int | str = None,
        user_id: int = None,
) -> ChatMember:
    params = _prepare_request_params(
        locals(),
        chat_id=ctx.chat_id,
        user_id=ctx.user_id,
    )

    result: dict = bot.request('getChatMember', params)

    _Model: type[ChatMember] = {
        'creator': ChatMemberOwner,
        'administrator': ChatMemberAdministrator,
        'member': ChatMemberMember,
        'restricted': ChatMemberRestricted,
        'left': ChatMemberLeft,
        'kicked': ChatMemberBanned,
    }[result['status']]

    return _Model.from_dict(result)


def get_my_commands(
        scope: BotCommandScope = None,
        language_code: str = None
) -> list[BotCommand]:
    params = _prepare_request_params(locals())

    result: list = bot.request('getMyCommands', params)
    return [BotCommand.from_dict(i) for (i) in result]


def set_my_commands(
        commands: list[BotCommand],
        scope: BotCommandScope = None,
        language_code: str = None,
) -> bool:
    params = _prepare_request_params(locals())

    result: bool = bot.request('setMyCommands', params)
    return result


def answer_callback_query(
        text: str | Translations = None,
        callback_query_id: str = None,
        show_alert: bool = None,
        url: str = None,
        cache_time: int = None,
) -> bool:
    params = _prepare_request_params(
        locals(),
        callback_query_id=ctx.callback_query_id,
    )

    result: bool = bot.request('AnswerCallbackQuery', params)
    return result


def create_chat_invite_link(
        chat_id: int | str = None,
        name: str = None,
        expire_date: int = None,
        member_limit: int = None,
        creates_join_request: bool = None,
) -> ChatInviteLink:
    params = _prepare_request_params(
        locals(),
        chat_id=ctx.chat_id,
    )

    result: dict = bot.request('CreateChatInviteLink', params)
    return ChatInviteLink.from_dict(result)


def copy_message(
        chat_id: int | str = None,
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
    params = _prepare_request_params(
        locals(),
        chat_id=ctx.chat_id,
        from_chat_id=ctx.chat_id,
        message_id=ctx.message_id,
        parse_mode=ctx.parse_mode,
        disable_notification=ctx.disable_notification,
        protect_content=ctx.protect_content,
    )

    result = bot.request('CopyMessage', params)
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
    params = _prepare_request_params(
        locals(),
        chat_id=ctx.chat_id,
        parse_mode=ctx.parse_mode,
        disable_web_page_preview=ctx.disable_web_page_preview,
        message_id=ctx.message_id,
    )

    result = bot.request('EditMessageText', params)
    if result is True:
        return result
    return Message.from_dict(result)
