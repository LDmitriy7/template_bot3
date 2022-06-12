from assets import *
from core import *


@before_command(cmd.START, state='*')
def _():
    ctx.state = None
    send_message(txt.main_menu, reply_markup=kb.MainMenu())
    raise exc.Cancel()
