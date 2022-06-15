# from __future__ import annotations

import typing
from dataclasses import dataclass

import mongoengine as me

from core import ctx, BaseModel, BaseDocument

T = typing.TypeVar('T', bound='MyModel')


class ModelProxy(typing.Generic[T]):
    def __init__(self, obj: T):
        self._obj = obj

    def __enter__(self) -> T:
        return self._obj

    def __exit__(self, exc_type, exc_value, trace):
        self._obj.save()


class Collection(BaseDocument):
    user_id: int = me.IntField()
    model: str = me.StringField()
    obj: dict = me.DictField()

    meta = {
        'collection': 'Collections__',
    }


class Model(BaseModel):

    @classmethod
    def get(cls) -> 'Model':
        storage = ctx.storage
        model = storage.models.get(cls.__name__)
        if not model:
            return cls()
        return cls.from_dict(model)

    def save(self):
        storage = ctx.storage
        storage.models[self.__class__.__name__] = self.to_dict()
        storage.save()

    def save_to_collection(self):
        Collection(
            user_id=ctx.user_id,
            model=self.__class__.__name__,
            obj=self.to_dict(),
        ).save()

    @classmethod
    def get_collection(cls: type[T]) -> list[T]:
        docs = Collection.get_docs(user_id=ctx.user_id, model=cls.__name__)
        return [cls.from_dict(doc.obj) for doc in docs]

    @classmethod
    def proxy(cls: type[T]) -> ModelProxy[T]:
        return ModelProxy(cls.get())


@dataclass
class Vacancy(Model):
    title: str = None
    work_experience: str = None
    salary: str = None
    schedule: str = None
    working_hours: str = None


@dataclass
class Institution(Model):
    type: str = None
    name: str = None
    address: str = None


@dataclass
class Ad(Model):
    regional_city: str = None
    city: str = None
    institution: Institution = None
    vacancies: list[Vacancy] = None
    extra_info: str = None
    contact_phone: str = None
    photo: str = None


@dataclass
class Order(Model):
    ad: Ad = None
    pin: bool = None
    duplicate: bool = None
    price: int = None
    created_from: str = None
    channel_id: int = None
    paid_up: bool = None
    approved: bool = None
    posts_dates: list[int] = None
    user_id: int = None
    date: int = None
