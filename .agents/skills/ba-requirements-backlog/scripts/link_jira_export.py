#!/usr/bin/env python3
"""Create a local-ID-to-Jira-key map from a Jira CSV export and update backlog Jira keys."""

from __future__ import annotations

import argparse
import csv
import re
from datetime import date
from pathlib import Path


LOCAL_ID_PATTERN = re.compile(r"\[(EPIC|REQ-\d{3}|TSK-\d{3})\]")


def normalized(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def select_header(fieldnames: list[str], candidates: set[str]) -> str | None:
    for fieldname in fieldnames:
        if normalized(fieldname) in candidates:
            return fieldname
    return None


def update_backlog_keys(text: str, mapping: dict[str, str]) -> str:
    current_id: str | None = None
    result: list[str] = []
    for line in text.splitlines():
        if line == "## Epic":
            current_id = "EPIC"
        else:
            heading = re.match(r"^### (REQ-\d{3}|TSK-\d{3}) —", line)
            if heading:
                current_id = heading.group(1)
        if line.startswith("- **Jira key:**") and current_id in mapping:
            line = f"- **Jira key:** `{mapping[current_id]}`"
        result.append(line)
    return "\n".join(result) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_id")
    parser.add_argument("jira_export")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[4]
    project_dir = repo_root / "projects" / args.project_id
    collateral_dir = (project_dir / "collateral").resolve()
    export_path = Path(args.jira_export).resolve()
    try:
        export_path.relative_to(collateral_dir)
    except ValueError:
        parser.error("Jira export must first be copied into the project's collateral folder")

    with export_path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        fieldnames = reader.fieldnames or []
        summary_header = select_header(fieldnames, {"summary"})
        key_header = select_header(fieldnames, {"issuekey", "workitemkey", "key"})
        if not summary_header or not key_header:
            parser.error("Jira export must contain Summary and Issue key or Work item key columns")
        mapping: dict[str, tuple[str, str]] = {}
        for row in reader:
            summary = row.get(summary_header, "")
            match = LOCAL_ID_PATTERN.search(summary)
            if not match:
                continue
            local_id = match.group(1)
            jira_key = row.get(key_header, "").strip()
            if not jira_key:
                continue
            if local_id in mapping and mapping[local_id][0] != jira_key:
                parser.error(f"multiple Jira keys found for {local_id}")
            mapping[local_id] = (jira_key, summary)

    if not mapping:
        parser.error("no stable local IDs were found in the Jira export summaries")
    map_path = project_dir / "jira-id-map.csv"
    with map_path.open("w", encoding="utf-8-sig", newline="") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(["Local ID", "Jira key", "Summary", "Imported or linked date"])
        for local_id in sorted(mapping):
            jira_key, summary = mapping[local_id]
            writer.writerow([local_id, jira_key, summary, date.today().isoformat()])

    backlog_path = project_dir / "backlog.md"
    backlog = backlog_path.read_text(encoding="utf-8")
    backlog_path.write_text(
        update_backlog_keys(backlog, {key: value[0] for key, value in mapping.items()}),
        encoding="utf-8",
    )
    print(map_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
