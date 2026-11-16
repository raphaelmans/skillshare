# Verification templates

Shared files that every app repo copies once during verification setup. They're generic: fill in the `<...>` placeholders per repo. This covers only the Skillshare side of the setup; the full repo setup (seed scripts, the generated verify skill, pilot) is section 10 of the Agent Verification Playbook.

| File | Copy to | Notes |
| --- | --- | --- |
| [VERIFICATION.md](VERIFICATION.md) | `VERIFICATION.md` at the repo root | The convention; agents load it only when they verify. |
| [AGENTS-pointer.md](AGENTS-pointer.md) | One line appended to `AGENTS.md` | Create `AGENTS.md` if the repo has none. |
| [promote-ticket.md](promote-ticket.md) | `.github/ISSUE_TEMPLATE/promote-to-keeper.md`, or the tracker's template location | Has GitHub issue-template frontmatter (title and `keeper` label). Record the path in `VERIFICATION.md`. |
| [labels.json](labels.json) | Created as labels on the tracker | Source of truth for names, colors and descriptions. |

## 1. Give the repo a project skill source

The skills themselves are global: `create-verification-skill`, `maintain-verification-skill`, `plan-with-verification`, `to-spec`, `to-tickets` and `setup-matt-pocock-skills` all live in the Skillshare library and reach every repo through the global targets. Nothing is installed per repo. The repo needs only a project source to hold its generated `verify-<app>` skill:

```bash
skillshare init -p   # once, if the repo has no .skillshare/ yet
```

Run `/setup-matt-pocock-skills` once too, if the repo hasn't been set up for it, so `to-spec` and `to-tickets` know the issue tracker.

## 2. Copy the files and create the labels

Do this before generating the verify skill, so that the `VERIFICATION.md` path override is in place when `create-verification-skill` runs.

The block is safe to run again: it never overwrites a file the repo already has and never adds a line twice.

```bash
T=~/.config/skillshare/skills/plan-with-verification/templates
cp -n "$T/VERIFICATION.md" VERIFICATION.md
grep -qF 'VERIFICATION.md' AGENTS.md 2>/dev/null || cat "$T/AGENTS-pointer.md" >> AGENTS.md
mkdir -p .github/ISSUE_TEMPLATE && cp -n "$T/promote-ticket.md" .github/ISSUE_TEMPLATE/promote-to-keeper.md
grep -qxF '.verification/' .gitignore 2>/dev/null || echo '.verification/' >> .gitignore

# GitHub labels; --force makes re-runs update instead of failing.
jq -c '.[]' "$T/labels.json" | while read -r l; do
  gh label create "$(jq -r .name <<<"$l")" --color "$(jq -r .color <<<"$l")" \
    --description "$(jq -r .description <<<"$l")" --force
done
```

On a tracker other than GitHub, create the two labels by hand from `labels.json`. On a local-markdown tracker, labels are a `**Labels:**` line in the ticket file, so there is nothing to create.

## 3. Where the generated verify skill goes

Upstream `create-verification-skill` writes to `.cursor/skills/verify-<app>/`. In a Skillshare repo, the skill belongs in the project source, `.skillshare/skills/verify-<app>/`, so it is committed with the code and synced to every agent's folder. (Skillshare's managed `.skillshare/.gitignore` ignores only installed skills, so a skill created there is committed.) `VERIFICATION.md` carries this override for the agent. After generating, run `skillshare sync -p`. If the skill was written somewhere else anyway, move its folder into `.skillshare/skills/` and run `skillshare sync -p`. (`.cursor/skills/` is not a Skillshare project target, so `skillshare collect` can't see it.)

## 4. Agents that run without the global library

A scheduled or cloud agent, CI, or a teammate's machine doesn't have this library's global skills. The committed `verify-<app>` skill travels with the repo, but `maintain-verification-skill` and the planning skills don't. Where one of those has to run, vendor it into the repo from its upstream source, which pins it in `.skillshare/skills.lock.json`:

```bash
skillshare install -p cursor/plugins/pstack/skills/maintain-verification-skill
skillshare sync -p
```

Commit `.skillshare/config.yaml` and the lockfile. The installed folder itself is gitignored, so a fresh clone restores it with `skillshare install -p && skillshare sync -p`.
