import os
from typing import TypeVar

T = TypeVar('T')


def clear_params(params: dict) -> dict:
    from core.models.tg_objects import TgObject
    from core.models.new_objects import MyType

    def clear_obj(obj):
        if isinstance(obj, (TgObject, MyType)):
            return obj.to_dict()
        if isinstance(obj, list):
            return [clear_obj(i) for i in obj]
        if isinstance(obj, dict):
            return {k: clear_obj(v) for k, v in obj.items() if clear_obj(v) is not None}
        return obj

    return clear_obj(params)


def listify(obj: T) -> T | list[T]:
    if obj is None:
        return []
    if isinstance(obj, list):
        return obj
    if isinstance(obj, tuple):
        return list(obj)

    return [obj]


class Env:
    _env = os.environ

    def get(self, key: str, default: T = ...) -> str | T:
        """Return variable (str) or default [if specified]"""
        value = self._env.get(key, default)

        if value is ...:
            raise ValueError(f'You must set env ${key}')
        return value

    def get_bool(self, key: str, default: T = ...) -> bool | T:
        """Return variable (bool) or default [if specified]"""
        value = self.get(key, default)

        if value in ['True', 'true', '1']:
            return True
        elif value in ['False', 'false', '0']:
            return False
        elif value == default:
            return default
        raise ValueError(f'Can\'t cast env ${key} to bool')

    def get_int(self, key: str, default: T = ...) -> int | T:
        """Return variable (int) or default [if specified]"""
        value = self.get(key, default)

        try:
            return int(value)
        except:
            if value == default:
                return default

        raise ValueError(f'Can\'t cast env ${key} to int')

    def get_list(self, key: str, default: T = ..., sep: str = ',') -> list[str] | T:
        """Return variable (list of str) or default [if specified]"""
        value = self.get(key, default)

        try:
            return [i.strip() for i in value.strip(sep).split(sep)]
        except:
            if value == default:
                return default

        raise ValueError(f'Can\'t cast env ${key} to list')

    def get_int_list(self, key: str, default: T = ..., sep: str = ',') -> list[int] | T:
        """Return variable (list of int) or default [if specified]"""
        value = self.get(key, default)

        try:
            return [int(i.strip()) for i in value.strip(sep).split(sep)]
        except:
            if value == default:
                return default

        raise ValueError(f'Can\'t cast env ${key} to list of int')


env = Env()
