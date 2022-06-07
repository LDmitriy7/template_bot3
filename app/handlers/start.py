from assets import *
from core import *


@on_command(cmd.START, state='*')
def welcome():
    send_message(t.welcome)
    send_message(t.ask_amount, reply_markup=kb.PayOptions())
