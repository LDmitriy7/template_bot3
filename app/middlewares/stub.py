import config
import texts
from core import *


@before_message()
def stub():
    if config.ENABLE_STUB:
        send_message(texts.stub)
        raise errors.Cancel()
