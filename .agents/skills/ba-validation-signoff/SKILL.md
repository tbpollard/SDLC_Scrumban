---
name: ba-validation-signoff
description: Create or update project-level validation from acceptance criteria and capture UAT Acceptance plus Security Sign-off when applicable, independently of release count. Use for validation planning, evidence, UAT decisions, or security disposition; do not fabricate results or approvals.
---

# BA Validation and Signoff

Read [the workspace definition](../../../docs/agent-project-workspace.md), [output contract](../../../docs/agent-output-contract.md), project backlog, changes, DTR, `validation.md`, and all relevant copied evidence.

Run the coordinator's status helper before work and include its fixed block. After any update, run the project checker and show status again if the stage or gate changed.

## Plan and record validation

1. Copy every supplied test, UAT, or Security artifact into project collateral before use.
2. Set the project to `5 of 7 — Validation` when delivered scope is ready for project-level validation.
3. Maintain one validation row per applicable acceptance criterion in `validation.md`. Reuse criteria as the test basis; add another artifact only when policy or complexity requires it.
4. Record results only from copied or observed evidence: `Pass`, `Fail`, `Blocked`, or `Accepted exception`. Otherwise use `Not run`.
5. Link relative evidence paths and identify tester/date.
6. Check material changes for revalidation and superseded approvals.
7. Capture UAT Acceptance in both `validation.md` and the DTR approval ledger only when evidence identifies approver, date, covered final scope, collateral type, and exceptions.
8. Capture Security Sign-off in the DTR when required. When not required, record `Not required` with rationale, decision owner/date, collateral type, and evidence.
9. Move to `6 of 7 — Completion Signoffs` only when validation is complete, UAT Acceptance covers final delivered scope, and Security is approved or documented as not required.
10. Run the project checker and status helper.

Validation and approvals are project-level and independent of releases. A demonstration or meeting is not approval unless the stakeholder decision is explicit.

When asked, draft a short signoff request naming the Project ID, covered final requirements, results, exceptions, collateral, and exact decision requested. Do not send it without separate authorization.
