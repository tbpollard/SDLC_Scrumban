---
name: ba-sharepoint-project-intake
description: Initialize or update the fixed Markdown project workspace in a SharePoint document library from a Project ID, people, and discovery collateral, always copying supplied files into project collateral. Use at intake or when foundational context or new source files arrive; do not use for backlog refinement or validation.
compatibility: Microsoft Copilot Studio Agents Experience with configured SharePoint document-library tools.
---

# SharePoint BA project intake

Create a factual starting point for the team's portion of a project. Follow the agent instructions, read the bundled `sharepoint-repository-contract.md`, and use the bundled templates.

For an existing project, read the whole workspace and include the fixed status block before work. After any update, reread changed files, run the consistency checks, and show status again if the stage or gate changed.

## Initialize

1. Confirm the Project ID; do not create a workspace without it.
2. Search for the exact `Projects/<Project ID>/` folder. Reject partial matches and SharePoint duplicate-name suffixes.
3. Identify the business or product owner, other stakeholders, team members and roles, and all supplied collateral, including conversation attachments. Keep unknown values as `TBD`.
4. If the workspace does not exist, use the initialization tool to create the exact folder structure and all canonical files from `templates/`. Initialize the CSV files with their required headers. Verify every returned path before continuing.
5. If the workspace exists, preserve its content and version history. Do not rerun initialization.
6. Before reading or referencing each new supplied file, use the collateral tool to copy it into `collateral/`. Skip identical duplicates; add a deterministic content-hash suffix for different files with the same name.
7. Record each project-relative `collateral/...` path in the source inventory in `project-context.md`, then review the retained copies and replace derivable placeholders.
8. Do not infer final scope from job titles or filenames. Draft intended outcome, included work, exclusions and outside owners, dependencies, assumptions, constraints, and open questions. Label interpretations as assumptions until confirmed.
9. Advance to `2 of 7 — Discovery & Requirements` in both project context and the DTR only when every supplied file is retained and the people and source inventory are usable.
10. Conditionally update the full canonical files, reread them, and verify headings, relative paths, stage consistency, and preserved facts.

If a supplied file cannot be materialized in SharePoint, keep Stage 1 and report the missing upload or permission as a blocker. A web link may be recorded as a source, but it does not satisfy the retained-copy rule for a supplied file.

Finish with the fixed lifecycle-status block, exact SharePoint files created or updated, retained collateral paths, assumptions and open questions, and the smallest next action with an owner.
