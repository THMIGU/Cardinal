# ***********************************************
# *  Project     : Cardinal
# *  File        : commands/schedule.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Command for showing the schedule

import csv
import json
import math
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path

import discord
from discord import Embed
from discord.ext import commands

from data import lang, logger
from utils import embeds


class DaySelection(Enum):
    yesterday = -1
    today = 0
    tomorrow = 1


class Schedule(commands.Cog):
    _PATTERN_PATH = Path("assets/schedules/pattern.json")

    bot: commands.Bot

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @staticmethod
    def _format_time(time: str) -> str:
        return datetime.strptime(time, "%H:%M").strftime("%I:%M %p").lstrip("0")

    @staticmethod
    def _get_datetime(time_str: str) -> datetime:
        time = datetime.strptime(f"{time_str} +0800", "%H:%M %z").time()
        date = datetime.now()

        return datetime.combine(date, time)

    @staticmethod
    def _get_current_period(times: list[datetime], now: datetime) -> int:
        for idx, time in enumerate(times):
            delta = time - now

            if delta.total_seconds() <= 0:
                continue

            return idx

        return -1

    @discord.app_commands.command(
        name="schedule",
        description="Look at the LHS bell schedule",
    )
    @discord.app_commands.describe(day="Day to display")
    async def schedule(
        self, interaction: discord.Interaction, day: DaySelection = DaySelection.today
    ) -> None:
        await interaction.response.defer()

        date = datetime.now() + timedelta(days=day.value)
        date_string = str(date)[:10]
        dotw = date.weekday()

        if dotw > 4:
            fail_embed = embeds.fail_embed(f"No schedule for {date.month}/{date.day}")

            await interaction.followup.send(embed=fail_embed)
            return

        if not self._PATTERN_PATH.exists():
            fail_embed = embeds.fail_embed("An internal error occurred!")
            logger.log("pattern-missing")

            await interaction.followup.send(embed=fail_embed)
            return

        with open(self._PATTERN_PATH, "r", encoding="utf-8") as f:
            pattern = json.load(f)

        if date_string in (override := pattern["override"]):
            schedule_type = override[date_string]
        else:
            schedule_type = pattern["default"][str(dotw)]

        schedule_path = Path(f"assets/schedules/{schedule_type}.csv")

        if not schedule_path.exists():
            fail_embed = embeds.fail_embed("An internal error occurred!")
            logger.log("schedule-missing", schedule=schedule_type)

            await interaction.followup.send(embed=fail_embed)
            return

        with open(schedule_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            schedule = [row for row in reader]

        times = [self._get_datetime(time["Start"]) for time in schedule]
        now = datetime(year=2026, month=4, day=3, hour=16, minute=23, second=0)
        current_period = self._get_current_period(times, now)

        if (day != DaySelection.today) or current_period == -1:
            visual_schedule = [
                period
                for period in schedule
                if not period["Name"].startswith("Passing")
            ]

            description = "\n".join(
                [
                    f"**{row['Name']}**: {self._format_time(row['Start'])} - {self._format_time(row['End'])}"
                    for row in visual_schedule
                ]
            )

            schedule_embed = Embed(
                title=lang.get(
                    "schedule-title",
                    month=date.month,
                    day=date.day,
                ),
                description=description,
                color=0xC41E3A,
            )

            await interaction.followup.send(embed=schedule_embed)
            return

        time = times[current_period]
        delta = time - now

        schedule_embed = embeds.success_embed(
            f"{math.floor(delta.seconds / 60)} minutes and {delta.seconds % 60} seconds"
        )
        await interaction.followup.send(embed=schedule_embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Schedule(bot))
