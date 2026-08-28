# Ouros Cold-Chain & Temperature-Controlled Custody Continuity Extension

Status: PROPOSED systems design. Not established Ouros canon. No PTU rules are created here.
Date: 2026-08-28
Research provenance: `research/2026-08-28-cold-chain-temperature-controlled-custody-scan-112.md`.

## Purpose

Ouros already owns the places, shipments, batches, care supplies, foods, utilities and maintenance workflows that can participate in temperature-controlled handling. This extension owns only continuity evidence across those boundaries.

Its job is to answer:

- Does this specific subject have an authored condition requirement?
- Which storage/transport/transfer segments were intended to preserve it?
- What was actually observed, where and when?
- Is there an evidence gap?
- Did an observation create an excursion hypothesis?
- Which downstream owning system must decide hold, clearance, use or disposition?
- Was a temporary continuity arrangement used, and did it leave persistent world history?

It does not invent spoilage, product safety, medicine potency, cold damage, storage thresholds or refrigeration technology.

## Authority boundary

This layer owns:

- persistent `condition_profile` references for subjects that already have an authored requirement;
- cold-chain continuity records spanning multiple owners;
- condition observations and monitoring gaps;
- continuity segments for storage, staging, transfer and transport;
- handoff condition-verification records;
- excursion hypotheses and affected-scope evidence;
- temporary condition-preservation arrangements;
- restoration/verification sequence for the continuity service itself;
- provenance and historical records.

It references but does not own:

- item/material/food identity or mechanical effects — Material Culture / Food / PTU/Caelo;
- physical storage location, putaway, picking and staging — Storage/Warehousing;
- shipment legs and custody transfer — Courier/Port/other transport owner;
- sourcing, receipt and acceptance — Procurement;
- treatment/use decisions — Care;
- quarantine, recall, correction, clearance and disposition — Batch Traceability or other governing owner;
- refrigeration equipment repair — Facility Maintenance;
- electrical or other upstream utility state — Technology/Energy and Infrastructure Outage;
- vehicle/service state — relevant transport layer;
- payment/compensation — Finance;
- tactical legality/effects — AutoPTU;
- Minecraft/Cobblemon visuals — presentation only.

## 1. Condition profile

A condition profile exists only when canon or an authoritative item/food/care source says the subject requires a controlled condition.

```yaml
condition_profile:
  condition_profile_id: null
  subject_definition_ref: null
  authored_condition_kind: null
  governing_source_refs: []
  authored_range_or_state_ref: null
  authored_duration_rule_ref: null
  authored_transition_rule_refs: []
  mechanical_effect_refs: []
  validation_state: SOURCE_REQUIRED
  notes: []
```

`authored_range_or_state_ref` is a reference, not a narrative-system number generator.

Allowed high-level kinds can include `COOLED`, `FROZEN`, `TEMPERATURE_CONTROLLED`, `OTHER_AUTHORED` or `UNSPECIFIED_CONTROLLED_CONDITION`. These labels grant no numeric threshold.

If no governing source exists, the system must use `UNKNOWN_REQUIREMENT` rather than inventing one.

## 2. Controlled subject

```yaml
controlled_subject:
  controlled_subject_id: null
  item_instance_refs: []
  material_batch_refs: []
  food_batch_refs: []
  care_supply_refs: []
  shipment_ref: null
  aggregate_subject_ref: null
  condition_profile_id: null
  current_owner_system_ref: null
  current_location_ref: null
  current_custody_ref: null
  continuity_record_id: null
  current_review_state: NO_REVIEW_REQUIRED
```

A subject can be aggregate when exact per-item identity is not useful. Significant or disputed units can retain exact instance/batch identity.

## 3. Continuity record

```yaml
condition_continuity_record:
  continuity_record_id: null
  controlled_subject_id: null
  condition_profile_id: null
  segment_ids: []
  observation_ids: []
  monitoring_gap_ids: []
  handoff_verification_ids: []
  excursion_record_ids: []
  temporary_arrangement_ids: []
  current_continuity_state: NOT_STARTED
  latest_verified_at: null
  uncertainty_refs: []
  provenance_refs: []
```

Suggested continuity states:

- NOT_STARTED
- VERIFIED_TO_CURRENT_POINT
- VERIFICATION_PENDING
- UNKNOWN_FOR_INTERVAL
- EXCURSION_SUSPECTED
- EXCURSION_CONFIRMED_BY_GOVERNING_SOURCE
- UNDER_EXTERNAL_REVIEW
- CONTINUITY_RESTORED_FOR_FUTURE_SEGMENTS
- CLOSED
- SUPERSEDED

`CONTINUITY_RESTORED_FOR_FUTURE_SEGMENTS` does not clear earlier affected goods.

## 4. Continuity segment

A segment records an interval during which an owning system was expected to preserve the authored condition.

```yaml
condition_segment:
  segment_id: null
  continuity_record_id: null
  segment_kind: null
  owner_system_ref: null
  facility_zone_or_vehicle_ref: null
  custody_ref: null
  started_at: null
  ended_at: null
  expected_condition_profile_id: null
  observation_ids: []
  dependency_refs: []
  status: PLANNED
  uncertainty_refs: []
```

