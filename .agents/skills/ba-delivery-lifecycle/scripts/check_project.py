#!/usr/bin/env python3
"""Check required project files, fixed headings, stage values, approvals, and release controls."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


STAGES = {
    "1 of 7 — Intake",
    "2 of 7 — Discovery & Requirements",
    "3 of 7 — Business Requirements Approval",
    "4 of 7 — Delivery",
    "5 of 7 — Validation",
    "6 of 7 — Completion Signoffs",
    "7 of 7 — Complete",
}
REQUIRED_FILES = {
    "project-context.md",
    "delivery-traceability-record.md",
    "backlog.md",
    "jira-backlog.csv",
    "jira-id-map.csv",
    "change-log.md",
    "validation.md",
}
REQUIRED_APPROVALS = {
    "Business Requirements Acceptance",
    "UAT Acceptance",
    "Security Sign-off",
    "Project Completion Sign-off",
}
APPROVAL_STATUSES = {
    "Pending",
    "Approved",
    "Approved with exceptions",
    "Rejected",
    "Superseded",
    "Not required",
}
APPROVED = {"Approved", "Approved with exceptions"}


def table_value(text: str, field: str) -> str | None:
    match = re.search(rf"^\| {re.escape(field)} \|\s*(.*?)\s*\|$", text, re.MULTILINE)
    return match.group(1) if match else None


def approval_statuses(dtr: str) -> dict[str, str]:
    statuses: dict[str, str] = {}
    for match in re.finditer(
        r"^\| APR-[^|]+ \|\s*([^|]+?)\s*\|[^|]*\|\s*([^|]+?)\s*\|",
        dtr,
        re.MULTILINE,
    ):
        statuses[match.group(1).strip()] = match.group(2).strip()
    return statuses


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_id")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[4]
    project_dir = repo_root / "projects" / args.project_id
    errors: list[str] = []
    if not project_dir.is_dir():
        parser.error(f"project workspace does not exist: {project_dir}")

    missing = sorted(name for name in REQUIRED_FILES if not (project_dir / name).is_file())
    if missing:
        errors.append(f"missing required files: {', '.join(missing)}")
    for directory in ("collateral", "releases"):
        if not (project_dir / directory).is_dir():
            errors.append(f"missing required directory: {directory}")

    context_path = project_dir / "project-context.md"
    dtr_path = project_dir / "delivery-traceability-record.md"
    context = context_path.read_text(encoding="utf-8") if context_path.is_file() else ""
    dtr = dtr_path.read_text(encoding="utf-8") if dtr_path.is_file() else ""
    context_stage = table_value(context, "Current lifecycle stage")
    dtr_stage = table_value(dtr, "Current lifecycle stage")
    if context_stage not in STAGES:
        errors.append(f"invalid project-context lifecycle stage: {context_stage}")
    if dtr_stage not in STAGES:
        errors.append(f"invalid DTR lifecycle stage: {dtr_stage}")
    if context_stage and dtr_stage and context_stage != dtr_stage:
        errors.append("project-context and DTR lifecycle stages differ")
    approvals = approval_statuses(dtr)
    for approval in sorted(REQUIRED_APPROVALS):
        if approval not in approvals:
            errors.append(f"DTR missing approval type: {approval}")
        status = approvals.get(approval)
        if status and status not in APPROVAL_STATUSES:
            errors.append(f"DTR has invalid {approval} status: {status}")

    stage_number = int(context_stage.split()[0]) if context_stage in STAGES else 0
    if stage_number >= 4 and approvals.get("Business Requirements Acceptance") not in APPROVED:
        errors.append("Stage 4 or later requires current Business Requirements Acceptance")
    if stage_number >= 6:
        if approvals.get("UAT Acceptance") not in APPROVED:
            errors.append("Stage 6 or later requires UAT Acceptance")
        if approvals.get("Security Sign-off") not in APPROVED | {"Not required"}:
            errors.append("Stage 6 or later requires Security Sign-off or documented Not required")
    if stage_number >= 7 and approvals.get("Project Completion Sign-off") not in APPROVED:
        errors.append("Stage 7 requires Project Completion Sign-off")
    if stage_number >= 7:
        attachment = re.search(r"^\*\*DTR attached to project record:\*\*\s*(.+)$", dtr, re.MULTILINE)
        if not attachment or "<" in attachment.group(1) or attachment.group(1).strip() in {"TBD", "Pending"}:
            errors.append("Stage 7 requires the DTR attachment date or central-record reference")

    csv_path = project_dir / "jira-backlog.csv"
    if csv_path.is_file():
        with csv_path.open("r", encoding="utf-8-sig", newline="") as source:
            header = next(csv.reader(source), [])
        expected = ["Work item ID", "Work type", "Summary", "Description", "Parent", "Labels"]
        if header != expected:
            errors.append(f"jira-backlog.csv header differs from contract: {header}")

    for release_path in sorted(
        (project_dir / "releases").glob("*.md"), key=lambda item: item.name.lower()
    ):
        release = release_path.read_text(encoding="utf-8")
        if table_value(release, "Status") == "Released":
            for field in ("Repository", "Tag / version", "Production date", "Change-management ticket"):
                value = table_value(release, field)
                if not value or value == "TBD" or "<" in value:
                    errors.append(f"{release_path.name}: Released status requires {field}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Project structure valid: {args.project_id} — {context_stage}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
