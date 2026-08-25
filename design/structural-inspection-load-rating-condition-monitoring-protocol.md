# Structural Inspection, Load Rating, and Condition Monitoring Protocol

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

Date: 2026-08-25

Authority note: this protocol extends `design/architecture-built-environment-adaptive-reuse-layer.md` and `design/civic-governance-public-works-layer.md`.

Architecture remains authoritative for `structure_id`, physical versions, coarse condition, use history and built-environment identity. Public Works remains authoritative for projects, implementation and repair/replacement work. Hydrology/Fluvial layers remain authoritative for water and channel state. Travel/transport layers remain authoritative for route/service consequences.

This protocol owns the evidence and assessment lifecycle between those systems.

## Purpose

Important structures should accumulate technical history without becoming engineering minigames or binary `SAFE/UNSAFE` props.

The protocol defines:

- inspection programs;
- inspection events;
- element/zone observations;
- defect observations;
- engineering assessments;
- scoped capacity/load assessments;
- operational restrictions justified by those assessments;
- special inspections after events;
- structural monitoring series;
- repair verification and reinspection;
- evidence handoff to Architecture, Public Works, Travel and Crisis.

## Core separation

```text
BUILT_STRUCTURE
  -> PHYSICAL VERSION / CURRENT USE
  -> INSPECTION PROGRAM
  -> INSPECTION EVENT
  -> OBSERVATIONS / MEASUREMENTS
  -> ENGINEERING ASSESSMENT
  -> CAPACITY OR SERVICEABILITY ASSESSMENT
  -> OPERATIONAL RESTRICTION / CONTINUE SERVICE
  -> PUBLIC-WORKS REPAIR OR MONITORING
  -> REINSPECTION / VERIFICATION
  -> REVISED ASSESSMENT
```

Critical no-inferences:

```text
visible crack != imminent collapse
rust / wear != root cause
routine inspection completed != permanently safe
repair work completed != verified capacity restored
bridge open != unrestricted for every load/user
bridge restricted != structure condemned
structure closed != structure destroyed
poor-looking Minecraft blocks != engineering failure
intact-looking blocks != engineering safety
flood occurred != scour damage confirmed
sensor alert != structural failure confirmed
sensor silence != structure stable
load restriction != PTU movement/status penalty
battle damage near structure != structural condition writeback
winning battle != structure safe
```

## STRUCTURAL_INSPECTION_PROGRAM

```yaml
structural_inspection_program:
  inspection_program_id: null
  structure_id: null
  owner_or_steward_refs: []
  authorized_inspection_body_refs: []
  scope_zone_refs: []
  inspection_types_supported: []
  current_program_revision_id: null
  monitoring_series_refs: []
  source_refs: []
  canon_status: PROPOSED
```

Inspection types are descriptive until Ouros authors institutions and methods. Candidate types include routine, detailed, underwater, post-event/special, repair-verification and targeted follow-up.

No real-world statutory interval is imported.

## INSPECTION_EVENT

```yaml
inspection_event:
  inspection_event_id: null
  inspection_program_id: null
  structure_id: null
  structure_version_id: null
  inspection_type: null
  started_at: null
  completed_at: null
  inspector_or_team_refs: []
  scope_zone_refs: []
  access_method_refs: []
  environmental_context_refs: []
  instrument_refs: []
  observation_ids: []
  inaccessible_zone_refs: []
  limitations: []
  result_status: COMPLETE
```

Suggested result states:

- COMPLETE
- COMPLETE_WITH_LIMITATIONS
- PARTIAL
- ABORTED_FOR_SAFETY
- ACCESS_BLOCKED
- DATA_QUALITY_REVIEW
- REQUIRES_SPECIALIST_FOLLOWUP

An incomplete inspection is history, not a failed quest.

## STRUCTURAL_ELEMENT_OBSERVATION

The protocol can reference authored zones/elements without requiring a finite-element model.

```yaml
structural_element_observation:
  observation_id: null
  inspection_event_id: null
  structure_id: null
  zone_or_element_ref: null
  observation_type: null
  observed_state: null
  qualitative_extent: null
  measurement_refs: []
  media_refs: []
  prior_comparison_refs: []
  confidence: null
  interpretation_status: OBSERVED_ONLY
```

Candidate observations include cracking, section loss/corrosion, deformation, displacement, loose/missing component, water intrusion, joint condition, bearing condition, foundation exposure, streambed change, impact mark, fire damage, settlement, scour evidence or simply `NO_RELEVANT_CHANGE_OBSERVED`.

The observation does not own causation.

## DEFECT_OR_ANOMALY_RECORD

