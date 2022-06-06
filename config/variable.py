from core import env

ENABLE_STUB = env.get_bool('ENABLE_STUB', False)


class Admins:

    @property
    def ids(self):
        return env.get_int_list('ADMINS_IDS', default=[])


admins = Admins()
