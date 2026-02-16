# ***********************************************
# *  Project     : Cardinal
# *  File        : utils/cogs.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Load cogs for commands and events

from typing import Callable, Coroutine, Any
import os


async def load(func: Callable[[str], Coroutine[Any, Any, None]]) -> None:
	for filename in os.listdir("commands"):
		if not filename.endswith(".py"):
			continue
		await func(f"commands.{filename[:-3]}")

	for filename in os.listdir("events"):
		if not filename.endswith(".py"):
			continue
		await func(f"events.{filename[:-3]}")
