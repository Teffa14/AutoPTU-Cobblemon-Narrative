# Ecological delegated-authority and accountability contract

Status: PROPOSED IMPLEMENTATION CONTRACT. No canon effect.
Pass: 277

Purpose

Define how one legitimate Ouros authority may delegate a bounded ecological-management function while preserving the delegator's retained authority, the delegate's exact scope, accountability evidence, expiry/revocation semantics and the separation between governance state and ecological/PTU truth.

Record

```yaml
ECOLOGICAL_DELEGATED_AUTHORITY_V1:
  delegation_id: null
  delegator_authority_ref: null
  delegate_actor_or_body_ref: null
  source_instrument_ref: null
  parent_jurisdiction_ref: null
  delegated_function_classes: []
  geographic_scope_refs: []
  ecological_process_scope_refs: []
  affected_action_classes: []
  effective_from_ref: null
  expiry_or_review_horizon_ref: null
  renewal_required: true
  retained_authority_refs: []
  reserved_decision_refs: []
  implementation_permissions: []
  subdelegation_policy: PROHIBITED_UNLESS_EXPLICIT
  approved_subdelegate_refs: []
  reporting_obligations: []
  evidence_obligations: []
  monitoring_obligations: []
  resource_or_capacity_commitments: []
  audit_or_review_refs: []
  corrective_action_refs: []
  suspension_conditions: []
  revocation_conditions: []
  termination_conditions: []
  linked_agreement_refs: []
  linked_joint_jurisdiction_refs: []
  status: PROPOSED
  provenance_refs: []
  canon_status: proposed
```

Accountability observation

```yaml
DELEGATION_ACCOUNTABILITY_OBSERVATION_V1:
  observation_id: null
  delegation_ref: null
  obligation_ref: null
  semantic_window_ref: null
  evidence_refs: []
  observed_performance: null
  ecological_outcome_refs: []
  process_compliance: UNKNOWN
  capacity_constraint_refs: []
  interpretation_refs: []
  disposition: REVIEW_PENDING
```

Delegation states

`PROPOSED`: an authored delegation is being considered but has no active authority effect.

`ACTIVE_WITH_OBLIGATIONS`: the delegated functions are active inside the authored scope and reporting/review duties remain live.

`ACTIVE_REVIEW_DUE`: authority remains active but a semantic review horizon or required oversight event has arrived.

`CORRECTIVE_ACTION_REQUIRED`: evidence shows a defined process or performance deficiency and the authored framework permits correction before stronger action.

`SUSPENDED_PENDING_REVIEW`: future use of some or all delegated functions is paused while review occurs.

`PARTIALLY_REVOKED`: one or more function/action scopes have been removed while others remain active.

`REVOKED`: future use of the delegation is no longer authorized.

`EXPIRED`: the authored term ended without valid renewal.

`COMPLETED`: a one-shot delegated assignment completed and carries no continuing authority.

`SUPERSEDED`: a later valid instrument replaced this one while history remains preserved.

Hard invariants

`DELEGATED_FUNCTION != JURISDICTION_TRANSFER`

`DELEGATED_AUTHORITY != OWNERSHIP`

`DELEGATE_CAPABILITY != DELEGATE_AUTHORITY`

`AUTHORITY != IMPLEMENTATION_CAPACITY`

`REPEATED_PERFORMANCE != PERMANENT_MANDATE`

`REPEATED_RENEWAL != PERMANENT_MANDATE`

`EXPIRY != AUTOMATIC_RENEWAL`

`TASK_COMPLETION != AUTHORITY_EXPANSION`

`SUCCESSFUL_ECOLOGICAL_OUTCOME != PROCESS_COMPLIANCE`

`PROCESS_NONCOMPLIANCE != ECOLOGICAL_FAILURE`

`MISSING_REPORT != BAD_FAITH`

`SUBDELEGATION != IMPLIED_PERMISSION`

`REVOCATION != RETROACTIVE_INVALIDATION`

`REVOCATION != ECOLOGICAL_REVERSAL`

`DELEGATOR_OVERSIGHT != DAILY_OPERATION`

`MINECRAFT_ROLEPLAY_SIGNIFIER != AUTHORITY_SOURCE`

`RESTART != TERM_EXTENSION`

Creation gate

Before `ACTIVE_WITH_OBLIGATIONS`, require:

- an identified delegator with authority over every delegated function;
- an identified delegate;
- a source instrument or authored decision;
- exact function/action scope;
- geographic and ecological-process scope when relevant;
- effective semantic time;
- expiry or review rule for temporary authority;
- retained/reserved powers;
- explicit subdelegation policy;
- reporting/evidence obligations when accountability depends on them;
- suspension/revocation/termination rules when applicable;
- no unresolved mandate conflict that invalidates the proposed transfer.

A quest, NPC statement, uniform, building, repeated prior assignment, faction reputation or player investment cannot create this record by implication.

Function-scoped delegation

