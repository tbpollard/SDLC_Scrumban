---
name: ba-release-closure
description: Record independent releases from one or more repositories with mandatory change tickets, or reconcile final team scope and capture Project Completion Sign-off. Use for release registration at any Delivery-or-later stage or for project closure; never equate a release with project completion.
---

# BA Release and Closure

Read [the completion rules](../../../docs/operating-guide.md), [workspace definition](../../../docs/agent-project-workspace.md), [output contract](../../../docs/agent-output-contract.md), DTR, backlog, change log, validation, and every release record.

Run the coordinator's status helper before work and include its fixed block. After any update, run the project checker and show status again if the stage or gate changed.

## Record a release

1. Copy supplied deployment or change evidence into project collateral.
2. Create `releases/<release-id>.md` from `templates/release-record.md` without changing its schema.
3. For an actual release, require repository, tag/version, production date, change-management ticket, delivered `REQ`/Jira scope, and evidence. Never infer a release from a branch name.
4. Update the release record, applicable backlog delivery status, and DTR release register consistently.
5. Preserve all earlier releases across all repositories. A later release supplements or supersedes only explicitly stated scope.
6. Do not change the lifecycle stage merely because a release occurred. Do not require Project Completion Sign-off to record a release.

## Decide closure

Reconcile every team-owned requirement as delivered, transferred, cancelled, or explicitly deferred. For non-delivered scope, identify disposition, owner, and evidence. Ensure each actual release has a change ticket and scope mapping; release count does not determine closure.

Mark the DTR complete only when:

- every team-owned requirement has a final disposition;
- current Business Requirements Acceptance covers the final baseline;
- material changes are decided or explicitly transferred/deferred;
- final-scope validation is complete and UAT Acceptance is approved;
- Security Sign-off is approved or documented as not required;
- all releases are recorded with repository, tag/version, date, change ticket, scope, and evidence;
- Project Completion Sign-off is approved; and
- the DTR attachment/link to the central project record is recorded.

Copy completion approval evidence, update the DTR ledger, and set `7 of 7 — Complete` only when all conditions are met. Otherwise leave the project active and provide the smallest closure checklist with named owners. Run the project checker and status helper. Do not create a GitHub release, merge code, or close Jira items unless separately authorized and the integration is available.
