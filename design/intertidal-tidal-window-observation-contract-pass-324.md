# Intertidal tidal-window observation contract — Pass 324

Status: DESIGN CONTRACT / NON-CANON
Date: 2026-09-07

## Purpose

Define a reusable Ouros contract for persistent coastal features whose access, observability and ecological state vary with authored tide phase. This contract must preserve world-agent knowledge boundaries and keep PTU mechanics outside Minecraft/Cobblemon authority.

## Core state separation

The following values must remain independent:

1. persistent feature identity;
2. authored tide-phase state;
3. current physical exposure/submergence state;
4. route/access state;
5. ecological observation state;
6. observation timestamp and provenance;
7. per-agent receipt;
8. per-agent interpretation/belief;
9. institutional decision/publication;
10. tactical PTU state when a structured encounter exists;
11. Minecraft/Cobblemon/Craftics presentation.

A rendering change must never collapse these layers.

## Required invariants

`FEATURE_IDENTITY != TIDE_PHASE`

`TIDE_PHASE != ROUTE_ACCESS_DECISION`

`OBSERVED_EXPOSED != SAFE_TO_TRAVERSE`

`OBSERVED_SUBMERGED != PERMANENTLY_CLOSED`

`LOW_TIDE_EVIDENCE != HIGH_TIDE_WORLD_TRUTH`

`PUBLIC_NOTICE != UNIVERSAL_NPC_KNOWLEDGE`

`MINECRAFT_WATERLINE != PTU_RULE_AUTHORITY`

## Authoritative world model

Each intertidal feature should have a stable ID and an authored state record.

Recommended fields:
- `feature_id`;
- `site_id`;
- `feature_type`;
- `semantic_time`;
- `tide_phase_id`;
- `exposure_state`;
- `route_state`;
- `observation_refs`;
- `last_authoritative_change_event_id`;
- `decision_refs`;
- `publication_refs`;
- optional `autoptu_encounter_binding`.

The tide phase may be deterministic, authored or event-driven. Pass 324 does not require astronomical simulation.

## Tide-phase model

A reduced implementation may use finite authored states such as:
- `HIGH`;
- `FALLING`;
- `LOW_WINDOW`;
- `RISING`.

The phase changes only through an authoritative world-state event. A renderer, player clock display or local particle effect cannot mutate it.

A future richer simulation may use more detailed water-level data, but it must preserve the same feature identity and provenance contract.

## Exposure and route state

Exposure should be feature-scoped.

Example exposure states:
- `EXPOSED`;
- `PARTIALLY_EXPOSED`;
- `SUBMERGED`;
- `UNKNOWN_CURRENT`.

Example route states:
- `OPEN`;
- `WINDOWED_ACCESS`;
- `MAINTENANCE_ONLY`;
- `RESTRICTED`;
- `CLOSED`;
- `MONITORING`.

These are world-state descriptors. They are not PTU statuses and do not imply tactical modifiers.

## Observation contract

Every observation should preserve:
- `observation_id`;
- `observer_id` or source identity;
- `feature_id`;
- `semantic_time`;
- `tide_phase_id` if known to the observer;
- observed fact;
- confidence if the existing evidence model requires it;
- provenance root;
- optional instrument or record source;
- superseding world event if later known.

Examples:
- `LOWER_STEP_EXPOSED_OBSERVED`;
- `LOWER_SHELF_SUBMERGED_OBSERVED`;
- `DEBRIS_MOVED_SINCE_LAST_VISIT`;
- `SERVICE_CACHE_ACCESSED_OBSERVED`;
- `MARKER_POSITION_CHANGED_OBSERVED`;
- `OBSERVATION_STALE_AFTER_TIDE_CHANGE`.

An observation never grants knowledge to an NPC until the information system records explicit receipt or the NPC made the observation directly.

## Interpretation and stale evidence

A previously accurate observation remains in history after the tide changes. It may become stale for a current access decision while remaining valid evidence about the earlier state.

Do not rewrite or delete the observation to represent staleness.

Instead, bind a later event or assessment that limits its current applicability.

This preserves causal history for later disputes, corrections and trust consequences.

## Public information boundary

A public route notice should identify the scope it actually governs.

A broad notice such as `COASTAL_STAIRS_OPEN` should be avoided when the decision applies only to upper features or a limited tide window.

Publication, audience expansion, receipt and belief remain governed by the existing global NPC information architecture. Tide changes do not automatically update every NPC.

