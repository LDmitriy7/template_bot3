""" https://core.telegram.org/bots/api#available-types (v 6.0) """

from __future__ import annotations

from dataclasses import dataclass, field

from .base import BaseModel

__all__ = [
    'TgObject',
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
]


class TgObject(BaseModel):
    """ Base class for all telegram objects """

    __aliases__ = {'from_user': 'from'}


# ==> Getting updates

@dataclass
class Update(TgObject):
    update_id: int
    message: Message = None
    edited_message: Message = None
    channel_post: Message = None
    edited_channel_post: Message = None
    inline_query: InlineQuery = None
    chosen_inline_result: ChosenInlineResult = None
    callback_query: CallbackQuery = None
    shipping_query: ShippingQuery = None
    pre_checkout_query: PreCheckoutQuery = None
    poll: Poll = None
    poll_answer: PollAnswer = None
    my_chat_member: ChatMemberUpdated = None
    chat_member: ChatMemberUpdated = None
    chat_join_request: ChatJoinRequest = None


@dataclass
class WebhookInfo(TgObject):
    url: str
    has_custom_certificate: bool
    pending_update_count: int
    ip_address: str = None
    last_error_date: int = None
    last_error_message: str = None
    last_synchronization_error_date: int = None
    max_connections: int = None
    allowed_updates: list[str] = None


# ==> Available types

@dataclass
class User(TgObject):
    id: int
    is_bot: bool
    first_name: str
    last_name: str = None
    username: str = None
    language_code: str = None
    can_join_groups: bool = None
    can_read_all_group_messages: bool = None
    supports_inline_queries: bool = None


@dataclass
class Chat(TgObject):
    id: int
    type: str
    title: str = None
    username: str = None
    first_name: str = None
    last_name: str = None
    photo: ChatPhoto = None
    bio: str = None
    has_private_forwards: bool = None
    description: str = None
    invite_link: str = None
    pinned_message: Message = None
    permissions: ChatPermissions = None
    slow_mode_delay: int = None
    message_auto_delete_time: int = None
    has_protected_content: bool = None
    sticker_set_name: str = None
    can_set_sticker_set: bool = None
    linked_chat_id: int = None
    location: ChatLocation = None


@dataclass
class Message(TgObject):
    message_id: int
    date: int
    chat: Chat
    from_user: User = None
    sender_chat: Chat = None
    forward_from: User = None
    forward_from_chat: Chat = None
    forward_from_message_id: int = None
    forward_signature: str = None
    forward_sender_name: str = None
    forward_date: int = None
    is_automatic_forward: bool = None
    reply_to_message: Message = None
    via_bot: User = None
    edit_date: int = None
    has_protected_content: bool = None
    media_group_id: str = None
    author_signature: str = None
    text: str = None
    entities: list[MessageEntity] = None
    animation: Animation = None
    audio: Audio = None
    document: Document = None
    photo: list[PhotoSize] = None
    sticker: Sticker = None
    video: Video = None
    video_note: VideoNote = None
    voice: Voice = None
    caption: str = None
    caption_entities: list[MessageEntity] = None
    contact: Contact = None
    dice: Dice = None
    game: Game = None
    poll: Poll = None
    venue: Venue = None
    location: Location = None
    new_chat_members: list[User] = None
    left_chat_member: User = None
    new_chat_title: str = None
    new_chat_photo: list[PhotoSize] = None
    delete_chat_photo: bool = None
    group_chat_created: bool = None
    supergroup_chat_created: bool = None
    channel_chat_created: bool = None
    message_auto_delete_timer_changed: MessageAutoDeleteTimerChanged = None
    migrate_to_chat_id: int = None
    migrate_from_chat_id: int = None
    pinned_message: Message = None
    invoice: Invoice = None
    successful_payment: SuccessfulPayment = None
    connected_website: str = None
    passport_data: PassportData = None
    proximity_alert_triggered: ProximityAlertTriggered = None
    video_chat_scheduled: VideoChatScheduled = None
    video_chat_started: VideoChatStarted = None
    video_chat_ended: VideoChatEnded = None
    video_chat_participants_invited: VideoChatParticipantsInvited = None
    web_app_data: WebAppData = None
    reply_markup: InlineKeyboardMarkup = None


