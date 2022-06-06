import logging
import os

from core import env

DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'TemplateBot')

logging.info(f'{DB_HOST = }')


class Admins:

    @property
    def ids(self):
        return env.get_int_list('ADMINS_IDS', default=[])


admins = Admins()
