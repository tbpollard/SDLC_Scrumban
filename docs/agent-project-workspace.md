# Agent Project Workspace

The BA skills use a small local workspace while Jira, GitHub, and central project-system integrations are unavailable.

```text
projects/<Project ID>/
├── project-context.md
├── delivery-traceability-record.md
├── backlog.md
├── change-log.md
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
| `change-log.md` | Index of material requirement changes while operating locally. |
| `collateral/` | Optional copies of supplied source files. Referencing originals is also acceptable. |
| `releases/<release-id>.md` | Scope, validation evidence, approval, and GitHub reference for one release. |

Do not add another record when one of these can hold the information. Large evidence files may remain elsewhere and be linked.

## Traceability identifiers

Use stable local IDs until Jira IDs exist:

- Requirements: `REQ-001`, `REQ-002`, ...
- Acceptance criteria: `AC-001-01`, `AC-001-02`, ...
- Material changes: `CHG-001`, `CHG-002`, ...

Never renumber an existing ID. When Jira items are created, add their keys beside the local IDs instead of replacing the local IDs.

## Source of truth

In local-only mode, this project workspace is the working record. After content is entered in Jira, Jira becomes authoritative for detailed requirements, acceptance criteria, status, and routine history. The DTR remains the cross-system index.

The Markdown project records may be version-controlled for local history. Copied files under `projects/*/collateral/` are ignored by Git by default because source collateral may be sensitive or already governed elsewhere.

Never invent a stakeholder decision, test result, Jira key, pull request, GitHub release, or approval. Use `Pending`, `Not run`, or `TBD`, and identify the needed owner or evidence.

## Updating the workspace

- Preserve user-supplied content and distinguish facts from BA inferences.
- Prefer links and short citations to copied source text.
- Keep the DTR concise; put detail in the other workspace files.
- Use one release record per planned or actual release.
- Reflect material changes in `change-log.md`, affected backlog items, and the DTR summary.
- Close team scope only when every item is delivered, transferred, cancelled, or explicitly deferred with an owner.
