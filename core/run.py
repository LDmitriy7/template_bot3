import time

from .api_methods import *
from .api_types import Update
from .loader import logger


def _process_update(update: Update):
    ctx.update = update

    try:
        for handler in bot.handlers:
            for f in handler.filters:
                if not f.check(update):
                    break
            else:
                result = handler.func()
                return result
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


def run(
        parse_mode: str = None,
        disable_web_page_preview: bool = None,
        disable_notification: bool = None,
        protect_content: bool = None,
        poll_interval: float = 0.0,
):
    import app

    app.init()

    logger.info('Starting up...')

    ctx.parse_mode = parse_mode
    ctx.disable_web_page_preview = disable_web_page_preview
    ctx.disable_notification = disable_notification
    ctx.protect_content = protect_content

    try:
        _start_polling(poll_interval)
    except KeyboardInterrupt:
        logger.info('Shutting down...')