Delegation is granular. An authority may delegate observation but reserve relocation; delegate implementation but reserve approval; delegate routine maintenance but reserve emergency closure; or delegate data collection while retaining interpretation and policy choice.

A record must never promote one authorized function into another merely because both concern the same place or ecological process.

Retained-authority rule

Unless an authored source explicitly says otherwise, delegation does not extinguish the delegator's parent mandate. `retained_authority_refs` records functions that remain with the delegator. This prevents a delegate from being treated as a replacement sovereign simply because it performs day-to-day work.

Subdelegation gate

A delegate may create a subdelegate only when the parent instrument explicitly permits it and the proposed subdelegation stays inside that permission.

Required fields include:

- parent delegation ref;
- authorized subdelegation function classes;
- approved recipient class or named recipient where required;
- inherited obligations;
- narrower-or-equal semantic term;
- no expansion of geographic, ecological-process or action scope.

If these are absent, return `REJECT_UNAUTHORIZED_SUBDELEGATION` and preserve the original delegation unchanged.

Accountability and evidence

Accountability records process and outcome separately.

Process evidence may include required reports, provenance, completion logs, consultation records, observation methodology, spending/resource records where authored, notices, safety checks or review attendance.

Ecological outcome remains owned by ecology contracts. A delegate can comply perfectly while the ecological objective remains uncertain or fails. A useful ecological outcome can occur even when a required report is late or incomplete. Neither state overwrites the other.

Corrective-action ladder

When the instrument permits progressive correction, use the narrowest supported state transition:

`ACTIVE_WITH_OBLIGATIONS -> CORRECTIVE_ACTION_REQUIRED -> ACTIVE_WITH_OBLIGATIONS`

or, if evidence and authority support it:

`CORRECTIVE_ACTION_REQUIRED -> SUSPENDED_PENDING_REVIEW -> PARTIALLY_REVOKED/REVOKED`

Do not infer intent from deficiency alone. Capacity constraints, ambiguous instructions, missing data and external disturbance can be recorded separately.

Expiry and renewal

Semantic time controls the term. Server restart, chunk unload or wall-clock downtime that does not advance authoritative Ouros semantic time cannot extend or shorten a delegation.

Renewal is a new affirmative authorization event. It may preserve the same terms, amend them or be denied. Historical successful assignments can be evidence considered by the decision owner but do not auto-renew the mandate.

A lapsed delegation becomes `EXPIRED`; performance after expiry requires another valid authority source.

Revocation semantics

Revocation controls future authority from its effective semantic point. Earlier actions validly taken under the delegation remain historical facts unless a separate adjudication contract invalidates them for another reason.

Revocation does not undo habitat work, recover a population, reopen a route, remove a sign, reverse relocation or otherwise author ecological/world outcomes. Those changes need their owning contracts.

One-shot assignment profile

A bounded delegated mission may use `COMPLETED` rather than remain as a standing mandate. Completion freezes the assignment history and ends continuing authority unless another instrument exists.

Pokémon-style mission adaptation

The reusable game structure is issuer -> bounded assignment -> eligibility/scope -> evidence of completion -> review/reward/consequence. No external Pokémon organization, proprietary rank ladder, characters, dialogue, economy or plot becomes Ouros content through this contract.

Integration with Pass 276

Pass 276 remains authoritative for determining whether the delegator actually holds the relevant function and whether other authorities must approve or be consulted.

Pass 277 consumes a valid authority map and records a bounded transfer of selected operational functions. It does not resolve mandate conflict on its own.

Integration with agreements/mediation

If delegation terms result from negotiation, reciprocal commitments, compensation, access exchange, cost sharing or dispute repair, link the existing agreements layer. Pass 277 owns delegated authority state, not bargaining.

Reduced encounter profile

Needs persistent Ouros governance state, provenance, semantic horizons, ecological evidence links and Minecraft/Cobblemon presentation. It can run with zero AutoPTU handoff.

Mechanically rich profile

Targeting/footprints/range/LoS applies to tactical detection/selection. Base movement legality covers ordinary traversal. Push/pull/knockback/interception/forced movement require complete movement. PTU arithmetic requires core calculations. Structured sequencing uses action economy/initiative and, where phase-spanning, full turn/round lifecycle. Damage-bearing encounters require full stateful damage pipeline. Persistent conditions require status lifecycle. Mechanical protected areas, terrain changes, weather, hazards, zones or reactions require terrain/weather/hazards/zones/reactions. Exact Moves, Abilities, Items and Trainer Features/perks require their verified paths. AI legal-action infrastructure can enumerate legal options; autonomous enforcement/escort/withdrawal policy requires AI tactical policy. Live manifestation requires Minecraft/Cobblemon/Craftics adapter/playback support.

A delegated permit, badge, vest, sign, patrol assignment or mission objective cannot synthesize any of those missing mechanics.

Canon effect

None. No actual Marea/Sendero authority, delegation, steward, player organization, access rule, ecological intervention, reporting duty, appeal system or enforcement power is canonized here.