## Reduced implementation contract

The reduced version is the default admission target.

It requires:
- stable feature IDs;
- semantic time;
- authored phase transitions between scenes or world events;
- feature-scoped route state;
- provenance-backed observations;
- explicit NPC receipt;
- ordinary route planning on open edges;
- blocked or unavailable edges where richer movement is unsupported;
- durable decisions and consequences;
- later revisits.

It does not require:
- dynamic current simulation;
- continuous water-level interpolation;
- swimming mechanics;
- drowning;
- slippery footing;
- underwater LoS;
- wave knockback;
- rescue reactions;
- environmental damage;
- custom statuses;
- tide-specific Moves, Abilities, Items or Trainer Features.

## Rich implementation admission gates

A mechanically rich encounter may only use a behavior when the exact capability family is verified.

Targeting / footprints / range / LoS:
ordinary contracts remain usable on exposed authored terrain. Underwater visibility, water-surface occlusion, spray/fog concealment or changing sightlines require additional verified contracts.

Base movement legality:
ordinary movement is usable on authored open surfaces. Swimming, wading, climbing wet rock, jumping gaps, footing penalties or species-specific traversal require source-backed mechanics.

Complete movement:
required for currents, wave push/pull, knockback near water, rescue pulls, interception and other forced movement.

Core calculations:
ordinary verified calculations may be used. No tide, buoyancy, drowning or fluid-force formula is authored by this contract.

Action economy / initiative:
ordinary supported actions are usable. Custom rescue, brace, climb, environmental interaction or interrupt actions require exact contracts.

Full turn / round lifecycle:
required for within-battle tide transitions, waterline movement, scheduled exposure windows, repeating environmental pulses or delayed coastal events.

Full stateful damage pipeline:
required for any environmental damage caused by falls, impacts, crushing water, submersion or other hazards.

Status lifecycle:
required for any persistent mechanical condition. Narrative descriptors must not masquerade as PTU statuses.

Terrain / weather / hazards / zones / reactions:
required for dynamic water terrain, wave/current zones, wet/slippery sectors, changing safe zones, environmental reactions or rescue windows.

Move-specific behavior:
every authored water, terrain, movement, weather, concealment or rescue Move must be verified individually.

Abilities:
every authored aquatic, weather, detection, movement, protection or terrain Ability must be verified individually.

Items:
mechanical ropes, flotation, survey tools, boots, sensors or rescue gear require exact item contracts. Until then they remain narrative props or records.

Trainer Features / perks:
any specialist coastal navigation, Survival, Research, Topography, Climatology, rescue or environmental privilege requires project-authoritative PTU/Caelo verification and implementation evidence.

AI legal-action infrastructure:
may enumerate only already supported actions. It cannot create water-specific legality.

AI tactical policy:
general autonomous reasoning about dynamic water coverage, route windows, rescue, evacuation or changing environmental geometry remains dependency-gated.

Minecraft / Cobblemon / Craftics adapter/playback:
may render authoritative waterline state, route barriers, exposed geometry, observations and semantic events. It cannot decide legal movement, damage, statuses, tide truth, NPC knowledge or encounter outcome.

## PTU / Caelo provenance boundary

The current repository inventory exposes `sources/kairos/KAIROS_SOURCE_INDEX.md`, which routes movement/terrain, hazards, terrain/weather, Fishing and encounter guidance into the supplied Kairos compilation. That index explicitly remains a routing aid and comparative source.

No adopted `sources/caelo` directory was visible during Pass 324 inspection.

Therefore this contract does not define numerical coastal mechanics. Any future use of Swim, water terrain, currents, drowning, underwater targeting, Fishing, rescue, relevant Moves, relevant Abilities, relevant Items or Trainer Features must be checked against the project-authoritative source before implementation.

## World-agent integration

Intertidal state should feed the global planner as explicit world facts and evidence references.

A route closure can trigger replanning only for affected agents.

A new observation can wake only recipients who actually receive it.

A corrected tide-window publication creates a new publication event; it does not rewrite prior receipt history.

A named NPC may plan off-screen using the latest state they know, even when that knowledge is stale relative to hidden authoritative world state.

This mismatch is intentional gameplay evidence, not an AI bug.

## Canon boundary

This contract approves no coast, settlement, route, tide schedule, institution, Pokémon population or historical event. Those require later canon promotion.