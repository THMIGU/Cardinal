# ***********************************************
# *  Project     : Cardinal
# *  File        : utils/embeds.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Embed factory

from github import Github

from data import lang

from discord import Embed, ClientUser


def success_embed(message: str) -> Embed:
	embed = Embed(
		title=lang.get("success-title", message=message),
		color=0x32CD32,
	)

	return embed


def fail_embed(message: str) -> Embed:
	embed = Embed(
		title=lang.get("fail-title", message=message),
		color=0xE34234,
	)

	return embed


def about_embed(user: ClientUser) -> Embed:
	github = Github()
	repo = github.get_repo("THMIGU/Cardinal")
	commits = repo.get_commits().totalCount

	embed = Embed(
		title=lang.get("about-title"),
		description=lang.get(
			"about-desc",
			mention=user.mention,
			commits=commits,
		),
		color=0xc41e3a,
	)

	embed.set_thumbnail(url=user.avatar)
	embed.set_footer(text=lang.get("about-footer"))

	return embed


def shutdown_embed() -> Embed:
	embed = Embed(
		title=lang.get("shutdown-title"),
		color=0xc41e3a,
	)

	return embed
