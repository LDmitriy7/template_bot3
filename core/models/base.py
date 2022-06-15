from __future__ import annotations

import json
import typing
from dataclasses import asdict, dataclass, Field

import mongoengine as me

from .. import utils

__all__ = ['BaseModel', 'BaseDocument', 'SimpleTypes']

DocT = typing.TypeVar('DocT', bound='Document')
SimpleTypes = int | float | bool | str | list | dict


def get_field_types(field: Field) -> list:
    return utils.listify(getattr(field.type, '__args__', field.type))


def is_list_type(_type):
    return getattr(_type, '__origin__', None) == list


def prepare_dict(_dict: dict, cast_types: list) -> dict | BaseModel:
    for _type in cast_types:
        if issubclass(_type, BaseModel):
            return _type.from_dict(_dict)
    return _dict


def prepare_list(_list: list, cast_types: list) -> list[SimpleTypes] | list[BaseModel]:
    new_list = []

    for item in _list:
        if isinstance(item, dict):
            item = prepare_dict(item, cast_types)
        elif isinstance(item, list):
            for _type in cast_types:
                if is_list_type(_type):
                    cast_types = getattr(_type, '__args__', [])
                    item = prepare_list(item, cast_types)
                    break

        new_list.append(item)

    return new_list


def prepare_value(value: SimpleTypes, cast_types: list) -> SimpleTypes | BaseModel | list[BaseModel]:
    if isinstance(value, list):
        return prepare_list(value, cast_types)
    if isinstance(value, dict):
        return prepare_dict(value, cast_types)
    return value


@dataclass
class BaseModel:
    __aliases__ = {}

    @classmethod
    def from_dict(cls, _dict: dict):
        prepared_dict = {}

        for field in cls._get_fields():
            if field.name in _dict:
                key = field.name
            elif field.name in cls.__aliases__:
                key = cls.__aliases__[field.name]
            else:
                continue

            field_value = _dict[key]
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


class BaseDocument(me.Document):
    meta = {
        'abstract': True,
    }

    @classmethod
    def get_doc(cls: type[DocT], *args, **kwargs) -> DocT | None:
        return cls.objects(*args, **kwargs).first()

    @classmethod
    def get_docs(cls: type[DocT], *args, **kwargs) -> list[DocT]:
        return [d for d in cls.objects(*args, **kwargs)]

    def to_dict(self) -> dict:
        return json.loads(self.to_json())
