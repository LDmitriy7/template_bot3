from assets import *
from core import *


@on_button(kb.PayOptions.option, state='*')
def _():
    answer_callback_query('😔 Платежная система еще не подключена')
