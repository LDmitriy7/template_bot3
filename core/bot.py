import logging
from dataclasses import dataclass
from typing import Callable, Any

import requests

from . import constants as c
from . import utils, exceptions
from .filters import Filter

__all__ = ['bot']

Func = Callable[[], Any]

API_ENDPOINT = 'https://api.telegram.org/bot{token}/{method}'


@dataclass
class Handler:
    func: Func
    filters: list[Filter]


@dataclass
class Task:
    func: Func


def handle_options(exclusive=True, first=False, last=False, after_any=False):
    """
    By default,

    :param exclusive: handling will be finished if this handler was executed
    :param first: handler will be moved to `pre_handlers`
    :param last: handler will be moved to `post_handlers`
    :param after_any: handler will be moved to `post_any_handler`

    If `last=True`, handler will be moved to `post_handlers`,
    If `first=True`, handler will be moved to `pre_handlers`,


    last -> `post_handlers` group
    after_any -> `post_any_handlers` group
    """
    params = {k: v for k, v in locals().items()}

    def _(func):
        func.__handle_options__ = params
        return func

    return _


class Bot:
    def __init__(self):
        self.handlers: list[Handler] = []
        self.pre_middlewares: list[Handler] = []
        self.post_middlewares: list[Handler] = []

        self.pre_handlers: list[Handler] = []
        self.post_handlers: list[Handler] = []
        self.post_any_handlers: list[Handler] = []

        self.tasks: list[Task] = []
        self.session = requests.Session()

    def add_handler(self, func: Func, filters: list[Filter] = None):
        handler = Handler(func, filters or [])
        self.handlers.append(handler)

    def add_pre_middleware(self, func: Func, filters: list[Filter] = None):
        handler = Handler(func, filters or [])
        self.pre_middlewares.append(handler)

    def add_post_middleware(self, func: Func, filters: list[Filter] = None):
        handler = Handler(func, filters or [])
        self.post_middlewares.append(handler)

    def request(self, method: str, params: dict) -> dict | list | bool | str | int:
        from .context import ctx

        params = utils.clear_params(params)
        url = API_ENDPOINT.format(token=ctx.token, method=method)

        logging.debug(f'Request {method} with params: {params}')
        resp = self.session.post(url, json=params)
        result: dict = resp.json()

        if result[c.OK]:
            return result[c.RESULT]

        raise exceptions.Error(result[c.ERROR_CODE], result[c.DESCRIPTION])


bot = Bot()
