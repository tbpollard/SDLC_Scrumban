# Lightweight Delivery Lifecycle

This repository defines a minimal, auditable lifecycle for software work delivered by our team. It applies whether the team owns an entire project or only one portion of it.

The lifecycle creates one traceability chain:

**Project ID → Team scope → Jira work → Requirements → Validation → Approval → GitHub release(s)**

## Required records

Only three records are required:

1. **Jira epic and stories** — detailed scope, requirements, acceptance criteria, work status, and native change history.
2. **Delivery Traceability Record (DTR)** — a one-page summary attached to the central project record.
3. **Linked evidence** — test results, stakeholder approval, and one or more GitHub releases referenced from the DTR or Jira.

Do not recreate information in multiple places. Link to the authoritative record whenever possible.

## Lifecycle

| Stage | Minimum outcome |
|---|---|
| 1. Intake | Project ID and team contact are known. |
| 2. Define | The team's scope, exclusions, stakeholders, and source requirements are recorded. |
| 3. Refine | Jira work has testable acceptance criteria and is ready for development. |
| 4. Build | Development is linked to Jira and follows the team's GitHub workflow. |
| 5. Validate | Acceptance criteria are tested; exceptions are recorded. |
| 6. Approve & release | The stakeholder accepts the delivered scope and the GitHub release is linked. |

A project may pass through Build–Validate–Approve multiple times when delivery uses multiple releases.

## Start here

- [Operating guide](docs/operating-guide.md)
- [Jira requirements guide](docs/jira-requirements-guide.md)
- [Delivery Traceability Record template](templates/delivery-traceability-record.md)
- [Completed example](examples/delivery-traceability-record-example.md)
- [Agent project workspace](docs/agent-project-workspace.md)

## BA agent skills

The repository includes a local-filesystem skill set under `.agents/skills`:

- `ba-delivery-lifecycle` — coordinates the lifecycle and selects the next stage.
- `ba-project-intake` — creates a project workspace from the Project ID, people, and collateral.
- `ba-requirements-backlog` — turns discovery inputs into scoped, Jira-ready requirements and acceptance criteria.
- `ba-requirement-change` — assesses and records requirement changes.
- `ba-validation-signoff` — prepares validation by release and records actual results and approval.
- `ba-release-closure` — traces GitHub releases and closes or transfers the team's scope.

Invoke the coordinator for end-to-end work or a stage skill for a focused update. The skills use `projects/<Project ID>/` and do not require Jira or GitHub connectivity.

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

The coordinator will inspect the available information, initialize `projects/PRJ-1042/`, complete the current lifecycle stage, and identify the smallest next action. It will not mark testing, approval, or release complete without evidence.

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

Reference the collateral in its current location; do not copy it.
```

#### Create Jira-ready requirements

```text
Use $ba-requirements-backlog for PRJ-1042. Review the project context and
discovery collateral, then draft the team-owned epic, requirements, stories,
and acceptance criteria. Clearly separate Identity-team work and list any
questions that prevent a story from being Ready.
```

The output remains local until someone enters it in Jira. Add Jira keys to the local requirement IDs afterward; do not replace the stable `REQ` and `AC` IDs.

#### Assess a requirement change

```text
Use $ba-requirement-change for PRJ-1042.

The product owner requested that enrollment invitations expire after 72 hours
instead of 48 hours. This affects REQ-003 and release v1.1.0. Record the change,
identify testing and approval impacts, and leave the decision pending until
Jordan Smith confirms it.
```

Routine wording clarifications update the backlog only. Material changes receive a `CHG` ID and are reflected in the backlog, change log, DTR, and affected release validation.

#### Plan validation or record signoff

```text
Use $ba-validation-signoff for PRJ-1042 release v1.1.0. Build the validation
record from the acceptance criteria assigned to this release. The tests have
not run yet, so leave results as Not run and draft a concise UAT request for
Jordan Smith.
```

After testing:

```text
Use $ba-validation-signoff for PRJ-1042 release v1.1.0. Update the release
record using C:\test-evidence\PRJ-1042\v1.1.0-results.md and the approval email
saved at C:\approvals\PRJ-1042-v1.1.0.txt. Record only results and approval
that those files support.
```

#### Record a release or assess closure

```text
Use $ba-release-closure for PRJ-1042. Release v1.1.0 was published as GitHub
tag v1.1.0 on 2026-09-18. Reconcile it with the backlog and validation record,
update the DTR, and tell me whether our team-owned scope can close. Do not close
the project if any requirement lacks a final disposition.
```

Multiple releases are added as separate records under `projects/<Project ID>/releases/` and as separate rows in the DTR.

### Expected local output

After intake, the project workspace contains:

```text
projects/<Project ID>/
├── project-context.md
├── delivery-traceability-record.md
├── backlog.md
├── change-log.md
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
