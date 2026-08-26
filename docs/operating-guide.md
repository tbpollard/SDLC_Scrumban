# Operating Guide

## Purpose

Use this lifecycle to provide reasonable traceability with the least practical administrative work. The team is accountable only for its assigned delivery scope, not for requirements or releases owned by other teams.

This internal lifecycle is informed by the [IIBA Business Analysis Standard](https://www.iiba.org/knowledgehub/the-business-analysis-standard/), the [Agile Extension to the BABOK Guide](https://www.iiba.org/globalassets/certification/aac/files/agile-extension-brochure.pdf), and the requirements-engineering principles in [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html). It is a tailored operating model, not a claim of formal compliance with those publications.

## Roles

| Role | Minimum responsibility |
|---|---|
| Project manager | Coordinates intake and stakeholder meetings; maintains the Project ID and central project record. |
| Business analyst | Defines the team's scope, structures requirements in Jira, maintains the DTR, and coordinates requirements approval, validation, and completion signoff. |
| Developer | Links code changes to Jira and identifies the GitHub release(s) containing delivered work. |
| Stakeholder/business owner | Confirms scope and requirements, participates in validation, and accepts or rejects the delivered result. |
| QA/tester, when used | Records validation results and evidence. |

One person may perform more than one role. The BA may reference requirements owned elsewhere without assuming ownership of them.

## Minimum workflow

### 1. Establish the delivery record

Create one DTR for the team's work under a Project ID. Record:

- the team-owned outcome and boundaries;
- the business owner and delivery contacts;
- links to source documents and the Jira epic(s); and
- known assumptions, dependencies, and exclusions.

The DTR summarizes the work. Jira and linked source documents remain authoritative for detail.

### 2. Refine work in Jira

Create or associate the appropriate epic and stories. Before development begins, each story should have:

- a clear outcome or requirement;
- testable acceptance criteria;
- relevant source links or attachments;
- dependencies or constraints that affect delivery; and
- an identified business owner or reviewer.

Use the [Jira requirements guide](jira-requirements-guide.md) for the smallest acceptable format.

### 3. Approve business requirements

Before development, require the business owner to approve the team scope and current Jira acceptance criteria as the Business Requirements Acceptance baseline. Capture the decision through a Jira approval, comment, email, meeting decision, or signed document; copy the evidence into project collateral and index it in the DTR approval ledger.

Do not proceed to Delivery while this approval is pending or rejected. This approval is not UAT Acceptance or Project Completion Sign-off.

### 4. Deliver and record releases

Developers link commits or pull requests to Jira using the team's normal Gitflow-style process. Testing validates the acceptance criteria. Evidence can be:

- Jira test results or comments;
- automated test results;
- a lightweight checklist;
- screenshots or demonstration notes; or
- a linked test-management record.

Do not create a separate test plan when the acceptance criteria and evidence are sufficient.

Record every production deployment as a release with its repository, tag/version, production date, delivered scope, change-management ticket, and evidence. Releases may occur throughout Delivery and Validation and do not complete the project.

### 5. Validate and complete

For project completion:

1. Validate final delivered scope against acceptance criteria.
2. Record UAT Acceptance covering the final delivered scope.
3. Record Security Sign-off when required, or document why it is not required.
4. Reconcile all team-owned scope and material changes.
5. Obtain Project Completion Sign-off.
6. Attach the final DTR to the central project record.

Release count and project completion are independent.

## Requirement changes

Jira's history is sufficient for wording improvements, added examples, and other clarifications that do not change intended behavior, scope, delivery risk, or stakeholder expectations.

Add a row to the DTR's **Material requirement changes** table when a change affects one or more of the following:

- team scope or an agreed exclusion;
- externally visible behavior or acceptance criteria;
- delivery date, cost, dependency, risk, or release allocation;
- previously completed testing; or
- a prior stakeholder acknowledgement or approval.

For a material change:

1. Update the affected Jira items and acceptance criteria.
2. Preserve the reason and decision in Jira or the linked source record.
3. Record a short DTR change entry with the decision date and approver.
4. Re-test affected acceptance criteria.
5. Obtain renewed Business Requirements Acceptance or other affected approval when the earlier approval is no longer valid.

The DTR is a change index, not a second change-management system.

## Exceptions and proportionality

Add artifacts only when justified. Examples include security review, architecture approval, formal test plans, data mappings, regulatory evidence, deployment plans, or a requirements traceability matrix.

If a required lifecycle step does not apply, mark it **N/A** and give a short reason. If the work is cancelled or transferred, record the disposition and remaining owner in the DTR.

## Definition of complete

The team's portion is complete when:

- Jira shows the final disposition of all team-owned scope;
- current Business Requirements Acceptance is approved;
- validation results are available for delivered acceptance criteria;
- material requirement changes are resolved or explicitly deferred;
- UAT Acceptance covers the final delivered scope;
- Security Sign-off is approved or documented as not required;
- Project Completion Sign-off is approved;
- all applicable GitHub releases are linked; and
- the DTR is attached or linked to the central project record.
