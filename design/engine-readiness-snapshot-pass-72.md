# Engine Readiness Snapshot — Pass 72

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-21

## Repositories inspected

Read-only:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`c36163210105df5a609863cb5583779b2db5f245`

Latest inspected commit:

`Derive Rider Agility Training from canonical mounted pairs`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/c36163210105df5a609863cb5583779b2db5f245

### New bounded evidence since Pass 71

Java first froze the Rider Agility Training mount relationship against the Python oracle, then moved mounted-pair state into canonical battle environment state and derives that initiative interaction from server-owned state.

This provides additional evidence for:
- authoritative runtime ownership of an environment/relationship input used by initiative;
- the already VERIFIED action economy / initiative family;
- a bounded Trainer Feature/perk interaction;
- separation from caller-supplied initiative compatibility context.

It does not prove:
- a general mounted movement system;
- complete Rider rules;
- complete Trainer Feature coverage;
- carrying passengers through forced movement;
- mount collision/interception;
- overworld riding;
- fungal/deadwood behavior;
- environmental status zones;
- dynamic terrain;
- wildlife tactical goals;
- Minecraft/Cobblemon adapter playback.

One Rider-related initiative slice never promotes complete movement or the whole Trainer Feature family.

## AutoPTU-Java declared remaining work

The current Java README still explicitly lists these large unfinished areas:
- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move/Ability/item/perk/Trainer Feature hook registries;
- full semantic transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The repository remains a headless Java rules library with Python AutoPTU as authority while parity is incomplete.

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible commits remain Career-focused and do not alter the permanent tactical capability assessment for Pass 72.

Available project-file evidence exposes narrow mechanics relevant to this pass:
- `Spore` has a defined status effect;
- `Effect Spore` has a defined contact-triggered status contract;
- forest/wood labels participate in specific Move/environment mappings inside Python.

These are examples of authored battle rules. They do not establish a generic fungal-environment subsystem.

## PTU / Caelo evidence relevant to Pass 72

Project-file search recovered narrow source-derived text for `Spore` and `Effect Spore`, enough to preserve the rule boundary that those effects come from specific mechanics.

The complete primary PTU/Caelo corpus for fungi, environmental spores, mushroom harvesting, Naturewalk or forest hazards was not reliably recoverable during this pass.

No new mechanic is therefore asserted for:
- ambient spores;
- mushroom toxicity or edibility;
- fungal disease;
- mycorrhizal effects;
- decaying wood terrain costs;
- rotten-log collapse;
- fungal visibility penalties;
- decomposer swarms;
- compost/fertility bonuses.

## Permanent capability map

| Permanent capability family | Pass 72 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Geometry, target anchors, footprints, ranges and LoS have bounded parity evidence. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers and fit predicates have bounded implementation evidence. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Broad forced movement, interception, dynamic route changes and movement reactions remain unfinished. |
| core calculations | VERIFIED | Core PTU tables/stages/accuracy and selected modifiers have implementation evidence. |
| action economy / initiative | VERIFIED | Initiative assembly/install/runtime projection plus multiple modifier families now have strong parity coverage. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial; complete status/Ability/Feature/reaction/delayed coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Multiple damage/post-damage slices exist; complete stateful behavior is not proven. |
| status lifecycle | PARTIAL | Several status contracts exist; full controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Some semantic environment state is authoritative, but broad terrain behavior, dynamic changes, hazards, zones and reactions remain incomplete. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; catalog behavior is incomplete. |
| abilities | PARTIAL | Multiple Ability hooks exist; complete registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog does not. |
| Trainer Features / perks | PARTIAL | Registry/runtime slices and several Features exist, now including Rider Agility Training initiative authority; complete catalog is not proven. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-choice generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware withdrawal, protection, avoid-hazard, route-preservation and survey behavior remain future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a headless rules core; world projection and semantic playback are incomplete. |

## Pass 72-specific overworld blockers

`OVERWORLD_DEAD_ORGANIC_OBJECT_IDENTITY = BLOCKING`

The world server needs persistent identity for narratively/ecologically important snags, logs, stumps and woody debris independent of Minecraft blocks.

`OVERWORLD_DECAY_REVISION_HISTORY = BLOCKING`

Structural/moisture/cavity/soil-incorporation state needs versioned history rather than per-tick block decay.

`OVERWORLD_FUNGAL_OCCURRENCE_REGISTRY = BLOCKING`

Observed fruiting, identification, substrate and samples require provenance and uncertainty.

`OVERWORLD_DECOMPOSER_ACTIVITY_PROFILE = BLOCKING`

Coarse seasonal/moisture-linked decomposer state does not yet exist as server authority.

`OVERWORLD_ROOT_FUNGAL_ASSOCIATION = BLOCKING`

