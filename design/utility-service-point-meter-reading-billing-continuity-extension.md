# Ouros Utility Service Point, Meter Reading & Billing Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-29
Research provenance: `research/2026-08-29-utility-service-point-meter-reading-billing-continuity-scan-141.md`

## Purpose

This extension preserves the administrative and evidentiary history between a utility service point, its observation devices, readings or estimates, customer/account relationships, billing records and later corrections.

It does not create a utility engineering simulator, tariff engine, banking system, debt-collection system, legal-regulatory regime or universal assumption that Ouros households use meters.

The intended narrative value is continuity. A meter can be replaced without replacing the service point. A street can be renamed without changing the endpoint. A reading can be estimated without being fraudulent. A bill can later be corrected without deleting the original record. Physical service can be restored while customer-facing records remain unresolved.

## Authority boundary

Electric Grid owns electricity generation, nodes, links, sectors, supply paths and technical verification.

Drinking-Water Continuity owns treatment/distribution and water service endpoints.

Other future utility-specific owners, if canonized, retain their own physical-network authority.

Infrastructure Outage owns multi-service loss, cascades, backup and restoration coordination.

Facility Maintenance owns inspection and repair of physical equipment when applicable.

Technology/Energy owns generic technical assets and faults.

Finance owns money movement, receivables/payables, settlement and narratively significant payment provenance.

Human Identity owns actor continuity, names and identity-record linkage.

Place Reference owns persistent location, address descriptors, entrances and service-point references.

Residential, Commercial Services, Hospitality, Care, Manufacturing and other downstream owners decide what utility availability means to their own operations.

Public Notices/Communications own notices and their delivery.

Request/Dispatch can own field-service requests and crew assignment when such a workflow exists.

This extension owns only:

- stable administrative utility service-point identity;
- account-to-service-point relationships;
- meter/observation-device association history;
- reading provenance;
- estimate provenance;
- reading/data acceptance for a billing period;
- bill-version references and correction lineage;
- administrative disconnect/reconnect request history when canon provides such processes;
- handoffs to physical utility owners and Finance.

## 1. Utility service point

```yaml
utility_service_point:
  utility_service_point_id: null
  utility_kind: authored
  physical_endpoint_ref: null
  place_ref_id: null
  facility_or_structure_ref: null
  physical_utility_owner_ref: null
  administrative_service_owner_ref: null
  current_physical_service_state_ref: null
  current_account_relationship_ids: []
  current_meter_association_ids: []
  historical_meter_association_ids: []
  reading_stream_ids: []
  restriction_or_admin_state_refs: []
  history_event_ids: []
  provenance_refs: []
  canon_status: proposed
```

`utility_service_point_id` is an internal continuity key. It is not automatically a diegetic customer number.

Hard rules:

`SERVICE_POINT_ID != METER_SERIAL`

`SERVICE_POINT_ID != ACCOUNT_NUMBER`

`SERVICE_POINT_ID != STREET_ADDRESS`

`PLACE_RENAMED != SERVICE_POINT_REPLACED`

`METER_REPLACED != SERVICE_POINT_REPLACED`

`ACCOUNT_HOLDER_CHANGED != SERVICE_POINT_REPLACED`

## 2. Physical service state remains external

This layer stores only a reference to the governing physical owner's current state.

```yaml
utility_physical_service_handoff:
  handoff_ref: null
  utility_service_point_id: null
  physical_owner_system: null
  physical_state_ref: null
  observed_or_effective_at: null
  verification_ref: null
  scope_notes: []
```

Examples of owner systems may include Electric Grid or Drinking-Water Continuity. The extension cannot override their truth.

`PHYSICAL_SERVICE_AVAILABLE != ACCOUNT_ACTIVE`

`ACCOUNT_ACTIVE != PHYSICAL_SERVICE_AVAILABLE`

`OUTAGE_RESTORED != BILLING_RECORD_CORRECTED`

`BILLING_RECORD_CORRECTED != PHYSICAL_SERVICE_RESTORED`

## 3. Account relationship

An account relationship records an authored administrative link between an actor/institution and a service point. It does not create ownership, tenancy, residence or debt by itself.

```yaml
utility_account_relationship:
  utility_account_relationship_id: null
  utility_service_point_id: null
  account_record_ref: null
  actor_or_institution_refs: []
  relationship_role: authored
  active_from: null
  active_until: null
  relationship_state: UNKNOWN
  authority_or_agreement_refs: []
  identity_linkage_refs: []
  contact_channel_refs: []
  privacy_scope_ref: null
  predecessor_relationship_ref: null
  successor_relationship_ref: null
  provenance_refs: []
```

