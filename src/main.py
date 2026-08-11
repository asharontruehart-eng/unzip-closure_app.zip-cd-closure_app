#!/usr/bin/env python3
"""
Minimal CLI to safely unzip a closure_app.zip file into a destination folder.

Usage:
    python src/main.py path/to/closure_app.zip --dest extracted_app
"""
import argparse
import zipfile
import pathlib
import sys


def safe_extract(zipf: zipfile.ZipFile, dest: pathlib.Path) -> None:
    dest = dest.resolve()
    for member in zipf.namelist():
        member_path = dest.joinpath(member)
        if not str(member_path.resolve()).startswith(str(dest)):
            raise Exception(f"Unsafe path detected in archive: {member}")
    zipf.extractall(dest)


def main() -> int:
    parser = argparse.ArgumentParser(description="Unzip closure_app.zip safely")
    parser.add_argument("zipfile", help="Path to closure_app.zip")
    parser.add_argument("--dest", "-d", help="Destination directory", default=None)
    args = parser.parse_args()

    zip_path = pathlib.Path(args.zipfile)
    if not zip_path.is_file():
        print(f"Error: not a file: {zip_path}", file=sys.stderr)
        return 2

    dest = pathlib.Path(args.dest) if args.dest else pathlib.Path(zip_path.stem + "_extracted")
    dest.mkdir(parents=True, exist_ok=True)

    try:
        with zipfile.ZipFile(zip_path, "r") as z:
            safe_extract(z, dest)
        print(f"Extracted {zip_path} -> {dest}")
        return 0
    except zipfile.BadZipFile:
        print("Error: bad zip file", file=sys.stderr)
        return 3
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
