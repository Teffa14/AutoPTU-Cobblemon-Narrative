# Hydrothermal Feature Observation Contract — Pass 328

Status: DESIGN CONTRACT / NON-CANON
Date: 2026-09-07

## Purpose

Define a reusable boundary for hydrothermal locations whose visible output can change over time while their subsurface cause remains unresolved. The contract protects world-state provenance, NPC knowledge boundaries, PTU authority, and Minecraft presentation boundaries.

## Core invariants

`FEATURE_IDENTITY != CURRENT_OUTPUT`

A spring, vent, terrace, runoff channel, or monitoring point keeps its identity when flow, heat, steam, or visible activity changes.

`OBSERVED_OUTPUT != SUBSURFACE_CAUSE`

An observation can establish that a surface feature changed. It does not by itself establish why.

`VENT_ACTIVE != SPRING_CONNECTED`

Two features changing close together in time is evidence for investigation, not automatic proof of a direct underground connection.

`HISTORICAL_USE != CURRENT_ACCESS_DECISION`

Long-standing public, economic, research, habitat, or cultural use does not automatically settle current access or safety decisions.

`MINECRAFT_PRESENTATION != WORLD_AUTHORITY`

Steam particles, water blocks, mineral textures, sounds, barriers, or animation do not decide hydrothermal truth, PTU legality, damage, statuses, or NPC knowledge.

## Authoritative data separation

The narrative system should preserve these layers independently:

1. `feature_id` and stable spatial relationships.
2. Historical feature-state records with provenance.
3. Current authored physical/surface state.
4. Individual observations with source, feature, semantic time, and confidence/limitations where supported.
5. Delivery/receipt records for actors and institutions.
6. Actor interpretation or belief.
7. Institutional decision with authority, scope, evidence set, and review condition.
8. Consequence applied to specific features or actors.
9. Optional AutoPTU encounter state created only through an explicit battle handoff.
10. Minecraft/Cobblemon/Craftics presentation created from authoritative results.

Do not allow hidden subsurface state to leak directly into NPC beliefs.

## Observation examples

World observations may include authored facts such as:

- `VISIBLE_FLOW_REDUCED`
- `STEAM_OUTPUT_OBSERVED`
- `OLD_MINERAL_DEPOSIT_OBSERVED`
- `NEW_DEPOSIT_OBSERVED`
- `RUNOFF_PATH_CHANGED_OBSERVED`
- `MAINTENANCE_WORK_CONFIRMED`
- `MONITOR_READING_RECEIVED`
- `FEATURE_DORMANT_OBSERVED`
- `FEATURE_ACTIVITY_CHANGED_SINCE_VISIT`

These labels are evidence descriptors. They are not Pokémon conditions, terrain tags, damage rules, or automatic causal diagnoses.

## Knowledge contract

An actor knows an observation only when the existing communication/receipt architecture gives that actor the information.

Institution membership does not grant shared omniscience.

Reading an archive record creates receipt of that record. It does not create direct memory of the historical event.

A monitoring summary can omit qualifiers that exist in the underlying record. Preserve both artifacts rather than collapsing them.

A corrected notice becomes a new communication event. It does not retroactively update every recipient of the old notice.

## Decision contract

A feature-scoped decision should record:

- decision ID;
- responsible authority;
- affected feature IDs;
- evidence IDs consulted;
- stated interpretation;
- semantic time;
- consequence IDs;
- review trigger or review date where appropriate.

Possible consequences include `OPEN`, `RESTRICTED`, `STAFF_ONLY`, `CLOSED`, `MONITORING`, or project-specific equivalents already supported by the world layer. These do not create PTU terrain mechanics by themselves.

## Reduced implementation profile

The reduced version is the default until richer capabilities are verified.

Hydrothermal changes occur between scenes through authoritative world events. Tactical encounters use static legal geometry. A sector that would require unsupported environmental mechanics can be blocked or excluded before battle begins.

