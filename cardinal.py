# ***********************************************
# *  Project     : Cardinal
# *  File        : cardinal.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-10
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# The third time I'm trying to make this bot...

import os

from utils import config

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
		for filename in os.listdir("./cogs"):
			if not filename.endswith(".py"):
				continue
			await self.load_extension(f"cogs.{filename[:-3]}")


cardinal = Cardinal()


@cardinal.event
async def on_ready() -> None:
	print(f"Logged in as {cardinal.user}")
	await cardinal.tree.sync()


def main() -> None:
	conf = config.load()
	if not conf:
		return

	token = conf["token"]
	cardinal.run(token)


if __name__ == "__main__":
	main()
