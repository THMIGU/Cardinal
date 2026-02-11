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