Ecological association claims need evidence and must remain separate from psychic/communications systems.

`OVERWORLD_NUTRIENT_RETURN_LEDGER = BLOCKING`

Evidence-backed transfer from dead organic material into Soil/Flora assessments needs its own contract and must not create direct yield buffs.

`OVERWORLD_DEADWOOD_HABITAT_USE = BLOCKING`

Repeated shelter/feeding/nesting observations need persistent state before becoming ecological relation edges.

`OVERWORLD_DEADWOOD_MANAGEMENT = BLOCKING`

Retention, removal, relocation and transfer to Material Culture need explicit decisions and provenance.

`OVERWORLD_DECOMPOSITION_TO_SOIL = BLOCKING`

Pass 72 may emit observations; Soil remains authority for condition assessment.

`OVERWORLD_DECOMPOSITION_TO_FLORA = BLOCKING`

Nutrient/resource observations may affect later vegetation assessments, but decomposition does not directly create recruitment or growth.

`OVERWORLD_DECOMPOSITION_TO_INTERSPECIES = BLOCKING`

Repeated use can propose relation edges; the Interspecies layer remains authority for persistent ecological relationships.

`OVERWORLD_DECOMPOSITION_TO_WILDFIRE = BLOCKING`

Wildfire supplies burn/deadwood origin history; decomposition must not rewrite fire severity.

`OVERWORLD_DECOMPOSITION_TO_MATERIAL_CULTURE = BLOCKING`

Removal of wood/material requires an explicit world-state transfer and preserved provenance.

`OVERWORLD_DECOMPOSITION_TO_COBBLEMON = BLOCKING`

Mushroom blocks, Pokémon spawns and loaded chunks must not become direct authority for fungal identity, decay age or ecological function.

`OVERWORLD_DECOMPOSITION_TO_BATTLE = BLOCKING`

A decay/fungal state cannot create PTU statuses, damage, terrain or hazards without exact rules and a verified projection contract.

## Critical distinction: fungal observation versus PTU spore mechanic

A mushroom or fungal fruiting body in the overworld is ecological/presentation state.

A Pokémon using `Spore`, possessing `Effect Spore`, or triggering another authored fungal Move/Ability is battle state.

Therefore:

```text
mushrooms visible nearby
≠ Spore Move
≠ Effect Spore
≠ Sleep
≠ Poisoned
≠ Paralysis
≠ hazard zone
```

Any link requires a specific legal combatant mechanic or separately authored PTU/Caelo environmental rule.

## Critical distinction: deadwood geometry versus dynamic hazard

Verified base movement can use a frozen arena containing stable static log/blocker geometry.

It does not prove:
- a rotten log collapsing mid-turn;
- actors being pushed when wood fails;
- destructible bridges;
- changing holes/gaps;
- spreading fungal zones;
- wildlife choosing an escape corridor;
- structural damage from decay.

Those require BLOCKING movement/hazard/AI/adapter families or other explicit contracts.

## Encounter dependency review

### Rot Log Passage

Full version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL
- full stateful damage — PARTIAL if actual structural/environmental damage is introduced
- status lifecycle — PARTIAL if a legal spore/status rule is used
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Reduced version:
Resolve the trail decision before battle and freeze the trunk as static geometry. No collapse, dynamic route, ambient spore status or noncombatant wildlife movement occurs inside AutoPTU.

### Hollow Trunk Refuge

Full version additionally depends on:
- PROTECT_ROUTE/WITHDRAW-style objective semantics — BLOCKING outside the current permanent capability map;
- autonomous withdrawal/protection tactical policy — BLOCKING;
- dynamic refuge/route state — BLOCKING terrain/movement/adapter families.

Reduced version:
Resolve refuge occupancy and evacuation in overworld state. Fight only actual hostile combatants on fixed nearby geometry.

### Fruiting Survey

Full version may eventually use specific legal Pokémon Moves/Abilities, but generic fruiting remains nonmechanical. Visitor/wildlife routing and environmental zones require tactical AI plus movement/terrain/adapter support.

Reduced version:
Keep mushrooms, samples, visitor timing and survey objectives outside battle. If a separate conflict occurs, use a static legal encounter and only the actual Moves/Abilities on participating sheets.

## Pass 72 implementation priority

This worldbuilding layer does not require the Java battle engine to implement decomposition.

A useful first implementation can exist entirely as server-owned overworld state plus static encounter projection.

Battle work should remain focused on the engine roadmap rather than adding ad-hoc Minecraft mushroom effects.

The highest-value integration contracts for this layer are:
1. persistent dead-organic identity and revisions;
2. provenance-backed ecological observations;
3. coarse offline advancement;
4. cross-layer links to Soil/Flora/Science;
5. static battle snapshot generation;
6. later, only after rules parity, exact fungal Move/Ability/hazard behavior.
