from contextlib import contextmanager
from dataclasses import dataclass

from .loader import logger

__all__ = [
    'Error',
    'suppress',
]


@dataclass
class Error(Exception):
    error_code: int
    description: str


@dataclass
class Cancel(Exception):
    description: str = None


@contextmanager
def suppress(*exceptions, log: bool = True, **log_kwargs):
    try:
        yield
    except exceptions as e:
        if log:
            logger.exception(f'{e} | {log_kwargs}')
