# draw

Draw or update Component Frames and Screen Artboards in Paper, in the product's font and tokens, and review them by screenshot.

- **Reads:** the approved scope report or Reconcile Plan (or the Sketch Brief), canonical frames and artboards, the [read-the-ui-system](read-the-ui-system.md) result, and the Spec or redesign coverage
- **May change:** Paper pages, Component Frames, Screen Artboards in the open Paper Target
- **Gate:** Scope Approval (Design), Reconcile Approval (Reconcile), none for a Sketch on its own Sketch Page. Overwriting conflicting shared Paper tokens needs its own ask.

## Before the first node

1. Follow the loaded Paper guide for typography, row alignment, clipping, and finishing.
2. Name the product font families and tokens in the report and use them from the first node, so nothing is drawn in a default and corrected later.
3. Reuse or create the approved owner pages, named by the Page arrangement table in [SKILL.md](../../SKILL.md). Get the owner page ID from `create_page` or `get_basic_info`. Pass it explicitly to page-scoped operations such as `create_artboard`. For node-scoped edits, use a parent node verified on that page and the resolved file ID. Reopening an already open file leaves its active page unchanged.
4. When a needed design exists only on a legacy spec-named page or a Sketch Page, copy that node once into its owner page and treat the copy as canonical. Leave the source untouched.

## Components

- One Component Frame per new or changed product Component Family, holding every required state and variation with short labels such as `Default` or `Disabled`.
- Map each family to existing wrappers or primitives where available. Use the visual authority established in [read-the-ui-system](read-the-ui-system.md), including a selected partial design within its confirmed boundary. Preserve supported behavior and accessibility contracts when the target changes a wrapper's anatomy.
- Unchanged primitives get no frame. Draw states evidenced by the Spec, the component contract or retained business behavior. Show role-based visibility on the relevant screen.
- Draw the canonical state first, duplicate it for each variation, apply only the differences, then reorder into reading order. Give overlay, dialog, and menu states a container tall enough to show them whole.

## Screens

- When a partial design supplies the visual foundation for a surrounding flow, draw it in its actual host. Use the host's real content, required actions, and material transitions from entry through return. Identify the supplied reference and the inferred composition in the report.
- One Screen Artboard per materially distinct scenario at each viewport the Spec, product or target design requires. Scenarios that render the same composition share one artboard.
- Clone canonical component nodes into screens and adjust their content and state. For a redesign, draw shared shell and navigation from the target, then reuse those nodes across the screens that consume them.
- Responsive screens keep intent and hierarchy rather than scaling.
- Use real domain content from the Spec, fixtures, or the Sketch Brief. Non-visual requirements stay off the canvas.

Leave Paper comment threads untouched; they are never a channel for requirements or findings.

## Review and finish

- Keep satisfactory existing work and make targeted edits.
- Take one screenshot per owner page or batch and check: required states present once, shared anatomy, content and actions per scenario, spacing, typography, contrast, alignment, and reuse of canonical nodes. Re-shoot only the nodes you fixed.
- After a flow or batch: check screen-to-screen continuity (User Flow), entry-to-outcome (User Journey), or cross-journey consistency (Product Overhaul).
- Call `finish_working_on_nodes` once per batch.

Done when: every approved family has one canonical frame with its required states, every required scenario and viewport has an artboard built from canonical nodes, and the screenshots pass review.
