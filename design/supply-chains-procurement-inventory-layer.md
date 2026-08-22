# Ouros Supply Chains, Procurement, Inventory & Warehousing Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already knows where materials come from, how workshops transform them, which routes and transport services exist, who staffs institutions, how money is authorized, how parcels move, and how crises change demand. This layer connects those systems through persistent supply state.

Its job is to answer practical world questions:

- What does an institution currently need?
- What stock actually exists?
- Which stock is available rather than merely present?
- Which batch/specification is suitable for the intended use?
- What has been ordered, allocated, shipped, received, inspected or consumed?
- What reserves exist and who may release them?
- Where is the bottleneck?
- Which alternate sources or substitutions are already known?
- Which decisions made earlier make a later shortage easier or harder to survive?

The goal is not a universal ERP, warehouse simulator or shopping economy. Routine healthy supply compresses into background state.

## 1. Authority boundaries

This layer owns:

- demand/request state;
- sourcing/procurement plans;
- source offers and availability claims;
- inventory pools;
- stock reservations and allocation;
- batch/specification compatibility references;
- warehouse/storage state;
- freight consignments not governed as addressed postal items;
- receiving and acceptance state;
- backorders and stockouts;
- substitutions;
- emergency reserves;
- bottleneck/resilience records;
- supply-chain history.

It does not own:

- item mechanics or material provenance -> Material Culture/Crafting;
- mechanical money -> PTU/Caelo/implementation;
- funding/payment state -> Finance;
- route/service feasibility -> Travel/Rail/Maritime/Aerial;
- addressed mail and last-mile letters/parcels -> Postal;
- staff schedules/qualifications -> Workplaces/Credentials;
- technical machine state -> Technology/Infrastructure;
- food-specific production/cultural state -> Food/Agriculture;
- medical diagnosis/treatment -> Care/Health Surveillance;
- crisis clocks -> Crisis;
- criminal/illicit diversion findings -> Cases/Illicit Networks;
- PTU carrying/encumbrance/item-use mechanics -> PTU/Caelo + AutoPTU;
- Minecraft container contents as authority -> never.

## 2. Core separation

Never collapse these states:

```text
NEED
REQUESTED
SOURCED
AUTHORIZED
ALLOCATED
PICKED
SHIPPED
IN_TRANSIT
RECEIVED
INSPECTED
ACCEPTED
AVAILABLE_FOR_USE
CONSUMED_OR_TRANSFORMED
```

A system may intentionally skip some steps for ordinary local goods, but the concepts remain distinct.

Important no-inferences:

```text
physical stock != available stock
available stock != suitable stock
suitable stock != allocated stock
allocated stock != shipped stock
shipped stock != received stock
received stock != accepted stock
accepted stock != consumed stock
purchase approval != payment
payment != delivery
inventory mismatch != theft
shipment delay != sabotage
```

## 3. SUPPLY_CHAIN

Use a persistent chain only when a flow matters repeatedly.

```yaml
supply_chain:
  supply_chain_id: null
  domain_tags: []
  supported_service_ids: []
  source_node_ids: []
  storage_node_ids: []
  distribution_node_ids: []
  consuming_node_ids: []
  material_or_item_refs: []
  active_route_ids: []
  alternate_route_ids: []
  current_bottleneck_ids: []
  resilience_measure_ids: []
  history_event_ids: []
  canon_state: PROPOSED
```

Candidate domains:

- CLINICAL_SUPPLIES
- RESEARCH_MATERIALS
- FOOD_AND_INGREDIENTS
- WORKSHOP_MATERIALS
- SPARE_PARTS
- TRANSPORT_MAINTENANCE
- FESTIVAL_AND_EVENT_SUPPLIES
- EMERGENCY_RELIEF
- NURSERY_SUPPLIES
- CONSERVATION_FIELD_SUPPLIES
- CONSTRUCTION_MATERIALS
- ARCHIVE_AND_MUSEUM_MATERIALS
- EXPEDITION_SUPPLIES

