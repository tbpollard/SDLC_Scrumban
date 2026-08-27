# SharePoint document-library repository contract

Use a single configured SharePoint document library as the working repository. Do not use SharePoint lists. Configure the site URL, library identifier, and `Projects` root folder as environment variables or fixed tool inputs rather than asking end users for internal IDs.

## Fixed project workspace

Maintain exactly the same project structure as the repository's original filesystem skills:

```text
Projects/<Project ID>/
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

Do not create other top-level project artifacts unless project-specific risk or policy justifies one. Use the bundled templates without renaming headings, columns, fields, or allowed status values.

## Artifact ownership

| Artifact | Purpose |
|---|---|
| `project-context.md` | People, team boundary, source inventory, dependencies, assumptions, constraints, and discovery questions. |
| `delivery-traceability-record.md` | Concise cross-system lifecycle summary attached or linked to the central project record. |
| `backlog.md` | Jira-ready Epic, requirements, acceptance criteria, and implementation tasks with stable IDs. |
| `jira-backlog.csv` | Current deterministic Jira import file. |
| `jira-id-map.csv` | Stable local IDs mapped to Jira keys after a retained Jira export is supplied. |
| `change-log.md` | Material requirement-change index. Routine clarification history remains in Jira after migration. |
| `validation.md` | Project-level acceptance-criteria results and UAT outcome, independent of release count. |
| `collateral/` | Retained copies of every user-supplied source and evidence artifact. |
| `releases/<release-id>.md` | One independent planned or actual deployment record. |

SharePoint version history provides recovery and file-level audit history. It does not replace explicit approval, validation, change, or release evidence.

## Templates

Skill packages include these files under `templates/`:

- `project-context.md`
- `delivery-traceability-record.md`
- `backlog.md`
- `change-log.md`
- `validation.md`
- `release-record.md`

At initialization, render every canonical project file from its template. Create `jira-backlog.csv` and `jira-id-map.csv` with their required headers. Replace template placeholders only with supported facts, `TBD`, `Pending`, or `Not run`.

## Collateral handling

Copy every supplied file, conversation attachment, approval artifact, Jira export, test result, and deployment record into `collateral/` before analysis or citation.

- Prefer a source already in SharePoint or OneDrive and copy it into the project folder.
- Preserve filenames when possible. If a different file already has that name, add a deterministic content-hash suffix; do not overwrite it.
- Skip a duplicate only when its content is identical.
- Record project-relative `collateral/...` paths in Markdown records. A SharePoint URL may accompany the relative path.
- If the agent cannot transfer a supplied file, keep Stage 1 or the affected approval gate blocked and identify the required upload action.

## Traceability identifiers

Use stable IDs until and after Jira IDs exist:

- requirements: `REQ-001`, `REQ-002`, ...
- acceptance criteria: `AC-001-01`, `AC-001-02`, ...
- implementation tasks: `TSK-001`, `TSK-002`, ...
- material changes: `CHG-001`, `CHG-002`, ...
- releases: `REL-001`, `REL-002`, ...
- approvals: `APR-REQ-001`, `APR-UAT-001`, `APR-SEC-001`, `APR-COMP-001`, ...

Never renumber an existing ID. Add Jira keys beside stable IDs, never in place of them.

## Jira CSV contract

`jira-backlog.csv` is UTF-8 and uses this exact header order:

```text
Work item ID,Work type,Summary,Description,Parent,Labels
```

The Epic row appears first, followed by requirements or stories, then implementation tasks. Stories and Tasks use the Epic as their Jira parent; each Task retains its related `REQ` ID in Description. Include acceptance criteria in Description and stable IDs in square brackets in Summary. Regenerate the complete canonical file after a backlog change; never patch individual CSV rows without validating the whole output.

`jira-id-map.csv` maps stable local IDs to Jira keys and records the retained source export. Never invent a Jira key or claim an import occurred.

## Required tool capabilities

The agent needs SharePoint connector actions or workflows whose descriptions clearly expose these capabilities:

- resolve the configured site, document library, project folder, and child paths;
- list folders and files and retrieve file metadata, including version, ETag, or last-modified data;
- read text and binary file content;
- create folders without accepting SharePoint's duplicate-name suffix as success;
- create and update canonical text or CSV files;
- copy or upload source files into `collateral/`; and
- create release Markdown files under `releases/`.

Recommended workflows:

1. `Read lifecycle workspace` — returns the canonical text files, child-file inventories, file URLs, and version tokens for one exact Project ID.
2. `Initialize lifecycle workspace` — creates the exact folder structure and canonical files from supplied content only when the Project ID folder does not exist.
3. `Update lifecycle files` — conditionally replaces the full content of named canonical files and returns new URLs and versions; rejects stale versions and paths outside the selected project.
4. `Store lifecycle collateral` — copies or uploads a supplied file, detects identical duplicates and filename collisions, and returns the retained relative path and SharePoint URL.

Power Platform SharePoint connector actions such as Get file content, Get file metadata using path, Create file, Update file, List folder, and Copy file can be composed into these workflows. Knowledge access is not a substitute for write tools.

## Consistency checks

Before and after writes, verify:

- exactly one project folder exists for the Project ID;
- all required canonical files and folders exist;
- template headings and field order are preserved;
- stage values match in project context and the DTR;
- stable IDs are unique, sorted, and never renumbered;
- relative evidence paths resolve under the same project's `collateral/` folder;
- backlog, Jira CSV, Jira map, change log, validation, releases, and DTR agree;
- current requirements and approval baselines agree;
- validation covers applicable acceptance criteria;
- actual releases contain every mandatory field; and
- closure conditions and the DTR's central-record attachment or link are complete.
