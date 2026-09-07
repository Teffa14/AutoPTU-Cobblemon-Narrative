# Volcanic Ash Remobilization Observation Contract — Pass 329

Status: DESIGN CONTRACT / NON-CANON WORLD FACTS
Date: 2026-09-07

## Purpose

This contract supports persistent world stories in which material deposited by an older event is later transported, removed, stored, redeposited, or observed again. It preserves enough provenance for NPC knowledge, institutional decisions, revisits, and tactical handoff without requiring the Minecraft adapter or AutoPTU to simulate unsupported volcanic processes.

The first application is volcanic ash remobilization. The model is intentionally reusable for other persistent particulate or loose-material systems after separate canon review.

## Authority chain

Authoritative state should be resolved through this sequence:

`historical source event -> material parcel/provenance -> persistent source feature -> transfer event -> receiving feature state -> observation -> explicit receipt -> interpretation -> institutional decision -> feature-scoped consequence -> optional AutoPTU handoff -> Minecraft/Cobblemon/Craftics presentation`

Each arrow is an explicit relation. Skipping relations creates omniscience or silently turns presentation into mechanics.

## Core invariants

`EVENT_ENDED != SECONDARY_EFFECTS_ENDED`

The primary ashfall can be over while old deposits remain available for later transport.

`ASH_REMOVED_FROM_FEATURE != ASH_REMOVED_FROM_SYSTEM`

Cleanup can move material into a disposal site, roadside storage, drainage edge, bagged storage, or another authored feature. The destination becomes part of provenance.

`FRESH_DEPOSIT != NEW_ERUPTION`

Deposit age and source-event age are separate properties. A recent transfer event can move old material.

`ROAD_OPEN != CATCHMENT_STABLE`

An access decision applies to the feature and evidence scope encoded in that decision.

`OBSERVATION != CAUSAL_EXPLANATION`

Seeing a deposit, dust cloud, blockage, or cleared road creates an observation. Cause remains an interpretation until supported by evidence.

`PUBLIC_NOTICE != UNIVERSAL_NPC_KNOWLEDGE`

Published information only becomes personal knowledge through the project's existing delivery/receipt rules.

## Minimal data model

A persistent material record should be able to preserve:

- `material_lineage_id`
- known or proposed historical source event
- source confidence
- last known storage/source feature
- transfer-event history
- receiving features
- cleanup/disposal history
- observation IDs
- evidence links
- unresolved hypotheses

A transfer event should preserve:

- `transfer_event_id`
- semantic time/window
- `from_feature_id` when known
- `to_feature_id` when known
- authored transfer class such as wind, runoff, traffic, cleanup, disposal, unknown, or mixed
- evidence supporting that class
- confidence and uncertainty
- world consequences created by the transfer

These are narrative/world-system fields. They do not define PTU tactical rules.

## Feature state

Persistent features can independently carry authored operational states. Example route values:

- `OPEN`
- `RESTRICTED`
- `MAINTENANCE_ONLY`
- `CLOSED`
- `MONITORING`

Material observations can use evidence labels such as:

- `DEPOSIT_OBSERVED`
- `AIRBORNE_PARTICULATE_OBSERVED`
- `CULVERT_BLOCKAGE_OBSERVED`
- `DRAINAGE_CLEAR_OBSERVED`
- `CLEANUP_BOUNDARY_OBSERVED`
- `DISPOSAL_FEATURE_OBSERVED`
- `MATERIAL_SOURCE_UNRESOLVED`
- `OBSERVATION_STALE_AFTER_TRANSFER_EVENT`

These labels must never masquerade as PTU statuses or imply unverified mechanics.

## Observation and provenance

Every meaningful observation should preserve observer, time, feature, method, scope, confidence, and source evidence when available.

A report such as “fresh ash on the road” should resolve to a bounded observation such as:

`observer A saw deposit D on ROAD_SEGMENT_CUT during window T`

It should not silently create:

- a new eruptive event;
- an ash status on all actors;
- a weather condition;
- a global road closure;
- knowledge for all members of the observer's faction;
- causal attribution to a Pokémon, institution, or geological process.

## NPC knowledge and institutions

Use the existing world-agent communication architecture. NPC knowledge changes when an actor directly observes an event, receives a report, reads an archive, participates in a meeting, or receives another explicitly modeled communication.

An observatory can know monitoring results. Public works can know cleanup disposition. A utility can know obstruction and maintenance history. Residents can know local observations. A road authority can know decisions and delivered reports. Those knowledge sets may overlap without becoming identical.

Institutional decisions must record their evidence set and scope. A later revision creates lineage:

`decision_A -> new evidence -> review -> decision_B`

The review does not erase decision_A or retroactively make its supporting observations false.

## Cleanup and disposal lineage

