---
name: ba-requirement-change
description: Assess a proposed or discovered requirement change, distinguish routine clarification from material change, and update local backlog, change, traceability, release, and revalidation records. Use after a baseline or stakeholder acknowledgement exists, or whenever delivery expectations change.
---

# BA Requirement Change

Read the requirement-change rules in [the operating guide](../../../docs/operating-guide.md), [workspace definition](../../../docs/agent-project-workspace.md), and all affected project records.

## Assess and update

1. State the current requirement and proposed change in neutral language.
2. Identify the requestor, reason, affected `REQ`/`AC` IDs, releases, dependencies, delivery impact, completed tests, and prior approvals.
3. Classify it as:
   - **Routine clarification** when intended behavior, scope, risk, release allocation, testing, and approval remain valid.
   - **Material change** when any of those change.
4. For a clarification, update the current backlog without adding change-log or DTR ceremony. After migration, Jira provides routine history.
5. For a material change, assign the next stable `CHG-nnn`, add it to `change-log.md` and the DTR, update affected backlog content, and mark impacted validation or approval as needing review.
6. Record the decision and approver only from evidence. Pending proposals remain `Pending`.

Do not delete the trace of superseded requirements. Use current text plus the material change reference and rely on version history for prior wording. Re-test affected acceptance criteria and seek renewed approval when the earlier decision no longer covers the changed result.

Finish with the change classification, affected records, approval/revalidation still needed, and the next responsible owner.
