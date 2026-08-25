# Seasonal Dormancy, Torpor and Hibernation Layer

Status: PROPOSED SYSTEM DESIGN. Not canon. Not a PTU rules replacement.
Pass: 171

## Purpose

This layer models prolonged or recurrent low-activity states that operate on a longer timescale than ordinary daily rest.

It extends Diel Activity and Seasonality without replacing either authority.

The layer must support:

- population- and individual-level dormancy histories;
- uncertain entry and exit dates;
- repeated torpor/arousal cycles where authored;
- den/hibernaculum identity;
- monitoring effort and disturbance-sensitive surveys;
- multi-year shifts in timing;
- separation between ecological inactivity and PTU Sleep.

## Authority boundaries

Diel Activity owns ordinary daily activity/rest profiles.

Seasonality owns recurring annual windows and phenological context.

Care owns welfare, diagnosis and treatment.

Cryosphere/Meteorology own snow, cold and weather truth.

Pokémon Agency owns individual identity, partnership, custody and release history.

Wildlife Telemetry/Community Science/Photography/Acoustics can provide observations.

Pass 171 owns the longitudinal dormancy state assembled from those observations.

## Core state model

### DORMANCY_PROFILE

```yaml
dormancy_profile_id: null
scope_type: SPECIES | POPULATION | COLLECTIVE | INDIVIDUAL
scope_id: null
location_scope_id: null
profile_type: HIBERNATION | DAILY_TORPOR | SEASONAL_TORPOR | AESTIVATION | OTHER_AUTHORED | UNKNOWN
expected_window_ref: null
entry_cues_claims: []
exit_cues_claims: []
known_site_refs: []
evidence_ids: []
confidence: null
valid_from: null
valid_to: null
```

A profile is an evidence-backed expectation, not a switch that forces every individual into the same state.

### DORMANCY_EPISODE

```yaml
dormancy_episode_id: null
scope_id: null
site_id: null
season_id: null
entry_interval:
  earliest: null
  latest: null
exit_interval:
  earliest: null
  latest: null
state: CANDIDATE | ENTRY_OBSERVED | DORMANT_INFERRED | AROUSAL_OBSERVED | EXIT_OBSERVED | CLOSED | UNRESOLVED
observation_ids: []
coverage_refs: []
interpretation_refs: []
confidence: null
```

Use intervals when the exact entry or exit was not observed.

Do not backfill a precise date because a monitoring series has a gap.

### TORPOR_AROUSAL_OBSERVATION

```yaml
torpor_arousal_observation_id: null
episode_id: null
observed_at: null
method: DIRECT | CAMERA | THERMAL | ACOUSTIC | TELEMETRY | TRACK | OTHER
observation_type: INACTIVE | TORPOR_LIKE | AROUSAL | MOVEMENT | FEEDING | EXIT | RETURN | UNKNOWN
sampling_effort_ref: null
disturbance_ref: null
source_refs: []
confidence: null
```

An arousal observation does not automatically close the episode.

### DORMANCY_SITE

```yaml
dormancy_site_id: null
location_id: null
site_type: DEN | HIBERNACULUM | BURROW | CAVE_SECTION | TREE_CAVITY | SUBSTRATE_REFUGE | STRUCTURE | OTHER
physical_revision_ref: null
use_history: []
access_sensitivity: PUBLIC | LIMITED | RESTRICTED | UNKNOWN
monitoring_refs: []
disturbance_refs: []
```

Repeated use does not prove ownership, kinship or exclusive occupancy.

### DORMANCY_TIMING_REVISION

```yaml
dormancy_timing_revision_id: null
scope_id: null
baseline_period: null
comparison_period: null
entry_shift_class: EARLIER | LATER | NO_CLEAR_SHIFT | UNKNOWN
exit_shift_class: EARLIER | LATER | NO_CLEAR_SHIFT | UNKNOWN
coverage_comparability_ref: null
candidate_drivers: []
status: OPEN | SUPPORTED | REJECTED | UNRESOLVED
```

Candidate drivers may reference temperature, snow, food availability, disturbance or other world-state systems. Correlation does not become causation automatically.

## Monitoring and non-detection

A winter survey must retain:

- dates and duration;
- site coverage;
- method;
- equipment uptime;
- inaccessible zones;
- disturbance limits;
- observer restrictions;
- weather/visibility context where relevant.

`NOT_DETECTED` is not `ABSENT`.

A monitoring program may intentionally avoid parts of a site to reduce disturbance.

## Entry and exit

Safe inference sequence:

```text
last normal-activity observation
    -> entry interval
    -> evidence of reduced activity/site use
    -> dormant inference
    -> possible arousal observations
    -> exit/emergence interval
    -> renewed activity observations
```

Do not create a universal temperature threshold.

## Individual identity

An individual retains the same `pokemon_entity_id` across dormancy.

Dormancy does not:

- suspend ownership/custody automatically;
- erase relationships;
- reset age;
- create a new entity on emergence;
- make a wild individual available for capture by default.

## Population projection

When a population is in a likely dormant period, the overworld projection may reduce ordinary visible activity only after population state, evidence and anti-exploit rules are considered.

Forbidden shortcut:

```text
winter -> species hidden
```

A dormant population can still produce occasional arousal observations, tracks, vocalizations or other evidence.

Loaded Cobblemon entities are never the dormancy census.

## Disturbance

Disturbance is world-state context.

Examples:

- cave tourism;
- roadwork;
- mining vibration;
- forestry;
- fire/smoke;
- floodwater;
- research access;
- recreation.

