from dataclasses import dataclass

from .base import Filter
from ..models.tg_objects import Update


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
