# ***********************************************
# *  Project     : Cardinal
# *  File        : tasks/flush_logs.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Flush logs every second

from data import logger

from discord.ext import commands, tasks


class FlushLogs(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot
		self.flush_logs.start()

	def cog_unload(self) -> None:
		self.flush_logs.cancel()

	@tasks.loop(seconds=1)
	async def flush_logs(self) -> None:
		logger.flush(verbose=False)

	@flush_logs.before_loop
	async def before_flush_logs(self) -> None:
		await self.bot.wait_until_ready()


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(FlushLogs(bot))
