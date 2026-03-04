# ***********************************************
# *  Project     : Cardinal
# *  File        : cardinal.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# The third time I'm trying to make this bot...

import signal

from data import logger, config
from utils import cogs, shutdown

import discord
from discord.ext import commands


class Cardinal(commands.Bot):
	def __init__(self) -> None:
		super().__init__(
			command_prefix="!",
			intents=discord.Intents.all(),
		)

	async def setup_hook(self) -> None:
		await cogs.load(self.load_extension)


def main() -> None:
	logger.init()
	signal.signal(signal.SIGTERM, shutdown.handle_sigterm)

	conf = config.load()
	token = conf["token"]

	cardinal = Cardinal()
	cardinal.run(token, log_handler=None)

	logger.log("logged-out")


if __name__ == "__main__":
	main()
