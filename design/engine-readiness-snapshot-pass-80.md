# Engine Readiness Snapshot — Pass 80

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`846060ee6c2573e80416928275c5176fff5afa05`

Latest visible commit:

`Freeze delayed-hit resource bookkeeping contract`

Parent used by Pass 79:

`fe9cfc5e073f444d5ef3182265f5313b4bb48e51`

AutoPTU Python oracle inspected at:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest Python commit remains Career-oriented and does not change the tactical category map below.

## What the new Java evidence proves

Pass 79 already recorded the delayed-hit execution call-chain contract. The new Java slice freezes resource bookkeeping when a delayed hit matures.

The new contract establishes for the covered path that a matured delayed hit:

- enters target resolution;
- does not spend a new action at maturity;
- does not consume Move frequency again at maturity;
- does not record a second ordinary Move use at maturity;
- still proceeds to attack resolution.

The commit includes a dedicated Java policy, Python exporter/parity fixture and CI gate.

This strengthens evidence for:

- action-economy/resource ownership around delayed Moves;
- one portion of turn/round lifecycle;
- one family of move-specific execution.

It does not prove:

- every delayed Move;
- every invalid-target case at maturity;
- full delayed-hit transcript parity;
- the full Move library;
- the full lifecycle;
- full damage/status resolution;
- terrain/weather/hazards;
- coastal movement, waves, tides, cliffs or erosion;
- AI tactical goals;
- Minecraft playback.

## Java README boundary

The current README still explicitly lists unfinished work for:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the primary anti-overclaim boundary.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

Range, areas, footprints, target anchors and geometric LoS remain verified for the implemented surface.

Pass 80 guardrail:

Geometric LoS does not establish visibility through sea spray, blowing sand, cliff geometry changes, dune elevation, wave crests or atmospheric haze.

### base movement legality

Static Shift/Jump foundations and Overland/Swim/Sky legality remain verified for the implemented surface.

Pass 80 guardrail:

This does not prove wave/current displacement, moving shorelines, unstable cliffs, dune collapse, dynamic water depth, evacuation lanes or crossing a breach while terrain changes.

### core calculations

Core PTU calculation primitives remain verified for the ported surface.

Pass 80 guardrail:

A tile labeled sand, water, ocean or desert does not establish beach/dune geomorphology, coastal erosion or storm-surge mechanics.

### action economy/initiative

VERIFIED.

The new delayed-hit resource contract strengthens resource bookkeeping: a matured delayed hit does not double-spend action/frequency/use bookkeeping on the covered path.

It does not promote full lifecycle or move-specific behavior.

### AI legal-action infrastructure

Deterministic `BattleChoice` legality remains available for supported actions/targets.

It does not prove goals such as EVACUATE, RETREAT_INLAND, HOLD_DUNE_GAP, AVOID_CLIFF, RETRIEVE_OBJECT, CROSS_BREACH or PROTECT_SURVEYOR.

## PARTIAL

### full turn/round lifecycle

Substantial phase, initiative, cleanup, delayed-effect and hook infrastructure exists. The new resource-bookkeeping contract is another bounded parity slice. Full lifecycle and full transcript parity remain unfinished.

### full stateful damage pipeline

Multiple calculation/damage/hook slices exist. The README still declares full resolution unfinished.

Pass 80 guardrail:

No generic wave damage, cliff-fall damage, storm-surge damage, collapsing-dune damage or debris damage exists by implication.

### status lifecycle

Selected status application/phase/expiry behavior has parity evidence. The complete controller remains unfinished.

Pass 80 guardrail:

No generic `soaked`, `buried`, `sandblinded`, `unstable footing`, `swept away` or `exhausted by surf` status is inferred.

### move-specific behavior

Selected Move contracts/behaviors exist. Delayed-hit execution/resource contracts improve one family but do not prove the full Move library.

Pass 80 guardrail:

An exact Move that manipulates water, sand or terrain would need its own verified behavior before a coastal encounter can depend on it.

### abilities

Multiple representative Ability hook families exist with parity evidence. Full Ability coverage is not demonstrated.

Pass 80 guardrail:

`Water Compaction`, Water-type flavor or a Sandygast/Palossand species entry cannot be converted into generic shoreline-control mechanics.

### items

Representative item state/effects exist. Full behavior remains incomplete.

### Trainer Features/perks

Representative Features and hook infrastructure exist. Full Classes/Features/Edges/Orders are not demonstrated.

Pass 80 guardrail:

Groundshaper, Survival, Naturewalk or any coastal/terrain Feature must have exact parity evidence before an encounter relies on it.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

Still BLOCKING as a family.

Pass 80 needs this for any intended mechanic involving:

- wave/current displacement;
- knockback toward a cliff or water edge;
- actors intercepting evacuees at a dune gap;
- moving through a breach while others cross;
- forced relocation from collapsing/advancing terrain;
- dynamic rescue corridors.

Reduced versions should resolve coastal physical change before battle and freeze one safe grid.

### terrain/weather/hazards/zones/reactions

Still BLOCKING as a family.