Possible descriptive states:

- UNKNOWN
- PENDING
- ACTIVE
- CLOSING
- CLOSED
- DISPUTED
- SUPERSEDED

Possible authored roles may include account holder, institutional payer, property manager, temporary operator or another canon-specific role.

The role vocabulary has no legal meaning unless canon supplies it.

Hard boundaries:

`ACCOUNT_HOLDER != PROPERTY_OWNER`

`ACCOUNT_HOLDER != OCCUPANT`

`ACCOUNT_HOLDER != RESIDENT`

`ACCOUNT_OPEN != SERVICE_USED`

`ACCOUNT_CLOSED != SERVICE_POINT_REMOVED`

`SAME_ADDRESS != SAME_ACCOUNT`

## 4. Meter or observation device

The term `meter` is optional. A region may use another authored observation mechanism or no customer-level measurement at all.

```yaml
utility_observation_device:
  device_id: null
  utility_kind: authored
  technical_asset_ref: null
  device_identifier_ref: protected_or_authored
  device_type: authored
  installed_at: null
  removed_at: null
  device_state_ref: null
  calibration_or_verification_refs: []
  provenance_refs: []
```

Device identity remains separate from service-point association.

## 5. Device-to-service-point association

```yaml
utility_device_association:
  association_id: null
  utility_service_point_id: null
  device_id: null
  association_role: primary|secondary|submeter|temporary|other
  active_from: null
  active_until: null
  installation_event_ref: null
  removal_event_ref: null
  initial_reading_ref: null
  final_reading_ref: null
  association_state: PLANNED|ACTIVE|ENDED|DISPUTED|UNKNOWN
  evidence_refs: []
```

`DEVICE_INSTALLED != ASSOCIATION_VERIFIED`.

`DEVICE_PRESENT_AT_SITE != DEVICE_ASSOCIATED_WITH_THIS_SERVICE_POINT`.

`DEVICE_REMOVED != HISTORICAL_READINGS_DELETED`.

A service point may retain history across several devices.

## 6. Meter exchange / device replacement

```yaml
utility_device_exchange_event:
  exchange_event_id: null
  utility_service_point_id: null
  outgoing_device_id: null
  incoming_device_id: null
  requested_at: null
  performed_at: null
  outgoing_final_observation_ref: null
  incoming_initial_observation_ref: null
  work_order_ref: null
  verification_refs: []
  data_handoff_refs: []
  exception_refs: []
  event_state: PLANNED|PERFORMED|VERIFYING|COMPLETE|DISPUTED|CANCELLED|UNKNOWN
```

A replacement may introduce a legitimate discontinuity in serials, scale representation or data channels. No arithmetic transformation is invented here.

`METER_REPLACED != CONSUMPTION_RESET_TO_ZERO_AS_WORLD_FACT`.

`NEW_DEVICE_INITIAL_READING != PRIOR_DEVICE_FINAL_READING` is not automatically an error because device representations may differ.

The owner process defines valid continuity.

## 7. Reading record

```yaml
utility_reading_record:
  reading_id: null
  utility_service_point_id: null
  device_id: null
  association_id: null
  reading_kind: OBSERVED|REMOTE_OBSERVED|SELF_REPORTED|ESTIMATED|SUBSTITUTED|CORRECTED|OTHER
  observed_or_effective_at: null
  period_ref: null
  raw_value_ref: mechanical_or_external
  unit_ref: authored
  observer_or_source_ref: null
  captured_at: null
  transmitted_at: null
  received_at: null
  accepted_at: null
  acceptance_state: UNREVIEWED|ACCEPTED_FOR_SCOPE|REJECTED|DISPUTED|SUPERSEDED|UNKNOWN
  estimate_method_ref: null
  evidence_refs: []
  supersedes_reading_id: null
  provenance_refs: []
```

The layer stores provenance and references. It does not calculate consumption unless a separate authored implementation supplies exact rules.

Critical separations:

`READING_CAPTURED != READING_RECEIVED`

`READING_RECEIVED != READING_ACCEPTED`

`READING_ACCEPTED != READING_OBSERVED`

`ESTIMATED_READING != OBSERVED_READING`

