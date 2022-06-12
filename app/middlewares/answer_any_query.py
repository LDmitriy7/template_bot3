from core import *


@after_callback_query(state='*')
def answer_any_query():
    answer_callback_query()
