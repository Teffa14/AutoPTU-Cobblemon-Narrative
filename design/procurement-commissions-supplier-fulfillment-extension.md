# Ouros Procurement, Commissioning & Supplier Fulfillment Extension

Status: Proposed systems design. Not established canon.

## Purpose

Ouros already knows how money can be authorized, how materials and item instances exist, how workshops produce or repair things, how storefronts expose services, how shipments move, how facilities are maintained, how public projects are approved, how agreements are amended and how workers are staffed.

This extension owns a narrower operational chain:

need identified → sourcing → supplier response → selection → order/commission → fulfillment → receipt → acceptance review → closeout or exception handoff.

Its purpose is to make acquisition and commissioned work persistent and inspectable without creating a universal procurement law, a hidden vendor score, a market simulator or a second ownership/payment system.

## 1. Authority boundary

This layer owns:

- the procurement need;
- sourcing history;
- supplier responses as claims/offers;
- selection provenance;
- order/commission lifecycle references;
- receipt and discrepancy observations;
- acceptance review against an authored specification;
- fulfillment history and exception handoffs.

It does not own:

- money, budgets or payment — Finance;
- mechanical prices or item availability — PTU/Caelo plus approved world data;
- physical item/material identity or crafting — Material Culture;
- customer-facing shop availability — Storefront;
- shipment movement/custody legs — Courier;
- repair/work-order technical completion — Facility Maintenance;
- public project authorization — Civic Governance;
- negotiated commitments, amendment or breach resolution — Agreements/Mediation;
- worker capacity — Staffing;
- qualification/authorization — Credentials;
- ownership law or universal commercial law — undecided canon.

## 2. Procurement need

A procurement episode starts from a documented need rather than a preselected vendor.

```yaml
procurement_need:
  procurement_need_id: null
  requester_actor_or_institution_id: null
  beneficiary_ids: []
  purpose_refs: []
  requested_good_refs: []
  requested_service_refs: []
  specification_id: null
  required_by_window: null
  urgency_claim_refs: []
  funding_authorization_refs: []
  project_or_work_order_refs: []
  source_event_ids: []
  decision_mandate_refs: []
  status: DRAFT
```

Suggested states:

- DRAFT
- IDENTIFIED
- APPROVED_TO_SOURCE
- SOURCING
- RESPONSE_REVIEW
- SELECTED
- ORDERED
- ON_HOLD
- SATISFIED
- CANCELLED
- SUPERSEDED

`APPROVED_TO_SOURCE` means the requester may seek options. It does not prove funds were transferred or that an order has been placed.

## 3. Specification

The system must know what the buyer actually needs before it can judge whether a response satisfies that need.

```yaml
procurement_specification:
  specification_id: null
  need_id: null
  functional_requirement_refs: []
  mechanical_item_or_service_refs: []
  quantity_or_capacity_refs: []
  compatibility_refs: []
  condition_requirements: []
  provenance_requirements: []
  cosmetic_or_cultural_requirements: []
  acceptable_substitution_rules: []
  forbidden_substitution_refs: []
  inspection_or_acceptance_refs: []
  authored_by_ids: []
  approved_by_ids: []
  revision_history: []
```

A specification may be intentionally broad. Do not fabricate exact tolerances, quantities, standards or certification requirements when canon has not established them.

A mechanical item reference cannot be replaced with an invented equivalent merely because the narrative wants a substitute.

## 4. Specification revision

Needs can change after sourcing begins.

```yaml
specification_revision:
  revision_id: null
  specification_id: null
  parent_revision_id: null
  changed_by_ids: []
  changed_at: null
  changed_fields: []
  reason_refs: []
  supplier_notification_refs: []
  effect_on_existing_responses: null
```

A revised specification must not silently rewrite earlier supplier responses. Older offers remain evidence of what was requested at that time.

## 5. Sourcing round

Sourcing records how possible providers were identified and invited or discovered.

```yaml
sourcing_round:
  sourcing_round_id: null
  need_id: null
  specification_revision_id: null
  sourcing_method: null
  candidate_supplier_ids: []
  invitation_or_request_ids: []
  discovery_source_ids: []
  response_ids: []
  response_window: null
  status: OPEN
```

Possible authored sourcing methods include:

- known supplier inquiry;
- open public request;
- invited responses;
- workshop referral;
- emergency direct sourcing;
- storefront inquiry;
- institutional catalog or roster;
- community recommendation.

