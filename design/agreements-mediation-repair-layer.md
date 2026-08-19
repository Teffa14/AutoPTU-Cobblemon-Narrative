# Ouros Agreements, Mediation & Repair Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models incidents, evidence, custody, factions, social history, civic proposals, finance and public memory. This layer adds a persistent structure for conflicts that parties try to manage through explicit commitments rather than immediate combat, unilateral institutional action or a single social check.

The system does not define a universal legal code. An agreement can be socially meaningful without being legally enforceable. Any enforcement power must come from an authored institution or future canon.

## 1. Core separations

The generator must preserve these distinctions:

- conflict != case;
- complaint != canonical truth;
- conversation != negotiation;
- proposal != acceptance;
- acceptance != friendship or allegiance;
- truce != alliance;
- agreement != legal enforceability;
- nonperformance != bad faith;
- repair != forgiveness;
- restitution != ownership transfer unless ownership state supports it.

## 2. Dispute object

A dispute stores the concrete incompatibility between parties.

```yaml
dispute:
  dispute_id: null
  party_ids: []
  subject_refs: []
  origin_event_ids: []
  claim_ids: []
  confirmed_fact_ids: []
  unresolved_fact_questions: []
  expressed_interests: []
  expressed_constraints: []
  linked_case_ids: []
  linked_civic_proposal_ids: []
  escalation_state: low
  public_visibility: private
  status: ACTIVE
```

A dispute should not require both parties to be equally correct. It only records that their current desired states are incompatible.

Suggested states:
- EMERGING
- ACTIVE
- PAUSED
- NEGOTIATING
- PARTIALLY_RESOLVED
- RESOLVED
- TRANSFORMED
- ENDED_WITHOUT_AGREEMENT

## 3. Negotiation session

A negotiation session records what was actually discussed.

```yaml
negotiation_session:
  session_id: null
  dispute_id: null
  participant_ids: []
  facilitator_ids: []
  location_id: null
  started_at: null
  ended_at: null
  agenda_items: []
  information_shared_ids: []
  evidence_presented_ids: []
  proposal_version_ids: []
  explicit_refusals: []
  unresolved_items: []
  access_state: private
  outcome: null
```

A facilitator does not automatically have authority to decide the outcome.

## 4. Party positions and interests

Positions and interests remain actor-authored or evidence-supported.

```yaml
negotiation_position:
  actor_or_group_id: null
  dispute_id: null
  requested_state: []
  stated_reasons: []
  accepted_constraints: []
  unacceptable_conditions: []
  negotiable_items: []
  source_event_ids: []
```

The system must not invent hidden motives merely to create a compromise.

## 5. Agreement proposal and version history

Every meaningful offer receives a stable version.

```yaml
agreement_proposal:
  proposal_version_id: null
  dispute_id: null
  proposed_by_ids: []
  offered_to_ids: []
  created_at: null
  parent_version_id: null
  commitment_drafts: []
  conditions: []
  duration_or_expiry: null
  verification_routes: []
  unresolved_terms: []
  status: OFFERED
```

Suggested states:
- DRAFT
- OFFERED
- COUNTERED
- WITHDRAWN
- REJECTED
- SUPERSEDED
- ACCEPTED

Old versions remain historical state.

## 6. Agreement object

An accepted agreement freezes the exact accepted version.

```yaml
agreement:
  agreement_id: null
  source_proposal_version_id: null
  party_ids: []
  accepted_at: null
  effective_from: null
  expires_at: null
  commitment_ids: []
  condition_ids: []
  witness_ids: []
  administering_institution_ids: []
  public_summary_id: null
  private_terms: []
  amendment_history: []
  termination_conditions: []
  enforcement_refs: []
  status: ACTIVE
```

Suggested states:
- PENDING_START
- ACTIVE
- PARTIALLY_FULFILLED
- FULFILLED
- RENEGOTIATING
- DISPUTED
- SUSPENDED
- EXPIRED
- WITHDRAWN
- TERMINATED
- SUPERSEDED

`enforcement_refs` may remain empty. An agreement does not gain coercive power merely because it exists in the database.

## 7. Commitments and obligations

Commitments should be observable and testable where possible.

```yaml
agreement_commitment:
  commitment_id: null
  agreement_id: null
  responsible_party_ids: []
  promised_action_or_state: null
  target_refs: []
  trigger_conditions: []
  completion_window: null
  dependencies: []
  verification_evidence_types: []
  privacy: party_only
  status: PENDING
```

