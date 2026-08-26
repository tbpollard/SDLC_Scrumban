---
name: ba-project-intake
description: Initialize or update a lightweight local BA project workspace from a Project ID, stakeholder and product-owner names, team resources, and discovery collateral. Use at project intake or when foundational project context changes; do not use for detailed backlog refinement or release validation.
---

# BA Project Intake

Create a factual starting point for the team's portion of a project. Read [the workspace definition](../../../docs/agent-project-workspace.md) before writing records.

## Initialize

1. Confirm the Project ID; do not create a workspace without it.
2. Identify the business/product owner, other stakeholders, team members and roles, and supplied collateral. Keep unknown values as `TBD`.
3. Run `scripts/new_project.py` from the repository root. Use `--copy-collateral` only when the user wants local copies; otherwise record the original paths or links.
4. Review every created file and replace any derivable placeholders. Do not infer final scope merely from job titles or a document filename.
5. Summarize the created path, recorded inputs, missing decisions, and next discovery action.

If `projects/<Project ID>/` already exists, do not rerun the initializer. Update the existing records carefully and preserve prior facts.

## Scope discovery

Read supplied collateral that is available and relevant. Draft the intended outcome, included work, exclusions, outside owners, dependencies, and open questions. Label interpretations as assumptions until a stakeholder confirms them.

The intake is complete when the people and source inventory are usable and the team's delivery boundary is either recorded or has explicit questions and owners.