These are descriptive categories. Ouros does not assume competitive bidding, tender law or mandatory publication.

## 6. Supplier identity and claimed capability

Existing world actors remain the source of supplier identity.

```yaml
supplier_profile_reference:
  supplier_actor_or_institution_id: null
  known_service_refs: []
  known_workshop_ids: []
  known_storefront_ids: []
  known_route_dependencies: []
  credential_refs: []
  prior_fulfillment_episode_ids: []
  public_claim_ids: []
  verified_capability_evidence_ids: []
```

A supplier saying “we can do this” is a claim until the relevant capability, item availability, professional evidence or prior delivery is verified where verification matters.

The profile must not become a hidden quality or morality score.

## 7. Supplier response

```yaml
supplier_response:
  response_id: null
  sourcing_round_id: null
  supplier_id: null
  offered_good_or_service_refs: []
  offered_quantity_or_capacity_refs: []
  proposed_substitution_refs: []
  proposed_material_or_provenance_refs: []
  availability_window: null
  fulfillment_dependency_ids: []
  route_dependency_ids: []
  finance_offer_refs: []
  agreement_term_refs: []
  exception_or_assumption_claims: []
  evidence_refs: []
  valid_until: null
  status: SUBMITTED
```

Suggested states:

- DRAFT
- SUBMITTED
- CLARIFICATION_REQUESTED
- REVISED
- WITHDRAWN
- EXPIRED
- NOT_SELECTED
- SELECTED
- SUPERSEDED

An offered price, if one exists, is a Finance/mechanical reference. This layer does not generate it.

## 8. Clarification and samples

A buyer may need more information before selection.

```yaml
supplier_clarification:
  clarification_id: null
  response_id: null
  requested_by_id: null
  requested_information_refs: []
  sample_item_instance_ids: []
  demonstration_event_ids: []
  answer_claim_ids: []
  received_at: null
```

A sample passing inspection does not prove every later batch is identical.

A demonstration can verify an observed function without proving every hidden specification.

## 9. Selection record

Selection must preserve the actual decision and its evidence.

```yaml
selection_record:
  selection_id: null
  need_id: null
  sourcing_round_id: null
  evaluated_response_ids: []
  authored_criteria_refs: []
  evidence_considered_ids: []
  uncertainty_refs: []
  selected_response_id: null
  nonselected_response_ids: []
  decision_actor_ids: []
  decision_mandate_refs: []
  decision_time: null
  public_summary_id: null
  private_reason_refs: []
```

No universal scoring formula is required.

Possible legitimate authored considerations include:

- actual availability;
- technical compatibility;
- delivery timing;
- provenance requirement;
- existing approved funding limits;
- route feasibility;
- prior observed fulfillment history;
- accessibility or cultural requirements;
- ability to support installation or repair;
- an explicitly approved local/community objective.

The cheapest response is not automatically required or superior.

Selecting the same supplier repeatedly does not prove favoritism.

## 10. Purchase or work order

The selected response becomes an executable commitment only when the appropriate authority creates an order or commission.

```yaml
procurement_order:
  procurement_order_id: null
  need_id: null
  selected_response_id: null
  buyer_id: null
  supplier_id: null
  ordered_output_refs: []
  specification_revision_id: null
  material_culture_commission_refs: []
  agreement_refs: []
  finance_commitment_refs: []
  workshop_or_project_refs: []
  shipment_refs: []
  milestone_refs: []
  acceptance_requirement_refs: []
  authorized_at: null
  status: AUTHORIZED
```

Suggested states:

- AUTHORIZED
- ACKNOWLEDGED
- WAITING_FOR_INPUTS
- IN_PRODUCTION
- IN_SERVICE_WORK
- READY_FOR_TRANSFER
- IN_TRANSIT
- PARTIALLY_FULFILLED
- RECEIVED_PENDING_ACCEPTANCE
- REWORK_REQUIRED
- ACCEPTED
- CANCELLED
- DISPUTED
- CLOSED

The precise state may be projected from Material Culture, Courier or Maintenance rather than duplicated when those systems already own the underlying event.

## 11. Fulfillment episode

