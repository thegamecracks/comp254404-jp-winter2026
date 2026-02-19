"""Recursively find files at a source directory matching a given glob pattern."""

import argparse
from fnmatch import fnmatch
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-name",
        "-iname",
        dest="name",
        help="The glob pattern to match",
        required=True,
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        dest="hidden",
        help="Recurse into directories prefixed with '.'",
    )
    parser.add_argument(
        "source",
        default=Path("."),
        help="The source directory to search (default: %s)",
        nargs="?",
        type=Path,
    )

    args = parser.parse_args()
    name: str = args.name
    hidden: bool = args.hidden
    source: Path = args.source

    find(source, name, hidden=hidden)


def find(
    path: Path,
    filename: str,
    *,
    hidden: bool = False,
) -> None:
    directories: list[Path] = []

    for file in path.iterdir():
        if fnmatch(file.name, filename):
            print(file)

        if file.is_dir() and (hidden or not file.name.startswith(".")):
            directories.append(file)

    for d in directories:
        find(d, filename)


if __name__ == "__main__":
    main()
