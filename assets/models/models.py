from __future__ import annotations

import typing
from dataclasses import dataclass

from core import ctx, BaseModel

T = typing.TypeVar('T', bound='MyModel')


class ModelProxy(typing.Generic[T]):
    def __init__(self, obj: T):
        self._obj = obj

    def __enter__(self) -> T:
        return self._obj

    def __exit__(self, exc_type, exc_value, trace):
        self._obj.save()


class MyModel(BaseModel):

    @classmethod
    def get(cls) -> MyModel:
        storage = ctx.storage
        model = storage.models.get(cls.__name__)
        if not model:
            return cls()
        return cls.from_dict(model)

    def save(self):
        storage = ctx.storage
        storage.models[self.__class__.__name__] = self.to_dict()
        storage.save()

    @classmethod
    def proxy(cls: type[T]) -> ModelProxy[T]:
        return ModelProxy(cls.get())


@dataclass
class Vacancy(MyModel):
    title: str = None
    work_experience: str = None
    salary: str = None
    schedule: str = None
    working_hours: str = None


@dataclass
class Institution(MyModel):
    type: str = None
    name: str = None
    address: str = None


@dataclass
class Ad(MyModel):
    regional_city: str = None
    city: str = None
    institution: Institution = None
    vacancies: list[Vacancy] = None
    extra_info: str = None
    contact_phone: str = None
    photo: str = None


@dataclass
class Order(MyModel):
    ad: Ad
    pin: bool
    duplicate: bool
    price: int
    created_from: str
    channel_id: int
    paid_up: bool
    approved: bool
    posts_dates: list[int]
    user_id: int
    date: int