```yaml
defect_or_anomaly_record:
  defect_record_id: null
  structure_id: null
  first_observation_id: null
  subsequent_observation_ids: []
  affected_zone_refs: []
  description: null
  current_extent_assessment: null
  change_direction: UNKNOWN
  causal_hypothesis_refs: []
  assessment_refs: []
  repair_refs: []
  status: OPEN
```

A record may survive multiple inspections.

Suggested status values:

- OPEN
- MONITORING
- STABLE_WITHIN_OBSERVED_LIMITS
- CHANGED
- REPAIRED_PENDING_VERIFICATION
- VERIFIED_REPAIRED_FOR_SCOPE
- SUPERSEDED_ASSESSMENT
- UNRESOLVED

Never label a defect `structural_failure_cause` without separate evidence.

## ENGINEERING_ASSESSMENT

```yaml
engineering_assessment:
  assessment_id: null
  structure_id: null
  assessment_type: null
  evidence_refs: []
  method_or_reference_revision: null
  assumptions: []
  excluded_scope: []
  resulting_claim_ids: []
  uncertainty_notes: []
  authored_decider_ref: null
  assessed_at: null
  status: PROVISIONAL
```

Assessment types can include condition, capacity, serviceability, post-event, foundation/scour vulnerability, repair verification and monitoring review.

Suggested states:

- PROVISIONAL
- ACTIVE
- ACTIVE_WITH_LIMITATIONS
- REQUIRES_MORE_DATA
- CONTESTED
- SUPERSEDED
- UNRESOLVED

An assessment is an interpretation supported by evidence. It never overwrites the observations.

## LOAD_OR_CAPACITY_ASSESSMENT

Ouros may need scoped capacity without simulating structural mechanics.

```yaml
load_capacity_assessment:
  capacity_assessment_id: null
  structure_id: null
  engineering_assessment_id: null
  load_or_use_scope_ref: null
  assessment_band: null
  numeric_value: null
  unit_system_ref: null
  method_revision: null
  relevant_condition_refs: []
  assumptions: []
  status: null
```

Default narrative implementation should prefer qualitative or authored bands unless numeric capacity is needed by canon.

Examples of scopes:

- ordinary pedestrian use;
- standard local road service;
- specific authored transit vehicle class;
- freight above an authored threshold;
- emergency-service vehicle class;
- event crowd loading where canon supports evaluation;
- temporary construction loading.

This protocol does not calculate those loads from Minecraft entities.

## OPERATIONAL_RESTRICTION

Restriction is separate from condition.

```yaml
structural_operational_restriction:
  restriction_id: null
  structure_id: null
  basis_assessment_refs: []
  authority_ref: null
  scope_type: null
  affected_user_or_vehicle_refs: []
  allowed_use_refs: []
  prohibited_use_refs: []
  effective_from: null
  review_trigger_refs: []
  detour_or_alternative_route_refs: []
  public_information_ref: null
  status: ACTIVE
```

Possible scopes include load/vehicle class, lane/zone, speed/operation, occupancy, temporary closure or complete closure. These are authored operational concepts, not imported traffic law.

Architecture stores resulting access/condition state. Travel and transport systems decide which journeys remain feasible.

## POST_EVENT_SPECIAL_INSPECTION

Special inspection can be triggered by another authoritative world event.

```yaml
special_inspection_trigger:
  trigger_id: null
  structure_id: null
  source_event_ref: null
  trigger_type: null
  observed_or_expected_affected_zone_refs: []
  urgency_band: null
  temporary_control_refs: []
  required_inspection_scope: []
  status: OPEN
```

Candidate triggers:

- flood/high flow;
- earthquake/ground movement;
- wildfire/fire exposure;
- vehicle/vessel impact;
- nearby construction incident;
- unusual deformation observation;
- monitoring threshold crossing;
- major storm/wind event;
- collision or debris strike.

The trigger never supplies the conclusion.

## SCOUR / FOUNDATION HANDOFF

For structures over water:

```text
Freshwater / Fluvial state
  -> streambed / flow observations
  -> Metrology-backed measurement
  -> structural foundation/scour assessment
  -> restriction / monitoring / public works decision
```

A transient scour hole may partially refill before a later visit. Chronicle should preserve the earlier observation or monitoring series.

The protocol must never infer foundation safety from a calm water surface.

## STRUCTURAL_MONITORING_SERIES

```yaml
structural_monitoring_series:
  monitoring_series_id: null
  structure_id: null
  target_zone_refs: []
  instrument_or_observation_method_refs: []
  deployment_refs: []
  measurement_series_refs: []
  expected_sampling_pattern: null
  outage_or_gap_refs: []
  alert_threshold_refs: []
  review_event_refs: []
  current_status: ACTIVE
```

