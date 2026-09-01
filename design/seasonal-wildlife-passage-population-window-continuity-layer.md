# Seasonal Wildlife Passage and Population Window Continuity Layer

Status: DESIGN / PROPOSED ARCHITECTURE
Pass: 194
Canon effect: NONE until explicit promotion. This layer must reuse canon locations, residents, factions, and authority boundaries.

## Purpose

Represent temporary ecological change in a durable world without treating spawn state as truth and without making every wildlife event a battle.

The layer covers recurring or one-off population windows such as:
- passage through a route segment;
- temporary gathering around water, food, shelter, or another observed condition;
- unusual local concentration;
- locally reduced sightings;
- recurring observation windows;
- temporary use of a corridor or resting area.

It does not define species-specific Caelo ecology. Those facts require explicit canon/source evidence.

## Core separation

The simulation needs two related but different objects:

1. `ecological_window`
   - authoritative world condition when an authored system has enough evidence to establish one;
   - may still have unknown cause;
   - controls world continuity, not NPC omniscience.

2. `ecological_observation`
   - what an observer actually recorded at a particular place and time;
   - includes method, confidence, source, and limitations;
   - can be wrong, incomplete, or superseded without rewriting the historical record.

This separation lets the world know that a temporary concentration exists while Nerea, Mara, a producer, and the player each hold different evidence about it.

## Proposed record: ecological_window

```yaml
ecological_window:
  ecological_window_id: null
  status: proposed | active | declining | ended | uncertain
  phenomenon_type: passage | concentration | reduced_presence | gathering | corridor_use | other_authored
  species_scope: []
  population_scope_note: null
  location_ids: []
  spatial_envelope_ref: null
  start_bound:
    earliest: null
    latest: null
  end_bound:
    earliest: null
    latest: null
  recurrence_model: none | suspected | historical_pattern | authored_recurring
  cause_state: unknown | hypothesis_only | established
  cause_refs: []
  observation_refs: []
  access_effect_refs: []
  settlement_effect_refs: []
  encounter_policy_ref: null
  provenance_refs: []
  canon_status: proposed | approved
```

`population_scope_note` must describe only what the authored window actually establishes. Avoid fabricated numeric populations unless a source/canon decision supplies them.

## Proposed record: ecological_observation

```yaml
ecological_observation:
  observation_id: null
  observer_refs: []
  institution_ref: null
  timestamp_or_window: null
  location_ref: null
  method: direct_sighting | transect | tracks | call | photo | report | indirect_sign | other
  species_claims: []
  count_claim:
    value: null
    type: exact | minimum | approximate | none
  behavior_claims: []
  environmental_context_refs: []
  disturbance_context: null
  negative_observation: false
  confidence: low | medium | high | method_specific
  limitations: []
  source_record_ref: null
  supersedes_ref: null
  interpretation_refs: []
```

A negative observation means the method did not detect the target during that observation. It does not mean zero individuals existed.

## Proposed record: ecology_hypothesis

```yaml
ecology_hypothesis:
  hypothesis_id: null
  statement: null
  author_refs: []
  first_recorded_at: null
  supporting_observation_refs: []
  conflicting_observation_refs: []
  status: open | weakened | strengthened | rejected | established
  revision_refs: []
```

This reuses the repository's existing provenance philosophy. It does not create a parallel scientific-truth system.

## Spatial model

Ecological windows should reference canonical geography at the smallest useful level.

Marea examples already available without creating new places:
- Sendero del Vidrio south trailhead;
- lower shelf;
- seasonal crossing;
- upper junction;
- Mirador transect trailhead;
- station surroundings;
- Puerto Bruma ferry landing where relevant to coastal observations.

A window can occupy one segment while the rest of the route remains ordinary.

Avoid `WHOLE_REGION_AFFECTED = true` when observations only cover one transect.

## Temporal model

Use bounded uncertainty where appropriate.

Example:
- first confirmed observation: day 18 morning;
- no observation was made between day 16 evening and day 18 morning;
- therefore the start is bounded, not known exactly.

The same applies to end state.

This creates useful revisits: the player may help narrow a window without receiving an arbitrary countdown timer.

## Recurrence model

Recurring events need provenance.

`historical_pattern` means records suggest recurrence.
`authored_recurring` means canon has explicitly established a recurring ecological pattern.
`suspected` means one or more actors believe recurrence is plausible.

Never promote `suspected` because an event happened twice in gameplay unless the evidence policy supports that inference.

## Human response boundary

Ecology can produce reasons for existing systems to act:
- Mara may recommend a route check;
- an authorized actor may issue or request an access change through the existing closure/access layer;
- Jo may reschedule a field-school exercise;
- Nerea/Ema may add transects;
- Alba or Brin may alter ordinary work timing if a relevant route is affected;
- Lia/Mina may report observations near ferry operations.

This layer stores the ecological reason and evidence. It does not grant those actors new powers.

`ECOLOGICAL_WINDOW != CLOSURE`
`ECOLOGICAL_WINDOW != EMERGENCY`
`ECOLOGICAL_WINDOW != CAPTURE_PERMISSION`

## Pokémon agency boundary

A population window describes a pattern across observations. It should not erase individual Pokémon agency.

An individual may:
- travel outside the dominant route;
- remain after most of a group leaves;
- approach or avoid people;
- be injured or separated;
- become a persistent individual only through an explicit identity transition.

Do not turn every member of a temporary concentration into interchangeable spawn inventory.

## Capture boundary

