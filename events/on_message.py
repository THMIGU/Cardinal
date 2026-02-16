# ***********************************************
# *  Project     : Cardinal
# *  File        : events/on_message.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
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

		msg_id = message.id
		username = message.author.name
		user_id = message.author.id
		msg = message.content
		attachments = " ".join(attachment.url for attachment in message.attachments)
		channel_id = message.channel.id

		logger.log(
			"message-log",
			msg_id=msg_id,
			username=username,
			user_id=user_id,
			message=msg + attachments,
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
				f"\"{attachments}\"",
			]
			f.write(",".join(map(str, values)) + "\n")

		await self.bot.process_commands(message)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(OnMessage(bot))
