# Engine Readiness Snapshot — Pass 105

Status: implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Live evidence inspected

AutoPTU-Java head observed during Pass 105:

`84b3aa8aafa6d52a5717b9d9ee079bed1f2fe35d`

Latest relevant commit:

`Port generic Trainer Feature resource gates (#140)`

The commit follows Pass 104’s prerequisite/context/frequency work with another generic Trainer Feature primitive. Java now has Python-parity helpers for:

- checking a Feature’s declared `resource_cost` against authoritative resource balances;
- consuming those declared resources after a legal successful use path calls the helper;
- preserving Python-compatible handling/coercion in parity fixtures;
- preventing Minecraft/Cobblemon from deciding whether the Feature can afford its resource cost.

The Java source explicitly states that this slice excludes:

- AP;
- frequency/usage bookkeeping;
- target scopes;
- effect application.

The immediately preceding slices separately cover generic prerequisite checks, context checks and frequency/cooldown eligibility. These pieces improve Feature infrastructure, but they do not form complete Trainer Feature execution and do not prove the catalog.

The new Java parity workflow checks out pinned Python AutoPTU commit:

`16d228efa63aabecb67fa788959a359aac7f8f03`

for this resource contract.

Current AutoPTU repository head observed separately during Pass 105:

`53720730fe9ddcf07da1668897b5c034f2ab98ed`

Its newest visible commit packages the validated Vercel runtime and adjusts deployment/validation infrastructure. That is useful product infrastructure but does not justify a tactical capability promotion.

The AutoPTU-Java README continues to state that Python remains authoritative while the port is incomplete and continues to list major unfinished work including:

- core combatant/grid battle state;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full transcript parity;
- tactical AI;
- Minecraft/Cobblemon adapter.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Static geometry, target anchors, footprint overlap, range and geometric line of sight remain VERIFIED.

Pass 105 non-inference:

- warehouse shelves do not create cover automatically;
- crates are not combatants or targetable objects unless BattleSpec represents them;
- a sealed storage zone is an access rule, not a LoS rule;
- a convoy being important does not make it untargetable;
- a cold room door does not become an interactable tactical object merely because it exists in Minecraft;
- freight position in world state does not define a legal battle target.

#### base movement legality

Established Shift/Jump and known movement-mode legality remain VERIFIED.

Pass 105 non-inference:

- pushing a pallet is not base Shift;
- moving a crate is not forced movement;
- loading/unloading cargo is not automatically an Interact action;
- a warehouse aisle does not have special movement cost without an authored battle map rule;
- vehicle or convoy movement is not covered by Pokémon/Trainer base movement;
- a Pokémon helping with logistics does not gain carrying capacity from movement mode alone.

#### core calculations

Established PTU calculation primitives remain VERIFIED.

Pass 105 adds no:

- stockout penalty;
- supply-chain risk score;
- scarcity damage modifier;
- cold-storage modifier;
- warehouse quality score;
- procurement check;
- cargo value formula;
- reserve release bonus;
- substitution equivalence calculation.

#### action economy / initiative

Established action economy and initiative remain VERIFIED.

Pass 105 non-inference:

- receiving freight does not grant battle actions;
- releasing reserve stock is not a battle interrupt;
- loading cargo does not have a defined Standard/Shift/Swift action cost;
- a procurement approval does not affect initiative;
- emergency priority does not grant initiative priority;
- convoy order is not battle initiative order.

#### AI legal-action infrastructure

Legal `BattleChoice` generation remains VERIFIED.

It still does not prove policy goals such as:

- PROTECT_CARGO;
- CLEAR_LOADING_ZONE;
- REACH_EXIT;
- WITHDRAW_WITH_SHIPMENT;
- AVOID_CIVILIANS;
- HOLD_WAREHOUSE_AISLE;
- PRESERVE_COLD_STORAGE;
- ESCORT_CONVOY;
- DO_NOT_DAMAGE_STOCK;
- DEESCALATE_NEAR_SENSITIVE_GOODS.

Those require AI tactical policy.

### PARTIAL

#### full turn / round lifecycle

Still PARTIAL.

Existing evidence covers meaningful slices of phase ordering, cleanup, delayed hits, initiative rebuilding, temporary effects, Trainer AP/action reset, declared-action cleanup and Trainer Feature ordering/gates.

Pass 105’s new generic Trainer Feature resource primitive does not complete lifecycle. Complete START/END behavior, all timing interactions, interrupts/reactions, durations and full transcript parity remain unproven.

Supply-chain world clocks are separate from battle rounds.

A shipment changing from `IN_TRANSIT` to `ARRIVED` cannot be driven by battle-round lifecycle.

#### full stateful damage pipeline

Still PARTIAL.

Representative authoritative damage and post-damage hooks exist, but the complete pipeline remains unfinished per the Java project’s own status.

Pass 105 non-inference:

- damaged packaging -> HP damage;
- dropped cargo -> damage roll;
- freezer failure -> cold damage;
- warehouse machinery -> automatic hazard damage;
- stock shortage -> reduced combat stats;
- convoy collision -> damage;
- spoiled item -> Poisoned.

