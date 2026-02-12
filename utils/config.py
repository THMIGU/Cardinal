# ***********************************************
# *  Project     : Cardinal
# *  File        : utils/config.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-11
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Load config file, create if missing.

from typing import Any
from pathlib import Path
import yaml

PATH = Path("config.yml")


def load() -> dict[str, Any]:
	PATH.touch(exist_ok=True)
	with open(PATH, "r") as file:
		config = yaml.safe_load(file)

	if not config:
		print("Config file is empty!")

	return config
