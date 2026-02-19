# ***********************************************
# *  Project     : Cardinal
# *  File        : data/logger.py
# *  Author      : Kai Parsons
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Saves logs to file and makes them look nice :)

import re
import sys
from datetime import datetime
from pathlib import Path

from data import info, lang

PATH = Path("logs")


class Logger:
	def __init__(self, logfile) -> None:
		self.terminal = sys.stdout
		self.log = logfile

	def write(self, message) -> None:
		if message != "\n":
			self.terminal.write(
				lang.get(
					"terminal-log",
					date=str(datetime.now())[:-7],
					message=message,
				)
			)

			ansi_escape_pattern = r'\x1B\[[0-?]*[ -/]*[@-~]'
			message = re.sub(ansi_escape_pattern, '', message)

			self.log.write(
				lang.get(
					"file-log",
					date=str(datetime.now())[:-7],
					message=message,
				)
			)
		else:
			self.terminal.write(message)
			self.log.write(message)

	def flush(self) -> None:
		self.terminal.flush()
		self.log.flush()


def init() -> None:
	inf = info.load()

	log_version = lang.get(
		"log-version",
		version=inf["version"],
		date=str(datetime.now())[:-7]
	)

	log_file_path = f"logs/log{datetime.now().strftime('-%b-%d-%H_%M_%S').lower()}.txt"
	log_file = open(log_file_path, "x", encoding="utf-8")
	log_file.write(
		lang.get(
			"log-header",
			log_version=log_version,
			separator="=" * len(log_version),
		)
	)

	sys.stdout = Logger(log_file)


def flush(*, verbose: bool = True) -> None:
	sys.stdout.flush()

	if not verbose:
		return

	log("flush-logs")


def log(key: str, **kwargs) -> None:
	message = lang.get(key, **kwargs)
	print(message)