```yaml
fulfillment_episode:
  fulfillment_episode_id: null
  order_id: null
  supplier_id: null
  output_refs: []
  production_or_work_event_ids: []
  material_batch_ids: []
  shipment_ids: []
  service_completion_refs: []
  dependency_event_ids: []
  supplier_claim_ids: []
  observed_status: null
```

A delay must have an observable or claimed cause before the generator assigns intent.

Possible causes include:

- input shortage;
- route disruption;
- weather;
- damaged supplier facility;
- staff absence;
- buyer specification revision;
- failed technical check;
- dependency on another supplier;
- buyer-side site not ready;
- unresolved authorization.

Late fulfillment alone does not establish bad faith.

## 12. Receipt

Physical arrival is a separate event.

```yaml
procurement_receipt:
  receipt_id: null
  order_id: null
  shipment_or_handoff_refs: []
  receiving_actor_ids: []
  receiving_location_id: null
  custody_event_refs: []
  item_instance_or_batch_refs: []
  observed_quantity_refs: []
  observed_condition_refs: []
  discrepancy_ids: []
  received_at: null
  status: RECEIVED_PENDING_REVIEW
```

Receipt does not prove:

- ownership transfer;
- specification compliance;
- mechanical compatibility;
- payment completion;
- installation completion;
- facility reopening.

## 13. Discrepancy record

```yaml
procurement_discrepancy:
  discrepancy_id: null
  order_id: null
  receipt_or_work_event_id: null
  discrepancy_type: null
  observation_ids: []
  specification_refs: []
  supplier_response_refs: []
  claimant_ids: []
  supplier_reply_ids: []
  resolution_handoff_refs: []
  status: OPEN
```

Possible authored types:

- quantity mismatch;
- wrong item or version;
- visible damage;
- missing provenance record;
- compatibility uncertainty;
- unapproved substitution;
- incomplete work;
- site not ready for acceptance;
- insufficient evidence.

A discrepancy is not automatically fraud, negligence or breach.

## 14. Acceptance review

Acceptance asks whether the delivered output meets the approved need/specification.

```yaml
acceptance_review:
  acceptance_review_id: null
  order_id: null
  receipt_or_completion_refs: []
  reviewer_ids: []
  reviewer_authorization_refs: []
  specification_revision_id: null
  inspection_or_test_refs: []
  provenance_check_refs: []
  compatibility_check_refs: []
  discrepancy_ids: []
  outcome: null
  reviewed_at: null
  downstream_handoff_refs: []
```

Suggested outcomes:

- ACCEPTED
- PARTIALLY_ACCEPTED
- ACCEPTED_WITH_RECORDED_VARIANCE
- REWORK_REQUIRED
- SUBSTITUTE_REVIEW_REQUIRED
- REJECTED_PENDING_RESOLUTION
- INSUFFICIENT_EVIDENCE

Acceptance itself does not authorize payment unless Finance/agreement state says so.

## 15. Substitution

Substitution is often a useful story choice because supply networks are imperfect.

```yaml
substitution_proposal:
  substitution_id: null
  order_or_response_id: null
  proposed_by_id: null
  original_requirement_refs: []
  substitute_refs: []
  claimed_equivalence_refs: []
  mechanical_validation_refs: []
  provenance_refs: []
  buyer_decision_ref: null
  status: PROPOSED
```

Suggested states:

- PROPOSED
- UNDER_REVIEW
- ACCEPTED
- ACCEPTED_FOR_LIMITED_USE
- REJECTED
- WITHDRAWN

Never assume two mechanical items are interchangeable. If the difference affects PTU behavior, the exact rule/item implementation must support the substitution.

## 16. Supplier relationship history

Stable commercial relationships can remember prior episodes without becoming a hidden reputation stat.

```yaml
supplier_relationship_history:
  buyer_id: null
  supplier_id: null
  procurement_need_ids: []
  response_ids: []
  selected_order_ids: []
  fulfillment_episode_ids: []
  correction_or_rework_ids: []
  dispute_ids: []
  observed_strength_refs: []
  observed_constraint_refs: []
  last_interaction_time: null
```

Safe remembered facts:

- supplied this material before;
- has previously used this route;
- once delivered a partial order during a closure;
- corrected an observed mismatch;
- requires a specialist input;
- normally needs a certain authored lead-time window.

Unsafe inference:

- “trust score 87”;
- “always reliable” from one success;
- “dishonest” from one delay;
- guaranteed future availability.

