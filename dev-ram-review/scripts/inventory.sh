#!/bin/sh
# Keep the full snapshot available even when the agent's output is truncated.
set -eu
export LC_ALL=C
umask 077
report=$(mktemp "${TMPDIR:-/tmp}/dev-ram-review.XXXXXXXX")
trap 'rm -f "$report"' EXIT
raw=$(mktemp "${TMPDIR:-/tmp}/dev-ram-raw.XXXXXXXX")
trap 'rm -f "$report" "$raw"' EXIT
ps -Aww -o pid=,ppid=,uid=,rss=,pcpu=,etime=,comm= > "$raw"
printf '%8s %8s %8s %10s %6s %14s  %s\n' PID PPID UID RSS_MiB CPU% ELAPSED EXECUTABLE > "$report"
sort -k4,4nr "$raw" | awk 'NF >= 7 {
    pid=$1; parent=$2; uid=$3; rss=$4; cpu=$5; elapsed=$6
    for (i=1; i<=6; i++) sub(/^[[:space:]]*[^[:space:]]+[[:space:]]+/, "")
    printf "%8d %8d %8d %10.1f %6s %14s  %s\n", pid,parent,uid,rss/1024,cpu,elapsed,$0
}' >> "$report"
rm -f "$raw"
trap - EXIT
printf '%s\n' "$report"
