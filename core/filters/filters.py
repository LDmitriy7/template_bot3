from dataclasses import dataclass

from .. import utils
from ..models.tg_objects import Update
from ..models.new_objects import CallbackButton


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
        from ..context import ctx

        return ctx.user_id in utils.listify(self.value)


@dataclass
class ChatType(Filter):
    value: str | list[str]

    def check(self, _):
        from ..context import ctx

        return ctx.chat_type in utils.listify(self.value)


@dataclass
class QueryData(Filter):
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
        from ..context import ctx

        return self.value == '*' or ctx.state == self.value


@dataclass
class Button(Filter):
    value: CallbackButton | list[str]

    def check(self, _):
        from ..context import ctx

        if isinstance(self.value, list):
            return ctx.text in self.value

        try:
            doc_id = ctx.query_data
            button = CallbackButton.get_button(doc_id)
            return button.text == self.value.text and button.button_id == self.value.button_id
        except (KeyError, AttributeError):
            return False
