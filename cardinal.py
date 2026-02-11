import os

import config

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


if __name__ == "__main__":
	conf = config.load()
	token = conf["token"]

	cardinal.run(token)
