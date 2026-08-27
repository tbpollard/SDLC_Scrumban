# Lightweight Delivery Lifecycle

This repository defines a minimal, auditable lifecycle for software work delivered by our team. It applies whether the team owns an entire project or only one portion of it.

The lifecycle creates one traceability chain:

**Project ID → Copied collateral → Requirements → Requirements approval → Delivery → Validation → Completion signoffs**

## Required records

Only three records are required:

1. **Jira epic and stories** — detailed scope, requirements, acceptance criteria, work status, and native change history.
2. **Delivery Traceability Record (DTR)** — a one-page summary attached to the central project record.
3. **Linked evidence** — test results, stakeholder approval, and one or more GitHub releases referenced from the DTR or Jira.

Do not recreate information in multiple places. Link to the authoritative record whenever possible.

## Lifecycle

| Stage | Minimum outcome |
|---|---|
| 1. Intake | Supplied collateral is copied and the people/source inventory is usable. |
| 2. Discovery & Requirements | Team scope, acceptance criteria, and Jira import CSV are Ready. |
| 3. Business Requirements Approval | The business owner approves the current requirements baseline. This is a hard gate. |
| 4. Delivery | Approved scope is implemented; any number of releases may be recorded. |
| 5. Validation | Final delivered scope is tested against acceptance criteria. |
| 6. Completion Signoffs | UAT, Security disposition, final reconciliation, and completion approval are recorded. |
| 7. Complete | The DTR is attached and all team scope has a final disposition. |

Releases are independent deployment events. A project may have multiple releases from multiple repositories before project completion, and each actual release records its change-management ticket.

## Start here

- [Operating guide](docs/operating-guide.md)
- [Jira requirements guide](docs/jira-requirements-guide.md)
- [Delivery Traceability Record template](templates/delivery-traceability-record.md)
- [Completed example](examples/delivery-traceability-record-example.md)
- [Agent project workspace](docs/agent-project-workspace.md)
- [Agent output contract](docs/agent-output-contract.md)

## BA agent skills

The repository includes a local-filesystem skill set under `.agents/skills`:

- `ba-delivery-lifecycle` — coordinates the lifecycle and selects the next stage.
- `ba-project-intake` — creates a project workspace from the Project ID, people, and collateral.
- `ba-requirements-backlog` — creates the fixed backlog and Jira CSV, links returned Jira IDs, and records requirements approval.
- `ba-requirement-change` — assesses and records requirement changes.
- `ba-validation-signoff` — manages project-level validation, UAT Acceptance, and Security Sign-off.
- `ba-release-closure` — records independent releases with change tickets or completes final project closure.

Invoke the coordinator for end-to-end work or a stage skill for a focused update. The skills use `projects/<Project ID>/` and do not require Jira or GitHub connectivity.

### Microsoft Copilot Studio variation

A SharePoint-backed variation for the Microsoft Copilot Studio Agents Experience is available under [copilot-studio](copilot-studio/setup-guide.md). It includes copy-ready agent instructions, six uploadable skill packages, the original Markdown templates, a SharePoint document-library contract, and configuration guidance. This variation maintains the same project artifacts in `Projects/<Project ID>/` within SharePoint rather than on a local filesystem.

### Quick start

For a new project, invoke `ba-delivery-lifecycle` and provide whatever source information is currently available. The Project ID is the only value required to create the workspace; missing details remain `TBD` rather than being invented.

```text
Use $ba-delivery-lifecycle to begin this project.

Project ID: PRJ-1042
Product owner: Jordan Smith
Stakeholders: Morgan Lee (Project Manager), Riley Patel (Operations)
Team: Avery Chen (BA), Sam Rivera (Developer), Taylor Kim (DBA)
Discovery collateral:
- C:\project-intake\PRJ-1042\process-notes.md
- C:\project-intake\PRJ-1042\enrollment-mockup.png

Our team owns the employee-enrollment portal changes. Identity and
authentication changes are owned by another team.
```

The coordinator will copy the supplied files into `projects/PRJ-1042/collateral/`, initialize the workspace, complete the current lifecycle stage, and identify the smallest next action. It will not advance past Business Requirements Approval or mark testing, signoffs, or releases complete without evidence.

Every skill response displays a consistent status block:

```text
LIFECYCLE STATUS — PRJ-1042
Stage: 3 of 7 — Business Requirements Approval
Gate: BLOCKED — Business Requirements Acceptance is Pending
Releases: 1 recorded; does not indicate project completion
Next: Obtain Business Requirements Acceptance from the business owner.
```

You do not need to invoke every stage skill manually. Continue using the coordinator as the project progresses:

```text
Use $ba-delivery-lifecycle for PRJ-1042. Review the existing project
workspace, summarize its current status, and complete the next BA step using
the new stakeholder notes in C:\project-intake\PRJ-1042\meeting-2026-09-03.md.
```