Cleanup is a world event with at least one source feature and one authored disposition. When a crew removes ash from a road, the system should preserve where the material went when that information matters.

Examples:

`ROAD_SEGMENT_CUT -> CLEANUP_EVENT_14 -> ASH_DISPOSAL_FEATURE`

`CULVERT_INLET -> CLEANUP_EVENT_22 -> BAGGED_STORAGE_FEATURE`

Later remobilization can then reference the stored material rather than fabricating a new source.

If disposal is unknown, keep it unknown. Do not infer destination from later evidence without a supported link.

## Semantic time and revisits

The world layer can apply authored transfer events between playable scenes. A later visit should query current feature state and the event history relevant to that feature.

This supports a reduced implementation in which:

- a rainfall window occurs off-screen;
- an authored transfer event moves material from an upstream feature to a culvert;
- the culvert changes operational state;
- an NPC observes the blockage;
- a report is delivered later;
- a road authority reviews only after receiving the report.

No combat-round simulation is required for that sequence.

## Reduced tactical contract

When a battle occurs before the rich environmental families are verified, hand AutoPTU a static legal battlefield that uses only currently verified ordinary contracts.

Allowed reduced assumptions:

- ordinary audited targeting/footprints/range/LoS;
- ordinary audited base movement legality;
- ordinary core calculations;
- ordinary action economy/initiative;
- current AI legal-action infrastructure;
- static blocked or legal spaces authored before combat.

Do not derive tactical penalties from visual ash. Do not create dynamic wind, ash clouds, flows, slipping, damage, exposure conditions, rescue reactions, or forced movement in the adapter.

## Full tactical dependency matrix

Targeting/footprints/range/LoS: ordinary baseline VERIFIED within audited contracts. Dynamic particulate obscurement, visibility reduction, or evolving LoS requires explicit additional evidence.

Base movement legality: ordinary baseline VERIFIED. Ash-specific traction, deep-deposit traversal, unstable surfaces, or special terrain costs require separate verified contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required for gust displacement, moving debris, wet-ash flow displacement, slide effects, rescue, or interception.

Core calculations: ordinary baseline VERIFIED.

Action economy/initiative: ordinary baseline VERIFIED.

Full turn/round lifecycle: PARTIAL. Required for timed gusts, evolving zones, delayed collapse, recurring machinery, environmental phases, or weather transitions during combat.

Full stateful damage pipeline: PARTIAL. Required for authoritative environmental damage such as falling debris, impact, collapse, heat, or other damaging exposure.

Status lifecycle: PARTIAL. Required for any persistent tactical exposure/condition.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by subfamily. Required for authoritative ash fields, wind, wet-debris zones, unstable ground, shelter, reactive hazard boundaries, or environment reactions.

Move-specific behavior: PARTIAL; every relevant move must be verified individually.

Abilities: PARTIAL; every relevant ability must be verified individually.

Items: PARTIAL; every relevant item must be verified individually.

Trainer Features/perks: PARTIAL; dispatcher/traversal evidence does not establish every Feature's prerequisites, resources, frequency, context, or effect.

AI legal-action infrastructure: ordinary baseline VERIFIED.

AI tactical policy: BLOCKING for general evacuation, escort, shelter-seeking, rescue, dynamic environmental objective selection, and similar rich policy.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end for authoritative dynamic environmental playback.

No category can be promoted because one representative subcase exists.

## Adapter boundary

Minecraft/Cobblemon/Craftics receives authoritative presentation state. It may display deposits, cleanup crews, barriers, particles, drainage blockage, stockpiles, weather visuals, and post-event changes.

It must not infer or author:

- ash source event;
- material lineage;
- road legality;
- PTU LoS modifiers;
- movement costs;
- forced movement;
- damage;
- statuses;
- weather rules;
- reaction windows;
- NPC knowledge;
- institutional decisions.

Playback should use semantic events where available and remain visibly subordinate to the authoritative world/tactical state.

## PTU / Caelo source boundary

The current narrative repository inventory exposes the adopted Kairos comparative material but no adopted `sources/caelo` rules source. This contract therefore supplies architecture only. It does not set ash, wind, weather, terrain, hazard, movement, status, damage, perception, skill-check, Move, Ability, Item, or Trainer Feature mechanics.

Those rules require authoritative PTU/Caelo evidence plus engine-contract verification before activation.

## Acceptance checks for future implementations

A future implementation should be rejected if any of these occur:

- cleaning a road globally deletes ash provenance;
- a new deposit automatically creates a new eruption;
- one faction member's observation becomes faction-wide knowledge without delivery;
- a Minecraft particle field changes battle LoS without an authoritative tactical event;
- a cleanup record retroactively changes an earlier observation;
- a road reopening automatically opens every connected drainage or catchment feature;
- a single implemented hazard or Trainer Feature is treated as proof of family-wide support.
