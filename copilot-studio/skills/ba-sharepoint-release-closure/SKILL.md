---
name: ba-sharepoint-release-closure
description: Record independent releases from one or more repositories in the SharePoint Markdown workspace with mandatory change tickets, or reconcile final team scope and capture Project Completion Sign-off. Use for release registration at Delivery or later and for project closure; never equate a release with completion.
compatibility: Microsoft Copilot Studio Agents Experience with configured SharePoint document-library tools.
---

# SharePoint BA release and closure

Follow the agent instructions and read the bundled `sharepoint-repository-contract.md`, `templates/release-record.md`, DTR, backlog, change log, validation, and every release record.

Read the whole workspace and show lifecycle status before work. After any update, reread affected files, run consistency checks, and show status again if the stage or gate changed.

## Record a release

1. Copy supplied deployment or change evidence into `collateral/` before use.
2. Search existing release IDs, assign the next stable `REL-nnn`, and create `releases/<release-id>.md` from the bundled template without changing its schema.
3. For an actual release, require repository, tag or version, production date, change-management ticket, delivered `REQ` or Jira scope, and retained evidence. Never infer a release from a branch name, pull request, or plan.
4. Update the release record, applicable backlog delivery status, and DTR release register consistently.
5. Preserve all earlier releases across all repositories. A later release supplements or supersedes only explicitly stated scope.
6. Do not change the lifecycle stage merely because a release occurred. Do not require Project Completion Sign-off to record a release.

## Decide closure

Reconcile every team-owned requirement as delivered, transferred, cancelled, or explicitly deferred. For non-delivered scope, identify disposition, owner, and retained evidence. Ensure each actual release has a change ticket and scope mapping; release count does not determine closure.

Mark the DTR complete only when:

- every team-owned requirement has a final disposition;
- current Business Requirements Acceptance covers the final baseline;
- material changes are decided or explicitly transferred or deferred;
- final-scope validation is complete and UAT Acceptance is approved;
- Security Sign-off is approved or documented as not required;
- all releases are recorded with repository, tag or version, date, change ticket, scope, and evidence;
- Project Completion Sign-off is approved from retained evidence; and
- the DTR attachment or link to the central project record is recorded.

Copy completion approval evidence, update the DTR approval ledger, set both stage fields to `7 of 7 — Complete`, and set project status `Complete` only when every condition is met. Otherwise leave the project active and provide the smallest closure checklist with named owners.

Conditionally update the full affected files, reread the entire workspace, and verify every closure condition. Do not merge code, create a repository release, close Jira items, send approvals, or attach to another system unless separately authorized and the relevant tool is available.

Finish with the status block, release or closure SharePoint paths updated, unmet conditions, and the smallest next action with an owner.
