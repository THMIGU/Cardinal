# ***********************************************
# *  Project     : Cardinal
# *  File        : data/config.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Load config file, create if missing.

from typing import Any
from pathlib import Path
import yaml

from data import logger
from utils import file

DEFAULT = Path("assets/config.yml")
PATH = Path("config.yml")


def load() -> dict[str, Any]:
	if file.copy(src=DEFAULT, dst=PATH):
		logger.log("config-missing")

	with open(PATH, "r", encoding="utf-8") as f:
		config = yaml.safe_load(f)

	if not config:
		logger.log("config-empty")

	return config