@dataclass
class MessageId(TgObject):
    message_id: int


@dataclass
class MessageEntity(TgObject):
    type: str
    offset: int
    length: int
    url: str = None
    user: User = None
    language: str = None


@dataclass
class PhotoSize(TgObject):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: int = None


@dataclass
class Animation(TgObject):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: PhotoSize = None
    file_name: str = None
    mime_type: str = None
    file_size: int = None


@dataclass
class Audio(TgObject):
    file_id: str
    file_unique_id: str
    duration: int
    performer: str = None
    title: str = None
    file_name: str = None
    mime_type: str = None
    file_size: int = None
    thumb: PhotoSize = None


@dataclass
class Document(TgObject):
    file_id: str
    file_unique_id: str
    thumb: PhotoSize = None
    file_name: str = None
    mime_type: str = None
    file_size: int = None


@dataclass
class Video(TgObject):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: PhotoSize = None
    file_name: str = None
    mime_type: str = None
    file_size: int = None


@dataclass
class VideoNote(TgObject):
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: PhotoSize = None
    file_size: int = None


@dataclass
class Voice(TgObject):
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: str = None
    file_size: int = None


@dataclass
class Contact(TgObject):
    phone_number: str
    first_name: str
    last_name: str = None
    user_id: int = None
    vcard: str = None


@dataclass
class Dice(TgObject):
    emoji: str
    value: int


@dataclass
class PollOption(TgObject):
    text: str
    voter_count: int


@dataclass
class PollAnswer(TgObject):
    poll_id: str
    user: User
    option_ids: list[int]


@dataclass
class Poll(TgObject):
    id: str
    question: str
    options: list[PollOption]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: int = None
    explanation: str = None
    explanation_entities: list[MessageEntity] = None
    open_period: int = None
    close_date: int = None


@dataclass
class Location(TgObject):
    longitude: float
    latitude: float
    horizontal_accuracy: float = None
    live_period: int = None
    heading: int = None
    proximity_alert_radius: int = None


@dataclass
class Venue(TgObject):
    location: Location
    title: str
    address: str
    foursquare_id: str = None
    foursquare_type: str = None
    google_place_id: str = None
    google_place_type: str = None


@dataclass
class WebAppData(TgObject):
    data: str
    button_text: str


@dataclass
class ProximityAlertTriggered(TgObject):
    traveler: User
    watcher: User
    distance: int


@dataclass
class MessageAutoDeleteTimerChanged(TgObject):
    message_auto_delete_time: int


@dataclass
class VideoChatScheduled(TgObject):
    start_date: int


@dataclass
class VideoChatStarted(TgObject):
    pass


@dataclass
class VideoChatEnded(TgObject):
    duration: int


@dataclass
class VideoChatParticipantsInvited(TgObject):
    users: list[User]


@dataclass
class UserProfilePhotos(TgObject):
    total_count: int
    photos: list[list[PhotoSize]]


@dataclass
class File(TgObject):
    file_id: str
    file_unique_id: str
    file_size: int = None
    file_path: str = None


@dataclass
class WebAppInfo(TgObject):
    url: str


@dataclass
class ReplyKeyboardMarkup(TgObject):
    keyboard: list[list[KeyboardButton]] = field(default_factory=list)
    resize_keyboard: bool = None
    one_time_keyboard: bool = None
    input_field_placeholder: str = None
    selective: bool = None

    def add_row(self, *buttons: str | KeyboardButton):
        buttons = [KeyboardButton(b) if isinstance(b, str) else b for b in buttons]
        self.keyboard.append(buttons)


