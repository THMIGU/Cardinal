# ***********************************************
# *  Project     : Cardinal
# *  File        : utils/file.py
# *  Author      : Kai Parsons
# *  Date        : 2026-02-15
# *  Description : Mod. & game bot for Ess. Ress.
# ***********************************************

# Load config file, create if missing.

import shutil
from pathlib import Path


def copy(*, src: Path, dst: Path, overwrite: bool = False) -> bool:
	if dst.exists() and not overwrite:
		return False

	dst.parent.mkdir(parents=True, exist_ok=True)
	shutil.copyfile(str(src), str(dst))
	return True
