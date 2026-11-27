# MVP scope

Use the prompt to identify what a person needs to do and what the owner wants to learn. Keep the smallest end-to-end path that answers that question. Revisit the scope when new work appears. Preserve explicit requirements and the requested UX. Use existing patterns and defer abstractions, configuration and scale work until needed.

**With Wayfinder**, propose that path as the **Destination**. Once confirmed, ticket only decisions needed to reach it. Put deferred work in **Out of scope**. For a rep capturing a lead during a call, saving one lead is enough. Bulk import can wait. In **Notes**, point to the repo's `mvp.md` while its MVP scope section exists. For a map-only request, name `mvp-scope` there.

**With Chief of Product**, recommend the v1 journey and carry it into the implementer handoff. State what the user can do and what can wait. The mandate governs reserved decisions and releases.

For a planning request, deliver the revised scope in the current map or recommendation.

**Formal verification** requires an explicit request for the specific work, including planning it, running it, collecting proof or creating or maintaining a verification skill. When requested, follow the repo's `VERIFICATION.md` or equivalent instructions. Leave tickets that require proof open until it exists.

For implementation, use these defaults.

- **Checks.** Exercise the ordinary case with an existing focused check or a quick manual pass. Add one common failure case if it affects a user's decision or recovery. Honor repo test bans and required checks. Write new automated tests only when requested or required. Skip speculative edge cases and coverage targets.
- **Database.** Edit the schema source and seed data for a fresh database. Skip writing or running incremental migrations and backfills by default. If a reset is necessary, name the database, environment and data it will erase. Ask once and reset only the approved disposable target. This also applies to resets inside launchers. If data is shared, live or must survive, keep it intact and surface the decision.
- **Accepted risks.** Make reversible trade-offs yourself. Record a material shortcut, its consequence and when to revisit it. Use a sibling **Accepted risks** section in the project's `mvp.md` or the current handoff for a one-off request. Keep access controls and data protections in place, including data isolation.
- **Handoff.** Say what the owner can try, what you actually checked and what feedback would change the next iteration. Stop when the requested path is ready for that feedback.
