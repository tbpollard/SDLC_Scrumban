# Delivery Traceability Record — Employee Enrollment

| Field | Value |
|---|---|
| Project ID | PRJ-1042 |
| Delivery title | Employee enrollment — portal component |
| Status | Complete |
| Current lifecycle stage | 7 of 7 — Complete |
| Project manager | Morgan Lee |
| BA / delivery lead | Avery Chen |
| Business owner | Jordan Smith, Benefits Operations |
| Jira epic(s) | BEN-120 Employee enrollment portal |
| Code repositories | Multiple; see release register |

## Team delivery boundary

**Outcome:** Deliver the portal functions that allow authorized HR administrators to create employees and issue enrollment invitations. The central Identity team owns account provisioning and authentication changes.

**Included:** Employee data entry, validation, invitation request, and audit event.  
**Excluded / owned elsewhere:** Authentication and identity provisioning — Identity team; enrollment-plan selection — Benefits Platform team.  
**Source requirements:** `collateral/process-notes.md`, `collateral/enrollment-mockup-v3.png`, and Jira epic BEN-120.

## Approval ledger

| ID | Approval type | Applies to | Status | Approver / date | Collateral type | Evidence |
|---|---|---|---|---|---|---|
| APR-REQ-001 | Business Requirements Acceptance | REQ-001–REQ-006 baseline dated 2026-05-20 | Approved | Jordan Smith / 2026-05-20 | Jira approval export | `collateral/requirements-approval.csv` |
| APR-REQ-002 | Business Requirements Acceptance | REQ-001–REQ-006 baseline after CHG-001 | Approved | Jordan Smith / 2026-06-04 | Email | `collateral/requirements-reapproval.msg` |
| APR-UAT-001 | UAT Acceptance | Final delivered REQ-001–REQ-006 | Approved | Jordan Smith / 2026-06-20 | UAT summary and email | `collateral/uat-acceptance.pdf` |
| APR-SEC-001 | Security Sign-off | Portal and API changes | Approved | Riley Patel / 2026-06-18 | Security review ticket | `collateral/SEC-2217.pdf` |
| APR-COMP-001 | Project Completion Sign-off | Team delivery completion | Approved | Jordan Smith / 2026-06-24 | Email | `collateral/project-completion.msg` |

## Material requirement changes

| ID | Date | Change and reason | Affected Jira / release | Decision / approver |
|---|---|---|---|---|
| CHG-001 | 2026-06-03 | Invitation expiry changed from 48 hours to 72 hours to match policy BEN-14. | BEN-138 / REL-002 | Approved — Jordan Smith; renewed requirements approval recorded in APR-REQ-002 |
| CHG-002 | 2026-06-10 | Bulk upload moved to a later project phase due to an external dependency. | BEN-151 / deferred | Approved — Morgan Lee and Jordan Smith |

## Release register

| Release ID | Repository | Tag / version | Production date | Change ticket | Delivered Jira / REQ scope | Evidence |
|---|---|---|---|---|---|---|
| REL-001 | `example-org/enrollment-portal` | v1.0.0 | 2026-05-29 | CHG0011012 | BEN-131, BEN-132 / REQ-001–REQ-003 | `releases/REL-001.md` |
| REL-002 | `example-org/enrollment-api` | v1.1.0 | 2026-06-12 | CHG0011477 | BEN-138, BEN-145 / REQ-004–REQ-006 | `releases/REL-002.md` |

## Completion

- **Disposition:** All committed team scope delivered; bulk upload returned to project intake with an owner.
- **Open items and owner:** BEN-151 — Morgan Lee to coordinate a future phase.
- **DTR attached to project record:** 2026-06-24.
