# inspired by https://github.com/Ahsoka/clovis/blob/main/clovis/__main__.py

from . import config
from .bot import bot
from .logs import setUpLogger, set_pretty_formatter, logs_dir, PrettyFormatter

set_pretty_formatter('%(levelname)s | %(name)s: %(asctime)s - [%(funcName)s()] %(message)s')
for name in ['bot', 'automated', 'commands', 'utils']:
    setUpLogger(f'ucmbot.{name}', files=not config.testing)

with open('test-token.txt' if config.testing else 'token.txt') as file:
    bot.run(file.read())