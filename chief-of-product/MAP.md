# Run a map

The **map** route of [`chief-of-product`](SKILL.md): an effort with fog. A thin layer over `wayfinder`, which owns the map: its body, its tickets and every operation on them. Here the CPO answers the decisions the owner would otherwise be asked, and once the map is clear the effort carries on into a build the owner can react to.

Where a step here differs from a wrapped skill, this file wins: each difference is deliberate. The words, the way the CPO speaks and the brief are in `SKILL.md`.

**Reached from a map's Notes** in a `/wayfinder` session the owner started, not one a chief-of-product session dispatched: work that session's one ticket as wayfinder says, answering as the CPO by step 2's rules. Write the map, the glossary and the ADRs yourself, and put any reserved question to the owner, who is there.

## 1. Chart with the owner

Follow wayfinder's **Chart the map**, with four changes.

- The live grilling covers what only the owner can say: the destination, who it is for, where scope ends, and any reserved decision already in view. Fanning out across the rest of the space is your legwork.
- Before the owner confirms the Destination, give your **case**: the need, the benefit to the business, the smallest version worth building, and the strongest reason to leave it unbuilt. Recommend one of build, build the smallest, or drop.
- Record in **Notes** that each session consults `chief-of-product` and that the CPO takes the clear map into a build. Include the MVP reference when it applies. Record a keeper request when the owner makes one.
- Leave the research tickets to step 2, which dispatches every frontier ticket.

Given a map that already exists, add those Notes lines and go to step 2. When charting surfaces no fog there is no map to settle: take the **concern** route in `SKILL.md` from its step 3, with this conversation as the source.

Done when the owner has confirmed the Destination with the need written in it, the Notes carry those lines, and the tickets are created and wired.

## 2. Settle the frontier

Give every frontier ticket its own subagent with a fresh context window. Run them concurrently; one that writes files works in its own worktree. Tell each one it is dispatched by this skill, and hand it context pointers to the map, its ticket, the mandate and this skill.

Each subagent works its ticket as wayfinder's **Work through the map** says (claim, resolve by type, comment, close, create and wire new tickets), answering as the CPO where wayfinder waits for the human:

- **Grilling**: draft the round in the `grilling` format, facts looked up, a recommended answer on every question. A comment on the ticket that opens with **Owner decision** is binding: build on it and leave it unasked. Answer every other question from the written sources. Where two of them disagree, the question is reserved. Where none speaks, your recommendation stands and the settlement is shaky. Report the glossary terms and ADRs the answers call for, and write none.
- **Prototype**: build the artifact, choose among its variants the same way, and link it.
- **Task**: do it where an agent can. A step only a human can take is reserved.

A resolution comment opens with **CPO settlement** and gives: what is built, in the glossary's words; what is deliberately left out; and the rule it rests on, quoted from its source, or **shaky**. A ticket holding a reserved question stays open and assigned, and its comment opens with **Reserved**: what is settled so far, then each question that waits, with a recommended answer.

Subagents report; you alone write the map body, so concurrent tickets cannot overwrite each other. From each report: append the context pointer to **Decisions so far**, its kind in front (`Owner decision:` when the owner answered any part of the ticket, else `CPO settlement:`); clear graduated fog; record out-of-scope rulings; update the tickets the answer invalidates. Hold the glossary terms and ADRs it proposes until step 3. When a subagent ends without a report, unassign its ticket and dispatch it again. Fog that waits on no ticket is yours to turn into tickets.

Done when every open ticket is reserved or blocked by a reserved one, and any fog left names the reserved ticket it waits on.

## 3. Review the settlements

Dispatch one reviewer subagent with a fresh context window and pointers to the map and the written sources. It reads every ticket closed since the last review, takes each **Owner decision** as given, and reports each CPO settlement that:

- settled a one-way door, or guessed a fact only the owner holds;
- contradicts a written source, or settles a question on which two of them disagree;
- contradicts another settlement;
- rests on no source and is not marked shaky;
- leaves the map's need untrue for a person who starts from one of the journey's entry points.

A settlement that only lacks its shaky mark gets the mark in place. Of two settlements that contradict each other, reopen the later one. For every other finding, reopen the ticket, strike its line from **Decisions so far** and undo what its report changed on the map. Mark it **Reserved** when the finding is a one-way door, an owner's fact or a disagreement between sources, or when this is the ticket's second finding; otherwise unassign it with the finding as a comment, so step 2 settles it again.

Then write the glossary terms and ADRs the surviving settlements proposed, and commit them to the branch the build will start from.

Done when every new settlement has been read and every finding is reopened.

## 4. Sit down with the owner

When anything is reserved, run one `grilling` sitting over every reserved question on the map, most consequential first, and let it run its rounds until the owner confirms. Mark each question one-way or two-way, so a bulk yes is read as covering the two-way ones and each one-way door gets its own answer. Comment each answer on its ticket as an **Owner decision**, then unassign the ticket so step 2 finishes it. Where the answer settles a disagreement between two written sources, amend the one that lost, so the question stays answered.

Repeat steps 2 to 4 until the map is clear.

## 5. Plan and build

Hand the clear map to `to-spec`, then `to-tickets`, then `implement-spec` on one integration branch. In repos with `VERIFICATION.md`, use `plan-with-verification` for planning by default outside MVP scope, or by explicit request under MVP scope. On that route, choose prototype unless the map's Notes say keeper.

Done when `implement-spec` has finished: every ticket's work is on the integration branch and the repo's checks pass. The pull request stays unmerged.

## 6. Check, preview, brief

Run the **gap check** in `SKILL.md` on the integration branch and fix what it finds.

Push the branch. Use the pull request `implement-spec` opened, or open one, and write its body with `pr`. Deploy the branch to the repo's preview environment, as its deployment doc describes, when that preview runs on its own data. Everything else follows **Release** in `SKILL.md`.

Then send the **brief** from `SKILL.md`, and post it as a comment on the map.

Done when the build is reachable at a link, or the brief says what it waits for.

## 7. Take the tweaks

Follow **Take the tweaks** in `SKILL.md`. On a map, each reaction also gets a `wayfinder:grilling` ticket: record the owner's answer as its resolution, then close and index it, naming the settlement it replaces. A reaction too big for one session goes through `to-tickets` first.

Done when the owner accepts the build.
