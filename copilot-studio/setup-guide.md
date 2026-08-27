# Configure the Copilot Studio agent

This package targets the Microsoft Copilot Studio Agents Experience and its GitHub Copilot harness. It preserves the original skill set's Markdown/CSV workspace while replacing local filesystem storage with one SharePoint document library.

## 1. Configure the SharePoint document library

Create or select a document library and enable versioning. Create a single root folder named `Projects`; the agent creates one child folder per Project ID using the exact structure in [sharepoint-repository-contract.md](sharepoint-repository-contract.md).

Do not create lifecycle SharePoint lists. The canonical records remain:

- `project-context.md`
- `delivery-traceability-record.md`
- `backlog.md`
- `jira-backlog.csv`
- `jira-id-map.csv`
- `change-log.md`
- `validation.md`
- `collateral/`
- `releases/<release-id>.md`

Apply site permissions, retention, sensitivity, checkout, and content-approval policies before production use. Configure the site URL, library, and Projects folder as environment variables or maker-defined tool inputs.

## 2. Create the agent

Create an agent in the new Copilot Studio experience. Set its name to `Delivery Lifecycle Facilitator`, then paste [agent-instructions.md](agent-instructions.md) into the Instructions field.

Upload each ZIP from `packages/` through **Build > Skills > Add skill > Upload a skill**. Every package contains its `SKILL.md`, the document-library contract, and the original Markdown templates.

## 3. Add SharePoint knowledge

Add the document library's `Projects` folder as a SharePoint knowledge source. Suggested description:

> Governed Markdown project workspaces, discovery collateral, and delivery evidence for projects coordinated by the Delivery Lifecycle Facilitator. Use only after resolving one exact Project ID.

The knowledge source is permission-trimmed and supports grounding; it does not write or update files. Users need at least Read access, and encrypted or password-protected content might not be available for grounding.

## 4. Add document-library tools

In **Build > Tools**, add SharePoint connector actions or workflows that implement the four recommended capabilities in the repository contract: read workspace, initialize workspace, conditionally update canonical files, and store collateral.

If exposing individual connector actions, include at least:

- Get file metadata using path
- Get file content
- List folder
- Create file
- Update file
- Copy file or an equivalent upload action

Prefer bounded workflows because they can enforce the exact project root, required filenames, collision handling, and stale-version checks while presenting a small tool surface to the agent. A workflow that updates files should take the expected version or ETag when available and reject paths outside `Projects/<Project ID>/`.

The Microsoft SharePoint MCP server is documented as a preview feature for the standard harness and its file tool set can change. If it becomes available and approved in your Agents Experience environment, it may supply some read, create, copy, and upload operations; ensure a supported canonical-file update capability still exists before relying on it.

## 5. Configure authentication and policy

- Prefer user authentication when SharePoint access should mirror the signed-in user's permissions.
- Use maker credentials only when governance explicitly permits a service identity, and restrict that identity to the lifecycle library.
- Review Power Platform data-loss-prevention policies for SharePoint and any Jira connector or MCP server.
- Do not provide delete tools for normal operation.

## 6. Test before publishing

Use Preview and inspect the activity trace for each scenario:

- Initialize a project and verify the exact canonical file and folder structure.
- Attempt intake without a Project ID and verify no folder is created.
- Supply a file and verify it is copied to `collateral/` before analysis.
- Produce a Ready backlog, regenerate `jira-backlog.csv`, and confirm the agent stops at Stage 3.
- Provide ambiguous approval language and confirm it remains Pending.
- Record explicit requirements approval and confirm both stage fields move to Stage 4.
- Apply a material change and confirm the approval becomes Superseded and both stage fields return to Stage 3.
- Record two releases from different repositories without completing the project.
- Attempt a released status without a change ticket and confirm rejection.
- Simulate a stale version or concurrent edit and confirm the workflow rejects the overwrite and the agent rereads.
- Complete validation, UAT, Security disposition, final reconciliation, completion approval, and DTR linkage; confirm closure only when every condition is present.

Publish only after tool calls, stored SharePoint files, permissions, version behavior, and status blocks match the expected outcomes.

## Microsoft references

- [Skills overview for agents](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/skills-overview)
- [Add an existing skill to an agent](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/skills-add-existing)
- [Configure agent details and instructions](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/authoring-instructions)
- [Available tools for agents](https://learn.microsoft.com/microsoft-copilot-studio/agents-experience/tools-available)
- [Add SharePoint as a knowledge source](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-add-sharepoint)
- [SharePoint connector actions](https://learn.microsoft.com/sharepoint/dev/business-apps/power-automate/sharepoint-connector-actions-triggers)
- [SharePoint MCP reference (preview)](https://learn.microsoft.com/microsoft-copilot-studio/mcp-sharepoint-tools)
