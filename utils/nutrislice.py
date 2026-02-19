# ***********************************************
# *  Project     : Cardinal
# *  File        : utils/nutrislice.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Nutrislice API abstract for lunch menu

from enum import Enum
import requests

URL = (
	"https://lvjusdchildnutrition.api.nutrislice.com/menu/api/weeks/"
	"school/livermore-high-school/menu-type/{}/?format=json"
)


class MenuType(Enum):
	BREAKFAST = "breakfast"
	SECONDARY_LUNCH = "secondary-lunch"


def get_lunch(*, menu: MenuType, year: int, month: int, day: int) -> dict[str, list[dict[str, str | None]]]:
	menu_data = f"{menu.value}/{year}/{month}/{day}"
	api_url = URL.format(menu_data)

	response = requests.get(api_url)
	response.raise_for_status()
	data = response.json()

	menu_items = []
	for date in data["days"]:
		if not date["date"] == f"{year}-{month:02}-{day:02}":
			continue

		menu_items = date["menu_items"]

	lunch = {
		"entree": [],
		"beverage": [],
		"other": [],
	}
	for item in menu_items:
		if not item["food"]:
			continue

		details = item["food"]
		category = details["food_category"]

		food = {
			"name": details["name"],
			"image_url": details["image_url"]
		}

		match category:
			case "entree":
				lunch["entree"].append(food)
			case "beverage":
				lunch["beverage"].append(food)
			case _:
				lunch["other"].append(food)

	return lunch
