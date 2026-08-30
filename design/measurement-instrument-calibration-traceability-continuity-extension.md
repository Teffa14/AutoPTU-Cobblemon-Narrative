# Ouros Measurement Instrument, Calibration & Traceability Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension preserves the history of measuring instruments and the provenance needed to understand results produced with them.

It connects physical instrument identity, monitoring-point assignment, configuration, reference use, calibration, verification, adjustment, maintenance, drift review, measurement-result lineage and later correction without replacing the existing Science layer or any domain owner.

The design exists so Ouros can remember that an instrument was replaced, a sensor drifted, a reference comparison happened later, a result was corrected or an observation point survived several equipment generations without rewriting history.

It does not define universal units, accuracy, uncertainty formulas, laboratory procedures, calibration intervals, Skill Check DCs, PTU bonuses, equipment durability or scientific truth.

## Authority boundaries

Science owns research questions, methods, datasets, hypotheses, analyses, research claims, review, replication and publication.

Air Quality, Weather, Seismic, Volcanic, Astronomy, Utilities, Wildlife Monitoring and other domain systems own their observations, domain-specific operational state and interpretations.

Material Culture owns persistent physical item identity when a measuring instrument is represented as a story-significant object.

Shared Equipment owns ordinary checkout/custody where applicable.

Facility Maintenance or another authored technical owner may own physical faults, repairs and work orders for a facility or installed asset.

Digital Systems owns storage, transmission, versions and access for digital records.

Human Identity, Organizations and Staffing own people, institutional roles and work assignments.

Case/Authority owns investigations and evidence custody when measurement records enter a case.

AutoPTU owns battle legality and tactical outcomes. Ouros owns world facts and selects combatants. Minecraft/Cobblemon/Craftics render or play back facts already decided by authoritative systems.

Pass 145 owns only the continuity among measurement point, instrument instance, configuration, calibration/verification/reference evidence, measurement result lineage and later quality review.

## Core invariants

`INSTRUMENT_ID != MEASUREMENT_POINT_ID`

`SENSOR_REPLACED != MONITORING_POINT_REPLACED`

`INSTRUMENT_PRESENT != INSTRUMENT_SERVICEABLE`

`INSTRUMENT_SERVICEABLE != RESULT_FIT_FOR_PURPOSE`

`CALIBRATION != ADJUSTMENT`

`CALIBRATION != VERIFICATION`

`CLEANING != CALIBRATION`

`MAINTENANCE_COMPLETED != CALIBRATION_CURRENT`

`REFERENCE_COMPARED != INSTRUMENT_ADJUSTED`

`RAW_INDICATION != MEASUREMENT_RESULT`

`MEASUREMENT_RESULT != DOMAIN_INTERPRETATION`

`MEASUREMENT_RESULT != WORLD_TRUTH`

`TRACEABILITY_DOCUMENTED != FIT_FOR_PURPOSE`

`OUT_OF_TOLERANCE_DISCOVERED != FAILURE_START_KNOWN`

`OUT_OF_TOLERANCE_DISCOVERED != ALL_PRIOR_RESULTS_FALSE`

`CORRECTED_RESULT != ORIGINAL_RECORD_DELETED`

`AUTOMATED_QUALITY_FLAG != INVALID_RESULT`

`NO_DATA != ZERO_VALUE`

`SAME_MODEL != SAME_INSTRUMENT_INSTANCE`

`SAME_INSTRUMENT != SAME_CONFIGURATION`

`SAME_LOCATION != SAME_MEASUREMENT_CONTEXT`

These separations are mandatory.

## 1. Measurement point

A point represents continuity of an observation location or measurement role independently of the hardware attached to it.

