# Global Species Interaction Graph

Status: PROPOSED DESIGN. Not established Ouros canon.
Date: 2026-09-03

## Purpose

Define the minimum world-wide ecology representation needed to answer, for any ecosystem in Ouros:

- who can eat whom;
- who avoids whom;
- who competes for the same resource;
- who displaces whom;
- who fights over territory, nesting space, shelter or feeding sites;
- what changes in local wild availability when these pressures change;
- what credible observers can learn and report.

This design applies to the whole map. Regions such as Marea are instances of the same global system, not special-case ecology engines.

## Core objects

### Species ecology profile

```yaml
species_id: null
source_refs: []
diet_tags: []
habitat_tags: []
size_band: null
movement_modes: []
activity_windows: []
foraging_roles: []
known_food_resources: []
explicit_species_links: []
confidence: null
```

PTU/PTR species data supplies authoritative or project-approved mechanical/species fields where available. Narrative code must not infer exact prey solely from a coarse diet tag.

### Ecosystem instance

```yaml
ecosystem_id: null
region_id: null
biome_tags: []
resource_nodes: []
cover_complexity: null
water_state: null
weather_state: null
season_state: null
human_disturbance: null
species_populations: []
interaction_edges: []
observer_channels: []
```

### Interaction edge

```yaml
interaction_id: null
actor_species_id: null
target_species_id: null
resource_id: null
type: null
status: proposed
provenance_grade: null
source_refs: []
context_requirements: []
intensity: 0.0
confidence: 0.0
last_evaluated_at: null
world_effects: []
```

Supported initial edge types:
- PREDATES_ON
- AVOIDS
- COMPETES_WITH
- DISPLACES
- TERRITORIAL_AGAINST
- SCAVENGES_FROM
- FORAGES_RESOURCE
- FACILITATES
- ASSOCIATES_WITH
- NEUTRAL_OBSERVED

## Interaction construction

The system must never compare every Pokémon against every other Pokémon globally each tick.

Candidate edges are built only where species can materially overlap in one ecosystem instance.

Candidate generation order:

1. explicit species-to-species evidence;
2. ecosystem co-occurrence;
3. diet/resource compatibility;
4. size and mobility plausibility;
5. activity overlap;
6. shelter/nest/territory overlap;
7. recent local population pressure;
8. human disturbance and management state.

An edge can exist with low confidence before it is canon-approved, but low-confidence edges must not create irreversible lore facts.

## Provenance grades

`PROVENANCE_EXPLICIT` means a source names the relationship directly.

`SPECIES_TRAIT_STRONG` means a source establishes a strong ecological role without naming the counterpart.

`PTU_DERIVED` means a candidate follows from approved PTU/PTR species data such as Diet/Habitat plus local context.

`BIOLOGICAL_ANALOGUE` means a real-world analogue proposes a possibility and remains non-canon until reviewed.

`OUROS_INFERRED` means the world engine derives a context-specific relationship from already approved inputs.

`OUROS_AUTHORED` means a human-reviewed original Ouros relationship.

## World-state resolution

Off-screen ecology resolves statistically/algorithmically. It does not instantiate hidden tactical battles.

An edge can affect:
- demographic loss;
- encounter availability;
- spatial distribution;
- time-of-day activity;
- migration pressure;
- refuge use;
- resource depletion;
- nest/territory occupancy;
- local behavior state;
- public/institutional observations.

Predation must support both consumptive and non-consumptive outcomes. A predator can make prey harder to encounter without consuming a member.

Competition must not automatically mean combat. It can reduce resource access, cause temporal partitioning, encourage migration or create localized territorial events.

Territorial pressure must be local. A species being territorial in one nesting site does not make the entire species globally hostile.

## Spawn projection contract

World truth flows in one direction:

```text
ecology ledger
  -> local species availability/activity
  -> Cobblemon spawn eligibility/weight/location/time window
  -> visible overworld encounters
```

Spawn generation never creates population truth by itself.

Suggested projection fields:

```yaml
species_id: null
population_pressure: 1.0
visibility_multiplier: 1.0
spawn_weight_multiplier: 1.0
allowed_microhabitats: []
active_time_windows: []
avoidance_zones: []
concentration_zones: []
reason_refs: []
```

