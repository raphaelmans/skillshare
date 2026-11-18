# open-paper-file

Resolve one Paper Target, confirm Paper is connected, and open it. Run this Step first in every Job, before any report or tracker read; the one check that may come earlier is [find-the-spec](find-the-spec.md)'s test that the tracker config exists.

- **Reads:** the user's message, recent conversation, the Paper Target in `docs/agents/paper.md`, the Paper MCP
- **May change:** nothing

## Resolve the target

Take the first source that yields exactly one Paper file link:

1. The Paper file link in the latest message.
2. Exactly one unambiguous Paper file link in recent conversation.
3. The single Paper Target in a valid `docs/agents/paper.md` (or legacy root `PAPER.md`) under one Manifest Root.
4. Otherwise ask for the link and stop.

Set-up accepts source 1 only.

When several plausible links remain, ask which one. A target comes only from a link: the open file, recent files, `list_files`, the selection, and a bare file ID are never targets. When the link is invalid or inaccessible, ask for a corrected link and stop.

A renamed file that keeps the manifest's file ID is the same target: continue, mention the new name once, and update the recorded name at the next authorized manifest write.

## Connect and open

1. Call `get_guide({ topic: "paper-mcp-instructions" })` as the first Paper call.
2. Call `open_file` with the link and keep the returned canonical file ID.
3. Pass that file ID to every later Paper call that accepts `fileId`.
4. Name the resolved file in the report by its name or link. Keep raw node IDs out of user-facing text.

### If Paper is not connected

When the Paper tools are missing or the guide call fails, stop and say Paper is not connected. Tell the user to open Paper Desktop with the file available and reconnect the `paper` MCP server (`/mcp`); it connects only at startup or reconnect. Run no other Step and ask for no approval until it connects, because a report made before reconnecting has to be repeated.

Done when: one file is open and its canonical file ID is held, or the Job has stopped with a single clear ask.