`SELF_REPORTED_READING != VERIFIED_READING`

`CORRECTED_READING != ORIGINAL_RECORD_DELETED`

## 8. Reading source confidence stays explicit

A reading source may be trusted for one purpose and insufficient for another.

```yaml
utility_reading_evidence_packet:
  evidence_packet_id: null
  reading_id: null
  source_type: field_observation|remote_device|customer_submission|photo|operator_record|derived_estimate|other
  source_ref: null
  captured_at: null
  chain_of_custody_ref: null
  validation_state: UNKNOWN
  limitations: []
  visibility_scope_ref: null
```

A photograph of a display may support what was visible at a time. It does not automatically prove correct device association, calibration or account ownership.

## 9. Estimated-reading episode

```yaml
utility_estimation_episode:
  estimation_episode_id: null
  utility_service_point_id: null
  affected_period_refs: []
  missing_or_unusable_reading_refs: []
  reason_claim_refs: []
  estimate_record_ids: []
  estimate_method_ref: authored
  later_observed_reading_refs: []
  reconciliation_event_refs: []
  status: OPEN|ESTIMATED|AWAITING_ACTUAL|RECONCILED|PARTIALLY_RECONCILED|CLOSED_UNRESOLVED
  provenance_refs: []
```

Reasons remain claims until supported. Candidate narrative reasons can include inaccessible device, device fault, delayed data, temporary communications loss or unknown cause.

Never turn these candidate reasons into universal technical rules.

`ESTIMATE_EXISTS != DEVICE_FAULT`.

`ESTIMATE_EXISTS != ACCESS_REFUSED`.

`ESTIMATE_EXISTS != DECEPTION`.

## 10. Billing period reference

```yaml
utility_billing_period_record:
  billing_period_id: null
  utility_service_point_id: null
  account_relationship_id: null
  period_start: null
  period_end: null
  accepted_reading_refs: []
  estimated_reading_refs: []
  physical_service_state_refs: []
  adjustment_refs: []
  billing_calculation_ref: external_or_authored
  bill_version_ids: []
  current_record_state: OPEN|READY|BILLED|AMENDED|DISPUTED|CLOSED|UNKNOWN
```

`PERIOD_ENDED != READINGS_COMPLETE`.

`READINGS_COMPLETE != BILL_ISSUED`.

`BILL_ISSUED != BILL_SETTLED`.

Finance owns settlement.

## 11. Bill record and version history

This extension may preserve bill provenance while Finance owns monetary movement.

```yaml
utility_bill_record:
  utility_bill_id: null
  utility_service_point_id: null
  account_relationship_id: null
  billing_period_ids: []
  bill_version_ids: []
  current_version_id: null
  finance_receivable_ref: null
  dispute_episode_refs: []
  correction_episode_refs: []
  status: DRAFT|ISSUED|AMENDED|SUPERSEDED|WITHDRAWN|DISPUTED|CLOSED|UNKNOWN
```

```yaml
utility_bill_version:
  bill_version_id: null
  utility_bill_id: null
  issued_at: null
  reading_basis_refs: []
  charge_calculation_ref: external_or_authored
  amount_ref: mechanical_or_finance
  supersedes_version_id: null
  reason_for_version_ref: null
  public_or_customer_copy_ref: null
  evidence_refs: []
```

Old issued versions remain historical artifacts.

`BILL_AMENDED != PRIOR_BILL_NEVER_EXISTED`.

`BILL_AMOUNT_REF != PAYMENT_EVENT`.

`PAYMENT_EVENT != BILL_ACCURACY_VERIFIED`.

## 12. Reconciliation / correction episode

```yaml
utility_record_reconciliation:
  reconciliation_id: null
  utility_service_point_id: null
  affected_reading_ids: []
  affected_period_ids: []
  affected_bill_ids: []
  trigger_ref: null
  issue_claims: []
  new_evidence_refs: []
  findings: []
  corrected_reading_refs: []
  bill_amendment_refs: []
  finance_adjustment_handoff_refs: []
  opened_at: null
  closed_at: null
  outcome: CORRECTED|PARTIALLY_CORRECTED|NO_CHANGE_SUPPORTED|UNRESOLVED|OUTSIDE_SCOPE|UNKNOWN
```

The outcome can remain unresolved.

`DISPUTE_OPENED != CUSTOMER_CORRECT`.

`DISPUTE_OPENED != UTILITY_CORRECT`.