```yaml
measurement_point:
  measurement_point_id: null
  public_or_local_name_ids: []
  owner_domain_ref: null
  location_id: null
  spatial_scope_ref: null
  institution_ids: []
  purpose_claim_refs: []
  active_assignment_ids: []
  historical_assignment_ids: []
  environment_or_installation_context_refs: []
  current_operational_claim_ref: null
  created_event_id: null
  retired_event_id: null
  provenance_refs: []
  canon_status: proposed
```

A measurement point may be permanent, temporary, mobile or conceptual depending on the governing domain.

The schema does not establish that every measurement needs a fixed point.

## 2. Measuring instrument instance

```yaml
measurement_instrument:
  instrument_id: null
  material_item_instance_ref: null
  instrument_class_ref: null
  maker_or_source_claim_ref: null
  visible_identifier_records: []
  owner_actor_or_institution_id: null
  current_custodian_id: null
  current_location_id: null
  current_service_state: STATUS_UNKNOWN
  configuration_episode_ids: []
  assignment_episode_ids: []
  calibration_event_ids: []
  verification_event_ids: []
  adjustment_event_ids: []
  maintenance_ref_ids: []
  drift_or_quality_review_ids: []
  retirement_event_id: null
  provenance_refs: []
```

The internal `instrument_id` provides persistent world continuity. A serial number, painted label, station code, nickname or inventory number is a visible identifier record with its own issuer and validity interval.

A visible identifier can be changed, duplicated or reused without changing physical identity.

## 3. Identifier record

```yaml
instrument_identifier_record:
  identifier_record_id: null
  instrument_id: null
  identifier_type: null
  identifier_value: null
  issuer_actor_or_institution_id: null
  valid_from: null
  valid_until: null
  supersedes_identifier_id: null
  reason_ref: null
  provenance_refs: []
```

`SAME_IDENTIFIER_STRING != SAME_INSTRUMENT` unless provenance and time support the linkage.

## 4. Instrument assignment episode

```yaml
instrument_assignment:
  assignment_id: null
  instrument_id: null
  measurement_point_id: null
  owner_domain_ref: null
  assignment_role_ref: null
  assigned_at: null
  effective_from: null
  effective_until: null
  installed_or_deployed_event_ref: null
  removed_or_reassigned_event_ref: null
  responsible_actor_ids: []
  configuration_id: null
  method_scope_refs: []
  provenance_refs: []
```

Candidate assignment roles may include:

- PRIMARY_SENSOR
- REFERENCE_INSTRUMENT
- COMPARISON_INSTRUMENT
- TEMPORARY_REPLACEMENT
- BACKUP
- FIELD_CHECK_INSTRUMENT
- MOBILE_SURVEY_INSTRUMENT
- LAB_REFERENCE
- OTHER_AUTHORED_ROLE

These labels have no PTU mechanical meaning.

## 5. Configuration episode

An instrument can remain the same physical object while its setup changes.

```yaml
instrument_configuration_episode:
  configuration_id: null
  instrument_id: null
  effective_from: null
  effective_until: null
  configuration_claims: []
  component_refs: []
  software_or_processing_ref: null
  range_or_mode_ref: null
  installation_context_ref: null
  method_compatibility_refs: []
  changed_by_actor_ids: []
  change_event_ref: null
  provenance_refs: []
```

Do not infer numeric performance from a configuration label unless canon and method data define it.

## 6. Reference object or reference result

A calibration or verification may rely on a reference whose authority is itself bounded.

```yaml
measurement_reference:
  reference_id: null
  reference_type: null
  physical_item_ref: null
  result_ref: null
  source_institution_id: null
  property_or_quantity_ref: null
  stated_value_or_category_ref: null
  uncertainty_or_quality_ref: null
  valid_conditions: []
  valid_from: null
  valid_until: null
  upstream_reference_ids: []
  provenance_refs: []
  canon_status: proposed
```

The existence of a reference object does not create SI, a national standard or any real-world metrology institution in Ouros.

## 7. Calibration event