These labels are narrative orchestration only.

## 4. DEMAND_SIGNAL

Demand can exist before anyone creates an order.

```yaml
demand_signal:
  demand_signal_id: null
  requesting_actor_or_institution_id: null
  consuming_location_id: null
  item_or_material_ref: null
  specification_ref: null
  quantity_band: null
  needed_by: null
  priority_claim: null
  reason_event_ids: []
  service_dependency_ids: []
  current_stock_snapshot_id: null
  confidence: null
  status: OBSERVED
```

Suggested states:

- OBSERVED
- FORECAST
- CONFIRMED
- SATISFIED
- PARTIALLY_SATISFIED
- DEFERRED
- CANCELLED
- SUPERSEDED

A demand signal can be wrong or become obsolete.

Examples:

- a clinic sees routine stock trending low;
- a relay needs a specific replacement revision;
- a festival expects a temporary demand spike;
- an expedition requests resupply before entering a remote route;
- a crisis shelter consumes fuel faster than normal.

## 5. PROCUREMENT_REQUEST

A procurement request is a request to source something, not proof of purchase.

```yaml
procurement_request:
  procurement_request_id: null
  demand_signal_ids: []
  requester_id: null
  approving_scope_id: null
  item_or_material_ref: null
  specification_ref: null
  quantity_band: null
  acceptable_substitution_refs: []
  destination_node_id: null
  needed_by: null
  funding_ref: null
  status: DRAFT
  source_offer_ids: []
  allocation_ids: []
  history_event_ids: []
```

Suggested states:

- DRAFT
- SUBMITTED
- UNDER_REVIEW
- APPROVED_TO_SOURCE
- SOURCING
- PARTIALLY_SOURCED
- SOURCED
- ON_HOLD
- CANCELLED
- CLOSED

`APPROVED_TO_SOURCE` is not `PAID`, `SHIPPED` or `RECEIVED`.

## 6. SUPPLY_SOURCE and SOURCE_OFFER

A producer/supplier may have different stock, lead time and compatibility at different moments.

```yaml
supply_source:
  supply_source_id: null
  actor_or_institution_id: null
  location_id: null
  offered_item_refs: []
  authored_capability_refs: []
  current_operational_state_ref: null
  transport_connection_ids: []
  qualification_or_permission_refs: []
  history_event_ids: []
```

```yaml
source_offer:
  source_offer_id: null
  supply_source_id: null
  procurement_request_id: null
  item_or_material_ref: null
  specification_ref: null
  available_quantity_band: null
  earliest_ready_window: null
  condition_claim_ids: []
  funding_or_price_ref: null
  route_assumption_ids: []
  expires_at: null
  status: OFFERED
```

An offer is a claim about availability. It can expire before allocation.

## 7. INVENTORY_POOL

Routine inventory should be aggregate until provenance or individual identity matters.

```yaml
inventory_pool:
  inventory_pool_id: null
  holder_or_institution_id: null
  storage_node_id: null
  item_or_material_ref: null
  specification_ref: null
  total_quantity_band: null
  available_quantity_band: null
  reserved_quantity_band: null
  held_quantity_band: null
  damaged_or_rejected_quantity_band: null
  emergency_reserve_quantity_band: null
  batch_refs: []
  last_count_event_id: null
  last_reconciled_event_id: null
  uncertainty_notes: []
```

Quantity may remain a band when precise simulation adds no value.

Possible bands:

- NONE
- TRACE
- LOW
- NORMAL
- HIGH
- SURPLUS
- UNKNOWN

Exact counts are appropriate when the item is mechanically discrete or player-facing.

## 8. INVENTORY_SNAPSHOT

Inventory observations are versioned.

```yaml
inventory_snapshot:
  inventory_snapshot_id: null
  inventory_pool_id: null
  observed_at: null
  observed_by_ids: []
  observation_method: null
  expected_quantity: null
  observed_quantity: null
  reserved_quantity: null
  held_quantity: null
  discrepancy_state: null
  evidence_ids: []
  supersedes_snapshot_id: null
```

