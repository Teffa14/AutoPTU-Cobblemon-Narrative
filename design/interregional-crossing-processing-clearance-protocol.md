# Interregional Crossing Processing & Scoped Clearance Protocol

Status: PROPOSED SYSTEMS PROTOCOL. Not established Ouros canon.
Date: 2026-08-25

## Purpose

This protocol extends, but does not replace:

- `interregional-mobility-recognition-layer.md`;
- `credentials-permissions-eligibility-layer.md`;
- Travel and transport layers;
- Supply Chains and Postal;
- Biosecurity;
- Pokémon Agency;
- Land Tenure;
- Institutional Review;
- Illicit Networks/Cases.

It models the operational passage of actors, Pokémon, vehicles, parcels, samples and consignments through a bounded processing facility when several existing authorities may need to contribute a decision.

It does **not** establish:

- national borders;
- citizenship;
- passports or visas;
- immigration law;
- customs law;
- tariffs, duties or taxes;
- search/seizure powers;
- detention authority;
- universal police powers;
- extradition;
- a single regional government.

Those concepts require separate authored canon if Ouros ever needs them.

## 1. Authority boundary

The crossing protocol owns process state, not the underlying rule.

```text
arrival
-> processing session
-> information/declaration snapshot
-> required checks identified
-> existing authorities queried
-> optional specialist referral
-> scoped hold if unresolved
-> scoped clearance/release decision
-> physical handoff/onward movement
-> historical record
```

Examples of questions answered elsewhere:

```text
Is this credential valid?                  -> Credentials
Is this actor recognized locally?          -> Interregional Mobility
May they enter this protected site?        -> Credentials + Conservation/Land Tenure
Is this Pokémon transfer authorized?       -> Pokémon Agency + relevant authored authority
Does this population pose biosecurity risk?-> Biosecurity
What is in this freight consignment?        -> Supply Chains / Material Culture / evidence
Is the ferry/train/road operating?          -> Travel / transport layer
Is this addressed parcel in transit?       -> Postal
Is a provenance mismatch suspicious?       -> Cases / Illicit Networks, if evidence supports it
Can a decision be reviewed?                 -> Institutional Review, if canon defines review
```

The processing facility can record and route these questions. It cannot answer them by inventing new rules.

## 2. CROSSING_FACILITY

Use a persistent facility only when passage is recurring or historically meaningful.

```yaml
crossing_facility:
  crossing_facility_id: null
  location_id: null
  facility_kind: LEAGUE_GATE
  connected_region_ids: []
  connected_route_or_service_ids: []
  operator_institution_ids: []
  processing_scope_tags: []
  checkpoint_refs: []
  specialist_desk_refs: []
  storage_or_staging_refs: []
  emergency_route_refs: []
  current_revision_id: null
  history_event_ids: []
  canon_status: PROPOSED
```

Candidate facility kinds are descriptive only:

- LEAGUE_GATE
- EVENT_RECEPTION_GATE
- PROTECTED_AREA_ENTRY
- RESEARCH_TRANSFER_POINT
- FERRY_TERMINAL
- RAIL_TRANSFER_POINT
- ROAD_TRANSFER_POINT
- FREIGHT_DEPOT
- POSTAL_HANDOFF_POINT
- BIOSECURITY_HANDOFF_POINT
- MULTI_SERVICE_GATE
- OTHER_AUTHORED

A facility kind does not imply a legal regime.

## 3. FACILITY_REVISION

A facility can change layout and process without losing identity.

```yaml
facility_revision:
  revision_id: null
  crossing_facility_id: null
  effective_from: null
  effective_until: null
  active_lane_or_desk_ids: []
  route_connections: []
  processing_capabilities: []
  accessibility_refs: []
  outage_fallback_refs: []
  signage_refs: []
  reason_refs: []
  provenance_refs: []
```

A gate rebuilt, consolidated or moved can remain the same historical institution if canon says continuity exists.

## 4. PROCESSING_SESSION

One passage attempt receives one persistent process record.

