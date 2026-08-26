# Commercial Services, Storefront Continuity & Local Exchange Extension

Status: Proposed systems design. Not established Ouros canon.

## Purpose

Ouros already has material production, supply routes, markets, staffing, finance, hospitality, settlement state, events and public memory. This extension gives recurring customer-facing service locations enough persistent state to change visibly over time without creating a full business-management simulator.

Use this extension when the important object is the continuing public service surface: a shop, desk, kiosk, studio, repair counter, market stall, service office or another authored commercial venue.

## 1. Commercial service node

```yaml
commercial_service_node:
  service_node_id: null
  location_id: null
  operator_actor_ids: []
  operator_institution_id: null
  workplace_id: null
  public_service_refs: []
  supply_dependency_ids: []
  staffing_dependency_ids: []
  facility_dependency_ids: []
  current_service_state: operating
  public_hours_claim: null
  current_availability: null
  temporary_limitations: []
  regular_customer_cohort_ids: []
  visible_state_refs: []
  history_event_ids: []
  public_memory_refs: []
  canon_refs: []
```

Possible state labels:

- OPERATING
- LIMITED
- SPECIAL_ORDER_ONLY
- TEMPORARILY_CLOSED
- RELOCATING
- RESTORING
- EVENT_MODE
- UNSTAFFED
- SUPPLY_BLOCKED

These are narrative states. They do not define prices, inventory counts or mechanical item legality.

## 2. Service availability record

```yaml
service_availability:
  service_node_id: null
  service_ref: null
  authoritative_mechanics_ref: null
  currently_offered: false
  availability_basis_ids: []
  limitation_reason_ids: []
  effective_from: null
  review_trigger_ids: []
```

The narrative layer may decide whether an authored service is currently available. It may not define the mechanical effect of that service.

## 3. Public stock surface

A storefront may expose coarse stock state without becoming a continuous inventory simulator.

```yaml
public_stock_surface:
  service_node_id: null
  mechanical_item_group_refs: []
  availability_band: normal
  shortage_reason_ids: []
  surplus_reason_ids: []
  special_order_refs: []
  last_authoritative_refresh_event_id: null
```

Candidate bands:

- NORMAL
- LIMITED
- SPECIALTY_AVAILABLE
- EVENT_DEMAND
- DELIVERY_DELAYED
- RESTOCKING
- UNAVAILABLE

Exact item lists, prices, quantities and purchase legality must come from approved PTU/Caelo/AutoPTU data.

## 4. Upstream dependency link

```yaml
commercial_dependency:
  dependency_id: null
  service_node_id: null
  dependency_type: supply|staffing|facility|transport|institution|knowledge|care|communication
  source_ref: null
  state_ref: null
  current_status: satisfied
  public_visibility: partial
  failure_effect_refs: []
  substitute_option_refs: []
  recovery_trigger_ids: []
```

A visible shortage should normally have one or more explicit upstream causes.

## 5. Commercial relationship edge

```yaml
commercial_relationship_edge:
  edge_id: null
  actor_or_institution_a: null
  actor_or_institution_b: null
  basis: supplier|operator|customer|landlord_claim|service_partner|competitor_claim|contractor|referral
  shared_event_ids: []
  unresolved_issue_ids: []
  current_operational_effects: []
  legal_status: unknown
  canon_refs: []
```

A recurring transaction does not prove friendship, contract, ownership, debt or legal exclusivity.

## 6. Customer cohorts

```yaml
customer_cohort:
  cohort_id: null
  service_node_id: null
  cohort_basis: local_households|commuters|visitors|workers|students|trainers|event_attendees|other
  estimated_presence_band: normal
  active_time_windows: []
  service_interest_refs: []
  pressure_state: normal
  source_state_ids: []
  materialized_actor_ids: []
```

Only materialize individual customers when one becomes a witness, recurring regular, specialist, rival, contact or another persistent actor.

## 7. Regular customer continuity

```yaml
commercial_regular:
  service_node_id: null
  actor_id: null
  observed_visit_event_ids: []
  known_service_interest_refs: []
  known_promises_or_orders: []
  public_interaction_history: []
  private_relationship_label: none
```

