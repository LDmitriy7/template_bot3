from assets import config
from core import *

START = 'start'
CANCEL = 'cancel'
BROADCAST = 'broadcast'
LOGS = 'logs'
RESTART = 'restart'
TEST = 'test'

USER_COMMANDS = [
    # BotCommand(command=START, description='Запустить бота'),
    # BotCommand(command=CANCEL, description='Отменить'),
]

ADMIN_COMMANDS = USER_COMMANDS + [
    # BotCommand(BROADCAST, 'Рассылка'),
    # BotCommand(LOGS, 'Логи'),
    # BotCommand(RESTART, 'Перезагрузка'),
    BotCommand(TEST, 'Тест'),
]


def setup():
    set_my_commands(USER_COMMANDS)

    for user_id in config.admins.ids:
        with exc.suppress(exc.Error, user_id=user_id):
            set_my_commands(ADMIN_COMMANDS, scope=BotCommandScopeChat(user_id))
