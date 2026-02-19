# ***********************************************
# *  Project     : Cardinal
# *  File        : events/on_error.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# On-error bot event

import sys
from traceback import format_exception

from data import logger

from discord.ext import commands


class OnError(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@commands.Cog.listener()
	async def on_error(self, _) -> None:
		error_type, value, traceback = sys.exc_info()

		formatted_exception = "".join(format_exception(error_type, value, traceback))
		formatted_exception = formatted_exception.split("\n")

		logger.log("error")

		for line in formatted_exception[:-1]:
			logger.log(f"<red>{line.replace("\n", "")}")


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(OnError(bot))
