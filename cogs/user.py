# ***********************************************
# *  Project     : Cardinal
# *  File        : cogs/user.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-10
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# User-accessible commands

from github import Github

import discord
from discord import Embed
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
		github = Github()
		repo = github.get_repo("THMIGU/Cardinal")
		commits = repo.get_commits().totalCount

		user = self.bot.user

		about_embed = Embed(
			title="About",
			description=f"{user.mention} is the official moderation\nand game bot of the Ess. Ress. Server!\n\n"
			f"[GitHub Repo](https://www.github.com/THMIGU/Cardinal) (**{commits}** total commits)",
			color=0xc41e3a,
		)

		about_embed.set_thumbnail(url=user.avatar)
		about_embed.set_footer(text="Created by THMIGU")

		await interaction.response.send_message(embed=about_embed)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(User(bot))
