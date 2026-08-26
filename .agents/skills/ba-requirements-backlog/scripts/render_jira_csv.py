#!/usr/bin/env python3
"""Render the fixed backlog Markdown format as a Jira Cloud import CSV."""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path


FIELD_PATTERN = re.compile(r"^- \*\*(?P<name>[^*]+):\*\*\s*(?P<value>.*)$", re.MULTILINE)
REQ_PATTERN = re.compile(
    r"^### (?P<id>REQ-\d{3}) — (?P<title>.+?)\n(?P<body>.*?)(?=^### REQ-\d{3} —|^## Questions preventing Ready)",
    re.MULTILINE | re.DOTALL,
)
TASK_PATTERN = re.compile(
    r"^### (?P<id>TSK-\d{3}) — (?P<title>.+?)\n(?P<body>.*?)(?=^### TSK-\d{3} —|\Z)",
    re.MULTILINE | re.DOTALL,
)
AC_PATTERN = re.compile(r"^- \[.\] \*\*(AC-\d{3}-\d{2}):\*\*\s*(.+)$", re.MULTILINE)


@dataclass
class WorkItem:
    local_id: str
    work_type: str
    title: str
    description: str
    parent_local_id: str | None


def fields(body: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for match in FIELD_PATTERN.finditer(body):
        value = match.group("value").strip()
        if len(value) >= 2 and value.startswith("`") and value.endswith("`"):
            value = value[1:-1]
        result[match.group("name").strip()] = value
    return result


def require_value(values: dict[str, str], name: str, context: str) -> str:
    value = values.get(name, "")
    if not value or "<" in value or ">" in value:
        raise ValueError(f"{context} requires a completed '{name}' field")
    return value


def parse_backlog(text: str, project_id: str, epic_type: str, story_type: str, task_type: str) -> list[WorkItem]:
    epic_match = re.search(r"^## Epic\n(?P<body>.*?)(?=^## Requirements and stories)", text, re.MULTILINE | re.DOTALL)
    if not epic_match:
        raise ValueError("backlog is missing the fixed Epic section")
    epic_fields = fields(epic_match.group("body"))
    epic_title = require_value(epic_fields, "Title", "Epic")
    epic_description = "\n".join(
        [
            f"Project ID: {project_id}",
            "Local ID: EPIC",
            f"Business owner: {require_value(epic_fields, 'Business owner', 'Epic')}",
            f"Scope boundary: {require_value(epic_fields, 'Scope boundary', 'Epic')}",
            f"Source requirements: {require_value(epic_fields, 'Source requirements', 'Epic')}",
            f"Business Requirements Acceptance: {epic_fields.get('Business Requirements Acceptance', 'Pending')}",
        ]
    )
    items = [WorkItem("EPIC", epic_type, epic_title, epic_description, None)]

    for match in REQ_PATTERN.finditer(text):
        local_id = match.group("id")
        body = match.group("body")
        values = fields(body)
        acceptance = AC_PATTERN.findall(body)
        if not acceptance:
            raise ValueError(f"{local_id} has no acceptance criteria")
        description_lines = [
            f"Project ID: {project_id}",
            f"Local ID: {local_id}",
            f"Outcome / requirement: {require_value(values, 'Outcome / requirement', local_id)}",
            f"Source: {require_value(values, 'Source', local_id)}",
            f"Target release: {values.get('Target release', 'TBD')}",
            "Acceptance criteria:",
        ]
        description_lines.extend(f"{ac_id}: {ac_text}" for ac_id, ac_text in acceptance)
        dependencies = re.search(r"^\*\*Dependencies / constraints:\*\*\s*(.+)$", body, re.MULTILINE)
        if dependencies:
            description_lines.append(f"Dependencies / constraints: {dependencies.group(1).strip()}")
        items.append(
            WorkItem(local_id, story_type, match.group("title").strip(), "\n".join(description_lines), "EPIC")
        )

    task_section = re.search(r"^## Implementation tasks\n(?P<body>.*)\Z", text, re.MULTILINE | re.DOTALL)
    if task_section:
        for match in TASK_PATTERN.finditer(task_section.group("body")):
            local_id = match.group("id")
            values = fields(match.group("body"))
            parent = require_value(values, "Parent requirement", local_id)
            if not re.fullmatch(r"REQ-\d{3}", parent):
                raise ValueError(f"{local_id} has invalid parent requirement: {parent}")
            description = "\n".join(
                [
                    f"Project ID: {project_id}",
                    f"Local ID: {local_id}",
                    f"Related requirement: {parent}",
                    f"Description: {require_value(values, 'Description', local_id)}",
                    f"Owner role: {require_value(values, 'Owner role', local_id)}",
                ]
            )
            items.append(WorkItem(local_id, task_type, match.group("title").strip(), description, "EPIC"))

    if len(items) == 1:
        raise ValueError("backlog contains no completed requirements")
    known_ids = {item.local_id for item in items}
    for item in items:
        if item.parent_local_id and item.parent_local_id not in known_ids:
            raise ValueError(f"{item.local_id} references missing parent {item.parent_local_id}")
    return items


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_id")
    parser.add_argument("--epic-type", default="Epic")
    parser.add_argument("--story-type", default="Story")
    parser.add_argument("--task-type", default="Task")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[4]
    project_dir = repo_root / "projects" / args.project_id
    backlog_path = project_dir / "backlog.md"
    if not backlog_path.is_file():
        parser.error(f"backlog does not exist: {backlog_path}")
    try:
        items = parse_backlog(
            backlog_path.read_text(encoding="utf-8"),
            args.project_id,
            args.epic_type,
            args.story_type,
            args.task_type,
        )
    except ValueError as error:
        parser.error(str(error))

    numeric_ids = {item.local_id: str(index) for index, item in enumerate(items, start=1)}
    output_path = project_dir / "jira-backlog.csv"
    with output_path.open("w", encoding="utf-8-sig", newline="") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(["Work item ID", "Work type", "Summary", "Description", "Parent", "Labels"])
        for item in items:
            parent = numeric_ids[item.parent_local_id] if item.parent_local_id else ""
            writer.writerow(
                [
                    numeric_ids[item.local_id],
                    item.work_type,
                    f"[{item.local_id}] {item.title}",
                    item.description,
                    parent,
                    args.project_id,
                ]
            )
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
