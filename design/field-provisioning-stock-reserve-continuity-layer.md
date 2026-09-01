# Field provisioning, stock, reserve, and replenishment continuity layer

Status: PROPOSED DESIGN. No canon facts are created by this file.
Date: 2026-09-01
Pass: 185

## Purpose

This layer gives Ouros a persistent operational model for usable stock, reservation, issue, consumption, return, substitution, replenishment, and shortages. It connects existing custody, access, preparedness, institutional, commerce, communications, and aftermath systems.

Preparedness remains authoritative for which resources are designated in a plan or cache. Custody/provenance remains authoritative for who physically controls an object and how it moved. Shared-resource access remains authoritative for who may take or use restricted resources. Institutional delegation remains authoritative for who may approve allocation. PTU/AutoPTU remains authoritative for mechanical Items and battle effects.

## Core records

### stock_lot

Suggested fields:

- `stock_lot_id`
- `resource_definition_ref`
- `physical_site_id`
- `custodian_role_id`
- `source_ref`
- `received_at`
- `received_quantity`
- `quantity_unit`
- `inspection_state`
- `condition_state`
- `usable_quantity`
- `reserved_quantity`
- `issued_quantity`
- `quarantined_quantity`
- `expiry_or_review_at`
- `provenance_refs`
- `notes`

Do not derive `usable_quantity` blindly from a Minecraft stack count. A received lot may be damaged, reserved, incomplete, quarantined, or unsuitable for a requested purpose.

### provision_request

Suggested fields:

- `request_id`
- `requesting_actor_or_role_id`
- `destination_site_id`
- `purpose_code`
- `requested_resource_ref`
- `requested_quantity`
- `needed_by`
- `priority_basis`
- `acceptable_substitution_constraints`
- `approval_state`
- `allocation_refs`
- `unresolved_constraints`
- `created_at`
- `closed_at`

A request expresses operational demand. It does not reserve stock until an authorized allocation exists.

### stock_allocation

Suggested fields:

- `allocation_id`
- `request_id`
- `stock_lot_ids`
- `allocated_quantity`
- `allocator_role_id`
- `reserved_from`
- `reserved_until`
- `issue_destination`
- `status`: reserved / issued / partially_issued / consumed / returned / cancelled / expired
- `custody_handoff_refs`
- `completion_evidence_refs`

### substitution_decision

Suggested fields:

- `substitution_id`
- `request_id`
- `original_resource_ref`
- `candidate_resource_ref`
- `compatibility_evidence_refs`
- `mechanical_rule_ref_if_any`
- `authorizing_role_id`
- `allowed_scope`
- `limitations`
- `decision_state`: proposed / approved / rejected / uncertain
- `decision_at`

A substitute can be acceptable for one purpose and unacceptable for another. The decision must remain scoped.

### replenishment_event

Suggested fields:

- `replenishment_id`
- `resource_ref`
- `source_ref`
- `destination_site_id`
- `ordered_at`
- `expected_at`
- `arrived_at`
- `received_quantity`
- `inspection_state`
- `accepted_stock_lot_ids`
- `shortage_or_damage_notes`
- `custody_refs`
- `status`

`ORDERED` and `ARRIVED` are distinct. `ARRIVED` and `USABLE` are also distinct.

### field_kit_manifest

Suggested fields:

- `kit_id`
- `kit_type`
- `home_site_id`
- `custodian_role_id`
- `manifest_version`
- `required_resource_refs`
- `optional_resource_refs`
- `current_issue_id`
- `condition_notes`
- `last_checked_at`
- `return_due_at`
- `discrepancy_refs`

A kit is a reusable operational bundle, not a magical equipment slot. Individual contents can remain mundane unless PTU provenance establishes mechanical effects.

## Permanent invariants

`PHYSICAL_STOCK != USABLE_STOCK`

`RECEIVED != INSPECTED`

`INSPECTED != AVAILABLE_FOR_EVERY_PURPOSE`

`REQUESTED != RESERVED`

`RESERVED != AVAILABLE_TO_OTHER_REQUESTS`

`ORDERED != ARRIVED`

`ARRIVED != ACCEPTED`

`STOCKOUT != THEFT`

`SHORT_DELIVERY != SABOTAGE`

`SUBSTITUTE_PRESENT != SUBSTITUTE_COMPATIBLE`

`SUBSTITUTE_COMPATIBLE != SUBSTITUTE_AUTHORIZED`

`KNOWN_CACHE_LOCATION != AUTHORIZED_ACCESS`

`PLAYER_INVENTORY != INSTITUTIONAL_STOCK_LEDGER`

`MINECRAFT_ITEM_STACK != PTU_MECHANICAL_ITEM`

`PTU_ITEM_OWNED != CIVIC_AUTHORITY_TO_ALLOCATE_STOCK`

`BATTLE_VICTORY != RESUPPLY_COMPLETE`

`COBBLEMON_ENTITY_DESPAWN != RESOURCE_CONSUMED`

## Availability projection

Useful UI states are IN_STOCK, LOW, RESERVED, ISSUE_PENDING, OUT_OF_STOCK, RESTOCK_ORDERED, ARRIVED_INSPECTION_PENDING, SUBSTITUTE_UNDER_REVIEW, and UNAVAILABLE_FOR_THIS_PURPOSE.

