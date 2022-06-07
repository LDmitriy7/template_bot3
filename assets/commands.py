from assets import config
from core import *

START = 'start'
CANCEL = 'cancel'
BROADCAST = 'broadcast'
LOGS = 'logs'
RESTART = 'restart'

USER_COMMANDS = [
    # BotCommand(command=START, description='Запустить бота'),
    # BotCommand(command=CANCEL, description='Отменить'),
]

ADMIN_COMMANDS = USER_COMMANDS + [
    BotCommand(command=BROADCAST, description='Рассылка'),
    BotCommand(command=LOGS, description='Логи'),
    BotCommand(command=RESTART, description='Перезагрузка'),
]


def setup():
    set_my_commands(USER_COMMANDS)

    for user_id in config.admins.ids:
        with errors.suppress(errors.Error, user_id=user_id):
            set_my_commands(ADMIN_COMMANDS, scope=BotCommandScopeChat(chat_id=user_id))