```yaml
processing_session:
  processing_session_id: null
  crossing_facility_id: null
  session_kind: ACTOR_ENTRY
  actor_ids: []
  pokemon_entity_ids: []
  vehicle_refs: []
  parcel_refs: []
  consignment_refs: []
  sample_refs: []
  arrival_time: null
  requested_onward_scope_refs: []
  declaration_record_ids: []
  required_check_ids: []
  referral_ids: []
  hold_ids: []
  clearance_decision_ids: []
  physical_release_event_id: null
  final_status: IN_PROCESS
  provenance_refs: []
```

Suggested session kinds:

- ACTOR_ENTRY
- GROUP_ENTRY
- EVENT_ADMISSION
- POKEMON_TRANSFER_HANDOFF
- CONSIGNMENT_TRANSFER
- POSTAL_TRANSFER
- RESEARCH_SAMPLE_TRANSFER
- VEHICLE_OR_SERVICE_TRANSFER
- MIXED_SESSION

The session groups process state. It does not merge the identities of its contents.

## 5. DECLARATION_RECORD

A declaration is a statement supplied by an actor, carrier, institution or system.

```yaml
declaration_record:
  declaration_id: null
  processing_session_id: null
  submitted_by_id: null
  submitted_time: null
  declaration_kind: PURPOSE
  declared_values: {}
  source_record_refs: []
  supersedes_declaration_id: null
  signature_or_confirmation_ref: null
  current_status: SUBMITTED
```

Candidate kinds:

- PURPOSE
- PARTY_OR_PASSENGER_LIST
- POKEMON_REFERENCE_LIST
- CARGO_MANIFEST_REFERENCE
- SAMPLE_MANIFEST_REFERENCE
- EVENT_REGISTRATION_REFERENCE
- INVITATION_REFERENCE
- DESTINATION_REFERENCE
- ROUTE_OR_SERVICE_REFERENCE
- OTHER_AUTHORED

Hard rule:

`declaration != world truth`

A mismatch can result from stale data, clerical error, misunderstanding, emergency reroute, changed custody, deliberate falsification or another unresolved cause.

## 6. REQUIRED_CHECK

Checks should reference existing rule authorities.

```yaml
required_check:
  check_id: null
  processing_session_id: null
  check_kind: CREDENTIAL_VALIDATION
  owning_authority_ref: null
  subject_refs: []
  rule_or_permission_ref: null
  requested_scope: null
  requested_time: null
  result_ref: null
  status: PENDING
```

Possible kinds:

- CREDENTIAL_VALIDATION
- LOCAL_RECOGNITION
- ACCESS_PERMISSION
- EVENT_ELIGIBILITY
- POKEMON_CUSTODY_OR_TRANSFER_REVIEW
- BIOSECURITY_REFERRAL
- CONSIGNMENT_IDENTITY
- POSTAL_HANDOFF
- RESEARCH_AUTHORIZATION
- CUSTODY_OR_PROVENANCE_CONFIRMATION
- TRANSPORT_FEASIBILITY
- SPECIALIST_AUTHORED

The protocol must never substitute a locally invented boolean for the owning system’s decision.

## 7. SCREENING_DECISION

Screening determines process routing, not guilt.

```yaml
screening_decision:
  screening_id: null
  processing_session_id: null
  screener_id: null
  considered_record_refs: []
  rule_revision_ref: null
  decision: ROUTINE_PROCESS
  reason_codes: []
  selected_referral_ids: []
  time: null
  provenance_refs: []
```

Suggested outcomes:

- ROUTINE_PROCESS
- ADDITIONAL_INFORMATION_NEEDED
- SPECIALIST_REFERRAL
- RANDOM_OR_ROUTINE_REVIEW
- WAIT_FOR_EXISTING_AUTHORITY
- CANNOT_PROCESS_AT_THIS_FACILITY
- EMERGENCY_FALLBACK

Do not use `SUSPICIOUS` as a generic routing category.

## 8. SPECIALIST_REFERRAL

