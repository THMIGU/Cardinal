# ***********************************************
# *  Project     : Cardinal
# *  File        : events/on_message.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# On-message bot event

from datetime import datetime

from data import logger, config, csv

import discord
from discord.ext import commands


class OnMessage(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message: discord.Message) -> None:
		conf = config.load()

		if message.author.bot:
			return
		if (server_id := message.guild.id) != conf["server"]:
			return

		reply = message.reference
		msg_id = message.id
		username = message.author.name
		user_id = message.author.id
		msg = message.content
		attachment_ids = ",".join(str(attachment.id) for attachment in message.attachments)
		channel_id = message.channel.id

		ref_id = ""
		if reply:
			ref_id = message.reference.message_id

		logger.log(
			"message-log" if not reply else "reply-log",
			msg_id=msg_id,
			ref_id=ref_id,
			username=username,
			user_id=user_id,
			message=f"{msg} {attachment_ids}".strip(),
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
				ref_id,
				user_id,
				username,
				f"\"{msg}\"",
				f"\"{attachment_ids}\"",
			]
			f.write(",".join(map(str, values)) + "\n")

		await self.bot.process_commands(message)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(OnMessage(bot))
