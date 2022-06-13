import typing

from core import ctx

T = typing.TypeVar('T', bound='MyModel')


class ModelProxy(typing.Generic[T]):
    def __init__(self, obj: T):
        self._obj = obj

    def __enter__(self) -> T:
        return self._obj

    def __exit__(self, exc_type, exc_value, trace):
        return True


class MyModel:

    @classmethod
    def _from_dict(cls, d: dict):
        # noinspection PyArgumentList
        return cls(**d)

    @classmethod
    def _from_context(cls):
        obj: dict = ctx[cls.__name__]
        return cls._from_dict(obj)

    @classmethod
    def proxy(cls: type[T]) -> ModelProxy[T]:
        return ModelProxy(cls._from_context())


class Vacancy(MyModel):
    title: str = None
    work_experience: str = None
    salary: str = None
    schedule: str = None
    working_hours: str = None


class Institution(MyModel):
    type: str = None
    name: str = None
    address: str = None


class Ad(MyModel):
    regional_city: str
    city: str
    institution: Institution
    vacancies: list[Vacancy]
    extra_info: str
    contact_phone: str
    photo: str


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