```yaml
specialist_referral:
  referral_id: null
  processing_session_id: null
  receiving_authority_id: null
  referral_scope: null
  triggering_record_refs: []
  requested_question: null
  sent_time: null
  response_ref: null
  status: OPEN
```

A referral asks another authority a bounded question.

Examples:

- Does this conservation translocation satisfy the existing authorization?
- Is this museum loan’s custody chain sufficient for handoff?
- Can this sample move under the research protocol?
- Does the host institution recognize this competition credential?
- Does the onward ferry still accept this cargo class after an operational change?

A referral does not create an allegation.

## 9. PROCESS_HOLD

```yaml
process_hold:
  hold_id: null
  processing_session_id: null
  held_subject_refs: []
  hold_scope: null
  basis_ref: null
  start_time: null
  expected_review_ref: null
  storage_or_care_ref: null
  responsible_authority_id: null
  release_condition_refs: []
  end_time: null
  status: ACTIVE
```

Candidate scopes:

- DOCUMENTATION_PENDING
- SPECIALIST_DECISION_PENDING
- ONWARD_ROUTE_UNAVAILABLE
- STORAGE_OR_CARE_HANDOFF_PENDING
- EVENT_WINDOW_PENDING
- IDENTITY_OR_RECORD_RECONCILIATION
- EMERGENCY_PAUSE
- OTHER_AUTHORED

The hold must identify exactly what is paused.

A person, Pokémon or consignment should not inherit restrictions placed on another subject unless an authored rule says so.

## 10. CLEARANCE_DECISION

```yaml
clearance_decision:
  clearance_decision_id: null
  processing_session_id: null
  deciding_authority_id: null
  decision_scope: null
  basis_refs: []
  conditions: []
  effective_time: null
  expiry_or_single_use_ref: null
  result: CLEARED_FOR_SCOPE
  review_ref: null
  provenance_refs: []
```

Suggested results:

- CLEARED_FOR_SCOPE
- CLEARED_WITH_CONDITIONS
- PARTIALLY_CLEARED
- PENDING_OTHER_AUTHORITY
- ROUTE_OR_SERVICE_UNAVAILABLE
- NOT_AUTHORIZED_FOR_REQUESTED_SCOPE
- RETURN_OR_REROUTE_REQUIRED
- UNRESOLVED

`NOT_AUTHORIZED_FOR_REQUESTED_SCOPE` does not imply wrongdoing.

A clearance decision also does not guarantee physical passage. Travel may still report a closure, cancellation, full service or environmental restriction.

## 11. PHYSICAL_RELEASE_EVENT

```yaml
physical_release_event:
  release_event_id: null
  processing_session_id: null
  released_subject_refs: []
  released_from_location_id: null
  released_to_route_or_service_ref: null
  custody_handoff_refs: []
  time: null
  observer_or_system_refs: []
  unresolved_exceptions: []
```

Physical release confirms that the relevant subject actually left the processing state.

It does not confirm final delivery or arrival at destination.

## 12. Pokémon-specific safeguards

For any Pokémon referenced in a session:

- preserve `pokemon_entity_id`;
- query Pokémon Agency for ownership/custody/partnership state when relevant;
- retain refusal/withdrawal observations without converting them to disobedience;
- do not treat a Poké Ball as proof that every requested transfer is authorized;
- do not convert a Biosecurity referral into an invasive-species finding;
- do not make a clearance stamp change Loyalty, Friendship, capture eligibility or battle legality;
- do not classify a Pokémon as cargo unless authored canon explicitly defines a specific logistical context while preserving agency.

If a Pokémon cannot or will not continue through the facility, world state records the operational consequence. The battle engine is not used to force passage.

## 13. Cargo, parcels and samples

Crossing Processing should reference persistent objects rather than recreate them.

```text
Supply Chains consignment -> processing session -> required checks/referrals -> physical release -> onward Supply Chain leg
Postal item -> handoff session -> existing postal state -> onward Postal leg
Research sample -> protocol/custody check -> release -> receiving institution
Museum object -> loan/custody/provenance check -> release -> collection handoff
```

