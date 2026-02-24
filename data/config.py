# ***********************************************
# *  Project     : Cardinal
# *  File        : data/config.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Load config file, create if missing.

from typing import Any
from pathlib import Path
import yaml

from data import logger
from utils import shutdown

PATH = Path("config.yml")


def load() -> dict[str, Any]:
	if not PATH.exists():
		logger.log("config-missing")
		shutdown.shutdown_force(1)

	with open(PATH, "r", encoding="utf-8") as f:
		config = yaml.safe_load(f)

	if not config:
		logger.log("config-empty")
		shutdown.shutdown_force(1)

	return config
