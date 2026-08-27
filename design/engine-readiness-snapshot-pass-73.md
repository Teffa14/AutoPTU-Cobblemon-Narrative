# Engine Readiness Snapshot — Pass 73

Status: implementation evidence snapshot. Not canon.

## Read-only sources inspected

AutoPTU-Java head: `6beb908f4246eb9f2e94161e3e28e4044be8fa92`

AutoPTU Python head: `408c3a1ca3253592dbd04d17594492439bcc90db`

Narrative repo pre-pass head: `c200cba18daed20b65730c537c0fb761723decdb`

## Java evidence since Pass 72

No newer AutoPTU-Java commit exists beyond the Pass 72 head.

The latest Java work remains:

- `343ff74d068cf42a7db83ad706cff03117a9fbd5` — generic held-item START temporary-effect resolver with Python parity;
- `6beb908f4246eb9f2e94161e3e28e4044be8fa92` — additional generic held-item START calculation-effect families with frozen contracts/tests.

This remains concrete PARTIAL evidence for items, status lifecycle and turn/round lifecycle. It does not prove a complete item registry or full stateful battle engine.

The live Java README continues to explicitly list as pending:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- semantic battle-event emission and full `BattleSpec -> BattleTranscript` parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Python evidence since Pass 72

AutoPTU Python advanced to `408c3a1ca3253592dbd04d17594492439bcc90db`.

The recent changes prevent Career from softlocking when Training Kit actions would leave a zero-Pokémon roster and keep preseason scouting available when the roster is empty.

This is robustness/persistence work in Career. It does not establish a new tactical rule family for the Java port and does not alter the permanent capability classification below.

## Permanent capability map

### targeting / footprints / range / LoS

Status: VERIFIED

Java has explicit range, area, footprint, target-anchor and LoS contracts in the deterministic action-space layer.

### base movement legality

Status: VERIFIED

Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers, Wallrunner, sprint and landing-fit behavior remain implemented.

This excludes forced movement and interception.

### complete movement including push / pull / knockback / interception / forced movement

Status: BLOCKING

Forced movement remains explicitly pending in the live Java README.

### core calculations

Status: VERIFIED

Damage Base, type effectiveness, combat stages, accuracy-stage calculations, weather DB primitive, crit probability, Burn and modifier/rounding primitives remain implemented.

Primitives do not imply full battle-state completion.

### action economy / initiative

Status: VERIFIED

Typed turn flow, phase sequence, action budget, deterministic initiative, Trick Room/League ordering and declared-action ordering remain present.

### full turn / round lifecycle

Status: PARTIAL

The live phase envelope and held-item START families are real parity-gated slices. Full combat state, complete StatusController behavior and transcript parity remain unfinished.

### full stateful damage pipeline

Status: PARTIAL

Core damage calculations exist. Full damage resolution is still explicitly pending.

### status lifecycle

Status: PARTIAL

StatusController phase-envelope wiring and some held-item START temporary effects are live. The complete status controller/behavior set remains unfinished.

### terrain / weather / hazards / zones / reactions

Status: BLOCKING

A weather calculation primitive exists, but tactical terrain, hazards, forced-environment behavior and reactions remain incomplete/pending.

### move-specific behavior

Status: PARTIAL

Representative infrastructure and slices exist. The complete move hook registry remains pending.

### abilities

Status: PARTIAL

Representative calculations do not establish full Ability coverage. Ability hooks remain incomplete.

### items

Status: PARTIAL

Generic held-item START effect families now have parity evidence. The full item registry, complete timing, consumption and stateful behavior remain incomplete.

### Trainer Features / perks

Status: PARTIAL

Focused Training/Chronicler Accuracy slices remain real evidence. Complete registry coverage remains pending.

### AI legal-action infrastructure

Status: VERIFIED

Deterministic legal-choice generation remains implemented for Shift, direct targets, SELF/FIELD, tile-AoE, footprints, LoS and action-budget filtering.

### AI tactical policy

Status: BLOCKING

AI scoring/policy remains explicitly pending.

### Minecraft / Cobblemon / Craftics adapter and playback

Status: BLOCKING

AutoPTU-Java still explicitly identifies itself as a Java rules library rather than a Minecraft mod. Adapter/playback remains future work.