@dataclass
class KeyboardButton(TgObject):
    text: str
    request_contact: bool = None
    request_location: bool = None
    request_poll: KeyboardButtonPollType = None
    web_app: WebAppInfo = None


@dataclass
class KeyboardButtonPollType(TgObject):
    type: str = None


@dataclass
class ReplyKeyboardRemove(TgObject):
    remove_keyboard: bool
    selective: bool = None


@dataclass
class InlineKeyboardMarkup(TgObject):
    inline_keyboard: list[list[InlineKeyboardButton]] = None

    def add_row(self, *buttons: InlineKeyboardButton):
        self.inline_keyboard = self.inline_keyboard or []
        self.inline_keyboard.append(list(buttons))


@dataclass
class InlineKeyboardButton(TgObject):
    text: str
    url: str = None
    callback_data: str = None
    web_app: WebAppInfo = None
    login_url: LoginUrl = None
    switch_inline_query: str = None
    switch_inline_query_current_chat: str = None
    callback_game: CallbackGame = None
    pay: bool = None


@dataclass
class LoginUrl(TgObject):
    url: str
    forward_text: str = None
    bot_username: str = None
    request_write_access: bool = None


@dataclass
class CallbackQuery(TgObject):
    id: str
    from_user: User
    chat_instance: str
    message: Message = None
    inline_message_id: str = None
    data: str = None
    game_short_name: str = None


@dataclass
class ForceReply(TgObject):
    force_reply: bool
    input_field_placeholder: str = None
    selective: bool = None


@dataclass
class ChatPhoto(TgObject):
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str


@dataclass
class ChatInviteLink(TgObject):
    invite_link: str
    creator: User
    creates_join_request: bool
    is_primary: bool
    is_revoked: bool
    name: str = None
    expire_date: int = None
    member_limit: int = None
    pending_join_request_count: int = None


@dataclass
class ChatAdministratorRights(TgObject):
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool = None
    can_edit_messages: bool = None
    can_pin_messages: bool = None


# abstract
class ChatMember(TgObject):
    status: str
    user: User


@dataclass
class ChatMemberOwner(ChatMember):
    user: User
    is_anonymous: bool
    custom_title: str = None
    status: str = 'creator'


@dataclass
class ChatMemberAdministrator(ChatMember):
    user: User
    can_be_edited: bool
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_video_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: bool = None
    can_edit_messages: bool = None
    can_pin_messages: bool = None
    custom_title: str = None
    status: str = 'administrator'


@dataclass
class ChatMemberMember(ChatMember):
    user: User
    status: str = 'member'


@dataclass
class ChatMemberRestricted(ChatMember):
    user: User
    is_member: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    until_date: int
    status: str = 'restricted'


@dataclass
class ChatMemberLeft(ChatMember):
    user: User
    status: str = 'left'


@dataclass
class ChatMemberBanned(ChatMember):
    user: User
    until_date: int
    status: str = 'kicked'


@dataclass
class ChatMemberUpdated(TgObject):
    chat: Chat
    from_user: User
    date: int
    old_chat_member: ChatMember
    new_chat_member: ChatMember
    invite_link: ChatInviteLink = None


@dataclass
class ChatJoinRequest(TgObject):
    chat: Chat
    from_user: User
    date: int
    bio: str = None
    invite_link: ChatInviteLink = None


@dataclass
class ChatPermissions(TgObject):
    can_send_messages: bool = None
    can_send_media_messages: bool = None
    can_send_polls: bool = None
    can_send_other_messages: bool = None
    can_add_web_page_previews: bool = None
    can_change_info: bool = None
    can_invite_users: bool = None
    can_pin_messages: bool = None


@dataclass
class ChatLocation(TgObject):
    location: Location
    address: str


@dataclass
class BotCommand(TgObject):
    command: str
    description: str


# abstract
class BotCommandScope(TgObject):
    type: str


@dataclass
class BotCommandScopeDefault(BotCommandScope):
    type: str = 'default'