The crossing never changes item provenance by itself. It records handoffs that the owning domain can consume.

## 14. Queue and process-load state

Routine bottlenecks can exist without becoming quests.

```yaml
processing_load_snapshot:
  snapshot_id: null
  crossing_facility_id: null
  time: null
  active_lane_or_desk_ids: []
  sessions_waiting_band: null
  specialist_backlog_tags: []
  route_or_service_disruption_refs: []
  emergency_priority_refs: []
  public_information_ref: null
```

Do not simulate every person in line.

Use coarse state unless an event specifically requires individuals.

## 15. Outage and fallback

A facility can lose one subsystem while remaining partially operational.

Possible examples:

- digital credential lookup unavailable but local records still usable;
- one lane closed;
- ferry manifests delayed while passengers continue processing;
- communications down, requiring a manual handoff;
- specialist desk unavailable, causing scoped holds;
- protected-route review paused while ordinary event admission continues.

Fallback must be authored. Do not assume paper records, offline caches or emergency authority exist everywhere.

## 16. Historical revisions and Chronicle

Crossing facilities are good longitudinal locations because the same physical node can accumulate:

- changed recognition rules;
- redesigned layouts;
- new transport connections;
- old signage;
- staff succession;
- Biosecurity procedures learned from earlier events;
- new accessible routes;
- emergency lanes that later become ordinary infrastructure;
- public memories of long queues that no longer occur.

Past decisions remain historically valid for their time even after procedures change.

## 17. Minecraft projection

Allowed presentation:

- gates, desks, lanes, ropes, signs and waiting areas;
- guards/staff as visible representatives;
- containers or vehicles as non-authoritative visual objects;
- current lane/desk closures;
- public queue bands;
- handoff animations;
- route signage.

Forbidden authority:

- redstone state deciding clearance;
- opened gate granting permission;
- broken gate revoking permission;
- defeating an NPC granting passage;
- visible chest contents defining a manifest;
- loaded entities defining party/cargo count;
- item possession alone proving ownership/authorization;
- Minecraft scoreboard becoming the credential authority.

Server-owned world state decides. Minecraft projects the result.

## 18. Explicit no-inferences

Never infer:

```text
checkpoint = national border
regional association = nationality
arrival = admission
admission = recognition of every credential
declaration = truth
screening = suspicion
specialist referral = accusation
hold = guilt
clearance = final delivery
clearance = ownership
permission = battle authority
Pokémon reference = property
credential mismatch = forgery
cargo mismatch = theft
route closure = denied permission
gate open = authorization
gate closed = revocation
battle victory = clearance
staff defeat = institution defeated
```

## 19. Canon-state policy

Everything in this protocol remains `PROPOSED` until a specific Ouros institution, route or rule is authored.

A future canon site can adopt only the subset it needs.

For example:

- a League gate may only check competition eligibility;
- a protected-area trailhead may only check research/access grants;
- a ferry terminal may only coordinate tickets, cargo and Biosecurity handoffs;
- an interregional institution might later gain a richer clearance process if canon establishes it.

Do not create unused bureaucracy merely because the data model can represent it.

## 20. Overworld implementation contracts

Future world-state support should include:

- persistent crossing-facility identity;
- facility revisions;
- processing sessions;
- declaration provenance;
- references to external authority decisions;
- specialist referrals;
- scoped holds;
- clearance decisions;
- physical release/handoff events;
- coarse process load;
- outage/fallback state;
- historical process records.

The protocol should prefer references to existing authoritative records over copying their contents.

## 21. PTU/Caelo boundary

This is an overworld orchestration protocol.

It creates no PTU action, Skill check, Status, Item effect, Trainer Feature, battle zone or movement permission.

If a future crossing scene invokes an exact PTU mechanic, that mechanic must be validated separately against the project’s PTU/Caelo material and current runtime evidence.

No complete Caelo rules corpus for crossing/clearance was available in the inspected project repositories. Super PTU Online Helper was not exposed as an invocable capability in this runtime.