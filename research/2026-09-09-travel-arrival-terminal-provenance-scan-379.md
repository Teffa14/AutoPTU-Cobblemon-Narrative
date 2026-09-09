# Travel arrival and terminal provenance scan — Pass 379

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-09
Canon effect: NONE

## Repository inspection and deduplication

The Narrative repository tree was inventoried recursively at `a143ea570bc1c9840de7e9a79efe2301ae1119ed` before writing. Current focus, canon governance, world-agent provenance owners through V17, semantic travel, AutoPTU handoff/result-ingress contracts, implementation fixtures, regressions and recent research/proposals were cross-searched.

Recent anchors including Pokémon World Tour: United, The Reckless Rollers, Adventures in the Millennium, Pokémon Stalactite, Pokémon Desolation, Pokémon Gaia, Pokémon Realidea System, Pokémon Prisme, Pokémon Odyssey, Pokémon Nova, Pokémon Bushido, Valoryn and other repeatedly processed sources were not reused as primary inspiration.

`Pokémon: Adventures in the Sun` was checked by title and source URL and had no prior research hit. `Pokémon Infinity` was checked by project/developer identifiers and had no prior project hit; unrelated references to the canonical term “Infinity Energy” were not treated as duplicates.

## Source 1 — Temporal durable event history

Public source:
https://github.com/temporalio/documentation/blob/main/docs/encyclopedia/workflow/workflow-execution/event.mdx

Temporal documents an append-only Event History used both to recover execution after crashes and to distinguish activity lifecycle events such as scheduled, started, completed, failed, timed out and canceled. An implementation detail is especially useful for Ouros: some start evidence can be delayed or optimized in history, so terminal state should be represented deliberately rather than reconstructed from the current workflow state.

Reusable Ouros lesson:

- preserve lifecycle transitions as evidence, not as retrospective labels;
- a terminal record should reference the earlier start that it closes;
- restart should replay the transition when deterministic source inputs exist;
- completion and failure remain different terminal families;
- current location, cleared UI or later state must not silently become historical proof.

No Temporal APIs, schemas, retry semantics or operational rules become Ouros canon.

## Source 2 — Pokémon Tabletop United campaign pitch: Adventures in the Sun

Public source:
https://www.reddit.com/r/PokemonTabletop/comments/l8bnmu

The public campaign pitch describes trainers beginning at a school, completing several small local quests, then setting out on a larger journey. The useful abstraction is scale transition: local obligations can form a bounded pre-departure phase, while physically setting out is a later world event with its own consequences.

Reusable Ouros lesson:

A field-team story can begin with mundane preparation, permissions, collection or training, then become a real expedition only when the team departs. Arrival at a destination should likewise be an explicit event rather than an inference from the earlier decision to travel.

No Ralakos setting, Sunshine City, characters, quest sequence, school structure, dialogue or encounter content is imported.

## Source 3 — Pokémon Infinity

Public source:
https://www.eeveeexpo.com/infinity/

The completed fan game advertises a world-time system, dynamic weather, extensive exploration and a design intent that rewards curiosity and discovery. The useful structure is that travel can expose information that was not available when the journey began; the destination is a new evidence state, not merely the endpoint of a timer.

Reusable Ouros lesson:

An expedition can be selected and started for one reason, reach its destination successfully, and still discover that the original objective has changed, expired or become impossible. Travel completion should therefore remain separate from mission success.

No Egho region, amnesia premise, characters, Fakemon, custom mechanics, locations or story is imported.

## PTU/Caelo authority cross-check

Project-internal PTU/Caelo material remains rules and setting authority. This pass does not introduce species, Moves, Abilities, Items, Trainer Features, encounter tables, regional geography or a new PTU resolution rule.

Semantic world travel remains graph-level world simulation. It does not claim PTU square movement, terrain resolution, interception, forced movement or tactical traversal.

The existing AutoPTU semantic-result ingress contract was inspected. It defines typed result ingestion and accepted/quarantined states, but the current global-NPC runtime does not expose a replayable `AUTOPTU_RESOLVED` transition tied to the action-start owner. Pass 379 therefore does not invent that terminal family.

## Live engine evidence

Read-only AutoPTU-Java head inspected: `6cc66d91d286fab06365cf37d88dd04038589195`, merge #415. The change adds oracle-backed parity for authoritative round rollover state: round number, initiative order/cursor and first actor after rollover. This strengthens that lifecycle seam only.

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head remains presentation-only viewport synchronization and does not change battle rules or outcomes.

No engine repository was modified.

## Pass 379 candidate

Implement one terminal state that already has deterministic evidence in the Narrative runtime: semantic travel destination arrival.

Proposed owner:
`OUROS_NPC_ACTION_TERMINAL_PROVENANCE_V1`

Supported Pass 379 terminal kind:
`TRAVEL_DESTINATION_ARRIVED`

The terminal record must reference a prior `TRAVEL_EDGE_STARTED`, preserve the replay inputs and final travel state, replay to `ARRIVED`, and fail closed if source-start provenance diverges.

Explicitly outside this slice:

- generic action success/failure;
- multi-step mission completion;
- AutoPTU session resolution;
- AutoPTU semantic-result ingress linked to a global NPC action;
- Minecraft playback completion;
- narrative objective success.

This leaves the causal boundary precise:

`PLAN_SELECTED -> ACTION_STARTED -> TRAVEL_DESTINATION_ARRIVED`

and separately:

`AUTOPTU_BINDING_ACCEPTED != AUTOPTU_RESOLVED != AUTOPTU_RESULT_INGRESSED`.