@dataclass
class BotCommandScopeAllPrivateChats(BotCommandScope):
    type: str = 'all_private_chats'


@dataclass
class BotCommandScopeAllGroupChats(BotCommandScope):
    type: str = 'all_group_chats'


@dataclass
class BotCommandScopeAllChatAdministrators(BotCommandScope):
    type: str = 'all_chat_administrators'


@dataclass
class BotCommandScopeChat(BotCommandScope):
    chat_id: int | str
    type: str = 'chat'


@dataclass
class BotCommandScopeChatAdministrators(BotCommandScope):
    chat_id: int | str
    type: str = 'chat_administrators'


@dataclass
class BotCommandScopeChatMember(BotCommandScope):
    chat_id: int | str
    user_id: int
    type: str = 'chat_member'


@dataclass
class MenuButton(TgObject):
    pass


@dataclass
class MenuButtonCommands(MenuButton):
    type: str


@dataclass
class MenuButtonWebApp(MenuButton):
    type: str
    text: str
    web_app: WebAppInfo


@dataclass
class MenuButtonDefault(MenuButton):
    type: str


@dataclass
class ResponseParameters(TgObject):
    migrate_to_chat_id: int = None
    retry_after: int = None


@dataclass
class InputMedia(TgObject):
    pass


@dataclass
class InputMediaPhoto(InputMedia):
    type: str
    media: str
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None


@dataclass
class InputMediaVideo(InputMedia):
    type: str
    media: str
    thumb: InputFile | str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    width: int = None
    height: int = None
    duration: int = None
    supports_streaming: bool = None


@dataclass
class InputMediaAnimation(InputMedia):
    type: str
    media: str
    thumb: InputFile | str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    width: int = None
    height: int = None
    duration: int = None


@dataclass
class InputMediaAudio(InputMedia):
    type: str
    media: str
    thumb: InputFile | str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    duration: int = None
    performer: str = None
    title: str = None


@dataclass
class InputMediaDocument(InputMedia):
    type: str
    media: str
    thumb: InputFile | str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    disable_content_type_detection: bool = None


@dataclass
class InputFile(TgObject):  # TODO
    ...


# ==> Stickers

@dataclass
class Sticker(TgObject):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    is_animated: bool
    is_video: bool
    thumb: PhotoSize = None
    emoji: str = None
    set_name: str = None
    mask_position: MaskPosition = None
    file_size: int = None


@dataclass
class StickerSet(TgObject):
    name: str
    title: str
    is_animated: bool
    is_video: bool
    contains_masks: bool
    stickers: list[Sticker]
    thumb: PhotoSize = None


@dataclass
class MaskPosition(TgObject):
    point: str
    x_shift: float
    y_shift: float
    scale: float


# ==> Inline mode

@dataclass
class InlineQuery(TgObject):
    id: str
    from_user: User
    query: str
    offset: str
    chat_type: str = None
    location: Location = None


@dataclass
class InlineQueryResult(TgObject):
    pass


@dataclass
class InlineQueryResultArticle(InlineQueryResult):
    type: str
    id: str
    title: str
    input_message_content: InputMessageContent
    reply_markup: InlineKeyboardMarkup = None
    url: str = None
    hide_url: bool = None
    description: str = None
    thumb_url: str = None
    thumb_width: int = None
    thumb_height: int = None


