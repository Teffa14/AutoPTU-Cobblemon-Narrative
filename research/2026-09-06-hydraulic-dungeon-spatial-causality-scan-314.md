# Hydraulic Dungeon Spatial Causality Scan

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-06
Pass: 314

## Purpose

This pass deliberately moves away from the recent custody/revision administration seam and looks for a mechanically legible exploration structure that can enrich Ouros without requiring missing AutoPTU rules.

Repository inspection before research found existing work on ecology, civic/public-works hooks, crisis/rescue, encounter contracts, persistent consequences and revisitable world state. Searches for `sluice`, `waterworks` and `Ashen Frost` did not identify an already-authored Ouros concept to extend, so a hydraulic infrastructure dungeon is a low-duplication candidate.

Nothing in this note changes canon. Any institution, region, species, water right, historical incident or hydraulic facility mentioned below remains a design candidate until separately approved.

## Public sources reviewed

### Pokémon Ashen Frost

Source: https://pokemundo.com/pokemon-ashen-frost/

The public overview describes a Pokémon fan game organized around nineteen mysteries, a new region and changing weather. The useful abstraction for Ouros is not its cases or setting. It is the idea that investigation can be a repeated mode of play across a region instead of a one-off detective quest, while weather changes the context in which clues are encountered.

Transform for Ouros: make the waterworks one investigation in a larger family of infrastructure/ecology mysteries. Returning under a different water or weather state can expose evidence that was physically unavailable before.

Do not copy Ashen Frost characters, cases, region, dialogue, maps, Pokémon distribution or mystery resolutions.

### Pontcysyllte Aqueduct and Canal / Canal & River Trust STEM material

Source: https://www.pontcysyllte-aqueduct.co.uk/object/windlass/

The public educational page explains the core spatial relationship that matters for this design: sluice gates control water associated with lock operation and water levels. That provides a grounded causal model for a puzzle space. A control does not open an arbitrary fantasy door; changing one water-control state can alter traversability somewhere else.

Transform for Ouros: use linked gate states, visible water marks, spill channels and bypasses so players can predict consequences from the environment. Avoid importing real engineering specifications, operating procedures or safety claims.

### Water Temple design history

Source: https://en.wikipedia.org/wiki/Water_Temple_%28Ocarina_of_Time%29

The useful historical design lesson is two-sided. Changing water level can make one physical space support several traversal states. The same structure also became famous for navigation friction and repeated backtracking; later versions added clearer visual guidance toward water-level controls.

Transform for Ouros: every hydraulic state should have strong visual landmarks and local feedback. Do not require the player to cycle the entire facility repeatedly just to discover which remote branch changed. A gate operation should communicate at least one downstream effect through sound, sight, gauges, wet-lines, moving debris or an updated route marker.

Do not reproduce the Water Temple layout, room sequence, puzzles, enemies, boss, key structure or distinctive set pieces.

### Water Works level-design portfolio

Source: https://www.kirkbaltzell.com/waterworks

This public level-design write-up describes a Half-Life 2 level built around manipulating water flow through a facility and explicitly frames the work in terms of systems, layout, flow, combat and a multi-step puzzle. The reusable lesson is to make the environmental system serve traversal and encounter composition together rather than placing a puzzle in a disconnected room.

Transform for Ouros: hydraulic choices should affect route availability, observation points, encounter geometry and what evidence becomes visible. The control system should remain understandable without copying the Half-Life level, objectives, technology, characters or implementation.

### Pokémon Aftershocks

Source: https://finalshowfilms.com/shows

Final Show Films publicly lists Pokémon Aftershocks as an actual-play adventure using Pokémon Tabletop United. The listing is sparse, so this source is not used to infer specific mechanics or plots. Its value here is provenance breadth: PTU continues to support campaign-format narrative play outside the previously processed shows.

Transform for Ouros: none required beyond retaining PTU actual-play campaign structure as a valid reference pool. Do not infer rules or campaign content that the public listing does not state.

## Reusable structures extracted

A hydraulic dungeon works best when the environment exposes cause and effect. A gate state should alter a small, comprehensible set of downstream spaces. The player should be able to form a model of the facility from labels, wet-lines, debris direction, sound, gauges and observed Pokémon behavior.

Multiple entrances prevent one missed clue from blocking the adventure. A public spillway, maintenance gallery and dry emergency bypass can each reveal a different part of the same system. They can converge on the same central control problem without becoming three unrelated dungeons.

Environmental evidence can separate chronology. Old mineral marks indicate long-term water levels. Fresh tool wear indicates recent handling. Drift caught above a current waterline suggests a prior surge. A maintenance diagram can explain intended flow while the actual environment shows what really happened.

Competing stakeholders do not require a villain. Stable supply, safe maintenance access and habitat continuity can all be legitimate goals that conflict under constrained water availability. A later deliberate gate change can still carry consequences without automatically implying malicious sabotage.

Revisits should change meaning, not merely reset enemies. Repairs, seasonal flow or a newly accessible bypass can expose rooms, habitat traces and records that were unavailable during the first visit.

## PTU / project-source boundary

No numerical hydraulic rule is adopted in this pass. No custom `current`, `slip`, `drowning`, `soaked`, `pressure` or water-level status is invented.

The reduced adventure can use authored world-state transitions plus already-audited basic traversal. If a later implementation uses PTU Swim capabilities, Athletics, Pokémon Moves, Abilities, Trainer Features, weather, forced movement or environmental damage, each exact interaction must be cross-checked against the authoritative project source before it becomes a mechanical contract.

The narrative repository currently exposes Kairos material under `sources/kairos`. No Caelo source directory was identified in the inspected narrative root. This pass therefore treats any Caelo-specific assumption as UNVERIFIED rather than filling the gap from memory.

## Candidate Ouros synthesis

Working concept: The Three-Gate Waterworks.

The facility has three hydraulically connected branches: an intake/distribution gate, a maintenance bypass and a habitat side-channel. Their exact names, ownership and region remain unapproved.

The opening symptom is contradictory downstream state: one pool repeatedly dries while another overtops even though the available operating record suggests normal distribution. Investigation can begin from more than one entrance.

The intended mystery is systemic rather than switch-based. Players reconstruct which gate states can create the observed water marks, then compare that model with maintenance records, recent tool marks and ecological observations. A human action may be involved, but the design remains valid if the final cause is maintenance error, emergency action, legitimate habitat protection, infrastructure failure or several concurrent causes.

## Design guardrails

Every control must have readable local feedback.

No solution requires exhaustive permutation testing of every gate state.

At least two evidence paths should support the central causal inference.

Combat cannot be the only way to advance the water-state puzzle.

Pokémon behavior can provide evidence only when species behavior and communication assumptions are separately validated.

The reduced implementation must preserve the same stakeholder conflict and causal mystery without tactical currents or dynamic water simulation.
