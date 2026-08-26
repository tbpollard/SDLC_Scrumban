# Jira Requirements Guide

Jira is the detailed system of record for the team's delivery requirements. Use the existing board and fields where possible; new fields are not required to adopt this guide.

For the local-filesystem MVP, generate `jira-backlog.csv` using the requirements skill's renderer. Its columns follow Jira Cloud's CSV hierarchy model: `Work item ID`, `Work type`, and `Parent`, with the required `Summary` field and details in `Description`. Map those columns in Jira's import wizard and validate before import.

The generated Epic is the Jira parent of both Stories and Tasks. A Task's related `REQ` ID remains in Description because standard Tasks are not children of Stories; use a Sub-task type only when the target Jira configuration explicitly supports that hierarchy.

## Work hierarchy

| Level | Use |
|---|---|
| Epic | The team-owned feature, outcome, or delivery component under a Project ID. |
| Story | A testable unit of stakeholder value or system behavior. |
| Task/sub-task | Implementation work that does not need separate business acceptance. |

Put business requirements and acceptance criteria on epics or stories. Do not bury them only in development tasks.

## Minimum epic content

- Project ID
- Team-owned outcome and scope boundary
- Business owner
- Links to source requirements
- Included stories
- Link to the DTR

## Minimum story content

Use this short form:

```text
Outcome / requirement
<What must the user, business, or system be able to do?>

Acceptance criteria
1. <Observable, testable result>
2. <Observable, testable result>

Source / context
<Link, document section, decision, mockup, or stakeholder>

Dependencies / constraints
<Only when applicable>
```

The familiar “As a / I want / so that” format is optional. Plain requirement statements are acceptable when clearer.

## Acceptance-criteria quality check

Acceptance criteria are ready when they are:

- specific enough that the expected result is understood;
- testable through observation or evidence;
- limited to the story's scope;
- inclusive of important errors, permissions, or boundary conditions; and
- understood by the stakeholder and delivery team.

Use Given/When/Then only when it makes a rule clearer.

## Minimal workflow states

Map the team's existing board to these outcomes rather than adding states solely for this guide:

**Discovery → Requirements Approval → Ready → In Development → Ready for Validation → Validation → Done**

Suggested **Ready** check:

- outcome and acceptance criteria are clear;
- source and business owner are identified;
- dependencies and material risks are known; and
- the item is small enough to implement and validate.

The project cannot enter Delivery until Business Requirements Acceptance covers the current scope and acceptance-criteria baseline.

## Traceability conventions

- Put the Project ID on the epic.
- Link stories to the epic.
- Include the Jira key in branches, commits, or pull requests when practical.
- Link validation evidence to the story and project validation record.
- Use a release/fix-version field if already supported; otherwise list Jira keys in the DTR release table.
- Use Jira comments or history to record requirement decisions and changes.
- Preserve the stable local ID embedded in each imported Summary so a later Jira export can be linked back to local records.

## Testing and approval

Testing answers one question: **Did the delivered behavior satisfy the acceptance criteria?** Record pass, fail, blocked, or accepted exception with a link to supporting evidence when useful.

Approval may be captured by workflow action, Jira comment, email, or meeting record. It must identify the approver, date, delivered scope, and any exceptions. The DTR links or cites that evidence.
