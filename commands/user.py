# ***********************************************
# *  Project     : Cardinal
# *  File        : commands/user.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# User-accessible commands

import discord
from discord.ext import commands

from utils import embeds


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


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(User(bot))