Candidate descriptive kinds:

- STORAGE
- STAGING
- INTERNAL_TRANSFER
- LOADING_OR_UNLOADING
- TRANSPORT
- TRANSFER_POINT
- TEMPORARY_HOLDING
- DESTINATION_STORAGE
- OTHER_AUTHORED

Lifecycle:

PLANNED -> READY -> ACTIVE -> PHYSICALLY_COMPLETE -> EVIDENCE_RECONCILED -> CLOSED.

Branches: INTERRUPTED, UNKNOWN, SUPERSEDED.

`PHYSICALLY_COMPLETE != EVIDENCE_RECONCILED`.

A courier may have completed a delivery leg while the condition evidence remains unresolved.

## 5. Condition observation

```yaml
condition_observation:
  observation_id: null
  continuity_record_id: null
  segment_id: null
  observed_at: null
  observed_location_ref: null
  observed_by_ref: null
  observation_method_ref: null
  raw_claim_ref: null
  interpreted_against_profile_ref: null
  interpretation_state: UNINTERPRETED
  source_refs: []
  trust_or_calibration_claim_refs: []
```

Possible interpretation states:

- UNINTERPRETED
- CONSISTENT_WITH_AUTHORED_PROFILE
- OUTSIDE_AUTHORED_PROFILE
- INSUFFICIENT_TO_EVALUATE
- CONFLICTING_EVIDENCE
- SUPERSEDED

The narrative system does not invent sensor accuracy, calibration or a threshold. It preserves the claim and provenance.

## 6. Monitoring gap

```yaml
monitoring_gap:
  monitoring_gap_id: null
  continuity_record_id: null
  segment_id: null
  gap_start: null
  gap_end: null
  reason_claim_refs: []
  corroborating_evidence_refs: []
  current_state: UNKNOWN_FOR_INTERVAL
  resolved_by_refs: []
```

A gap is not automatically an excursion.

`NO_READING != OUT_OF_RANGE`.

A closed door, powered refrigerator, intact icebox or confident NPC statement is not enough to fabricate a missing measurement if the authored continuity contract requires evidence.

## 7. Handoff verification

Custody and condition must remain separate.

```yaml
condition_handoff_verification:
  verification_id: null
  continuity_record_id: null
  related_custody_transfer_ref: null
  from_segment_id: null
  to_segment_id: null
  observed_at: null
  observation_refs: []
  records_received_refs: []
  records_missing_refs: []
  receiving_actor_or_system_ref: null
  condition_evidence_state: PENDING
```

Suggested states:

- PENDING
- ACCEPTED_AS_CONTINUOUS
- ACCEPTED_WITH_GAP
- EXCURSION_REVIEW_REQUIRED
- CONFLICTING_RECORDS
- NOT_APPLICABLE
- SUPERSEDED

A shipment can be legally/operationally received while condition evidence remains under review, if the governing owning systems permit that workflow. The cold-chain layer itself does not decide acceptance law or product disposition.

## 8. Excursion record

```yaml
condition_excursion_record:
  excursion_record_id: null
  continuity_record_id: null
  first_trigger_observation_refs: []
  suspected_start: null
  suspected_end: null
  affected_segment_ids: []
  potentially_affected_subject_refs: []
  evidence_refs: []
  uncertainty_refs: []
  governing_review_handoff_refs: []
  state: SUSPECTED
```

Suggested states:

- SUSPECTED
- EVIDENCE_GATHERING
- CONFIRMED_BY_GOVERNING_SOURCE
- NOT_CONFIRMED
- SCOPE_REVISED
- HANDED_OFF_FOR_DISPOSITION
- CLOSED

This layer may identify potentially affected subjects. It may not decide that food spoiled, medicine lost potency, an item became unsafe, or a mechanical effect changed unless an authoritative owner/rule establishes that result.

## 9. Review handoff

```yaml
condition_review_handoff:
  review_handoff_id: null
  excursion_record_id: null
  receiving_owner_system_ref: null
  subject_refs: []
  evidence_bundle_refs: []
  requested_at: null
  received_at: null
  decision_ref: null
  status: REQUESTED
```

Examples of receiving owners:

- Batch Traceability for a hold/quarantine/clearance workflow;
- Care for treatment-use suitability where canon supports such a question;
- Food system for non-mechanical service disposition;
- Procurement for supplier/receipt follow-up;
- another explicit canon authority.

The cold-chain system never silently consumes or destroys the goods.

## 10. Controlled facility/vehicle capability

Do not infer capability from appearance.

```yaml
condition_control_capability:
  capability_record_id: null
  asset_ref: null
  supported_profile_refs: []
  governing_design_or_canon_refs: []
  current_service_state: UNKNOWN
  maintenance_dependency_refs: []
  utility_dependency_refs: []
  verification_refs: []
  effective_from: null
```

Candidate service states:

