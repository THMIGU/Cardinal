# ***********************************************
# *  Project     : Cardinal
# *  File        : events/on_ready.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# On-ready bot event

from data import logger
from utils import redis_

from discord.ext import commands


class OnReady(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self) -> None:
		logger.log(
			"logged-in",
			user=self.bot.user,
			id=self.bot.user.id,
		)
		logger.log(
			"session-id",
			id=self.bot.ws.session_id,
		)

		await self.bot.tree.sync()

		await redis_.subscribe(self.bot)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(OnReady(bot))
