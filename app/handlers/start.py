from assets import *
from core import *


@on_command(cmd.START, state='*')
def welcome():
    send_message('text1', reply_markup=kb.PayOptions())

    ctx['x-key'] = 123
    ctx.state = 'test'

    if ctx.user_id in cfg.admins.ids:
        cmd.setup()


@on_command(cmd.TEST, state='test')
def test():
    if 'x-key' in ctx:
        send_message(f'{ctx["x-key"] = }')

    send_message(f'{ctx.get("x-key") = }')
    send_message(f'{ctx.get("x-key2") = }')
    send_message(f'{"x-key2" in ctx = }')

    ctx.clear()
    ctx.state = None

    ctx['test'] = doc.Config().to_dict()
