# Engine Readiness Snapshot — Pass 82

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`3c82018e8f9f123500688d59cc94eba565593231`

Latest visible commit:

`Derive matured delayed-hit combat inputs from runtime state (#116)`

Parent recorded by Pass 81:

`c6b85e619fbc91f21067911987ad056966046b9b`

AutoPTU Python oracle inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its current head remains Career-oriented and does not change the permanent tactical map.

## What the new Java evidence proves

Pass 81 already established that matured combatant delayed hits can re-enter the authoritative attack pipeline without a second action/frequency spend.

The new Java slice strengthens that path by re-deriving combat inputs from the current authoritative `BattleRuntimeState` when a delayed hit matures. For the covered combatant-target path, current move metadata, actor/target stat projections, evasion, accuracy stage, STAB-related effective DB, type effectiveness, damage modifiers and post-result hooks are bound from current runtime state before resolution.

This is important because a delayed attack should not blindly reuse stale combat inputs captured when it was scheduled.

The implementation remains bounded. TILE-target delayed hits and the full delayed-Move family are not thereby proven.

## What Pass 82 must not infer from the new delayed-hit slice

The new evidence does not prove:

- reef structure or underwater geometry;
- current or wave movement;
- underwater visibility;
- heat stress or bleaching;
- coral damage;
- structural fragility;
- restoration objects as battle items;
- objective-aware wild AI;
- escape/withdrawal policy;
- all delayed Moves;
- TILE-target delayed hits;
- all post-damage hooks;
- all Move/Ability/Item/Feature interactions;
- Minecraft/Cobblemon projection.

## Java README boundary

The current AutoPTU-Java README still lists unfinished work for:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic `BattleSpec -> BattleTranscript` parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the primary anti-overclaim boundary.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

VERIFIED for the implemented geometric surface.

Pass 82 guardrail:

Geometric LoS does not prove underwater visibility, turbidity, refraction, depth-related perception, reef concealment or sight through coral structure.

A reef block palette must not alter LoS unless a verified battle snapshot explicitly projects blockers or a supported visibility rule.

### base movement legality

VERIFIED for the implemented static Shift/Jump and Overland/Swim/Sky surface.

Pass 82 guardrail:

This proves a bounded Swim legality foundation, not currents, waves, vertical diving, pressure, buoyancy, squeezing through reef channels, fragile-coral avoidance or passenger transport.

### core calculations

VERIFIED for the ported primitives.

Pass 82 guardrail:

There is no generic `reef bonus`, `coral cover bonus`, `warm-current bonus`, `bleaching penalty`, `rugosity defense`, `sediment accuracy penalty` or `restoration buff` by implication.

### action economy/initiative

VERIFIED for the implemented surface.

The new delayed-hit path preserves the action/frequency boundary established by previous slices and uses current authoritative combat state when the hit matures.

Pass 82 guardrail:

This has no implication for dive timing, current phases, survey objectives, restoration-transfer clocks or reef lifecycle.

### AI legal-action infrastructure

VERIFIED for deterministic supported legal choices.

It does not establish goals such as:

- SURVEY_POINT;
- WITHDRAW_FROM_REEF;
- PROTECT_COHORT;
- AVOID_FRAGILE_ZONE;
- FOLLOW_CURRENT_EDGE;
- SEPARATE_GROUPS;
- HOLD_CHANNEL;
- RETREAT_TO_SHELTER;
- PRESERVE_EVIDENCE.

## PARTIAL

### full turn/round lifecycle

PARTIAL.

Java has substantial typed phases, initiative, cleanup, status/Ability/Feature hooks, delayed-effect storage and covered delayed-hit execution.

Pass 82 adds no new evidence beyond the new delayed-hit state rebinding path.

The category remains incomplete because representative slices do not prove all START/END effects, durations, delayed forms, switching/send-out behavior, reactions and full transcript parity.

### full stateful damage pipeline

PARTIAL.

The new delayed-hit code re-derives more current combat inputs from `BattleRuntimeState` before resolving the covered delayed hit. This strengthens one bounded path.

The README still declares full damage resolution unfinished.

Pass 82 guardrail:

No environmental reef damage, collision damage, heat damage, pressure damage, sharp-coral damage or structural damage exists by implication.

### status lifecycle

PARTIAL.

Selected statuses have application/phase/expiry parity evidence. The full controller remains incomplete.

Pass 82 guardrail:

No `bleached`, `heat-stressed`, `cut-by-coral`, `sediment-blinded`, `decompressed`, `oxygen-low` or similar battle Status may be invented from reef state.

### move-specific behavior

PARTIAL.

Selected Move contracts exist. Delayed combatant-target resolution is increasingly authoritative, but the library remains incomplete.

Pass 82 guardrail:

Dive, Whirlpool, Surf, Aqua Ring, Brine or any other aquatic Move requires exact current behavior evidence before an encounter depends on it.

### abilities

PARTIAL.

Multiple representative hooks have parity evidence. Full coverage is not demonstrated.

Pass 82 guardrail:

Toxapex behavior, Water-type flavor, Merciless, Regenerator or any other Ability cannot be transformed into reef ecology, territorial AI, restoration behavior or environmental resistance without an exact rule and implementation.

### items

PARTIAL.

Representative held-item state/effects exist; complete behavior does not.

Pass 82 guardrail:

Dive equipment, restoration containers, tags, cameras, coral frames, scientific instruments and visitor gear are world-state assets unless an actual PTU Item definition is validated.

### Trainer Features/perks

PARTIAL.

Representative Features and hook infrastructure exist, including terrain-linked Python-oracle evidence for specific Features. Full classes/Features/Edges/Orders do not.

Pass 82 guardrail:

