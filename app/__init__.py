from . import handlers
from . import middlewares
from . import tasks


def setup():
    handlers.setup()
    middlewares.setup()
    tasks.setup()
