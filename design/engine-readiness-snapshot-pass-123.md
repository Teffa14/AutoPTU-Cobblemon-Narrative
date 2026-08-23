# Engine Readiness Snapshot — Pass 123

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU were inspected read-only.

## Live heads inspected

AutoPTU-Java `main`: `45feae6161c9b92ccb008a60d9b6e16dcbc0c377`

Newest Java slice ports the spatial Ability-based status-prevention family for Aroma Veil, Aroma Veil [Errata], Pastel Veil and Sweet Veil. The implementation uses canonical battle state, battle geometry, Ability suppression, ordered status-application hooks and semantic `status_block` events.

This is concrete progress for status application, Abilities and geometry-aware battle hooks. It does not complete the status controller, all status-prevention rules, all Abilities or any overworld propagation/communications system.

AutoPTU `main`: `cd2d31ab9438713629ad3fc65939e8cc622b5a1f`

Newest Python change verifies the deployable Career browser artifact and source provenance. It is Career/deployment CI work and does not promote a tactical capability family.

## Java README evidence

The live Java README still lists these major areas as incomplete:
- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Permanent capability categories

VERIFIED:
- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:
- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:
- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 123.

## Why wireless propagation remains outside the battle core

Nothing inspected establishes an authoritative overworld system for:
- wireless service topology;
- transmitter/repeater coverage;
- radio propagation around terrain/buildings/vegetation;
- dead-zone history;
- channel congestion;
- service interoperability;
- radio interference diagnosis;
- portable repeater deployment;
- communication coverage maps;
- field-service restoration verification.

These belong to world/server persistence. AutoPTU receives a battle snapshot after communications state has influenced narrative knowledge, dispatch, coordination and encounter setup.

## Important geometry boundary

Java now has two kinds of evidence that could be incorrectly overgeneralized:

1. targeting/footprints/range/LoS are VERIFIED for battle geometry;
2. the newest spatial status-prevention Ability family uses battle positions and footprint distance for specific Ability radii.

Neither proves radio propagation.

Battle LoS is not signal coverage.

A three-meter Ability radius is not a repeater model.

Footprint distance is not an RF path-loss model.

Minecraft visual distance is not network availability.

## Pass 123 encounter dependency map

### Relay Ridge Access — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if technicians/equipment move inside the tactical objective
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if a verified ridge hazard or environmental rule is active
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for PROTECT/CLEAR_ROUTE/REACH_OBJECTIVE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: technicians and relay equipment remain outside tactical authority. The site is isolated into a safe maintenance state before combat. AutoPTU receives a static access platform. Coverage/service restoration is tested afterward in world state.

### Festival Channel Saturation — FULL

- targeting/footprints/range/LoS: VERIFIED for combatants
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING when crowds/responders move through the grid
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: only required when a separately validated environmental mechanic is active; otherwise communications congestion is not a tactical zone
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for EVACUATE/WITHDRAW/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: crowd routing and communications load are resolved in overworld state first. Any confrontation uses a cleared static area. Communications degradation changes information delivery, not combat statistics.

### Emergency Interoperability Bridge — FULL

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for equipment carriers and moving deployment objectives
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if a real validated environmental hazard enters the battle
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL if portable communications equipment is ever represented mechanically as an item; world-state equipment should remain outside this family
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for PROTECT/REACH_OBJECTIVE/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version: the gateway/repeater is deployed before battle and frozen outside tactical authority. The battle protects a static location. Afterward the wireless layer tests compatibility and coverage. Battle victory cannot set interoperability to successful automatically.

## New overworld blockers introduced by Pass 123

- `WIRELESS_SERVICE_REGISTRY`
- `RADIO_SITE_TOPOLOGY`
- `RELAY_LINK_STATE`
- `PROPAGATION_PROFILE_REVISIONS`
- `COVERAGE_OBSERVATION_LEDGER`
- `COVERAGE_ASSESSMENTS`
- `DEAD_ZONE_HISTORY`
- `WIRELESS_INTERFERENCE_INCIDENT_GRAPH`
- `INTERFERENCE_HYPOTHESIS_GRAPH`
- `INTEROPERABILITY_PROFILE_STATE`
- `CHANNEL_LOAD_EPISODES`
- `FIELD_REPEATER_DEPLOYMENTS`
- `FALLBACK_COMMUNICATION_PLANS`
- `COVERAGE_TO_COMMUNICATION_CHANNEL_HANDOFF`
- `TECHNOLOGY_TO_WIRELESS_SERVICE_HANDOFF`
- `GEOMAGNETISM_TO_INTERFERENCE_HANDOFF`
- `METEOROLOGY_TO_PROPAGATION_CONTEXT_HANDOFF`
- `RADIO_TO_EMERGENCY_SERVICES_HANDOFF`
- `RADIO_TO_MINECRAFT_PRESENTATION`

## Hard non-inferences for Pass 123

Do not infer:
- tower online -> full coverage;
- repeater powered -> correct configuration;
- device indicates signal -> message delivered;
- one successful contact -> reliable service;
- no signal -> sabotage;
- dead zone -> jamming;
- interference -> Electric-type Pokémon causation;
- Rotom in a device -> network administrator privileges;
- Magnemite/Probopass nearby -> confirmed interference source;
- Electric Terrain -> radio interference;
- Electric Move -> equipment damage;
- Java battle LoS -> radio line of sight;
- Java footprint distance -> propagation radius;
- spatial Ability hook -> overworld aura/network system;
- Minecraft client signal icon -> authoritative coverage state;
- battle victory -> communications restored;
- communications failure -> tactical Accuracy/initiative/Command penalty.

## PTU/Caelo validation state

The accessible project/File Library search did not recover the complete primary Caelo Player’s Guide/rulebook/errata corpus needed to establish exact Technology Education, communications-equipment, electronic-interference or device-damage mechanics. Super PTU Online Helper was not exposed as an invocable capability.

The Python oracle has concrete Electric Terrain behavior in battle, including grounded sleep-prevention logic. That is a tactical field rule only. Pass 123 does not generalize it into wireless interference.

No PTU/Caelo radio range, jamming DC, communications Skill check, electronic hazard, signal bonus or device-damage rule is claimed.

## Current engine conclusion

Java's status path is stronger than at Pass 122 because a spatial Ability-prevention family now resolves through canonical battle geometry and Ability suppression. Status lifecycle and Abilities remain PARTIAL because four closely related Ability contracts do not represent family-complete coverage.

Radio/wireless stories are safe to advance primarily through world state. Communications can determine what actors know, which responders can coordinate and whether an expedition has contact, while combat remains an independent static snapshot until complete movement, tactical AI and Minecraft playback can represent richer objectives without duplicating PTU rules.