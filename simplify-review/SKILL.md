---
name: simplify-review
description: Review changed code for reuse, simplification, efficiency, and altitude cleanups using four parallel reviewers, then apply the fixes. Quality only, not bug hunting. Use when the user asks to simplify, clean up, or tidy a diff, branch, PR, or work-in-progress changes.
---

# Simplify review

Improve the quality of the changed code. Do not look for correctness bugs; that is a code review's job.

## Phase 0: Gather the diff

Run `git diff @{upstream}...HEAD`; with no upstream, use `git diff main...HEAD` or `git diff HEAD~1`. If there are uncommitted changes or the range diff is empty, also run `git diff HEAD` and include the working tree, because this review often runs before the commit. If the user named a PR, branch, or file path, review that target instead. This diff is the review scope.

## Phase 1: Review from four angles in parallel

Launch four independent reviewers at once, one per angle below, each given the diff. If your harness has no subagents, do the four passes yourself, one after another. Each reviewer returns findings with `file`, `line`, a one-line `summary`, and the concrete cost: what is duplicated, wasted, or harder to maintain.

**Reuse.** Flag new code that re-implements something the codebase already has. Search shared and utility modules and files next to the change, and name the existing helper to call instead.

**Simplification.** Flag complexity the diff adds that it doesn't need: redundant or derivable state, copy-paste with slight variation, deep nesting, dead code left behind. Name the simpler form that does the same job.

**Efficiency.** Flag work the diff wastes: redundant computation or repeated I/O, independent operations run one after another, blocking work added to startup or hot paths. Also flag long-lived objects built from closures or captured environments. They keep the whole enclosing scope alive for the object's lifetime, which leaks memory when that scope holds large values; prefer a class or struct that copies only the fields it needs. Name the cheaper alternative.

**Altitude.** Check that each change fixes the root cause at the right depth instead of patching a symptom with a fragile workaround. Special cases layered on shared infrastructure mean the fix isn't deep enough. Prefer a simpler, more general change to the underlying mechanism, and name that change.

## Phase 2: Apply the fixes

Wait for all four reviewers. Merge findings that point at the same line or mechanism, then fix each remaining one directly. Skip a finding if its fix would change intended behavior, would need changes well outside the diff, or looks like a false positive. Note each skip instead of arguing with it. End with a short summary of what you fixed and what you skipped, or say the code was already clean.
