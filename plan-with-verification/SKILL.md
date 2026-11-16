---
name: plan-with-verification
description: "Plan a feature as a prototype or a keeper: wraps to-spec and to-tickets, then labels each ticket and gives keepers their user journeys and personas. Also promotes prototypes and ships the verification templates."
disable-model-invocation: true
---

# Plan with verification

A thin layer over `to-spec` and `to-tickets`. Those skills do the planning. This skill adds the one decision they don't make (prototype or keeper) and the verification inputs that a keeper ticket needs. Never edit `to-spec` or `to-tickets`. If their behavior should change for this workflow, change it here.

## Before you start

- **Repo convention.** Read `VERIFICATION.md` at the repo root. It names the two labels and holds the persona table (persona, login, entry point) and the feature map's location. If it's missing, use the defaults in [templates/labels.json](templates/labels.json), tell the user that the repo hasn't done verification setup, and point them at [templates/README.md](templates/README.md).
- **Tracker config.** `to-spec` and `to-tickets` read the issue tracker and triage labels that `/setup-matt-pocock-skills` writes (`docs/agents/issue-tracker.md`). If that file is missing, stop and tell the user to run that setup first.
- **Loading the wrapped skills.** `to-spec` and `to-tickets` are user-invoked only (`disable-model-invocation: true`), so the harness may not let you call them as skills. In that case, read their `SKILL.md` from the sibling folders `../to-spec/` and `../to-tickets/` next to this skill, or from wherever the harness lists them. Then follow each one exactly as if the user had invoked it: same steps, same user check-ins, same output. Do not paraphrase or shortcut them.

## 1. Ask: prototype or keeper?

Ask this first, before any spec work, as a single question:

> Is this a **prototype** (first iteration or throwaway; no live verification) or a **keeper** (it stays; every ticket is verified live before it closes)?

If the request already answers it, confirm in one line and continue. The answer applies to every ticket in this plan. If the user wants a mix, run two plans.

## 2. Run to-spec

Follow `to-spec` as written. It publishes the spec to the tracker.

## 3. Run to-tickets

Follow `to-tickets` as written, using the spec from step 2. For a keeper, when `to-tickets` quizzes the user on the breakdown (its "Quiz the user" step), also show each ticket's draft journeys and personas, so the user approves both in one pass. Don't change the breakdown's format or how `to-tickets` publishes.

## 4. Add the verification layer to each published ticket

After `to-tickets` publishes, edit every ticket it created, using the operations in `docs/agents/issue-tracker.md`. Append to the ticket. Never rewrite what `to-tickets` wrote.

- **GitHub:** `gh issue edit <n> --add-label <label>`. For the body, write the current body plus the new section to a temp file, then run `gh issue edit <n> --body-file <file>`.
- **GitLab:** `glab issue update <n> --label <label>`, then update the description the same way.
- **Local markdown (`.scratch/<feature>/issues/*.md`):** add a `**Labels:** <label>` line directly under the `**Status:**` line, then append the section to the end of the file.
- **Other trackers:** use the workflow recorded in the tracker doc.

If the tracker rejects a label because it doesn't exist yet, create it from [templates/labels.json](templates/labels.json), then apply it.

### Keeper

Add the keeper label and append this section:

```markdown
## Verification (keeper)

**Log in as:**
- <persona>: entry point `<route, screen or command>` (seeded login in VERIFICATION.md)

**User journeys:**
1. **<Journey name>.** As <persona>, starting at <entry point>: <what the user does, step by step>. **Proves it:** <observable end state, plus the side effect it should leave, such as a saved record, a sent email or a written file>.
2. ...

**Regression check:** feature-map entries this change could affect: <feature files from the verify skill's map, or "none known">.

Verify per `VERIFICATION.md`. This ticket closes only when every journey passes and the proof is posted here.
```

Journey rules:

- Write from the user's point of view, not the code's. When a feature crosses personas, write the journey across them: one persona acts, and a second persona sees the result in their own area.
- Every journey names its persona and entry point and ends in a state that can be observed in the app. If a requirement can't be observed through the app, make it an acceptance criterion instead of a journey.
- Personas come from the persona table in `VERIFICATION.md`. If a ticket adds or changes a persona, add this acceptance criterion to the same ticket: "Seed adds or updates the <persona> user and its entry point, and the persona table in VERIFICATION.md matches."
- Cover the main path and the one failure or empty state a user is most likely to hit. Stay inside the ticket's slice.

### Prototype

Add the prototype label only. No journeys, no personas, no verification section.

## 5. Report

List each ticket with its label. For keepers, add the number of journeys and the personas, and call out any ticket that needs a seed change.

## Promote a prototype module to keeper

Use this when the user asks to promote a module, not when they're planning new work. Swap the prototype label for the keeper label on the module's open tickets. Then open one promote ticket for the module. Use the repo's promote template at the path `VERIFICATION.md` records, or [templates/promote-ticket.md](templates/promote-ticket.md) if the repo has none. The template's frontmatter gives the title and the label; the rest is the ticket body, with `<module>` filled in. Don't run `to-spec` or `to-tickets` for a promotion.

## Repo setup

The files an app repo copies during setup ship in [templates/](templates/): the `VERIFICATION.md` template, the one-line `AGENTS.md` pointer, the promote-ticket template and the label definitions. Read [templates/README.md](templates/README.md) only when setting a repo up.