`RECONCILIATION_CLOSED != EVERY_HISTORICAL_RECORD_CERTAIN`.

## 13. Account succession at a persistent place

A service point can outlive occupants, businesses and account holders.

```yaml
utility_account_transition_event:
  transition_id: null
  utility_service_point_id: null
  predecessor_account_relationship_ref: null
  successor_account_relationship_ref: null
  transition_reason: authored
  requested_effective_at: null
  accepted_effective_at: null
  closing_reading_refs: []
  opening_reading_refs: []
  unresolved_record_refs: []
  privacy_boundary_refs: []
  status: PENDING|EFFECTIVE|PARTIAL|DISPUTED|SUPERSEDED|UNKNOWN
```

Critical boundaries:

`NEW_OCCUPANT != PRIOR_ACCOUNT_DEBT_OWNER`.

`NEW_ACCOUNT != NEW_SERVICE_POINT`.

`OLD_ACCOUNT_CLOSED != OLD_RECORDS_PUBLIC`.

`SAME_SERVICE_POINT != SAME_HUMAN_IDENTITY`.

Human Identity and privacy rules determine what records can be linked or disclosed.

## 14. Place/address changes

Place Reference remains authoritative.

```yaml
utility_place_reference_update:
  update_id: null
  utility_service_point_id: null
  prior_place_or_descriptor_ref: null
  successor_place_or_descriptor_ref: null
  effective_at: null
  service_point_identity_continues: true
  downstream_directory_update_refs: []
  evidence_refs: []
```

`ADDRESS_CHANGED != SERVICE_POINT_CHANGED`.

A map, sign, account directory and bill header may update at different times. Historical documents retain the reference used when issued.

## 15. Administrative service restriction or reconnection request

Some canonized utilities may have an administrative process that asks a physical owner to restrict or restore service. This extension can record the request without inventing who has authority or why it is valid.

```yaml
utility_admin_service_action_request:
  action_request_id: null
  utility_service_point_id: null
  requested_action: DISCONNECT|RECONNECT|LIMIT|RESTORE_ADMIN_STATE|OTHER
  requested_by_ref: null
  authority_ref: null
  reason_claim_refs: []
  requested_at: null
  physical_owner_handoff_ref: null
  acknowledgement_ref: null
  execution_ref: null
  verification_ref: null
  status: DRAFT|REQUESTED|ACKNOWLEDGED|EXECUTED|REJECTED|CANCELLED|SUPERSEDED|UNKNOWN
```

Hard rule:

`ADMIN_REQUESTED_DISCONNECT != PHYSICAL_SERVICE_DISCONNECTED`.

`PHYSICAL_SERVICE_DISCONNECTED != DELINQUENCY_PROVEN`.

`PAYMENT_SETTLED != RECONNECTION_EXECUTED`.

`RECONNECTION_EXECUTED != DOWNSTREAM_SERVICE_READY`.

Finance, physical utility owners and downstream service owners each retain their own authority.

## 16. Temporary service points

Markets, festivals, construction sites, field clinics or emergency facilities may use a temporary service point only if canon establishes such infrastructure.

```yaml
utility_temporary_service_point_episode:
  episode_id: null
  utility_service_point_id: null
  supported_activity_or_site_ref: null
  activation_window: null
  physical_connection_ref: null
  device_association_ids: []
  account_relationship_ids: []
  closure_event_ref: null
  post_use_history_refs: []
  state: PLANNED|ACTIVE|ENDED|DECOMMISSIONED|UNKNOWN
```

A temporary point can become a remembered landmark after its technical role ends.

## 17. Public-facing statements are scoped

Statements like “the power came back,” “the meter was fixed,” “the bill was corrected” or “the account is closed” need an owner and timestamp.

Possible legitimate event times include:

- physical service restoration;
- device repair;
- field reading;
- data receipt;
- reading acceptance;
- bill issue;
- bill amendment;
- Finance adjustment;
- administrative account closure.

No single timestamp replaces the others.

## 18. Privacy and disclosure

Utility records can contain actor identity, residence/business relationships, usage patterns or financial references.

This extension stores visibility scope but does not invent privacy law.

```yaml
utility_record_visibility:
  visibility_ref: null
  record_ref: null
  permitted_actor_or_role_refs: []
  permitted_purpose_refs: []
  redaction_refs: []
  authority_ref: null
  effective_window: null
```

`OUROS_INTERNAL_LINKAGE != NPC_KNOWLEDGE`.