No generic Ouros rule is introduced for capture restrictions, bonuses, scarcity, or ethical penalties during a population window.

If PTU/Caelo establishes such a rule later, use it directly.

Narrative may record social expectations only after canon establishes them.

## Spawn and Minecraft boundary

Minecraft/Cobblemon actors may project an ecological window visually, but projection must be downstream from Ouros world state.

Required invariants:

`MINECRAFT_SPAWN != CANONICAL_ARRIVAL`
`MINECRAFT_DESPAWN != CANONICAL_DEPARTURE`
`CHUNK_UNLOAD != POPULATION_LEFT`
`SPAWN_COUNT != AUTHORITATIVE_POPULATION_COUNT`
`SPECIES_HABITAT_TAG != CURRENT_LOCAL_PRESENCE`
`PLAYER_FAILED_TO_SEE != SPECIES_ABSENT`

The adapter may choose a bounded visible sample appropriate for performance. The narrative state remains independent of how many actors are simultaneously rendered.

## Observation gameplay

Useful actions that require no battle:
- repeat a transect at another time;
- compare direct sightings with historical records;
- inspect a route segment for indirect signs;
- deliver a dated field note to Mirador;
- compare observations from different residents;
- identify that two counts used incompatible methods;
- mark a report as insufficient rather than forcing a conclusion;
- revisit after the window may have ended;
- document an ordinary route returning to normal use.

Skills and Features can gate or modify specific actions only when authoritative PTU rules support them. Narrative must not create generic `Ecology +2` bonuses.

## Population-event quest structure

A robust small arc can use this sequence:

`signal -> corroboration attempt -> bounded response -> repeat observation -> interpretation -> end/continuation -> aftermath`

The player does not need to witness every stage.

Example autonomous progression:
- Ema records the first concentration;
- Mara changes an ordinary field visit time;
- the player is elsewhere;
- Nerea schedules a second observation;
- the player returns to find two dated records and a practical route advisory;
- a later transect finds ordinary activity again.

## Thin Delivery Season integration

This layer may generate evidence relevant to `ouros.arc.thin_delivery_season` but cannot resolve it automatically.

Allowed relationship:
- a temporary concentration overlaps a delivery route segment;
- one or more deliveries were irregular during part of that interval;
- residents discuss whether the events are connected.

Forbidden automatic inference:

`TEMPORAL_OVERLAP -> DELIVERY_CAUSE`

The delivery arc already states that no canonical cause is established at campaign start. Any eventual causal conclusion needs its own evidence and canon promotion.

## Encounter compilation policy

An ecological observation should not compile a BattleSpec merely because wild Pokémon exist nearby.

Compile combat only when:
- a concrete immediate confrontation exists;
- the roster is explicitly determined by world state;
- battle legality can be assembled from authoritative content;
- the battle output can remain narrow enough that it does not decide ecological causation.

An outbreak/concentration must never be represented by “fight arbitrary waves until the ecology is solved.”

## Rich encounter concept template

### Passage at the Seasonal Crossing

Narrative premise:
A temporary concentration is using the Sendero del Vidrio seasonal crossing. A route user reaches the segment while a field observation is underway. Most of the scene concerns distance, timing, observation, and withdrawal. A confrontation only develops if a specific individual actively blocks safe passage or another authored immediate trigger exists.

Full version can include:
- irregular footprint geometry;
- route-edge positioning;
- corridor protection;
- interception;
- forced movement near an unsafe edge;
- environmental zones;
- status-producing Moves;
- objective-aware wild AI that may prefer withdrawal, space-making, or route passage over KO seeking;
- faithful Minecraft/Cobblemon projection.

Full dependency families:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when used;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items when roster uses them;
- Trainer Features/perks when Trainers participate;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

### Reduced version

Narrative owns:
- active ecological window;
- observers and noncombatants;
- route advisory/access state;
- safe-distance movement before combat;
- population observations;
- whether the larger group continues through the corridor.

If one immediate wild actor still prevents safe passage, compile a separate ordinary audited BattleSpec on stable geometry. Do not represent the whole migrating/gathering population as combatants.

Allowed narrow outputs:
- `IMMEDIATE_CROSSING_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`
- `IMMEDIATE_FIELD_TEAM_CAN_WITHDRAW`

Disallowed battle outputs:
- `MIGRATION_ENDED`
- `POPULATION_DISPERSED`
- `SPECIES_CAUSED_DELIVERY_SHORTFALL`
- `ROUTE_PERMANENTLY_SAFE`
- `CAPTURE_NOW_AUTHORIZED`
- `ECOLOGY_HYPOTHESIS_PROVEN`

## Persistent aftermath

A window ending should leave evidence rather than vanish cleanly.

Possible aftermath:
- dated Mirador observations;
- a revised route advisory;
- a field-school handout updated after better evidence;
- an old report preserved at Tideglass;
- changed work timing during the window;
- a later survey comparing the same segment;
- a resident remembering a practical inconvenience without knowing the ecological cause.

## Canon promotion checklist

Before promoting a specific Marea ecological window, canon review should answer only the facts needed for that window:
- species or species group;
- location envelope;
- temporal envelope or recurrence rule;
- what is actually known about behavior;
- whether a cause is known;
- whether any institutional response is canon;
- whether capture/access doctrine is defined elsewhere;
- whether the event modifies Thin Delivery Season evidence;
- whether any persistent individual Pokémon emerges from the event.

Unknown fields should remain unknown instead of being filled for completeness.
