import logging

import dotenv
import mongoengine as me

from .bot import Bot
from .context import Context
from .utils import env

dotenv.load_dotenv()

me.connect(
    db=env.get('DB_NAME'),
    host=env.get('DB_HOST', 'localhost'),
)

bot = Bot()
context = Context()
logger = logging.getLogger()

context.token = env.get('BOT_TOKEN')

logging.basicConfig(
    level=env.get_int('LOG_LEVEL', 30),
    handlers=[
        logging.StreamHandler(),
    ]
)