`ACCOUNT_RECORD_EXISTS != PUBLIC_RECORD`.

`HISTORICAL_BILL_EXISTS != PLAYER_AUTHORIZED_TO_READ_IT`.

## 19. Mystery design rules

Utility mysteries should prefer chronology, scope and provenance before malice.

Good questions:

- Was this an observed or estimated reading?
- Which device was associated with the service point at that time?
- Did the address change while the service point remained the same?
- Did the account holder change?
- Was data received after the original bill was issued?
- Did physical restoration precede administrative correction?
- Did a temporary connection later become confused with a permanent point?

Bad default conclusions:

- discrepancy means fraud;
- high bill means meter tampering;
- meter replacement means theft;
- old account name proves present residence;
- Electric-type Pokémon presence proves utility cause;
- battle victory proves administrative truth.

## 20. Environmental storytelling

Persistent visual objects can expose history without becoming authoritative state:

- old meter boxes beside replacements;
- service labels carrying former street names;
- blanked-out account windows in archived bills;
- temporary conduits left as sealed infrastructure;
- old utility counters reused as another public service;
- handwritten route maps from field crews;
- inactive cabinets in buildings whose service point moved;
- building renovations around an unchanged endpoint;
- several generations of inspection tags.

Presentation should be derived from authoritative Ouros state where possible.

## 21. Pokémon participation boundary

```yaml
utility_pokemon_role_record:
  pokemon_id: null
  institution_id: null
  authored_role_description: null
  assignment_refs: []
  voluntary_state: unknown
  governing_capability_refs: []
  governing_move_refs: []
  governing_ability_refs: []
  governing_feature_refs: []
  mechanical_validation_state: unresolved
  evidence_refs: []
```

Never infer utility competence from Type, species, Pokédex flavor, animation or proximity.

Electric type does not create generation/metering authority.

Water type does not create water-service authority.

Psychic or Aura capability does not reveal account identity or billing truth.

A Pokémon can participate only as an authored individual with a supported role.

## 22. Minecraft/Cobblemon boundary

Minecraft/Cobblemon may present:

- meters and boxes as props;
- old and new device models;
- cables/pipes as visual infrastructure;
- utility counters;
- field crews;
- temporary barriers;
- service labels;
- NPC schedules;
- Pokémon models, poses, animations and sounds;
- UI showing already-authoritative administrative state;
- persistence/networking hooks.

It does not own service-point identity, readings, billing, account relationships or financial settlement.

A block with a dial does not produce an authoritative reading.

A redstone signal does not prove utility supply.

A chest containing paper does not create a bill.

A scoreboard tag does not become an account number.

An entity UUID does not become a customer identifier.

Cobblemon BattleState/controller logic never selects authoritative combatants, legality, HP/status, tactical positions or utility consequences.

## 23. Encounter concept — Meter Inspection Withdrawal Corridor

Narrative premise:

A utility inspector or field reader is documenting a service-point/device mismatch when an independent territorial or hostile threat enters the service alley. The administrative question remains unresolved while the civilian team withdraws.

FULL intended version:

- staged inspector/crew withdrawal;
- escort/interception around a narrow corridor;
- possible Push/Pull/Knockback interactions around static obstacles;
- generalized reactions;
- reviewed authored terrain/hazard zones only when exact mechanics exist;
- objective-aware AI with PROTECT/WITHDRAW/CLEAR_ROUTE behavior;
- semantic playback of the protected corridor and frozen utility state.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for generalized reactions or any live technical/environmental zone;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Full version status: BLOCKED FOR RICH SEMANTICS.

REDUCED version: READY.

Reduced contract:

1. The inspector records are secured before BattleSpec creation.
2. Inspectors, customers, meters as interactive objects and private account data stay outside the tactical grid.
3. Utility administrative state is frozen.
4. Ouros selects explicit combatants.
5. AutoPTU receives reviewed static alley geometry.
6. Victory may create only `IMMEDIATE_SERVICE_ALLEY_CLEAR`.
7. The utility owner resumes inspection after battle and independently decides any reading/device/account finding.

`TACTICAL_VICTORY != METER_ASSOCIATION_VERIFIED`.

`ALLEY_CLEAR != READING_ACCEPTED`.

## 24. Encounter concept — Reconnection Access Perimeter

Narrative premise:

A physical utility owner has an authorized field task at a service point after the relevant administrative prerequisites were resolved elsewhere. An unrelated threat blocks the safe public approach.

