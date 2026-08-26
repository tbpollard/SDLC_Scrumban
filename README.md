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

## Ground rules

- Document only the scope assigned to this team.
- Use acceptance criteria as the connection between requirements and testing.
- Reference stakeholder documents instead of copying them.
- Record material requirement changes; rely on Jira history for routine clarifications.
- Record every production release that delivers part of the team's scope.
- Add documentation only when risk, complexity, policy, or regulation requires it.

