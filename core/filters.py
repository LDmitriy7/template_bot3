from contextlib import suppress
from dataclasses import dataclass

from . import utils
from .api_types import Update
from .my_types import CallbackButton


@dataclass
class Filter:
    pass

    def check(self, update: Update) -> bool:
        return bool(update)


@dataclass
class Message(Filter):

    def check(self, update: Update):
        return bool(update.message)


@dataclass
class CallbackQuery(Filter):

    def check(self, update: Update):
        return bool(update.callback_query)


@dataclass
class Text(Filter):
    value: str | None

    def check(self, update: Update):
        if message := update.message:
            if self.value is None:
                return bool(message.text)
            return message.text == self.value

        return False


@dataclass
class Command(Filter):
    value: str | None

    def check(self, update: Update):
        if message := update.message:
            if self.value is None:
                return message.text.startswith('/')
            return message.text == f'/{self.value}'

        return False


@dataclass
class UserId(Filter):
    value: int | list[int]

    def check(self, _):
        from .loader import context

        return context.user_id in utils.listify(self.value)


@dataclass
class ChatType(Filter):
    value: str | list[str]

    def check(self, _):
        from loader import context

        return context.chat_type in utils.listify(self.value)


@dataclass
class Data(Filter):
    value: str | None

    def check(self, update: Update):
        if callback_query := update.callback_query:
            if self.value is None:
                return bool(callback_query.data)
            return callback_query.data == self.value

        return False


@dataclass
class State(Filter):
    value: str | None

    def check(self, _):
        from .loader import context

        return self.value == '*' or context.state == self.value


@dataclass
class Button(Filter):
    value: CallbackButton | list[str]

    def check(self, _):
        from .loader import context

        if isinstance(self.value, list):
            return context.text in self.value

        try:
            doc_id = context.data
            button = CallbackButton.get_button(doc_id)
            return button.text == self.value.text and button.button_id == self.value.button_id
        except (KeyError, AttributeError):
            return False
