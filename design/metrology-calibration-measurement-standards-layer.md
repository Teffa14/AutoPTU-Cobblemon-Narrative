# Ouros Metrology, Calibration & Measurement Standards Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already creates measurements in Science, Meteorology, Air Quality, Astronomy, Cartography, Hydrology, Groundwater, Seismic monitoring, Manufacturing, Water Service and many other systems. This layer supplies the shared provenance needed to decide what those numbers mean and whether they can be compared.

It models instruments, reference standards, calibration events, valid scope, uncertainty, benchmarks, checks, drift, reference-system revisions and historical comparability.

It does not create new PTU Skills, equipment bonuses, scientific truth or Minecraft authority.

## 1. Authority boundaries

This layer owns:

- persistent identity of measurement instruments when narratively important;
- measurement-variable definitions and reference conventions;
- reference standards and transfer standards;
- calibration/check events;
- calibration scope and validity claims;
- uncertainty/precision/resolution metadata;
- out-of-tolerance findings;
- reference benchmarks/datums;
- unit/reference-system revisions;
- conversion/correction records;
- traceability chains between a measurement result and its reference context;
- comparison campaigns between instruments/sites;
- historical measurement comparability.

It does not own:

- the physical phenomenon being measured -> owning domain layer;
- research questions, datasets, hypotheses and publications -> Science;
- instrument maintenance/failure -> Technology/Infrastructure;
- manufacturing conformity decisions -> Manufacturing;
- weather truth/forecasting -> Meteorology;
- map truth/routes -> Cartography;
- criminal findings -> Cases;
- staff qualifications -> Workplaces/Credentials;
- research subject authorization -> Research Ethics;
- PTU/Caelo mechanics -> authoritative rules/AutoPTU;
- Minecraft block/entity state as measurement truth -> never.

## 2. Core separation

Keep this chain explicit:

```text
PHYSICAL_STATE
  -> MEASURAND / VARIABLE
  -> METHOD
  -> INSTRUMENT + REFERENCE CONTEXT
  -> RAW OBSERVATION
  -> QUALITY / UNCERTAINTY
  -> DERIVED OR CORRECTED RESULT
  -> DATASET
  -> INTERPRETATION
  -> DECISION
```

Important no-inferences:

```text
instrument calibrated != instrument always correct
calibration current != valid for every range/method
precise display != accurate result
same unit != same reference convention
same instrument model != same calibration history
measurement disagreement != fraud
measurement disagreement != instrument failure
out of tolerance != all historical data invalid
recalibration != rewrite raw history
new reference system != old record was false
sensor offline != phenomenon absent
Minecraft coordinate != authoritative survey datum
Pokédex entry != perfect world truth
```

## 3. MEASUREMENT_VARIABLE

A variable says what is being measured and how it is represented.

```yaml
measurement_variable:
  variable_id: null
  name: null
  domain_layer: null
  quantity_or_category_type: null
  canonical_representation_ref: null
  allowed_unit_refs: []
  method_family_refs: []
  expected_resolution_band: null
  comparison_constraints: []
  canon_state: PROPOSED
```

Examples can include river stage, air temperature, particulate concentration, magnetic declination, component dimension, telescope time reference or soil moisture.

These examples do not establish which exact variables Ouros canon tracks.

## 4. INSTRUMENT_INSTANCE

Use persistent identity only when the device matters to provenance, maintenance or story.

```yaml
instrument_instance:
  instrument_id: null
  instrument_type_ref: null
  serial_or_local_identifier: null
  institution_id: null
  current_location_id: null
  technical_asset_id: null
  supported_variable_ids: []
  supported_method_refs: []
  operating_range_claims: []
  resolution_claims: []
  calibration_event_ids: []
  check_event_ids: []
  maintenance_record_ids: []
  incident_ids: []
  current_metrology_state: UNKNOWN
  history_event_ids: []
```

Candidate metrology states:

- UNKNOWN
- IN_SERVICE
- CHECK_DUE
- CALIBRATION_DUE
- RESTRICTED_RANGE
- OUT_OF_TOLERANCE
- QUARANTINED
- RETIRED

