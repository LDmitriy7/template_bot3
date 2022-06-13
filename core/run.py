import time
from importlib import import_module
from pathlib import Path

from . import exceptions
from core.models.tg_methods import *
from core.models.tg_objects import Update
from .loader import logger
from .context import ctx


def _check_handlers(update: Update):
    for handler in bot.handlers:
        for f in handler.filters:
            if not f.check(update):
                break
        else:
            result = handler.func()
            return result


def _check_pre_middlewares(update: Update):
    for handler in bot.pre_middlewares:
        for f in handler.filters:
            if not f.check(update):
                break
        else:
            handler.func()


def _check_post_middlewares(update: Update):
    for handler in bot.post_middlewares:
        for f in handler.filters:
            if not f.check(update):
                break
        else:
            handler.func()


def _process_update(update: Update):
    ctx.update = update

    try:
        _check_pre_middlewares(update)
        result = _check_handlers(update)
        _check_post_middlewares(update)
        return result
    except exceptions.Cancel:
        pass
    except Exception as e:
        logger.exception(e)


def _process_updates(updates: list[Update]):
    for update in updates:
        _process_update(update)


def _start_polling(poll_interval: float):
    offset = None

    while True:
        try:
            updates = get_updates(offset=offset)

            if updates:
                logger.info(updates)
                _process_updates(updates)
                offset = updates[-1].update_id + 1

            time.sleep(poll_interval)
        except Exception as e:
            logger.exception(e)


def _import_all(package: str):
    dirname = package.replace('.', '/')
    for f in Path(dirname).glob('*.py'):
        if not f.stem.startswith('_'):
            import_module(f'.{f.stem}', package)


APP_MODULES = ['handlers', 'middlewares', 'tasks']


def _init_app():
    import app

    if hasattr(app, 'init'):
        app.init()
    else:
        for m_name in APP_MODULES:
            m = import_module(f'app.{m_name}')
            if hasattr(m, 'setup'):
                m.setup()
            else:
                _import_all(f'app.{m_name}')


def run(
        parse_mode: str = None,
        disable_web_page_preview: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        poll_interval: float = 0.0,
):
    _init_app()

    logger.info('Starting up...')

    ctx.parse_mode = parse_mode
    ctx.disable_web_page_preview = disable_web_page_preview
    ctx.disable_notification = disable_notification
    ctx.protect_content = protect_content

    try:
        _start_polling(poll_interval)
    except KeyboardInterrupt:
        logger.info('Shutting down...')
