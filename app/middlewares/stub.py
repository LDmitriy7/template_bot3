from assets import *
from core import *


@before_message()
def stub():
    if cfg.ENABLE_STUB:
        send_message(t.stub)
        raise errors.Cancel()
