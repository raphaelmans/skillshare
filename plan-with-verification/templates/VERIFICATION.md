# Verification

How agents prove a change works in this repo. Tests alone don't count as proof. A change is verified only when an agent has run the app locally, used it the way a real user would, and posted the evidence on the ticket.

Read this file only when you verify a ticket or create or maintain the verify skill. During repo setup, fill in every `<...>` placeholder above the proof comment format. `<ticket-id>` and the proof format's placeholders stay as they are.

## Labels

Every ticket carries exactly one of these labels, defined in the Skillshare `plan-with-verification` templates (`labels.json`):

| Label | Meaning | What the agent does |
| --- | --- | --- |
| `prototype` | First iteration or throwaway | Skips live verification and comments "Not verified, prototype." before closing. |
| `keeper` | Feature that stays | Runs the full loop below and closes only on a full pass. |

The `plan-with-verification` skill applies these labels while planning. To promote a prototype module, swap its labels and open one ticket from the promote-ticket template (`<path, e.g. .github/ISSUE_TEMPLATE/promote-to-keeper.md>`).

## Local environment

| What | Command |
| --- | --- |
| Start the app | `<one command>` |
| Start the local database | `<command; runs in Docker, separate from production>` |
| Reset and re-seed | `<one command that wipes the local database and re-seeds it>` |

The seed is deterministic: every run creates the same starting state.

## Personas

The seed creates one email-and-password user per persona. Personas follow who uses the app, not RBAC roles; roles inside a workspace or tenant belong to the specs and tickets that introduce them. When a ticket adds or changes a persona, the same ticket updates the seed and this table.

| Persona | Login (seeded) | Entry point | Notes |
| --- | --- | --- | --- |
| `<persona>` | `<email>` / `<password or env var>` | `<route, screen or command>` | `<optional>` |

## Verify skill

- **Location:** `.skillshare/skills/verify-<app>/`, committed with the code and synced by `skillshare sync -p`. The feature map is in its `features/` folder.
- **Path override:** `create-verification-skill` and `maintain-verification-skill` say `.cursor/skills/verify-<app>/`. In this repo, read that path as `.skillshare/skills/verify-<app>/`: write and edit the skill there, then run `skillshare sync -p`. If a generated skill ever lands somewhere else, such as `.cursor/skills/` or `.claude/skills/`, move its folder into `.skillshare/skills/` and run `skillshare sync -p`.
- **Browser driving:** `<agent-browser or playwright-cli>`. No test scripts are written; the agent uses the app live.
- **Upkeep:** `maintain-verification-skill` runs `<daily, and how it's scheduled>`. Each run opens at most one PR of proven map corrections.

The feature map describes what the app does today. The code is its source of truth, not the specs, and the map changes in the same PR as the code.

## Verification loop (keeper tickets)

1. **Launch and health check** with the verify skill. Launch resets and re-seeds the database.
2. **Check the change.** Walk every journey in the ticket's "Verification (keeper)" section, logged in as the named persona through that persona's entry point.
3. **Check for regressions.** Re-run the existing journeys that the feature map says the change could affect.
4. **Collect proof.** Screenshots, a short log, and pass or fail for each journey, saved to `.verification/evidence/<ticket-id>/`. That folder is gitignored and cleanup never deletes it.
5. **Post the proof** as a comment on the same ticket: <how this repo's tracker takes attachments; for example, GitHub's CLI cannot upload images, so say how screenshots get attached>.
6. **Close or flag.** If every journey passes, close the ticket. If anything fails or can't be checked, leave it open, say why in the comment and apply `<flag label, e.g. ready-for-human>`. Human approval before closing: `<off | on>`.
7. **Clean up** with the verify skill. The evidence stays.

Proof comment format:

```markdown
## Verification proof

| Journey | Persona | Result | Evidence |
| --- | --- | --- | --- |
| <name> | <persona> | pass / fail / not checked (why) | <screenshot or log> |

Regression journeys re-run: <feature files>
Log: <short log or summary>
```
