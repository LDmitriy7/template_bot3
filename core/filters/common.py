from dataclasses import dataclass

from .base import Filter
from .. import utils
from ..models.new_objects import CallbackButton


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
            return button.button_id == self.value.button_id
        except (KeyError, AttributeError):
            return False