## Pass 73 encounter consequences

### Warehouse Recovery Window

Intended full version requires:

- VERIFIED targeting/footprints/range/LoS;
- VERIFIED base movement;
- BLOCKING complete movement/interception/forced movement for staff withdrawal and changing access;
- VERIFIED core calculations;
- VERIFIED action economy/initiative;
- PARTIAL full lifecycle;
- PARTIAL full stateful damage;
- PARTIAL status lifecycle;
- BLOCKING terrain/hazards/zones/reactions if unstable shelving, spill zones or changing restrictions matter tactically;
- PARTIAL move-specific behavior;
- PARTIAL abilities;
- PARTIAL items;
- PARTIAL Trainer Features/perks;
- VERIFIED AI legal-action infrastructure;
- BLOCKING AI tactical policy for WITHDRAW/CLEAR_ROUTE/PROTECT behavior;
- BLOCKING adapter/playback for preserving which recovery zones were reached and which stock physically moved.

Reduced version:

Staff quarantine every safely reachable affected unit before battle and leave inaccessible units explicitly unresolved. AutoPTU receives a static conventional arena with no product-recovery objective. After the authoritative result, trace/recovery resumes from world state. Victory cannot locate, authenticate, quarantine or recover an item.

### Restricted Shelf Breakout

Intended full version requires:

- BLOCKING complete movement if civilians and staff are simultaneously withdrawing;
- BLOCKING environment/zones/reactions if access barriers or protected stock areas change during battle;
- BLOCKING tactical AI for escape/territorial objectives;
- BLOCKING adapter/playback for synchronising shop closure, stock protection and entity movement;
- PARTIAL ordinary move/ability/item/status/damage families.

Reduced version:

The store closes and all civilians leave before battle. Affected stock is already sealed in world state. AutoPTU resolves a static conventional encounter. Storefront and market-action state are reviewed afterward.

### Component Retrieval at a Closed Facility

Intended full version requires:

- BLOCKING complete movement for technician withdrawal/interception-sensitive routing;
- BLOCKING environment/hazard/zone/reaction support for active technical spaces;
- BLOCKING tactical AI for territory/withdrawal/protection goals;
- BLOCKING adapter/playback for exact component/world-state preservation through combat.

Reduced version:

Technicians remain outside the tactical grid. The component stays in Maintenance/traceability state. AutoPTU resolves only the combat threat, then technical inspection/removal resumes afterward.

## Batch-traceability mechanical boundary

Pass 73 usually needs no battle mechanics.

It may reference:

- a PTU/Caelo mechanical item;
- a physical item instance that maps to such an item;
- a material or production batch;
- a procurement receipt;
- an installed component;
- a shipment or custody handoff;
- a care-supply batch;
- an authoritative battle transcript if an exact implemented item behavior was observed.

It must never itself create or alter:

- held-item effects;
- item timing or consumption;
- Moves;
- Ability effects;
- Trainer Features;
- Accuracy;
- damage;
- initiative;
- action budget;
- movement;
- statuses;
- terrain/weather/hazards;
- AI behavior.

A “defective” or counterfeit mechanical item variant is not allowed merely because the narrative record says a unit is suspect. Mechanical variance requires explicit PTU/Caelo rules and verified engine support.

## Promotion decision

No permanent capability category is promoted in Pass 73.

No new Java tactical evidence has landed since Pass 72. Python Career robustness advanced, but that does not change the Java combat capability map.

## Open mechanical questions

- Which held-item START families remain missing after `6beb908f`?
- When will held-item END, consumption and other stateful item behavior become parity-complete?
- When will StatusController be complete rather than a set of live representative slices?
- Which move/ability/item/Trainer Feature hook registries will be ported next?
- When will forced movement/interception become authoritative?
- What objective semantics will exist for WITHDRAW, PROTECT, CLEAR_ROUTE, RECOVER or ESCAPE?
- What is the first parity-safe Minecraft/Cobblemon/Craftics adapter slice?
- Can BattleTranscript eventually expose item-use provenance strongly enough for world-state systems to link an exact persistent item instance to a battle event without duplicating rule ownership?

Until these are answered by live contracts/tests, rich Pass 73 encounters retain reduced implementations.
