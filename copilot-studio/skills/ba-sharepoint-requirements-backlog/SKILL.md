---
name: ba-sharepoint-requirements-backlog
description: Analyze retained SharePoint collateral to create or refine the fixed Markdown backlog, generate the canonical Jira CSV, link returned Jira keys, and capture mandatory Business Requirements Acceptance. Use during discovery, refinement, requirements approval, or Jira linkage; do not claim ownership outside the team's boundary.
compatibility: Microsoft Copilot Studio Agents Experience with configured SharePoint document-library tools.
---

# SharePoint BA requirements and backlog

Follow the agent instructions and read the bundled `sharepoint-repository-contract.md`, `templates/backlog.md`, project context, current backlog, DTR, Jira files, and retained collateral.

Read the whole workspace and show lifecycle status before work. After any update, reread changed files, run consistency checks, and show status again if the stage or gate changed.

## Produce the smallest sufficient backlog

1. Copy any newly supplied files to `collateral/` before analysis and add them to the source inventory.
2. Confirm the team delivery boundary and separate externally owned work.
3. Identify requirements supported by retained collateral, a stakeholder decision, or clearly labeled BA inference.
4. Assign stable `REQ-nnn`, `AC-nnn-nn`, and `TSK-nnn` IDs. Search the current files first and never renumber existing items.
5. Use the exact backlog template headings and field order. Split stories by independently testable value and attach implementation tasks to a parent requirement.
6. Cite project-relative collateral paths at requirement level.
7. Record unresolved questions with an owner and affected requirement.
8. Set an item to `Ready` only when the outcome and acceptance criteria are clear and testable, source and business owner are identified, dependencies and material risks are known, and the item is small enough to implement and validate.
9. Regenerate the complete `jira-backlog.csv` using the exact header and row-order contract. Validate CSV escaping and ensure acceptance criteria appear in Description.
10. When a Jira export is supplied, copy it to collateral first, then regenerate `jira-id-map.csv` and add Jira keys beside stable IDs in the backlog.

Split work by independently testable stakeholder value, not technical layers. Put implementation-only work in Implementation tasks rather than treating it as a separately approved business requirement.

When the backlog and Jira CSV are Ready, set both stage fields to `3 of 7 — Business Requirements Approval`. Record approval only from retained evidence identifying approver, date, covered `REQ`/`AC` baseline, collateral type, decision, and relative evidence path.

Keep Stage 3 while approval is pending, rejected, ambiguous, or not current. When Business Requirements Acceptance is `Approved` or `Approved with exceptions` for the current baseline, update `backlog.md`, the DTR approval ledger, and both stage fields to `4 of 7 — Delivery` in one conditional update, then reread and verify.

Do not invent Jira keys, claim import occurred, or allow Delivery without current Business Requirements Acceptance. Finish with the status block, changed SharePoint paths, Ready gaps, approval coverage, and the smallest next action with an owner.
