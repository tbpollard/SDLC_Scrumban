---
name: ba-release-closure
description: Map one or more planned or actual GitHub releases to Jira-ready requirements, validation evidence, stakeholder approvals, and final team-scope disposition. Use when recording a release, reconciling multi-release delivery, or deciding whether the BA delivery record can close.
---

# BA Release and Closure

Read [the completion rules](../../../docs/operating-guide.md), [workspace definition](../../../docs/agent-project-workspace.md), DTR, backlog, change log, and every release record.

## Record a release

1. Verify the actual GitHub release/tag or leave it `TBD`; never infer a release from a branch name alone.
2. Map the release to included `REQ`, acceptance-criteria, and Jira IDs.
3. Confirm validation status, business decision, exceptions, and deferred work from evidence.
4. Update the release record, backlog status, and DTR release row consistently.
5. Preserve all earlier release rows. A later release supplements or supersedes only the scope explicitly stated.

## Decide closure

Reconcile every team-owned requirement as delivered, transferred, cancelled, or explicitly deferred. For non-delivered scope, identify the disposition, owner, and evidence. Confirm that each delivered release has validation and approval or a documented approved exception.

Mark the DTR complete only when:

- every team-owned requirement has a final disposition;
- material changes are decided or explicitly transferred/deferred;
- each delivered release is linked and has required validation and approval evidence; and
- the DTR attachment/link to the central project record is recorded.

If those conditions are not met, leave the project active and provide the smallest closure checklist with named owners. Do not create a GitHub release, merge code, or close Jira items unless the user separately authorizes and the relevant integration is available.
