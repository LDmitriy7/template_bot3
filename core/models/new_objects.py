from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

from . import documents as doc
from . import tg_objects
from .base import BaseModel
from .. import constants as c


class NewObject(BaseModel):
    pass


@dataclass
class CallbackButton:
    text: str
    button_id: str = None
    _vars = {}

    def __post_init__(self):
        self.button_id = self.button_id or self.text

    def __getitem__(self, item):
        return self._vars[item]

    def get(self, item: str, default=None):
        return self._vars.get(item, default)

    def __contains__(self, item: str):
        return item in self._vars

    def save(self) -> str:
        string = f'{self.text}|{self.button_id}|{self._vars}'
        doc_id = hashlib.md5(string.encode()).hexdigest()
        doc.CallbackButton(
            _id=doc_id,
            text=self.text,
            button_id=self.button_id,
            vars=self._vars
        ).save()
        return doc_id

    @classmethod
    def get_button(cls, doc_id: str) -> CallbackButton | None:
        _doc = doc.CallbackButton.get_doc(_id=doc_id)

        if not _doc:
            return None

        button = CallbackButton(_doc.text, _doc.button_id)
        button._vars = _doc.vars
        return button

    def __call__(self, **_vars: str | int | list | dict | set) -> tg_objects.InlineKeyboardButton:
        """Return InlineKeyboardButton(text=text.format(**args), callback_data=button_doc_id)"""
        new_button = CallbackButton(self.text, self.button_id)
        new_button._vars = _vars
        doc_id = new_button.save()

        return tg_objects.InlineKeyboardButton(
            text=new_button.text.format(**_vars),
            callback_data=doc_id,
        )


@dataclass
class Translations:
    """
    Inherit and add your languages:

    >>> @dataclass
    ... class Ts(Translations):
    ...     ru: str
    ...     ua: str

    >>> hi = Ts('Hi', ru='Привет', ua='Вітання')

    >>> assert hi.get() == 'Hi'
    >>> assert hi.get('ua') == 'Вітання'
    >>> assert hi.get('unknown') == 'Hi'
    """

    default: str

    def _get_default(self):
        return getattr(self, c.DEFAULT)

    def get(self, lang: str = c.DEFAULT) -> str:
        """ Return translation to `lang` or `default` """
        if not lang:
            return self._get_default()
        return getattr(self, lang, self._get_default())


class UrlButton:

    def __init__(self, text: str, url: str):
        self.text = text
        self.url = url

    def __call__(self) -> tg_objects.InlineKeyboardButton:
        return tg_objects.InlineKeyboardButton(self.text, url=self.url)


class State:

    def __init__(self):
        self._value = None

    def __get__(self, instance, owner) -> str:
        return self._value

    def __set_name__(self, owner: type, name):
        self._value = f'{owner.__name__}.{name}'


@dataclass
class InlineKeyboard(NewObject):
    keyboard: list[list[tg_objects.InlineKeyboardButton]] = field(default_factory=list)

    def add_row(self, *buttons: tg_objects.InlineKeyboardButton):
        self.keyboard.append(list(buttons))

    def __call__(self) -> tg_objects.InlineKeyboardMarkup:
        return tg_objects.InlineKeyboardMarkup(inline_keyboard=self.keyboard)


@dataclass
class ReplyKeyboard(NewObject):
    keyboard: list[list[tg_objects.KeyboardButton]] = field(default_factory=list)
    resize_keyboard: bool = True

    def add_row(self, *buttons: str | tg_objects.KeyboardButton):
        buttons = [tg_objects.KeyboardButton(b) if isinstance(b, str) else b for b in buttons]
        self.keyboard.append(buttons)

    def __call__(self) -> tg_objects.ReplyKeyboardMarkup:
        return tg_objects.ReplyKeyboardMarkup(keyboard=self.keyboard, resize_keyboard=self.resize_keyboard)
