# ***********************************************
# *  Project     : Cardinal
# *  File        : tasks/fotm_check.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Check if it's the first of the month and send an annoying message

from datetime import datetime

import discord

from data import config

from discord.ext import commands, tasks


class FOTMCheck(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot
		self.fotm_check.start()

	def cog_unload(self) -> None:
		self.fotm_check.cancel()

	@tasks.loop(seconds=1)
	async def fotm_check(self) -> None:
		now = datetime.now().replace(microsecond=0)
		target = datetime(
			now.year,
			now.month,
			1, 8, 0, 0
		)

		if now != target:
			return

		conf = config.load()
		channel_id = conf["c-announcements"]
		channel = self.bot.get_channel(channel_id)

		with open("assets/fotm.gif", "rb") as f:
			file = discord.File(f, filename="fotm.gif")

		await channel.send("@everyone", file=file)

	@fotm_check.before_loop
	async def before_fotm_check(self) -> None:
		await self.bot.wait_until_ready()


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(FOTMCheck(bot))