The narrative premise remains intact because investigation concerns evidence, provenance, access, responsibility, and changing feature state rather than real-time fluid simulation.

Required engine families for the reduced battle, if one occurs:

- targeting/footprints/range/LoS: VERIFIED for ordinary audited use only;
- base movement legality: VERIFIED for ordinary audited use only;
- core calculations: VERIFIED for ordinary audited use only;
- action economy/initiative: VERIFIED for ordinary audited use only;
- AI legal-action infrastructure: VERIFIED for ordinary audited use only.

No hydrothermal-specific behavior is inferred from those verified seams.

## Intended full implementation dependencies

### targeting/footprints/range/LoS

Ordinary LoS is verified within audited contracts. Steam, vapor, glare, spray, or changing obscurement require a separate verified behavior and remain dependency-bearing.

### base movement legality

Ordinary movement legality is verified. Special footing on mineral crust, slick surfaces, unstable edges, or thermal ground cannot be inferred from it.

### complete movement including push/pull/knockback/interception/forced movement

PARTIAL. Required for vent blasts that move actors, rescue/interception, forced slides, falls represented as movement, or displacement caused by changing terrain.

### core calculations

VERIFIED for ordinary audited calculations. Environmental thermal damage does not become valid merely because ordinary arithmetic is available.

### action economy/initiative

VERIFIED for ordinary audited turn actions. Environmental interrupts or reaction windows require the relevant lifecycle/hazard contracts.

### full turn/round lifecycle

PARTIAL. Required for timed geyser pulses, delayed pressure events, start/end phase changes, scheduled vent activity, or other real-time environmental sequencing.

### full stateful damage pipeline

PARTIAL. Required for scalding, heat, crushing, fall, or other environment-originated damage that must participate in authoritative PTU damage state.

### status lifecycle

PARTIAL. Required for Burn or any persistent exposure/condition. Do not create a custom thermal status in the narrative layer.

### terrain/weather/hazards/zones/reactions

MIXED/PARTIAL/BLOCKING by subfamily. Required for hot zones, steam fields, unstable surfaces, changing boundaries, hazard reactions, or weather-linked thermal behavior.

### move-specific behavior

PARTIAL. Any Move that affects heat, water, ground, steam, weather, terrain, digging, cooling, or feature state must be checked individually.

### abilities

PARTIAL. Species flavor or an Ability name cannot establish environmental authority. Verify each Ability contract.

### items

PARTIAL. Sensors, protective gear, healing items, or environmental tools need authoritative item behavior before mechanical use.

### Trainer Features/perks

PARTIAL. Dispatch seams and traversal parity do not prove concrete Feature effects. Verify each Feature before using it for surveying, survival, environment control, interrupts, or protection.

### AI legal-action infrastructure

VERIFIED for the audited ordinary legal-action boundary. Dynamic hazard-aware legality must be proven separately.

### AI tactical policy

BLOCKING for general autonomous reasoning about rescue, feature manipulation, retreat through changing hazards, civilians, or multi-objective environmental encounters.

### Minecraft/Cobblemon/Craftics adapter/playback support

PARTIAL/BLOCKING end-to-end. The adapter may present authoritative feature states and battle results. It must not synthesize missing PTU rules from blocks, particles, fluids, entities, or animations.

## PTU / Caelo boundary

No adopted Caelo source surfaced in the project source inventory inspected for this pass. Kairos remains comparative routing/evidence where already documented, not Ouros mechanical authority.

Until authoritative mechanics and engine tests exist, do not assign numerical temperature checks, Burn/scald rules, hot-spring healing, gas exposure, steam LoS penalties, special movement costs, environmental initiative, Move effects, Ability effects, Item bonuses, or Trainer Feature benefits.

## Canon boundary

This contract authorizes a data model and implementation boundary only. It does not approve a geothermal region, location, faction, species, history, geology, or cause.