```yaml
instrument_calibration_event:
  calibration_event_id: null
  instrument_id: null
  configuration_id: null
  method_ref: null
  performed_at: null
  location_id: null
  performer_actor_ids: []
  reference_ids: []
  pre_operation_indication_refs: []
  calibration_relation_ref: null
  uncertainty_or_quality_refs: []
  applicable_conditions: []
  applicable_result_scope_refs: []
  outcome_state: RECORDED
  followup_action_refs: []
  provenance_refs: []
```

Suggested outcome states:

- RECORDED
- ACCEPTED_FOR_AUTHORED_SCOPE
- LIMITED_SCOPE
- FOLLOWUP_REQUIRED
- REFERENCE_QUESTIONED
- INSTRUMENT_RESPONSE_QUESTIONED
- SUPERSEDED
- VOIDED_BY_PROVENANCE_ERROR

These are workflow labels. They are not numeric accuracy classes.

## 8. Verification event

Verification checks an authored performance condition or comparison without automatically changing the instrument.

```yaml
instrument_verification_event:
  verification_event_id: null
  instrument_id: null
  configuration_id: null
  reference_ids: []
  verification_method_ref: null
  performed_at: null
  performer_actor_ids: []
  observed_indication_refs: []
  acceptance_criterion_ref: null
  outcome: UNRESOLVED
  adjustment_followup_ref: null
  calibration_followup_ref: null
  provenance_refs: []
```

Candidate outcomes:

- WITHIN_AUTHORED_CRITERION
- OUTSIDE_AUTHORED_CRITERION
- INCONCLUSIVE
- REFERENCE_UNAVAILABLE
- METHOD_NOT_COMPARABLE
- RECORD_INCOMPLETE
- UNRESOLVED

Pass 145 creates no universal acceptance criterion.

## 9. Adjustment event

```yaml
instrument_adjustment_event:
  adjustment_event_id: null
  instrument_id: null
  configuration_before_id: null
  adjustment_type_ref: null
  performed_at: null
  performer_actor_ids: []
  reason_ref: null
  pre_adjustment_indication_refs: []
  operations_claim_refs: []
  configuration_after_id: null
  required_recalibration_ref: null
  followup_verification_ref: null
  provenance_refs: []
```

Adjustment changes the measuring system. It never masquerades as calibration.

## 10. Cleaning and maintenance linkage

Ordinary maintenance remains owned by the relevant physical-asset system. Pass 145 stores only the relationship to measurement continuity.

```yaml
measurement_instrument_service_link:
  service_link_id: null
  instrument_id: null
  maintenance_or_repair_ref: null
  service_type_ref: null
  service_started_at: null
  service_completed_at: null
  pre_service_check_refs: []
  post_service_check_refs: []
  calibration_required_claim_ref: null
  affected_configuration_ids: []
  provenance_refs: []
```

Candidate service types may include CLEANING, COMPONENT_REPLACEMENT, REPAIR, INSPECTION, STORAGE_PREPARATION or OTHER_AUTHORED_SERVICE.

Those labels do not define technical procedures.

## 11. Instrument indication record

```yaml
instrument_indication_record:
  indication_id: null
  instrument_id: null
  configuration_id: null
  measurement_point_id: null
  observed_at: null
  received_at: null
  indication_value_ref: null
  display_or_output_unit_ref: null
  raw_source_ref: null
  operator_actor_ids: []
  environmental_context_refs: []
  automated_flag_refs: []
  manual_note_refs: []
  provenance_refs: []
```

An indication is what the instrument output under that context. It is not automatically the final measurement result.

## 12. Measurement-result lineage

Science already owns `measurement`. Pass 145 adds lineage around it without duplicating the scientific record.

```yaml
measurement_result_lineage:
  lineage_id: null
  science_measurement_id: null
  source_indication_ids: []
  instrument_id: null
  configuration_id: null
  measurement_point_id: null
  method_ref: null
  calibration_event_refs: []
  verification_event_refs: []
  reference_chain_refs: []
  processing_or_correction_refs: []
  uncertainty_or_quality_refs: []
  traceability_claim_ref: null
  fit_for_purpose_assessment_refs: []
  supersedes_lineage_id: null
  superseded_by_lineage_ids: []
  provenance_refs: []
```

