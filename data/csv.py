# ***********************************************
# *  Project     : Cardinal
# *  File        : data/csv.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Load CSV log file, create if missing.

from pathlib import Path

from data import logger
from utils import file

DEFAULT = Path("assets/log.csv")
PATH = Path("log.csv")


def load() -> Path:
	if file.copy(src=DEFAULT, dst=PATH):
		logger.log("csv-missing")
	return PATH