The state describes measurement confidence/use policy, not whether the device physically powers on.

## 5. REFERENCE_STANDARD

A reference can be an instrument, artefact, stable reference process, benchmark or institutional convention.

```yaml
reference_standard:
  reference_standard_id: null
  variable_id: null
  reference_type: null
  owning_or_custodian_institution_id: null
  location_id: null
  reference_value_or_definition: null
  uncertainty_or_quality_ref: null
  valid_scope: null
  effective_from: null
  supersedes_reference_id: null
  calibration_or_comparison_refs: []
  custody_history_refs: []
  status: ACTIVE
```

Candidate reference types:

- PRIMARY_LOCAL_STANDARD
- TRANSFER_STANDARD
- REFERENCE_MATERIAL
- SURVEY_BENCHMARK
- TIME_REFERENCE
- CONSENSUS_COMPARISON
- HISTORICAL_CONVENTION

These labels do not imply real-world SI or NIST structures in Ouros.

## 6. CALIBRATION_EVENT

A calibration event relates an instrument result to a reference within a stated scope.

```yaml
calibration_event:
  calibration_event_id: null
  instrument_id: null
  performed_at: null
  performed_by_actor_ids: []
  institution_id: null
  variable_id: null
  method_ref: null
  reference_standard_ids: []
  tested_range_ref: null
  environmental_conditions_ref: null
  as_found_results: []
  adjustments_made: []
  as_left_results: []
  uncertainty_ref: null
  valid_scope_ref: null
  next_check_policy_ref: null
  source_record_refs: []
  outcome: ACCEPTED
```

Candidate outcomes:

- ACCEPTED
- ACCEPTED_RESTRICTED_SCOPE
- ADJUSTED_AND_ACCEPTED
- OUT_OF_TOLERANCE
- INCONCLUSIVE
- FAILED_CHECK

A calibration applies to its documented scope. It never provides a permanent global `accurate=true` flag.

## 7. CALIBRATION_CHECK

A lighter comparison can occur between formal calibration events.

```yaml
calibration_check:
  check_id: null
  instrument_id: null
  checked_at: null
  comparison_reference_ids: []
  comparison_instrument_ids: []
  variable_id: null
  tested_condition_refs: []
  observed_difference: null
  acceptance_claim_ref: null
  reviewer_ids: []
  outcome: WITHIN_EXPECTATION
```

Candidate outcomes:

- WITHIN_EXPECTATION
- DRIFT_SUSPECTED
- OUT_OF_EXPECTATION
- INCONCLUSIVE
- RECHECK_REQUIRED

A failed check creates a metrology problem. It does not prove sabotage or invalidate every result produced since the previous calibration.

## 8. MEASUREMENT_RESULT extension

Science already owns the research measurement record. Domain layers may also create measurements. Add shared metrology references rather than duplicating observations.

```yaml
measurement_metrology_context:
  measurement_id: null
  variable_id: null
  instrument_id: null
  method_id: null
  raw_value_ref: null
  unit_ref: null
  reference_system_id: null
  calibration_event_id: null
  check_state_at_measurement_ref: null
  uncertainty_ref: null
  resolution_ref: null
  detection_limit_ref: null
  quality_flags: []
  correction_record_ids: []
  traceability_chain_id: null
```

The raw observation stays immutable. Later corrections create derived values.

## 9. TRACEABILITY_CHAIN

```yaml
traceability_chain:
  traceability_chain_id: null
  measurement_id: null
  link_ids: []
  terminal_reference_id: null
  combined_uncertainty_ref: null
  missing_link_claim_ids: []
  review_status: COMPLETE_ENOUGH_FOR_SCOPE
```

Possible link:

```yaml
traceability_link:
  link_id: null
  from_instrument_or_result_ref: null
  to_reference_ref: null
  comparison_event_id: null
  uncertainty_contribution_ref: null
  performed_at: null
  source_record_refs: []
```

Ouros does not need every measurement to have a long chain. Use this detail only when comparability or investigation matters.

## 10. REFERENCE_SYSTEM and versions

Maps, gauges, clocks and institutional records can use historical conventions.