Wilderness Guide's exact `ocean/wetlands` behavior cannot be generalized into a passive reef buff. Survival, Researcher, Chronicler or similar concepts cannot grant reef survey bonuses unless exact PTU/Caelo and Java contracts support them.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

BLOCKING as a family.

Pass 82 FULL encounters need this when they intend to model:

- currents moving combatants;
- wave displacement;
- interception in narrow reef channels;
- escorts through chokepoints;
- forced movement away from fragile/restoration zones;
- physical separation of fighting wild groups;
- moving noncombatants or restoration cargo.

Reduced versions must freeze reef geometry and keep currents/escorts outside the grid.

### terrain/weather/hazards/zones/reactions

BLOCKING as a family.

Pass 82 would need this for:

- current boundaries as tactical zones;
- wave/exposure phases;
- fragile reef areas;
- rubble hazards;
- sediment/turbidity zones;
- heat-stress battle phases;
- underwater environmental hazards;
- reactions to entering or damaging sensitive areas;
- changing water/weather conditions.

Until this family is verified, reef condition remains world state/presentation only.

### AI tactical policy

BLOCKING.

Legal actions do not establish AI understanding of:

- territorial defense;
- withdrawal;
- separation rather than KO;
- defending a channel;
- avoiding restoration equipment;
- protecting young;
- observing rather than attacking;
- escaping through a reef route;
- preserving a noncombat objective.

### Minecraft/Cobblemon/Craftics adapter/playback support

BLOCKING.

The adapter does not yet have a parity-safe contract for projecting a versioned reef into an authoritative battle snapshot and rendering semantic events back into Minecraft.

Minecraft must not calculate:

- reef PTU Terrain;
- underwater movement legality;
- currents;
- cover;
- heat/bleaching effects;
- restoration success;
- capture legality;
- species bonuses;
- tactical damage.

# Pass 82 reef-specific evidence boundary

Available evidence supports these narrow statements:

- Narrative Maritime already recognizes reef as a generic marine-habitat/location category.
- Python AutoPTU has explicit `can_swim()` and selected `ocean/wetlands` terrain-linked Feature behavior.
- Java has static Swim legality within its base movement surface.
- Java has strong geometric targeting and action-economy/initiative foundations.
- Java has an increasingly authoritative delayed-hit path for covered combatant targets.
- Java's README still marks the larger terrain/hazard/forced-movement/registry/AI/adapter families incomplete.

These facts do not establish a reef battle subsystem.

No verified general subsystem was found for:

- coral structure/condition;
- reef complexity/rugosity;
- bleaching;
- coral disease;
- reef recruitment;
- reef restoration;
- coral nurseries/outplants;
- fragile coral;
- reef-specific cover;
- currents/waves as forced movement;
- turbidity/underwater visibility;
- reef ecology -> Cobblemon spawning;
- reef state -> battle projection.

The primary Caelo material was not reliably retrievable during this run. No Caelo-specific reef rule is asserted.

# Pass 82 overworld-specific blockers

These are outside the permanent battle-core category map and remain BLOCKING at the narrative-server/integration level:

- persistent `REEF_SYSTEM` state;
- internal reef-zone registry;
- versioned structural revisions;
- condition-observation provenance;
- bleaching/stress observation history;
- recruitment history;
- disturbance-event graph;
- restoration-project lifecycle;
- restoration cohort provenance;
- reef complexity/structural monitoring;
- Reef -> Water Quality linkage;
- Reef -> Meteorology/ocean-heat linkage;
- Reef -> Fisheries linkage;
- Reef -> Tourism linkage;
- Reef -> Conservation linkage;
- Reef -> Cobblemon population projection;
- Reef -> Minecraft physical revision projection;
- Reef -> authoritative AutoPTU battle snapshot.

# Encounter readiness

## Broken Crest Survey

FULL requires:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/forced movement/interception: BLOCKING when current/displacement matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full lifecycle: PARTIAL
- full stateful damage: PARTIAL
- statuses: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

REDUCED is viable once a static battle can be opened from narrative world state: freeze one reef geometry revision, represent only static blockers, keep survey points/current/fragility outside battle and use a conventional legal encounter.

## Nursery Transfer Interruption

FULL is BLOCKING primarily on complete movement/interception, terrain/hazards if environment matters, tactical AI and adapter/playback.

REDUCED keeps cohort/staff off-grid and resolves a single static chokepoint battle. Restoration provenance and transfer outcome remain narrative-server state.

## Warm-Current Boundary

FULL is BLOCKING on current-as-zone behavior, objective-aware multi-group AI, non-KO goals and adapter support.

REDUCED keeps the current boundary and ecological relationship outside battle. A conventional static battle may occur with no invented reef/current/territorial modifier.

# Live capability map after Pass 82

VERIFIED:

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted by Pass 82.

# Unresolved mechanical questions

- Exact PTU/Caelo underwater movement and breathing rules.
- Exact interaction of Swim/Gilled/Dive and underwater encounters.
- Whether Caelo modifies water/reef travel or visibility.
- Exact rules, if any, for current-driven movement.
- Exact environmental hazard rules for underwater combat.
- Capture/retreat semantics while swimming.
- Which aquatic Moves/Abilities/Features already have Java parity.
- Whether a future battle snapshot should flatten reef height into static blockers or support discrete underwater elevation/depth bands.
- How Minecraft should render a reef revision without inferring tactical properties from blocks.

# Unresolved canon questions

- Which reef systems exist in Ouros before player arrival.
- Which species are historically associated with each reef.
- Which disturbances and restoration projects predate the campaign.
- Which institutions own monitoring/restoration responsibility.
- How tourism, fishing and protected access are governed.
- What technology is used for reef monitoring and restoration.
- Which coordinates/data are sensitive in multiplayer.
- How quickly reef structural and biological state advances while chunks are unloaded.
