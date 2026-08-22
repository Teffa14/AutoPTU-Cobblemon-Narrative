# Diel Activity and Circadian Rhythms Layer

Status: PROPOSED SYSTEM DESIGN. Not canon. Not a PTU rules replacement.
Pass: 96

## Purpose

This layer gives Ouros a persistent model for when Pokémon, populations, NPCs and ecological interactions are actually active across the daily cycle.

It exists because the repository already knows what time it is, what the light level is, what season it is and what locations exist, but those facts do not by themselves determine biological activity.

The layer must support repeated discovery, local variation and long-term shifts without turning time of day into an unofficial battle modifier.

## Core separations

Ouros must keep these facts independent:

- local clock time;
- sunrise/sunset/twilight window;
- physical lightscape;
- broad species expectation;
- local population activity profile;
- individual activity history;
- observation effort;
- what a player believes;
- current loaded Cobblemon entities;
- PTU Sleep/status state;
- tactical battle effects.

A Pokémon resting in a roost is not mechanically Asleep unless the PTU engine says so.

A nocturnal species does not gain a nighttime combat bonus from this layer.

## 1. DIEL_PROFILE

A `DIEL_PROFILE` describes an evidence-backed activity pattern for a specific scope.

Suggested fields:

```yaml
diel_profile_id: null
scope_type: SPECIES | POPULATION | COLLECTIVE | INDIVIDUAL
scope_id: null
location_scope_id: null
season_scope_id: null
revision_id: null
valid_from: null
valid_to: null
classification: UNKNOWN
activity_windows: []
rest_windows: []
activity_peaks: []
observation_basis_ids: []
sampling_effort_summary: null
confidence: null
source_refs: []
```

Allowed coarse classifications can include:

- DIURNAL
- NOCTURNAL
- CREPUSCULAR
- CATHEMERAL
- MULTI_PEAK
- SEASONALLY_VARIABLE
- LOCALLY_SHIFTED
- UNKNOWN

These classifications summarize evidence. They do not define spawn rules by themselves.

## 2. ACTIVITY_WINDOW

An `ACTIVITY_WINDOW` records a recurring interval in local ecological time.

```yaml
activity_window_id: null
profile_id: null
window_type: FORAGING | TRAVEL | DISPLAY | SOCIAL | HUNTING | REST | ROOST | NEST_ATTENDANCE | OTHER
anchor_type: CLOCK | DAWN | DUSK | SUNRISE | SUNSET | TIDE | EVENT
start_offset: null
end_offset: null
season_refs: []
weather_constraints: []
location_refs: []
evidence_ids: []
confidence: null
```

Use relative dawn/dusk anchors where useful instead of hardcoding 18:00 across every region and season.

## 3. ACTIVITY_OBSERVATION

An observation records detection or behavior at a specific time.

```yaml
activity_observation_id: null
observer_id: null
observed_entity_ids: []
species_ids: []
collective_id: null
location_id: null
timestamp: null
observation_method: DIRECT | CAMERA | AUDIO | TRACK | SENSOR | REPORT
behavior_code: null
presence_state: DETECTED | NOT_DETECTED
sampling_duration: null
sampling_effort_ref: null
lightscape_ref: null
weather_ref: null
temperature_ref: null
human_activity_ref: null
source_refs: []
confidence: null
```

`NOT_DETECTED` is not `ABSENT`.

## 4. SAMPLING_EFFORT

Activity inference is unreliable if observation effort is uneven.

```yaml
sampling_effort_id: null
location_id: null
method: null
start_time: null
end_time: null
active_hours: null
coverage_gaps: []
equipment_state_ref: null
observer_count: null
notes: null
```

A route with ten night camera-hours and zero day camera-hours cannot support a strong night/day comparison.

## 5. REST_SITE and ROOST_SITE

Resting places can be persistent ecological objects.

