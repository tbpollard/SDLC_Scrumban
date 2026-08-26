# Agent Output Contract

All BA skills must follow this contract so project output remains consistent across models and sessions.

## Fixed project structure

```text
projects/<Project ID>/
├── project-context.md
├── delivery-traceability-record.md
├── backlog.md
├── jira-backlog.csv
├── jira-id-map.csv
├── change-log.md
├── validation.md
├── collateral/
└── releases/
    └── <release-id>.md
```

Do not create additional top-level project records unless a policy or project-specific risk requires one. Preserve the headings, tables, field order, identifiers, and allowed status values defined by the repository templates.

## Collateral rule

Every user-supplied file—including files attached to the conversation, approval evidence, test results, Jira exports, and release evidence—must be copied into `projects/<Project ID>/collateral/` before it is analyzed or referenced in a project record.

Use the intake skill's `scripts/copy_collateral.py` helper. It accepts files or directories, preserves directory contents, skips identical duplicates, and assigns a deterministic hash suffix when different files have the same name. Project records must use paths relative to the project folder.

If a supplied file cannot be materialized locally, keep the project at Stage 1 and report the missing copy as a blocker. A web link may be recorded as a source, but it does not satisfy the copy requirement for a user-supplied file.

## Lifecycle stages

Use exactly one of these values in `project-context.md` and the DTR:

| Stage | Entry and exit rule |
|---|---|
| `1 of 7 — Intake` | Project inputs or collateral copies are incomplete. Exit when supplied collateral is copied and people/source inventory is usable. |
| `2 of 7 — Discovery & Requirements` | Team boundary, requirements, acceptance criteria, and Jira CSV are being prepared. Exit when the backlog meets Ready and unresolved scope questions are closed. |
| `3 of 7 — Business Requirements Approval` | The requirements baseline is ready but current Business Requirements Acceptance is pending. This is a hard gate. |
| `4 of 7 — Delivery` | Current Business Requirements Acceptance is approved and work is being implemented. Releases may occur during this or later stages without completing the project. |
| `5 of 7 — Validation` | Delivered team scope is being validated against acceptance criteria. Exit when final-scope validation is complete and UAT Acceptance is recorded. |
| `6 of 7 — Completion Signoffs` | UAT is accepted; Security Sign-off is approved or documented as not required; final dispositions and Project Completion Sign-off are pending. |
| `7 of 7 — Complete` | All team scope has a final disposition, all required approvals are current, the DTR is attached to the central project record, and Project Completion Sign-off is approved. |

A material requirement change invalidates Business Requirements Acceptance when it changes the approved baseline. Move the project back to Stage 3 until renewed approval is recorded. A release never advances the lifecycle stage by itself.

## Required approval ledger

The DTR must always contain these approval types:

1. Business Requirements Acceptance — required before Stage 4.
2. UAT Acceptance — required before Stage 6 and must cover final delivered scope.
3. Security Sign-off — record `Approved` when required or `Not required` with rationale and decision evidence.
4. Project Completion Sign-off — required for Stage 7.

Every approval row identifies its scope, status, approver/date, collateral type, and relative evidence path. Valid statuses are `Pending`, `Approved`, `Approved with exceptions`, `Rejected`, `Superseded`, and `Not required`.

## Release records

Releases are deployment events, not project-completion approvals. A project may contain any number of releases from any number of repositories before completion.

Each actual release must record:

- stable release ID;
- repository;
- tag or version;
- production date;
- change-management ticket number;
- delivered requirement/Jira scope; and
- deployment evidence.

Do not record an actual release without its change-management ticket. Do not require UAT or Project Completion Sign-off merely to record a release; separately record any control that was required for that deployment.

## Jira CSV contract

`jira-backlog.csv` uses this exact header order:

```text
Work item ID,Work type,Summary,Description,Parent,Labels
```

The Epic row appears first, followed by requirements/stories, then implementation tasks. Stories and Tasks use the Epic as their Jira parent; each Task retains its related `REQ` ID in Description. `Summary` contains the stable local ID in brackets. Acceptance criteria are included in `Description`, avoiding reliance on a Jira custom field. Use the repository renderer rather than composing CSV manually.

When a Jira export is supplied, copy it to collateral first, then use the linkage helper to create `jira-id-map.csv` and add Jira keys beside—not in place of—the stable local IDs.

## Required status display

Every substantive skill response must prominently include this block using current project data:

```text
LIFECYCLE STATUS — <Project ID>
Stage: <n of 7 — Stage name>
Gate: <CLEAR, BLOCKED, or NOT APPLICABLE — short reason>
Releases: <count recorded; does not indicate project completion>
Next: <smallest required action and owner>
```

Show the status after inspecting the project and again after any update if the stage or gate changed.

## Consistency rules

- Use repository templates without renaming headings or columns.
- Use stable IDs: `REQ-nnn`, `AC-nnn-nn`, `TSK-nnn`, `CHG-nnn`, `REL-nnn`, `APR-REQ-nnn`, `APR-UAT-nnn`, `APR-SEC-nnn`, and `APR-COMP-nnn`.
- Never renumber an existing ID.
- Use ISO dates (`YYYY-MM-DD`).
- Use `TBD`, `Pending`, or `Not run` instead of guessing.
- Sort requirements, tasks, changes, and releases by stable ID. Keep approval types in lifecycle order and multiple approvals of the same type in numeric order.
- Update the current stage in both project context and DTR in the same turn.
- Run the project checker after changing project records.
- Never stage, commit, or force-add anything under `projects/`.