@dataclass
class InlineQueryResultPhoto(InlineQueryResult):
    type: str
    id: str
    photo_url: str
    thumb_url: str
    photo_width: int = None
    photo_height: int = None
    title: str = None
    description: str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultGif(InlineQueryResult):
    type: str
    id: str
    gif_url: str
    thumb_url: str
    gif_width: int = None
    gif_height: int = None
    gif_duration: int = None
    thumb_mime_type: str = None
    title: str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultMpeg4Gif(InlineQueryResult):
    type: str
    id: str
    mpeg4_url: str
    thumb_url: str
    mpeg4_width: int = None
    mpeg4_height: int = None
    mpeg4_duration: int = None
    thumb_mime_type: str = None
    title: str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultVideo(InlineQueryResult):
    type: str
    id: str
    video_url: str
    mime_type: str
    thumb_url: str
    title: str
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    video_width: int = None
    video_height: int = None
    video_duration: int = None
    description: str = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultAudio(InlineQueryResult):
    type: str
    id: str
    audio_url: str
    title: str
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    performer: str = None
    audio_duration: int = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultVoice(InlineQueryResult):
    type: str
    id: str
    voice_url: str
    title: str
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    voice_duration: int = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultDocument(InlineQueryResult):
    type: str
    id: str
    title: str
    document_url: str
    mime_type: str
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    description: str = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None
    thumb_url: str = None
    thumb_width: int = None
    thumb_height: int = None


@dataclass
class InlineQueryResultLocation(InlineQueryResult):
    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    horizontal_accuracy: float = None
    live_period: int = None
    heading: int = None
    proximity_alert_radius: int = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None
    thumb_url: str = None
    thumb_width: int = None
    thumb_height: int = None


@dataclass
class InlineQueryResultVenue(InlineQueryResult):
    type: str
    id: str
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str = None
    foursquare_type: str = None
    google_place_id: str = None
    google_place_type: str = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None
    thumb_url: str = None
    thumb_width: int = None
    thumb_height: int = None


@dataclass
class InlineQueryResultContact(InlineQueryResult):
    type: str
    id: str
    phone_number: str
    first_name: str
    last_name: str = None
    vcard: str = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None
    thumb_url: str = None
    thumb_width: int = None
    thumb_height: int = None


@dataclass
class InlineQueryResultGame(InlineQueryResult):
    type: str
    id: str
    game_short_name: str
    reply_markup: InlineKeyboardMarkup = None


@dataclass
class InlineQueryResultCachedPhoto(InlineQueryResult):
    type: str
    id: str
    photo_file_id: str
    title: str = None
    description: str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultCachedGif(InlineQueryResult):
    type: str
    id: str
    gif_file_id: str
    title: str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultCachedMpeg4Gif(InlineQueryResult):
    type: str
    id: str
    mpeg4_file_id: str
    title: str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultCachedSticker(InlineQueryResult):
    type: str
    id: str
    sticker_file_id: str
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultCachedDocument(InlineQueryResult):
    type: str
    id: str
    title: str
    document_file_id: str
    description: str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultCachedVideo(InlineQueryResult):
    type: str
    id: str
    video_file_id: str
    title: str
    description: str = None
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultCachedVoice(InlineQueryResult):
    type: str
    id: str
    voice_file_id: str
    title: str
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InlineQueryResultCachedAudio(InlineQueryResult):
    type: str
    id: str
    audio_file_id: str
    caption: str = None
    parse_mode: str = None
    caption_entities: list[MessageEntity] = None
    reply_markup: InlineKeyboardMarkup = None
    input_message_content: InputMessageContent = None


@dataclass
class InputMessageContent(TgObject):
    pass


@dataclass
class InputTextMessageContent(InputMessageContent):
    message_text: str
    parse_mode: str = None
    entities: list[MessageEntity] = None
    disable_web_page_preview: bool = None


@dataclass
class InputLocationMessageContent(InputMessageContent):
    latitude: float
    longitude: float
    horizontal_accuracy: float = None
    live_period: int = None
    heading: int = None
    proximity_alert_radius: int = None


@dataclass
class InputVenueMessageContent(InputMessageContent):
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: str = None
    foursquare_InputMessageContent: str = None
    google_place_id: str = None
    google_place_InputMessageContent: str = None


@dataclass
class InputContactMessageContent(InputMessageContent):
    phone_number: str
    first_name: str
    last_name: str = None
    vcard: str = None