```yaml
rest_site_id: null
location_id: null
site_type: ROOST | BURROW | NEST | SHELTER | WATER_REFUGE | CANOPY_REFUGE | STRUCTURE
known_user_scope_ids: []
use_windows: []
occupancy_observations: []
disturbance_refs: []
physical_state_ref: null
access_sensitivity: null
```

Do not infer ownership, family structure or emotional attachment from repeated use.

## 6. ACTIVITY_SHIFT_CASE

A local activity pattern can change over time.

```yaml
activity_shift_case_id: null
scope_id: null
baseline_profile_id: null
candidate_profile_id: null
first_detected: null
change_dimensions: []
hypotheses: []
linked_disturbance_ids: []
linked_weather_ids: []
linked_light_ids: []
linked_heat_ids: []
linked_predator_prey_ids: []
status: OPEN | SUPPORTED | REJECTED | UNRESOLVED
```

Possible observations:

- later activity after a new road opens;
- earlier dawn movement during a heatwave;
- reduced overlap between two species;
- increased use of a city park after midnight;
- abandonment of a daytime rest site.

Do not write fear, stress or avoidance as internal emotion unless evidence supports it.

## 7. TEMPORAL_NICHE_OVERLAP

Ouros may compare when two populations use the same place.

```yaml
temporal_overlap_id: null
scope_a_id: null
scope_b_id: null
location_id: null
period: null
profile_a_ref: null
profile_b_ref: null
overlap_class: LOW | MODERATE | HIGH | UNKNOWN
method_ref: null
interpretation_refs: []
```

This is ecological analysis, not a battle aggro relationship.

## 8. DAILY_ECOLOGICAL_STATE

For performance, the world server can derive coarse current activity bands without simulating every individual.

Example:

```yaml
daily_ecological_state:
  location_id: route-14-marsh
  local_time_band: PRE_DAWN
  active_profile_refs:
    - pop-wooper-east
    - collective-murkrow-3
  low_activity_profile_refs:
    - pop-oddish-orchard
  projected_presence_budget: LOW
  last_recomputed_at: null
```

The projection is a cache. Persistent population truth remains elsewhere.

## 9. PLAYER DISCOVERY

Players can learn timing through:

- repeated direct observation;
- camera traps;
- acoustic logs;
- field notebooks;
- local knowledge;
- old reports;
- comparing day/night versions of the same route;
- following tracks to a rest site;
- discovering that an old schedule no longer fits current behavior.

The UI should present uncertainty qualitatively unless a research system explicitly supports quantitative estimates.

## 10. ENCOUNTER GENERATION

The diel layer can influence whether a population is eligible to be considered for an overworld encounter.

Safe pipeline:

```text
persistent population
    -> habitat eligibility
    -> season/weather constraints
    -> diel activity profile
    -> current local activity band
    -> bounded Cobblemon projection
    -> player/world interaction
    -> optional AutoPTU battle
```

Forbidden shortcut:

```text
clock says night -> spawn rare nocturnal Pokémon
```

The server should apply rate limits, population state and anti-exploit controls before any projection.

## 11. DAILY ROUTINES FOR IMPORTANT NPCs

NPC schedules can use the same local clock but remain authored/social state rather than biological profiles.

A researcher might work dawn surveys for one month and switch shifts later.

Do not infer that a person is nocturnal, depressed, insomniac or unhealthy because they work at night.

## 12. MULTIPLAYER

Different players can know different timing information.

One player may have observed a Dreepy group at dusk. Another may only know a public report that says “evening”. A third may possess a newer survey showing the activity window shifted.

Shared party maps should not automatically reveal private research notes unless the player shares them.

## 13. OFFLINE ADVANCEMENT

The world does not need minute-by-minute simulation.

When a location is unloaded, the server can advance:

- clock and season;
- expected activity phase;
- coarse population/collective state;
- scheduled observations or institutional monitoring where explicitly modeled.

Do not generate thousands of unseen individual foraging events.

## 14. HANDOFF TO OTHER LAYERS

Calendar/Seasonality supplies local time and solar anchors.

Light supplies illumination.