Metrology owns calibration/measurement traceability. Timekeeping owns clocks. Remote sensing or Photography owns relevant source records. This protocol only links those observations to a structural question.

A threshold alert creates review. It does not create damage.

## REPAIR_VERIFICATION

```yaml
repair_verification:
  verification_id: null
  structure_id: null
  public_works_project_ref: null
  repaired_zone_refs: []
  completion_record_refs: []
  verification_inspection_ref: null
  remaining_defect_refs: []
  capacity_reassessment_ref: null
  restriction_review_ref: null
  result: PENDING
```

Possible results:

- VERIFIED_FOR_SCOPE
- VERIFIED_WITH_REMAINING_LIMITATIONS
- ADDITIONAL_WORK_REQUIRED
- MONITORING_REQUIRED
- REASSESSMENT_REQUIRED
- UNRESOLVED

A contractor marking work complete cannot automatically reopen the route.

## Longitudinal structure history

The same bridge or building can accumulate:

- multiple physical versions;
- dozens of inspections;
- defects that appear stable for years;
- restrictions that change without visible reconstruction;
- repairs that address only one component;
- revised assessment methods;
- instrument upgrades;
- historic photographs showing prior conditions;
- a transport network that adapts around it.

This allows Chronicle to produce callbacks without requiring repeated disasters.

## Public information

Public Memory/Media can receive simplified states such as:

- open normally;
- open with authored restriction;
- temporary closure pending inspection;
- repair underway;
- reopened after verification.

Public wording does not replace the technical record.

A rumor that “the bridge is about to collapse” remains a claim unless evidence supports it.

## Minecraft projection

Minecraft may render:

- cracks or patches;
- temporary shoring;
- barriers;
- closed lanes;
- scaffolding;
- repair works;
- inspection platforms;
- exposed foundations;
- altered signage.

Minecraft cannot authoritatively decide:

- structural adequacy;
- capacity;
- load rating;
- inspection completeness;
- crack severity;
- failure probability;
- scour depth;
- whether a repair is verified;
- whether the structure should reopen.

Block hardness, entity weight, redstone state or chunk loading must not become structural-analysis inputs unless a future authored subsystem explicitly defines such a handoff.

## PTU mechanical boundary

Do not infer:

- Technology Education = structural-engineering license;
- Groundshaper = foundation repair;
- Mold the Earth = structural stabilization;
- Power/Strength = bridge capacity;
- Rock/Steel/Ground typing = engineering suitability;
- a Move damaging Minecraft blocks = structure damage under this protocol;
- a repair scene = Trainer Feature or crafting reward;
- shoring = Cover/DR without an exact battle contract.

If a battle includes an actual moving collapse, falling deck, push into a gap, unstable surface, debris zone or reaction to structural failure, those mechanics must depend on the exact battle capability families rather than being implemented in Minecraft.

## Cross-system handoffs

Architecture:

- owns persistent structure identity and physical version;
- receives coarse condition/access changes justified by assessments.

Public Works:

- owns repair, strengthening, replacement and inspection-support projects.

Travel / Rail / Road Transit / Emergency Services:

- consume scoped route restrictions and alternative connections.

Freshwater / Fluvial / Stormwater / Seismic / Wildfire:

- own environmental event/state that may trigger inspection.

Metrology / Timekeeping / Photography / Remote Sensing:

- own measurement and observation provenance.

Cases / Institutional Review:

- own any misconduct, dispute or formal review. A defect or late repair does not prove wrongdoing.

## World-state implementation blockers

Outside battle parity, Ouros still needs:

- persistent inspection-program state;
- structure-zone/element references appropriate to narrative scale;
- observation/defect history;
- assessment revision history;
- restriction and reopening workflow;
- repair-verification handoff;
- bridge/foundation monitoring links;
- transport rerouting response;
- public-information projection;
- Minecraft representation without block-based structural authority.

## Canon questions intentionally unresolved

- Which structures require formal inspection in each Ouros region?
- Which institutions can issue restrictions or reopenings?
- Does Ouros use numerical load ratings or qualitative service classes?
- Which bridges/towers/halls already have long inspection histories at campaign start?
- What engineering technologies and nondestructive methods exist?
- Which rivers create known scour concerns?
- How are heritage constraints balanced with strengthening/replacement?
- Can player institutions own or steward inspectable structures?
- Which PTU/Caelo Skills or Features apply to technical investigation, and only under what exact rules?

The complete Caelo source corpus was not recovered reliably in this pass. Super PTU Online Helper was not available as an invocable capability. No rules are invented from either.