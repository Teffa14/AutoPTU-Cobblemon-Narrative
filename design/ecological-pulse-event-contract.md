# Ecological Pulse Event Contract

Status: PROPOSED DESIGN
Date: 2026-09-03

## Purpose

Define how Ouros represents temporary ecological events that alter visible wildlife activity without corrupting persistent population truth or silently invoking tactical battle rules.

Examples include weather-linked concentration, breeding aggregation, resource flush/collapse, disturbance displacement, migration bottlenecks, predator-pressure shifts and temporary rescue corridors.

This contract consumes `research/2026-09-03-ecological-pulse-outbreak-event-window-scan-231.md` and remains subordinate to `design/ecology-development-program.md` and `design/ouros-source-authority-and-species-policy.md`.

## Core invariant

A visible surge is not automatically a population increase.

Ouros must keep these fields separate:

```text
population truth
activity state
exposure state
projection state
observation state
```

No Minecraft/Cobblemon entity count may write population truth directly.

## Event model

```yaml
id: null
type: ecological_pulse
status: proposed
provenance_refs: []
source_process_ref: null
trigger:
  kind: null
  condition_refs: []
  started_at: null
window:
  start_tick: null
  peak_tick: null
  end_tick: null
  decay_mode: linear
scope:
  ecology_cell_ids: []
  route_ids: []
  resource_node_ids: []
  species_ids: []
deltas:
  activity: {}
  exposure: {}
  resource_pressure: {}
  movement_pressure: {}
  projection_weight: {}
weather_context:
  required: false
  minecraft_weather_refs: []
  tactical_weather_authority: false
observations:
  channels: []
  confidence_rules: []
interventions: []
consequences: []
mechanical_handoff:
  mode: none_by_default
  capability_dependencies: []
```

## Trigger families

Allowed initial trigger families:

- `WEATHER_PULSE`
- `RESOURCE_FLUSH`
- `RESOURCE_COLLAPSE`
- `BREEDING_AGGREGATION`
- `NESTING_DEFENSE_WINDOW`
- `MIGRATION_WAVE`
- `MIGRATION_BOTTLENECK`
- `DISTURBANCE_DISPLACEMENT`
- `PREDATOR_PRESSURE_SHIFT`
- `ROUTE_CLOSURE_REDISTRIBUTION`
- `RECOVERY_SUCCESSION_PULSE`

An anomaly/supernatural family requires separate approval and provenance. It must not be inferred from ordinary ecology.

## Lifecycle

```text
DORMANT
-> FORMING
-> ACTIVE
-> DECAYING
-> RESOLVED
```

Optional terminal state:

`TRANSFORMED`

Use `TRANSFORMED` when the pulse creates a new persistent ecological condition rather than returning to baseline.

Examples:

- temporary rain aggregation returns to baseline -> RESOLVED;
- repeated disturbance causes long-term route abandonment -> TRANSFORMED;
- resource collapse causes durable migration shift -> TRANSFORMED.

## Population protection

A pulse may modify:

- probability of a persistent individual being locally active;
- probability of a population member being exposed;
- local movement pressure;
- temporary concentration across cells;
- native spawn projection weight within already legal habitat/context;
- observation likelihood.

A pulse may not directly modify:

- population count;
- births/deaths;
- individual HP/status;
- tactical position;
- capture/fainting outcome;
- species habitat legality.

Those require their owning systems.

## Cobblemon projection

Projection order:

```text
Minecraft/Cobblemon native eligibility
-> Ouros approved species presence
-> persistent ecology state
-> pulse activity/exposure modifiers
-> persistent-individual reconciliation
-> visible actor projection
```

A pulse cannot make an ecologically or natively invalid species legal merely because it is dramatic or popular.

Generic spawned actors remain presentation candidates. They do not become canonical population records unless a separate Ouros persistence boundary explicitly promotes an individual.

## Weather authority

Minecraft weather can serve as:

- trigger context;
- observation evidence;
- projection condition;
- ambient presentation.

