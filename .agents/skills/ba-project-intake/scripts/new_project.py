#!/usr/bin/env python3
"""Create the minimal local BA project workspace without overwriting existing work."""

from __future__ import annotations

import argparse
import re
import shutil
from datetime import date
from pathlib import Path


PROJECT_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")


def escape_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\r", " ").replace("\n", " ").strip()


def parse_team_member(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("team member must use ROLE=NAME format")
    left, right = (part.strip() for part in value.split("=", 1))
    if not left or not right:
        raise argparse.ArgumentTypeError("team member must include both role and name")
    return left, right


def project_context(args: argparse.Namespace, collateral_entries: list[str]) -> str:
    people: list[tuple[str, str, str]] = []
    if args.business_owner:
        people.append((args.business_owner, "Business / product owner", "Scope decisions and business approval"))
    for stakeholder in args.stakeholder:
        people.append((stakeholder, "Stakeholder", "Requirements input and review"))
    for role, name in args.team_member:
        people.append((name, role, "Delivery team resource"))

    people_rows = "\n".join(
        f"| {escape_cell(name)} | {escape_cell(role)} | {escape_cell(responsibility)} |"
        for name, role, responsibility in people
    ) or "| TBD | TBD | Confirm project participants and responsibilities. |"

    collateral_rows = "\n".join(
        f"| `{escape_cell(entry)}` | TBD | Review and classify | Original source or supplied copy |"
        for entry in collateral_entries
    ) or "| TBD | TBD | Obtain discovery collateral or requirement sources. | Not supplied at intake. |"

    return f"""# Project Context — {escape_cell(args.project_id)}

| Field | Value |
|---|---|
| Project ID | {escape_cell(args.project_id)} |
| Project title | {escape_cell(args.title or args.project_id)} |
| Project manager | {escape_cell(args.project_manager or 'TBD')} |
| BA / delivery lead | {escape_cell(args.ba_lead or 'TBD')} |
| Business owner / product owner | {escape_cell(args.business_owner or 'TBD')} |
| Status | Discovery |
| Last updated | {date.today().isoformat()} |

## Team delivery boundary

**Intended outcome:** TBD — determine from discovery collateral and stakeholder discussion.

- **Included:** TBD
- **Excluded / owned elsewhere:** TBD

## People

| Name | Role | Responsibility for this delivery |
|---|---|---|
{people_rows}

## Discovery collateral

| Source | Provided by / date | Relevant scope or requirement | Notes |
|---|---|---|---|
{collateral_rows}

## Dependencies, assumptions, and constraints

- None identified at intake.

## Open discovery questions

- [ ] Confirm the team's delivery boundary — Owner: {escape_cell(args.business_owner or 'TBD')}
"""


def replace_dtr_fields(text: str, args: argparse.Namespace) -> str:
    replacements = {
        "| Project ID | `<ID>` |": f"| Project ID | {escape_cell(args.project_id)} |",
        "| Delivery title | `<short name>` |": f"| Delivery title | {escape_cell(args.title or args.project_id)} |",
        "| Project manager | `<name>` |": f"| Project manager | {escape_cell(args.project_manager or 'TBD')} |",
        "| BA / delivery lead | `<name>` |": f"| BA / delivery lead | {escape_cell(args.ba_lead or 'TBD')} |",
        "| Business owner | `<name>` |": f"| Business owner | {escape_cell(args.business_owner or 'TBD')} |",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_id")
    parser.add_argument("--root", default="projects", help="Project workspace root (default: projects)")
    parser.add_argument("--title")
    parser.add_argument("--project-manager")
    parser.add_argument("--ba-lead")
    parser.add_argument("--business-owner")
    parser.add_argument("--stakeholder", action="append", default=[])
    parser.add_argument(
        "--team-member", action="append", default=[], type=parse_team_member, metavar="ROLE=NAME"
    )
    parser.add_argument("--collateral", action="append", default=[])
    parser.add_argument("--copy-collateral", action="store_true")
    args = parser.parse_args()

    if not PROJECT_ID_PATTERN.fullmatch(args.project_id):
        parser.error("project_id must be 1-64 letters, numbers, dots, underscores, or hyphens")

    repo_root = Path(__file__).resolve().parents[4]
    workspace_root = (repo_root / args.root).resolve()
    try:
        workspace_root.relative_to(repo_root)
    except ValueError:
        parser.error("root must resolve inside the lifecycle repository")
    project_dir = workspace_root / args.project_id
    if project_dir.exists():
        parser.error(f"workspace already exists: {project_dir}")

    project_dir.mkdir(parents=True)
    (project_dir / "collateral").mkdir()
    (project_dir / "releases").mkdir()

    collateral_entries: list[str] = []
    for supplied in args.collateral:
        source = Path(supplied).expanduser()
        if args.copy_collateral:
            if not source.is_file():
                parser.error(f"collateral is not a readable file: {source}")
            destination = project_dir / "collateral" / source.name
            if destination.exists():
                parser.error(f"duplicate collateral filename: {source.name}")
            shutil.copy2(source, destination)
            collateral_entries.append(destination.relative_to(project_dir).as_posix())
        else:
            collateral_entries.append(supplied)

    templates = repo_root / "templates"
    (project_dir / "project-context.md").write_text(
        project_context(args, collateral_entries), encoding="utf-8"
    )
    dtr = (templates / "delivery-traceability-record.md").read_text(encoding="utf-8")
    (project_dir / "delivery-traceability-record.md").write_text(
        replace_dtr_fields(dtr, args), encoding="utf-8"
    )
    for template_name, output_name in (
        ("backlog.md", "backlog.md"),
        ("change-log.md", "change-log.md"),
    ):
        content = (templates / template_name).read_text(encoding="utf-8")
        content = content.replace("<Project ID>", escape_cell(args.project_id))
        (project_dir / output_name).write_text(content, encoding="utf-8")

    print(project_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
