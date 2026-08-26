---
name: ba-requirements-backlog
description: Analyze copied project collateral to create or refine the fixed backlog, generate an importable Jira CSV, link returned Jira keys, and capture mandatory Business Requirements Acceptance. Use during discovery, refinement, requirements approval, or Jira linkage; do not claim ownership outside the team's boundary.
---

# BA Requirements and Backlog

Read [the Jira requirements guide](../../../docs/jira-requirements-guide.md), [workspace definition](../../../docs/agent-project-workspace.md), [output contract](../../../docs/agent-output-contract.md), project context, current backlog, and copied collateral.

Run the coordinator's status helper before work and include its fixed block. After any update, run the project checker and show status again if the stage or gate changed.

## Produce the smallest sufficient backlog

1. Copy any newly supplied files to project collateral before analysis.
2. Confirm the team delivery boundary and separate externally owned work.
3. Identify requirements supported by a copied source, stakeholder decision, or clearly labeled BA inference.
4. Assign stable `REQ-nnn`, `AC-nnn-nn`, and `TSK-nnn` IDs. Never renumber existing items.
5. Use the exact backlog template headings and field order. Split stories by independently testable value and attach implementation tasks to a parent requirement.
6. Cite relative collateral paths at requirement level.
7. Record unresolved questions with an owner and affected requirement.
8. Set an item to `Ready` only when it meets the repository's Ready check.
9. Run `scripts/render_jira_csv.py <Project ID>`; never hand-author `jira-backlog.csv`.
10. When a Jira export is supplied, copy it to collateral first, then run `scripts/link_jira_export.py` to create the ID map and update Jira keys.

Split work according to independently testable stakeholder value, not technical layers. Put implementation-only work in the fixed Implementation tasks section rather than treating it as a separately approved business requirement.

When the backlog and Jira CSV are Ready, set the stage to `3 of 7 — Business Requirements Approval`. Record approval only from copied evidence identifying the approver, date, covered REQ/AC baseline, collateral type, and decision. Keep the project at Stage 3 while approval is pending or rejected. When current Business Requirements Acceptance is `Approved` or `Approved with exceptions`, update the backlog and DTR, set the stage to `4 of 7 — Delivery`, and run the checker/status helper.

Do not invent Jira keys, claim import occurred, or allow Delivery to proceed without current Business Requirements Acceptance.
