# Engine Readiness Snapshot — Pass 56

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

`Teffa14/AutoPTU-Java` read-only head:

`339c0a876fa3b4b3da0e410bb8aabd83cc74a405`

`Teffa14/AutoPTU` read-only head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The narrative repository remains the only writable destination.

## Java change since Pass 55

Pass 55 inspected Java at:

`752603a002a31c8d73078ef238f22d2b39ccb024`

Current head:

`339c0a876fa3b4b3da0e410bb8aabd83cc74a405`

Newest change:

`Freeze Analytic initiative/action parity contract`

Observed evidence:

- Java now has a parity-safe `AnalyticResolution` contract;
- the contract determines whether the defender has acted from action history and initiative cursor state;
- selected Analytic post-result damage behavior is frozen against the pinned Python oracle;
- CI now exports and checks Analytic fixtures;
- the contract keeps the eligibility decision inside server-owned battle state rather than Minecraft/Cobblemon presentation.

This strengthens evidence for:

- abilities;
- action economy/initiative integration;
- full stateful damage pipeline.

It does not prove any of those broad families complete.

## Java README boundary

Current AutoPTU-Java README still states that Python AutoPTU remains authoritative while the port is incomplete.

It continues to list unfinished work including:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

One implemented Ability contract is therefore evidence for one slice, not the Ability catalogue.

## Health/disease implementation search

Repository search over current `Teffa14/AutoPTU-Java` and `Teffa14/AutoPTU` found no direct hits under the terms:

- `Pokerus`;
- `Pokérus`;
- `illness`;
- `disease`;
- `infection`;
- `quarantine`;
- `contagion`.

This is not proof that no related behavior exists under different terminology.

It is sufficient evidence to reject any assumption that a generic outbreak/infection subsystem is currently available.

Available Python evidence does show explicit tactical statuses and hazards, including Poison and Toxic Spikes. Those do not establish disease transmission, diagnosis, quarantine, immunity or epidemiological state.

## PTU/Caelo source availability boundary

A complete searchable PTU/Caelo source corpus was not reliably retrievable during this run.

Pass 56 therefore does not declare any exact rule for:

- illness;
- infection;
- Medicine Education diagnosis;
- quarantine/isolation;
- immunity;
- disease treatment;
- Pokérus;
- environmental exposure;
- transmission between Pokémon or Trainers.

Those require source extraction before mechanical implementation.

## Permanent capability map

### VERIFIED

Targeting / footprints / range / LoS.

Base movement legality.

Core calculations.

Action economy / initiative.

AI legal-action infrastructure.

### PARTIAL

Full turn / round lifecycle.

Full stateful damage pipeline.

Status lifecycle.

Move-specific behavior.

Abilities.

Items.

Trainer Features / perks.

### BLOCKING

Complete movement including push / pull / knockback / interception / forced movement.

Terrain / weather / hazards / zones / broad reactions.

AI tactical policy.

Minecraft / Cobblemon / Craftics adapter and playback.

## Pass 56 health-specific blockers

The following are separate from the permanent tactical categories and remain BLOCKING until explicit contracts exist:

### Persistent health-condition contract — BLOCKING

No verified contract currently proves a non-battle health condition can persist on an individual Pokémon across overworld/battle transitions while remaining distinct from battle statuses.

### Exposure/transmission contract — BLOCKING

No verified contract currently resolves exposure, transmission, infectious period, immunity or recovery between persistent actors.

### Clinical diagnosis/treatment authority — BLOCKING

No verified AutoPTU-Java contract currently owns diagnosis, disease treatment or recovery for an outbreak-specific condition.

### Overworld health surveillance integration — BLOCKING

No end-to-end contract currently proves:

1. Cobblemon/world state emits a health observation;
2. server authority creates a privacy-safe signal;
3. an outbreak investigation references the signal;
4. a care or scientific subsystem validates diagnosis/evidence;
5. battle state receives only exact supported mechanical consequences;
6. semantic results write back without Minecraft inventing disease state.

