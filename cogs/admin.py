# ***********************************************
# *  Project     : Cardinal
# *  File        : cogs/admin.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-10
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Admin-only commands (nothing rn)

import discord
from discord.ext import commands


class Admin(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@discord.app_commands.command(
		name="shutdown",
		description="Shutdown Cardinal",
	)
	@discord.app_commands.default_permissions(manage_messages=True)
	async def shutdown(self, interaction: discord.Interaction) -> None:
		await interaction.response.send_message("plaecholderfds :tanabata_tree:")


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(Admin(bot))
