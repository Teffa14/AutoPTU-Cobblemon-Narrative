# Floodplain inundation observation contract — Pass 321

Status: PROPOSED DESIGN CONTRACT / NON-CANON
Date: 2026-09-06

This contract keeps floodplain history, current physical state, observations, NPC knowledge, institutional decisions, tactical rules, and Minecraft presentation separate.

## Core invariant

A floodplain is not a binary flooded/not-flooded location.

The runtime and authored content must preserve these layers separately:

1. persistent feature identity;
2. historical hydrologic/event provenance;
3. current authored physical state;
4. observations made by a source at a semantic time;
5. information actually received by each actor;
6. actor interpretation or assessment;
7. institutional decision;
8. feature-scoped operational consequence;
9. PTU tactical state, only when exact rules are supported;
10. Minecraft/Cobblemon presentation.

No downstream layer may silently rewrite an upstream one.

## Required distinctions

Historical floodplain membership does not prove current inundation.

Historical event extent does not prove current feature state.

A high-water mark records evidence of a past peak or extent. It does not set current water level.

Current water presence does not prove hazardous current.

Hazardous current does not exist mechanically unless an authoritative tactical contract defines it.

A dry road surface does not prove structural safety or institutional reopening.

A closed route does not prove that every feature within the floodplain is dangerous.

An NPC does not know a gauge reading, field trace, route state, or interpretation until that information is received through an authorized path.

Minecraft water blocks, particles, sound, animations, or visual depth do not establish PTU rules or hidden world truth.

## Suggested data model

### FloodplainFeature

Minimum fields:
- `feature_id`;
- `feature_kind`;
- `location_ref`;
- `parent_landscape_ref`;
- `created_at` or historical provenance reference;
- optional authored relationships to route edges or observation points.

Feature kinds should remain descriptive: causeway, culvert, side channel, survey rise, refuge strip, route spur, gauge point, maintenance access.

### HydrologicStateRecord

Minimum fields:
- `state_id`;
- `feature_id`;
- `semantic_time`;
- `authored_state`;
- `source_ref`;
- optional predecessor state;
- optional supersession reason.

Reduced-version state vocabulary may include `DRY_OPEN`, `SHALLOW_RESTRICTED`, `INUNDATED_CLOSED`, `BYPASS_OPEN`, `MONITORING`, or more domain-specific equivalents. These are world/operational labels, not PTU statuses.

### FloodObservation

Minimum fields:
- `observation_id`;
- `feature_id`;
- `semantic_time`;
- `observer_ref`;
- `observation_type`;
- `observed_value`;
- `source_ref`;
- optional confidence/qualification;
- optional instrument/reference-point ref.

Observation types may include high-water mark, mud/seed/debris line, scour/wash evidence, fresh silt, culvert blockage, current inundation, gauge record, route surface condition, or habitat use.

### FloodInterpretation

Minimum fields:
- `interpretation_id`;
- `actor_id`;
- `created_at`;
- exact observation/receipt refs used;
- conclusion type;
- confidence/uncertainty if supported by the world-agent contract;
- supersession/review linkage.

An interpretation may be wrong while its input observation remains historically valid.

## Evidence reliability

Do not encode every environmental trace as equally authoritative.

The authoring layer may qualify evidence as direct, corroborated, provisional, disturbed, instrument-derived, or unresolved. Any formal enum should be introduced only after reviewing existing evidence/provenance vocabulary so the project does not create duplicate concepts.

A weaker trace may still be useful for quest progression. It simply cannot overwrite a stronger source automatically.

## Temporal semantics

Every water-state or observation record needs semantic time.

Two reports can be simultaneously valid historical records while contradicting as current-state claims because they were created hours or days apart.

Revisits should append new observations rather than mutate old ones.

If a later observation changes an actor's assessment, use the project's explicit receipt/review lineage. Do not retroactively edit what the actor previously knew.

## Route and consequence integration

Feature physical state, route graph state, and institutional permission should remain independently addressable.

Example:
- the causeway surface becomes dry;
- a route authority receives an inspection;
- a previous closure decision is reviewed;
- the main crossing consequence is ceased;
- a side-channel refuge consequence remains active;
- a monitoring notice remains published until separately updated.

Selective consequence repair should change only the consequence justified by the review.

## Reduced tactical contract

The reduced version intentionally avoids fluid combat simulation.

Use ordinary route edges and ordinary verified movement on accessible nodes.

Represent inundated or unsafe sections as authored unavailable/restricted route edges rather than dynamic current squares.

Perform water-level changes between tactical scenes or through explicit world-state transitions.

Do not infer:
- Swim movement costs;
- wading penalties;
- drowning;
- underwater LoS;
- turbidity modifiers;
- current-driven push/pull;
- debris collision;
- slippery statuses;
- environmental damage;
- rescue reactions;
- Water-type privileges;
- Move, Ability, Item, or Trainer Feature interactions.

The story must remain playable under this contract.

## Full tactical contract gates

A richer version may be authored only after exact engine evidence exists for every activated family.

Targeting / footprints / range / LoS: ordinary geometry is currently verified within audited contracts. Water-surface occlusion, underwater visibility, turbidity, or depth-sensitive LoS remain separate unverified subfamilies.

Base movement legality: ordinary movement is verified within audited contracts. Water traversal must be sourced before use.

Complete movement including push/pull/knockback/interception/forced movement: currently PARTIAL; required for current displacement and rescue/interception.

Core calculations: deterministic arithmetic is verified within audited contracts; no hydrodynamic formula is authorized.

Action economy / initiative: verified within audited primitives; specialized flood actions still require their own contracts.

Full turn / round lifecycle: currently PARTIAL; required for scheduled rises/falls, changing zones, pulses, delayed debris, or phase-bound water transitions.

Full stateful damage pipeline: currently PARTIAL; required for drowning, debris impact, crushing, falling, or other environmental battle damage.

Status lifecycle: currently PARTIAL; required only for real persistent mechanical conditions.

Terrain / weather / hazards / zones / reactions: currently MIXED / PARTIAL / BLOCKING by subfamily; required for active current zones, rain interaction, dynamic water boundaries, rescue reactions, or unstable footing.

Move-specific behavior: currently PARTIAL; each water/weather/terrain/rescue Move must be verified independently.

Abilities: currently PARTIAL; each interaction must be verified independently.

Items: currently PARTIAL; rules-level ropes, flotation, pumps, sensors, held items, or protection need exact support.

Trainer Features / perks: currently PARTIAL; rescue, traversal, weather, terrain, Survival, or intervention Features need exact support.

AI legal-action infrastructure: VERIFIED within audited contracts once authoritative actions and legality exist.

AI tactical policy: BLOCKING for generalized autonomous current navigation, flood rescue, evacuation, dynamic hazard avoidance, or crossing strategy.

Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end for dynamic flood/current playback. The adapter consumes canonical state; it does not create PTU mechanics.

## Source boundary

Current repository source inventory exposes `sources/kairos` and no adopted `sources/caelo` directory was located during Pass 321 inspection.

Kairos is a routing/comparison source, not automatic Ouros authority.

Until project-authoritative PTU/Caelo text is located and checked, the following remain UNVERIFIED: Swim/current rules, drowning, water terrain costs, underwater/turbidity visibility, rainfall interaction, water hazards, rescue interrupts, and all Move/Ability/Item/Trainer Feature interactions used by the encounter.

## Canon boundary

This contract defines separation of concerns for proposed content. It does not establish that Ouros contains the causeway, floodplain, river, institutions, Pokémon populations, flood history, or final explanation described in Pass 321.
