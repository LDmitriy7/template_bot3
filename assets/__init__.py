from . import api
from . import commands
from . import config
from . import loader
from . import texts
# from .models import documents
from .models import keyboards
from .models import models as model
from .models import states

# aliases
cmd = commands
cfg = config
txt = texts
kb = keyboards
st = states
# doc = documents

__all__ = [
    'api',
    'loader',
    'cmd', 'commands',
    'cfg', 'config',
    'txt', 'texts',
    # 'documents',
    'kb', 'keyboards',
    'model',
    'st', 'states',
]
