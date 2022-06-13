from dataclasses import dataclass

from .base import Filter
from ..models.tg_objects import Update


@dataclass
class Message(Filter):

    def check(self, update: Update):
        return bool(update.message)


@dataclass
class CallbackQuery(Filter):

    def check(self, update: Update):
        return bool(update.callback_query)
