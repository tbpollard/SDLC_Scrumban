---
name: ba-requirements-backlog
description: Analyze project collateral and decisions to create or refine the team's local Jira-ready epic, requirements, stories, and testable acceptance criteria. Use during discovery and backlog refinement; do not claim ownership of requirements outside the team's delivery boundary.
---

# BA Requirements and Backlog

Read [the Jira requirements guide](../../../docs/jira-requirements-guide.md), [workspace definition](../../../docs/agent-project-workspace.md), the project's context, current backlog, and relevant collateral.

## Produce the smallest sufficient backlog

1. Confirm the team delivery boundary and separate externally owned work.
2. Identify requirements supported by a source, stakeholder decision, or clearly labeled BA inference.
3. Assign stable `REQ-nnn` IDs. Never renumber existing items.
4. Write outcome-focused stories or requirement statements. The user-story sentence form is optional.
5. Add stable `AC-nnn-nn` acceptance criteria that are observable and testable, including important permissions, errors, and boundary cases.
6. Cite the source at requirement level instead of copying collateral.
7. Record unresolved questions with an owner and affected requirement.
8. Set an item to `Ready` only when it meets the repository's Ready check.

Split work according to independently testable stakeholder value, not technical layers. Put implementation-only work in suggested tasks rather than treating it as a separately approved business requirement.

Update the DTR's scope and source links, but record scope/requirements acknowledgement only when actual evidence identifies the person and date. Provide a concise Jira-entry summary; do not invent Jira keys or claim that local drafts were entered in Jira.
