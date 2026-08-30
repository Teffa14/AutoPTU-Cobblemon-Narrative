# Ouros Covert Operation, Infiltration, Access & Extraction Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established canon.

## Purpose

This extension gives Ouros a persistent model for covert operations without creating a universal stealth subsystem.

It connects existing mission, world-agency, antagonist, case, organization, communications, material-culture and travel state so that infiltration stories can preserve preparation, access, cover, exposure, extraction and fallout across multiple scenes.

The core rule is that an operation is a world-state process. AutoPTU only resolves the tactical facts explicitly delegated to BattleSpec.

## 1. Operation identity

```yaml
covert_operation:
  operation_id: null
  status: PLANNING
  sponsor_actor_ids: []
  participant_actor_ids: []
  target_actor_ids: []
  target_organization_ids: []
  target_location_ids: []
  objective_ids: []
  cover_state_ids: []
  access_state_ids: []
  route_knowledge_ids: []
  exposure_event_ids: []
  extraction_plan_ids: []
  evidence_output_ids: []
  battle_contract_ids: []
  chronicle_event_ids: []
  followup_refs: []
```

Candidate states:

- PLANNING
- PREPARED
- ACTIVE
- COMPROMISED
- EXTRACTING
- LOCALLY_COMPLETE
- ABORTED
- FAILED
- CLOSED

Status does not encode success by itself.

## 2. Objectives are independent state

```yaml
operation_objective:
  objective_id: null
  operation_id: null
  owner_actor_ids: []
  objective_type: null
  target_refs: []
  visibility_scope: []
  success_condition_refs: []
  prohibited_outcome_refs: []
  current_state: OPEN
  evidence_refs: []
  result_fact_ids: []
```

Suggested states:

- OPEN
- PARTIALLY_SATISFIED
- SATISFIED
- FAILED
- ABANDONED
- INVALIDATED
- UNKNOWN

Multiple objectives may conflict.

Example abstract structure:

- learn who controls a site;
- preserve cover with one cell;
- avoid exposing a witness;
- leave with one item instance;
- avoid damaging a public facility.

One operation can satisfy some and fail others.

## 3. Cover state

Cover is an actor-relative claim, not invisibility.

```yaml
cover_state:
  cover_state_id: null
  operation_id: null
  presenting_actor_id: null
  cover_claim_refs: []
  identity_ref: null
  supporting_item_refs: []
  supporting_record_refs: []
  audience_actor_ids: []
  audience_org_ids: []
  known_to_be_false_by: []
  accepted_by: []
  questioned_by: []
  unresolved_for: []
  burned_for: []
  last_update_event_id: null
```

Hard rules:

- cover acceptance is scoped to an observer or organization;
- acceptance can change when new information arrives;
- a uniform, badge or document is evidence supporting a claim, not automatic authority;
- visual disguise never grants tactical invisibility unless an exact governing rule says so;
- narrative cover cannot rewrite a combatant identity inside AutoPTU.

## 4. Access state

```yaml
access_state:
  access_state_id: null
  operation_id: null
  actor_id: null
  scope_refs: []
  access_type: null
  source_ref: null
  granted_by_actor_id: null
  credential_item_ref: null
  valid_from: null
  valid_until: null
  revocation_event_id: null
  current_state: UNKNOWN
```

Candidate access types:

- PUBLIC
- INVITED
- STAFF
- SERVICE
- DELIVERY
- RESEARCH
- EMERGENCY
- CREDENTIAL
- ESCORTED
- PHYSICAL_ROUTE_ONLY
- UNKNOWN

Candidate states:

- UNKNOWN
- CLAIMED
- VERIFIED_VALID
- VERIFIED_INVALID
- REVOKED
- EXPIRED
- DISPUTED

Access is scoped.

`VERIFIED_VALID` for one door or route does not grant access to unrelated systems.

## 5. Route knowledge

```yaml
operation_route_knowledge:
  knowledge_id: null
  actor_ids: []
  location_id: null
  route_ref: null
  learned_event_id: null
  last_verified_event_id: null
  current_confidence: null
  known_constraints: []
  stale_reason_refs: []
```

A route can become stale because:

- doors were changed;
- a facility moved;
- construction altered circulation;
- a faction changed procedures;
- a prior shortcut was sealed;
- a crisis changed access;
- security or staffing state changed.

Knowledge never updates itself from presentation-layer geometry.

## 6. Exposure model

Do not use a single global suspicion meter.

```yaml
exposure_event:
  exposure_event_id: null
  operation_id: null
  observer_actor_ids: []
  observer_org_ids: []
  observed_fact_refs: []
  identification_state: null
  inferred_claim_refs: []
  confidence: null
  communicated_packet_ids: []
  resulting_attention_refs: []
  chronicle_event_id: null
```

