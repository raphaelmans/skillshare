---
name: Promote to keeper
about: Promote a prototype module to a keeper and verify it once in full.
title: "Promote <module> from prototype to keeper"
labels: keeper
---

## Why

<module> started as a prototype and is now staying. This ticket gives it the same verification a keeper feature gets, once, so that later tickets touching it can be verified against the feature map.

## What to do

- [ ] Swap the `prototype` label for `keeper` on every open ticket in <module>.
- [ ] Write <module>'s user journeys from the user's point of view. Each one names its persona, its entry point and an observable end state (see the keeper section format in the `plan-with-verification` skill).
- [ ] Check that every persona the journeys need is seeded with a login and an entry point. If one is missing, add it to the seed and to the persona table in `VERIFICATION.md`.
- [ ] Add <module> to the feature map in the verify skill: one feature file per user-facing feature, following the map's README.
- [ ] Run one full verification per `VERIFICATION.md`: every journey above, plus the existing journeys the feature map says <module> could affect.
- [ ] Post the proof as a comment on this ticket.

## Done when

Every journey passes with proof posted here, and <module>'s feature-map entries ship in the same PR as any fixes this ticket needed. If a journey fails or can't be checked, leave this ticket open and flag it for review.
