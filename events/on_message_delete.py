# ***********************************************
# *  Project     : Cardinal
# *  File        : events/on_message_delete.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# On-message delete bot event

from data import logger, config

import discord
from discord.ext import commands


class OnMessageDelete(commands.Cog):
	bot: commands.Bot

	def __init__(self, bot: commands.Bot) -> None:
		self.bot = bot

	@commands.Cog.listener()
	async def on_message_delete(self, message: discord.Message) -> None:
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
			"delete-log",
			msg_id=msg_id,
			username=username,
			user_id=user_id,
			message=f"{msg} {attachment_ids}",
			channel_id=channel_id,
			server_id=server_id,
		)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(OnMessageDelete(bot))