## 17. Standing and recurring orders

Repeated needs can compress into a recurring arrangement when canon supports it.

```yaml
recurring_procurement_arrangement:
  arrangement_id: null
  buyer_id: null
  supplier_id: null
  repeated_need_refs: []
  specification_refs: []
  cadence_ref: null
  review_trigger_refs: []
  active_order_ids: []
  pause_reason_refs: []
  status: ACTIVE
```

A standing arrangement must be reviewable. It should not create infinite stock or permanent monopoly by implication.

## 18. Emergency sourcing

Crises may require a shortened process.

```yaml
emergency_sourcing_event:
  event_id: null
  source_crisis_or_incident_id: null
  need_id: null
  normal_step_variance_refs: []
  authorizing_actor_ids: []
  authority_refs: []
  selected_supplier_id: null
  later_review_required: true
  end_condition_ref: null
```

Ouros does not assume emergency procurement powers exist. This object is usable only if an authored institution has such authority.

Temporary emergency practice must not silently become the permanent default.

## 19. Integration handoffs

Finance:

- owns budget, amount, commitments, transfers, restricted funds and payment evidence;
- procurement may reference them but cannot modify balances.

Material Culture:

- owns item instances, batches, workshops, commissions, crafting and repair provenance;
- procurement says what was requested/accepted, not how the item mechanically works.

Storefront:

- owns customer-facing availability;
- accepted supply may later cause a storefront state change.

Courier:

- owns shipment legs, custody transfers, delivery attempts and redirects;
- procurement owns the fact that a shipment satisfies an order.

Facility Maintenance:

- owns repair/work-order condition, technical completion, verification and reopening;
- procurement can source a part or contractor, but cannot declare the facility operational.

Civic Governance:

- owns collective decision procedure, mandate and public-project approval;
- procurement does not invent tender rules for civic bodies.

Agreements/Mediation:

- owns explicit negotiated terms, amendments, compliance disputes, breach claims and repair plans;
- procurement discrepancies can hand off there.

Credentials:

- owns qualification and authorization records;
- procurement may require a verified credential only if canon/source procedure establishes that requirement.

Staffing:

- owns personnel availability;
- supplier staffing can be a dependency rather than a procurement-owned state.

## 20. Information and privacy

Supplier responses, internal selection reasons and exact financial terms may be private.

Possible public information:

- a public request for suppliers;
- selected contractor when an institution publishes it;
- visible work or deliveries;
- a public project status;
- an announced delay;
- an accepted donation or sponsorship where disclosure exists.

Do not leak:

- private quotes;
- rejected applications;
- confidential technical details;
- internal budget limits;
- private disputes;
- undisclosed supplier constraints.

Rumor/Media may report claims, but publication does not convert them into procurement truth.

## 21. Minecraft representation

Useful physical projections include:

- a request/specification board at a workshop or institution;
- samples on an inspection table;
- supplier crates tied to real shipment state;
- staging areas that fill or empty as fulfillment progresses;
- visible temporary substitutes;
- an installation area paused while a part is missing;
- an ACCEPTANCE PENDING tag or NPC interaction state;
- rejected/rework goods kept separate from accepted stock;
- a supplier representative visiting a site;
- a completed installation only after the owning technical layer verifies it.

Minecraft should render server-owned state. Moving a crate block must not create acceptance, payment or ownership by itself.

## 22. Routine compression

Compress ordinary procurement when all of these are true:

- need is routine;
- supplier is currently available;
- specification is known;
- funding/authorization is already valid;
- route is functioning;
- no meaningful substitution, scarcity or choice exists;
- receipt/acceptance is routine.

Expand when procurement changes:

- access;
- project timing;
- public services;
- supplier relationships;
- material provenance;
- local production;
- restoration or construction;
- ecological pressure;
- institutional priorities;
- player-facing choices.

## 23. No-inference rules

Do not infer:

- cheapest = required choice;
- most expensive = highest quality;
- repeated selection = corruption;
- nonselection = incompetence;
- late delivery = bad faith;
- missing shipment = theft;
- payment = delivery;
- delivery = acceptance;
- acceptance = payment;
- receipt = ownership;
- sample quality = batch quality;
- supplier claim = verified capability;
- local supplier = culturally preferable unless actors say so;
- emergency purchase = permanent authority;
- rejected substitution = personal conflict;
- public project = universal public bidding;
- invoice/document form = legally binding instrument;
- contract = legally enforceable without authored authority.

