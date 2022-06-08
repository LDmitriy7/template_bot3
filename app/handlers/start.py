from assets import *
from core import *


@on_command(cmd.START, state='*')
def welcome():
    send_message(txt.welcome)
    send_message(txt.ask_amount, reply_markup=kb.PayOptions())