A discrepancy can come from:

- late posting;
- miscount;
- unrecorded legitimate use;
- pending receipt;
- damaged stock;
- transformation into another batch;
- transfer to another storage location;
- data-sync failure;
- theft/diversion only when evidence supports it.

## 9. STOCK_BATCH

Use a specific batch when provenance, condition, compatibility or transformation matters.

```yaml
stock_batch:
  stock_batch_id: null
  material_batch_ref: null
  mechanical_item_ref: null
  source_id: null
  manufacturing_or_harvest_ref: null
  specification_ref: null
  quantity_state: null
  current_storage_node_id: null
  custody_ref: null
  reservation_ids: []
  condition_log_ref: null
  quality_hold_ids: []
  transformation_refs: []
  accepted_use_scope_ids: []
  history_event_ids: []
```

The Material Culture layer remains authority for material provenance and story-significant physical objects. Pass 105 only references that identity.

## 10. SPECIFICATION_REF

Same item name does not guarantee interchangeability.

A specification can represent authored differences such as:

- machine revision compatibility;
- container size;
- research grade versus ordinary material;
- approved food batch category;
- cold-storage requirement;
- regional connector/interface;
- institution-specific standard;
- PTU mechanical item identity where validated.

```yaml
specification_ref:
  specification_id: null
  subject_ref: null
  authored_requirement_ids: []
  compatible_with_refs: []
  incompatible_with_refs: []
  evidence_or_document_refs: []
  mechanical_rule_refs: []
```

Narrative generation must not invent mechanical equivalence between two PTU items.

## 11. STOCK_RESERVATION / ALLOCATION

Stock can be present but unavailable because it is reserved.

```yaml
stock_allocation:
  allocation_id: null
  inventory_pool_or_batch_id: null
  demand_signal_id: null
  consuming_actor_or_institution_id: null
  purpose_id: null
  quantity_state: null
  authorized_by_ref: null
  priority_basis_ref: null
  reserved_at: null
  expires_at: null
  release_event_id: null
  status: RESERVED
```

Suggested states:

- PROPOSED
- RESERVED
- PICKED
- RELEASED_TO_SHIPMENT
- CONSUMED
- RELEASED_BACK_TO_STOCK
- EXPIRED
- CANCELLED

Allocation can create meaningful conflict without making either side villainous.

Example: a clinic may have medicine physically present but reserved for a forecasted outbreak response. A routine case may need an alternate source.

## 12. EMERGENCY_RESERVE

```yaml
emergency_reserve:
  reserve_id: null
  inventory_pool_id: null
  purpose_scope_ids: []
  minimum_hold_state: null
  release_authority_refs: []
  triggering_condition_refs: []
  current_quantity_state: null
  release_event_ids: []
  replenishment_plan_id: null
```

A reserve is not free inventory.

Using it can solve today’s problem while increasing later vulnerability.

## 13. STORAGE_NODE / WAREHOUSE_ZONE

```yaml
storage_node:
  storage_node_id: null
  location_id: null
  operator_ids: []
  storage_type: null
  capacity_state: null
  compatible_item_refs: []
  environmental_requirement_refs: []
  monitoring_asset_ids: []
  security_or_access_refs: []
  current_inventory_pool_ids: []
  backlog_or_congestion_state: null
  technical_dependency_ids: []
  staffing_dependency_ids: []
```

Possible authored types:

- GENERAL_WAREHOUSE
- CLINIC_STORE
- COLD_STORAGE
- WORKSHOP_PARTS_ROOM
- MUSEUM_STORAGE
- EXPEDITION_CACHE
- EMERGENCY_DEPOT
- MARKET_STORAGE
- PORT_OR_RAIL_FREIGHT_STORE
- MOBILE_STOCK_POINT

Storage type does not itself create a mechanical effect.

## 14. STORAGE_CONDITION_LOG

Only use condition tracking for goods that have authored requirements.

