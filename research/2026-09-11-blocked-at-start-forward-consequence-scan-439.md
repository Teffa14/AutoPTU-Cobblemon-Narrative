# Research — Blocked at Start, Forward Consequence — Pass 439

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE

## Repository basis

The Narrative repository tree at `687985a03895adc3da5a7256c6513eb13f6aad35` was inventoried recursively before writing. The active global NPC focus, canon surfaces, assistance Passes 422–438, schedule/commitment logic, viability owner, replan queue, recent proposals/research and PTU/Kairos boundary were checked before selecting this seam.

Exact source-title searches found no prior use of `80 Days`, `A Highland Song`, or the November 2024 PTU exploration discussion used below as research anchors. No canon file is changed.

## Public source A — 80 Days / inkle

Primary material:

- inkle, `80 Days`: https://www.inklestudios.com/80days/
- Game Developer, `Postmortem: Inkle's 80 Days`: https://www.gamedeveloper.com/business/postmortem-inkle-s-i-80-days-i-
- Short and Adams, `Procedural Storytelling in Game Design`, section discussing 80 Days forward momentum: https://wileywiggins.com/documents/dorf/Short%20and%20Adams%20-%202019%20-%20Procedural%20storytelling%20in%20game%20design.pdf

High-level reusable lesson:

A timed journey does not need every failed or skipped opportunity to stop the story. Time pressure can make missing one opportunity a forward-moving state that changes what becomes possible next. The useful abstraction for Ouros is that a missed or blocked appointment can remain a durable fact and feed later decisions instead of rewinding the world or pretending the promise never existed.

Transformation boundary:

No characters, cities, routes, prose, alternate-history setting, travel economy, dialogue or specific events are imported.

## Public source B — A Highland Song

Primary material:

- inkle official page: https://www.inklestudios.com/a-highland-song/
- inkle press kit: https://www.inklestudios.com/press/a-highland-song/

High-level reusable lesson:

The game ties route choice, weather, hidden paths and a time-sensitive destination together. Reaching the destination late does not erase the journey; route/weather state explains why arrival changed. For Ouros this supports separating an accepted obligation from the travel/access conditions that can later make fulfillment risky or impossible.

Transformation boundary:

No protagonist, family relationship, folklore, landscape, map-fragment system, dialogue, route layout or story event is imported.

## Public source C — PTU exploration discussion

Public discussion:

- r/PokemonTabletop, `Question for Exploration.` (2024-11-22): https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9

Reusable PTU-facing observations:

The discussion describes routes as active spaces rather than empty transitions. Examples include rivers/ravines blocking paths, alternate routes through mines or mountains, environmental Pokémon behavior and local side stories. It also notes that traversal capabilities can invalidate obstacles that were meaningful earlier.

For Ouros this supports a strict distinction between `the route is blocked at the promised start` and `the appointment is permanently impossible`. Current capabilities, permissions, local state and alternative access still need evaluation by their own owners.

Transformation boundary:

No campaign setting, encounter roster, map, NPC, dialogue or authored scene is copied.

## Ouros synthesis

The reusable pattern is:

accepted promise -> later blocker/risk -> semantic start wake -> factual start assessment -> planner chooses what to do next.

The key narrative value is accountability without predestination. The world can remember that an NPC made a promise and that circumstances prevented normal fulfillment. A later scene can distinguish bad faith, unavoidable obstruction, poor preparation, delayed communication, heroic improvisation or successful recovery using subsequent evidence rather than rewriting the original agreement.

## PTU / Caelo mechanical boundary

Pass 439 adds no tactical resolution.

The reduced narrative form uses semantic time, accepted commitments, private evidence, viability history and event-driven replanning only.

A richer field version can require travel, access, inspection, escort, retrieval, protection or extraction. If that version becomes tactical, it must classify every relevant permanent engine family independently. In particular, an environmental obstruction does not imply that complete movement, forced movement, hazards, reactions, delayed effects or Trainer Feature interrupts are already supported.

## Live engine evidence checked

AutoPTU-Java `main` was rechecked at `d2b3c593d235f1c841ca936df91c42c4a881f000` (PR #447). The current head provides specific server-authoritative Quick Switch planning/trigger behavior. This remains narrow evidence and does not verify complete action economy/initiative, reactions/interrupts or Trainer Features/perks as whole families.

AutoPTU Python `main` was rechecked at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head states that the change is presentation-only and does not alter battle rules or outcomes.

No engine repository is modified by this pass.
