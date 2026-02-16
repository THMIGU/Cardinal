# ***********************************************
# *  Project     : Cardinal
# *  File        : data/lang.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Load language stuff

from typing import Any
from pathlib import Path
import yaml

from utils import color

PATH = Path("assets/lang.yml")


def load() -> dict[str, Any]:
	with open(PATH, "r", encoding="utf-8") as f:
		lang = yaml.safe_load(f)

	return lang


def get(key: str, **kwargs) -> str:
	lng = load()

	if key not in lng.keys():
		return key

	message = lng[key]
	message = message.format(**kwargs)
	message = color.deserialize(message)

	return message
