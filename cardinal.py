# ***********************************************
# *  Project     : Cardinal
# *  File        : cardinal.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# The third time I'm trying to make this bot...

import os

import discord
from discord.ext import commands

import config
from data import logger
from services import redis_, flush

intents = discord.Intents.all()


class Cardinal(commands.Bot):
	def __init__(self) -> None:
		super().__init__(
			command_prefix="!",
			intents=intents,
		)

	async def setup_hook(self) -> None:
		for filename in os.listdir("./cogs"):
			if not filename.endswith(".py"):
				continue
			await self.load_extension(f"cogs.{filename[:-3]}")


cardinal = Cardinal()


@cardinal.event
async def on_ready() -> None:
	flush.flush_logs.start()

	logger.log(
		"logged-in",
		user=cardinal.user,
		id=cardinal.user.id,
	)
	logger.log(
		"session-id",
		id=cardinal.ws.session_id,
	)

	await cardinal.tree.sync()

	await redis_.subscribe(cardinal)


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