FULL intended version:

- perimeter protection;
- movement around work boundaries;
- escort/withdrawal;
- generalized reactions;
- authored technical/environmental zones only with exact PTU/Caelo contracts;
- objective-aware AI;
- semantic playback.

Reduced version: READY.

Reduced contract:

1. Authority and administrative prerequisites are resolved before combat.
2. Technical equipment and crew remain outside BattleSpec.
3. The physical utility state stays unchanged during battle.
4. Tactical victory may create only `IMMEDIATE_APPROACH_CLEAR`.
5. The physical owner separately performs and verifies any reconnection under its own rules.
6. Downstream owners separately evaluate readiness.

`TACTICAL_VICTORY != SERVICE_RECONNECTED`.

`SERVICE_RECONNECTED != ACCOUNT_CORRECT`.

`SERVICE_RECONNECTED != DOWNSTREAM_OPERATION_RESUMED`.

## 25. Encounter concept — Temporary Service Point Chokepoint

Narrative premise:

A temporary market, festival or relief site has an authored utility endpoint. The endpoint itself is not a combat object, but territorial activity develops on the access route used by staff.

FULL intended version:

- protect/withdraw behavior;
- complete movement and Intercept;
- optional reviewed hazard/weather interaction;
- objective-aware route-clearing AI;
- adapter playback of the service perimeter.

Reduced version: READY.

The temporary service point, meter/device, records and staff remain outside BattleSpec. Victory clears only a nearby static chokepoint. It cannot activate the endpoint, extend its authorized window, change account responsibility, change priority or create utility capacity.

## 26. Exploration concept — The Meter Room With Four Generations

No combat required.

An old mixed-use building contains four layers of utility history: one decommissioned box, one removed-device mount, one current device, and one label referring to a former street name. Archive photos, renovation records and current service-point state allow the player to reconstruct the sequence.

Possible outcomes:

- identify which artifacts belong to the current endpoint;
- confirm that an old bill was historically correct despite using a former address;
- preserve one unresolved association if evidence is insufficient;
- discover a later reuse of the old utility room.

No arbitrary Technology Education roll is required unless PTU/Caelo and scenario canon define a check.

## 27. Exploration concept — The Temporary Connection Nobody Removed From Memory

A seasonal market once used a temporary service point. The physical connection is now retired, but locals still refer to the corner by the old utility nickname. A new visitor mistakes the nickname for an active service location.

The story links Place Reference, Public Memory and this extension without reactivating any technical asset.

## 28. Immediate readiness

Usable now as world-state continuity:

- stable service-point identity;
- account succession;
- device association history;
- meter/device replacement history;
- observed/estimated/self-reported reading distinction;
- delayed data timestamps;
- append-only correction lineage;
- bill version provenance;
- Finance handoffs;
- physical-service handoffs;
- place/address updates;
- temporary service-point history;
- privacy-safe record linkage;
- noncombat mysteries and exploration;
- reduced encounter variants using static reviewed BattleSpecs.

No new battle rule is required for these core features.

## 29. PTU/Caelo questions left UNKNOWN

Until exact source evidence exists, do not invent:

- generic meter-reading Skill Checks;
- universal Technology Education utility rules;
- meter tampering checks;
- utility tariffs;
- consumption formulas;
- disconnect/reconnect combat actions;
- electrical/water utility Items;
- meter HP/DR;
- generalized electrical cabinet hazards;
- automatic Electric-type utility competence;
- automatic Water-type water-service competence;
- Pokémon-based billing estimation;
- Trainer Feature authority over utilities;
- battle rewards that erase or settle bills;
- battle outcomes that prove account ownership.

## 30. Canon questions left open

- Which Ouros regions meter household or business utilities?
- Which utilities have stable service-point records?
- Which institutions operate customer-facing accounts?
- Are service points individual, household, building, parcel, facility or community scoped?
- Which observation-device technologies exist?
- Are remote readings possible in any region?
- Are estimates used, and under what authored practice?
- Who can request corrections?
- Which historical records survive?
- What privacy rules apply?
- Which administrative reasons, if any, can lead to restriction or restoration?
- Which prices, tariffs or subsidies exist, if any?
- Which temporary connections exist for markets, festivals, construction or crisis response?
- Which individual Pokémon participate in utility work?

All remain PROPOSED/UNKNOWN until canon explicitly answers them.