# open

Turn the OpenSpec changes on the current branch into one pull request a reviewer can read without opening a single `proposal.md`.

## 1. Find the changes

```bash
python3 scripts/list_changes.py [base-ref]
```

Each line is `name  state  tasks  proposal-path` for a change touched since the merge base, committed or not. An archived change (`openspec/changes/archive/<date>-<name>/`) is listed once, under its plain name.

- If the user named changes, use those and ignore the rest.
- If the list holds changes the branch's code doesn't deliver (a proposal captured for later, `0/n` tasks beside finished ones), say which you are leaving out and why, then carry on.
- If the list is empty, or the changes live in an OpenSpec store, run `openspec list` and ask which changes the PR covers.

## 2. Read each change

Read `proposal.md` in full from disk. Open `design.md` and the spec deltas only when the proposal alone doesn't give you the visual or the risk. Compare what the proposal promises with `git diff <base>...HEAD`: the body describes what the branch delivers, so drop or flag anything proposed but not built.

## 3. Write the body

Follow the `pr` skill (`../../pr/SKILL.md`) for the choice of visual, the evidence tiers and the merge-danger rules. If it isn't installed, keep the same sections with one small diagram, diff sketch or tree per change.

```markdown
## Summary

<one or two sentences: what the PR delivers as a whole>

| Change | What it does | Tasks |
| --- | --- | --- |
| [`<name>`](<proposal-path>) | <one line, in user terms> | <done>/<total> |

### `<name>`

**Why:** <the problem, one or two sentences from the proposal's Why>

<one visual: diagram, diff sketch or tree>

- <What Changes, condensed to the bullets a reviewer must know>
- **BREAKING** <keep every breaking marker>

**Specs:** new `<capability>` · modified `<capability>`

### `<next-name>`

...

## Related PRs

<only when crosscheck or catchup has written it; see below>

## Evidence

- **Before:** <screenshot/output/failing test run>
  **After:** <screenshot/output/passing test run>

## Merge Danger

**Door:** <one-way or two-way>

**Blast Radius:** <one-word description>
```

Rules:

- **One change:** drop the table and the `### <name>` heading. The Why, visual and bullets sit directly under Summary, with the proposal linked once.
- **Four or more changes:** keep the table open and wrap each change section in `<details><summary><code>name</code>: one line</summary>`, so the table is the way in.
- Order changes so a reviewer can read top to bottom: foundations first, then what builds on them. Say so in one line when a change depends on another.
- Rewrite, don't paste. A proposal is written for the person building the change. The PR is for the person approving it, so cut file inventories, env var lists and rationale they don't need to judge the merge.
- Link each proposal with a path relative to the repo root, so it opens at the PR's commit.
- A change with unfinished tasks is marked in the table (`12/40`, or `spec only` at `0/n` with no code). Never present it as done.
- Evidence is one section for the whole PR. Label each item with its change when there are several. For a spec-only change, the evidence is `openspec validate <name>` passing.
- Merge Danger is one verdict for the whole PR, set by the riskiest change. The proposal's **BREAKING** bullets and its Impact lines on data, migrations and configuration are the inputs. Name the change that sets the verdict.
- **Related PRs** belongs to `crosscheck` and `catchup`. Never write it here. When updating an existing body, carry the section over unchanged, along with anything a person added by hand.

## 4. Open or update the PR

1. Write the body to a temporary file, then:
   - A PR already exists for the branch (`gh pr view --json number,url`): `gh pr edit --body-file <file>`.
   - Otherwise: `git push -u origin HEAD`, then `gh pr create --base <base> --title "<title>" --body-file <file>`.
2. Title: match the repo's recent PR and commit titles (`git log --oneline -10`). One change: name what it delivers. Several: name the shared outcome, not a list of change names.
3. Reply with the PR link and the list of changes it covers, including any you left out.