The Science `measurement_id` remains the scientific owner. This object records how that result was produced and reviewed.

## 13. Traceability claim

```yaml
measurement_traceability_claim:
  traceability_claim_id: null
  measurement_result_ids: []
  specified_reference_ids: []
  chain_link_ids: []
  claimed_by_actor_or_institution_id: null
  claim_created_at: null
  applicable_scope: null
  uncertainty_or_quality_refs: []
  known_breaks_or_gaps: []
  review_state: UNREVIEWED
  reviewer_ids: []
  provenance_refs: []
```

Candidate review states:

- UNREVIEWED
- SUPPORTED_FOR_SCOPE
- PARTIALLY_SUPPORTED
- UNSUPPORTED
- INCOMPLETE_CHAIN
- SUPERSEDED
- ACCEPTED_AMBIGUITY

Traceability is never stored as a permanent boolean on the instrument.

## 14. Fit-for-purpose assessment

```yaml
measurement_fit_assessment:
  assessment_id: null
  measurement_result_id: null
  intended_use_ref: null
  assessor_actor_or_institution_id: null
  method_requirement_refs: []
  uncertainty_or_quality_refs: []
  known_limitations: []
  outcome: UNRESOLVED
  assessed_at: null
  supersedes_assessment_id: null
  provenance_refs: []
```

Candidate outcomes:

- SUITABLE_FOR_AUTHORED_USE
- SUITABLE_WITH_LIMITATIONS
- INSUFFICIENT_FOR_AUTHORED_USE
- METHOD_NOT_COMPARABLE
- EVIDENCE_INCOMPLETE
- UNRESOLVED

The system must know the intended use before claiming suitability.

## 15. Drift or out-of-tolerance review

```yaml
instrument_performance_review:
  review_id: null
  instrument_id: null
  opened_at: null
  trigger_event_refs: []
  latest_known_good_ref: null
  earliest_questioned_ref: null
  discovery_time: null
  candidate_start_window: null
  candidate_end_window: null
  affected_measurement_candidate_ids: []
  reviewed_measurement_ids: []
  excluded_from_effect_ids: []
  correction_episode_ids: []
  unresolved_questions: []
  current_state: OPEN
  provenance_refs: []
```

Candidate states:

- OPEN
- SCOPE_BOUNDED
- RESULTS_UNDER_REVIEW
- CORRECTIONS_ISSUED
- NO_MATERIAL_EFFECT_FOUND
- PARTIALLY_RESOLVED
- ACCEPTED_AMBIGUITY
- CLOSED

Hard rule: discovery time cannot silently become failure start time.

## 16. Correction and reprocessing episode

```yaml
measurement_correction_episode:
  correction_episode_id: null
  triggering_review_id: null
  original_measurement_ids: []
  original_indication_refs: []
  processing_change_ref: null
  correction_method_ref: null
  corrected_measurement_ids: []
  unchanged_measurement_ids: []
  invalidated_measurement_ids: []
  issued_at: null
  issuer_actor_or_institution_id: null
  downstream_revision_refs: []
  public_correction_handoff_refs: []
  provenance_refs: []
```

Original measurements remain queryable with their original timestamps, source chain and historical use.

`CORRECTED_VALUE != ORIGINAL_RECORD_DELETED`.

## 17. Instrument replacement and overlap

```yaml
instrument_succession_episode:
  succession_id: null
  measurement_point_id: null
  outgoing_instrument_id: null
  incoming_instrument_id: null
  overlap_start: null
  overlap_end: null
  comparison_event_refs: []
  reason_ref: null
  outgoing_state_ref: null
  incoming_acceptance_ref: null
  continuity_claim_ref: null
  provenance_refs: []
```