Meteorology and Urban Heat supply environmental context.

Photography and Soundscape supply timestamped evidence.

Wild Collectives supply group identity.

Interspecies Ecology can consume temporal overlap.

Road Ecology, Tourism, Public Space and Conservation can generate disturbance schedules.

Travel can consume verified activity windows for optional route content.

## 15. PTU / AutoPTU BOUNDARY

Narrative activity state never creates:

- Sleep;
- Insomnia;
- Early Bird;
- Vital Spirit;
- Accuracy modifiers;
- initiative modifiers;
- surprise;
- stealth bonuses;
- encounter-rate bonuses;
- fatigue;
- AP recovery;
- healing;
- damage;
- Weather;
- Terrain;
- status immunity.

Those require exact PTU/Caelo rules and engine support.

## 16. ENCOUNTER CONTRACTS

### Dawn Roost Survey

Narrative premise:
A long-monitored roost empties earlier than its historical dawn window during a period of road construction and warm nights.

FULL version:
Players survey the roost while groups leave dynamically. The battle area can include moving noncombatants, protected roost zones and withdrawal objectives if a conflict occurs.

Dependencies:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement including interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy for WITHDRAW/PROTECT_ROOST;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED version:
The roost departure is resolved before combat. If a confrontation occurs, only involved combatants enter a static arena after the roost has cleared.

### Evening Flight Window

Narrative premise:
A recurring Dreepy evening movement over a coastal reach no longer overlaps the observation station's historical schedule.

FULL version:
Moving aerial groups cross the area during a limited window while players protect instruments and collect observations.

Key blockers:
- complete movement;
- aerial/vertical tactical representation;
- tactical AI;
- adapter/playback.

REDUCED version:
The flight is an overworld observation event. Any battle is separate and static.

### Night Market Wildlife Shift

Narrative premise:
A settlement extends a night market and a nearby population begins using the public-space edge at a different time.

FULL version:
Civilian flows, wildlife withdrawal and protected lanes coexist dynamically.

Key blockers:
- complete movement;
- zones/reactions;
- tactical AI;
- civilian/adaptor playback.

REDUCED version:
The server clears the encounter perimeter first. Market activity and wildlife timing remain persistent world state; AutoPTU receives a normal battle.

## 17. IMPLEMENTATION BLOCKERS

`OVERWORLD_DIEL_PROFILE_STATE`
Versioned activity profiles by population/location/season.

`OVERWORLD_ACTIVITY_OBSERVATION_LEDGER`
Timestamped observations with method and provenance.

`OVERWORLD_SAMPLING_EFFORT`
Coverage needed to distinguish absence from non-detection.

`OVERWORLD_REST_ROOST_STATE`
Persistent rest sites and use histories.

`OVERWORLD_ACTIVITY_SHIFT_CASES`
Evidence-backed changes through time.

`OVERWORLD_TEMPORAL_NICHE_OVERLAP`
Coarse overlap analysis between populations.

`OVERWORLD_DIEL_TO_COBBLEMON`
Bounded activity projection without making loaded spawns population truth.

`OVERWORLD_DIEL_TO_BATTLE`
A battle snapshot contract that only maps time-dependent mechanics when exact PTU rules exist.

## 18. CANON QUESTIONS

Before promotion, Ouros needs decisions on:

- which species/populations receive authored baseline activity profiles;
- whether profiles start mostly unknown and are discovered through play;
- how much local variation is allowed before human review;
- how daily timing interacts with regional seasons and latitude;
- whether institutions publish wildlife activity guides;
- what time-based access is considered ordinary versus protected;
- what anti-exploit rules constrain repeated time skipping;
- which PTU/Caelo mechanics actually depend on time of day, if any;
- whether Minecraft time can be accelerated and how that affects ecological state.

## Guardrail summary

Time is world state.

Activity is biological/social state.

Detection is evidence.

Sleep is a PTU mechanic only when the rules engine says so.

A change in timing can matter for ecology and story without changing battle math.