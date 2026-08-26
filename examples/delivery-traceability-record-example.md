# Delivery Traceability Record — Employee Enrollment

| Field | Value |
|---|---|
| Project ID | PRJ-1042 |
| Delivery title | Employee enrollment — portal component |
| Status | Complete |
| Project manager | Morgan Lee |
| BA / delivery lead | Avery Chen |
| Business owner | Jordan Smith, Benefits Operations |
| Jira epic(s) | ENR-120 Employee enrollment portal |
| GitHub repository | `example-org/enrollment-portal` |

## Team delivery boundary

**Outcome:** Deliver the portal functions that allow authorized HR administrators to create employees and issue enrollment invitations. The central Identity team owns account provisioning and authentication changes.

**Included:** Employee data entry, validation, invitation request, and audit event.  
**Excluded / owned elsewhere:** Authentication and identity provisioning — Identity team; enrollment-plan selection — Benefits Platform team.  
**Source requirements:** Stakeholder process notes dated 2026-05-12; approved enrollment mockup v3; policy BEN-14.

**Scope and requirements acknowledged:** Jordan Smith, 2026-05-20, Jira comment on ENR-120.

## Material requirement changes

| ID | Date | Change and reason | Affected Jira / release | Decision / approver |
|---|---|---|---|---|
| CHG-01 | 2026-06-03 | Invitation expiry changed from 48 hours to 72 hours to match policy BEN-14. | ENR-138 / v1.1.0 | Approved — Jordan Smith |
| CHG-02 | 2026-06-10 | Bulk upload moved to a later project phase due to an external dependency. | ENR-151 / deferred | Approved — Morgan Lee and Jordan Smith |

## Validation and releases

| Release / date | Delivered Jira scope | Validation result / evidence | Business approval | Exceptions / deferred work |
|---|---|---|---|---|
| v1.0.0 / 2026-05-29 | ENR-131, ENR-132, ENR-134 | Pass — Jira validation results | Jordan Smith, 2026-05-28, ENR-120 comment | Invitation expiry change assigned to v1.1.0 |
| v1.1.0 / 2026-06-12 | ENR-138, ENR-145 | Pass — automated results and UAT notes | Jordan Smith, 2026-06-11, approval email linked in ENR-120 | ENR-151 bulk upload deferred |

## Completion

**Disposition:** All committed team scope delivered; bulk upload removed from the current team commitment and returned to project intake.  
**Open items and owner:** ENR-151 — Morgan Lee to coordinate future phase.  
**DTR attached to project record:** 2026-06-13.

