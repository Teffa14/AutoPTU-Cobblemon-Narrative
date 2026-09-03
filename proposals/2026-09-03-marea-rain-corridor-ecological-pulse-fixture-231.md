# Marea Rain Corridor Ecological Pulse Fixture — Pass 231

Status: PROPOSED IMPLEMENTATION FIXTURE. Does not change canon.
Date: 2026-09-03

## Purpose

Provide one concrete Marea use of `design/ecological-pulse-event-contract.md` while preserving the current global-world migration gate and avoiding unverified species/biome assumptions.

This is a reusable scenario family rather than a fixed plot.

## Semantic sites

```yaml
site_refs:
  - marea.sendero_lower_shelf
  - marea.sendero_seasonal_crossing
  - marea.estacion_mirador_observation_network
coordinate_binding: migrate_after_global_world_lock
minecraft_biome_binding: unresolved
species_binding: unresolved_until_native_habitat_validation
```

Existing canonical coordinate anchors remain untouched.

## Scenario family — Rain Corridor Compression

A sustained rain pulse changes route usability and resource access across part of Sendero del Vidrio.

The ecology service records a temporary movement-pressure shift. Several approved local populations concentrate along the remaining viable corridor. Other areas show temporary absence.

The player-facing world therefore shows both concentration and silence.

The event is not automatically a population boom.

## Authoritative state

```yaml
id: marea.fixture.rain_corridor.01
type: ecological_pulse
trigger:
  kind: WEATHER_PULSE
  condition_refs:
    - persistent_rain_context
scope:
  ecology_cell_ids:
    - sendero_lower_shelf_unbound
    - sendero_crossing_unbound
deltas:
  activity:
    corridor_users: +moderate
  exposure:
    corridor_users: +high
    displaced_elsewhere: -moderate
  movement_pressure:
    seasonal_crossing: constrained
  projection_weight:
    legal_corridor_species: +temporary
weather_context:
  required: true
  tactical_weather_authority: false
mechanical_handoff:
  mode: none_by_default
```

Species keys remain abstract until the generated world and native Cobblemon habitat envelope are validated.

## Visible manifestations

Potential world-facing signs:

- unusually frequent wildlife crossings along one safe shelf;
- fresh tracks/traces overlapping in a narrow corridor;
- reduced sightings at normally active side paths;
- water/current/noise changes at the seasonal crossing;
- repeated Mirador reports showing the same spatial shift;
- producer/route-worker reports of wildlife appearing at unusual times or closer to human movement.

No single sign identifies the hidden driver with certainty.

## Player entry points

The scenario can surface through different institutions without changing its ecology truth.

Mara Veyra can receive route congestion reports and request field confirmation.

Dr. Nerea Sol can notice a change in repeated observation density and ask for additional transect evidence.

A route worker can report that Pokémon are using a crossing at an unusual rate.

A producer can notice increased edge activity without knowing whether rain, food pressure or another species caused it.

## Competing hypotheses

```text
H1: rain physically compressed normal movement into a smaller viable corridor
H2: a resource pulse is attracting multiple species independently
H3: predator pressure displaced prey toward the corridor
H4: human disturbance closed an alternate route
H5: the sightings are biased because observers themselves moved to the safer route
```

The system should permit multiple causes to coexist.

## Investigation loop

```text
report
-> inspect corridor
-> inspect low-activity comparison site
-> compare weather/resource/trace evidence
-> update hypotheses
-> choose intervention or observe only
-> allow pulse to decay or transform
-> compare later state
```

## Intervention options

### Observation only

No tactical handoff.

Effect:
- higher evidence quality;
- no direct ecology pressure change.

### Temporary human-route diversion

No tactical handoff by default.

Effect:
- reduces human disturbance in the compressed corridor;
- may lower defensive/avoidance pressure;
- may increase travel inconvenience elsewhere.

### Resource protection

No battle required.

Effect:
- prevents a concentrated wildlife pulse from damaging one vulnerable resource node;
- can shift activity to another legal resource.

### Guided crossing / rescue

Reduced implementation:
- world-state objective plus visible movement presentation;
- no claim that Minecraft pathfinding proves PTU movement legality;
- success determined by explicit Ouros objective state, not entity survival heuristics.

Full intended version may include movement checks, hazards, reactions and escort protection if those contracts are verified.

### Defensive structured encounter

Only when a visible actor escalates and Ouros explicitly hands off to AutoPTU.

Reduced version dependencies:

- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- core calculations: VERIFIED;
- action economy / initiative: VERIFIED;
- AI legal-action infrastructure: VERIFIED;
- exact moves/abilities/statuses used: verify individually;
- AI tactical policy: BLOCKING as complete family;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

Full version may additionally require:

- complete movement: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL.

## Weather rule

The Minecraft rain event can trigger or present the ecological pulse.

It must not silently become tactical rain.

If battle begins, Ouros explicitly decides whether the encounter has tactical weather and only passes that state when the AutoPTU weather contract for the encounter is supported.

## Possible consequences

The event can resolve without permanent change.

Possible persistent outcomes if conditions justify them:

- animals habituate to a temporary human diversion;
- repeated corridor compression increases future avoidance pressure;
- route workers establish a seasonal warning practice;
- a resource node becomes degraded after repeated concentration;
- the movement route becomes a recurring seasonal migration path;
- evidence disproves the initial human explanation and changes institutional knowledge.

None of these outcomes are canon until promoted through the normal review path.

## Success criteria

The fixture works when:

- visible abundance changes without population inflation;
- at least one comparison site becomes quieter while the corridor becomes busier;
- NPCs receive evidence rather than hidden truth;
- the player can intervene without mandatory combat;
- a direct encounter uses AutoPTU authority only;
- weather presentation cannot silently write tactical state;
- the scenario can bind to real generated coordinates/biomes later without rewriting its narrative premise.

## Open implementation questions

- exact Minecraft weather duration to ecology-tick conversion;
- how route viability is represented before final world geometry is frozen;
- maximum projection multiplier before visible density becomes implausible;
- how persistent named Pokémon choose corridor presence during a pulse;
- whether repeated rain pulses can promote a seasonal migration edge in the species interaction graph.
