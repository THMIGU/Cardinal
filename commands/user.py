# ***********************************************
# *  Project     : Cardinal
# *  File        : commands/user.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# User-accessible commands

from datetime import datetime

from utils import embeds
from utils import nutrislice
from utils.nutrislice import MenuType

import discord
from discord.ext import commands
from discord import Embed


class User(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@discord.app_commands.command(
		name="about",
		description="Get information about Cardinal",
	)
	async def about(self, interaction: discord.Interaction) -> None:
		user = self.bot.user

		about_embed = embeds.about_embed(user)
		await interaction.response.send_message(embed=about_embed)

	@discord.app_commands.command(
		name="lunch",
		description="Look at the LHS lunch menu",
	)
	async def lunch(self, interaction: discord.Interaction) -> None:
		await interaction.response.defer()

		date = datetime.now()
		year = date.year
		month = date.month
		day = date.day

		lunch_data = nutrislice.get_lunch(menu=MenuType.SECONDARY_LUNCH, year=year, month=month, day=day)

		lunch_embed = Embed(
			description="\n".join(item["name"] for item in lunch_data["entree"]),
			color=0xc41e3a,
		)

		await interaction.followup.send(embed=lunch_embed)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(User(bot))