Possible reasons include routine replacement, repair rotation, temporary substitution, upgrade, loss, damage or unknown historical change.

Pass 145 does not define upgrade bonuses.

## 18. Comparison/collocation episode

```yaml
instrument_comparison_episode:
  comparison_id: null
  instrument_ids: []
  measurement_point_id: null
  comparison_location_id: null
  start_at: null
  end_at: null
  method_ref: null
  source_measurement_ids: []
  reference_instrument_ids: []
  alignment_or_processing_refs: []
  comparison_findings: []
  adjustment_followup_refs: []
  calibration_followup_refs: []
  result_review_refs: []
  provenance_refs: []
```

Co-location in space/time does not merge instrument identity or make the instruments equivalent for all later uses.

## 19. Monitoring gap caused by instrument state

Domain systems already own many monitoring-gap objects. Pass 145 should provide a reason/evidence handoff rather than create competing gaps.

```yaml
instrument_gap_handoff:
  handoff_id: null
  instrument_id: null
  measurement_point_id: null
  owner_domain_ref: null
  instrument_state_ref: null
  suspected_gap_start: null
  confirmed_gap_start: null
  restored_at: null
  quality_review_ref: null
  downstream_gap_ref: null
  provenance_refs: []
```

`INSTRUMENT_OFFLINE != PHENOMENON_ABSENT`.

## 20. Historical and public-memory continuity

Instrument history can leave visible traces after the technical problem ends.

Possible world facts:

- a retired sensor remains mounted on an old tower;
- a temporary monitoring hut becomes a familiar landmark;
- two generations of equipment leave different brackets on a wall;
- an old instrument sits in a museum beside the dataset it helped produce;
- residents remember a disputed reading long after a corrected report;
- researchers still refer to a station by an obsolete instrument nickname;
- a calibration log becomes relevant to a later case;
- a field notebook resolves which sensor was active during an old event.

Public memory remains separate from current scientific position.

## 21. Mysteries from provenance

### Five Times the Instrument Was “Calibrated”

Five records use the same casual word for five different events: comparison, cleaning, adjustment, formal calibration and post-repair verification.

Resolution requires chronology and event type, not accusation.

### Three Sensors, One Station

A long dataset lists three hardware identities. The monitoring point itself never moved.

### The Reading Before the Drift Was Found

A later verification discovers performance outside an authored criterion. Investigation must bound the questionable interval without declaring every older record false.

### The Value That Changed Twice

The raw indication remains stable in archive. A processing correction creates a revised result, then a later method change creates a second interpretation. All three records can be historically authentic.

### The Reference With No Provenance

A historical calibration note names a reference object whose own chain is missing. The correct endpoint may be `ACCEPTED_AMBIGUITY` rather than invented certainty.

## 22. Quest generators

Candidate state-driven jobs include:

- retrieve a reference instrument from another field station;
- escort a technician to a site whose data is under review;
- compare an aging sensor with a temporary reference;
- locate the physical instrument named in an old field notebook;
- reconstruct which configuration was active during a disputed observation;
- recover raw records before a correction can be evaluated;
- inspect an abandoned station where several device generations overlap;
- deliver a replacement sensor without treating delivery as installation;
- verify that a repaired instrument has returned before a monitoring gap is closed;
- interview former staff about an unresolved historical identifier;
- preserve a historically important instrument after retirement;
- map which downstream reports used results now under review.

These quests should emerge from world state rather than generic “collect data” menus.

## 23. Long-form arc pattern — A Valley Learns What Its Measurements Mean

Phase one establishes normal monitoring routines. Players repeatedly see one station, field crew and set of instruments without crisis.

Phase two introduces a small inconsistency: an aging sensor and a visiting reference do not agree under one set of conditions. No sabotage is assumed.

