---
name: ba-validation-signoff
description: Create or update a release-specific validation record from acceptance criteria, record actual test evidence and exceptions, and capture scope-specific stakeholder approval. Use for UAT planning, execution tracking, approval requests, or signoff; do not fabricate results or approval.
---

# BA Validation and Signoff

Read [the workspace definition](../../../docs/agent-project-workspace.md), project backlog, material changes, DTR, and any existing record for the target release.

## Plan and record validation

1. Identify the release ID, intended date, included `REQ`/Jira items, and included acceptance-criteria IDs.
2. Create `releases/<release-id>.md` from `templates/release-validation.md` if it does not exist.
3. Create one validation row per applicable acceptance criterion. Reuse criteria as the test basis; add a separate test artifact only when complexity or policy requires it.
4. Record results only from supplied or observed evidence: `Pass`, `Fail`, `Blocked`, or `Accepted exception`. Otherwise use `Not run`.
5. Link evidence and identify tester/date when available.
6. Check material changes for revalidation needs and make incomplete coverage visible.
7. Capture approval only when evidence identifies the approver, date, covered scope, and exceptions.
8. Update the DTR release row with current validation and approval status.

Approval is for this team's delivered scope in this release, not automatically for the entire project. A demonstration or meeting is not approval unless the stakeholder's decision is explicit.

When asked, draft a short signoff request that names the release, covered requirements, results, exceptions, and the exact decision requested. Do not send it without separate authorization.
