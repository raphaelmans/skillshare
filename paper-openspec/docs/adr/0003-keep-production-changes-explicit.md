# Keep production changes behind an explicit implementation slice

`paper-openspec` keeps bare resume, `design`, `all`, fully read-only `parity`, and read-only sync audits non-implementing. Production changes run only through the code-only `implement` workflow, authorized either by an explicit `implement` invocation or by an approved Sync Plan whose approval request separately and explicitly includes code implementation. This boundary prevents design or audit requests from unexpectedly modifying code while allowing sync to reuse implementation rather than duplicate it.
