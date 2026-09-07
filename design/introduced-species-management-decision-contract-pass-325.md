# Introduced-species management decision contract — Pass 325

Status: DESIGN CONTRACT / NON-CANON
Date: 2026-09-07

## Purpose

Define a reusable Ouros boundary for ecological-management stories where an intervention has historical provenance, current populations have changed context, multiple institutions hold partial information, and later policy may revise earlier decisions without rewriting history.

This contract governs world state and narrative causality. It does not create PTU mechanics.

## Authoritative state separation

The implementation must keep these layers distinct:

1. population identity and current authored distribution;
2. historical intervention record;
3. current feature-scoped impact evidence;
4. observations and their provenance;
5. information actually received by each NPC;
6. each actor's interpretation or belief;
7. institutional authority and policy objective;
8. decision event and effective scope;
9. feature-scoped consequence;
10. optional AutoPTU handoff;
11. semantic battle result ingress;
12. Minecraft/Cobblemon/Craftics presentation.

A value moving through one layer never silently mutates another.

`HISTORICAL_CLASSIFICATION != CURRENT_IMPACT`

`POPULATION_PRESENT != IMPACT_CAUSED`

`PAST_AUTHORIZATION != CURRENT_BLANKET_AUTHORITY`

`MINECRAFT_PRESENTATION != WORLD_OR_RULES_AUTHORITY`

## Historical intervention record

Each material intervention should preserve a stable record with fields conceptually equivalent to:

- `intervention_id`;
- `authorized_at`;
- `authorizing_actor_or_institution`;
- `original_problem_claim_ids`;
- `target_feature_ids`;
- `target_population_or_condition`;
- `introduced_or_managed_population`, if any;
- `objective`;
- `scope`;
- `review_conditions`;
- `known_constraints`;
- `source_record_ids`;
- `superseded_by`, if later revised.

An old notice or oral summary may reference this record without reproducing its full scope. That shortened message is a separate information event.

## Current impact evidence

Current policy must consume current evidence. Useful observation kinds may include presence, feeding, damage, nesting, route use, displacement, habitat use or absence-with-limited-detection. Every observation needs feature identity, semantic time, observer/source and confidence where appropriate.

Presence alone cannot establish damage causality. Damage alone cannot establish which population caused it. Historical intent alone cannot establish current effectiveness.

## NPC knowledge boundary

The global world-agent system remains non-omniscient.

A management officer who receives a summary knows that summary. A field monitor who records a nest knows that observation. A worker who saw damage knows what they saw. Shared employment or faction membership does not merge those ledgers.

Archive lookup creates external evidence. It does not retroactively become personal memory of the original intervention.

Corrections, revised identifications and amended notices are new events with their own audience and receipt histories.

## Decision model

A management decision should identify:

- decision ID;
- deciding authority;
- objective;
- evidence considered;
- feature/population scope;
- permitted action class;
- effective semantic-time window;
- review condition/date;
- publication/recipient plan;
- consequences created;
- predecessor decision if this is a revision.

A later decision can narrow, suspend, extend, replace or review an earlier one. It must not erase the earlier record or its realized consequences.

## Feature-scoped consequences

Avoid global toggles such as `SPECIES_ALLOWED=false` when the actual decision concerns one storage yard or nursery.

Examples of world-level consequences:

- route restricted during a work window;
- food storage upgraded;
- monitoring duty created;
- habitat edge protected;
- exclusion installed at one feature;
- public notice corrected;
- contract or job created;
- inspection scheduled;
- trust/reputation changed through existing social systems;
- review becomes due after a semantic interval.

These consequences should bind to persistent feature IDs and named institutions where relevant.

## Displacement and secondary effects

A feature-scoped intervention may create later observations somewhere else. Do not model this as automatic omniscient ecological simulation unless a verified subsystem exists.

Reduced implementation can author deterministic consequence events such as:

- `ROUTE_USE_SHIFT_OBSERVED`;
- `NEW_DAMAGE_REPORT_RECEIVED`;
- `MONITORING_RESULT_RECORDED`;
- `INTERVENTION_EFFECT_REVIEW_DUE`.

Each event remains provenance-backed and can wake only affected world agents through existing replanning infrastructure.

## AutoPTU handoff

Structured battle resolution requires an explicit `REQUEST_AUTOPTU` boundary. The world planner supplies only supported authoritative battle inputs.

While AutoPTU owns tactical resolution:

- world-agent AI does not choose tactical actions;
- Minecraft does not invent legal actions;
- ecological labels do not become statuses;
- species flavor does not grant unimplemented movement, sensing or combat behavior.

After battle, only admitted semantic results may update world state.

## Reduced implementation

The reduced form is the default until richer engine support is verified.

It uses:

- static authored tactical geometry if combat occurs;
- ordinary verified targeting/range/LoS;
- ordinary verified base movement legality;
- ordinary verified core calculations;
- ordinary verified action economy/initiative;
- explicit world-level policy and feature state outside combat;
- semantic-time observations and review events;
- existing NPC knowledge, publication, memory, travel and replanning systems;
- authored secondary consequences between encounters.

No special population-control mechanic is required.

## Rich implementation gates

A richer version may include moving refuge boundaries, rescue/interception, territorial displacement, environmental machinery, specialized terrain, noncombatant routing, delayed arrivals, repeated zone effects or species-specific Move/Ability behavior.

Those features require exact evidence in the permanent capability family that owns them. Representative support elsewhere cannot be generalized.

## PTU / Caelo boundary

The visible narrative source registry currently exposes `sources/kairos` and no adopted `sources/caelo` directory. Kairos remains comparative evidence rather than automatic Ouros law.

Before mechanical authoring, verify project-authoritative definitions for any relevant tracking, capture, handling, ecology/research Skills, Trainer Features, movement Capabilities, Moves, Abilities, Items, terrain effects, reactions or environmental damage.

Do not derive PTU values from Pokédex flavor or real ecological sources.

## Minecraft / Cobblemon / Craftics boundary

Presentation may show:

- barriers;
- notices;
- work crews;
- habitat changes;
- Pokémon presence;
- damaged goods;
- monitoring equipment;
- semantic battle events.

Presentation cannot decide:

- whether a population caused an impact;
- whether a policy is legally or institutionally valid;
- what an NPC knows;
- route or battle legality;
- damage;
- status application;
- Move/Ability effects;
- policy consequences not emitted by authoritative world state.

## Acceptance criteria for future implementation

A compliant implementation demonstrates that:

- historical intervention provenance survives policy revision;
- old summaries do not automatically expose the full charter;
- presence observations cannot become causal impact without evidence;
- decisions bind to explicit objectives and feature scope;
- NPCs receive evidence individually;
- reviews create new decisions rather than rewriting history;
- consequences can trigger later monitoring/replanning;
- reduced battles use only verified mechanics;
- rich mechanics remain gated by capability evidence;
- Minecraft remains presentation-only.