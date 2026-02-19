# ***********************************************
# *  Project     : Cardinal
# *  File        : data/info.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Load info about Cardinal

from typing import Any
from pathlib import Path
import yaml

PATH = Path("assets/info.yml")


def load() -> dict[str, Any]:
	with open(PATH, "r", encoding="utf-8") as f:
		info = yaml.safe_load(f)

	return info
