# Engine Readiness Snapshot — Pass 96

Status: Implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Evidence inspected

AutoPTU-Java live head inspected:
`66d82a5beb767ec8dd32803b5d08afaad3d454aa`

Latest relevant Java change:
`Expire Follow Me and Foresight during ROUND_START (#132)`

Observed behavior in that slice:

- Java now has reusable round-scoped temporary-effect expiry logic;
- Follow Me and Foresight entries carrying `until_round` can expire during `ROUND_START`;
- expiry is ordered after delayed-hit maturity in the default lifecycle registry;
- removal behavior intentionally mirrors Python's first-live-occurrence semantics;
- malformed or absent expiry payloads are preserved rather than guessed;
- Python fixtures and a dedicated parity gate freeze this representative behavior.

Source:
https://github.com/Teffa14/AutoPTU-Java/commit/66d82a5beb767ec8dd32803b5d08afaad3d454aa

The immediately preceding Java slice also executes position-only delayed targets through authoritative geometry.

Java README still states that the port is incomplete and explicitly leaves full battle-state expansion, full damage, status controller, terrain/hazards/forced movement/reactions, complete hook registries, full transcript parity, tactical AI and Minecraft/Cobblemon adapter work unfinished.

Source:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

AutoPTU Python live head inspected:
`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its recent commits remain Career-oriented and do not justify changing the tactical capability map.

Available Python evidence includes exact Sleep blockers such as Insomnia and Vital Spirit. Those are battle rules, not proof of a persistent sleep/rest or diel-activity subsystem.

The full primary Caelo corpus was not reliably retrievable during this pass. No Caelo-specific time-of-day modifier is asserted.

## Permanent capability categories

### VERIFIED

#### targeting / footprints / range / LoS

Static geometry, range, footprints and geometric LoS remain verified at the established project level.

Recent delayed-target slices add stronger evidence for authoritative geometry re-evaluation.

Pass 96 non-inference:
A nocturnal observation, roost location, dark refuge or dawn activity window does not change LoS by itself.

#### base movement legality

Established Shift/Jump and Overland/Swim/Sky movement legality remains verified.

Pass 96 non-inference:
A population being active at dusk does not grant extra movement, free Shift, pursuit, retreat or crossing rules.

#### core calculations

Established PTU calculation primitives remain verified.

#### action economy / initiative

Established action economy and initiative remain verified.

Pass 96 non-inference:
Early morning, dusk, night activity or an internal biological clock does not change initiative unless an exact PTU rule says so.

#### AI legal-action infrastructure

Deterministic legal-choice generation remains verified.

This does not prove AI goals such as leaving a roost, returning to a refuge, avoiding a market, crossing before sunrise or protecting a rest site.

### PARTIAL

#### full turn / round lifecycle

Lifecycle ownership now has representative evidence for phase progression, initiative, field progression, delayed-hit maturity and selected round-scoped temporary-effect expiry.

The latest slice strengthens ROUND_START cleanup for Follow Me/Foresight.

Still partial because representative expiry does not prove every START/END trigger, duration family, delayed Move, Status, Ability, Feature, reaction or transcript interaction.

Important Pass 96 distinction:
`round lifecycle` is battle time. It does not implement world clock, circadian cycles, sleep schedules or dawn/dusk ecology.

#### full stateful damage pipeline

Representative delayed-hit paths can re-enter authoritative resolution.

Still partial because the README explicitly leaves full damage unfinished.

Pass 96 introduces no time-of-day damage modifier.

#### status lifecycle

Representative status application/phase/cleanup behavior exists.

Still partial because the complete controller is unfinished.

Narrative rest or roosting cannot apply Sleep. Insomnia/Vital Spirit remain exact Ability interactions with the Sleep status, not ecological classifiers.

#### move-specific behavior

Delayed-hit and several other representative Move behaviors have parity contracts.

Still partial because the complete PTU Move library is not ported.

No Move is assumed to gain power or legality because it is dawn, dusk or night.

#### abilities

Representative Ability hooks exist with parity tests.

Still partial because the full registry is incomplete.

Pass 96 specifically does not infer:

- Insomnia = never rests;
- Vital Spirit = diurnal;
- Early Bird = dawn-active;
- Illuminate = attracts wildlife in world state;
- Keen Eye = improved nighttime ecology/perception;
- Run Away = autonomous withdrawal AI.

#### items

Representative held-item behavior exists.

Still partial because coverage remains incomplete.

#### Trainer Features / perks

Representative Feature infrastructure and multiple concrete Features exist.

Still partial because broad coverage and reaction/interrupt families remain incomplete.

Any Feature affecting rest, tracking, observation, night travel or encounter availability must be verified individually.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Still blocking as a complete family.

Pass 96 implications:

- a roosting group cannot dynamically withdraw through a protected lane;
- civilians cannot be safely routed around moving wildlife using verified interception rules;
- aerial groups cannot cross a live 3D tactical corridor;
- fleeing actors cannot rely on complete pursuit/disengagement semantics.

#### terrain / weather / hazards / zones / reactions

Still blocking as a complete family.

Canonical field-state primitives and representative round progression exist, but the README still lists terrain/hazards/reactions as unfinished.

Pass 96 does not infer:

- night = Darkness Terrain;
- dawn = field effect;
- roost = protection zone;
- rest site = healing zone;
- dusk = Accuracy modifier;
- nocturnal species = night buff;
- daytime species = night penalty;
- artificial light = tactical hazard;
- quiet hours = Silence/Sonic restriction.

#### AI tactical policy

Still blocking.

No current evidence proves reliable AI for:

- WITHDRAW_TO_ROOST;
- LEAVE_AT_DAWN;
- RETURN_AT_DUSK;
- PROTECT_ROOST;
- AVOID_CIVILIANS;
- CROSS_TEMPORAL_WINDOW;
- FOLLOW_COLLECTIVE_ACTIVITY;
- NONLETHAL_DISENGAGE.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still blocking.

No verified adapter contract currently turns:

- persistent diel profiles;
- activity-window revisions;
- sampling effort;
- rest/roost-site use;
- local activity shifts;
- temporal-niche overlap;
- time-dependent population projection

into authoritative battle state and semantic playback without duplicating PTU rules.

## Pass 96 specific blockers

`OVERWORLD_DIEL_PROFILE_STATE`
Versioned species/population/collective/individual activity profiles scoped by location and season.

`OVERWORLD_ACTIVITY_OBSERVATION_LEDGER`
Timestamped detections and non-detections with method, sampling duration and provenance.

`OVERWORLD_SAMPLING_EFFORT`
Coverage state required before interpreting apparent day/night absence.

`OVERWORLD_REST_ROOST_STATE`
Persistent rest/refuge locations and use histories without inferring PTU Sleep.

`OVERWORLD_ACTIVITY_SHIFT_CASES`
Evidence-backed revisions when timing changes.

`OVERWORLD_TEMPORAL_NICHE_OVERLAP`
Coarse population overlap estimates separated from battle hostility.

`OVERWORLD_DIEL_TO_COBBLEMON`
Bounded projection of likely active populations without allowing time-skip rare-spawn farming.

`OVERWORLD_DIEL_TO_BATTLE`
A frozen encounter snapshot that only maps time-dependent mechanics explicitly supported by PTU/Caelo and Java.

## Encounter dependency summary

### Dawn Roost Survey — FULL

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
- complete movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version is viable earlier by resolving roost departure before combat and opening a static arena only for actual combatants.

### Evening Flight Window — FULL

VERIFIED:
- static targeting/range/LoS;
- current base movement legality;
- core calculations;
- action economy/initiative;
- legal-action generation.

PARTIAL:
- lifecycle;
- damage;
- status/move/ability/item/Feature behavior.

BLOCKING:
- complete/vertical movement semantics;
- environmental zones/reactions;
- tactical AI;
- adapter/playback.

Reduced version is viable as overworld observation plus an independent static battle.

### Night Market Wildlife Shift — FULL

VERIFIED:
- targeting/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- legal-action infrastructure.

PARTIAL:
- lifecycle;
- damage;
- status/move/ability/item/Feature families.

BLOCKING:
- complete movement/interception;
- zones/reactions;
- tactical AI for withdrawal/protection;
- civilian/Minecraft playback.

Reduced version is viable by clearing civilians and uninvolved wildlife before AutoPTU starts.

## Current capability map

VERIFIED:
- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

BLOCKING:
- complete movement including push / pull / knockback / interception / forced movement;
- terrain / weather / hazards / zones / reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter and playback.

## Pass 96 rule boundary

World clock and diel ecology belong outside the battle core until a battle starts.

When a battle does start, the adapter may pass only explicit, validated mechanical state. It must not translate `night`, `dawn`, `resting`, `nocturnal`, `roost` or `activity peak` into PTU effects on its own.

A single parity-tested temporary-effect expiry does not prove complete lifecycle. A single Sleep blocker does not prove ecological sleep. A known species behavior does not prove a mechanical Ability.

That boundary allows the Ouros world to become temporally alive now without forcing Minecraft to recreate missing PTU rules.