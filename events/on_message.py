# ***********************************************
# *  Project     : Cardinal
# *  File        : events/on_message.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************
import config
# On-message bot event

from data import logger

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
		channel_id = message.channel.id

		logger.log(
			"message-log",
			msg_id=msg_id,
			username=username,
			user_id=user_id,
			message=msg,
			channel_id=channel_id,
			server_id=server_id,
		)

		await self.bot.process_commands(message)


async def setup(bot: commands.Bot) -> None:
	await bot.add_cog(OnMessage(bot))
