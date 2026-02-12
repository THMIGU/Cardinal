# ***********************************************
# *  Project     : Cardinal
# *  File        : cogs/admin.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-11
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Admin-only commands

import discord
from discord.ext import commands

from utils.embeds import shutdown_embed
from utils.shutdown import shutdown_safely


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
		shutdown_embed_ = shutdown_embed()
		await interaction.response.send_message(embed=shutdown_embed_)

		await shutdown_safely(self.bot)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(Admin(bot))
