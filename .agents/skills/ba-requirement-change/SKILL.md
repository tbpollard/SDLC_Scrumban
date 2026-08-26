---
name: ba-requirement-change
description: Assess a proposed or discovered requirement change, distinguish routine clarification from material change, and update local backlog, Jira CSV, traceability, releases, approvals, and revalidation records. Use after a requirements baseline exists or whenever delivery expectations change.
---

# BA Requirement Change

Read the requirement-change rules in [the operating guide](../../../docs/operating-guide.md), [workspace definition](../../../docs/agent-project-workspace.md), [output contract](../../../docs/agent-output-contract.md), and all affected project records. Copy newly supplied change evidence to collateral before analysis.

Run the coordinator's status helper before work and include its fixed block. After any update, run the project checker and show status again if the stage or gate changed.

## Assess and update

1. State the current requirement and proposed change in neutral language.
2. Identify the requestor, reason, affected `REQ`/`AC` IDs, releases, dependencies, delivery impact, completed tests, and prior approvals.
3. Classify it as:
   - **Routine clarification** when intended behavior, scope, risk, release allocation, testing, and approval remain valid.
   - **Material change** when any of those change.
4. For a clarification, update the current backlog without adding change-log or DTR ceremony. After migration, Jira provides routine history.
5. For a material change, assign the next stable `CHG-nnn`, add it to `change-log.md` and the DTR, update affected backlog and Jira CSV, and mark impacted validation or approval as needing review.
6. Record the decision and approver only from evidence. Pending proposals remain `Pending`.

Do not delete the trace of superseded requirements. Use current text plus the material change reference and Jira history for prior wording. If the approved requirements baseline changes, mark the applicable Business Requirements Acceptance `Superseded`, move the project to `3 of 7 — Business Requirements Approval`, and stop Delivery progression until renewed approval is recorded. Re-test affected acceptance criteria and supersede any UAT or Security approval whose covered scope is no longer current.

Run the project checker and status helper. Finish with the fixed lifecycle-status block, change classification, affected records, approval/revalidation still needed, and next owner.
