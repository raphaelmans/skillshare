#!/usr/bin/env python3
"""Compare this branch with every other open PR and local worktree branch.

Usage: find_overlaps.py [base-ref]

Prints one block per other PR or branch that carries OpenSpec changes or
shares files with this branch. The signals are candidates only: read the
artifacts before calling anything a conflict.

    spec capabilities   both sides touch the same capability's spec
    change names        both sides carry a change with the same name
    number collisions   both sides add a different file under the same
                        number in one folder (ADRs, migrations)
    shared files        other files both sides touch
"""
import json
import re
import subprocess
import sys
from pathlib import PurePosixPath

CHANGE = re.compile(r"(?:^|/)openspec/changes/(archive/)?([^/]+)/(?:specs/([^/]+)/)?")
SPEC = re.compile(r"(?:^|/)openspec/specs/([^/]+)/")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}-")
NUMBERED = re.compile(r"^(\d{3,})[-_]")
SHOWN = 15


def run(cmd, check=True):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"{' '.join(cmd)}: {r.stderr.strip()}")
    return r.stdout.strip() if r.returncode == 0 else None


def git(*args, check=True):
    return run(["git", *args], check)


def default_base():
    head = git("symbolic-ref", "--quiet", "refs/remotes/origin/HEAD", check=False)
    if head:
        return head.removeprefix("refs/remotes/")
    for ref in ("origin/main", "origin/master", "main", "master"):
        if git("rev-parse", "--verify", "--quiet", ref, check=False):
            return ref
    sys.exit("No base ref found; pass one as the first argument.")


def parse_status(lines):
    """Lines of '<status>\\t<path>[\\t<new path>]' -> {path: 'A'|'M'|'D'}."""
    files = {}
    for line in lines:
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        code = parts[0][:1].upper()
        if code == "R":  # git rename, or GitHub's "renamed"/"removed"
            code = "D" if parts[0].lower() == "removed" else "M"
        files[parts[-1]] = code if code in "AMD" else "M"
    return files


def branch_files(base, ref=None):
    """Files a ref changed since its merge base; the working tree when ref is None."""
    merge_base = git("merge-base", base, ref or "HEAD", check=False)
    if not merge_base:
        return {}
    args = ["diff", "--name-status", "-M", merge_base] + ([ref] if ref else [])
    files = parse_status(git(*args).splitlines())
    if not ref:
        for path in git("ls-files", "--others", "--exclude-standard").splitlines():
            files[path] = "A"
    return files


def signals(files):
    caps, changes, numbered, plain = set(), {}, {}, set()
    for path, status in files.items():
        m, s = CHANGE.search(path), SPEC.search(path)
        if m and not (m.group(2) == "archive" and not m.group(1)):
            name = DATE.sub("", m.group(2)) if m.group(1) else m.group(2)
            changes.setdefault(name, path[: m.end(2)])
            if m.group(3) and status != "D":
                caps.add(m.group(3))
        elif s:
            caps.add(s.group(1))
        else:
            plain.add(path)
        p = PurePosixPath(path)
        n = NUMBERED.match(p.name)
        if n and status == "A":
            numbered[(str(p.parent), n.group(1))] = p.name
    return caps, changes, numbered, plain


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else default_base()
    current = git("branch", "--show-current")
    root = git("rev-parse", "--show-toplevel")
    mine = signals(branch_files(base))

    others = []  # (label, how to read its files, files)
    pr_heads = set()
    prs = run(["gh", "pr", "list", "--state", "open", "--limit", "100",
               "--json", "number,title,headRefName,url,isDraft"], check=False)
    if prs is None:
        print("! Could not list pull requests with gh; showing local worktrees only.\n")
    for pr in json.loads(prs or "[]"):
        pr_heads.add(pr["headRefName"])
        if pr["headRefName"] == current:
            print(f"Own PR: #{pr['number']} {pr['url']}\n")
            continue
        listing = run(["gh", "api", f"repos/{{owner}}/{{repo}}/pulls/{pr['number']}/files",
                       "--paginate", "--jq", '.[] | [.status, .filename] | @tsv'], check=False)
        draft = " (draft)" if pr["isDraft"] else ""
        others.append((f"PR #{pr['number']}{draft}: {pr['title']}",
                       f"git fetch origin {pr['headRefName']} && git show FETCH_HEAD:<path>",
                       parse_status((listing or "").splitlines())))

    base_name = base.split("/", 1)[-1]
    path = None
    for line in git("worktree", "list", "--porcelain").splitlines():
        if line.startswith("worktree "):
            path = line[9:]
        elif line.startswith("branch refs/heads/"):
            branch = line[18:]
            if branch in (current, base_name) or branch in pr_heads or path == root:
                continue
            others.append((f"Worktree branch {branch} (no PR; report only) at {path}",
                           f"git show {branch}:<path>", branch_files(base, branch)))

    found = False
    for label, read_hint, files in others:
        caps, changes, numbered, plain = signals(files)
        shared_caps = sorted(mine[0] & caps)
        shared_changes = sorted(set(mine[1]) & set(changes))
        collisions = sorted(f"{d}/{mine[2][(d, n)]} vs {name}"
                            for (d, n), name in numbered.items()
                            if (d, n) in mine[2] and mine[2][(d, n)] != name)
        shared_files = sorted(mine[3] & plain)
        if not (changes or shared_caps or collisions or shared_files):
            continue
        found = True
        print(label)
        print(f"  read with:          {read_hint}")
        for name, folder in sorted(changes.items()):
            print(f"  carries change:     {name}  ({folder}/proposal.md)")
        if shared_caps:
            print(f"  spec capabilities:  {', '.join(shared_caps)}")
        if shared_changes:
            print(f"  change names:       {', '.join(shared_changes)}")
        for c in collisions:
            print(f"  number collision:   {c}")
        if shared_files:
            print(f"  shared files ({len(shared_files)}):")
            for f in shared_files[:SHOWN]:
                print(f"    {f}")
            if len(shared_files) > SHOWN:
                print(f"    … and {len(shared_files) - SHOWN} more")
        print()
    if not found:
        print(f"No other open PR or worktree branch overlaps this branch (base {base}).")


if __name__ == "__main__":
    main()
