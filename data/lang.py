# ***********************************************
# *  Project     : Cardinal
# *  File        : data/lang.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Load language stuff

from typing import Any
from pathlib import Path
import yaml

from utils import color, shutdown

PATH = Path("assets/lang.yml")


def load() -> dict[str, Any]:
	if not PATH.exists():
		print("Lang file not found!")
		shutdown.shutdown_force(1)

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
