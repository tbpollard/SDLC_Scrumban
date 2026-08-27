---
name: ba-sharepoint-requirement-change
description: Assess a requirement change in the SharePoint Markdown workspace, distinguish routine clarification from material change, and update backlog, Jira CSV, traceability, releases, approvals, and revalidation records. Use after a requirements baseline exists or whenever delivery expectations change.
compatibility: Microsoft Copilot Studio Agents Experience with configured SharePoint document-library tools.
---

# SharePoint BA requirement change

Follow the agent instructions and read the bundled `sharepoint-repository-contract.md` plus every affected canonical file and release record. Copy newly supplied change evidence to `collateral/` before analysis.

Read the whole workspace and show lifecycle status before work. After any update, reread affected files, run consistency checks, and show status again if the stage or gate changed.

## Assess and update

1. State the current requirement and proposed change in neutral language.
2. Identify requestor, reason, affected `REQ`, `AC`, and `TSK` IDs, releases, dependencies, delivery impact, completed tests, and prior approvals.
3. Classify it as a **routine clarification** only when intended behavior, scope, risk, release allocation, testing, and approval remain valid.
4. Classify it as a **material change** when any of those changes.
5. For a clarification, update the current `backlog.md` without adding change-log or DTR ceremony. After migration, Jira provides routine history.
6. For a material change, assign the next stable `CHG-nnn`, add it to `change-log.md` and the DTR, update affected backlog content, regenerate the complete Jira CSV, and mark impacted validation or approval as needing review.
7. Record the decision and approver only from retained evidence. Pending proposals remain `Pending`.

Do not delete the trace of superseded requirements. Use current text plus the material-change reference and Jira history for prior wording. If the approved requirements baseline changes, mark the applicable Business Requirements Acceptance `Superseded`, update both stage fields to `3 of 7 — Business Requirements Approval`, and stop Delivery progression until renewed approval is recorded. Re-test affected criteria and supersede UAT or Security approval whose covered scope is no longer current.

Conditionally update the full affected canonical files, then reread and verify that backlog, Jira CSV, change log, validation, releases, DTR, and stage agree.

Finish with the status block, change classification and rationale, SharePoint paths updated, approval or revalidation still needed, and the smallest next action with an owner.
