# Scenario Screens

Compose Paper screens from the component families required by the approved Design Scope.

## Determine the screen matrix

Follow the approved User Flow or Design Batch sequence. Create a screen artboard for each materially distinct visual scenario and each viewport explicitly required by the artifacts or established implementation. Combine scenarios when they render the same composition and differ only in non-visual behavior.

Do not automatically generate mobile, tablet, and desktop. Use artifact requirements, repository breakpoints, routes, and existing product targets to select viewports. Use Paper's default device dimensions only when a required target has no established dimensions.

Exclude non-visual requirements such as metadata, cache invalidation, ISR, persistence, or service-worker behavior from the canvas. Keep them in the parity matrix for artifact-to-code review.

## Compose screens

1. Ensure each changed component used by a screen has a complete canonical component frame. Load the component slice for missing dependencies.
2. Reuse or create artboards named `Screen / <Surface> / <Scenario> / <Viewport>`.
3. Clone or duplicate canonical component nodes into screens. Do not independently redraw changed components.
4. Adjust cloned content and state-specific properties without changing the shared anatomy unless the scenario requires it.
5. Reuse established application chrome, navigation, layout containers, primitives, and tokens.
6. Use realistic domain content from artifacts or existing fixtures without exposing specification prose.
7. Preserve separate artboards for states that materially alter hierarchy, available actions, visibility, or navigation.

For repeated rows, reserve fixed-width lanes for icons and trailing actions. For responsive screens, preserve intent and hierarchy rather than mechanically scaling the desktop composition.

## Review

After each material screen section, screenshot and verify:

- The scenario's visible content, actions, navigation, and conditional elements are present.
- Changed components match their canonical frames and are reused rather than redrawn.
- Repeated elements align across rows and states.
- Typography, spacing, contrast, and artboard fit meet the Paper review checklist.
- No requirement matrix, acceptance criteria, annotations, or review comments appear in the artboard.

Use targeted fixes and switch clipped artboards to `height: "fit-content"`; do not guess replacement heights or recreate the screen.

After completing a dependency-ready flow or batch, validate upward at the approved scope: screen-to-screen continuity for User Flow, entry-to-outcome completion for User Journey, and cross-journey consistency for Product Overhaul. Do not create journey maps, flow notes, or validation annotations on the canvas.

## Completion contract

Consider the slice complete when every material visual scenario has the required viewport artboards, all changed components originate from canonical component nodes, and non-visual requirements remain off-canvas.