```yaml
storage_condition_log:
  condition_log_id: null
  storage_node_or_consignment_id: null
  requirement_ref: null
  observation_ids: []
  excursion_event_ids: []
  monitoring_gap_ids: []
  current_assessment: UNKNOWN
  assessed_by_ids: []
```

Suggested assessments:

- WITHIN_REQUIREMENT
- EXCURSION_OBSERVED
- MONITORING_GAP
- CONDITION_UNKNOWN
- REQUIRES_REVIEW
- REJECTED_FOR_INTENDED_USE

Visual frost, particles or a powered refrigerator in Minecraft cannot establish `WITHIN_REQUIREMENT`.

## 15. FREIGHT_CONSIGNMENT

Use this for bulk/institutional freight. Addressed postal items remain under the Postal layer.

```yaml
freight_consignment:
  consignment_id: null
  shipper_id: null
  intended_receiver_id: null
  origin_node_id: null
  destination_node_id: null
  inventory_or_batch_refs: []
  allocation_ids: []
  expected_quantity_state: null
  transport_leg_ids: []
  condition_log_ref: null
  custody_event_ids: []
  departure_event_id: null
  arrival_event_id: null
  receiving_event_id: null
  status: PLANNED
```

Suggested states:

- PLANNED
- READY
- PICKED
- DEPARTED
- IN_TRANSIT
- HELD
- DELAYED
- REROUTED
- ARRIVED
- PARTIALLY_ARRIVED
- RECEIVED
- CANCELLED
- LOST_CLAIMED
- RECOVERED

`ARRIVED` means the freight reached the destination site. `RECEIVED` means a receiving process actually accepted custody of what was delivered.

## 16. TRANSPORT_LEG handoff

The Travel/Rail/Maritime/Aerial layers remain authoritative for route and service feasibility.

Pass 105 stores only the supply-chain meaning of the leg:

```yaml
supply_transport_leg:
  supply_leg_id: null
  consignment_id: null
  transport_service_ref: null
  connection_ref: null
  planned_departure: null
  actual_departure: null
  planned_arrival: null
  actual_arrival: null
  custody_from_id: null
  custody_to_id: null
  status: PLANNED
```

If a ferry is cancelled, Travel changes the service state. Pass 105 then recalculates the consignment plan; it does not declare the ferry operational.

## 17. RECEIVING_EVENT

Expected contents and actual contents are distinct.

```yaml
receiving_event:
  receiving_event_id: null
  consignment_id: null
  receiver_id: null
  storage_node_id: null
  received_at: null
  expected_refs: []
  observed_refs: []
  discrepancy_ids: []
  condition_review_ids: []
  accepted_refs: []
  held_refs: []
  rejected_refs: []
  custody_event_id: null
```

A receiving mismatch can trigger reconciliation or a Case if later evidence supports one.

## 18. QUALITY_HOLD / ACCEPTANCE

```yaml
stock_hold:
  hold_id: null
  stock_batch_or_inventory_ref: null
  reason_claim_ids: []
  imposed_by_scope_ref: null
  started_at: null
  review_required: true
  release_or_rejection_event_id: null
  status: HELD
```

A batch on hold is physically present but unavailable for normal use.

The generator must not invent inspection standards or legal authority.

## 19. BACKORDER / STOCKOUT

```yaml
supply_shortage:
  shortage_id: null
  demand_signal_id: null
  affected_item_or_material_ref: null
  affected_service_ids: []
  first_observed_at: null
  current_gap_state: null
  cause_hypothesis_ids: []
  confirmed_cause_ids: []
  alternate_source_ids: []
  substitution_option_ids: []
  expected_recovery_window: null
  status: ACTIVE
```

Suggested gap states:

- LOW_BUFFER
- PARTIAL_SHORTFALL
- STOCKOUT
- WRONG_SPEC_ONLY
- RESERVED_ONLY
- QUALITY_HOLD_ONLY
- ROUTE_BLOCKED
- UNKNOWN

