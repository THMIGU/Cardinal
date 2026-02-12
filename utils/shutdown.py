# ***********************************************
# *  Project     : Cardinal
# *  File        : cogs/shutdown.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-11
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Shutdown Cardinal safely

from discord.ext import commands


async def shutdown_safely(bot: commands.Bot) -> None:
	print("Shutting down!")

	await bot.close()
