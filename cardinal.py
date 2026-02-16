# ***********************************************
# *  Project     : Cardinal
# *  File        : cardinal.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# The third time I'm trying to make this bot...

import config
from data import logger
from utils import cogs

import discord
from discord.ext import commands

intents = discord.Intents.all()


class Cardinal(commands.Bot):
	def __init__(self) -> None:
		super().__init__(
			command_prefix="!",
			intents=intents,
		)

	async def setup_hook(self) -> None:
		await cogs.load(self.load_extension)


cardinal = Cardinal()


def main() -> None:
	logger.init()

	conf = config.load()
	if not conf:
		return

	token = conf["token"]

	if token == "TOKEN":
		logger.log("supply-token")
		return

	cardinal.run(token, log_handler=None)

	logger.log("logged-out")


if __name__ == "__main__":
	main()
