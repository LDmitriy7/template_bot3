from . import base
from . import documents
from .new_objects import *
from .tg_methods import *
from .tg_objects import *

__all__ = [
    # Scopes
    'documents',
    'base',

    # Telegram objects
    'Update',
    'WebhookInfo',
    'User',
    'Chat',
    'Message',
    'MessageId',
    'MessageEntity',
    'PhotoSize',
    'Animation',
    'Audio',
    'Document',
    'Video',
    'VideoNote',
    'Voice',
    'Contact',
    'Dice',
    'PollOption',
    'PollAnswer',
    'Poll',
    'Location',
    'Venue',
    'WebAppData',
    'ProximityAlertTriggered',
    'MessageAutoDeleteTimerChanged',
    'VideoChatScheduled',
    'VideoChatStarted',
    'VideoChatEnded',
    'VideoChatParticipantsInvited',
    'UserProfilePhotos',
    'File',
    'WebAppInfo',
    'ReplyKeyboardMarkup',
    'KeyboardButton',
    'KeyboardButtonPollType',
    'ReplyKeyboardRemove',
    'InlineKeyboardMarkup',
    'InlineKeyboardButton',
    'LoginUrl',
    'CallbackQuery',
    'ForceReply',
    'ChatPhoto',
    'ChatInviteLink',
    'ChatAdministratorRights',
    'ChatMember',
    'ChatMemberOwner',
    'ChatMemberAdministrator',
    'ChatMemberMember',
    'ChatMemberRestricted',
    'ChatMemberLeft',
    'ChatMemberBanned',
    'ChatMemberUpdated',
    'ChatJoinRequest',
    'ChatPermissions',
    'ChatLocation',
    'BotCommand',
    'BotCommandScope',
    'BotCommandScopeDefault',
    'BotCommandScopeAllPrivateChats',
    'BotCommandScopeAllGroupChats',
    'BotCommandScopeAllChatAdministrators',
    'BotCommandScopeChat',
    'BotCommandScopeChatAdministrators',
    'BotCommandScopeChatMember',
    'MenuButton',
    'MenuButtonCommands',
    'MenuButtonWebApp',
    'MenuButtonDefault',
    'ResponseParameters',
    'InputMedia',
    'InputMediaPhoto',
    'InputMediaVideo',
    'InputMediaAnimation',
    'InputMediaAudio',
    'InputMediaDocument',
    'InputFile',
    'Sticker',
    'StickerSet',
    'MaskPosition',
    'InlineQuery',
    'InlineQueryResult',
    'InlineQueryResultArticle',
    'InlineQueryResultPhoto',
    'InlineQueryResultGif',
    'InlineQueryResultMpeg4Gif',
    'InlineQueryResultVideo',
    'InlineQueryResultAudio',
    'InlineQueryResultVoice',
    'InlineQueryResultDocument',
    'InlineQueryResultLocation',
    'InlineQueryResultVenue',
    'InlineQueryResultContact',
    'InlineQueryResultGame',
    'InlineQueryResultCachedPhoto',
    'InlineQueryResultCachedGif',
    'InlineQueryResultCachedMpeg4Gif',
    'InlineQueryResultCachedSticker',
    'InlineQueryResultCachedDocument',
    'InlineQueryResultCachedVideo',
    'InlineQueryResultCachedVoice',
    'InlineQueryResultCachedAudio',
    'InputMessageContent',
    'InputTextMessageContent',
    'InputLocationMessageContent',
    'InputVenueMessageContent',
    'InputContactMessageContent',
    'InputInvoiceMessageContent',
    'ChosenInlineResult',
    'SentWebAppMessage',
    'LabeledPrice',
    'Invoice',
    'ShippingAddress',
    'OrderInfo',
    'ShippingOption',
    'SuccessfulPayment',
    'ShippingQuery',
    'PreCheckoutQuery',
    'PassportData',
    'PassportFile',
    'EncryptedPassportElement',
    'EncryptedCredentials',
    'PassportElementError',
    'PassportElementErrorDataField',
    'PassportElementErrorFrontSide',
    'PassportElementErrorReverseSide',
    'PassportElementErrorSelfie',
    'PassportElementErrorFile',
    'PassportElementErrorFiles',
    'PassportElementErrorTranslationFile',
    'PassportElementErrorTranslationFiles',
    'PassportElementErrorUnspecified',
    'Game',
    'CallbackGame',
    'GameHighScore',

    # New objects
    'NewObject',
    'CallbackButton',
    'UrlButton',
    'Translations',
    'State',
    'InlineKeyboard',
    'ReplyKeyboard',

    # Tg methods
    'send_message',
    'get_updates',
    'get_chat_member',
    'get_my_commands',
    'set_my_commands',
    'answer_callback_query',
    'create_chat_invite_link',
    'copy_message',
    'edit_message_text',
    'delete_message',
    'send_photo',
    'send_document',
]
