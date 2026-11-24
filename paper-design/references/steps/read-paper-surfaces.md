# read-paper-surfaces

Read exactly the canonical frames and artboards a Job needs, with exact values from Paper rather than screenshots.

- **Reads:** Paper frames and artboards via `get_tree_summary`, `get_jsx`, `get_computed_styles`, `get_tokens`
- **May change:** nothing

## Read

1. Scope the read to the surfaces the Job names. For a redesign, follow its coverage record to the target artboards, component states and shared layout, including surfaces with no ticket yet. Legacy spec-named pages and Sketch Pages are read when they hold the needed design.
2. Start with tree summaries, then batch `get_jsx` and `get_computed_styles` for nodes that need exact comparison.
3. Read tokens directly. Take sizes and colors from computed styles, never from screenshots or the selection.
4. When the Job writes the surfaces up, capture what they show: screens and their scenarios, states, real text, actions, navigation, and which canonical components they use.

## Reuse

Keep the evidence in working context. Reuse it across Jobs in the conversation while the Spec, Paper Target, relevant nodes, requested boundary, and repository context are unchanged; re-read only stale or missing surfaces.

Done when: every surface the Job named has structure and exact styles in working context, or is recorded as Pending Evidence.