Phase three opens several independent timelines: replacement hardware arrives, the old sensor is removed, Science reviews affected measurements, a public report still quotes the earlier value and a downstream institution has already acted on it.

Phase four resolves what can be established. Some results survive unchanged. Some are corrected. One old interval remains ambiguous because a reference record is missing.

Phase five preserves consequences. A replacement device becomes the familiar station instrument, an old chart remains in a shop window, a later researcher cites the corrected dataset and residents remember when “the station changed its mind.”

The arc can be meaningful without a villain or combat.

## 24. Encounter contract — Monitoring Station Withdrawal Corridor

Narrative premise:

A field crew has paused monitoring operations and is withdrawing from a station while a separate tactical threat occupies the safe route.

Full-version dependency classification:

- targeting/footprints/range/LoS — VERIFIED baseline required;
- base movement legality — VERIFIED baseline required;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL if the full scene uses Intercept, displacement, escort-like movement or protected lanes;
- core calculations — VERIFIED baseline required;
- action economy/initiative — VERIFIED baseline required;
- full turn/round lifecycle — PARTIAL if withdrawal is staged across rounds;
- full stateful damage pipeline — PARTIAL for ordinary selected combatants;
- status lifecycle — PARTIAL only for exact selected statuses;
- terrain/weather/hazards/zones/reactions — BLOCKING if equipment lanes, active environmental zones, weather phases or generalized reactions matter;
- move-specific behavior — PARTIAL for selected legal Moves;
- abilities — PARTIAL for selected legal Abilities;
- items — PARTIAL only for exact implemented combat Items;
- Trainer Features/perks — PARTIAL only for exact legal participation;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `WITHDRAW`, `PROTECT_EXIT`, `AVOID_EQUIPMENT` or escort-aware behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic instrument/withdrawal state.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Monitoring is paused before BattleSpec.
2. Technicians, researchers and instruments leave BattleSpec.
3. Measurement-point state and instrument assignments freeze.
4. Ouros explicitly selects combatants.
5. AutoPTU receives reviewed static geometry.
6. No equipment HP, damage, theft, pickup or calibration mechanic is invented.
7. Victory creates only `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR` or `IMMEDIATE_STATION_APPROACH_CLEAR`.
8. Domain and measurement owners resume operations afterward.

`TACTICAL_VICTORY != INSTRUMENT_SERVICEABLE`.

`TACTICAL_VICTORY != MEASUREMENT_VALIDATED`.

`TACTICAL_VICTORY != MONITORING_RESUMED`.

## 25. Encounter contract — Reference Instrument Handoff Chokepoint

Narrative premise:

A reference/comparison instrument is waiting for a controlled handoff while an unrelated tactical threat blocks access to the meeting point.

Full-version dependencies match the permanent map above, with complete movement, full lifecycle, terrain/reactions and tactical policy required only if the intended design actually uses escort, moving custody, timed exchange or reactive zones.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Reference instrument remains outside BattleSpec.
2. Custody state freezes before combat.
3. Staff and couriers withdraw.
4. AutoPTU resolves a static nearby encounter.
5. Victory creates `IMMEDIATE_HANDOFF_APPROACH_CLEAR` only.
6. Shared Equipment/Material Culture/measurement owners perform custody and comparison events afterward.

`APPROACH_CLEAR != CUSTODY_TRANSFERRED`.

`CUSTODY_TRANSFERRED != CALIBRATION_COMPLETED`.

`CALIBRATION_COMPLETED != RESULT_FIT_FOR_PURPOSE`.

## 26. Encounter contract — Field Calibration Perimeter

Narrative premise:

A field team pauses a bounded calibration or verification operation when a separate tactical threat enters the work perimeter.

If the intended full version includes active weather, environmental hazards, changing work zones, delayed calibration windows, reactive movement or forced displacement, those exact families remain required.

Full version status: BLOCKED FOR RICH SEMANTICS.

Reduced version status: READY.

