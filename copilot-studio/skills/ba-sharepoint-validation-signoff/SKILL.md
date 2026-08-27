---
name: ba-sharepoint-validation-signoff
description: Create or update project-level validation in the SharePoint Markdown workspace and capture UAT Acceptance plus Security Sign-off when applicable, independently of release count. Use for validation planning, evidence, UAT decisions, or security disposition; do not fabricate results or approvals.
compatibility: Microsoft Copilot Studio Agents Experience with configured SharePoint document-library tools.
---

# SharePoint BA validation and signoff

Follow the agent instructions and read the bundled `sharepoint-repository-contract.md`, `templates/validation.md`, current backlog, changes, DTR, validation file, all release records, and retained evidence.

Read the whole workspace and show lifecycle status before work. After any update, reread affected files, run consistency checks, and show status again if the stage or gate changed.

## Plan and record validation

1. Copy every supplied test, UAT, or Security artifact into `collateral/` before use.
2. Set both stage fields to `5 of 7 — Validation` when delivered scope is ready for project-level validation; do not infer readiness from a release alone.
3. Maintain one validation row per applicable acceptance criterion in `validation.md`. Reuse criteria as the test basis; add another artifact only when policy or complexity requires it.
4. Record results only from retained or directly observed evidence: `Pass`, `Fail`, `Blocked`, or `Accepted exception`. Otherwise use `Not run`.
5. Link project-relative evidence paths and identify tester and date.
6. Check material changes for revalidation and superseded approvals.
7. Capture UAT Acceptance in both `validation.md` and the DTR approval ledger only when retained evidence identifies approver, date, covered final scope, collateral type, decision, exceptions, and relative evidence path.
8. Capture Security Sign-off in the DTR when required. When not required, record `Not required` with rationale, decision owner and date, collateral type, and retained evidence.
9. Move both stage fields to `6 of 7 — Completion Signoffs` only when validation is complete, UAT covers final delivered scope, and Security is approved or documented as not required.
10. Conditionally update the full validation and DTR files, plus project context when the stage changes; reread and verify coverage and stage consistency.

Validation and approvals are project-level and independent of releases. A demonstration or meeting is not approval unless the stakeholder decision is explicit.

When asked, draft a short signoff request naming the Project ID, final requirements, results, exceptions, retained collateral, and exact decision requested. Do not send it without separate authorization and a messaging tool.

Finish with the status block, changed SharePoint paths, validation coverage and gaps, approvals recorded or pending, and the smallest next action with an owner.
