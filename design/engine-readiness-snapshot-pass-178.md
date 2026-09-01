# Engine Readiness Snapshot — Pass 178

Status: READ-ONLY EVIDENCE SNAPSHOT
Date: 2026-09-01

Purpose: freeze live implementation evidence used by the ecological phenology/migration concepts in pass 178. No write was made to AutoPTU-Java, AutoPTU or AutoPTU-Cobblemon-RPG.

## AutoPTU-Java

Inspected head: `8fd11090b31d413072808662c01fc2e2316420ff`.

Newest relevant commit: `Compose content-backed forced movement prevention (#314)`.

Observed evidence:
- forced-movement prevention can compose declaratively from Trainer Feature + capability requirements;
- post-hit displacement consults this content-backed prevention path;
- candidate-step constraints and Shadow Tag displacement had already been added and tested in the immediately preceding slices;
- Python-oracle parity coverage exists for those representative branches.

What this proves:
- meaningful post-hit forced-movement infrastructure exists;
- several prevention and candidate-step semantics are tested;
- forced displacement is integrated more deeply than in earlier snapshots.

What this does not prove:
- the complete movement family;
- all Push/Pull/Knockback semantics;
- all interception behavior;
- all collision/partial-stop behavior;
- arbitrary moving-objective/escort semantics;
- terrain/hazard/reaction integration;
- complete Trainer Feature coverage.

Pass 178 therefore keeps `complete movement including push/pull/knockback/interception/forced movement` at PARTIAL.

## AutoPTU Python

Inspected recent head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

The newest visible commits are Career/presentation and roster-recovery work. No new tactical authority evidence in this run changes the permanent capability classification.

The Python repository remains the read-only oracle/reference source where applicable; this narrative task did not modify it.

## AutoPTU-Cobblemon-RPG adapter

Recent inspected evidence:
- `40ef2d4af9100d5ce5a1dbc8308a350482cffff2` provisions a persistent canonical Cedar field-notes quest object in the normal Overworld and gates progress to that exact server-owned physical object;
- `077167dbfc96b69a48a217f343f3a57aeda1b347` adds authoritative graphical in-world RPG scene capture and CI evidence;
- prior Marea work establishes fixed physical sites, server-owned NPC identities and safe companion projection boundaries.

Narrative implication:
- non-combat ecological observation quests can reasonably target physical field-note objects, boards, observation posts and visible world actors;
- a phenology ledger or first-arrival board is adapter-feasible as world-state/UI work;
- Cobblemon entity counts, spawn/despawn and AI still cannot become ecological authority;
- complete tactical battle playback remains unverified as a family.

## Permanent capability categories

### VERIFIED for current covered contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` means current audited contracts in the category are real. It does not mean every future combination is covered.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING as complete families when required by a design

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

The adapter has narrower verified world/presentation surfaces. It remains BLOCKING when a concept requires complete battle playback rather than ordinary physical quest/world projection.

## Pass 178 low-risk concepts

The following proposals require no BattleSpec and are narratively/architecturally ready:
- `Three Mornings at Mirador`;
- `The Crossing Window` reduced observation form;
- `The Missing Stopover`;
- `Ferry Noise, Fewer Sightings`;
- `The False Outbreak`;
- `First Arrival Board`;
- `Old Year, New Route`;
- `Marea Phenology Ledger`.

`One Pokémon Behind the Window` is also possible as non-combat observation/care workflow, but any exact health/status determination must remain inside existing PTU/care boundaries.

## Pass 178 mechanically rich concept

`Corridor Under Pressure` full version requires:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected combatants require it;
- terrain/weather/hazards/zones/reactions;
- exact move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Full-version status: BLOCKED.

Reason:
Representative forced-movement progress does not provide the full corridor/escort/moving-objective semantics, hazard/reaction family, tactical policy or complete playback required by the intended scene.

Reduced-version status: NARRATIVELY READY.

Reduced version keeps:
- ecological passage state outside BattleSpec;
- route closure/restriction as world state;
- observation from safe points;
- any separate combat on stable audited terrain;
- narrow battle writeback only.

Combat cannot decide migration cause, population size, long-term route safety or whether the whole migration succeeded.

## PTU/Caelo questions still unresolved

1. Which supplied Caelo location/encounter sources define region-specific ecological distributions or recurring migration windows that should constrain future Ouros species placement?
2. Which PTU Skills/Features are authoritative for formal field observation, tracking or ecological inference in the adopted source priority?
3. Which individual Pokémon movement/capability rules matter for following or safely observing moving wild groups outside combat?
4. Which exact wild-encounter provisioning contracts currently exist in Java/RPG for server-owned ecology to request a visible subgroup without treating Cobblemon spawns as authority?
5. Which weather/environment observations can be stored as narrative context without invoking mechanical weather state?
6. What evidence threshold should an Ouros institution require before changing a public route advisory from `possible passage` to `active passage`?

Until these are resolved, pass 178 keeps species, exact thresholds, migration dates, encounter weights and mechanical ecological effects proposed/uncertain.