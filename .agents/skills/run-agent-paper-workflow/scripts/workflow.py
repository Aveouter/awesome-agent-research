#!/usr/bin/env python3
"""Validate and operate the paper-reading workflow without third-party packages."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
TRACKER = ROOT / "papers.md"

STATUSES = {
    "TO_READ",
    "SKIMMED",
    "DEEP_READ",
    "REPRODUCING",
    "REPRODUCED",
    "DROPPED",
}
EVIDENCE_LEVELS = {"abstract-only", "skimmed", "full-paper", "reproduced"}
TRANSITIONS = {
    "TO_READ": {"SKIMMED", "DROPPED"},
    "SKIMMED": {"DEEP_READ", "DROPPED"},
    "DEEP_READ": {"REPRODUCING", "DROPPED"},
    "REPRODUCING": {"REPRODUCED", "DEEP_READ"},
    "REPRODUCED": {"REPRODUCING"},
    "DROPPED": {"TO_READ"},
}
REQUIRED_FILES = {
    ".agents/skills/run-agent-paper-workflow/SKILL.md",
    ".github/workflows/validate.yml",
    "AGENTS.md",
    "CONTEXT.md",
    "README.md",
    "WORKFLOW.md",
    "artifacts/README.md",
    "experiments/README.md",
    "inbox.md",
    "papers.md",
    "references/library.bib",
    "research/direction-map.md",
    "research/idea-backlog.md",
    "templates/paper-note.md",
}
PAPER_ID_PATTERN = re.compile(r"^(?:MA|CL|MC|X)-\d{3}$")
MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
NOTE_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def table_rows() -> list[tuple[int, list[str]]]:
    rows: list[tuple[int, list[str]]] = []
    for line_number, line in enumerate(TRACKER.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not cells or cells[0] == "ID" or set(cells[0]) == {"-"}:
            continue
        rows.append((line_number, cells))
    return rows


def validate() -> list[str]:
    errors: list[str] = []
    for relative_path in sorted(REQUIRED_FILES):
        if not (ROOT / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")

    if not TRACKER.is_file():
        return errors

    tracker: dict[str, tuple[str, str, Path]] = {}
    for line_number, cells in table_rows():
        if len(cells) != 8:
            errors.append(f"papers.md:{line_number}: expected 8 columns, found {len(cells)}")
            continue

        paper_id, status, evidence = cells[0], cells[4], cells[5]
        if not PAPER_ID_PATTERN.fullmatch(paper_id):
            errors.append(f"papers.md:{line_number}: invalid paper ID {paper_id!r}")
        elif paper_id in tracker:
            errors.append(f"papers.md:{line_number}: duplicate paper ID {paper_id}")

        if status not in STATUSES:
            errors.append(f"papers.md:{line_number}: invalid status {status!r}")
        if evidence not in EVIDENCE_LEVELS:
            errors.append(f"papers.md:{line_number}: invalid evidence level {evidence!r}")

        link_match = NOTE_LINK_PATTERN.search(cells[6])
        if not link_match:
            errors.append(f"papers.md:{line_number}: note column has no Markdown link")
            continue
        note_path = ROOT / link_match.group(1)
        if not note_path.is_file():
            errors.append(f"papers.md:{line_number}: missing note {link_match.group(1)!r}")
        tracker[paper_id] = (status, evidence, note_path)

    note_ids: set[str] = set()
    for note in sorted((ROOT / "notes").rglob("*.md")):
        content = note.read_text(encoding="utf-8")
        relative_path = note.relative_to(ROOT)

        id_match = re.search(r"^- ID：\s*(\S+)", content, re.MULTILINE)
        if not id_match:
            errors.append(f"{relative_path}: missing metadata ID")
            continue
        paper_id = id_match.group(1)
        if paper_id in note_ids:
            errors.append(f"{relative_path}: duplicate note ID {paper_id}")
        note_ids.add(paper_id)

        if paper_id not in tracker:
            errors.append(f"{relative_path}: ID {paper_id} is absent from papers.md")
            continue

        note_status_match = re.search(r"^- Status：\s*([A-Z_]+)", content, re.MULTILINE)
        note_evidence_match = re.search(
            r"^- Evidence level：\s*([a-z-]+)", content, re.MULTILINE
        )
        tracker_status, tracker_evidence, tracker_note = tracker[paper_id]

        if not note_status_match:
            errors.append(f"{relative_path}: missing metadata Status")
        elif note_status_match.group(1) != tracker_status:
            errors.append(
                f"{relative_path}: status {note_status_match.group(1)!r} "
                f"does not match tracker {tracker_status!r}"
            )

        if not note_evidence_match:
            errors.append(f"{relative_path}: missing metadata Evidence level")
        elif note_evidence_match.group(1) != tracker_evidence:
            errors.append(
                f"{relative_path}: evidence {note_evidence_match.group(1)!r} "
                f"does not match tracker {tracker_evidence!r}"
            )

        if note.resolve() != tracker_note.resolve():
            errors.append(f"{relative_path}: tracker points to a different note")
        if not re.search(r"^- Paper：\s*https?://", content, re.MULTILINE):
            errors.append(f"{relative_path}: Paper must use an HTTP(S) source URL")

    for paper_id in sorted(set(tracker) - note_ids):
        errors.append(f"papers.md: {paper_id} has no canonical note under notes/")

    for artifact_dir in sorted((ROOT / "artifacts").iterdir()):
        if artifact_dir.is_dir() and not PAPER_ID_PATTERN.fullmatch(artifact_dir.name):
            errors.append(f"artifacts/{artifact_dir.name}: directory must use a paper ID")

    for markdown_file in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown_file.parts:
            continue
        content = markdown_file.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK_PATTERN.findall(content):
            target = target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (markdown_file.parent / target).resolve().exists():
                relative_path = markdown_file.relative_to(ROOT)
                errors.append(f"{relative_path}: broken local link {target!r}")

    return errors


def print_validation() -> int:
    errors = validate()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Repository validation passed: {len(table_rows())} papers checked.")
    return 0


def print_status() -> int:
    errors = validate()
    if errors:
        print("Cannot summarize an invalid repository. Run the validate command.")
        return 1

    rows = [cells for _, cells in table_rows()]
    status_counts = Counter(cells[4] for cells in rows)
    evidence_counts = Counter(cells[5] for cells in rows)
    print(f"Papers: {len(rows)}")
    print("Status: " + ", ".join(f"{key}={status_counts[key]}" for key in sorted(status_counts)))
    print(
        "Evidence: "
        + ", ".join(f"{key}={evidence_counts[key]}" for key in sorted(evidence_counts))
    )
    queue = [cells[0] for cells in rows if cells[4] == "TO_READ"]
    print("TO_READ queue: " + (", ".join(queue) if queue else "empty"))
    return 0


def transition(paper_id: str, new_status: str, reason: str | None) -> int:
    errors = validate()
    if errors:
        print("Refusing to update an invalid repository. Run validate first.")
        return 1

    if new_status not in STATUSES:
        print(f"Unknown status: {new_status}")
        return 1

    lines = TRACKER.read_text(encoding="utf-8").splitlines()
    matched_index: int | None = None
    matched_cells: list[str] | None = None
    for index, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells and cells[0] == paper_id:
            matched_index, matched_cells = index, cells
            break

    if matched_index is None or matched_cells is None:
        print(f"Paper ID not found: {paper_id}")
        return 1

    old_status = matched_cells[4]
    if new_status == old_status:
        print(f"{paper_id} is already {new_status}.")
        return 0
    if new_status not in TRANSITIONS[old_status]:
        allowed = ", ".join(sorted(TRANSITIONS[old_status])) or "none"
        print(f"Invalid transition {old_status} -> {new_status}; allowed: {allowed}")
        return 1
    if old_status == "DROPPED" and new_status == "TO_READ" and not reason:
        print("DROPPED -> TO_READ requires --reason with the new evidence or priority change.")
        return 1

    note_match = NOTE_LINK_PATTERN.search(matched_cells[6])
    if not note_match:
        print(f"Cannot resolve canonical note for {paper_id}")
        return 1
    note_path = ROOT / note_match.group(1)
    note_content = note_path.read_text(encoding="utf-8")
    updated_note, substitutions = re.subn(
        r"(^- Status：\s*)[A-Z_]+",
        rf"\g<1>{new_status}",
        note_content,
        count=1,
        flags=re.MULTILINE,
    )
    if substitutions != 1:
        print(f"Could not update Status metadata in {note_path.relative_to(ROOT)}")
        return 1

    matched_cells[4] = new_status
    if reason:
        matched_cells[7] = reason
    lines[matched_index] = "| " + " | ".join(matched_cells) + " |"

    tracker_tmp = TRACKER.with_suffix(".md.tmp")
    note_tmp = note_path.with_suffix(".md.tmp")
    tracker_tmp.write_text("\n".join(lines) + "\n", encoding="utf-8")
    note_tmp.write_text(updated_note, encoding="utf-8")
    tracker_tmp.replace(TRACKER)
    note_tmp.replace(note_path)
    print(f"Transitioned {paper_id}: {old_status} -> {new_status}")
    return print_validation()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate", help="validate repository structure and metadata")
    subparsers.add_parser("status", help="summarize paper status and evidence levels")
    transition_parser = subparsers.add_parser("transition", help="apply a valid status transition")
    transition_parser.add_argument("paper_id")
    transition_parser.add_argument("new_status")
    transition_parser.add_argument(
        "--reason", help="record why the transition is being made in the tracker"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "validate":
        return print_validation()
    if args.command == "status":
        return print_status()
    return transition(args.paper_id, args.new_status, args.reason)


if __name__ == "__main__":
    sys.exit(main())
