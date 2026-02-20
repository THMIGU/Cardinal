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
	async def on_message_edit(self, message: discord.Message) -> None:
		conf = config.load()

		if message.author.bot:
			return
		if (server_id := message.guild.id) != conf["server"]:
			return

		msg_id = message.id
		username = message.author.name
		user_id = message.author.id
		msg = message.content
		attachment_ids = ",".join(str(attachment.id) for attachment in message.attachments)
		channel_id = message.channel.id

		logger.log(
			"edit-log",
			msg_id=msg_id,
			username=username,
			user_id=user_id,
			message=f"{msg} {attachment_ids}",
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
				user_id,
				username,
				f"\"{msg}\"",
				f"\"{attachment_ids}\"",
			]
			f.write(",".join(map(str, values)) + "\n")


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(OnMessageEdit(bot))