Repeated custom does not infer friendship, loyalty or wealth.

## 8. Service-change event

```yaml
service_change_event:
  service_change_id: null
  service_node_id: null
  previous_state: null
  new_state: null
  cause_event_ids: []
  dependency_change_ids: []
  service_refs_added: []
  service_refs_removed: []
  visible_output_refs: []
  customer_notice_refs: []
  effective_time: null
  followup_review_trigger: null
```

This event is the key bridge between world-state causes and visible Minecraft/service UI changes.

## 9. Storefront revisit ladder

A recurring commercial node can support:

1. BASELINE — player learns who operates the place and what it does.
2. LIMITATION — one or more dependencies become visible.
3. INTERVENTION — players choose whether/how to influence the blocker.
4. STATE CHANGE — service availability changes visibly.
5. CALLBACK — later world state tests whether the change held or created a new consequence.

Routine shopping should compress. A scene should surface only when a decision, relationship, shortage, dispute, unusual order, witness, delivery, staffing issue or larger world consequence makes the visit meaningful.

## 10. Commercial problem

```yaml
commercial_problem:
  problem_id: null
  service_node_id: null
  problem_type: supply|staffing|facility|demand_spike|knowledge_gap|route_disruption|customer_flow|relocation|dispute|other
  observation_refs: []
  cause_claim_ids: []
  confirmed_cause_ids: []
  affected_service_refs: []
  affected_actor_ids: []
  candidate_response_ids: []
  escalation_trigger_ids: []
  status: investigating
```

A commercial problem should not become a random fetch quest by default.

## 11. Supplier mediation case

```yaml
supplier_mediation_case:
  case_id: null
  service_node_id: null
  provider_ids: []
  supplier_or_institution_ids: []
  disputed_or_blocked_service_refs: []
  known_positions: []
  evidence_refs: []
  unresolved_questions: []
  player_authority_basis: none
  status: open
```

The player may be asked to carry information, gather evidence or facilitate contact. The layer must not invent legal authority, compel a supplier or infer a binding contract.

## 12. Service substitution

```yaml
service_substitution_plan:
  affected_service_ref: null
  primary_node_id: null
  alternate_node_ids: []
  temporary_provider_ids: []
  institutional_distribution_refs: []
  delayed_fulfillment_allowed: null
  route_dependencies: []
  current_choice: null
```

This prevents one missing operator from freezing an entire settlement when alternatives logically exist.

## 13. Storefront succession and continuity

```yaml
commercial_succession:
  service_node_id: null
  current_operator_ids: []
  successor_candidate_ids: []
  training_record_ids: []
  institutional_knowledge_refs: []
  unresolved_dependency_ids: []
  transition_state: none
```

Succession uses workplace training/career state. This extension only records the customer-facing continuity consequence.

Possible outcomes:

- same service, new operator;
- reduced service during transition;
- service split between multiple providers;
- relocation;
- temporary closure;
- permanent closure when explicitly authored;
- conversion to another approved use.

## 14. Relocation of a service node

Commercial relocation is separate from residential relocation.

```yaml
commercial_relocation:
  service_node_id: null
  origin_location_id: null
  candidate_location_ids: []
  reason_refs: []
  supply_route_effect_refs: []
  customer_access_effect_refs: []
  staffing_effect_refs: []
  facility_requirement_refs: []
  selected_location_id: null
  status: evaluating
```

A move can alter neighborhood foot traffic, worker routes, supplier access and visual settlement state without inventing rent or property law.

## 15. Demand pulse

```yaml
commercial_demand_pulse:
  pulse_id: null
  source_event_id: null
  affected_service_node_ids: []
  affected_service_refs: []
  pressure_band: elevated
  expected_duration: null
  staffing_response_ids: []
  supply_response_ids: []
  public_notice_ids: []
```

Potential sources already modeled elsewhere:

- tournament;
- festival;
- storm/recovery;
- migration season;
- expedition departure;
- tourism peak;
- settlement construction;
- care crisis;
- transport disruption.

No random demand spike should exist without a world-state cause.

## 16. Commercial memory

A recurring service node can preserve:

