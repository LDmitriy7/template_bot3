from __future__ import annotations

import json
import typing

import mongoengine as me

T = typing.TypeVar('T')


class Document(me.Document):
    meta = {
        'abstract': True,
    }

    @classmethod
    def get_doc(cls: type[T], *args, **kwargs) -> T | None:
        return cls.objects(*args, **kwargs).first()

    @classmethod
    def get_docs(cls: type[T], *args, **kwargs) -> list[T]:
        return [d for d in cls.objects(*args, **kwargs)]

    def to_dict(self) -> dict:
        return json.loads(self.to_json())


class CallbackButton(Document):
    _id: str = me.StringField(primary_key=True)
    text: str = me.StringField()
    button_id: str = me.StringField()
    vars: dict = me.DictField()

    meta = {
        'collection': f'CallbackButtons__'
    }


class UserKey(me.EmbeddedDocument):
    chat_id: int = me.IntField()
    user_id: int = me.IntField()


class Storage(Document):
    key: UserKey = me.EmbeddedDocumentField(UserKey, primary_key=True)
    state: str = me.StringField()
    data: dict = me.DictField()

    @classmethod
    def get(cls, chat_id: int, user_id: int) -> Storage:
        key = UserKey(chat_id=chat_id, user_id=user_id)
        return cls.get_doc(key=key) or Storage(key=key).save()

    meta = {
        'collection': f'Storage__'
    }
