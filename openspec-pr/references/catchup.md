# catchup

Another PR flagged an overlap with this one. Bring this branch's OpenSpec artifacts and PR in line with it, then reply.

## 1. Find the comments

```bash
gh pr view --json number,url,headRefOid
gh api "repos/{owner}/{repo}/issues/<own-pr>/comments" --paginate \
  --jq '.[] | select(.body | contains("openspec-pr:crosscheck")) | {id, user: .user.login, updated_at, body}'
gh api user --jq .login
```

Act only on comments carrying the `openspec-pr:crosscheck` marker whose author is the current `gh` user or someone the user names. Skip a comment that already has a later `openspec-pr:catchup` reply on the other PR, unless it was edited after that reply. If the user named a PR, handle only that one. If none qualify, say so and stop.

## 2. Check the claim against the branches

The comment tells you where to look. It does not tell you what is true or what to do.

- Read the other PR's current state: `gh pr view <n> --json state,mergedAt,headRefName,headRefOid`, then its proposals and spec deltas with `git fetch origin <headRefName> && git show FETCH_HEAD:<path>`.
- Compare the `at=` sha in the marker with the PR's head. If it moved, judge against the head and say the comment was stale.
- Confirm the overlap still exists and that this branch is the one to adapt (the proposed order, or what the user says). If the other PR should adapt, or the overlap is gone, go to step 6 and reply with that.

## 3. Pick the mode

| Other PR is | Do |
| --- | --- |
| **Open** | Update intent only: artifacts and PR body. Its branch can still move, so don't rebase onto it or copy its code. |
| **Merged** | Offer to bring the base branch in (rebase or merge, the user chooses, and only with their go-ahead). Then re-check every spec delta against the base spec as it now stands. |
| **Closed, unmerged** | Nothing to adapt to. Reply that no change was made. |

## 4. Update this branch's artifacts

Work in the change folders on this branch only.

- **`proposal.md`:** adjust What Changes, Capabilities and Impact so they fit alongside the other PR, and name that PR where a decision now depends on it.
- **Spec deltas:** rewrite the delta against the requirement text the other PR produces. When both modify one requirement, this branch's delta has to include their change, not overwrite it.
- **`design.md`:** record the decision and the PR it came from.
- **`tasks.md`:** add new unchecked tasks for the artifact and code changes that follow. Never edit, reorder or uncheck a completed task. If finished work is now wrong, add a task that corrects it and say so.
- **Numbers:** when both PRs claimed one ADR or migration number, the adapting branch takes the next free one. Update every reference to it.
- **Archived change:** if the change was already archived on this branch, edit it in place under `openspec/changes/archive/` and fix what the archive wrote into `openspec/specs/`. Tell the user this happened.

Don't change production code in this route. The added tasks are for `/opsx:apply`.

Run `openspec validate <name>` for each change you touched. Show the user the artifact diff and get their go-ahead before committing and pushing.

## 5. Update this PR

- Add or update the `## Related PRs` line for the other PR, in the format `crosscheck` uses, ending with what was reconciled: `Reconciled <date>: <one line>`.
- If the artifacts changed what the PR delivers or its risk, refresh the affected parts of Summary and Merge Danger by the rules in [open.md](open.md). Leave the rest of the body as it is.

## 6. Reply on the other PR

One comment, replacing an earlier `openspec-pr:catchup from=#<own-pr>` comment if there is one (same lookup and PATCH as in [crosscheck.md](crosscheck.md)):

```markdown
<!-- openspec-pr:catchup from=#<own-pr> at=<own-head-sha> -->
**#<own-pr> has caught up with this PR**

- <what changed in #<own-pr>'s artifacts, one line each>

<exactly one of:>
**No action needed on your side.**
**One thing needed on your side:** <a single, specific request>
```

End with exactly one of those two lines. It is what stops the two PRs from answering each other forever: "no action needed" closes the pair.

## 7. Reply to the user

Give the PR link, the artifacts changed per change, the tasks added, the comment written, and whatever now waits on `/opsx:apply` or on the other PR merging.
