import time
from importlib import import_module
from pathlib import Path

from core.models.tg_methods import get_updates
from core.models.tg_objects import Update
from . import exceptions
from .bot import bot
from .context import ctx
from .loader import logger


def _check_handlers(update: Update):
    for handler in bot.handlers:
        for _filter in handler.filters:
            if not _filter.check(update):
                break
        else:
            result = handler.func()
            return result


def _check_pre_middlewares(update: Update):
    for handler in bot.pre_middlewares:
        for _filter in handler.filters:
            if not _filter.check(update):
                break
        else:
            handler.func()


def _check_post_middlewares(update: Update):
    for handler in bot.post_middlewares:
        for _filter in handler.filters:
            if not _filter.check(update):
                break
        else:
            handler.func()


def process_update(update: Update):
    ctx.update = update

    try:
        _check_pre_middlewares(update)
        result = _check_handlers(update)
        _check_post_middlewares(update)
        return result
    except exceptions.Cancel:
        pass
    except Exception as exc:
        logger.exception(exc)

    return None


def _process_updates(updates: list[Update]):
    for update in updates:
        process_update(update)


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
        except Exception as exc:
            logger.exception(exc)


def _import_all(package: str):
    dirname = package.replace('.', '/')
    for file in Path(dirname).glob('*.py'):
        if not file.stem.startswith('_'):
            import_module(f'.{file.stem}', package)


APP_MODULES = ['handlers', 'middlewares', 'tasks']


def _init_app():
    import app

    if hasattr(app, 'init'):
        app.init()
    else:
        for m_name in APP_MODULES:
            module = import_module(f'app.{m_name}')
            if hasattr(module, 'setup'):
                module.setup()
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