Reduced contract:

1. Calibration/verification is paused before BattleSpec.
2. Instrument, references and technical records remain outside combat.
3. Ouros freezes all pre-operation indications and technical state.
4. AutoPTU receives explicit combatants and static geometry.
5. Victory creates only `IMMEDIATE_FIELD_WORK_PERIMETER_CLEAR`.
6. The technical operation restarts afterward and can still fail, be inconclusive or require another reference.

`PERIMETER_CLEAR != CALIBRATION_SUCCESS`.

`PERIMETER_CLEAR != ADJUSTMENT_PERFORMED`.

`PERIMETER_CLEAR != RESULT_TRACEABLE`.

## 27. Reduced-version implementation rule

Pass 145 can advance without rich battle support because measurement continuity is primarily world-state/provenance logic.

Before battle, existing world owners resolve or freeze:

- instrument identity;
- instrument custody;
- measurement-point assignment;
- configuration;
- physical service state;
- calibration/verification state;
- reference identity;
- Science measurements and datasets;
- quality-review state;
- private or restricted records;
- noncombatants.

Battle receives only explicit combatants and static reviewed geometry.

Battle returns a narrow physical-access fact.

World-state owners resume afterward.

## 28. Minecraft/Cobblemon/Craftics boundary

Presentation may display authored facts such as:

- sensor towers;
- instrument cases;
- reference objects;
- mounting brackets;
- temporary field stations;
- calibration/maintenance tags;
- equipment swaps;
- old and new device models;
- technician NPCs;
- field notebooks or UI records;
- warning signs;
- a retired instrument in a museum;
- changed particles or sounds when Ouros has already decided an equipment state.

Presentation cannot infer:

- calibration from placing an item near another item;
- validity from a glowing indicator;
- traceability from an item name;
- instrument identity from entity UUID alone;
- sensor replacement from despawn/spawn alone;
- measurement-point identity from block coordinates alone;
- a domain phenomenon from a redstone signal;
- scientific truth from an animation;
- tactical status from an environmental prop.

Minecraft physics does not create PTU instrument durability, calibration, collision, exposure or measurement rules.

Cobblemon BattleState remains non-authoritative for combatants, legality, HP/status, tactical position and world consequences.

## 29. PTU/Caelo guardrail

Pass 145 does not establish:

- generic calibration actions;
- universal instrument Skill Checks;
- scientific precision bonuses;
- generic equipment accuracy;
- universal drift;
- universal units;
- generic reference standards;
- Researcher-class authority over all instruments;
- Technology Education authority over all calibration;
- Perception as automatic diagnosis;
- species/Type/Move/Ability as universal detector or reference;
- Pokédex as a universal calibrated standard;
- battle damage rules for scientific equipment.

Exact mechanics require exact governing sources and current implementation evidence.

## Canon questions left open

Pass 145 deliberately leaves unanswered:

- which Ouros regions or institutions use formal calibration practices;
- which measurement systems exist;
- which units or scales are used;
- whether reference standards are local, regional, institutional or informal;
- whether specialized metrology institutions exist;
- which instruments can be calibrated, verified or only compared;
- acceptable uncertainty or performance for any purpose;
- calibration or verification frequency;
- who is authorized or trusted to perform technical work;
- record-retention practices;
- whether citizen/community monitoring exists in particular regions;
- privacy or access rules around measurement records;
- named laboratories, observatories, field stations or recurring technicians;
- Pokémon roles in measurement work;
- exact PTU/Caelo mechanics for any instrument-related action.

## Conclusion

This extension gives Ouros durable scientific infrastructure without turning instruments into truth machines.

It allows one monitoring point to outlive several sensors, one sensor to move through several assignments, one result to acquire a later correction and one old calibration chain to remain incomplete. The resulting discrepancies create quests, mysteries, institutional memory and environmental storytelling while preserving existing domain authority and the boundary around AutoPTU.