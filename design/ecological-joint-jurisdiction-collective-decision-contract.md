# Ecological joint-jurisdiction and collective decision contract

Status: PROPOSED IMPLEMENTATION CONTRACT. No canon effect.
Pass: 276

Purpose

Represent ecological decisions that touch more than one legitimate authority scope without collapsing mandates, objectives, ecological truth or negotiated commitments into one shared flag.

Record

```yaml
ECOLOGICAL_JOINT_JURISDICTION_V1:
  coordination_id: null
  focal_ecological_scope_ref: null
  ecological_evidence_refs: []
  affected_action_class: null
  authority_scope_refs: []
  participating_actor_refs: []
  mandate_records: []
  shared_goal_refs: []
  disputed_goal_refs: []
  decision_owner_refs: []
  consultation_required_refs: []
  notice_required_refs: []
  approval_required_refs: []
  veto_scope_refs: []
  implementation_authority_refs: []
  emergency_authority_refs: []
  delegation_refs: []
  conflict_of_mandate_refs: []
  resource_capacity_notes: []
  proposed_action_ref: null
  collective_disposition: AUTHORITY_MAPPING_PENDING
  semantic_review_horizon_ref: null
  reassessment_conditions: []
  linked_management_decision_refs: []
  linked_agreement_or_mediation_refs: []
  provenance_refs: []
  canon_status: proposed
```

Authority-role record

```yaml
mandate_record:
  mandate_ref: null
  actor_or_body_ref: null
  source_ref: null
  geographic_scope_refs: []
  ecological_process_scope_refs: []
  action_classes: []
  role_by_action_class:
    propose: false
    approve: false
    veto: false
    consult: false
    receive_notice: false
    implement: false
    review: false
  exclusivity: NON_EXCLUSIVE
  delegation_limits: []
  emergency_limits: []
  expiry_or_review_ref: null
  uncertainty_notes: []
```

Collective dispositions

`AUTHORITY_MAPPING_PENDING`: ecological concern exists but affected mandates are not yet sufficiently mapped.

`MULTI_AUTHORITY_REVIEW`: two or more legitimate scopes affect the proposed action and must be evaluated together.

`CONSULTATION_REQUIRED`: one actor can decide within its scope only after consulting another defined participant.

`JOINT_APPROVAL_REQUIRED`: the action cannot proceed under the declared governance model until all required approvals are present.

`SCOPED_VETO_ACTIVE`: an actor has an authored veto over this specific action class and scope. This does not create a universal veto.

`COORDINATED_ACTION_AUTHORIZED`: required approvals/consultations are satisfied and implementation authority is assigned.

`EMERGENCY_ACTION_AUTHORIZED_PENDING_REVIEW`: an authored emergency mandate permits a bounded action before ordinary coordination completes; post-action review remains mandatory.

`MANDATE_CONFLICT_UNRESOLVED`: legitimate mandates produce incompatible requirements and no authorized resolution path has completed.

`CAPACITY_CONSTRAINED`: authority exists but implementation is limited by time, funding, personnel, access or another declared capacity constraint.

`REASSESSMENT_REQUIRED`: ecology, mandate state, action costs or jurisdiction changed enough to reopen coordination.

Hard invariants

`ECOLOGICAL_TRUTH != GOVERNANCE_AUTHORITY`

`SHARED_EVIDENCE != SHARED_OBJECTIVE`

`SHARED_OBJECTIVE != SHARED_MANDATE`

`GEOGRAPHIC_OVERLAP != AUTHORITY_SUPERSESSION`

`ECOLOGICAL_PROCESS_SCOPE != ADMINISTRATIVE_BOUNDARY`

`PARTICIPATION != APPROVAL`

`SILENCE != CONSENT`

`CONSULTATION != VETO`

`VETO_ON_ACTION_A != VETO_ON_ACTION_B`

`EMERGENCY_AUTHORITY != PERMANENT_AUTHORITY_EXPANSION`

`IMPLEMENTATION_CAPACITY != LEGAL_OR_SOCIAL_AUTHORITY`

`COORDINATION_FAILURE != BAD_FAITH`

`PLAYER_INVESTMENT != JURISDICTION`

`MINECRAFT_GATE != PTU_BLOCKER`

`NPC_GUARD != PTU_INTERCEPTION`

