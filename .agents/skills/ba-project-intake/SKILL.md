---
name: ba-project-intake
description: Initialize or update the fixed local BA project workspace from a Project ID, people, and discovery collateral, always copying every supplied file into project collateral. Use at intake or when foundational context or new source files arrive; do not use for backlog refinement or validation.
---

# BA Project Intake

Create a factual starting point for the team's portion of a project. Read [the workspace definition](../../../docs/agent-project-workspace.md) and [output contract](../../../docs/agent-output-contract.md) before writing records.

For an existing project, run the coordinator's status helper before work and include its fixed block. After any update, run the project checker and show status again if the stage or gate changed.

## Initialize

1. Confirm the Project ID; do not create a workspace without it.
2. Identify the business/product owner, other stakeholders, team members and roles, and all supplied collateral, including conversation attachments. Keep unknown values as `TBD`.
3. Run `scripts/new_project.py` from the repository root. Every `--collateral` file or directory is copied automatically; never retain an external path as the project evidence reference.
4. If the workspace already exists, run `scripts/copy_collateral.py <Project ID> <sources...>` before reading or referencing new files.
5. Record each relative `collateral/...` path in the source inventory, review the copies, and replace derivable placeholders. Do not infer final scope merely from job titles or filenames.
6. Advance to `2 of 7 — Discovery & Requirements` only when all supplied collateral is copied and the people/source inventory is usable.
7. Run the coordinator's project checker and status helper; include the fixed lifecycle-status block in the response.

If `projects/<Project ID>/` already exists, do not rerun the initializer. Copy new collateral, update existing records carefully, and preserve prior facts.

Project workspaces are intentionally unversioned. Never stage, commit, or force-add anything under `projects/`.

## Scope discovery

Read supplied collateral that is available and relevant. Draft the intended outcome, included work, exclusions, outside owners, dependencies, and open questions. Label interpretations as assumptions until a stakeholder confirms them.

The intake is complete when every supplied file exists under project collateral, the people and source inventory are usable, and the team's delivery boundary is either recorded or has explicit questions and owners.