This makes “we are out” much more precise.

## 20. SUBSTITUTION_DECISION

Substitution is a choice, not automatic equivalence.

```yaml
substitution_decision:
  substitution_id: null
  original_requirement_ref: null
  candidate_ref: null
  proposed_by_id: null
  mechanical_validation_ref: null
  technical_compatibility_ref: null
  institutional_acceptance_ref: null
  tradeoff_claim_ids: []
  status: PROPOSED
```

Possible states:

- PROPOSED
- TECHNICALLY_VALID
- MECHANICALLY_VALID
- ACCEPTED_FOR_SCOPE
- REJECTED
- WITHDRAWN

An improvised replacement can solve a narrative infrastructure problem only if the relevant authored system says it is compatible. It cannot replace a PTU item mechanically by analogy.

## 21. BOTTLENECK_RECORD

```yaml
bottleneck_record:
  bottleneck_id: null
  supply_chain_id: null
  affected_flow_ids: []
  bottleneck_type: null
  location_or_node_id: null
  observed_capacity_state: null
  cause_claim_ids: []
  confirmed_dependency_ids: []
  mitigation_ids: []
  current_status: ACTIVE
```

Candidate types:

- PRODUCTION
- STORAGE
- STAFFING
- QUALIFICATION
- TRANSPORT
- FUNDING
- INSPECTION
- SPECIFICATION
- INFORMATION
- ALLOCATION
- TECHNICAL_DEPENDENCY

The bottleneck may be mundane and still produce meaningful consequences.

## 22. RESILIENCE_MEASURE

```yaml
resilience_measure:
  resilience_measure_id: null
  supply_chain_id: null
  measure_type: null
  created_by_event_id: null
  supported_item_refs: []
  activation_condition_refs: []
  capacity_or_scope_state: null
  maintenance_dependency_ids: []
  last_test_event_id: null
  current_readiness: UNKNOWN
```

Candidate measures:

- ALTERNATE_SOURCE
- ALTERNATE_ROUTE
- EMERGENCY_RESERVE
- PREPOSITIONED_STOCK
- MUTUAL_AID
- COMPATIBLE_SUBSTITUTE
- REDUNDANT_STORAGE
- MOBILE_DEPOT
- LOCAL_REPAIR_CAPACITY
- SHARED_SPARE_POOL
- SEASONAL_PREBUILD

A resilience measure can fail if it was never maintained or if the disruption affects multiple dependencies.

## 23. Demand spikes and allocation conflicts

Demand can rise because of:

- crisis;
- festival/tournament;
- migration/tourism;
- weather;
- infrastructure failure;
- outbreak investigation;
- reconstruction;
- research expedition;
- seasonal agriculture;
- new settlement growth.

Allocation conflict should remain explicit.

```yaml
allocation_conflict:
  conflict_id: null
  stock_ref: null
  competing_demand_ids: []
  current_allocation_ids: []
  authority_or_agreement_refs: []
  consequence_claim_ids: []
  decision_event_id: null
```

The generator must not assume that “highest narrative drama” gets priority.

## 24. Multiplayer visibility and privacy

Players should not automatically see every warehouse count, supplier or reserve.

Track:

- public stock notices;
- institution-internal inventory;
- confidential emergency reserves;
- sensitive medical/research batches;
- player-owned stock;
- shared club/guild stock if canon allows it;
- access/permission state.

Knowledge comes through observations, roles, reports or legitimate access.

## 25. Offline advancement

Do not simulate each box moving every minute.

Advance supply at event boundaries:

- production completion;
- scheduled pickup/departure;
- route state change;
- arrival/receiving;
- inventory consumption threshold;
- stockout trigger;
- reserve release;
- demand spike;
- periodic reconciliation.

When a player returns after downtime, summarize the meaningful state deltas.

## 26. Minecraft projection

Minecraft may show:

- crates/pallets as representative props;
- warehouse fullness bands;
- sealed or held areas;
- loading docks;
- cold-room alarms;
- empty shelves;
- convoy vehicles;
- workers;
- posted stock notices;
- emergency depots.