#### status lifecycle

Still PARTIAL.

Supply-chain state does not create PTU Status conditions.

No automatic mapping exists for:

- cold-room exposure -> Frozen/Slowed;
- smoke in loading area -> Poisoned;
- stress over shortages -> Fear/Confused;
- heavy carrying -> Slowed;
- damaged food -> Poisoned;
- stockout -> Vulnerable.

Any such mapping requires an exact governing rule and implementation.

#### move-specific behavior

Still PARTIAL.

Representative Move slices exist. Pass 105 adds no evidence about Moves used for carrying, loading, refrigeration, transport, warehouse interaction or convoy defense.

A Move that can manipulate an object under PTU rules must be validated specifically before it changes freight state.

#### abilities

Still PARTIAL.

Representative Ability hooks exist. Pass 105 does not infer logistics powers from flavor.

Examples of prohibited inference:

- Pickup -> warehouse retrieval automation;
- Super Luck -> procurement advantage;
- Heatproof -> cold-chain control;
- Refrigerate -> refrigeration infrastructure;
- Heavy Metal -> lifting bonus;
- Pickup/Harvest -> unlimited supply production.

Only exact authored rules can support a narrow behavior.

#### items

Still PARTIAL.

Representative held-item behavior exists.

World inventory is not the battle item registry.

A stock batch, crate, shipment, purchase order, container, spare part or food batch is a world/material record unless it maps to an implemented mechanical Item.

A warehouse containing a Potion does not automatically place that Potion in a Trainer’s battle inventory.

#### Trainer Features / perks

Still PARTIAL, with stronger generic infrastructure evidence in Pass 105.

Recent Java sequence now includes:

- #137 — generic prerequisite gates;
- #138 — generic context gates;
- #139 — generic frequency/cooldown gates;
- #140 — generic Feature resource availability/consumption primitive.

The newest resource slice is real progress: declared resource balances can be evaluated and consumed through a Python-parity helper rather than Minecraft-owned logic.

The family remains PARTIAL because generic execution is still not complete. The latest code itself excludes AP, frequency/usage mutation, target scopes and effect application from the new resource helper, while concrete Feature behavior remains separately incomplete.

Pass 105 non-inference:

- procurement officer role = Trainer Feature;
- warehouse worker = Skill rank;
- access to stock = Feature prerequisite;
- inventory reserve = Feature resource;
- institutional budget = Trainer AP;
- stock consumption = Feature resource consumption;
- shipment frequency = Feature cooldown;
- logistics role = target scope;
- successfully sourcing a part = Feature effect.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Still BLOCKING as a complete family.

Pass 105 impact:

- no real moving convoy objective;
- no in-grid forklift/pallet displacement;
- no escort/interception around cargo;
- no forced movement caused by industrial machinery;
- no moving workers/civilians through an active battlefield;
- no pushing freight carts using battle movement rules;
- no moving loading-zone chokepoints.

Reduced encounter versions must keep cargo and noncombat logistics actors outside the grid.

#### terrain / weather / hazards / zones / reactions

Still BLOCKING as a complete family.

Pass 105 impact:

- cold storage does not create Ice/Snow/Weather effects;
- steam does not create a hazard;
- loading machinery does not create hazard zones;
- refrigerated rooms do not create movement penalties;
- warehouse spills do not create terrain automatically;
- restricted stock areas do not become protected tactical zones;
- reserve-release decisions do not create reactions;
- route weather remains overworld state unless an authored battle environment is validated.

Existing field-state primitives do not prove complete environmental behavior.

#### AI tactical policy

Still BLOCKING.

Supply-chain encounters frequently need non-KO objectives that legal-action generation alone cannot provide:

- protect a route;
- withdraw from sensitive stock;
- preserve cargo;
- avoid machinery;
- clear an exit;
- escort a convoy;
- disengage after access is restored;
- avoid damaging a storage area.

Until objective-aware policy exists, reduced versions should use static conventional encounters.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still BLOCKING.

No verified end-to-end authority contract yet exists for:

- world inventory -> visual warehouse representation;
- stock reservations -> container access/UI;
- batch IDs -> Minecraft items without duplication;
- freight consignments -> vehicles/representative cargo;
- storage-condition state -> visual alarms;
- route/service state -> freight playback;
- battle inventory projection -> authoritative AutoPTU item usage;
- battle results -> world cargo consequences;
- server stock corrections -> unloaded chunks;
- preventing Minecraft container state from becoming inventory truth.

## Pass 105 specific overworld blockers

### SUPPLY_CHAIN_GRAPH

Persistent source/storage/distribution/consumption relationships with history.

Status: BLOCKING outside battle core.

### DEMAND_AND_PROCUREMENT_STATE

Demand signals, requests, approval-to-source and source offers.

Status: BLOCKING outside battle core.

### INVENTORY_POOL_AND_RECONCILIATION

