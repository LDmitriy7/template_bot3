from assets import *

CONFIRMED = 'confirmed'
CONFIRM_MSG_ID = 'confirm_msg_id'
NEXT_UPDATE = 'next_update'


class ConfirmKb(InlineKeyboardMarkup):
    button = CallbackButton('Confirm', 'confirm__')

    def __init__(self):
        super().__init__()

        self.add_row(self.button())


def confirm():
    next_update = ctx.data.get(NEXT_UPDATE)

    if not next_update:
        return

    ctx.data[CONFIRMED] = True
    next_update = Update.from_dict(next_update)
    delete_message()

    update = ctx.update
    process_update(next_update)
    ctx.update = update


def confirm_required(func):
    if confirm not in [handler.func for handler in bot.handlers]:
        bot.add_handler(confirm, [filters.Button(ConfirmKb.button)])

    def deco():
        if not ctx.data.get(CONFIRMED):
            send_message('...', reply_markup=ConfirmKb())
            ctx.data[NEXT_UPDATE] = ctx.update.to_dict()
            return

        ctx.data[CONFIRMED] = None
        ctx.data[NEXT_UPDATE] = None

        return func()

    return deco


# ===

def handle_options(exclusive=True, first=False, last=False, after_any=False):
    params = {k: v for k, v in locals().items()}

    def _(func):
        func.__handle_options__ = params
        return func

    return _


@on_command('test')
@handle_options(exclusive=False, first=True, after_any=True)
def boom():
    send_message('boom!')


print(boom.__handle_options__)
