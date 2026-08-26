#!/usr/bin/env python3
"""Print the fixed lifecycle-status block from current project records."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


NEXT_ACTION = {
    "1 of 7 — Intake": "Copy all supplied collateral and complete the people/source inventory.",
    "2 of 7 — Discovery & Requirements": "Complete the team boundary, Ready backlog, and Jira import CSV.",
    "3 of 7 — Business Requirements Approval": "Obtain Business Requirements Acceptance from the business owner.",
    "4 of 7 — Delivery": "Deliver approved scope; record each deployment and change ticket independently.",
    "5 of 7 — Validation": "Complete final-scope validation and obtain UAT Acceptance.",
    "6 of 7 — Completion Signoffs": "Complete required security disposition, final reconciliation, and Project Completion Sign-off.",
    "7 of 7 — Complete": "No lifecycle action required; preserve the centrally attached DTR.",
}


def table_value(text: str, field: str) -> str:
    match = re.search(rf"^\| {re.escape(field)} \|\s*(.*?)\s*\|$", text, re.MULTILINE)
    return match.group(1) if match else "TBD"


def approval_status(dtr: str, approval_type: str) -> str:
    matches = re.findall(
        rf"^\| (APR-[^|]+) \| {re.escape(approval_type)} \|[^|]*\|\s*([^|]+?)\s*\|",
        dtr,
        re.MULTILINE,
    )
    return matches[-1][1] if matches else "Missing"


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_id")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[4]
    project_dir = repo_root / "projects" / args.project_id
    context = (project_dir / "project-context.md").read_text(encoding="utf-8")
    dtr = (project_dir / "delivery-traceability-record.md").read_text(encoding="utf-8")
    stage = table_value(context, "Current lifecycle stage")
    requirements_status = approval_status(dtr, "Business Requirements Acceptance")
    uat_status = approval_status(dtr, "UAT Acceptance")
    security_status = approval_status(dtr, "Security Sign-off")
    completion_status = approval_status(dtr, "Project Completion Sign-off")
    release_count = sum(
        1
        for path in (project_dir / "releases").glob("*.md")
        if table_value(path.read_text(encoding="utf-8"), "Status") == "Released"
    )

    if stage == "3 of 7 — Business Requirements Approval" and requirements_status not in {
        "Approved",
        "Approved with exceptions",
    }:
        gate = f"BLOCKED — Business Requirements Acceptance is {requirements_status}"
        next_action = "Obtain Business Requirements Acceptance from the business owner."
    elif stage == "3 of 7 — Business Requirements Approval":
        gate = "CLEAR — requirements approval is recorded; advance to Delivery"
        next_action = "Update both stage fields to 4 of 7 — Delivery."
    elif stage == "6 of 7 — Completion Signoffs":
        missing = []
        if uat_status not in {"Approved", "Approved with exceptions"}:
            missing.append(f"UAT={uat_status}")
        if security_status not in {"Approved", "Approved with exceptions", "Not required"}:
            missing.append(f"Security={security_status}")
        if completion_status not in {"Approved", "Approved with exceptions"}:
            missing.append(f"Completion={completion_status}")
        gate = "BLOCKED — " + (", ".join(missing) if missing else "final reconciliation or DTR attachment remains")
        next_action = NEXT_ACTION[stage]
    elif stage == "1 of 7 — Intake":
        gate = "BLOCKED — intake or collateral copy is incomplete"
        next_action = NEXT_ACTION[stage]
    else:
        gate = "CLEAR — current stage may proceed"
        next_action = NEXT_ACTION.get(stage, "Correct the lifecycle stage value.")

    print(f"LIFECYCLE STATUS — {args.project_id}")
    print(f"Stage: {stage}")
    print(f"Gate: {gate}")
    print(f"Releases: {release_count} recorded; does not indicate project completion")
    print(f"Next: {next_action}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
