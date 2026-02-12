# ***********************************************
# *  Project     : Cardinal
# *  File        : utils/embeds.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-11
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Embed factory

from github import Github

from discord import Embed, ClientUser


def success_embed(message: str) -> Embed:
	embed = Embed(
		title=f"✅ {message}",
		color=0x32CD32,
	)

	return embed


def fail_embed(message: str) -> Embed:
	embed = Embed(
		title=f"❌ {message}",
		color=0xE34234,
	)

	return embed


def about_embed(user: ClientUser) -> Embed:
	github = Github()
	repo = github.get_repo("THMIGU/Cardinal")
	commits = repo.get_commits().totalCount

	embed = Embed(
		title="About",
		description=f"{user.mention} is the official moderation\nand game bot of the Ess. Ress. Server!\n\n"
		f"[GitHub Repo](https://www.github.com/THMIGU/Cardinal) (**{commits}** total commits)",
		color=0xc41e3a,
	)

	embed.set_thumbnail(url=user.avatar)
	embed.set_footer(text="Created by THMIGU")

	return embed


def shutdown_embed(user: ClientUser) -> Embed:
	embed = Embed(
		title="Shutdown",
		description=f"Shutting down {user.mention}!",
		color=0xc41e3a,
	)

	return embed
