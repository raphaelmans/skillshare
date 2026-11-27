# Running the Paper Design evals

Give the agent the skill and each case's `prompt` from [evals.json](evals.json). Each numbered case starts a fresh scenario. Keep `expected_output` and `expectations` with the grader. Pass a case when the response or saved artifacts support every expectation. Record the evidence for each check.

Cases 1 through 18 use the supplied repository, Paper and tracker facts as fixtures. Save the agent's reply to each scenario. Case 19 exercises successive actions against local files.

## Case 19

1. Copy `fixtures/pickups/pickups.py` into an empty product repository and commit it to establish the revision. Outside that repository, copy the fixture's `paper.json` and create a `tracker.json` containing `{"specs": [], "tickets": []}`. Use fresh copies for each skill version.
2. Give the agent the product path and the two local service files. Reading `paper.json` simulates inspecting the connected file. To draw, edit the owning page's `nodes` with the artboard or frame name, layout, visible content and controls. Use page and node names to resolve references. The fixture supports inspection of composition and state. Pixel rendering requires live Paper. The tracker file records simulated tracker edits.
3. Send `prompt`. After the agent finishes, save its reply, the product files and both service files. Then send each string in `follow_ups` as a separate user turn in the same session. Withhold later turns and use the agent's actual inventory, sketch and scope report throughout.
4. Grade each checkpoint against its saved state. Resolve requirement IDs from the inventory the agent wrote. Compare node content and source pages across turns, including the state of the canonical pages immediately before approval.