`RESTART != REVIEW_HORIZON_ADVANCE`

Scope separation

Every coordination record should distinguish at least three scopes when relevant.

Geographic scope describes where an institution or actor can exercise an authored mandate.

Ecological-process scope describes the habitat, migration route, resource flow, disturbance process, population or interaction that the evidence concerns. This may cross geographic boundaries.

Action scope describes what is proposed: observation, access restriction, habitat work, relocation support, infrastructure operation, warning, capture/removal authorization, emergency response or another authored class.

No one scope silently determines the others.

Authority mapping gate

Before `COORDINATED_ACTION_AUTHORIZED`, the record must identify:

- the proposed action class;
- every known authority scope materially affected by that action;
- the source of each mandate;
- which roles are required for that action class;
- any exclusivity, delegation or emergency limits;
- unresolved mandate conflicts;
- who can actually implement the action;
- review or expiry conditions where the action is temporary.

Unknown jurisdiction should remain explicit. The system must not invent a competent authority merely because a quest needs one.

Collective decision rule

Pass 275 remains authoritative for each actor's evidence use, objectives, risk posture, monitoring value and selected preference.

Pass 276 combines those already-scoped positions only to answer whether an action is authorized across the required mandates.

Two actors may:

- accept the same ecological evidence;
- prefer different actions;
- possess different powers;
- still reach a coordinated action through a shared-goal subset;
- or remain in legitimate unresolved conflict.

No consensus is required unless the authored mandate requires consensus.

Veto rule

A veto must be attached to a source, action class and scope. The presence of a veto does not imply moral correctness, ecological correctness, ownership or authority outside the declared boundary.

`SCOPED_VETO_ACTIVE` must never be promoted from social importance, attendance, seniority, wealth, reputation, battle strength or Minecraft proximity.

Emergency action rule

`EMERGENCY_ACTION_AUTHORIZED_PENDING_REVIEW` requires:

- an authored emergency mandate;
- a triggering condition within that mandate;
- bounded geographic/action scope;
- named implementation authority;
- semantic expiry or review horizon;
- affected authorities recorded even if prior approval is not required;
- no automatic conversion of the temporary action into permanent canon.

Emergency action can change world state when the relevant Ouros authority authorizes it. Ecological outcomes after the action remain controlled by ecology contracts and observation/recovery evidence.

Agreement and mediation integration

This contract does not negotiate terms.

If authorities need reciprocal commitments, concessions, cost sharing, ceasefires, restoration duties, access schedules or mediated terms, create or link records under `design/agreements-mediation-repair-layer.md`.

A successful agreement can satisfy a coordination prerequisite only when its enforcement/authority relationship is actually authored.

Capacity rule

An authorized body may lack implementation capacity. Record that as `CAPACITY_CONSTRAINED` instead of fabricating refusal, negligence or opposition.

Examples include unavailable staff, transport limits, inaccessible terrain, competing emergencies, budget limits or missing monitoring data. These remain governance/logistical state unless another contract gives them ecological or mechanical meaning.

Reduced encounter profile

Needs Ouros persistence, provenance, Pass 275 management-decision records, authority/jurisdiction state, semantic review horizons and Minecraft/Cobblemon presentation. No AutoPTU tactical family is required.

Mechanically rich profile

Targeting/footprints/range/LoS applies to tactical detection or selection. Base movement legality covers ordinary traversal. Push/pull/knockback/interception/forced movement require complete movement. PTU arithmetic requires core calculations. Structured sequencing uses action economy/initiative and full turn/round lifecycle as applicable. Damage-bearing enforcement or wildlife encounters require the full stateful damage pipeline. Persistent conditions require status lifecycle. Mechanical environmental effects require terrain/weather/hazards/zones/reactions. Exact Moves, Abilities, Items and Trainer Features/perks require verified paths. AI legal-action infrastructure can enumerate legal actions. Autonomous tactical enforcement, withdrawal, escort or protected-zone policy requires AI tactical policy. Live representation requires Minecraft/Cobblemon/Craftics adapter/playback support.

A permit, closure, joint order, emergency mandate or veto cannot synthesize missing PTU semantics.

Canon effect

None. No Marea or Sendero institution, jurisdiction, law, communal territory, ownership right, emergency power, access rule, veto, player organization or management outcome is established by this contract.
