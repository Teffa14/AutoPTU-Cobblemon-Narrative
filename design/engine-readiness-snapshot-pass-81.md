# Engine Readiness Snapshot — Pass 81

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`c6b85e619fbc91f21067911987ad056966046b9b`

Latest visible commit:

`Execute matured combatant delayed hits without double-spending resources`

Parent recorded by Pass 80:

`846060ee6c2573e80416928275c5176fff5afa05`

AutoPTU Python oracle inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The current Python head remains Career-oriented and does not change the permanent tactical map below.

## What the new Java evidence proves

The new Java slice advances delayed-hit execution beyond bookkeeping-only evidence.

For the covered combatant-target delayed-hit path, a matured hit now re-enters the same authoritative accuracy, damage, RNG, post-damage-hook, HP, damage-history and semantic event pipeline used by an ordinary Move while avoiding a second action/frequency spend.

The implementation explicitly keeps TILE-target delayed-hit expansion for later work.

This strengthens evidence for:

- one bounded portion of full turn/round lifecycle;
- one bounded family of move-specific behavior;
- one bounded path through the stateful damage pipeline;
- action-economy bookkeeping around delayed effects.

It does not prove:

- all delayed Moves;
- TILE-target delayed hits;
- invalid/departed targets in every case;
- full delayed-effect lifecycle;
- full BattleTranscript parity;
- the full Move library;
- terrain/weather/hazards;
- magnetic fields or interference;
- AI tactics;
- Minecraft playback.

## Java README boundary

The current README still explicitly lists unfinished work for:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the primary anti-overclaim boundary.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

Range, areas, footprints, target anchors and geometric LoS remain verified for the implemented surface.

Pass 81 guardrail:

Geometric LoS does not establish magnetic sensing, compass direction, electromagnetic detection, radio propagation or visibility of aurora.

### base movement legality

Static Shift/Jump foundations and Overland/Swim/Sky legality remain verified for the implemented surface.

Pass 81 guardrail:

This does not prove magnetic attraction/repulsion, metal-object movement, environmental Magnet Pull, levitation through magnetic fields or navigation by compass.

### core calculations

Core PTU tables/calculation primitives remain verified for the ported surface.

Pass 81 guardrail:

No generic magnetic-field modifier exists by implication. A numeric field intensity must not become Accuracy, Speed, Damage, Evasion or movement cost without an exact PTU rule.

### action economy/initiative

VERIFIED.

The new delayed-hit execution path preserves the already-verified resource-bookkeeping boundary for the covered case and executes the delayed hit without a second action/frequency spend.

### AI legal-action infrastructure

Deterministic `BattleChoice` legality remains available for supported actions/targets.

It does not establish AI goals such as INSPECT_SENSOR, PROTECT_RELAY, RETREAT_FROM_INTERFERENCE, REACH_CALIBRATION_POINT, AVOID_DEVICE or FOLLOW_ROUTE.

## PARTIAL

### full turn/round lifecycle

Substantial phase, initiative, cleanup, delayed-effect and hook infrastructure exists. Pass 81 adds actual matured combatant delayed-hit execution through the standard attack pipeline.

Full lifecycle remains incomplete because representative parity slices do not prove all START/END effects, durations, delayed forms, reactions, switch/send-out interactions or complete transcript parity.

### full stateful damage pipeline

Multiple calculation/damage/hook slices exist. Pass 81 confirms another bounded path through authoritative damage application for combatant delayed hits.

The README still declares full resolution unfinished.

Pass 81 guardrail:

No electromagnetic damage, induced-current damage, device shock, metal-projectile damage or aurora damage exists by implication.

### status lifecycle

Selected status application/phase/expiry behavior has parity evidence. The complete controller remains unfinished.

Pass 81 guardrail:

No `magnetized`, `jammed`, `disoriented`, `compass-confused`, `EMP`, `radio-silenced` or similar status is inferred.

### move-specific behavior

Selected Move contracts/behaviors exist. Delayed-hit execution is now stronger for combatant targets but does not prove the Move library.

Pass 81 guardrail:

Magnet Bomb, Magnet Rise, Magnetic Flux or any other magnetic Move needs exact parity evidence before a narrative encounter can rely on its behavior.

### abilities

Multiple representative Ability hooks exist with parity evidence. Full Ability coverage is not demonstrated.

Available Python-oracle evidence shows a concrete `magnet_pull` temporary-effect path that can constrain movement relative to a source. That demonstrates one specific mechanic in Python, not Java parity and not generic environmental magnetism.

Pass 81 guardrail:

Magnet Pull must never be projected from a location, species flavor or nearby magnetic field unless exact Java parity exists for the chosen mechanic.

### items

Representative item state/effects exist. Full behavior remains incomplete.

Pass 81 guardrail:

Compass, magnetometer, radio, navigation device or shielding gear has no PTU item behavior unless separately authored/validated.

### Trainer Features/perks

Representative Features and hook infrastructure exist. Full Classes/Features/Edges/Orders are not demonstrated.

Pass 81 guardrail:

Technology Education, Survival or another Feature/Skill cannot grant magnetic-navigation or interference rules until exact PTU/Caelo text and runtime behavior are validated.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

