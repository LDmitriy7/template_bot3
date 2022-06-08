from assets import *
from core import *


@before_message()
def stub():
    if cfg.ENABLE_STUB:
        send_message(txt.stub)
        raise exc.Cancel()
