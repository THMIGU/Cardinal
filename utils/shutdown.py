# ***********************************************
# *  Project     : Cardinal
# *  File        : utils/shutdown.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Shutdown Cardinal safely

from services import redis_
from data import logger

from discord.ext import commands


async def shutdown_safely(bot: commands.Bot) -> None:
	logger.log("shutdown")

	await bot.close()

	redis_.publish("__shutdown__")