- UNKNOWN
- AVAILABLE
- CONSTRAINED
- TEMPORARILY_UNAVAILABLE
- MAINTENANCE
- TESTING
- VERIFIED_AVAILABLE
- RETIRED

`POWER_AVAILABLE != CONDITION_CONTROL_VERIFIED`.

`UNIT_RUNNING != CONTROLLED_SUBJECT_CLEARED`.

## 11. Temporary preservation arrangement

```yaml
temporary_condition_arrangement:
  arrangement_id: null
  affected_profile_refs: []
  subject_refs: []
  temporary_asset_or_location_refs: []
  operator_refs: []
  started_at: null
  ended_at: null
  verification_refs: []
  capacity_claim_ref: null
  dependency_refs: []
  state: PROPOSED
  history_event_refs: []
```

Suggested states:

- PROPOSED
- PREPARING
- VERIFIED_READY
- ACTIVE
- CONSTRAINED
- FAILED_OR_INTERRUPTED
- STANDING_DOWN
- CLOSED
- RETAINED_AS_PERMANENT

A temporary arrangement can become persistent world history without gaining numeric capacity or safety properties that were never authored.

## 12. Restoration sequence

When condition control is disrupted, recovery should be staged.

Possible sequence:

1. interruption observed;
2. affected subjects/segments identified as far as evidence allows;
3. upstream fault isolated by its owner;
4. repair or service recovery occurs;
5. condition-control asset is tested/verified;
6. new/future segments can resume;
7. earlier exposed or uncertain subjects remain under their own review;
8. downstream business/care/food service resumes according to its own authority.

Never compress this into `POWER_ON -> ALL_GOODS_SAFE`.

## 13. World-memory patterns

The system should preserve:

- former refrigerated depots and their old bay names;
- temporary cold rooms that became community infrastructure;
- carriers known for a difficult emergency route;
- repeated monitoring gaps associated with one aging asset without auto-assigning blame;
- businesses whose morning schedules changed during a continuity disruption;
- former workers or Pokémon whose routines remain attached to a decommissioned site;
- alternative routes discovered during a service interruption.

These become Chronicle/world-state hooks, not stat bonuses.

## 14. Pokémon participation boundary

A specific Pokémon may participate in carrying, monitoring, guarding, cooling or other work only when the role is individually authored and any mechanical prerequisite is validated against governing PTU/Caelo sources.

Never infer from species or Type:

- cold tolerance;
- refrigeration output;
- food/medicine safety;
- ability to monitor temperature;
- occupational qualification;
- immunity to a cold-room hazard.

A model, animation, Move name or Ice typing is insufficient evidence.

## 15. Encounter contract boundary

Temperature-controlled logistics should normally remain overworld state. Combat is justified only when conflict independently exists.

A BattleSpec must exclude civilians, workers, vehicles, controlled goods and active equipment unless their tactical participation has an exact governing rule and implementation support.

Winning combat may establish facts such as:

- `IMMEDIATE_LOADING_BAY_SECURED`;
- `ACCESS_TO_BACKUP_ROOM_SECURED`;
- `COURIER_ROUTE_PERIMETER_SECURED`.

It may not establish:

- `TEMPERATURE_RESTORED`;
- `EXCURSION_CLEARED`;
- `GOODS_SAFE`;
- `MEDICINE_VALID`;
- `FOOD_RELEASED`;
- `SHIPMENT_CONDITION_VERIFIED`;
- `POWER_RESTORED`.

Those require their respective world-state owners.

## 16. Minecraft/Cobblemon/Craftics boundary

Presentation can reuse cold-room builds, doors, insulated containers, crates, gauges/screens, refrigeration props, vehicles, lights, alarms, frost/condensation visuals, particles, sounds, NPCs and Pokémon models/animations.

Visual state never becomes authority:

- frost texture does not prove a verified condition;
- ice blocks do not create a cold-chain reading;
- a redstone-powered machine does not prove condition-control availability;
- a chest does not own custody or continuity truth;
- a thermometer-like UI element must display authoritative Ouros data, not derive it from Minecraft biome temperature;
- native ice/slipperiness does not create PTU forced movement;
- powder snow/freezing damage does not substitute for PTU damage/status;
- an Ice-type model standing in a cold room does not maintain refrigeration;
- Cobblemon BattleState/controller logic does not decide combatants, legality, HP/status, positions or battle outcomes.

Ouros owns world facts and combatant selection. AutoPTU owns tactical legality/resolution. Minecraft/Cobblemon/Craftics presents authoritative outcomes.

## 17. Canon classification

CANON-APPROVED by this extension: none. Existing established canon is not overwritten.

PROPOSED: the continuity objects and state transitions in this file.

UNCERTAIN: regional technologies, temperature-sensitive goods, operators, monitoring methods, backup systems, priorities, privacy rules and Pokémon work roles.

MECHANICALLY UNKNOWN: thermal thresholds, exposure consequences, cold terrain/hazards, slippery movement, temperature-caused damage/status and all Move/Ability/Item/Trainer Feature interactions unless an exact source and engine contract verify them.