These are projections of authoritative records. They must not become universal Marea vocabulary unless canon promotes them.

A public board can simplify information while staff retain lot-level detail. Different actors may hold stale copies through the communications/local-knowledge systems.

## Reservation and priority

Priority must have provenance. A high-priority request can be based on a current repair, scheduled fieldwork, preparedness plan, medical/care requirement, or another canon-approved reason. The layer itself creates no universal hierarchy.

Partial allocation is valid. Two requests can both remain open after available stock is divided.

Avoid a single numeric `importance` score when the conflict is between distinct obligations. Preserve who authorized the decision and why.

## Consumption, return, and reconciliation

Issue records should distinguish consumables from reusable assets. A reusable tool can return damaged, incomplete, late, or reassigned. A consumable can be partly used and partly returned when meaningful.

A discrepancy begins as a discrepancy. Investigation may reveal counting error, stale paperwork, damage, authorized drawdown, misplaced custody, spoilage, or theft. Do not choose the dramatic explanation before evidence exists.

## Substitution

Substitution is one of the strongest ordinary-world narrative loops because it exposes practical knowledge.

Examples include recipe ingredients, lamp parts, cart fittings, survey materials, packaging, archival containers, or field supplies. Exact compatibility must come from authored world knowledge or PTU rules when mechanics are involved.

No generic substitution bonus or penalty is created here.

## Autonomous continuity

NPCs can reserve, issue, receive, inspect, consume, return, and replenish stock while the player is elsewhere when their roles and schedules permit it.

The player may return to find a replacement already installed, a promised shipment still delayed, a reserve partly drawn down, or an old request closed by another resident. This supports a world that continues without player observation.

## Minecraft/Cobblemon projection

Useful surfaces include labeled shelves, crates, racks, seal tags, issue boards, kit cases, delivery carts, empty shelf spaces, inspection markers, return bins, NPC carry animations, and dated stock notices.

Minecraft remains presentation. Breaking a crate does not delete the server ledger unless an authorized world verb writes that event. Duplicating a stack cannot create institutional stock. Chunk unload cannot resolve a delivery.

Cobblemon inventory/state may represent PTU battle ownership where the adapter contract explicitly supports it. It does not become the source of truth for Marea storehouse allocation.

## Battle handoff rule

Provisioning authority remains outside AutoPTU. If a resupply or delivery story produces combat, Narrative compiles BattleSpec only for tactical facts already supported by the engine. Cargo, allocation priority, delivery acceptance, inspection, and replenishment status remain world state.

AutoPTU may return narrow immediate physical outcomes. It cannot authorize consumption, complete a delivery ledger, decide who owns a crate, establish compatibility, or refill a cache.

## Mechanically rich reference encounter: Last Crate at Upper Bend

Full intended version: a small resupply movement toward an upper-route work site coincides with wild activity. A carrier and one or more workers need a safe route while a limited crate matters to later repair work. Terrain may constrain movement and an actor may try to protect or clear a corridor. Cargo remains narratively valuable rather than tactical loot.

Capability dependencies:

- targeting/footprints/range/LoS — REQUIRED
- base movement legality — REQUIRED
- complete movement including push/pull/knockback/interception/forced movement — REQUIRED if carrier protection, displacement, collision, interception, partial stops, or forced retreat are tactical
- core calculations — REQUIRED
- action economy/initiative — REQUIRED
- full turn/round lifecycle — REQUIRED
- full stateful damage pipeline — REQUIRED
- status lifecycle — REQUIRED for any selected effect that can create status
- terrain/weather/hazards/zones/reactions — REQUIRED if route conditions, hazards, zones, reactions, or weather affect battle state
- move-specific behavior — REQUIRED and roster-audited
- abilities — REQUIRED and roster-audited
- items — REQUIRED if tactical Items are used; the cargo itself remains outside BattleSpec unless a real PTU item contract explicitly requires otherwise
- Trainer Features/perks — REQUIRED if Trainers use them
- AI legal-action infrastructure — REQUIRED
- AI tactical policy — REQUIRED if actors must understand escort/protection/withdrawal objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — REQUIRED for faithful in-world tactical presentation

Current readiness for the full version: BLOCKED because complete movement and several stateful/content families are partial, while terrain/weather/hazards/zones/reactions, tactical policy, and full adapter/playback remain blocking families.

Reduced executable version: the crate, carrier, workers, route allocation, and custody handoffs remain outside BattleSpec. World state places noncombatants at a safe holding point. If a wild actor prevents further travel, an audited ordinary battle occurs separately on stable terrain with a vetted roster and no unsupported dynamic hazards or escort objective.

Allowed battle handoffs include `IMMEDIATE_PATH_CLEAR` or `IMMEDIATE_WILD_THREAT_WITHDREW`. Narrative then determines whether the shipment advances, whether the lot is damaged, whether the recipient accepts it, and whether the repair request can proceed.

The premise remains the same: a limited resupply matters because of what depends on it later.

## Canon boundary

This layer creates no Marea currency system, ration regime, shortage history, rationing authority, supply law, warehouse policy, standardized kit, item effect, carrying rule, recipe, production quantity, import route, protected reserve, or Caelo logistics doctrine. Site-specific content remains proposed until promoted through canon review.