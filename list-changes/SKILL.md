---
name: list-changes
description: Convert Git commit history and code changes into concise, nontechnical product updates for stakeholders. Use when a user asks for product changes, release highlights, weekly updates, changelog summaries, or business-facing updates from commits, branches, tags, pull requests, or a date range. Also use when the summary must exclude previously reported changes, avoid implementation detail, or fit a bullet limit.
---

# List Changes

Turn repository history into a short, accurate summary of implemented product outcomes.

## Workflow

1. Determine the requested repository scope, branch, date range, and time zone from the user and the local context.
2. Inspect the commit history for that scope. Treat date boundaries as inclusive unless the user says otherwise.
3. Inspect the actual diffs and affected files. Do not rely only on commit subjects.
4. Group related commits into one product change. Combine follow-up fixes with the feature that they complete.
5. Separate implemented behavior from plans, proposals, tests, refactors, and internal maintenance.
6. Remove changes that the user identifies as previously reported. Remove semantic duplicates, not only exact text matches.
7. Rank the remaining changes by stakeholder importance.
8. Write the requested output in plain product language.

## Evidence Rules

- Report a change only when the repository provides enough evidence that it was implemented.
- Use code, migrations, user interface changes, and tests as supporting evidence.
- Do not present a planning document as an implemented feature.
- Do not infer a production release date from a commit date.
- State the repository-versus-production limitation only when it is material or the user asks about release status.
- If a change affects only internal implementation, omit it unless it changes reliability, security, cost, or user experience in a way that matters to stakeholders.
- Preserve meaningful qualifications. Do not overstate the scope or benefit.

## Stakeholder Translation

Describe what changed for a user, administrator, team, or business. Prefer this pattern:

`[Audience] can now [capability], which [useful outcome].`

Use direct product terms such as:

- “Advisors can search the client list.”
- “Returning users go directly to the correct workspace.”
- “Administrators can remove duplicate companies through a protected process.”

Avoid commit types, file names, database terms, framework names, API details, and engineering jargon. Do not use phrases such as “refactored,” “endpoint,” “schema,” or “component” unless the user asks for technical detail.

## Compression Rules

- Follow the user's requested format and bullet limit.
- If the user gives no limit, use no more than 10 bullets.
- Give one main product outcome in each bullet.
- Merge commits that contribute to the same outcome.
- Remove repeated context and minor implementation details.
- Keep distinct benefits separate when combining them would hide important information.
- Do not repeat excluded or previously reported changes in different words.

## Default Output

Return only the stakeholder-ready bullet list unless the user requests analysis or supporting evidence.

Use short, nontechnical sentences. Lead with the audience or visible outcome. Order the bullets by business importance, not commit time.

## Example Request

“Review changes from August 28 through August 31. Give me no more than 10 bullets for nontechnical stakeholders. Exclude the three changes below because I already reported them.”

For this request, inspect the full period, remove all excluded topics, combine related commits, omit unimplemented plans, and return only the final bullet list.
