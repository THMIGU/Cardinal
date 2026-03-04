# ***********************************************
# *  Project     : Cardinal
# *  File        : utils/shutdown.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Shutdown Cardinal safely

import types

from utils import redis_
from data import logger

from discord.ext import commands


async def shutdown_safely(bot: commands.Bot) -> None:
	await bot.close()

	logger.log("shutdown")
	logger.flush()
	redis_.publish("__shutdown__")


def shutdown_force(exit_code: int = 0) -> None:
	logger.log("shutdown")
	logger.flush()
	redis_.publish("__shutdown__")

	exit(exit_code)


def handle_sigterm(*_) -> None:
	logger.log("sigterm")
	shutdown_force(0)
