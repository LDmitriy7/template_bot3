from dataclasses import dataclass

from ..models.tg_objects import Update


@dataclass
class Filter:

    def check(self, update: Update) -> bool:
        raise NotImplementedError()
