# Ouros Narrative Architecture

Status: Proposed design architecture. Not established world canon.

## Goal

Ouros should behave like a persistent Pokémon tabletop world implemented through a Minecraft overworld and AutoPTU battle engine. The narrative system should remember what players do, transform those actions into durable world state, and generate future opportunities from that state without replacing human-authored major arcs.

## Core design principles

### 1. Local closure, global consequence

Most adventures should resolve a meaningful local problem in one arc. Completion may also emit one or more consequences into the world graph.

A quest can finish while its consequences continue.

Example consequence types:
- NPC relationship changes
- faction reputation changes
- settlement condition changes
- route safety changes
- encounter-table changes
- shop inventory changes
- rumor creation
- future rival behavior
- unlocked or sealed dungeon access
- migration of a Pokémon population
- new job availability
- disappearance or arrival of NPCs

### 2. Quiet phase / pressure phase

The PTU Core Rulebook recommends alternating periods where players freely pursue Gyms and personal interests with periods where a larger plot demands attention.

Ouros should encode this as an arc pacing tool rather than a mandatory global schedule.

Quiet phase content:
- social scenes
- catching and training
- exploration
- contests
- professions
- research
- optional jobs
- local mysteries
- rival interactions

Pressure phase content:
- faction operations
- regional crises
- raids
- dungeon escalation
- boss encounters
- settlement threats
- time-sensitive decisions

Players should still retain optional content during pressure phases where plausible.

### 3. Activity containers

Caelo demonstrates a useful living-world taxonomy. Ouros can adapt the same conceptual categories while implementing them as game content rather than Discord thread slots.

Proposed Ouros activity types:
- SOCIAL
- WILD_ENCOUNTER
- TRAINER_BATTLE
- JOB
- RAID
- CONTEST
- GYM
- DOJO
- EXPEDITION
- DUNGEON
- INVESTIGATION
- WORLD_EVENT

An arc may contain several activity types.

### 4. World-state first

The generator must not ask only, "What quest should happen next?"

It should ask:
- What is true in this location now?
- Who is present?
- Which factions care about it?
- What did players previously change?
- What Pokémon live here and why?
- What environmental state exists?
- Which unresolved promises, debts, discoveries or threats connect here?

Only then should it select or instantiate a quest structure.

### 5. Narrative graph

Represent narrative content as connected data.

Minimum proposed node types:
- CHARACTER
- NPC
- POKEMON_ENTITY
- FACTION
- LOCATION
- SETTLEMENT
- DUNGEON
- EVENT
- QUEST
- ARC
- RUMOR
- CLUE
- ITEM_OF_INTEREST
- RELATIONSHIP
- WORLD_STATE

Minimum proposed edge types:
- located_at
- knows
- trusts
- opposes
- owes
- witnessed
- caused
- discovered
- controls
- threatens
- protects
- requires
- unlocks
- changes
- foreshadows
- resolves

### 6. Player Chronicle

Every meaningful player-caused event should be eligible for the Chronicle.

Chronicle entries should record structured facts, not generated legend prose only.

Suggested record:

```yaml
id: chronicle_event_id
actor_ids: []
location_id: null
timestamp: null
event_type: null
facts: []
world_state_changes: []
witness_ids: []
faction_impacts: []
source_refs: []
narrative_weight: 0
callback_eligible: true
```

The Chronicle enables later callbacks without requiring the system to reread entire chat logs or adventure transcripts.

### 7. Reputation is multidimensional

A single good/evil meter is too shallow.

Each faction or important NPC may track dimensions such as:
- trust
- fear
- respect
- debt
- suspicion

Not every relationship needs every dimension.

Reputation should alter access, information, assistance, prices, dialogue options, opposition and future job availability. It should not automatically determine player morality.

### 8. Locations are game systems

Important locations need more than descriptions.

Caelo's Toxic Ravine is a useful design precedent: its environmental identity has direct mechanical implications. Ouros locations should therefore have an environmental profile that the battle engine can eventually consume.

Proposed location data:

```yaml
location_id: null
biomes: []
connected_locations: []
access_requirements: []
encounter_ecology: []
environment_tags: []
battlefield_tags: []
world_state_variants: []
secrets: []
factions_present: []
quest_hooks: []
```

Mechanical effects remain unimplemented until checked against governing PTU/Caelo rules and AutoPTU engine support.

### 9. Ecological causality

Pokémon encounters should not be random lists detached from the world.

Possible causes for encounter changes:
- season
- time of day
- weather
- pollution
- construction
- faction activity
- migration
- predator removal
- dungeon disturbance
- food availability
- player interventions

This turns encounter tables into storytelling devices.

### 10. Emergent callback budget

A percentage of newly authored content should deliberately reuse old Chronicle material.

Examples:
- an NPC rescued months ago becomes a service provider
- a defeated rival changes tactics
- an abandoned location is occupied by another group
- a Pokémon population reacts to a previous ecological decision
- a joke, rumor or incidental object becomes a minor optional callback

Callbacks must be transformed by elapsed time or changed context. Mere repetition is not enough.

## Quest data model proposal

```yaml
quest_id: null
title: null
status: proposed
activity_types: []
location_ids: []
actor_ids: []
faction_ids: []
preconditions: []
inciting_state: []
objectives: []
optional_objectives: []
encounter_slots: []
choice_nodes: []
fail_forward_states: []
completion_states: []
world_state_changes: []
chronicle_hooks: []
future_edges: []
mechanics_review_required: true
source_inspiration_refs: []
```

## Rules boundary

Narrative generation may propose encounter roles and environmental ideas, but it must not fabricate legal combat execution.

Before implementation, AutoPTU/PTU validation must resolve:
- Pokémon species and level
- legal Moves
- legal Abilities
- capabilities
- initiative
- movement
- terrain interaction
- status effects
- damage
- capture mechanics
- rewards and experience
- any Caelo-specific modifications

Narrative documents should state desired encounter experience in system-neutral terms until mechanics are reviewed.

## Minecraft/Cobblemon translation

The narrative architecture should expose state that can drive a Minecraft overworld.

Examples:
- NPC spawn or despawn
- changed dialogue
- building state or repair
- blocked/open passages
- signs, notices and rumors
- faction guards
- altered wild Pokémon populations
- dungeon entrance state
- environmental visual state
- shop availability
- world-event markers

AutoPTU remains responsible for grid-battle resolution when combat moves into the tactical layer.

## Human-authored canon boundary

Automated research and generation may populate `research/` and `proposals/`.

Only reviewed material should enter a future `canon/` tree.

Promotion checklist:
1. Originality and provenance reviewed.
2. Fits Ouros world tone and established continuity.
3. PTU/Caelo mechanics validated where applicable.
4. AutoPTU can represent required battle interactions, or implementation gap is recorded.
5. Minecraft/Cobblemon world-state requirements are feasible.
6. No external plot, prose or distinctive character has been transplanted.
