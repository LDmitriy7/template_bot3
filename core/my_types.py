from __future__ import annotations

import hashlib
from dataclasses import dataclass

from . import api_types
from . import constants as c
from . import models

__all__ = [
    'MyType',
    'CallbackButton',
    'UrlButton',
    'Translations',
    'State',
]


class MyType:

    def to_dict(self) -> dict:
        pass


class CallbackButton:

    def __init__(self, text: str, button_id: str = None):
        self.text = text
        self.button_id = button_id or text
        self._vars = {}

    def __getitem__(self, item):
        return self._vars[item]

    def get(self, item: str, default=None):
        return self._vars.get(item, default)

    def __contains__(self, item: str):
        return item in self._vars

    def save(self) -> str:
        string = f'{self.text}|{self.button_id}|{self._vars}'
        doc_id = hashlib.md5(string.encode()).hexdigest()
        models.CallbackButton(_id=doc_id, text=self.text, button_id=self.button_id, vars=self._vars).save()
        return doc_id

    @classmethod
    def get_button(cls, doc_id: str) -> CallbackButton | None:
        doc = models.CallbackButton.get_doc(_id=doc_id)

        if not doc:
            return None

        button = CallbackButton(doc.text, doc.button_id)
        button._vars = doc.vars
        return button

    def __call__(self, **_vars: str | int | list | dict | set) -> api_types.InlineKeyboardButton:
        """Return InlineKeyboardButton(text=text.format(**args), callback_data=button_doc_id)"""
        new_button = CallbackButton(self.text, self.button_id)
        new_button._vars = _vars
        doc_id = new_button.save()

        return api_types.InlineKeyboardButton(
            text=new_button.text.format(**_vars),
            callback_data=doc_id,
        )


@dataclass
class Translations:
    default: str

    def _get_default(self):
        return getattr(self, c.DEFAULT)

    def get(self, lang: str = c.DEFAULT):
        if not lang:
            return self._get_default()
        return getattr(self, lang, self._get_default())


class UrlButton:

    def __init__(self, text: str, url: str):
        self.text = text
        self.url = url

    def __call__(self) -> api_types.InlineKeyboardButton:
        return api_types.InlineKeyboardButton(self.text, url=self.url)


class State:

    def __init__(self):
        self._value = None

    def __get__(self, instance, owner) -> str:
        return self._value

    def __set_name__(self, owner: type, name):
        self._value = f'{owner.__name__}.{name}'
