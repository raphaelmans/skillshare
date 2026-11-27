---
name: mvp-scope
description: Narrow a plan or task to a useful first version when the owner requests MVP scope, a Wayfinder map names this skill, or the repo links an active mvp.md.
---

# MVP Scope

For a task, consult the project's linked `mvp.md` or use [the scope reference](assets/mvp.md) for this task alone. Continue in the caller's workflow.

## Make the reference persistent

Install the reference when the owner invokes `$mvp-scope` without a task in a product repo or explicitly asks to enable it there.

1. Add the reference as the **MVP scope** section of the root `mvp.md`, creating the file if needed. Reuse an existing section and preserve local edits. For an older “MVP build conventions” section, rename it and add the scoping guidance.
2. Add or update this pointer in the root `AGENTS.md` or `CLAUDE.md`. If one imports the other, edit the shared source once. If both are independent, update both. If neither exists, create `AGENTS.md`.

   ```markdown
   Before planning or doing work, consult [mvp.md](./mvp.md) while its “MVP scope” section exists. If removed, use the repo's normal production conventions.
   ```

To retire the reference on request, remove its pointers and scope section. Preserve project notes and accepted risks. Delete the file if empty.