A low visible spawn rate can come from low abundance or from avoidance/refuge behavior. Those causes must remain distinct internally so NPC reports and later recovery behave correctly.

## NPC observation contract

The ecology simulator emits evidence packets, not dialogue.

```yaml
observation_id: null
ecosystem_id: null
subject_species_ids: []
event_type: null
observed_facts: []
confidence: null
observer_requirements: []
created_at: null
expires_at: null
source_world_events: []
```

Useful event types include:
- predator_pressure_rising
- prey_sightings_declining
- territorial_displacement
- feeding_site_conflict
- migration_arrival
- predator_following_migration
- activity_window_shift
- unusual_strength_distribution
- nesting_site_abandoned
- resource_shortage
- population_recovery

Rangers, researchers, explorers, traveling Trainers and residents receive packets through existing knowledge/communication systems according to actual access. NPC generation converts known packets into role-appropriate statements, warnings, tasks or route decisions.

NPCs never read hidden population numbers directly unless an institution has a valid survey mechanism that produced that knowledge.

## Example explicit edge

Official Pokémon material explicitly states that Wurmple is targeted by Swellow as prey.

```yaml
actor_species_id: swellow
target_species_id: wurmple
type: PREDATES_ON
provenance_grade: PROVENANCE_EXPLICIT
context_requirements:
  - co_occurs_in_ecosystem
world_effects:
  - consumptive_pressure
  - prey_avoidance_pressure
```

The exact predation rate remains an Ouros simulation parameter and is not imported from Pokémon prose.

## Example derived edge

Pidgeotto is species-grounded as a territorial predator but its official entry does not name its prey. If an Ouros woodland contains Pidgeotto and several compatible small prey species, the system may create proposed candidate edges from approved Diet/Habitat/size/activity evidence.

Those edges remain `PTU_DERIVED` or `OUROS_INFERRED` until reviewed. The generator must not present the relationship as official Pokémon canon.

## Mechanical dependency boundary

The persistent interaction graph, demographic pressure, spawn projection and NPC knowledge packets are world-state systems. They do not require AutoPTU tactical execution.

When an ecological event becomes a real encounter, dependencies must be declared per encounter.

### Baseline field observation / avoidance encounter

Intended version: player observes prey changing route because a predator is nearby, with no battle required.

Permanent capability dependencies:
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for reliable semantic spawn/activity projection and NPC/world feedback.
- no tactical category is required if no battle occurs.

Reduced version: change spawn eligibility and deliver ranger/explorer observations without bespoke animations.

### Territorial battle at a feeding or nesting site

Intended full version may require:
- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL if the encounter premise uses forced displacement;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when relevant;
- terrain/weather/hazards/zones/reactions: BLOCKING as a complete family when environmental mechanics are required;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING as a complete policy;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for full semantic playback/world writeback.

Reduced version: instantiate a normal legal AutoPTU battle on simple terrain using only verified/basic mechanics. Resolve the ecological consequence after the authoritative battle outcome without custom knockback, reactive terrain, bespoke hazards or AI tactics.

### Predator pursuit through complex habitat

Intended full version may additionally depend on complete movement, terrain/zones/reactions, move-specific behavior and tactical AI policy.

Reduced version: the overworld decides whether the player reaches a simple battle instance or avoids it. Tactical combat begins only after pursuit has ended, preserving the narrative premise without inventing unsupported chase mechanics.

## Current readiness snapshot

Based on `design/engine-readiness-snapshot-pass-224.md`:

VERIFIED within audited contracts:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING as complete families when required:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy.

PARTIAL/BLOCKING:
- Minecraft/Cobblemon/Craftics adapter/playback for semantic ecosystem projection and reliable end-to-end feedback.

## Open questions

- authoritative mapping from PTU/PTR Diet categories to edible resource classes;
- authoritative Habitat normalization across all available species sources;
- age/evolution-stage effects on diet and predator vulnerability;
- species-specific territoriality evidence;
- confidence threshold for converting an inferred edge into persistent simulation truth;
- edge intensity arithmetic and simulation cadence;
- whether habitat complexity is represented categorically or numerically;
- how much recent predator exposure should affect prey behavior before decaying;
- exact spawn-weight API contract with Cobblemon;
- survey/observation mechanics that allow institutions to estimate population state.
