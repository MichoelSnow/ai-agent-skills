#!/usr/bin/env python3
"""Link repository skills into the Codex and Claude Code skill directories."""

from __future__ import annotations

import os
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent
TARGET_DIRECTORIES = (
    Path.home() / ".codex" / "skills",
    Path.home() / ".claude" / "skills",
)


def discover_skills() -> list[Path]:
    """Return top-level skill directories, identified by their SKILL.md file."""
    return sorted(
        (
            path
            for path in REPOSITORY_ROOT.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        ),
        key=lambda path: path.name,
    )


def same_path(left: Path, right: Path) -> bool:
    """Compare paths after resolving symlinks, including broken-link paths."""
    return left.resolve(strict=False) == right.resolve(strict=False)


def link_skills(skills: list[Path]) -> int:
    conflicts = 0
    failures = 0

    for target_directory in TARGET_DIRECTORIES:
        try:
            target_directory.mkdir(parents=True, exist_ok=True)
        except OSError as error:
            print(
                f"ERROR: cannot create {target_directory}: {error}",
                file=sys.stderr,
            )
            failures += 1
            continue

        for skill in skills:
            destination = target_directory / skill.name

            # os.path.lexists also detects broken symlinks, which must not be
            # silently replaced.
            if os.path.lexists(destination):
                if destination.is_symlink() and same_path(destination, skill):
                    print(f"SKIP: {destination} already links to this repository")
                else:
                    print(
                        f"WARNING: conflict at {destination}; "
                        f"not linking {skill}",
                        file=sys.stderr,
                    )
                    conflicts += 1
                continue

            try:
                destination.symlink_to(skill)
                print(f"LINK: {destination} -> {skill}")
            except OSError as error:
                print(f"ERROR: cannot link {destination}: {error}", file=sys.stderr)
                failures += 1

    if conflicts or failures:
        print(
            f"Finished with {conflicts} conflict(s) and {failures} failure(s).",
            file=sys.stderr,
        )
        return 1

    print(f"Finished: processed {len(skills)} skill(s).")
    return 0


def main() -> int:
    skills = discover_skills()
    if not skills:
        print(f"No skill directories containing SKILL.md found in {REPOSITORY_ROOT}.")
        return 0

    return link_skills(skills)


if __name__ == "__main__":
    raise SystemExit(main())
