# ***********************************************
# *  Project     : Cardinal
# *  File        : commands/user.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# User-accessible commands

from utils import embeds

import discord
from discord.ext import commands


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
