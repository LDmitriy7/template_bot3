from core import *


@on_message()
def _():
    print(ctx.message.caption_entities)
