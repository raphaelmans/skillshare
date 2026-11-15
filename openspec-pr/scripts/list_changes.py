#!/usr/bin/env python3
"""List the OpenSpec changes a branch carries, compared with its base.

Usage: list_changes.py [base-ref]

A change counts when any file under openspec/changes/<name>/ (or its archived
copy, openspec/changes/archive/<date>-<name>/) was added or modified since the
merge base, committed or not. Prints one tab-separated line per change:

    name  state(active|archived)  tasks(done/total|-)  proposal-path|MISSING
"""
import re
import subprocess
import sys
from pathlib import Path

CHANGE = re.compile(r"^(.*?/)?openspec/changes/(archive/)?([^/]+)/")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}-")
TASK = re.compile(r"^\s*[-*] \[([ xX])\]", re.M)


def git(*args, check=True):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout.strip()


def default_base():
    head = git("symbolic-ref", "--quiet", "refs/remotes/origin/HEAD", check=False)
    if head:
        return head.removeprefix("refs/remotes/")
    for ref in ("origin/main", "origin/master", "main", "master"):
        if git("rev-parse", "--verify", "--quiet", ref, check=False):
            return ref
    sys.exit("No base ref found; pass one as the first argument.")


def main():
    root = Path(git("rev-parse", "--show-toplevel"))
    base = sys.argv[1] if len(sys.argv) > 1 else default_base()
    merge_base = git("merge-base", base, "HEAD")

    paths = git("-C", str(root), "diff", "--name-only", "-M", "--diff-filter=d", merge_base).splitlines()
    paths += git("-C", str(root), "ls-files", "--others", "--exclude-standard").splitlines()

    changes = {}
    for path in paths:
        m = CHANGE.match(path)
        if not m or (m.group(3) == "archive" and not m.group(2)):
            continue
        name = DATE.sub("", m.group(3)) if m.group(2) else m.group(3)
        folder = root / m.group(0)
        # An archived copy wins: it is where the change lives now.
        if name not in changes or m.group(2):
            changes[name] = ("archived" if m.group(2) else "active", folder)

    if not changes:
        print(f"No OpenSpec changes differ from {base} ({merge_base[:8]}).", file=sys.stderr)
        return

    for name, (state, folder) in sorted(changes.items()):
        proposal = folder / "proposal.md"
        tasks = folder / "tasks.md"
        progress = "-"
        if tasks.exists():
            marks = TASK.findall(tasks.read_text())
            progress = f"{sum(m != ' ' for m in marks)}/{len(marks)}"
        shown = proposal.relative_to(root) if proposal.exists() else "MISSING"
        print(f"{name}\t{state}\t{progress}\t{shown}")


if __name__ == "__main__":
    main()
