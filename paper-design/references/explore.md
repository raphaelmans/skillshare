# Explore

Draw in Paper from a brief when no planned Change should be required: drafts, wireframes, content or copy previews, A/B comparisons, hi-fi concepts, and journey walkthroughs. The page arrangement in [inventory-tree.md](inventory-tree.md) still applies.

## When this route applies

Select `explore` when the invocation names it, or when the request asks to draft, wireframe, sketch, preview, mock up, or compare variants in Paper, or says no planning artifacts are needed. Requests such as "let's draft a component", "preview the new copy in Paper before code", "create draft wireframes here", and "follow the tree structure, no need for any artifacts" are all `explore`.

Do not resolve a change, check planning readiness, write planning artifacts, or run `scope`. Resolve the Paper target through [workflow.md](workflow.md), run the connection check, and read [ui-system.md](ui-system.md) for the owning workspace when one exists.

## The brief

The Exploration Brief is the intent source in place of a Change Source. Build it from what the user already supplied: their words in this conversation, linked audits or product briefs, existing wireframes, emails or documents they pointed at, and the current Paper and code state.

State the brief back in a few lines before the first write: what is being drawn, which surfaces and viewports, the fidelity, what varies and what stays fixed, and the target page. Then start drawing in the same turn. Do not stop for approval. Ask one question first only when the request contradicts itself on something that changes what gets drawn, such as "everything" against "one screen".

## Where it goes

- Default to a new `Exploration / <Name>` page, named for the subject and purpose in human words, such as `Exploration / Round 2 copy`.
- Give every exploration its own page. Never add a new round, variant set, or topic to an existing Exploration page unless the user names that page as the place to draw. A linked page that holds finished canonical work is a reference, not a destination.
- Draw on canonical owner pages (`<Module> / Components`, `Shared / Components`, `<Module> / <Feature>`) only when the user asks for the canonical tree without planning artifacts. Follow every naming and reuse rule for those pages, and say in the report that the surfaces have no Change Source behind them.
- For a journey walkthrough, use one page with one row per User Journey or User Flow, read left to right, each row labelled with the journey name. Reuse the hi-fi screens by duplicating them; do not redraw.

## Rules for what gets drawn

- **Stay in the established design system.** Use the repository and Paper tokens, the product font, and existing components. An exploration varies only what the user asked to vary. A content or copy comparison changes content and nothing else: no new palette, type, layout direction, or component styling. Propose a new visual direction only when the user asks for one.
- **Start from what exists.** When the surface already exists in Paper, duplicate its canonical artboard and edit the copy. Redraw only what is new.
- **Label variants.** Name artboards so the difference is readable in the page list and on canvas, such as `A · Current` and `B · New content`, and place compared variants side by side in the same order per viewport.
- **Use real content only.** Take copy, names, prices, dates, images, and counts from the brief or the product. Never fill a gap with placeholder text, invented prices, "coming soon" stand-ins, stock photos, or lorem ipsum. When real content is missing, leave the element out and list it under open items.
- **Do not remove or hide existing content on your own judgment.** Keep sections, testimonials, listings, and similar content unless the brief says to remove them. Raise a concern in the report instead of acting on it.
- **Match the fidelity asked for.** Wireframes stay grey-box with real labels; hi-fi uses the full system. Do not upgrade or downgrade fidelity unasked.
- Keep specification prose, matrices, and notes off the canvas, as on every other page.

Review screenshots after each meaningful section and call `finish_working_on_nodes` when done.

## What an exploration is not

- It is not canonical. Exploration pages stay out of the Paper Manifest inventory and cannot own production components or screen coverage. Surfaces drawn on canonical pages without a Change Source enter the manifest only through `init`.
- It carries no Scope Approval, Paper Approval, Design Alignment, or Full Parity verdict.
- It never authorizes production code. A request to build an exploration goes through promotion.

## Report

Report the Paper target, the page with its link, the brief as drawn, what each artboard or row shows, open items needing real content or a decision, and the next step. Offer promotion in one line when the exploration looks like something to build.

## Promote to a change

When the user asks to build, apply, or make an exploration canonical:

1. Write the Change Source through the repository's Planning Convention (see **When no change exists** in [workflow.md](workflow.md)), using the exploration and the conversation as the source. Announce the change and where it was written; do not stop to ask whether to create it.
2. Run `scope` on that change and stop once at Scope Approval. The user reviews the Change Source and the scope together in that one stop.
3. After approval, copy the needed nodes from the Exploration page into their canonical owner pages and reconcile them there. Leave the Exploration page in place.
4. Continue through `components`, `screens`, and, when the request explicitly asked for code, `implement`.
