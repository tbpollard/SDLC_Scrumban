# Delivery Traceability Record

> Keep this record concise. Link to detail in Jira, GitHub, and source documents instead of copying it here.

| Field | Value |
|---|---|
| Project ID | `<ID>` |
| Delivery title | `<short name>` |
| Status | `Discovery / Active / Complete / Cancelled / Transferred` |
| Current lifecycle stage | 1 of 7 — Intake |
| Project manager | `<name>` |
| BA / delivery lead | `<name>` |
| Business owner | `<name>` |
| Jira epic(s) | `<links>` |
| Code repositories | `<links or see release register>` |

## Team delivery boundary

**Outcome:** `<one or two sentences describing what this team will deliver>`

**Included:** `<short list or Jira link>`  
**Excluded / owned elsewhere:** `<short list, owner, or N/A>`  
**Source requirements:** `<relative collateral paths and Jira references>`

## Approval ledger

| ID | Approval type | Applies to | Status | Approver / date | Collateral type | Evidence |
|---|---|---|---|---|---|---|
| APR-REQ-001 | Business Requirements Acceptance | `<scope and REQ/AC baseline>` | Pending | `<name / date>` | `<email, Jira approval, meeting decision, signed document>` | `collateral/<file or TBD>` |
| APR-UAT-001 | UAT Acceptance | `<final delivered scope>` | Pending | `<name / date>` | `<UAT summary, email, Jira approval, signed document>` | `collateral/<file or TBD>` |
| APR-SEC-001 | Security Sign-off | `<applicable solution scope>` | Pending | `<name / date>` | `<security review, email, ticket, scan report, or N/A rationale>` | `collateral/<file or TBD>` |
| APR-COMP-001 | Project Completion Sign-off | `<team delivery completion>` | Pending | `<name / date>` | `<email, Jira approval, meeting decision, signed document>` | `collateral/<file or TBD>` |

## Material requirement changes

> Omit this section if there were none. Routine clarifications remain in Jira history.

| ID | Date | Change and reason | Affected Jira / release | Decision / approver |
|---|---|---|---|---|
| CHG-01 | `<date>` | `<brief description>` | `<links or keys>` | `<approved, rejected, deferred; name>` |

## Release register

> Releases are independent of project completion. Use one row per deployment from each repository.

| Release ID | Repository | Tag / version | Production date | Change ticket | Delivered Jira / REQ scope | Evidence |
|---|---|---|---|---|---|---|
| `<REL-001>` | `<repository>` | `<tag or version>` | `<date>` | `<change ticket>` | `<keys / REQ IDs>` | `releases/<release-id>.md` |

## Completion

**Disposition:** `<all team scope delivered / remaining work transferred / cancelled / deferred>`  
**Open items and owner:** `<links and owner, or none>`  
**DTR attached to project record:** `<date or link>`
