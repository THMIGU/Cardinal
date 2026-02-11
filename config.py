from typing import Any
import yaml


def load() -> dict[str, Any]:
	with open("config.yml", "r") as file:
		config = yaml.safe_load(file)

	return config