Candidate identification states:

- PRESENCE_NOTICED
- APPEARANCE_RECORDED
- ALIAS_ASSOCIATED
- PERSON_IDENTIFIED
- AFFILIATION_SUSPECTED
- AFFILIATION_CONFIRMED
- OBJECTIVE_SUSPECTED
- OBJECTIVE_CONFIRMED

These states are not a ladder that must advance in order.

An observer can identify a person without understanding the objective.

## 7. Alarm and communication

An alarm is a communication event with scope.

```yaml
operation_alert:
  alert_id: null
  source_actor_or_system_ref: null
  trigger_event_id: null
  packet_ref: null
  channel_ref: null
  intended_recipient_refs: []
  delivery_state_refs: []
  acknowledged_by: []
```

Rules:

- `ALARM_TRIGGERED != ALL_HOSTILES_AWARE`;
- Communications owns delivery;
- an offline relay, local runner or disconnected site can produce limited awareness if canon supports that infrastructure state;
- narrative code cannot grant tactical omniscience to AI combatants.

## 8. Preparation ledger

```yaml
operation_preparation:
  preparation_id: null
  operation_id: null
  actor_ids: []
  preparation_type: null
  output_refs: []
  cost_refs: []
  completed_event_id: null
  current_validity: null
```

Candidate preparation outputs:

- route knowledge;
- a legitimate appointment;
- a contact willing to speak;
- a credential already owned or lawfully issued in canon;
- delivery timing;
- equipment staged at an authored location;
- transport availability;
- copied public records;
- a safe rendezvous location;
- medical or evacuation support arranged by an existing institution.

Preparation records what actually happened. It does not retroactively invent resources.

## 9. No universal flashback mechanic

Pass 151 borrows only the design lesson that exhaustive pre-planning is undesirable.

Ouros does not gain a generic flashback currency or retroactive action system.

If a future authored mechanic allows retrospective preparation, it must preserve Chronicle causality and cannot contradict established observations.

## 10. Extraction state

```yaml
extraction_plan:
  extraction_plan_id: null
  operation_id: null
  participant_refs: []
  item_or_evidence_refs: []
  origin_ref: null
  destination_ref: null
  route_refs: []
  transport_refs: []
  preconditions: []
  current_state: PLANNED
  blocking_state_refs: []
  completion_event_id: null
```

Candidate states:

- PLANNED
- AVAILABLE
- DEGRADED
- BLOCKED
- ACTIVE
- COMPLETED
- ABANDONED
- UNKNOWN

Hard boundaries:

- objective possession is not extraction;
- clearing an immediate tactical route is not proof of arrival at destination;
- Travel owns onward movement after BattleSpec;
- missing persons or evidence require their owning systems to establish later state.

## 11. Evidence and provenance

A covert operation may generate evidence against its participants, its targets or neither.

Evidence state must use existing Evidence Graph / Case owners.

Examples:

- camera or observer record where technology exists;
- damaged door;
- missing item instance;
- copied record access trace where authored systems support it;
- witness recollection;
- abandoned equipment with provenance;
- battle aftermath;
- message traffic;
- contradictory staff reports.

No evidence output automatically proves identity or motive.

## 12. Operation fallout

```yaml
operation_fallout:
  fallout_id: null
  operation_id: null
  caused_by_event_ids: []
  actor_attention_changes: []
  access_changes: []
  organization_plan_refs: []
  case_refs: []
  public_memory_refs: []
  communication_refs: []
  physical_site_change_refs: []
  unresolved_questions: []
```

Fallout may include:

- a credential being retired;
- a site changing procedures;
- an organization relocating one operation;
- an internal review;
- a contact refusing future involvement;
- an adversarial actor increasing attention;
- a false public explanation;
- a witness remembering only part of the event;
- a previously unknown branch becoming visible;
- a shortcut being sealed;
- a future operation becoming easier because route knowledge was preserved;
- a future operation becoming harder because the target adapted.

## 13. Covert operation and organization lineage

Never infer that every person encountered inside a hostile site belongs to the same organization.

Record:

- employees;
- contractors;
- guests;
- coerced participants;
- separate branches;
- temporary allies;
- unrelated occupants;
- successor organizations;
- reused facilities.

Organization Lineage owns those identities.

## 14. Covert operation and Antagonist Agency

A target reacts only from knowledge it actually has.

A compromised operation can raise:

- awareness;
- concern;
- priority;
- assigned resources;
- fallback-plan selection.

It cannot make the antagonist magically know the player's full plan.

## 15. Covert operation and cases

