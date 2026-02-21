# ***********************************************
# *  Project     : Cardinal
# *  File        : events/on_message_edit.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# On-message edit bot event

from datetime import datetime

from data import logger, config, csv

import discord
from discord.ext import commands


class OnMessageEdit(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@commands.Cog.listener()
	async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
		conf = config.load()

		if after.author.bot:
			return
		if (server_id := after.guild.id) != conf["server"]:
			return

		msg_id = after.id
		username = after.author.name
		user_id = after.author.id
		msg_before = before.content
		msg_after = after.content
		attachment_ids_before = ",".join(str(attachment.id) for attachment in before.attachments)
		attachment_ids_after = ",".join(str(attachment.id) for attachment in after.attachments)
		channel_id = after.channel.id

		logger.log(
			"edit-log",
			msg_id=msg_id,
			username=username,
			user_id=user_id,
			msg_before=f"{msg_before} {attachment_ids_before}".strip(),
			msg_after=f"{msg_after} {attachment_ids_after}".strip(),
			channel_id=channel_id,
			server_id=server_id,
		)

		csv_path = csv.load()

		with open(csv_path, "a", encoding="utf-8") as f:
			values = [
				str(datetime.now())[:-7].replace(" ", "-"),
				server_id,
				channel_id,
				msg_id,
				None,
				user_id,
				username,
				f"\"{msg_after}\"",
				f"\"{attachment_ids_after}\"",
			]
			f.write(",".join(map(str, values)) + "\n")


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(OnMessageEdit(bot))
