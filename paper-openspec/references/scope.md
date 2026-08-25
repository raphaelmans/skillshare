# Artifact-Driven Design Scope

Determine the smallest Design Scope that fully contains the OpenSpec change before proposing or creating Paper UI. Let OpenSpec artifacts own intended behavior and scope. Use affected current specs, Paper, and repository routes, screens, components, tests, and navigation as current-state and downstream-impact evidence.

## Classify upward

Begin with a screen/component change and escalate only when the artifacts require a broader boundary:

- **Screen/Component Change**: A localized surface, interaction, state, variation, or responsive behavior changes without introducing a multi-step sequence or distinct user goal.
- **User Flow**: An ordered set of actions or decisions is introduced or materially changed inside an existing User Journey. It may require multiple screens while preserving the journey's overall goal and outcome.
- **User Journey**: A distinct end-to-end user goal, entry, or outcome is introduced or materially changed and may contain one or more User Flows.
- **Product Overhaul**: Multiple User Journeys, major product areas, global navigation, information architecture, or shared experience foundations change together.

Use the highest level required by the artifact set as the overall route. Keep every lower level as a nested design dependency rather than performing separate competing classifications. Classify from user-visible experience impact rather than data-model complexity alone.

## Analyze the selected route

For every route, separate confirmed requirements, assumptions, unresolved items, and optional enhancements.

For a **Screen/Component Change**, identify purpose, usage context, user goal, trigger, inputs, outputs, actions, states, variations, content behavior, interactions, reuse, responsive and accessibility requirements, affected screens or flows, dependencies, and downstream effects. Do not expand into a full journey audit unless impact crosses the local boundary.

For a **User Flow**, identify the containing journey, user and business goals, trigger, successful outcome, required data, rules, constraints, reusable behavior, primary happy path, core screens, states, decision points, branch happy paths, exceptions, recovery, meaningful edge cases, and connected-flow effects.

For a **User Journey**, identify the distinct user and business goals, entry and exit points, constituent flows, navigation, dependencies between flows or journeys, existing and missing experiences, primary successful route, major branches, exceptions, shared components, and downstream product effects. Do not re-audit unrelated journeys.

For a **Product Overhaul**, identify business goals, functional requirements, constraints, rules, dependencies, assumptions, optional enhancements, affected journeys and flows, shared foundations, navigation or information-architecture changes, duplicate or conflicting experiences, missing coverage, and a dependency-aware delivery sequence.

## Build the working matrix

Show an **Impact Matrix** for a Screen/Component Change and an **Experience Coverage Matrix** for User Flow, User Journey, or Product Overhaul. Include only applicable columns from:

- Requirement and confirmation status
- User and business goal
- Design Scope, User Journey, and User Flow
- Existing versus new behavior
- Screens and Component Families
- States and variations
- Decision points, branches, exceptions, and recovery
- Dependencies and downstream impact
- Coverage status, gap, conflict, or unresolved decision

Keep the matrix in chat and working context. Never place it in Paper, persist it as a new OpenSpec artifact, or turn it into a specification frame. When a material gap originates in the artifacts, propose the owner-specific artifact edit and wait for approval.

Block Paper design only when an unresolved item determines required behavior, navigation, permissions, data, state coverage, flow, or composition. List optional enhancements separately and do not add them to the design unless the artifacts are approved to include them. After an approved artifact correction, validate the change, rerun scope analysis, and obtain fresh Scope Approval.

## Recommend and sequence design

Choose **User Flow** grouping when an end-to-end experience should be designed and validated together. Choose a **Design Batch** when shared foundations, components, patterns, states, or dependencies are more efficient to solve together.

Order work by shared foundations, primary journeys, primary happy paths, high-impact requirements, major branch happy paths, exception paths, and meaningful edge cases. Within each dependency-ready flow or batch, create every required canonical Component Frame and its states before composing consuming Screen Artboards. Validate upward from screens to flow continuity, journey completion, and product consistency as applicable.

Before considering the approved scope complete, validate requirement coverage, user-goal completion, flow continuity, screen and state completeness, decision and branch consistency, error recovery, dependency handling, established-pattern consistency, accessibility, responsive behavior, unnecessary complexity, duplicate experiences, and dead ends.

## Report and approve

Report the Paper target, OpenSpec change, selected route and escalation evidence, matrix, material gaps, optional enhancements, and recommended sequence before any Paper mutation.

Also report the potentially affected existing Component Families, Screen Artboards, states, flows, and required viewports that may have drifted because of the change. Derive this candidate set from OpenSpec and repository evidence without a detailed Paper audit. Ask whether to run the targeted Sync Audit; declining or deferring it must not prevent the approved current-change design sequence. A later explicit `sync` invocation resumes this audit independently.

Treat an explicit `scope` invocation as analysis-only and stop after the report. For automatic preflight, stop and request Scope Approval. One approval authorizes the requested ordered design work while its source inputs remain unchanged outside the approved sequence: the artifact set, Paper target and pre-existing relevant design, requested boundary, and material repository context. Paper changes produced by the approved work do not invalidate it. A new conversation without unambiguous recent approval requires the analysis and approval again.