Still BLOCKING as a family.

Pass 81 needs this if a future encounter intends to model:

- magnetic pull/repulsion as actual displacement;
- Steel actors being held relative to a source;
- metal objects moving through a battlefield;
- forced relocation near a magnetic device;
- interception while protecting a calibration route.

Reduced versions must keep magnetic world state outside tactical movement unless an exact supported PTU effect exists.

### terrain/weather/hazards/zones/reactions

Still BLOCKING as a family.

Pass 81 would need this for any intended mechanic involving:

- magnetic zones;
- electromagnetic interference zones;
- aurora/geomagnetic battle phases;
- device-disruption areas;
- reactions to entering/leaving a field;
- environment-triggered Magnet Pull;
- field-dependent evolution during battle.

Until verified, all such concepts remain world state/presentation only.

### AI tactical policy

Still BLOCKING.

Legal choices do not imply AI understanding of:

- protecting an observatory;
- choosing a calibration target;
- retreating from sensitive equipment;
- disabling a relay without attacking people/Pokémon;
- following an evacuation/navigation route;
- preserving evidence;
- withdrawing rather than fighting.

### Minecraft/Cobblemon/Craftics adapter/playback support

Still BLOCKING.

Minecraft must not calculate PTU magnetism, compass modifiers, device failure, movement restriction, evolution eligibility or damage.

The future adapter may render server-authoritative compass/aurora/instrument state and translate a verified battle snapshot.

# Pass 81 geomagnetic authority boundary

Available evidence supports only narrow statements:

- Python AutoPTU has a concrete `magnet_pull` temporary-effect path affecting Shift validation;
- Python recognizes specific magnetic Moves/Abilities elsewhere in its rules surface, but coverage is not established here;
- Java has strong geometric targeting and static movement foundations;
- Java has substantial initiative/lifecycle infrastructure;
- Java now executes matured combatant delayed hits through the standard authoritative attack pipeline without double spending resources;
- Java's README still marks the larger environment/registry/AI/adapter families incomplete.

These facts do not establish a generic geomagnetism subsystem.

No verified general subsystem was found for:

- magnetic-field maps;
- magnetic declination/navigation;
- compass drift;
- magnetic observatories;
- geomagnetic storms;
- aurora;
- electromagnetic interference;
- device disruption by magnetic Pokémon;
- environmental magnetic pull;
- metal-object displacement;
- magnetic-field evolution;
- magnetic ecology;
- geomagnetism -> Cobblemon spawning;
- geomagnetism -> battle projection.

The primary Caelo material was not reliably retrievable during this run. No Caelo-specific magnetic-field rule is asserted.

# Pass 81 overworld-specific blockers

These are outside the battle-core category map and remain BLOCKING at the narrative-server/integration level:

- `MAGNETIC_REGION` persistent state;
- versioned `MAGNETIC_FIELD_REVISION` state;
- magnetic observatory/instrument state;
- observation provenance and quality control;
- magnetic-anomaly graph;
- cause-hypothesis graph;
- magnetic-navigation profiles and historical corrections;
- electromagnetic-interference incidents;
- geomagnetic-event history;
- aurora observations;
- Pokémon magnetic-behavior observations;
- Geomagnetism -> Cartography/Travel integration;
- Geomagnetism -> Technology/Communications integration;
- Geomagnetism -> Astronomy integration;
- Geomagnetism -> Cobblemon projection;
- Geomagnetism -> Battle snapshot contract.

# Encounter readiness

## Observatory Calibration Failure

FULL version:

BLOCKED by complete movement if magnetic displacement/escort is used, terrain/weather/hazards/zones/reactions for any actual field zone, tactical AI for protect/inspect goals and Minecraft playback. Selected Move/Ability/Item/Feature dependencies remain individually PARTIAL until exact parity evidence exists.

REDUCED version:

Runnable conceptually with world-state investigation plus a static conventional battle. No magnetic battle mechanic required.

## Compass Pass

FULL version:

BLOCKED for dynamic route goals, complete movement/interception, tactical AI and adapter playback. Magnetic navigation itself belongs to overworld authority.

REDUCED version:

Resolve navigation before battle, then freeze static geometry.

## Aurora Relay Night

FULL version:

BLOCKED for interactable tactical service goals and tactical AI if battle overlaps relay operation. The aurora does not need a PTU mechanic.

REDUCED version:

World-state relay/communications incident plus optional standard battle.

# Exact non-inferences from Python evidence

The Python `magnet_pull` Shift validation can restrict movement relative to a source under its own temporary-effect contract.

It does not prove:

- every Magnet Pull rule branch;
- Java parity;
- environmental magnetism;
- compass behavior;
- magnetic evolution;
- device interference;
- metal-object physics;
- magnetic zones;
- geomagnetic storms.

# Next mechanical questions

Before tactical promotion, extract/validate the exact PTU/Caelo definitions and runtime coverage for Magnet Pull, Magnet Rise, Magnetic Flux, Magnet Bomb, relevant Pokémon capabilities and any special magnetic-field evolution rule.

Before overworld promotion, define whether Ouros has global magnetic-field revisions, local anomaly zones, observatories, magnetic-navigation products and any authored Pokémon/infrastructure relationships.