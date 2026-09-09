# Allocation application restart provenance scan — Pass 367

Status: RESEARCH / PROVENANCE. NOT CANON.
Date: 2026-09-08

## Repository review first

The complete recursive repository tree on `main` was inspected before writing. Relevant content was then checked directly: current global-NPC focus, Passes 347–349 ownership contracts, V7/V12 checkpoint work, reservation lifecycle, Pass 349 executable application records, tests and CI. Existing research was searched for candidate source families before selecting new material.

The selected gap is durable Pass 349 application history. Ouros can already remember a historical resource conflict and the authorized institutional decision. Without application persistence, restart can still lose whether that decision had actually reached the operational reservation projection.

## New source 1 — ESO Service Mode scheduling and execution

Sources:
- https://www.eso.org/sci/observing/phase2/SMPhilosophy/SMScheduling.html
- https://support.eso.org/en-GB/kb/articles/program-execution-status
- https://www.eso.org/sci/observing/phase2/SMPolicies/ExecutionOverheads.html

ESO publicly separates programme allocation, preparation of Observation Blocks, queue ranking/scheduling and actual execution. Approved work enters a queue, execution depends on priority/constraints/current conditions, and an allocated programme can therefore exist before any particular observation is executed.

Reusable Ouros structure: authorization or prioritization does not prove operational execution. Persist the decision and the later application/execution as separate facts. A downstream actor may rationally continue to see an older operational state during the interval between them.

Transformation boundary: Ouros does not import ESO governance, astronomy policy, ranking formulae, telescope operations or terminology as regional canon.

## New source 2 — Pokémon World Tour / PTU: VVV public campaign post

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/1m6zdes

The public 2025 campaign post describes a long-running project derived from Pokémon Tabletop United, with an earlier campaign completed, a new campaign already running, streamed sessions and a heavily modified automated sheet.

Reusable Ouros structure: campaign continuity can span substantial system iteration while preserving ongoing jobs, consequences and world history across sessions. This supports keeping small operational facts durable instead of treating them as disposable scene flags.

Transformation boundary: PTU: VVV homebrew changes, campaign characters, locations, plots and custom mechanics have no rules authority in Ouros and are not copied.

## New source 3 — Pokémon Realidea System

Sources:
- https://www.pokeuniverso.com/2022/11/pokemon-realidea-system-android-y-pc.html
- https://www.adrivelive.com/video/803e97a6-5cef-46ce-9528-c67f731d14e3

Public descriptions identify a fan game built around a new region, mysteries, exploration and a mission/quest system alongside the normal trainer journey.

Reusable Ouros structure: secondary obligations and discoveries can coexist with a larger adventure path. An equipment-allocation problem can remain meaningful across travel or exploration without becoming the main plot.

Transformation boundary: no characters, region, antagonist, technology, dialogue, quest sequence, fakemon, bespoke Moves or Abilities are imported.

## Synthesis for Ouros

A useful persistent-world distinction is:

`CONFLICT_OBSERVED -> DECISION_MADE -> APPLICATION_RECORDED -> NOTICE_CREATED -> NOTICE_DELIVERED -> ACTOR_KNOWS`

Each transition can occur at a different semantic time and belongs to a different owner. Restart must preserve which transitions happened instead of inferring them from the final calendar, current custody or NPC behavior.

This supports investigation without omniscience. One scheduler may know the decision was applied. A field technician may still act from an older booking because no notice reached them. A later closed booking does not erase that it was operationally displaced earlier.

## PTU / Caelo boundary

Internal project authority remains the indexed PTU Core/Pokédex material, Caelo Player's Guide, Caelo rulebook/errata and region/location/encounter material where available. None of the external sources in this scan establishes battle rules or regional facts.

Pass 367 changes persistence architecture and adds non-canon scenario material only.

## Engine dependency note

The reduced scenario requires no AutoPTU capability. A field version after equipment pickup can involve an optional tactical interruption. Targeting/footprints/range/LoS, base movement legality, core calculations, audited action-economy/initiative primitives and ordinary AI legal-action infrastructure remain verified only within previously audited scopes. Complete movement, turn/round lifecycle, stateful damage, statuses and advanced objective actions remain partial or gated. Terrain/weather/hazards/zones/reactions are mechanism-specific. Moves, Abilities, Items and Trainer Features remain individually gated. Objective-aware tactical policy and Minecraft/Cobblemon/Craftics cargo/objective playback remain blocking/partial.
