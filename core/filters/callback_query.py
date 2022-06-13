from dataclasses import dataclass

from .base import Filter
from ..models.tg_objects import Update


@dataclass
class QueryData(Filter):
    value: str | None

    def check(self, update: Update):
        if callback_query := update.callback_query:
            if self.value is None:
                return bool(callback_query.data)
            return callback_query.data == self.value

        return False
