# ***********************************************
# *  Project     : Cardinal
# *  File        : services/redis_.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Message sending through Redis

import asyncio
from redis import Redis
from typing import Any, Generator

from data import logger, config

from discord.ext import commands


async def send_message(msg: bytes, bot: commands.Bot) -> None:
	message = msg.decode()
	if message == "__shutdown__":
		return

	logger.log("redis-send", message=message)

	conf = config.load()
	channel_id = conf["channel"]
	channel = bot.get_channel(channel_id)

	await channel.send(message)


def listen() -> Generator[str | bytes, Any, None]:
	conf = config.load()
	host = conf["redis-host"]
	port = conf["redis-port"]

	r = Redis(host=host, port=port, db=0)
	pubsub = r.pubsub()
	pubsub.subscribe("cardinal:message")

	for message in pubsub.listen():
		if message["type"] == "message":
			yield message["data"]


async def subscribe(bot: commands.Bot) -> None:
	while not bot.is_closed():
		msg = await asyncio.to_thread(lambda: next(listen()))
		asyncio.create_task(send_message(msg, bot))


def publish(message: str) -> None:
	conf = config.load()
	host = conf["redis-host"]
	port = conf["redis-port"]

	r = Redis(host=host, port=port, db=0)

	r.publish("cardinal:message", message)