Pass 80 needs it for future mechanics involving:

- dynamic wet/dry sand zones;
- active overwash;
- storm-surge areas;
- wave or spray zones;
- changing dune geometry;
- cliff-edge hazards;
- moving debris;
- erosion during combat;
- weather phases that alter terrain;
- reactions around unstable terrain or moving water.

Until verified, these remain world state/presentation.

### AI tactical policy

Still BLOCKING.

Legal choices do not imply AI understanding of:

- retreating inland;
- protecting civilians/surveyors;
- avoiding cliff edges;
- choosing a safe crossing window;
- retrieving an object without attacking;
- withdrawing from an overwash zone;
- de-escalating around wild Pokémon using the same coast.

### Minecraft/Cobblemon/Craftics adapter/playback support

Still BLOCKING.

The Java README still states that the core is not yet a Minecraft mod and that the adapter comes after a parity-safe vertical slice.

Minecraft must not become the authority for shoreline position, dune condition, waves, sediment, PTU terrain or damage.

# Pass 80 coastal authority boundary

Available evidence supports only narrow statements:

- Python AutoPTU recognizes semantic terrain/environment strings including ocean/water and sand/desert/dune in selected rule paths;
- exact Features/Moves can consume those labels;
- Java has static movement and geometric targeting foundations;
- Java has a semantic environment state used by selected initiative modifiers;
- Java has substantial initiative/lifecycle infrastructure;
- Java now freezes delayed-hit execution and resource-bookkeeping contracts against Python.

These facts do not establish a generic coastal subsystem.

No verified general subsystem was found for:

- shoreline retreat/advance;
- beach-profile change;
- dune growth/erosion;
- sediment transport;
- overwash;
- barrier breaches;
- cliff retreat;
- wave runup;
- storm surge;
- beach nourishment;
- dune recovery;
- coastal-structure sediment effects;
- coastal ecology -> Cobblemon spawning;
- shoreline -> battle terrain projection.

The primary Caelo material was not reliably retrievable during this run. No Caelo-specific beach/dune/coastal-hazard rule is asserted.

# Pass 80 overworld-specific blockers

These are outside the battle-core category map and remain BLOCKING at the narrative-server/integration level:

- `COASTAL_SYSTEM` persistent state;
- versioned shoreline geometry;
- beach-profile revisions;
- dune-system revisions;
- overwash/breach history;
- cliff-edge/retreat history;
- coarse sediment-budget state;
- coastal restoration/nourishment provenance;
- coastal-access revisions;
- Coastal -> Travel integration;
- Coastal -> Tourism integration;
- Coastal -> Conservation integration;
- Coastal -> Architecture/Public Works integration;
- Coastal -> Cartography/Public Memory integration;
- Coastal -> Cobblemon ecology projection;
- Coastal -> frozen AutoPTU battle projection;
- Minecraft chunk projection from authoritative coastal revisions.

# Pass 80 encounter dependencies

## Dune Breach Evacuation — FULL

Required category state:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED for static surfaces;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if exact PTU statuses are involved;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version can run narratively by completing evacuation/world geometry first, freezing one stable arena and using only ordinary supported combatants/actions.

## Cliff Path Survey — FULL

Primary blockers:

- complete movement/forced movement/interception — BLOCKING;
- terrain/hazards/zones/reactions — BLOCKING;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Targeting and static movement can support a reduced version where the unsafe cliff edge is simply an impassable blocker and all survey/fall logic remains outside battle.

## Storm-Wrack Recovery — FULL

Primary blockers:

- dynamic terrain/water/debris zones — BLOCKING;
- object-oriented tactical goals — AI tactical policy BLOCKING;
- moving-water displacement — complete movement BLOCKING;
- adapter/playback — BLOCKING.

The reduced version handles searching, provenance and custody in world state and uses a static beach battle only if actual combat occurs.

# No-inference rules from Python terrain labels

Python source can recognize labels such as `ocean`, `water`, `river`, `lake`, `desert`, `sand` and `dune` in specific Move/Feature/environment paths.

That does not prove:

- shoreline position;
- wave physics;
- beach morphology;
- wet/dry sand mechanics;
- dunes as elevation/cover;
- coastal erosion;
- sediment transport;
- beach nourishment;
- overwash;
- storm surge;
- cliff-fall rules;
- dynamic tidal depth;
- Java parity for all terrain-sensitive rules.

# Unresolved mechanical/canon questions

- Exact PTU/Caelo rules for Groundshaper, Naturewalk, sand, water, cliffs, falling and environmental hazards.
- Whether Ouros will ever support dynamic coastal terrain during battle or always freeze the coast at battle start.
- Which coastal systems and major historic shoreline changes are authored canon at campaign start.
- How Minecraft chunks rebuild from shoreline/dune revisions without resetting player-built or persistent objects.
- Which structures can move, retreat or be abandoned as the coast changes.
- How coastal physical change affects Cobblemon presence without creating a rare-spawn manipulation exploit.
- How frequently shoreline and dune state advances while chunks are unloaded.
