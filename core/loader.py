import logging

import dotenv
import mongoengine as me

from .context import ctx
from .utils import env

dotenv.load_dotenv()

me.connect(
    db=env.get('DB_NAME'),
    host=env.get('DB_HOST', 'localhost'),
)

logger = logging.getLogger()

ctx.token = env.get('BOT_TOKEN')

logging.basicConfig(
    level=env.get_int('LOG_LEVEL', 30),
    handlers=[
        logging.StreamHandler(),
    ]
)
