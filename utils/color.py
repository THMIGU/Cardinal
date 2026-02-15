# ***********************************************
# *  Project     : Cardinal
# *  File        : utils/color.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Formats string to have color escape codes

from colorama import Fore


def deserialize(msg: str) -> str:
	for color_name in dir(Fore):
		if not color_name.startswith("_") and color_name != "RESET":
			tag = f"<{color_name.lower().replace("light", "l").replace("_ex", "")}>"
			msg = msg.replace(tag, getattr(Fore, color_name))
	return msg.replace("<bold>", "\033[1m").replace("<reset>", "\033[0m")
