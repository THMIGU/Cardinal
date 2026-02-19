# ***********************************************
# *  Project     : Cardinal
# *  File        : services/flush.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Flushes the logs every second

from data import logger

from discord.ext import tasks


@tasks.loop(seconds=1)
async def flush_logs() -> None:
	logger.flush(verbose=False)
