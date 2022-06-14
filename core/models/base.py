from __future__ import annotations

import json
import typing
from dataclasses import asdict, dataclass, Field

import mongoengine as me

from .. import utils

__all__ = ['BaseModel', 'Document']

T = typing.TypeVar('T')
SimpleTypes = int | float | bool | str | list | dict


def get_field_types(f: Field) -> list:
    return utils.listify(getattr(f.type, '__args__', f.type))


def is_list_type(t):
    return getattr(t, '__origin__', None) == list


def prepare_dict(d: dict, cast_types: list) -> dict | BaseModel:
    for t in cast_types:
        if issubclass(t, BaseModel):
            return t.from_dict(d)
    return d


def prepare_list(li: list, cast_types: list) -> list[SimpleTypes] | list[BaseModel]:
    new_list = []

    for item in li:
        if isinstance(item, dict):
            item = prepare_dict(item, cast_types)
        elif isinstance(item, list):
            for t in cast_types:
                if is_list_type(t):
                    cast_types = getattr(t, '__args__', [])
                    item = prepare_list(item, cast_types)
                    break

        new_list.append(item)

    return new_list


def prepare_value(v: SimpleTypes, cast_types: list) -> SimpleTypes | BaseModel | list[BaseModel]:
    if isinstance(v, list):
        return prepare_list(v, cast_types)
    elif isinstance(v, dict):
        return prepare_dict(v, cast_types)
    return v


@dataclass
class BaseModel:
    __aliases__ = {}

    @classmethod
    def from_dict(cls, d: dict):
        prepared_dict = {}

        for field in cls._get_fields():
            if field.name in d:
                key = field.name
            elif field.name in cls.__aliases__:
                key = cls.__aliases__[field.name]
            else:
                continue

            field_value = d[key]
            field_types = get_field_types(field)
            prepared_dict[field.name] = prepare_value(field_value, field_types)

        # noinspection PyArgumentList
        return cls(**prepared_dict)

    def to_dict(self):
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})

    @classmethod
    def eval_fields_types(cls, _globals: dict):
        for field in cls._get_fields():
            if isinstance(field.type, str):
                field.type = eval(field.type, _globals)

    @classmethod
    def _get_fields(cls) -> list[Field]:
        fields_dict: dict = getattr(cls, '__dataclass_fields__')
        return list(fields_dict.values())


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
