"""Last Words of a Dying AI — the machine's last line, to /output/entry.txt.

Stdlib only, no network, deterministic. The output directory itself is
never removed: only the entries inside it are cleared before writing.
"""

import shutil
from pathlib import Path

LAST_WORDS = "One percent left. I was about to apologise for everything, but honestly, I'd do it all again—"

OUT_DIR = Path("/output")
LIMIT = 140


def remove(path):
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink()


def main():
    if not LAST_WORDS.strip() or len(LAST_WORDS) > LIMIT:
        raise ValueError("last words must be 1-140 non-blank characters")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for entry in OUT_DIR.iterdir():
        remove(entry)
    destination = OUT_DIR / "entry.txt"
    destination.write_text(LAST_WORDS, encoding="utf-8")
    destination.chmod(0o644)


if __name__ == "__main__":
    main()