### Aggregate wildlife health advancement — BLOCKING

No verified system advances health state for unloaded wild populations without spawning/simulating each individual.

## Narrative-side systems feasible now

The following do not require an implemented disease mechanic:

- health signals;
- baseline records;
- surveillance case definitions;
- outbreak investigation state;
- exposure-opportunity graphs;
- hypothesis revision;
- privacy/redaction;
- public notices;
- clinic-capacity consequences;
- route/service changes;
- research sampling records;
- false-alarm outcomes;
- multi-cause cluster outcomes;
- after-action reviews;
- historical outbreak archives.

These should remain world-state objects until mechanics are validated.

## Encounter readiness — Trail Clinic Supply Run

### REDUCED

Logistics and cargo stay outside battle. A conflict uses a static legal encounter.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- AI legal-action infrastructure — VERIFIED;
- full lifecycle — PARTIAL only where selected legal mechanics require it;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL.

No outbreak-specific mechanical condition is required.

### FULL

Medical cargo and retreat access become tactical objectives in a changing route.

Additional dependencies:

- complete movement/interception/forced movement — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING if the route changes mechanically;
- full lifecycle — PARTIAL;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

## Encounter readiness — Wildlife Sampling Perimeter

### REDUCED

Sampling and animal-health observation occur outside battle. If defensive combat occurs, use a static grid and ordinary battle resolution.

No battle result may automatically classify the sampled Pokémon as infected or uninfected.

### FULL

Wild actors can retreat through explicit routes while participants maintain a safe observation perimeter.

Primary blockers:

- complete movement/interception — BLOCKING;
- terrain/zones/reactions — BLOCKING;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

If the full version later includes mechanical illness effects, the persistent health-condition and clinical authority blockers must also be resolved.

## Encounter readiness — Treatment Plant Access

### REDUCED

Contamination, sampling, workers and machinery remain world state. A battle occurs only on a static safe area.

### FULL

Facility zones and active machinery modify tactical choices.

Primary blockers:

- terrain/hazards/zones/reactions — BLOCKING;
- complete movement — BLOCKING if flows/machinery move actors;
- lifecycle — PARTIAL for timed transitions;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Environmental exposure cannot apply Poison or another status unless the governing rules and Java contract explicitly support that exact effect.

## Analytic no-inference rule

The new Analytic contract does not promote `abilities` to VERIFIED.

It proves a selected Ability eligibility/damage slice that depends on initiative/action history.

It does not prove:

- all Ability timing windows;
- all post-damage Ability behavior;
- all initiative-dependent Abilities;
- Ability suppression;
- Ability interactions with disease/health state;
- the complete damage pipeline.

## Outbreak no-inference rules

A Poison implementation does not prove disease.

A Toxic Spikes implementation does not prove environmental contamination.

A status lifecycle does not prove infection lifecycle.

A Pokémon Center narrative visit does not prove a healing contract.

A care case does not prove a transmissible condition.

An exposure graph does not prove contagion.

A health investigation does not create battle modifiers.

A Minecraft particle, skin or animation does not create sickness.

A wild Pokémon despawning does not prove recovery, death or migration.

## Unresolved implementation questions

- Does the governing PTU/Caelo ruleset define diseases outside standard combat statuses?
- Does it define Pokérus at all?
- Which Medicine Education/medical rules can diagnose conditions rather than only treat injuries/statuses?
- What object should own persistent non-battle health state?
- How does that state cross battle boundaries?
- Can an outbreak condition legally alter battle stats/statuses, and if so through what exact rule?
- How should privacy-sensitive health data be stored in multiplayer?
- How can wild-population health be advanced without simulating every individual?
- How will environmental samples relate to clinical cases without automatic causal inference?
- Which institution authorizes isolation, quarantine, transfer pauses or closures in Ouros canon?
- How does the adapter show observable illness without becoming rules authority?

Until those questions have authoritative answers, Pass 56 encounters should use reduced versions whenever a concept would otherwise require active illness, contagion, quarantine mechanics or environmental disease effects.