A covert mission may intersect an investigation, but it does not create universal law-enforcement authority.

Before generating any premise involving seizure, detention, search authority, protected evidence, warrants, police powers or criminal status, the relevant Ouros institution and mandate must already exist in canon.

## 16. Covert operation and social state

A participant's willingness must come from existing relationship, role, obligation, faction or authored motive state.

A friend does not automatically agree to infiltrate somewhere.

A contact agreeing to introduce the player does not automatically agree to commit further acts.

## 17. Covert operation and Pokémon

Pokémon participation requires explicit role and mechanics review.

Do not assume a species can:

- bypass a lock;
- crawl through any vent;
- become silent;
- disable electronics;
- erase records;
- impersonate another entity;
- carry arbitrary weight;
- scout invisibly;
- teleport through barriers;
- create communications interference.

If an individual Pokémon has an authoritative capability, Move, Ability, Feature interaction or other rule that supports a specific action, cite it and validate implementation before using it mechanically.

## 18. Operation result vocabulary

Useful narrow result facts:

- `IMMEDIATE_ACCESS_ROUTE_CLEAR`
- `IMMEDIATE_EXIT_ROUTE_CLEAR`
- `IMMEDIATE_RECORD_ROOM_APPROACH_CLEAR`
- `TARGET_LOCATION_REACHED`
- `OBSERVATION_WINDOW_CREATED`
- `OBJECTIVE_ITEM_IN_PLAYER_CUSTODY`
- `CONTACT_REACHED_RENDEZVOUS`
- `COVER_BURNED_FOR_ACTOR_SET`
- `ALIAS_LINKED_TO_REAL_IDENTITY_BY_ACTOR_SET`
- `SITE_EVACUATION_STARTED`

Each result requires an owner and evidence.

BattleSpec should normally return only immediate tactical facts, not social or investigative conclusions.

## 19. Tactical encounter contract pattern

A mechanically rich covert encounter must declare:

- explicit combatants;
- explicit static starting geometry;
- exact objective delegated to AutoPTU;
- exact result facts AutoPTU may commit;
- dependencies by permanent capability family;
- semantic actors/items removed from BattleSpec;
- post-battle world-state owner.

## 20. Full/reduced design rule

When a concept requires blocked capabilities, keep the narrative premise and reduce only tactical complexity.

Typical reduction:

Full version:

- active guards choose objective-aware routes;
- alarms change reinforcement behavior;
- doors or zones change during battle;
- allies protect an extractor;
- forced movement can interrupt escape;
- timed withdrawal matters.

Reduced version:

- Ouros resolves alert/arrival state before BattleSpec;
- explicit combatants are fixed;
- geometry is static;
- semantic evidence or noncombatants leave BattleSpec;
- AutoPTU resolves an ordinary legal battle;
- victory may clear one immediate approach or exit;
- extraction and exposure are evaluated afterward by their owning systems.

## 21. Minecraft/Cobblemon/Craftics boundary

Presentation may show already-decided state:

- staff badges;
- locked doors;
- uniforms;
- a loading bay;
- a facility alert light;
- a guard moving according to authored world simulation;
- opened shortcuts;
- a changed site after fallout;
- an alias-specific dialogue surface;
- a cutscene representing an already-resolved extraction.

Presentation must not decide:

- who is a combatant;
- whether cover succeeds;
- whether an NPC believes a claim;
- who receives an alert;
- PTU HP/status/positions;
- tactical legal moves;
- Intercept destination;
- whether an item was mechanically stolen;
- whether evidence proves guilt;
- whether extraction succeeded;
- whether an organization was defeated.

Minecraft pathfinding and Cobblemon battle state remain non-authoritative for AutoPTU tactical truth.

## 22. Canon review checklist

Before promoting a covert concept:

1. Is every organization already established or explicitly proposed?
2. Does the target location exist?
3. Are access systems plausible for that place?
4. Are credentials scoped and provenance-backed?
5. Are participant motives grounded?
6. Are cover claims observer-scoped?
7. Are alarm/communication assumptions supported?
8. Are objectives independently tracked?
9. Are case/legal assumptions established rather than imported?
10. Are Pokémon capabilities sourced?
11. Are BattleSpec combatants explicit?
12. Are tactical dependencies classified?
13. Is a reduced version available when needed?
14. Are extraction and aftermath owned outside BattleSpec?
15. Is research provenance separate from canon?

## 23. Implementation priority

This continuity layer is READY as narrative architecture because it primarily connects existing state owners.

Mechanically rich infiltration battles remain gated by incomplete tactical families. The engine-readiness snapshot for Pass 151 records those dependencies without promoting any category from representative Intercept work.