A disturbance record does not create damage, stress, awakening or abandonment without evidence.

## Long-term Chronicle

This layer supports:

- a den used for decades;
- emergence windows shifting gradually;
- a site becoming inaccessible after infrastructure change;
- a former monitoring site becoming protected;
- a winter with incomplete data;
- an individual reappearing after several seasons;
- a dormancy tradition in local culture that is only partly supported by ecology.

## Minecraft boundary

Minecraft can project:

- a closed cave gate;
- a den entrance;
- seasonal signage;
- monitoring equipment;
- a quiet overworld area;
- occasional authored emergence events.

Minecraft cannot decide:

- whether a Pokémon is biologically dormant;
- whether a site is occupied;
- exact entry/exit timing;
- welfare state;
- PTU Sleep;
- capture eligibility;
- disturbance consequences.

Chunk unload/despawn is never evidence of hibernation.

## PTU / AutoPTU boundary

Dormancy does not create:

- Asleep/Sleep;
- Frozen;
- Slowed;
- Vulnerable;
- Helpless;
- Fatigue;
- reduced Speed;
- reduced Evasion;
- AP changes;
- healing;
- HP regeneration;
- initiative modifiers;
- Surprise;
- automatic wake-up checks;
- capture bonuses.

If a battle explicitly requires a PTU Status or Move interaction, that mechanic must be validated separately against PTU/Caelo and live engine evidence.

## Encounter contracts

### Hibernaculum Access Interruption

Narrative premise:
A restricted winter cave needs a short equipment-recovery visit after a monitoring unit fails. The ecological objective is to minimize disturbance, not defeat the occupants.

FULL version:
Researchers and players move through a constrained route while dormant wildlife remains in protected/noncombat zones. A separate threat may force a tactical encounter with withdrawal and protected-area objectives.

Dependencies:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL when invoked:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement including interception/forced movement;
- terrain/weather/hazards/zones/reactions if cave constraints or protected cells have tactical effects;
- AI tactical policy for `WITHDRAW`, `PROTECT_RESEARCHER`, `AVOID_PROTECTED_ZONE`, `REACH_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED version:
Resolve equipment access and protected-site movement entirely in world state. Researchers leave the dormancy chamber. If a confrontation remains, use a static arena outside the sensitive zone. No dormant Pokémon enter combat automatically.

### Early Emergence Road Closure

Narrative premise:
Repeated observations suggest a local population is using a roadside area earlier than the historical emergence window, creating a temporary transport conflict.

FULL version:
Wildlife withdrawal/crossing, traffic closure and responders coexist dynamically.

BLOCKING:
- complete movement;
- AI tactical policy for `CROSS`, `WITHDRAW`, `CLEAR_ROUTE`;
- adapter/playback;
- terrain/weather/hazards/zones/reactions only if snow, ice or barriers have actual tactical effects.

REDUCED version:
Road/Wayfinding resolves the closure and population movement before battle. AutoPTU receives a normal static confrontation only if an unrelated threat remains.

### Midwinter Arousal Survey

Narrative premise:
A camera records brief activity in the middle of a presumed dormancy season. Researchers need corroboration without repeatedly entering the site.

FULL version:
Usually non-combat. If an external threat interrupts fieldwork, use the same dependency map as above.

REDUCED version:
Keep the entire survey in world state. The key outcome can remain `AROUSAL_OBSERVED` or `UNRESOLVED`; there is no requirement for combat.

### Den-Site Reconstruction After Storm

Narrative premise:
A storm changes the physical entrance to a long-used den site. The question is whether the site remains usable and whether occupants shifted elsewhere.

FULL version:
Dynamic debris, unstable terrain, wildlife withdrawal and rescue routes would require complete movement, environment systems, tactical AI and adapter support.

REDUCED version:
Architecture/Cryosphere/Wayfinding resolves the site revision. Dormancy monitoring records coverage gaps. Any battle occurs later on stable terrain.

## World-state blockers

- `OVERWORLD_DORMANCY_PROFILE_STATE`
- `OVERWORLD_DORMANCY_EPISODE_HISTORY`
- `OVERWORLD_DORMANCY_SITE_IDENTITY`
- `OVERWORLD_TORPOR_AROUSAL_OBSERVATIONS`
- `OVERWORLD_DORMANCY_SURVEY_EFFORT`
- `OVERWORLD_DORMANCY_TIMING_REVISIONS`
- `OVERWORLD_DORMANCY_TO_POPULATION_PROJECTION`
- `OVERWORLD_DORMANCY_TO_COBBLEMON`
- `OVERWORLD_DORMANCY_TO_BATTLE_SNAPSHOT`

## Canon questions

Before promotion, Ouros needs decisions on:

- which species/populations have authored dormancy behavior;
- whether `hibernation`, `torpor`, `aestivation` and related terms are used scientifically in-setting;
- which dormant sites exist before the players arrive;
- which locations are sensitive/restricted;
- how much dormancy timing may shift procedurally;
- how climate and food state can inform but not force revisions;
- whether institutions publish emergence forecasts;
- how wild and partnered Pokémon differ in monitoring/care authority;
- which PTU/Caelo rules, if any, model prolonged noncombat inactivity.

## Guardrail summary

Dormancy is ecological state.

Sleep is a PTU status only when the rules engine says so.

Arousal is an observation, not necessarily the end of a season.

Non-detection is evidence about a survey, not proof of absence.