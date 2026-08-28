# Engine Readiness Snapshot — Pass 104

Status: IMPLEMENTATION-READINESS EVIDENCE. Creates no PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 104 adds proposed continuity for storage and warehouse operations: facilities, zones/slots, authorized intake, putaway, internal movement, verified physical presence, picking, staging, inventory observations/reconciliation, broad capacity/overflow state and external-hold enforcement.

Narrative baseline before Pass 104 writes: `ee4484f678114663c56dbc419e67f7c76a1649dc`.

The complete recursive Narrative repository inventory was inspected at baseline and returned `truncated=false`. Nearby Procurement, Courier, Manufacturing, Batch Traceability, Storefront, Material Culture, Ports and Shared Equipment layers were inspected so this pass owns only the missing internal-storage lifecycle.

## Live engine evidence

AutoPTU-Java head inspected during this pass: `136cf6d090b6387481fc7bb908abb098abddd8be`.

New Java evidence since Pass 103:

- #259 `Compose intercept spatial success authoritatively`;
- parent: #258 `Compose intercept candidate sequence authoritatively`;
- #259 composes the Intercept sequence through the spatial-success branch and adds parity/gating evidence for that specific path.

This is meaningful progress for Intercept orchestration and spatial success. It still does not verify the permanent family `complete movement including push/pull/knockback/interception/forced movement` as a whole.

Still outside family-wide verified coverage:

- broad Push/Pull from all supported sources;
- broad Knockback from all supported sources;
- competing/generalized reactions;
- reaction ordering outside the frozen Intercept path;
- every forced-movement source;
- environmental displacement;
- active vehicle/equipment displacement;
- complete Move/Ability/Item/Trainer Feature integration;
- objective-aware tactical policy;
- semantic Minecraft/Cobblemon playback.

AutoPTU Python head inspected during this pass: `3c8ab68b5266085cb931568ca5e8918986a4e688`.

Its latest merged change, PR #212, tolerates malformed legacy Career battle events during replay. This is Career stability/backward-compatibility work. It does not add tactical battle-family coverage for the warehouse encounters proposed here.

No permanent capability category is promoted in Pass 104.

## PTU / Caelo storage boundary

The project already preserves item instances, material batches, provenance, ownership/custody references and mechanically governed item/crafting behavior.

Public PTU 1.05 source availability was rechecked during this pass. No governing evidence inspected establishes a universal warehouse-management subsystem for slotting, putaway, cycle counting, storage-capacity math, forklifts, pallet/container handling, rack collapse, cold-chain degradation, inventory-accuracy modifiers or species-based warehouse labor.

A separate Pokémon Tabletop wiki page surfaced an `Inventory` concept, but that page is not treated as PTU 1.05 governing evidence for Ouros warehouse operations. Pass 104 therefore does not import its slot model or downtime assumptions.

Any exact Item, Move, Ability, Capability or Trainer Feature used during storage work still requires the governing PTU/Caelo source and AutoPTU implementation evidence.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Verified for reviewed static arenas. Shelving, walls, containers and aisles only affect tactical geometry after explicit arena review.

`base movement legality`

Verified for ordinary static movement. It does not create conveyor movement, forklift traffic, climbing-rack rules, moving pallets or evacuation semantics.

`core calculations`

Verified calculation primitives remain available. No mass, load, temperature, shelf-capacity, collision or structural arithmetic is inferred.

`action economy/initiative`

Verified typed action budget/order remains available.

`AI legal-action infrastructure`

Verified legal-action enumeration remains available. It does not choose withdrawal, perimeter defense, cargo protection or noncombatant-safe routes.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. Java #259 extends the authoritative Intercept sequence through spatial success on top of #256-#258. This remains a specific path, not proof of broad reaction/forced-movement completeness.

`full turn/round lifecycle`

PARTIAL.

`full stateful damage pipeline`

PARTIAL. Pass 104 introduces no falling-rack, vehicle, crushing, cold, collision or container damage.

`status lifecycle`

PARTIAL. Alarm, panic, cold exposure, contamination, fatigue or access restriction are not PTU statuses unless governing rules explicitly establish them.

`move-specific behavior`

PARTIAL. A Move cannot be generalized into lifting, stacking, cooling, scanning, opening, securing, transporting or inventory verification.

`abilities`

PARTIAL. An Ability does not automatically qualify a Pokémon for storage work or environmental immunity.

`items`

PARTIAL. Racks, pallets, crates, labels, scanners, forklifts and containers remain world objects unless authoritative item rules apply.

`Trainer Features/perks`

PARTIAL. No universal warehousing/logistics Feature family has been established.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for active loading equipment, moving vehicles, falling racks, dynamic conveyors, outdoor weather effects, cold/hazard zones or generalized protective reactions.

