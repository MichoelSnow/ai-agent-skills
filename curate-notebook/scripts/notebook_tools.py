#!/usr/bin/env python3
"""
Mechanical Jupyter notebook inspection and editing utilities.

This script intentionally does not make analytical judgments. It provides
safe, deterministic operations for inspecting, backing up, validating, and
editing .ipynb files.

Dependency:
    poetry add nbformat

Examples:
    python notebook_tools.py inspect notebook.ipynb
    python notebook_tools.py backup notebook.ipynb
    python notebook_tools.py validate notebook.ipynb
    python notebook_tools.py move notebook.ipynb --cell-id abc123 --before def456
    python notebook_tools.py delete notebook.ipynb --cell-id abc123
    python notebook_tools.py insert-markdown notebook.ipynb --before def456 --file section.md
    python notebook_tools.py replace notebook.ipynb --cell-id abc123 --file replacement.py
    python notebook_tools.py clear-outputs notebook.ipynb
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import nbformat
from nbformat import NotebookNode


def load_notebook(path: Path) -> NotebookNode:
    if not path.exists():
        raise FileNotFoundError(f"Notebook not found: {path}")
    if path.suffix.lower() != ".ipynb":
        raise ValueError(f"Expected a .ipynb file: {path}")
    return nbformat.read(path, as_version=4)


def write_notebook(path: Path, notebook: NotebookNode) -> None:
    nbformat.validate(notebook)
    nbformat.write(notebook, path)


def first_nonempty_line(source: str) -> str:
    for line in source.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def cell_id(cell: NotebookNode) -> str | None:
    return cell.get("id")


def find_cell_index(notebook: NotebookNode, requested_id: str) -> int:
    matches = [
        index
        for index, cell in enumerate(notebook.cells)
        if cell_id(cell) == requested_id
    ]
    if not matches:
        raise ValueError(f"Cell id not found: {requested_id}")
    if len(matches) > 1:
        raise ValueError(f"Duplicate cell id found: {requested_id}")
    return matches[0]


def require_backup(source: Path, backup_path: Path | None) -> Path:
    if backup_path is None:
        raise ValueError(
            "Mutating operations require --backup. "
            "Create a backup first or provide an existing backup path."
        )
    if not backup_path.exists():
        raise FileNotFoundError(f"Backup does not exist: {backup_path}")
    if backup_path.resolve() == source.resolve():
        raise ValueError("Backup path must differ from the source notebook.")
    return backup_path


def default_backup_path(source: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return source.with_name(f"{source.stem}.backup_{timestamp}{source.suffix}")


def cmd_inspect(args: argparse.Namespace) -> None:
    path = Path(args.notebook)
    notebook = load_notebook(path)

    rows: list[dict[str, Any]] = []
    for index, cell in enumerate(notebook.cells):
        source = cell.get("source", "")
        rows.append(
            {
                "index": index,
                "id": cell_id(cell),
                "type": cell.cell_type,
                "execution_count": (
                    cell.get("execution_count")
                    if cell.cell_type == "code"
                    else None
                ),
                "output_count": (
                    len(cell.get("outputs", []))
                    if cell.cell_type == "code"
                    else None
                ),
                "empty": not bool(source.strip()),
                "first_line": first_nonempty_line(source),
            }
        )

    if args.json:
        print(
            json.dumps(
                {
                    "path": str(path),
                    "nbformat": notebook.nbformat,
                    "nbformat_minor": notebook.nbformat_minor,
                    "cell_count": len(notebook.cells),
                    "cells": rows,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
        return

    print(f"Notebook: {path}")
    print(f"Cells: {len(rows)}")
    print()
    for row in rows:
        print(
            f"[{row['index']:03d}] "
            f"id={row['id'] or '-'} "
            f"type={row['type']} "
            f"exec={row['execution_count']} "
            f"outputs={row['output_count']} "
            f"empty={row['empty']} "
            f"| {row['first_line'][:120]}"
        )


def cmd_backup(args: argparse.Namespace) -> None:
    source = Path(args.notebook)
    load_notebook(source)

    destination = (
        Path(args.output)
        if args.output
        else default_backup_path(source)
    )

    if destination.exists() and not args.overwrite:
        raise FileExistsError(
            f"Backup already exists: {destination}. "
            "Use --overwrite only if replacing it is intentional."
        )

    shutil.copy2(source, destination)
    print(destination)


def cmd_validate(args: argparse.Namespace) -> None:
    path = Path(args.notebook)
    notebook = load_notebook(path)
    nbformat.validate(notebook)

    ids = [cell_id(cell) for cell in notebook.cells if cell_id(cell)]
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})

    empty_cells = [
        index
        for index, cell in enumerate(notebook.cells)
        if not cell.get("source", "").strip()
    ]

    non_monotonic_execution: list[tuple[int, int, int]] = []
    previous: int | None = None
    previous_index: int | None = None
    for index, cell in enumerate(notebook.cells):
        if cell.cell_type != "code":
            continue
        count = cell.get("execution_count")
        if count is None:
            continue
        if previous is not None and count < previous:
            non_monotonic_execution.append(
                (previous_index if previous_index is not None else -1, index, count)
            )
        previous = count
        previous_index = index

    result = {
        "valid_nbformat": True,
        "cell_count": len(notebook.cells),
        "duplicate_cell_ids": duplicate_ids,
        "empty_cell_indexes": empty_cells,
        "non_monotonic_execution_transitions": non_monotonic_execution,
    }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("Notebook format: valid")
        print(f"Cells: {result['cell_count']}")
        print(f"Duplicate cell ids: {duplicate_ids or 'none'}")
        print(f"Empty cells: {empty_cells or 'none'}")
        print(
            "Non-monotonic execution transitions: "
            f"{non_monotonic_execution or 'none'}"
        )


def cmd_move(args: argparse.Namespace) -> None:
    path = Path(args.notebook)
    backup = Path(args.backup) if args.backup else None
    require_backup(path, backup)

    if bool(args.before) == bool(args.after):
        raise ValueError("Provide exactly one of --before or --after.")

    notebook = load_notebook(path)
    source_index = find_cell_index(notebook, args.cell_id)
    moving_cell = notebook.cells.pop(source_index)

    target_id = args.before or args.after
    target_index = find_cell_index(notebook, target_id)

    insert_at = target_index if args.before else target_index + 1
    notebook.cells.insert(insert_at, moving_cell)
    write_notebook(path, notebook)

    print(
        f"Moved cell {args.cell_id} "
        f"{'before' if args.before else 'after'} {target_id}"
    )


def cmd_delete(args: argparse.Namespace) -> None:
    path = Path(args.notebook)
    backup = Path(args.backup) if args.backup else None
    require_backup(path, backup)

    notebook = load_notebook(path)
    index = find_cell_index(notebook, args.cell_id)
    deleted = notebook.cells.pop(index)
    write_notebook(path, notebook)

    print(
        f"Deleted cell {args.cell_id}: "
        f"{first_nonempty_line(deleted.get('source', ''))[:120]}"
    )


def read_text_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def insertion_index(
    notebook: NotebookNode,
    *,
    before: str | None,
    after: str | None,
    index: int | None,
) -> int:
    specified = sum(
        value is not None
        for value in (before, after, index)
    )
    if specified != 1:
        raise ValueError(
            "Provide exactly one insertion location: "
            "--before, --after, or --index."
        )

    if before is not None:
        return find_cell_index(notebook, before)
    if after is not None:
        return find_cell_index(notebook, after) + 1

    assert index is not None
    if index < 0 or index > len(notebook.cells):
        raise ValueError(
            f"Insertion index must be between 0 and {len(notebook.cells)}."
        )
    return index


def cmd_insert_markdown(args: argparse.Namespace) -> None:
    path = Path(args.notebook)
    backup = Path(args.backup) if args.backup else None
    require_backup(path, backup)

    notebook = load_notebook(path)
    source = read_text_file(args.file)
    cell = nbformat.v4.new_markdown_cell(source=source)

    insert_at = insertion_index(
        notebook,
        before=args.before,
        after=args.after,
        index=args.index,
    )
    notebook.cells.insert(insert_at, cell)
    write_notebook(path, notebook)

    print(f"Inserted markdown cell at index {insert_at}, id={cell.get('id')}")


def cmd_insert_code(args: argparse.Namespace) -> None:
    path = Path(args.notebook)
    backup = Path(args.backup) if args.backup else None
    require_backup(path, backup)

    notebook = load_notebook(path)
    source = read_text_file(args.file)
    cell = nbformat.v4.new_code_cell(source=source)

    insert_at = insertion_index(
        notebook,
        before=args.before,
        after=args.after,
        index=args.index,
    )
    notebook.cells.insert(insert_at, cell)
    write_notebook(path, notebook)

    print(f"Inserted code cell at index {insert_at}, id={cell.get('id')}")


def cmd_replace(args: argparse.Namespace) -> None:
    path = Path(args.notebook)
    backup = Path(args.backup) if args.backup else None
    require_backup(path, backup)

    notebook = load_notebook(path)
    index = find_cell_index(notebook, args.cell_id)
    original = notebook.cells[index]
    source = read_text_file(args.file)

    if args.type == "keep":
        replacement_type = original.cell_type
    else:
        replacement_type = args.type

    if replacement_type == "markdown":
        replacement = nbformat.v4.new_markdown_cell(source=source)
    elif replacement_type == "code":
        replacement = nbformat.v4.new_code_cell(source=source)
    else:
        raise ValueError(f"Unsupported replacement type: {replacement_type}")

    if original.get("id"):
        replacement["id"] = original["id"]

    notebook.cells[index] = replacement
    write_notebook(path, notebook)

    print(f"Replaced cell {args.cell_id} as {replacement_type}")


def cmd_clear_outputs(args: argparse.Namespace) -> None:
    path = Path(args.notebook)
    backup = Path(args.backup) if args.backup else None
    require_backup(path, backup)

    notebook = load_notebook(path)

    if args.cell_id:
        indexes = [find_cell_index(notebook, value) for value in args.cell_id]
    else:
        indexes = list(range(len(notebook.cells)))

    cleared = 0
    for index in indexes:
        cell = notebook.cells[index]
        if cell.cell_type != "code":
            continue
        if cell.get("outputs") or cell.get("execution_count") is not None:
            cleared += 1
        cell["outputs"] = []
        if args.reset_execution_counts:
            cell["execution_count"] = None

    write_notebook(path, notebook)
    print(f"Cleared outputs from {cleared} code cell(s)")


def cmd_reset_execution_counts(args: argparse.Namespace) -> None:
    path = Path(args.notebook)
    backup = Path(args.backup) if args.backup else None
    require_backup(path, backup)

    notebook = load_notebook(path)
    changed = 0
    for cell in notebook.cells:
        if cell.cell_type == "code" and cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed += 1

    write_notebook(path, notebook)
    print(f"Reset execution counts on {changed} code cell(s)")


def add_location_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--before", help="Insert before this cell id")
    parser.add_argument("--after", help="Insert after this cell id")
    parser.add_argument("--index", type=int, help="Insert at numeric cell index")


def add_backup_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--backup",
        required=True,
        help="Path to an existing backup of the source notebook",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Safe mechanical utilities for Jupyter notebook curation."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser(
        "inspect",
        help="Print a compact structural inventory of the notebook",
    )
    inspect_parser.add_argument("notebook")
    inspect_parser.add_argument("--json", action="store_true")
    inspect_parser.set_defaults(func=cmd_inspect)

    backup_parser = subparsers.add_parser(
        "backup",
        help="Create a timestamped or explicitly named backup",
    )
    backup_parser.add_argument("notebook")
    backup_parser.add_argument("--output")
    backup_parser.add_argument("--overwrite", action="store_true")
    backup_parser.set_defaults(func=cmd_backup)

    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate nbformat and report basic structural warnings",
    )
    validate_parser.add_argument("notebook")
    validate_parser.add_argument("--json", action="store_true")
    validate_parser.set_defaults(func=cmd_validate)

    move_parser = subparsers.add_parser(
        "move",
        help="Move one cell relative to another using stable cell ids",
    )
    move_parser.add_argument("notebook")
    move_parser.add_argument("--cell-id", required=True)
    move_parser.add_argument("--before")
    move_parser.add_argument("--after")
    add_backup_argument(move_parser)
    move_parser.set_defaults(func=cmd_move)

    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a cell by stable cell id",
    )
    delete_parser.add_argument("notebook")
    delete_parser.add_argument("--cell-id", required=True)
    add_backup_argument(delete_parser)
    delete_parser.set_defaults(func=cmd_delete)

    insert_md_parser = subparsers.add_parser(
        "insert-markdown",
        help="Insert a markdown cell from a UTF-8 text file",
    )
    insert_md_parser.add_argument("notebook")
    insert_md_parser.add_argument("--file", required=True)
    add_location_arguments(insert_md_parser)
    add_backup_argument(insert_md_parser)
    insert_md_parser.set_defaults(func=cmd_insert_markdown)

    insert_code_parser = subparsers.add_parser(
        "insert-code",
        help="Insert a code cell from a UTF-8 text file",
    )
    insert_code_parser.add_argument("notebook")
    insert_code_parser.add_argument("--file", required=True)
    add_location_arguments(insert_code_parser)
    add_backup_argument(insert_code_parser)
    insert_code_parser.set_defaults(func=cmd_insert_code)

    replace_parser = subparsers.add_parser(
        "replace",
        help="Replace cell source while preserving its stable cell id",
    )
    replace_parser.add_argument("notebook")
    replace_parser.add_argument("--cell-id", required=True)
    replace_parser.add_argument("--file", required=True)
    replace_parser.add_argument(
        "--type",
        choices=["keep", "markdown", "code"],
        default="keep",
    )
    add_backup_argument(replace_parser)
    replace_parser.set_defaults(func=cmd_replace)

    clear_parser = subparsers.add_parser(
        "clear-outputs",
        help="Clear code-cell outputs, optionally for selected cell ids",
    )
    clear_parser.add_argument("notebook")
    clear_parser.add_argument(
        "--cell-id",
        action="append",
        help="Cell id to clear; repeat for multiple cells. "
             "If omitted, clears all code cells.",
    )
    clear_parser.add_argument(
        "--reset-execution-counts",
        action="store_true",
        help="Also set execution_count to null",
    )
    add_backup_argument(clear_parser)
    clear_parser.set_defaults(func=cmd_clear_outputs)

    reset_parser = subparsers.add_parser(
        "reset-execution-counts",
        help="Set execution_count to null for all code cells",
    )
    reset_parser.add_argument("notebook")
    add_backup_argument(reset_parser)
    reset_parser.set_defaults(func=cmd_reset_execution_counts)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        args.func(args)
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
