# ***********************************************
# *  Project     : Cardinal
# *  File        : commands/lunch.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Lunch command

from datetime import datetime, timedelta
from enum import Enum

from utils import nutrislice
from utils.nutrislice import MenuType
from data import lang

import discord
from discord.ext import commands
from discord import Embed


def menu_section(category: str, menu_items: list[str]) -> str:
	if len(menu_items) == 1:
		return lang.get(
			"menu-list-s",
			category=category,
			item_1=menu_items[0],
		)
	elif len(menu_items) == 2:
		return lang.get(
			"menu-list-m",
			category=category,
			item_1=menu_items[0],
			item_2=menu_items[1],
		)
	elif len(menu_items) > 2:
		return lang.get(
			"menu-list-l",
			category=category,
			item_1=menu_items[0],
			item_2=menu_items[1],
			remaining=len(menu_items) - 2,
		)
	else:
		return lang.get("no-item", category=category)


class MenuSelection(Enum):
	lunch = MenuType.SECONDARY_LUNCH
	breakfast = MenuType.BREAKFAST


class DaySelection(Enum):
	yesterday = -1
	today = 0
	tomorrow = 1


class Lunch(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@discord.app_commands.command(
		name="lunch",
		description="Look at the LHS lunch menu",
	)
	@discord.app_commands.describe(menu="Menu to display")
	@discord.app_commands.describe(day="Day to display")
	async def lunch(
		self,
		interaction: discord.Interaction,
		menu: MenuSelection = MenuSelection.lunch,
		day: DaySelection = DaySelection.today,
	) -> None:
		await interaction.response.defer()

		date = datetime.now() + timedelta(days=day.value)
		year = date.year
		month = date.month
		day = date.day

		lunch_data = nutrislice.get_lunch(
			menu=menu.value,
			year=year,
			month=month,
			day=day,
		)

		entree_items = [item["name"] for item in lunch_data["entree"]]
		beverage_items = [item["name"] for item in lunch_data["beverage"]]
		other_items = [item["name"] for item in lunch_data["other"]]

		entrees = menu_section("Entrees", entree_items)
		beverages = menu_section("Beverages", beverage_items)
		others = menu_section("Other", other_items)

		description = "\n".join([entrees, beverages, others])

		lunch_embed = Embed(
			title=lang.get("lunch-title", month=month, day=day),
			description=description,
			color=0xc41e3a,
		)
		lunch_embed.set_footer(text="Menu provided by Nutrislice")

		await interaction.followup.send(embed=lunch_embed)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(Lunch(bot))