## 24. PTU/Caelo boundary

This layer cannot create or alter:

- item prices;
- universal item availability;
- crafting costs;
- recipes;
- prerequisites;
- item effects;
- held-item timing;
- repair bonuses;
- material yields;
- salaries;
- shipping capacities;
- carrying limits;
- Skill DCs;
- vendor negotiation modifiers;
- warranties or penalties;
- mechanical quality grades;
- combat bonuses from supplier history.

Exact mechanical items and services remain governed by PTU/Caelo plus approved implementation/world data.

## 25. AutoPTU boundary

Procurement state normally exists outside battle.

A procurement record may reference a mechanically implemented item. That does not mean the entire Items category is implemented in AutoPTU-Java.

Exact battle-facing item behavior must be verified mechanic by mechanic against the live engine.

Supplier history, selection status, order value, provenance or contract status never grant combat modifiers.

## 26. Encounter contract — Supplier Yard Transfer Under Pressure

Premise:

A completed order is being transferred from a supplier staging yard when an unrelated Pokémon disturbance makes the yard unsafe. The goods are already identified and remain procurement/custody state rather than loot.

FULL version:

- workers and transfer staff withdraw toward safe exits;
- one or more cargo units can change tactical position;
- narrow lanes and stacked materials create meaningful route choices;
- combatants may need to protect a transfer corridor or withdraw;
- damaged/unsafe zones can alter access;
- wild or hostile AI can prioritize escape, territory or obstruction rather than KO;
- Minecraft playback preserves which cargo actually moved and whether the handoff completed.

Capability dependencies:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter and playback — BLOCKING

REDUCED version:

Workers withdraw and cargo is secured outside tactical state before battle instantiation. AutoPTU runs a conventional static battle in a cleared yard section using only verified/basic supported mechanics. After battle, Courier/procurement state resumes the physical transfer. Victory cannot mark the order accepted; receipt and acceptance review still occur separately.

## 27. Encounter contract — Installation Window Interrupted

Premise:

A supplier or specialist crew has arrived during a narrow scheduled installation window. A local disturbance forces the work to pause while the site owner protects people and equipment.

FULL version:

- technicians move toward protected exits;
- an installation zone or equipment bank must remain intact;
- access/safe zones can change during the encounter;
- environmental complications can create hazards or restricted tiles;
- objective-aware AI can prefer CLEAR_ROUTE, PROTECT or WITHDRAW behavior;
- playback preserves which installation stage had actually been reached.

Capability dependencies:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement / interception / forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full lifecycle — PARTIAL
- damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal actions — VERIFIED
- tactical AI — BLOCKING
- Minecraft adapter/playback — BLOCKING

REDUCED version:

Technicians evacuate, the installation is explicitly paused, all dynamic machinery/site controls remain outside battle and AutoPTU resolves a static conventional encounter. Afterward, Facility Maintenance or the owning technical layer determines whether work can resume, procurement tracks fulfillment, and acceptance occurs only after the real verification step.

## 28. Promotion rule

A procurement proposal may move toward canon only when review confirms:

- buyer/requester and supplier are grounded actors/institutions;
- the need follows existing world state rather than a random fetch generator;
- item/service availability is mechanically and geographically plausible;
- no price, legal rule or vendor authority was invented;
- selection criteria have provenance;
- finance, ownership, custody, production, transport and technical verification stay with their owning layers;
- substitutions are mechanically legal where mechanics matter;
- player consent is preserved for PC obligations;
- any battle encounter accurately reflects live AutoPTU capabilities.

## 29. Open canon questions

- Which Ouros institutions regularly source goods or outside work?
- Which use known suppliers, public requests, cooperatives, internal workshops or mixed methods?
- Does any region have formal procurement/tender rules, and for which institutions only?
- What records are public versus private?
- Which supplier credentials or inspections are actually required?
- Are standing orders common anywhere?
- Which emergency sourcing powers, if any, exist?
- What does “local supplier” mean in each region, if actors use that concept at all?
- Which ownership-transfer and acceptance customs are established?
- How are substitutions authorized?
- When does a procurement discrepancy become a negotiated dispute, maintenance issue, case or finance problem?

Until canon answers these, the system stores provenance and choices without inventing law.