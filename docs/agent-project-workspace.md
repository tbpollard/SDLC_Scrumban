# Agent Project Workspace

The BA skills use a small local workspace while Jira, GitHub, and central project-system integrations are unavailable.

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

## Record ownership

| File | Purpose |
|---|---|
| `project-context.md` | People, team boundary, source inventory, dependencies, and unresolved discovery questions. |
| `delivery-traceability-record.md` | Compact summary attached to the central project record. |
| `backlog.md` | Local Jira-ready epic and story drafts with stable requirement and acceptance-criteria IDs. |
| `jira-backlog.csv` | Deterministically generated Jira import containing the Epic, stories, and tasks. |
| `jira-id-map.csv` | Stable local IDs mapped to Jira keys after a Jira export is supplied. |
| `change-log.md` | Index of material requirement changes while operating locally. |
| `validation.md` | Project-level acceptance-criteria validation and UAT result, independent of release count. |
| `collateral/` | Required local copies of every user-supplied file and evidence artifact. |
| `releases/<release-id>.md` | Repository, tag/version, date, change ticket, scope, and evidence for one deployment. |

Do not add another record when one of these can hold the information. Large evidence files may remain elsewhere and be linked.

## Traceability identifiers

Use stable local IDs until Jira IDs exist:

- Requirements: `REQ-001`, `REQ-002`, ...
- Acceptance criteria: `AC-001-01`, `AC-001-02`, ...
- Material changes: `CHG-001`, `CHG-002`, ...
- Implementation tasks: `TSK-001`, `TSK-002`, ...
- Releases: `REL-001`, `REL-002`, ...
- Approvals: `APR-REQ-001`, `APR-UAT-001`, `APR-SEC-001`, `APR-COMP-001`, ...

Never renumber an existing ID. When Jira items are created, add their keys beside the local IDs instead of replacing the local IDs.

## Source of truth

In local-only mode, this project workspace is the working record. After content is entered in Jira, Jira becomes authoritative for detailed requirements, acceptance criteria, status, and routine history. The DTR remains the cross-system index.

Everything under `projects/` is working output and must remain outside version control. The repository's `.gitignore` excludes the entire folder. Do not force-add project Markdown or collateral. Attach the completed DTR to the central project record and place other evidence in its appropriate governed system.

Never invent a stakeholder decision, test result, Jira key, pull request, GitHub release, or approval. Use `Pending`, `Not run`, or `TBD`, and identify the needed owner or evidence.

## Updating the workspace

- Preserve user-supplied content and distinguish facts from BA inferences.
- Copy every user-supplied file to `collateral/` and reference the relative copy.
- Keep the DTR concise; put detail in the other workspace files.
- Use one release record per actual or planned deployment and require a change ticket for an actual release.
- Reflect material changes in `change-log.md`, affected backlog items, and the DTR summary.
- Close team scope only when every item is delivered, transferred, cancelled, or explicitly deferred with an owner.
- Follow the [agent output contract](agent-output-contract.md) for lifecycle gates, approvals, status display, and deterministic formatting.