Minecraft weather does not automatically become authoritative tactical weather.

When a structured encounter begins:

```text
Ouros decides whether tactical weather is part of encounter state
-> AutoPTU receives explicit weather state if supported
-> AutoPTU resolves mechanics
-> semantic result returns to ecology
```

This prevents a client/server weather frame from silently changing PTU outcomes.

## Observation contract

Every pulse can expose signals without exposing hidden cause.

Recommended channels:

- visual concentration;
- visual absence elsewhere;
- calls/alarm behaviour;
- tracks/traces;
- resource damage/use;
- nesting activity;
- route congestion;
- weather/instrument reading;
- human report;
- institutional report;
- repeated survey comparison.

Observation records should reference the event only internally. Player/NPC-facing knowledge receives evidence packets, not `event_id -> true cause` unless a legitimate information path exists.

## Intervention contract

Interventions alter drivers, pressure or consequences. They do not merely set `quest_complete`.

Examples:

```yaml
- type: route_closure
  target: disturbance_pressure
  expected_effect: reduce_contact

- type: resource_support
  target: resource_pressure
  expected_effect: redistribute_foraging

- type: observation_only
  target: evidence_quality
  expected_effect: improve_hypothesis_confidence

- type: escort_or_rescue
  target: movement_pressure
  expected_effect: preserve_safe_passage
```

Interventions can fail, partially work or create side effects.

## Mechanical handoff

Default pulse operation is world-state only and requires no AutoPTU tactical categories.

A direct structured encounter must list exact dependencies.

Current audited status:

- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy / initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

Latest read-only AutoPTU-Java evidence checked for this contract:

`1d3ce8784cf5a327ef8dce44e6e73effd1956c3a` — generic movement landing hook registry.

This does not promote any permanent family.

## Reduced encounter profile

A pulse-related encounter can ship before rich tactical support if it uses this reduced profile:

```text
Ouros world-state pulse
-> visible actor projection
-> simple explicit escalation decision
-> ordinary AutoPTU battle using only individually verified move/ability/status subset
-> semantic outcome
-> ecology consequence
```

Forbidden shortcuts:

- Minecraft collision decides capture/fainting;
- visual despawn equals death/flee success;
- vanilla weather applies PTU modifiers without handoff;
- pathfinding result decides forced movement legality;
- hidden NPC-vs-wild tactical battle is simulated to update ecology.

## Full encounter profile

The intended richer version can add:

- pursuit/escape;
- forced displacement;
- weather phases;
- hazard zones;
- reactions/interception;
- ability-driven terrain/weather;
- Trainer Feature interrupts;
- multi-actor tactical policy.

Each of those consumes its exact capability family and remains blocked/partial until verified by current engine tests/contracts.

## Persistence and decay

Pulse state must survive server lifecycle when its active window spans persistence boundaries.

Required durable fields:

```text
event id
source process
lifecycle state
start/peak/end times
deltas already applied
interventions received
consequence candidates
last evaluated tick/version
```

On reload, Ouros recalculates event state from authoritative time/state. It must not replay already-applied consequences.

## Determinism fixture requirements

At least these cases need regression coverage:

1. pulse raises exposure without changing population count;
2. pulse decay restores baseline projection weights;
3. two observations can disagree without revealing hidden cause;
4. intervention changes pressure before resolution;
5. server reload does not duplicate consequences;
6. persistent named individual is not cloned during a high-projection pulse;
7. invalid native habitat remains invalid even with positive pulse weight;
8. structured battle outcome returns semantic consequence without importing Minecraft combat facts.

## Immediate implementation value

This contract gives the ecology service a bounded event primitive that can drive visible world change before full tactical ecology is available.

It also provides a clean seam for later global-world integration:

```text
real generated biome/cell
-> persistent population/resource state
-> pulse driver
-> Cobblemon-compatible projection
-> player observation/intervention
```

No new canon species, biome, country, route or permanent event is created by this design document.