Suggested commitment states:
- PENDING
- READY
- IN_PROGRESS
- PERFORMED
- PARTIALLY_PERFORMED
- DELAYED
- IMPOSSIBLE_UNDER_CURRENT_STATE
- DISPUTED
- WAIVED
- REPLACED
- ENDED

A route closure, outage, Injury, weather event or missing resource can explain nonperformance. The system records cause before assigning intent.

## 8. Compliance events

```yaml
compliance_event:
  compliance_event_id: null
  commitment_id: null
  actor_ids: []
  timestamp: null
  event_type: null
  evidence_refs: []
  observed_result: null
  interpretation_claim_ids: []
```

Possible event types:
- PERFORMANCE_RECORDED
- PARTIAL_PERFORMANCE
- DEADLINE_PASSED
- DEPENDENCY_FAILED
- PERFORMANCE_REFUSED
- PERFORMANCE_BLOCKED
- PERFORMANCE_CONTESTED
- TERM_WAIVED
- TERM_AMENDED

The raw event remains separate from claims such as `deliberate breach`.

## 9. Breach claims

```yaml
breach_claim:
  breach_claim_id: null
  agreement_id: null
  commitment_id: null
  claimant_ids: []
  alleged_nonperformance_event_ids: []
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  response_ids: []
  status: UNREVIEWED
```

Suggested states:
- UNREVIEWED
- CONTESTED
- SUPPORTED
- UNSUPPORTED
- WITHDRAWN
- RESOLVED_BY_AMENDMENT
- RESOLVED_BY_REPAIR
- UNRESOLVED

A breach claim must not silently become a crime or faction hostility flag.

## 10. Mediation

```yaml
mediation_record:
  mediation_id: null
  dispute_id: null
  mediator_ids: []
  mediator_mandate_refs: []
  consented_party_ids: []
  conflict_of_interest_records: []
  session_ids: []
  option_sets: []
  resulting_proposal_ids: []
  status: ACTIVE
```

A mediator may:
- help establish shared facts;
- clarify interests;
- preserve proposals;
- identify dependencies;
- separate immediate safety from long-term disagreement;
- help parties draft terms.

A mediator may not impose an outcome unless an authored mandate explicitly permits it.

## 11. Player-character agency

A PC cannot be forced into an enduring social commitment by generated persuasion logic.

For PC-to-PC or NPC-to-PC agreements, acceptance of commitments that control future player behavior must be explicit player input.

The system may record:
- what the PC offered;
- what they accepted;
- what they refused;
- what they later performed;
- what the world believes about the arrangement.

It must not infer:
- friendship;
- forgiveness;
- loyalty;
- romance;
- guilt;
- trust;
- ideological conversion.

Those may exist only when supported by player-authored or canon-authored evidence.

## 12. Social Skill boundary

PTU/Caelo remains authoritative for mechanical social checks.

The narrative layer may identify that a moment could involve Charm, Command, Guile, Intimidate, Intuition or another governed Skill. It must not invent a DC or result.

Even where a Skill Check is valid, a roll should affect an allowed mechanical question such as:
- whether an NPC considers an offer;
- whether information is communicated clearly;
- whether a deception is believed;
- whether access is granted;
- whether tension escalates;
- whether a witness provides cooperation.

A roll cannot create player consent or erase a party's authored material interests.

## 13. Temporary truces and ceasefires

```yaml
ceasefire:
  ceasefire_id: null
  party_ids: []
  scope_location_ids: []
  prohibited_actions: []
  permitted_actions: []
  shared_objective_refs: []
  start_condition: null
  end_condition: null
  communication_route_ids: []
  verification_refs: []
  status: ACTIVE
```

A ceasefire can end normally when its condition is met. Returning to rivalry afterward is not automatically betrayal.

## 14. Repair and restitution plans

Repair should support more than monetary compensation.

```yaml
repair_plan:
  repair_plan_id: null
  dispute_or_case_ids: []
  accepted_by_ids: []
  acknowledged_harm_or_loss_refs: []
  contested_claim_refs: []
  repair_commitment_ids: []
  review_dates: []
  completion_evidence_ids: []
  status: ACTIVE
```

Possible repair forms:
- return an object;
- replace a damaged item where ownership supports it;
- repair infrastructure;
- restore habitat;
- correct a public record;
- publish a correction;
- restore access;
- provide agreed service;
- revise a procedure;
- fund or perform remediation when canon supports the resource relationship;
- create a monitoring/review period.