### Stage-specific examples

Use a focused skill when you already know which lifecycle activity is needed.

#### Initialize or update intake

```text
Use $ba-project-intake to initialize PRJ-1042.

Product owner: Jordan Smith
Stakeholders: Riley Patel and Morgan Lee
Team: Avery Chen (BA), Sam Rivera (Developer), Taylor Kim (DBA),
Casey Jones (Cloud Engineer)
Collateral: C:\project-intake\PRJ-1042\

Copy every supplied file into the project collateral folder before using it.
```

#### Create Jira-ready requirements

```text
Use $ba-requirements-backlog for PRJ-1042. Review the copied collateral, then
create the team-owned epic, requirements, stories, implementation tasks, and
acceptance criteria using the fixed template. Generate jira-backlog.csv and
move the project to Business Requirements Approval when the backlog is Ready.
Clearly separate Identity-team work.
```

Import `jira-backlog.csv` through Jira's CSV importer, map `Work item ID`, `Work type`, `Summary`, `Description`, `Parent`, and `Labels`, then use Jira's Validate action before import. The Epic appears before its children and acceptance criteria are included in Description.

After import, export the created Jira work and provide the CSV back to the skill:

```text
Use $ba-requirements-backlog for PRJ-1042. Copy this Jira export into project
collateral, create jira-id-map.csv, and link the Jira keys to the stable local
IDs: C:\jira-exports\PRJ-1042-created-work.csv
```

Business Requirements Acceptance is required before Delivery:

```text
Use $ba-requirements-backlog for PRJ-1042. Record Jordan Smith's Business
Requirements Acceptance from C:\approvals\PRJ-1042-requirements-email.msg.
It covers REQ-001 through REQ-006 and their current acceptance criteria.
Advance the lifecycle only if the evidence contains an explicit approval.
```

#### Assess a requirement change

```text
Use $ba-requirement-change for PRJ-1042.

The product owner requested that enrollment invitations expire after 72 hours
instead of 48 hours. This affects REQ-003 and release v1.1.0. Record the change,
identify testing and approval impacts, and leave the decision pending until
Jordan Smith confirms it.
```

Routine wording clarifications update the backlog only. Material changes receive a `CHG` ID and are reflected in the backlog, Jira CSV, change log, DTR, and project validation. A changed approved baseline returns to Stage 3 for renewed requirements approval.

#### Plan validation or record signoff

```text
Use $ba-validation-signoff for PRJ-1042. Build project-level validation.md from
the final delivered acceptance criteria. The tests have not run yet, so leave
results as Not run and draft a concise UAT request for Jordan Smith.
```

After testing:

```text
Use $ba-validation-signoff for PRJ-1042. Copy and apply the test results,
UAT-acceptance email, and Security approval below. Record the collateral type,
approver, date, scope, and relative evidence path for each approval. If
Security is not required, record the decision and rationale rather than
assuming N/A.

- C:\test-evidence\PRJ-1042-results.md
- C:\approvals\PRJ-1042-uat.txt
- C:\approvals\PRJ-1042-security.txt
```

#### Record a release or assess closure

```text
Use $ba-release-closure for PRJ-1042. Record release REL-002 from repository
https://github.example.com/payments/api, tag v1.1.0, deployed 2026-09-18 under
change ticket CHG0098123. It delivered REQ-003, REQ-004, and TSK-006. Copy the
deployment evidence from C:\changes\CHG0098123.pdf. Do not change the project
lifecycle stage solely because this release occurred.
```

Multiple releases from multiple repositories are added as separate records under `projects/<Project ID>/releases/` and as separate rows in the DTR.

For project completion:

```text
Use $ba-release-closure for PRJ-1042 to assess project completion. Reconcile
all team scope, verify requirements approval, final UAT acceptance, Security
disposition, release change tickets, and DTR attachment. Record Project
Completion Sign-off from C:\approvals\PRJ-1042-completion-email.msg only if it
explicitly approves completion.
```

### Expected local output

After intake, the project workspace contains:

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
```

Everything under `projects/` is local working output and is ignored by Git. Audit evidence belongs in Jira, GitHub releases, linked evidence repositories, and the DTR attached to the central project record—not in this framework repository. See the [agent project workspace](docs/agent-project-workspace.md) for record ownership and traceability conventions.

## Ground rules

- Document only the scope assigned to this team.
- Use acceptance criteria as the connection between requirements and testing.
- Reference stakeholder documents instead of copying them.
- Record material requirement changes; rely on Jira history for routine clarifications.
- Record every production release that delivers part of the team's scope.
- Add documentation only when risk, complexity, policy, or regulation requires it.