`AI tactical policy`

BLOCKING for withdrawal, corridor protection, perimeter defense, noncombatant avoidance and handoff-area objectives.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING for stable facility/zone/slot bindings, authoritative world-state projection, world-to-arena conversion and semantic battle playback.

## Encounter readiness

### Receiving Dock Withdrawal

Full intended form requires protective withdrawal, multiple routes, Intercept/forced movement, generalized reactions, objective-aware AI and playback. Active vehicles/loading equipment additionally require terrain/hazards/zones plus exact governing mechanics.

Current profile: REDUCED.

Safe form:

Ouros pauses intake and dispatch before encounter creation. Workers, cargo, equipment/vehicles and nonparticipant Pokémon are removed from tactical participation. AutoPTU receives explicit combatants on a reviewed static yard/apron. Victory secures only the immediate perimeter. Procurement, Courier and Storage resume their workflows separately afterward.

### Staging Aisle Perimeter

Full intended form may require narrow-route protection, Intercept/forced movement, generalized reactions, tactical AI, playback and exact hazard mechanics if racks/conveyors/equipment matter.

Current profile: REDUCED.

Safe form:

Staged goods remain off-grid or inert non-targetable world objects. External handoff remains frozen at its last verified state. AutoPTU receives explicit combatants in a static aisle/perimeter. Victory changes immediate access only; it does not dispatch goods, change custody or reveal contents.

### Overflow Yard Conflict

Full intended form may require reviewed terrain, weather/hazard zones, route protection, reactions, objective-aware AI and playback.

Current profile: REDUCED.

Safe form:

Stored goods, staff and handling equipment remain outside the BattleSpec. Weather remains presentation-only unless an exact PTU battle Weather contract is intentionally active. Combat uses a static perimeter. Victory does not change ownership, count, hold status or storage disposition.

## Immediate noncombat readiness

Usable immediately as proposed narrative state:

- persistent storage-facility identity;
- nested zone/slot identity only where needed;
- facility/zone operating states;
- accepted intake awaiting putaway;
- putaway task history;
- internal location moves;
- timestamped presence/count observations;
- pick and staging workflow;
- handoff-readiness without premature custody transfer;
- discrepancy reconciliation with provenance;
- broad capacity bands without invented volume/throughput math;
- temporary overflow episodes;
- physical enforcement of externally owned holds;
- facility demolition, relocation and reuse;
- individual Pokémon work assignments without species-level inference.

## Minecraft/Cobblemon consequence

Binding architecture remains:

`Ouros world/storage state -> explicit encounter composition -> AutoPTU authoritative BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Safe presentation reuse includes warehouse geometry, shelving, racks, bays, crates/containers, doors, lights, signs, barriers, sounds, particles, decorative handling equipment, Pokémon models/forms/poses/animations/cries, NPCs, UI, networking, tracking and persistence hooks.

Adapter work is required for stable facility/zone/slot identity, authoritative state projection, physical-object/world-record binding, reviewed arena conversion and semantic battle playback.

Minecraft/Cobblemon must never decide that:

- inventory is stored because an item entity entered a chest;
- putaway completed because a hopper/conveyor moved an entity;
- a visually empty slot is operationally available;
- a count is authoritative because visible entities match it;
- custody transferred because an entity crossed a dock line;
- quarantine ended because a sign/barrier moved;
- a Pokémon is a worker because it stands near goods;
- native collision/falling blocks/fire/ice apply PTU damage/status;
- every entity in a depot is a combatant;
- Cobblemon BattleState/controller logic owns combatants, legality, HP/status, positions or battle result.

## Readiness conclusion

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

- Which settlements use dedicated warehouses versus back rooms/institutional stores?
- Which regions have refrigerated, secure or other specialized storage?
- Which technologies exist for internal handling and identification?
- Which institutions operate large depots or distribution stores?
- What access/privacy norms apply to stored goods?
- Which historic storage districts have been demolished, relocated or repurposed?
- Which individual Pokémon perform storage work, and what explicit evidence authorizes each task?

## Unresolved mechanical questions

- exact PTU/Caelo support for any proposed lifting/carrying/handling task;
- whether any governing Capability, Move, Ability, Item or Trainer Feature authorizes a specific warehouse action;
- whether any storage equipment is ever a tactical object with rules-bearing HP/state;
- any valid environmental rules for refrigerated or hazardous storage;
- active vehicle/equipment handling if ever needed tactically;
- objective-aware withdrawal/protection policy;
- adapter handling for animated storage equipment without giving Minecraft tactical or inventory authority.

No answer is invented by this snapshot.