Repair does not guarantee forgiveness or erase the historical event.

## 15. Agreements involving Pokémon

Human actors can agree to change their own behavior around a Pokémon population, habitat or individual Pokémon.

Examples:
- avoid a nesting site during a defined period;
- stop operating machinery during a migration window;
- return an owned Pokémon where ownership is established;
- fund habitat restoration;
- maintain a quiet corridor.

A wild or nonverbal Pokémon should not become a formal signatory unless a canonically supported communication and consent route exists.

Observed cooperation is recorded as behavior, not contract acceptance.

## 16. Integration with existing layers

Case & Authority:
Cases can produce disputed facts, evidence and institutional handoffs. An agreement may resolve operational conflict without closing every historical question.

Civic Governance:
A civic body may approve or administer an arrangement only when its authored procedure permits it.

Antagonist Agency:
A truce may reduce escalation without changing faction doctrine or allegiance.

Media & Public Memory:
The public summary of an agreement can differ from private terms. Reports of a breach remain claims until verified.

Finance:
Payments may be commitments when canon supports them, but no automatic debt law, interest or penalty exists.

Custody & Material Provenance:
Return or transfer terms must respect existing ownership/custody state.

Conservation:
Seasonal access or restoration arrangements can become explicit commitments among human institutions without pretending wild populations signed them.

Travel & Infrastructure:
Performance may depend on route state, services, maintenance windows or material availability.

## 17. Minecraft presentation

Minecraft/Cobblemon can present agreement consequences through:
- changed access schedules;
- signs and notices;
- guards standing down from a specific corridor;
- returned or relocated objects;
- repaired structures;
- changed shop/service availability;
- faction NPC placement;
- public meeting spaces;
- visible restoration work.

The adapter must never decide whether an agreement was accepted, breached or fulfilled. It renders server-owned state.

## 18. Encounter contract — Relay Station Ceasefire

Premise:
Two hostile groups need a short, explicitly bounded ceasefire so technicians can stabilize a failing communications relay while an external threat approaches.

FULL version:
The tactical map contains members of both groups, a protected work corridor, withdrawal conditions, a third-party threat and objective-aware behavior that preserves the ceasefire unless a verified trigger breaks it.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including interception/forced movement — BLOCKING
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

REDUCED version:
The ceasefire is resolved as world state before combat. The two hostile parties occupy separate physical spaces. If battle occurs, AutoPTU runs one conventional static fight against the external threat. No battle AI is expected to understand truce law, protected corridors or allied-but-not-allied relationships.

## 19. Encounter contract — Waterworks Boundary Agreement

Premise:
Two settlements disagree about access windows to a shared pump complex. A sudden disturbance at the facility creates an immediate need to cooperate without resolving every long-term allocation question.

FULL version:
The battlefield includes an interactable pump, protected work zones, moving participants and objective-aware AI around HOLD_ZONE / PROTECT_OBJECT / ACTIVATE_OBJECT style goals.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage — PARTIAL
- statuses — PARTIAL
- terrain/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal actions — VERIFIED
- tactical AI — BLOCKING
- Minecraft playback/interactables — BLOCKING

REDUCED version:
Parties negotiate access terms and emergency responsibilities outside the grid. A conventional static battle clears the immediate disturbance if needed. Afterward, server world state updates the agreed schedule and commitment records.

## 20. Encounter contract — Restitution at the Market Gate

Premise:
A custody dispute over damaged or missing goods is moving toward a voluntary return/repair arrangement when a separate incident threatens the handoff.

FULL version:
Cargo has tactical location state, actors can intercept or protect its movement, and victory conditions support ESCORT / PROTECT / WITHDRAW rather than defeat-all.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- lifecycle — PARTIAL
- damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when environmental complications are used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics playback — BLOCKING

REDUCED version:
The custody transfer and repair commitments remain outside battle. Cargo never becomes a combat objective. If an encounter occurs, the party clears a chokepoint through a normal battle and then resumes the handoff.

## 21. Promotion rule

An agreement or mediation proposal can move toward canon only after review confirms:
- parties and mandates exist in established world state;
- no PC consent was fabricated;
- ownership/custody assumptions are valid;
- social mechanics do not invent PTU/Caelo rules;
- enforcement power, if any, is explicitly authored;
- obligations can be represented by available server state;
- any battle contract accurately reflects current AutoPTU-Java capabilities.