Minecraft must not infer:

- exact inventory from visible crates;
- batch identity from block type;
- compatibility from item appearance;
- acceptance from physical arrival;
- ownership from container location;
- mechanical item availability from decorative stock;
- cold-chain validity from snow/ice particles.

The server projects authoritative supply state into a visual representation.

## 27. Pokémon participation

Pokémon may participate in supply work only through authored or observed roles and, where mechanics matter, validated individual capabilities.

Possible narrative roles:

- carrying within a workplace;
- pulling or moving material;
- temperature monitoring/support;
- scent detection;
- guarding;
- route scouting;
- loading/unloading assistance;
- power support;
- messenger work.

No species stereotype grants:

- carrying capacity;
- Mountable;
- lifting limits;
- Shift speed;
- cargo endurance;
- refrigeration;
- security authority;
- inventory access.

## 28. Cases and illicit diversion

Inventory discrepancies can create a Case, but the evidence chain must remain separate.

Flow:

```text
stock discrepancy
-> reconciliation
-> plausible administrative/operational explanations
-> evidence collection
-> if supported, diversion/theft hypothesis
-> Case / Illicit Network handoff
```

Never reverse this into `missing stock -> smuggling network`.

## 29. Cold storage and care

A care facility can have:

- sufficient medicine count;
- insufficient accepted medicine count;
- adequate stock but insufficient refrigeration capacity;
- accepted stock reserved for emergency use;
- stock requiring specialist review;
- a resupply in transit;
- alternate treatment materials pending PTU/Caelo validation.

Care owns treatment legality. Pass 105 only owns the supply state.

## 30. Workshops and spare parts

A machine failure can request a part that is:

- in stock locally;
- in stock regionally;
- wrong revision;
- allocated elsewhere;
- waiting for transport;
- held for inspection;
- manufacturable locally if a validated recipe exists;
- replaceable by an authored compatible substitute;
- unavailable until a supplier resumes operation.

Technology owns the repair outcome. Material Culture owns physical part provenance. Pass 105 owns sourcing/allocation.

## 31. Food and transformation

Food batches can move through:

```text
farm/fishery/producer
-> aggregation/storage
-> transport
-> market/kitchen
-> transformation into prepared batch/dish
```

When transformation creates a new batch identity, provenance points back to inputs.

Food remains authority for culinary/cultural state and any food-specific quality claims.

## 32. Encounter contract — Regional Depot Chokepoint

Narrative premise:

A depot holds a shipment needed by two settlements. A route disruption creates a temporary chokepoint. The conflict is about clearing access and preserving the shipment, not defeating every actor in the district.

FULL version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if used;
- terrain/weather/hazards/zones/reactions — BLOCKING if loading areas or hazards matter;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for PROTECT_CARGO / CLEAR_ROUTE / WITHDRAW;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:

- cargo and noncombat workers remain outside the battle grid;
- the server freezes a static legal chokepoint arena;
- AutoPTU resolves a conventional encounter;
- after battle, world state decides whether the route is clear and the shipment can resume;
- no escort/interception/cargo-HP mechanics are invented.

## 33. Encounter contract — Cold Storage Alarm

Narrative premise:

A storage facility reports a condition-monitoring problem while staff are also dealing with an unrelated Pokémon disturbance. The players must separate equipment/stock assessment from the actual encounter.

FULL version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING if moving staff/stock matters;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if cold/steam/electrical zones become mechanical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal actions — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED version:

- storage conditions, equipment faults and batch holds resolve in world state;
- no cold damage or Ice/Snow field effect is generated;
- workers leave the tactical area;
- any battle uses a static safe aisle/room;
- stock acceptance is evaluated afterward from monitoring evidence, not from battle outcome.

## 34. Encounter contract — Emergency Convoy Split

Narrative premise:

A convoy carrying relief stock reaches a junction where two communities have legitimate urgent demand and one route becomes unavailable.

