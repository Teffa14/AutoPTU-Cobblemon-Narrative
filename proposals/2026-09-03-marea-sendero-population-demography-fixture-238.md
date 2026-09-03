# Marea / Sendero population demography fixture — Pass 238

Status: PROPOSED / NON-CANON SCENARIO
Date: 2026-09-03

## Purpose

Turn the Pass 238 demographic contract into a playable-world premise without inventing a final abundance, breeding rate or new Marea species.

The scenario uses the already canon-authorized Sendero del Vidrio Fletchling population only as an identity anchor. All counts and demographic events below are deterministic fixture values for validation, not lore claims.

## Premise

After a period of habitat disturbance and partial recovery, local observers report that Fletchling are “back.” The visible evidence is ambiguous: several birds can be seen again around the lower shelf, but the ecological system must determine whether this reflects local recruitment, immigration from another connected patch, increased activity/exposure, or only projection noise.

The player-facing question is therefore not “how many spawned?” but “what demographic process actually happened?”

## Narrative loop

A field-research quest can expose four evidence classes across multiple visits:

1. old nest sites and juvenile dependency evidence;
2. individually recognizable resident birds where persistence is known;
3. movement evidence between connected shelves/corridors;
4. visibility records that can rise or fall without abundance changing.

A local ranger/researcher can initially hold multiple hypotheses:

```text
H1_LOCAL_RECRUITMENT
H2_IMMIGRATION_FROM_CONNECTED_PATCH
H3_RETURN_FROM_TEMPORARY_DISPERSAL
H4_ACTIVITY_EXPOSURE_INCREASE_ONLY
```

The quest should not reveal the hidden canonical event ledger directly. Pass 240 later owns the observation/knowledge pipeline.

## Reduced implementation version

The reduced version needs no special battle mechanics.

Ouros advances deterministic demographic events from the implementation fixture. Minecraft/Cobblemon changes visible eligibility and presentation leases. The player can inspect signs, compare sightings and revisit the site. No combat is required.

If a conventional wild encounter occurs, the system leases one canonical population member before handoff. A KO without capture/removal semantics returns that member to the population after battle.

## Rich version

A later version can involve protecting a recolonization corridor while a small dispersal group crosses between patches, or preventing repeated capture pressure from pushing a recovering population below a local threshold.

That version can involve:
- explicit timed movement across a corridor;
- interception by hostile actors;
- escort/protection objectives;
- terrain and route hazards;
- AI that prefers retreat, escort or corridor traversal rather than KO seeking;
- visible Minecraft playback synchronized to authoritative outcomes.

## Dependency classification

Reduced version:
- targeting/footprints/range/LoS: not required unless combat starts;
- base movement legality: not required for demographic arithmetic;
- complete movement: not required;
- core calculations: not required;
- action economy/initiative: not required;
- full turn/round lifecycle: not required;
- full stateful damage pipeline: not required;
- status lifecycle: not required;
- terrain/weather/hazards/zones/reactions: not required;
- move-specific behavior: not required;
- abilities: not required;
- items: not required;
- Trainer Features/perks: not required;
- AI legal-action infrastructure: not required;
- AI tactical policy: not required;
- Minecraft/Cobblemon/Craftics adapter/playback: required only for visible projection, currently PARTIAL/BLOCKING end-to-end.

Rich corridor version:
- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

AutoPTU-Java commit `2ca8552c640c582c98e7a2cc4667a29426b8173a` improves forced-movement landing consequence wiring. It does not prove complete movement, interception, escort AI or full corridor objective lifecycle.

## Consequence design

Possible semantic world consequences later include:

```text
LOCAL_RECRUITMENT_CONFIRMED
IMMIGRATION_CORRIDOR_CONFIRMED
POPULATION_STABLE_BUT_MORE_VISIBLE
CAPTURE_PRESSURE_REDUCED
CORRIDOR_BLOCKED
RECOLONIZATION_DELAYED
RECOLONIZATION_ESTABLISHED
```

These are world-state outcomes, not PTU Status Afflictions.

## Important non-canon boundaries

This proposal does not establish:
- a canon population count of 12;
- an actual second Fletchling population above Sendero;
- a canon extirpation or recolonization event;
- a breeding season or recruitment rate;
- any new species for Marea.

Those details remain proposed/test-only until separately approved.

## Implementation target

The concrete data contract is `implementation/marea-sendero-population-demography-fixture-v1.json`.

An implementation consuming that fixture should be able to prove that identical visible counts can arise from different hidden demographic histories, and that the demographic ledger remains authoritative across chunk/server lifecycle.