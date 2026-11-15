# crosscheck

Find the parallel work that overlaps this branch, record it in this PR, and tell each affected PR with one comment.

## 1. Find candidates

```bash
python3 scripts/find_overlaps.py [base-ref]
```

It compares this branch with every other open PR and every local worktree branch, and prints for each: the OpenSpec changes it carries, spec capabilities both sides touch, clashing change names, number collisions (two different files added under the same number in one folder, as with ADRs and migrations) and other shared files. It also prints the command for reading a file from that branch.

These are candidates. A shared file is not yet a conflict.

## 2. Judge each candidate

Read this branch's proposals and spec deltas, then the candidate's, using the printed read command. Read every candidate that carries an OpenSpec change, even with no shared file: a dependency often shares none. Put each candidate in one level:

| Level | It is this when | Action |
| --- | --- | --- |
| **Conflict** | Both change the same requirement of a spec, the same table, index or migration, claim the same number, or give one term two meanings | Link and comment |
| **Dependency** | One relies on a capability, field, route or term the other adds, renames or removes | Link and comment |
| **Adjacent** | Shared files, with no shared intent | Link only |
| **Unrelated** | Nothing a reviewer of either PR needs to know | Nothing |

For a conflict or dependency, name the exact thing: the requirement heading, the column, the ADR number. If you cannot name it, it is adjacent.

## 3. Propose who adapts

The PR that merges second adapts. Propose the order from what you can see: a PR others depend on goes first, then the one closer to merging (review state, finished tasks, not a draft). State it as a proposal. The user decides, and may overrule it before you write anything.

## 4. Update this PR

Needs this branch's own PR. Without one, report the findings and stop: tell the user to run `openspec-pr open` first.

Write or replace the `## Related PRs` section of the body, placed before `## Evidence`, and change nothing else in the body:

```markdown
## Related PRs

- #15 · **conflict** · both change "Enrollment exits" in spec `outreach-automation`. Proposed order: this PR first.
- #18 · **dependency** · this PR reads the `source` custom field that #18 adds. Proposed order: #18 first.
- #21 · **adjacent** · both touch `src/lib/shell/navigation.ts`.
```

If this branch is the one that should adapt, say so in the reply and name `openspec-pr catchup` as the way to do it. Don't change artifacts in this route.

## 5. Comment on each affected PR

One comment per conflict or dependency. None for adjacent.

```markdown
<!-- openspec-pr:crosscheck from=#<own-pr> at=<own-head-sha> -->
**Parallel work: #<own-pr> overlaps this PR**

- **<conflict|dependency>:** <the exact requirement, table, number or term, and what each PR does to it>

**Proposed merge order:** <#a first, then #b>, because <one reason>. The second PR adapts.

**If this PR adapts:** run `openspec-pr catchup` on its branch.

Changes involved: [`<own-change>`](<link to proposal on own branch>) here, `<their-change>` in this PR.
```

- **One comment per pair.** Look for an earlier one first: `gh api "repos/{owner}/{repo}/issues/<n>/comments" --paginate --jq '.[] | select(.body | contains("openspec-pr:crosscheck from=#<own-pr> ")) | .id'`. If found, replace its body with `gh api -X PATCH "repos/{owner}/{repo}/issues/comments/<id>" -F body=@<file>`. Otherwise `gh pr comment <n> --body-file <file>`.
- **Overlap gone.** If an earlier comment's overlap no longer exists, edit that comment to say it is resolved and why. Don't delete it.
- **Catchup reply.** If the other PR already replied with `openspec-pr:catchup` and "No action needed on your side", treat the pair as closed unless the overlap itself changed.
- State facts about the two PRs. Don't tell the other PR's author how to build their change.

## 6. Reply

List each related PR with its level and proposed order, link the comments you wrote or edited, and list separately the worktree branches with no PR that overlap. Those can't be commented on, so the user has to carry the news.