- opening and reopening events;
- supplier changes;
- notable shortages;
- staff succession;
- relocation;
- public event participation;
- significant commissions;
- repairs;
- long-running customer relationships;
- changes caused by player decisions.

These facts can support callbacks. They do not create universal reputation points.

## 17. Boundary with existing systems

Use `material-culture-economy-crafting-layer.md` for workshops, item provenance, commissions, supply routes, scarcity and market-level material state.

Use `workplaces-professions-staffing-layer.md` for roles, schedules, training, staffing and career history.

Use `food-agriculture-hospitality-layer.md` when food production, restaurant service, farms or lodging are central.

Use `finance-sponsorship-risk-layer.md` for funding, financial risk, sponsorship and approved economic relationships.

Use `temporary-public-event-operations-extension.md` for event-only vendors and temporary service overlays.

Use `travel-transport-expedition-layer.md` for physical delivery routes and transport services.

Use this extension when a recurring customer-facing service location and its visible continuity are the central state object.

## 18. Minecraft representation

Preferred outputs:

- open/closed/limited signage;
- counter staffing;
- changed displayed stock props;
- added or removed service interaction options;
- empty delivery shelves/crates when a real supply blocker exists;
- restock arrival props;
- special-order notices;
- queue density represented abstractly or with limited cohorts;
- temporary relocation signs;
- successor/trainee placement;
- reopened or repaired interiors;
- callbacks to prior events through decoration/public notices.

Minecraft renders authoritative state. It must not generate legal item stock, prices or service effects independently.

## 19. Encounter contract — Backroom Containment

Narrative premise: a commercial service node closes its public floor after a panicked or hostile Pokémon becomes trapped in a storage/backroom area during a disrupted delivery.

Full version may require:

- narrow-space movement;
- blocked access points;
- movable/fragile storage obstacles;
- protection of stored goods without treating them as combatants;
- forced movement or knockback consequences;
- environmental zones/hazards;
- AI that understands escape or containment goals;
- embodied storefront state in Minecraft.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:
Close and evacuate the public area through narrative state. Fix the tactical map before combat begins. Do not simulate customers, moving crates, destructible stock, dynamic hazards or objective-aware containment. Run only legal combatants. The authoritative result updates whether the service remains closed, reopens in LIMITED state or proceeds to repair/recovery.

## 20. Encounter contract — Delivery Route Interruption

Narrative premise: a scheduled delivery fails because an encounter blocks a known route shortly before the service node would otherwise enter limited stock.

Full version may require route terrain, weather, retreat/escort goals, hazards, forced displacement and objective-aware AI.

Reduced version:
Represent the route blockage as narrative world state. If a battle occurs, instantiate a static legal encounter at a fixed location. Resolve delivery recovery only after the authoritative battle result. Do not have Minecraft invent transport combat rules or PTU escort mechanics.

## 21. Noncombat contract — Supplier Relationship Review

A provider has a recurring availability problem. Players inspect delivery records, talk to operator/supplier actors, compare claims and identify the actual blocker.

This can run now using:

- information packets;
- service history;
- supply route state;
- staffing state;
- public notices;
- material provenance;
- case/evidence records where applicable.

It must not invent legal obligations, prices, debt or coercive authority.

## 22. Procedural hook generator

```yaml
commercial_hook_candidate:
  service_node_id: null
  trigger_state_ids: []
  affected_service_refs: []
  dependency_ids: []
  actor_ids: []
  public_visibility_refs: []
  playable_decisions: []
  likely_outputs: []
  compression_allowed: true
  mechanics_review_required: false
```

Reject the hook when the only purpose is buying an arbitrary amount of material, repeating routine shopping or forcing a closure with no causal world state.

## 23. Promotion questions

Before a service node becomes canon, confirm:

- the settlement and physical location exist;
- the provider/operator exists;
- the service type is compatible with established regional technology and institutions;
- any mechanical item/service references are authoritative;
- supply/staffing dependencies are grounded;
- ownership/legal assumptions have not been invented;
- customer cohorts make sense for the location;
- Minecraft representation is feasible;
- tactical incidents use explicit capability contracts.
