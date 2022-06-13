from assets import *
from core import *


@before_command(cmd.START, state='*')
def _():
    ctx.state = None
    msg = send_message(txt.main_menu, reply_markup=kb.MainMenu())
    print(msg.reply_markup.inline_keyboard[0][0])
    raise exc.Cancel()
