# Engine Readiness Snapshot — Pass 61

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-20

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`daa8956f913322fd7a17c3374f838303d0aa4a4e`

Latest inspected commit:

`Port base Pokemon initiative entry resolution (#93)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/daa8956f913322fd7a17c3374f838303d0aa4a4e

Since the Pass 60 snapshot at `6678d4563116a4ec8c70d9daafc00d28bb9ab25b`, Java is two commits ahead.

The new evidence includes:

- an initiative-rebuild contract workflow;
- a base Pokémon initiative-entry resolver;
- Python-oracle fixtures and parity tests for that resolver;
- explicit handling in that slice for resolved Speed input, trainer modifier, Bashed, Tailwind, temporary initiative bonus and initiative-zero state.

The resolver explicitly states that weather/terrain Ability multipliers, Early Bird, Agility Training and Hardened Initiative remain separate parity slices.

This is important evidence discipline: one initiative-entry resolver does not prove every initiative modifier.

## README boundary remains unchanged

The Java README still states that Python AutoPTU remains authoritative while the port is incomplete.

It still lists unfinished broad work including:

- core battle state expansion;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/Ability/item/perk/Trainer Feature registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

README:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest work remains Career-focused (`Career: make roster recovery deterministic`).

No new Python tactical commit observed in this run changes the permanent capability classification.

Python is the behavioral oracle only for slices explicitly frozen and compared by the Java migration process.

## Permanent capability map

One representative mechanic never promotes an entire family.

| Permanent capability family | Pass 61 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Dedicated targeting, areas, footprints, anchors and LoS coverage exist. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers, Wallrunner and fit predicates exist. This is not complete movement. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement and interception/broad movement reactions remain unfinished. |
| core calculations | VERIFIED | Damage Base/type tables, stages, accuracy primitives, crit probability and multiple calculation modifiers exist. |
| action economy / initiative | VERIFIED | Typed turn flow, action budget, deterministic ordering, authoritative initiative progress, round rollover and now a parity-tested base Pokémon initiative-entry resolver are directly evidenced. |
| full turn / round lifecycle | PARTIAL | Initiative infrastructure is stronger, but complete phase/status/Ability/Feature/reaction/delayed-effect coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Several damage and post-damage slices exist while the README still lists full damage as unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts and lifecycle timing slices exist; full controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Terrain movement costs and calculation primitives do not prove runtime terrain, weather phases, hazards, zones or broad reactions. |
| move-specific behavior | PARTIAL | Selected contracts exist; complete PTU Move behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; full catalog behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered/lifecycle infrastructure and selected Features exist; full catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal action generation/filtering is implemented. |
| AI tactical policy | BLOCKING | Scoring/policy remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core, not the Minecraft adapter. |

## Why initiative remains VERIFIED while lifecycle remains PARTIAL

The new Java resolver makes initiative evidence stronger.

It does not close every turn/round timing path.

Lifecycle still includes:

- every START/END round effect;
- status application, duration and expiration;
- Ability phase hooks;
- Trainer Feature phase hooks;
- reaction/interrupt windows;
- delayed and queued effects;
- interaction with complete damage;
- interaction with forced movement;
- interaction with terrain/weather/hazards;
- full event/transcript parity.

Therefore:

`action economy / initiative = VERIFIED`

`full turn / round lifecycle = PARTIAL`

## Pass 61-specific overworld blockers

Biosecurity and population provenance are primarily world-state systems outside AutoPTU-Java.

`OVERWORLD_BIOSECURITY_CASE_GRAPH = BLOCKING`

The server needs persistent case objects linking observations, provenance hypotheses, pathways, establishment, spread, impact assessments and management reviews.

`OVERWORLD_ECOLOGICAL_PROVENANCE = BLOCKING`

The server needs to preserve whether a population is native, range-expanding, introduced, escaped, released, translocated or unresolved without collapsing those states into one label.

`OVERWORLD_ARRIVAL_PATHWAYS = BLOCKING`

Transport, cargo, nursery, release, crisis and anomalous-space systems need a common pathway contract.

`OVERWORLD_POPULATION_ESTABLISHMENT_AND_SPREAD = BLOCKING`

The server needs coarse population persistence/spread state without simulating every individual.

`OVERWORLD_BIOSECURITY_IMPACT_EVIDENCE = BLOCKING`

The server needs evidence-bearing ecological-impact assessments linked to existing interspecies, pollution, infrastructure, agriculture and conservation state.

`OVERWORLD_TRANSLOCATION_IDENTITY = BLOCKING`

Relocation/release must preserve persistent Pokémon IDs, custody history and source/destination provenance.

`OVERWORLD_COBBLEMON_SPAWN_PROJECTION = BLOCKING`

Minecraft/Cobblemon needs a safe adapter that projects population state into spawn context without making loaded entities authoritative or creating exploitable rarity manipulation.

These blockers do not lower battle-core capability categories.

## Encounter dependency review

### Cargo-Hitchhiker Discovery

Full version requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if cargo lanes change dynamically;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy for escape/protect/withdraw goals — BLOCKING;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- ecological-provenance/pathway writeback — BLOCKING outside battle core.

Reduced version:

Resolve escape paths in overworld state before combat. Freeze cargo geometry. Run a conventional static legal encounter only when conflict occurs. Record escaped/captured/observed individuals afterward without inferring population establishment.

### Nursery Escape Perimeter

Full version requires:

- complete movement/interception — BLOCKING for mobile recovery targets;
- terrain/weather/hazards/zones/reactions — BLOCKING when damaged infrastructure creates dynamic danger;
- tactical AI — BLOCKING for escape/withdraw behavior;
- playback — BLOCKING;
- exact Move/Ability/item/Feature families — PARTIAL unless the specific mechanic is verified;
- base targeting/calculations/initiative/legal-action infrastructure — VERIFIED where applicable.

Reduced version:

Search and containment occur in overworld state. Each Pokémon remains a persistent entity. Keep workers outside the grid. Only a genuine confrontation becomes a static AutoPTU battle.

### Wetland Spread Survey

Full version requires:

- targeting/LoS — VERIFIED;
- base movement including Swim legality — VERIFIED;
- complete movement/interception — BLOCKING for moving groups;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL;
- damage/status/Move/Ability/item/Feature families — PARTIAL as actually used;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic wetland/weather state;
- AI tactical policy — BLOCKING for withdrawal or route behavior;
- playback — BLOCKING;
- population/spread inference — BLOCKING outside battle core.

Reduced version:

Survey and inference remain world-state operations. Freeze any battle map before encounter start. Battle results provide facts about the encountered individuals only.

## PTU / Caelo caution

Pass 61 creates no new mechanical effect for introduced or newly arrived species.

Do not infer or invent:

- capture bonuses or penalties;
- mandatory capture/removal;
- auto-hostility;
- pack bonuses;
- relocation Skill checks;
- ecological damage from normal attacks;
- disease transmission;
- quarantine status;
- habitat-control Abilities;
- encounter XP changes;
- population-level consequences from one Fainted result;
- legal authority to seize a Pokémon.

The project-supplied primary Caelo corpus was not reliably available in this automation runtime, so no new Caelo-specific biosecurity, capture, relocation or conservation rule is asserted.

## Snapshot conclusion

Pass 61 does not justify any permanent capability promotion.

Java's newest work strengthens the already-VERIFIED action economy/initiative family with a parity-tested base Pokémon initiative-entry contract. Lifecycle remains PARTIAL because broad timing and interaction surfaces remain open.

Biosecurity worldbuilding can advance now because observation, provenance, pathways, establishment, spread and management are overworld state. Mechanically rich capture/escape/containment scenes remain blocked by complete movement, broad terrain/zones/reactions, tactical AI and Minecraft playback.

Reduced encounters can preserve the same ecological premise while keeping population inference and movement outside the battle grid.