@dataclass
class InputInvoiceMessageContent(InputMessageContent):
    title: str
    description: str
    payload: str
    provider_token: str
    currency: str
    prices: list[LabeledPrice]
    max_tip_amount: int = None
    suggested_tip_amounts: list[int] = None
    provider_data: str = None
    photo_url: str = None
    photo_size: int = None
    photo_width: int = None
    photo_height: int = None
    need_name: bool = None
    need_phone_number: bool = None
    need_email: bool = None
    need_shipping_address: bool = None
    send_phone_number_to_provider: bool = None
    send_email_to_provider: bool = None
    is_flexible: bool = None


@dataclass
class ChosenInlineResult(TgObject):
    result_id: str
    from_user: User
    query: str
    location: Location = None
    inline_message_id: str = None


@dataclass
class SentWebAppMessage(TgObject):
    inline_message_id: str = None


# ==> Payments

@dataclass
class LabeledPrice(TgObject):
    label: str
    amount: int


@dataclass
class Invoice(TgObject):
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int


@dataclass
class ShippingAddress(TgObject):
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


@dataclass
class OrderInfo(TgObject):
    name: str = None
    phone_number: str = None
    email: str = None
    shipping_address: ShippingAddress = None


@dataclass
class ShippingOption(TgObject):
    id: str
    title: str
    prices: list[LabeledPrice]


@dataclass
class SuccessfulPayment(TgObject):
    currency: str
    total_amount: int
    invoice_payload: str
    telegram_payment_charge_id: str
    provider_payment_charge_id: str
    shipping_option_id: str = None
    order_info: OrderInfo = None


@dataclass
class ShippingQuery(TgObject):
    id: str
    from_user: User
    invoice_payload: str
    shipping_address: ShippingAddress


@dataclass
class PreCheckoutQuery(TgObject):
    id: str
    from_user: User
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: str = None
    order_info: OrderInfo = None


# ==> Telegram Passport

@dataclass
class PassportData(TgObject):
    data: list[EncryptedPassportElement]
    credentials: EncryptedCredentials


@dataclass
class PassportFile(TgObject):
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int


@dataclass
class EncryptedPassportElement(TgObject):
    type: str
    hash: str
    data: str = None
    phone_number: str = None
    email: str = None
    files: list[PassportFile] = None
    front_side: PassportFile = None
    reverse_side: PassportFile = None
    selfie: PassportFile = None
    translation: list[PassportFile] = None


@dataclass
class EncryptedCredentials(TgObject):
    data: str
    hash: str
    secret: str


@dataclass
class PassportElementError(TgObject):
    pass


@dataclass
class PassportElementErrorDataField(PassportElementError):
    source: str
    type: str
    field_name: str
    data_hash: str
    message: str


@dataclass
class PassportElementErrorFrontSide(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorReverseSide(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorSelfie(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorFile(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorFiles(PassportElementError):
    source: str
    type: str
    file_hashes: list[str]
    message: str


@dataclass
class PassportElementErrorTranslationFile(PassportElementError):
    source: str
    type: str
    file_hash: str
    message: str


@dataclass
class PassportElementErrorTranslationFiles(PassportElementError):
    source: str
    type: str
    file_hashes: list[str]
    message: str


@dataclass
class PassportElementErrorUnspecified(PassportElementError):
    source: str
    type: str
    element_hash: str
    message: str


# ==> Games

@dataclass
class Game(TgObject):
    title: str
    description: str
    photo: list[PhotoSize]
    text: str = None
    text_entities: list[MessageEntity] = None
    animation: Animation = None


@dataclass
class CallbackGame(TgObject):
    user_id: int
    score: int
    force: bool = None
    disable_edit_message: bool = None
    chat_id: int = None
    message_id: int = None
    inline_message_id: str = None


@dataclass
class GameHighScore(TgObject):
    position: int
    user: User
    score: int


# fix errors
for i in __all__:
    cls: type[TgObject] = globals()[i]
    cls.eval_fields_types(globals())
