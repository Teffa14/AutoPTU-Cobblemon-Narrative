# Marea Migration Stopover Fixture — Pass 235

Status: PROPOSED / NON-CANON
Date: 2026-09-03
Depends on: `design/migration-stopover-temporal-niche-contract.md`

## Purpose

Exercise migration, stopover pressure, delayed observation and reduced/full encounter handoff using existing Marea geography without fixing species before global-world biome and Cobblemon spawn compatibility are verified.

## Existing anchors used

This fixture references existing Marea anchors only:

- Sendero del Vidrio seasonal crossing;
- upper junction;
- Estación Mirador;
- field transect trailhead;
- Puerto Bruma institutional reporting through the Field Office if required.

No coordinate is changed by this proposal.

## Species assignment

```yaml
migratory_species_id: null
source_population_id: null
cohort_id: null
native_spawn_compatibility_verified: false
status: BLOCKED_ON_WORLDGEN_AND_NATIVE_SPAWN_BINDING
```

Candidate species selection must wait for:

1. final generated biome IDs/tags at the route and stopover sites;
2. pinned Cobblemon native spawn definitions;
3. species evidence supporting movement/group behavior;
4. population plausibility under Ouros ecology.

Popularity may prioritize which compatible species receives polish first, but cannot override these gates.

## Narrative premise

A recurrent moving cohort is normally observed near the upper Sendero corridor during a narrow seasonal window. Estación Mirador maintains low-confidence historical counts based on field observations rather than omniscient tracking.

This year the first expected observation window opens, but the cohort does not appear on schedule.

The absence creates the initial quest signal.

## Hidden ecological truth candidates

Only one is selected by world state in a concrete implementation.

Possible causes:

- an upstream stopover has insufficient recoverable resources;
- recent disturbance delayed departure;
- unsuitable weather shifted the departure window;
- the cohort split and a smaller group used an alternate corridor;
- the local route is still valid but the historical timing estimate was overconfident;
- a human-created attractor diverted the cohort toward a poorer stopover.

The player does not receive the selected cause directly.

## Observation loop

### Stage A — Expected arrival

Visible evidence:
- Mirador has prior dated observations;
- local resources expected to show feeding pressure remain unusually intact;
- no reliable current sighting exists.

Possible player actions:
- inspect old counts;
- survey the transect trailhead;
- ask Puerto Bruma or Loma Clara for recent sightings;
- wait through the normal time-of-day window;
- search for directional movement evidence.

### Stage B — Partial evidence

The player can discover one or more:
- tracks or feeding signs that indicate a small advance group;
- reports with inconsistent dates;
- a disturbed stopover/resource patch;
- signs that local presence increased at the wrong time of day;
- evidence of an alternate corridor.

Evidence packets have confidence and provenance. No NPC gains the true route automatically.

### Stage C — Intervention

Possible interventions:
- reduce human traffic for a defined window;
- restore or protect a stopover resource;
- remove a non-essential artificial attractor;
- establish a temporary observation station;
- leave the system alone because intervention evidence is weak.

### Stage D — Delayed verification

Resolution is checked after ecological time passes.

Possible outcomes:
- cohort arrives late but in normal condition;
- cohort arrives late and remains longer to recover;
- only part of the cohort arrives;
- cohort bypasses the site and later reports confirm an alternate route;
- no arrival occurs, escalating the investigation upstream.

A quest cannot mark the ecological hypothesis as confirmed solely because an intervention was performed.

## Stopover resource consequences

If the cohort arrives:

```text
arrival
-> occupancy pressure rises
-> food/water/shelter demand rises
-> local visible density rises
-> resident competition/avoidance can change
-> departure pressure updates as recovery progresses
-> departure
-> temporary resource debt and observation evidence remain
```

This creates consequences before and after the visible encounter window.

## Reduced encounter version

This version is intended to be implementable before rich tactical capability families are complete.

If a structured confrontation occurs:

- Ouros selects explicit combatants from the local projected subset;
- cohort transit is paused/abstracted outside the tactical grid;
- AutoPTU resolves a normal supported battle using static terrain and verified foundations;
- non-combat cohort members do not become tactical actors;
- semantic result returns as disturbance, delay, route confidence or condition pressure;
- migration resumes through Ouros world state.

Required broad verified foundations:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

No claim is made that all move/ability/status/item content used by a concrete species is already supported.

## Full encounter version

A richer version could stage a crossing while the cohort is physically moving through a constrained route.

Potential mechanics:
- protect a moving subset without blocking its exit;
- hostile or panicked actors enter from different approach vectors;
- weather changes route safety;
- hazardous tiles create alternate lanes;
- forced movement can push actors away from or into the migration lane;
- reactions/interception can protect or obstruct crossings;
- autonomous actors prioritize escape, cohesion or protection over KOs.

Exact dependency classification:

- targeting/footprints/range/LoS: VERIFIED foundation;
- base movement legality: VERIFIED foundation;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED foundation;
- action economy/initiative: VERIFIED foundation;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED foundation;
- AI tactical policy: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

## Narrative invariant

The premise survives reduction.

Both versions tell the same story:
- a migration window matters;
- expected arrival is uncertain;
- field evidence can be incomplete;
- stopover quality affects onward movement;
- player action can help, harm or simply reveal the system;
- later observations verify consequences.

The reduced version removes tactical richness, not ecological causality.

## NPC/faction use

Existing institutions can gain differentiated roles without omniscience:

- Estación Mirador: repeated observations, counts, weather/local-route context;
- Puerto Bruma Field Office: report aggregation and coordination;
- local producers/route users: disturbance/resource observations;
- player: connects evidence across sites and decides whether intervention is justified.

No new faction is canonized by this fixture.

## Persistence outputs

A completed run may write:

```yaml
migration_observation_record: []
route_confidence_delta: null
stopover_resource_delta: null
disturbance_delta: null
cohort_condition_delta: null
arrival_time_observed: null
departure_time_observed: null
alternate_route_evidence: []
institutional_knowledge_updates: []
```

## Canon gates

Before promotion:

- bind route/stopover to final world coordinates and biome tags;
- select a compatible species/population;
- verify Cobblemon native spawn envelope;
- verify movement/seasonality evidence and provenance;
- define recurrence window from Ouros calendar/time system;
- test population accounting across origin, transit, stopover and destination;
- confirm no conflict with existing Marea resident-network canon.