```yaml
reference_system:
  reference_system_id: null
  reference_family: null
  revision_id: null
  definition_ref: null
  effective_from: null
  supersedes_revision_id: null
  conversion_refs: []
  benchmark_ids: []
  owning_or_maintaining_institution_ids: []
  status: ACTIVE
```

Candidate reference families:

- VERTICAL_DATUM
- HORIZONTAL_SURVEY_REFERENCE
- LOCAL_DISTANCE_STANDARD
- MASS_STANDARD
- TIME_STANDARD
- TEMPERATURE_SCALE
- INSTRUMENT_SPECIFICATION_REFERENCE

The names are conceptual. Canon decides what Ouros actually uses.

## 11. SURVEY_BENCHMARK

```yaml
survey_benchmark:
  benchmark_id: null
  location_id: null
  physical_marker_asset_id: null
  reference_system_id: null
  established_at: null
  reference_value_ref: null
  independent_check_marker_ids: []
  inspection_event_ids: []
  disturbance_event_ids: []
  current_status: VERIFIED
```

Candidate status values:

- VERIFIED
- SUSPECT
- DISTURBED
- LOST
- RELOCATED
- SUPERSEDED

A moved marker does not move the landscape. It damages or changes the reference relationship.

## 12. OUT_OF_TOLERANCE_EVENT

```yaml
out_of_tolerance_event:
  oot_event_id: null
  instrument_id: null
  detected_at: null
  detected_by_event_id: null
  affected_variable_ids: []
  suspected_start_window: null
  demonstrated_scope: null
  potentially_affected_measurement_ids: []
  review_case_id: null
  correction_plan_ref: null
  current_status: UNDER_REVIEW
```

Do not automatically mark all potentially affected data as false. Review can classify records as:

- UNAFFECTED
- CORRECTABLE
- UNCERTAIN
- UNUSABLE_FOR_SPECIFIC_PURPOSE
- STILL_USEFUL_AT_COARSER_RESOLUTION

This supports failure-forward science instead of deleting history.

## 13. CORRECTION_RECORD

```yaml
measurement_correction:
  correction_id: null
  original_measurement_id: null
  correction_reason: null
  correction_method_ref: null
  derived_value_ref: null
  new_uncertainty_ref: null
  reviewer_ids: []
  created_at: null
  supersedes_correction_id: null
  source_refs: []
```

Never overwrite the raw value.

## 14. COMPARISON_CAMPAIGN

Institutions can periodically compare instruments or regional standards.

```yaml
comparison_campaign:
  comparison_campaign_id: null
  variable_id: null
  participating_institution_ids: []
  participating_instrument_ids: []
  reference_ids: []
  site_ids: []
  planned_window: null
  observation_ids: []
  discrepancy_ids: []
  conclusion_claim_ids: []
  status: PLANNED
```

This can create recurring scientific events without creating a new crisis every time.

## 15. Relationship to Science

Science owns what researchers ask and conclude.

Metrology answers whether the observations feeding those conclusions are comparable within a known scope.

Example:

```text
Science question: Is the spring declining?
Groundwater: owns actual spring discharge state.
Metrology: owns gauge/reference/calibration history.
Science: analyzes the measurement series.
Institution: decides whether more monitoring is needed.
```

A metrology correction can change a dataset without directly writing a scientific conclusion.

## 16. Relationship to Manufacturing

Manufacturing owns process quality and disposition.

Metrology can explain why a measurement is under review.

```text
production lot exists
  -> inspection measurement taken
  -> instrument later found out of tolerance
  -> affected observations reviewed
  -> Manufacturing decides whether lot disposition changes
```

An instrument issue does not automatically mean the lot is defective.

## 17. Relationship to Meteorology, Air Quality and Environmental monitoring

Domain layer owns the phenomenon and station network meaning.

Metrology owns reference/calibration context shared by the instruments.

A sensor can be operational in Technology but `CALIBRATION_DUE` here. A weather observation can therefore remain stored with a quality flag while the station itself remains online.

## 18. Relationship to Cartography and historical maps

Cartography owns maps, route traces and spatial knowledge.

Metrology owns survey benchmarks/reference revisions.