FULL version dependencies:

- complete movement/interception/forced movement — BLOCKING for moving convoy objectives;
- terrain/weather/hazards/zones/reactions — BLOCKING if the route event has tactical effects;
- AI tactical policy — BLOCKING for convoy/withdrawal/protection goals;
- adapter/playback — BLOCKING;
- all standard battle families retain their permanent VERIFIED/PARTIAL states.

REDUCED version:

- allocation decision occurs before combat;
- vehicles/cargo do not enter the grid;
- route obstruction is represented by static geometry;
- battle clears or fails to clear the chokepoint;
- remaining stock, rerouting and downstream consequences resolve through supply state.

## 35. Long-term story generation

Supply chains should create durable consequences rather than repeated fetch quests.

Good long arcs include:

- a region gradually building a spare-parts network;
- a clinic system discovering that its main weakness is storage rather than medicine supply;
- two settlements coordinating seasonal reserves;
- a legacy warehouse becoming incompatible with modern transport patterns;
- a supplier recovering after a crisis but demand never returning to the old pattern;
- players investing in resilience during calm years and seeing it matter later.

## 36. Compression policy

Compress when:

- demand is routine;
- stock is healthy;
- source is known;
- funding/authority exists;
- route operates;
- receiving succeeds;
- no provenance or player goal makes the shipment special.

Expand when:

- a choice exists between competing legitimate demands;
- the wrong specification is available;
- a batch is on hold;
- the reserve can be released at a future cost;
- a route disruption changes allocation;
- a substitute needs validation;
- provenance matters;
- the players choose a logistics profession/project;
- evidence suggests a case without proving one.

## 37. PTU/Caelo mechanical guardrails

Pass 105 does not define:

- carrying capacity;
- encumbrance;
- item slots;
- prices;
- inventory maximums;
- Pokémon load limits;
- vehicle cargo mechanics;
- cold/heat damage;
- spoilage timers;
- medicine expiration;
- food freshness bonuses;
- item substitution effects;
- crafting yields;
- warehouse checks;
- procurement Skill DCs;
- bargaining rules;
- mechanical scarcity modifiers;
- battle inventory availability.

Any such behavior needs direct PTU/Caelo evidence and implementation support.

## 38. AutoPTU-Java boundary

AutoPTU-Java should receive a battle-ready projection only.

Possible future handoff:

```yaml
battle_inventory_projection:
  actor_id: null
  validated_mechanical_item_refs: []
  validated_quantity_or_usage_state: []
  source_world_inventory_refs: []
  projection_event_id: null
```

The world inventory remains authoritative outside battle. The projection must never allow Minecraft to create or consume PTU items independently.

## 39. Canon promotion checklist

Before a supply-chain element enters canon, review:

1. Does the source/producer exist in authored world state?
2. Does the destination/service actually depend on this item/material?
3. Is the specification meaningful and supported?
4. Is the route/service real?
5. Are funding/authority assumptions established?
6. Are storage requirements authored rather than invented?
7. Does any Pokémon labor claim require a capability check?
8. Does any mechanical item effect come from PTU/Caelo?
9. Is provenance separated from public belief or allegation?
10. Can the same premise run in a reduced implementation without duplicating missing PTU rules?

## 40. Open design questions

- Which institutions operate regional warehouses or shared depots?
- Does the League run any common procurement, or are institutions independent?
- Which goods deserve precise counts versus qualitative bands?
- Which categories can be substituted and who validates compatibility?
- How are player-owned businesses or clubs allowed to reserve/shared stock?
- How much stock advances offline?
- Which sensitive batches require condition monitoring?
- How are stock corrections reconciled across multiplayer clients?
- How should emergency reserves be presented without exposing every hidden contingency?
- What Minecraft container representation is useful without turning loaded chunks into inventory authority?
- Which PTU/Caelo Features or Skills, if any, govern carrying, logistics, repair sourcing or specialized storage?

Until those questions are answered, the layer remains proposed architecture rather than canon.