Aggregate total/available/reserved/held stock plus versioned counts and discrepancy handling.

Status: BLOCKING outside battle core.

### STOCK_BATCH_SPECIFICATION_STATE

Batch identity, compatibility/specification refs and provenance handoff.

Status: BLOCKING outside battle core.

### STOCK_ALLOCATION_AND_RESERVATION

Purpose-scoped reservations and releases.

Status: BLOCKING outside battle core.

### STORAGE_NODE_AND_CONDITION_STATE

Warehouses, caches, cold rooms, storage dependencies and monitoring evidence.

Status: BLOCKING outside battle core.

### FREIGHT_CONSIGNMENT_STATE

Bulk freight identity, legs, custody, arrival and receipt separate from addressed postal items.

Status: BLOCKING outside battle core.

### RECEIVING_ACCEPTANCE_STATE

Expected versus observed contents, holds, acceptance/rejection and discrepancy records.

Status: BLOCKING outside battle core.

### SHORTAGE_AND_BACKORDER_STATE

Precise shortage classes such as stockout, wrong specification, reserved-only, quality hold and route blocked.

Status: BLOCKING outside battle core.

### SUBSTITUTION_VALIDATION_STATE

Candidate substitutions with technical, institutional and mechanical validation kept separate.

Status: BLOCKING outside battle core.

### EMERGENCY_RESERVE_STATE

Purpose-restricted stock, release authority and replenishment plans.

Status: BLOCKING outside battle core.

### SUPPLY_RESILIENCE_STATE

Alternate sources/routes, mutual aid, pre-positioned stock and readiness review.

Status: BLOCKING outside battle core.

### WORLD_INVENTORY_TO_BATTLE_INVENTORY_PROJECTION

A server-authoritative contract must decide which implemented mechanical items and legal usage state enter a BattleSpec.

Status: BLOCKING.

This is especially important because loaded Minecraft containers must never become PTU inventory authority.

## Encounter readiness

### Regional Depot Chokepoint

FULL:

Requires complete movement/interception for moving objectives, AI tactical policy for cargo/route goals, adapter/playback for freight and possibly terrain/hazards/zones if industrial features become tactical.

Current state: BLOCKED at full fidelity.

REDUCED:

Cargo/workers remain off-grid. Static geometry and standard legal actions can support the combat portion. World state resolves shipment movement afterward.

Current state: viable only to the degree the chosen conventional battle uses implemented PARTIAL combat families.

### Cold Storage Alarm

FULL:

Requires environment/hazards if temperature/equipment becomes tactical, complete movement for workers/cargo, objective-aware AI and adapter/playback.

Current state: BLOCKED at full fidelity.

REDUCED:

Storage assessment and evacuation occur before combat. Static safe room; no cold hazard. Batch acceptance resolved separately.

Current state: narratively viable without inventing PTU environment mechanics.

### Emergency Convoy Split

FULL:

Requires moving convoy objectives, interception/forced movement, route environment where applicable, objective-aware AI and playback.

Current state: BLOCKED.

REDUCED:

Allocation and convoy position resolve as overworld state. If conflict occurs, AutoPTU receives a static chokepoint encounter and world state resumes afterward.

Current state: viable as a reduced implementation.

## Supply-specific no-inference ledger

Pass 105 explicitly prohibits:

- `stock present` -> `stock available`;
- `stock available` -> `mechanically usable`;
- `same item name` -> `same specification`;
- `allocated` -> `shipped`;
- `shipped` -> `received`;
- `received` -> `accepted`;
- `accepted` -> `battle inventory`;
- `missing stock` -> `theft`;
- `delay` -> `sabotage`;
- `cold room` -> `Ice Terrain`;
- `refrigeration failure` -> `damage or Status`;
- `heavy cargo` -> `Slowed`;
- `Pokémon worker` -> `carrying capacity`;
- `forklift/crane` -> `forced movement`;
- `emergency reserve` -> `free mechanical items`;
- `scarcity` -> `combat debuff`;
- `substitute` -> `mechanical item equivalence`;
- `warehouse crates visible` -> `inventory count`.

## Canon/mechanical questions still unresolved

- Which institutions own or operate warehouses/depots?
- Which goods require exact counts versus broad inventory bands?
- Which storage requirements are authored canon?
- How are technical specification/compatibility records represented?
- What authority can reserve or release emergency stock?
- Do player clubs/businesses have shared inventories?
- How much inventory state advances while chunks are unloaded?
- What is the battle-inventory handoff contract?
- Which Pokémon can legally carry cargo, and under which PTU/Caelo capabilities?
- What are the project’s exact encumbrance/carrying rules?
- Which Trainer Features, if any, affect procurement, fabrication, repair sourcing or storage?
- How are sensitive medical/research batches kept private in multiplayer?
- How are stock discrepancies reconciled without generating false theft cases?

The full primary Caelo corpus was not reliably retrievable during this runtime, so no new Caelo rule is asserted in Pass 105.

Super PTU Online Helper was not exposed as an invocable capability. No output is attributed to it.