Two maps can disagree because:

- the landscape changed;
- one survey used an older reference;
- one benchmark moved;
- one map contains an error;
- the maps were produced at different precision.

Do not pick one cause until evidence supports it.

## 19. Relationship to Technology

Technology owns physical health, maintenance, power and interfaces.

Metrology owns measurement fitness.

Examples:

- device powers on but calibration is invalid;
- device is physically damaged but still produces usable coarse readings;
- calibration is current but the device is later dropped;
- software update changes displayed rounding without changing the sensor itself.

## 20. Pokémon interactions

Pokémon can affect or assist measurement only when supported by authored behavior and/or validated mechanics.

Possible worldbuilding uses:

- a Magnemite population creates a local interference hypothesis around a magnetic station;
- a Rotom repeatedly enters one specific instrument;
- a Pokémon physically moves a benchmark marker;
- a Pokémon’s recurring behavior becomes an independent observation stream.

Hard restrictions:

- Electric-type does not mean calibrated voltage reference;
- Psychic-type does not mean perfect sensor;
- Porygon does not automatically validate software;
- Nosepass does not automatically provide survey-grade north;
- Rotom possession does not grant universal diagnostics;
- a Pokémon observation does not become a numerical measurement without an actual method.

## 21. Multiplayer knowledge/privacy

Players may receive different layers of measurement information.

Possible visibility states:

- raw reading visible to technician;
- quality warning visible to institution;
- corrected public value published later;
- sensitive site coordinates redacted;
- maintenance history restricted;
- historical calibration certificate archived publicly.

Do not hide mechanical battle truth behind metrology. This privacy model applies to overworld records only.

## 22. Persistence and offline progression

Safe offline progression can include:

- calibration due dates advancing;
- scheduled comparison windows arriving;
- station checks becoming overdue;
- known reference revisions taking effect;
- approved instrument replacement completing through Supply Chains/Technology.

Do not silently create instrument drift every time the player logs out. Drift events require authored/procedural evidence rules, not random punishment.

## 23. Minecraft projection

Minecraft may display:

- physical gauges;
- survey markers;
- calibration labs;
- instrument racks;
- portable reference kits;
- station status lights;
- historical plaques;
- sensor readouts.

Minecraft does not own:

- authoritative measurement values;
- calibration validity;
- uncertainty;
- reference-system revisions;
- traceability;
- whether a sensor result is accepted;
- scientific conclusions.

Breaking a block can create a physical incident through Technology/Architecture. It cannot retroactively delete measurements already stored in Chronicle.

## 24. Battle boundary

Metrology is overworld state.

A measurement can inform encounter setup only through explicit mechanics review.

Examples:

- a weather station measurement does not directly create battlefield Weather;
- a survey distance does not override AutoPTU range calculations;
- a calibrated scope does not grant Accuracy;
- a timing instrument does not alter initiative;
- a pressure gauge does not create a hazard zone;
- a Geiger-counter-like fictional device would not create damage/status by itself.

AutoPTU-Java remains authoritative for every tactical calculation.

## 25. Canon gates

Before canonizing regional metrology, decide:

- what measurement traditions existed historically;
- which institutions maintain reference standards;
- whether regions share standards or maintain conversions;
- what units/conventions players actually see;
- how historical maps/records expose reference versions;
- which networks are coarse qualitative versus precise numerical;
- how much calibration detail should be visible to ordinary players;
- whether player-run institutions can maintain recognized standards.

## 26. Open PTU/Caelo questions

Require primary project text before adding mechanics for:

- Technology Education applied to measurement or instruments;
- Researcher/Scientist Features relevant to analysis;
- Pokédex/identification mechanics;
- equipment/tool bonuses;
- Survival/Perception interactions with field measurement;
- any Pokémon Capability used as an instrument substitute;
- any Caelo-specific research, engineering or survey rules.

Until verified, these remain narrative/overworld records only.

## 27. Core design rule

Preserve three things separately: what the world did, what the instrument reported, and what people concluded.

That separation lets Ouros support bad sensors, excellent technicians, obsolete reference systems, honest disagreement, corrected archives and long-running scientific progress without retconning the world.