# Ouros Community Health Surveillance & Cluster Investigation Continuity Extension

Status: PROPOSED systems design. Not established Ouros canon.

## Purpose

This extension preserves community-level health evidence across time without becoming a medical rules engine.

It owns the investigation bridge between isolated observations and downstream owner systems:

signal intake -> cluster candidate -> working scope -> evidence gathering -> hypothesis revision -> notices/handoffs -> follow-up -> closure or durable legacy.

It does not diagnose patients, invent contagion, apply status conditions, prescribe treatment, create quarantine law or decide environmental/product causation.

## Authority boundary

This extension owns:

- community-health signal references;
- cross-source pattern/cluster candidates;
- versioned working case definitions for investigation scope;
- surveillance classifications used only for the investigation;
- exposure/common-source hypotheses;
- source and transmission hypotheses with confidence/provenance;
- monitoring gaps;
- investigation milestones;
- aggregate/public-safe summaries;
- notification/handoff records;
- closure/revision history;
- legacy investigation records.

It does not own:

- diagnosis, treatment, healing, medical readiness or patient discharge — Care;
- HP, Injury, status, mechanical recovery or item effects — PTU/Caelo + AutoPTU;
- product/batch hold, quarantine, recall or correction — Batch Traceability;
- food-service state — Food/Agriculture/Hospitality;
- drinking-water, wastewater, pollution, air, workplace or facility operational truth — their owning systems;
- wild-Pokémon ecological interpretation — Ecology/Conservation;
- emergency evacuation/shelter coordination — Crisis/Rescue;
- public delivery of alerts — Communications/Public Notices;
- formal allegations, warrants, culpability or evidence custody — Case/Authority;
- legal public-health authority, mandatory isolation or regional regulation — undecided canon.

## Core invariants

`HEALTH_SIGNAL != CASE`

`SURVEILLANCE_CLASSIFICATION != DIAGNOSIS`

`CLUSTER_CANDIDATE != OUTBREAK_CONFIRMED`

`COMMON_EXPOSURE_HYPOTHESIS != CAUSE_ESTABLISHED`

`CONTACT_IDENTIFIED != EXPOSURE_CONFIRMED`

`EXPOSURE_SUPPORTED != TRANSMISSION_PROVEN`

`NOTICE_AUTHORIZED != NOTICE_DELIVERED`

`NOTICE_DELIVERED != NOTICE_UNDERSTOOD`

`CONTROL_ACTION_ACTIVE != SOURCE_CONFIRMED`

`NO_NEW_REPORTS != INVESTIGATION_CLOSED`

`INVESTIGATION_CLOSED != CAUSE_KNOWN`

`PUBLIC_AGGREGATE != PRIVATE_CASE_RECORD`

These distinctions are mandatory because a health investigation can create strong narrative pressure while still containing uncertainty.

## Community health signal

A signal is a bounded observation or aggregate from an existing owner system.

```yaml
community_health_signal:
  signal_id: null
  source_system_ref: null
  source_record_refs_private: []
  reporting_actor_or_institution_id: null
  observation_scope:
    location_refs: []
    time_window_ref: null
    subject_population_ref: null
  observed_pattern_tags: []
  aggregate_count_band_ref: null
  individual_identity_visibility: PROTECTED
  source_confidence: null
  received_at: null
  related_signal_refs: []
  status: RECEIVED
```

A signal can originate from:

- a clinic aggregate;
- repeated care observations;
- a shelter;
- workplace or school absence/observation patterns if those systems exist and privacy permits;
- food or market complaints;
- environmental observations;
- wildlife health observations;
- an authored laboratory/science result;
- a public report requiring verification;
- a previous investigation callback.

A signal is not automatically evidence of infection.

## Cluster candidate

```yaml
health_cluster_candidate:
  cluster_id: null
  opened_at: null
  opened_by_ids: []
  source_signal_ids: []
  current_scope_revision_id: null
  current_case_definition_id: null
  classification_summary_refs: []
  hypothesis_ids: []
  monitoring_gap_ids: []
  downstream_handoff_ids: []
  public_summary_ref: null
  status: SIGNAL_REVIEW | INVESTIGATING | MONITORING | CLOSING | CLOSED
  closure_id: null
```

The cluster may later be:

- supported as one shared event;
- split into multiple unrelated events;
- narrowed;
- expanded;
- reclassified as a noninfectious common exposure;
- handed to a product/environment owner;
- closed with insufficient evidence.

No path requires an outbreak conclusion.

## Working case definition

This is an investigation filter, not a diagnosis.

```yaml
working_case_definition:
  definition_id: null
  cluster_id: null
  revision_number: null
  parent_definition_id: null
  effective_at: null
  authored_by_ids: []
  subject_scope_tags: []
  place_criteria_refs: []
  time_criteria_refs: []
  observation_criteria_refs: []
  exclusion_criteria_refs: []
  evidence_requirements: []
  known_limitations: []
  rationale_refs: []
  status: ACTIVE | SUPERSEDED | RETIRED
```

Earlier definitions remain historical.

A record classified under v1 may be excluded under v2 without rewriting history. The investigation records the reclassification event.

## Surveillance classification

```yaml
surveillance_classification:
  classification_id: null
  cluster_id: null
  subject_record_ref_private: null
  case_definition_id: null
  classification: INCLUDED | EXCLUDED | POSSIBLE | PENDING | INSUFFICIENT_DATA
  evidence_refs: []
  classified_by_ids: []
  classified_at: null
  prior_classification_ref: null
  privacy_scope: INVESTIGATION_RESTRICTED
```

This classification must never write a diagnosis or tactical status.

## Hypothesis graph

Health mysteries need multiple competing explanations without pretending that one has secretly been selected by the generator.

```yaml
health_investigation_hypothesis:
  hypothesis_id: null
  cluster_id: null
  hypothesis_type: COMMON_EXPOSURE | PERSON_TO_PERSON | POKEMON_TO_POKEMON | CROSS_SPECIES | PRODUCT_RELATED | FOOD_RELATED | WATER_RELATED | AIR_OR_ENVIRONMENTAL | WORKPLACE | FACILITY | ECOLOGICAL | MULTIPLE_CAUSES | NONRELATED_CASES | OTHER_AUTHORED
  claim_summary: null
  evidence_for_refs: []
  evidence_against_refs: []
  unknown_refs: []
  source_system_handoff_refs: []
  confidence: UNSPECIFIED
  status: OPEN | SUPPORTED | WEAKENED | REJECTED | UNRESOLVED
  updated_at: null
```

The presence of a hypothesis never grants a mechanic.

`PERSON_TO_PERSON`, `POKEMON_TO_POKEMON` and `CROSS_SPECIES` may be used only when the authored condition and governing setting evidence permit such a transmission hypothesis.

## Exposure event

An exposure record is evidence about overlap with a candidate source or setting. It does not automatically mean transmission.

```yaml
possible_exposure_event:
  exposure_event_id: null
  cluster_id: null
  subject_ref_private: null
  candidate_source_ref: null
  location_id: null
  start_time_ref: null
  end_time_ref: null
  evidence_refs: []
  exposure_definition_ref: null
  classification: POSSIBLE | SUPPORTED | NOT_SUPPORTED | UNKNOWN
  privacy_scope: INVESTIGATION_RESTRICTED
```

Never derive this record simply from Minecraft proximity, chunk co-presence or nearby entities.

## Contact tracing boundary

Some authored conditions may support a contact graph. Many will not.

```yaml
contact_investigation_record:
  contact_record_id: null
  cluster_id: null
  source_subject_ref_private: null
  contact_subject_ref_private: null
  governing_contact_definition_ref: null
  identification_evidence_refs: []
  notification_handoff_ref: null
  followup_refs: []
  release_or_closure_ref: null
  status: IDENTIFIED | REVIEWED | NOTIFIED | FOLLOWUP | CLOSED
```

The object may exist only when an exact authored condition or canon institution defines why contact identification is appropriate.

It does not establish infection.

## Monitoring gap

```yaml
health_monitoring_gap:
  gap_id: null
  cluster_id: null
  source_or_location_ref: null
  gap_start: null
  gap_end: null
  reason: UNKNOWN | REPORTING_DELAY | SYSTEM_OFFLINE | STAFF_UNAVAILABLE | COVERAGE_NOT_ESTABLISHED | RECORDS_UNAVAILABLE | OTHER_AUTHORED
  expected_signal_types: []
  observed_signal_types: []
  inference_limitations: []
  status: OPEN | DOCUMENTED | RESOLVED
```

No reports during a gap do not establish no cases.

## Investigation timeline

The investigation should support parallel work.

Suggested milestone types:

- SIGNAL_RECEIVED
- DUPLICATE_SIGNAL_RECONCILED
- CLUSTER_OPENED
- DEFINITION_REVISION_CREATED
- RECORD_CLASSIFIED
- HYPOTHESIS_OPENED
- HYPOTHESIS_WEAKENED
- HYPOTHESIS_SUPPORTED
- MONITORING_GAP_IDENTIFIED
- OWNER_SYSTEM_HANDOFF_CREATED
- NOTICE_REQUESTED
- PUBLIC_AGGREGATE_UPDATED
- CASE_SCOPE_SPLIT
- CASE_SCOPE_MERGED
- FOLLOWUP_REVIEWED
- INVESTIGATION_CLOSED
- INVESTIGATION_REOPENED

This is an event log rather than a linear quest state.

## Owner-system handoffs

A health investigation should route consequences to the owner that can legally and mechanically decide them.

### Care

May receive:

- aggregate signal;
- affected population scope;
- authored concern;
- referral need;
- notice of possible common exposure.

Care decides diagnosis/treatment/readiness.

### Batch Traceability

May receive:

- suspected product/batch refs;
- usage/distribution evidence;
- affected locations;
- investigation scope.

Batch Traceability decides hold/quarantine/recall/correction under its own authority.

### Food

May receive a food-service or ingredient hypothesis. Food systems decide operational response.

### Water / Wastewater / Pollution / Facilities / Workplace

May receive a candidate location, asset, exposure or inspection need. Each system records its own observations and state.

### Ecology / Conservation

May receive wildlife health patterns or potential shared-environment questions. It decides ecological interpretation.

### Crisis

May receive a confirmed or sufficiently authorized emergency condition that requires evacuation, shelter, surge care or regional coordination. This layer does not itself activate crisis authority.

### Communications

Receives approved public or direct notice content plus audience and privacy rules. Sent/delivered/received remain distinct.

### Case/Authority

Receives a formal allegation only when evidence and valid authority justify one. A cluster does not imply negligence, sabotage, concealment or wrongdoing.

## Public summary

```yaml
health_public_aggregate:
  aggregate_id: null
  cluster_id: null
  definition_revision_ref: null
  geographic_scope_refs: []
  time_scope_ref: null
  summary_band_refs: []
  verified_public_facts: []
  explicit_unknowns: []
  advice_or_action_notice_refs: []
  privacy_review_ref: null
  published_at: null
```

No private subject IDs belong in this object.

The public record can say that an investigation exists without naming patients or claiming a cause.

## Notice semantics

A public or direct notice needs its own delivery evidence.

Useful states:

- DRAFTED
- AUTHORIZED
- HANDED_TO_DELIVERY_SYSTEM
- DELIVERED_TO_CHANNEL
- RECEIPT_SUPPORTED
- SUPERSEDED
- WITHDRAWN

A changed notice does not erase the older version. It remains part of public memory and can explain later confusion.

## Precautionary action under uncertainty

Ouros must permit reasonable temporary action without converting it into causal proof.

Examples:

- a room is closed pending inspection;
- an event is relocated;
- a batch is held;
- a water point is not used pending review;
- a clinic redirects nonurgent traffic;
- a wildlife area receives observation-only access restrictions.

The owning system records the action. The health layer records that the action was taken while a hypothesis remained unresolved.

`PRECAUTION_TAKEN != CAUSE_CONFIRMED`.

## Investigation closure

```yaml
health_cluster_closure:
  closure_id: null
  cluster_id: null
  final_definition_ref: null
  final_classification_summary_refs: []
  final_hypothesis_states: []
  supported_source_or_cause_refs: []
  unresolved_questions: []
  downstream_open_items: []
  followup_schedule_refs: []
  public_correction_or_summary_refs: []
  closed_by_ids: []
  closed_at: null
  closure_type: SOURCE_SUPPORTED | MULTIPLE_CAUSES | NO_COMMON_CAUSE_SUPPORTED | INSUFFICIENT_EVIDENCE | TRANSFERRED_TO_OTHER_AUTHORITY | OTHER_AUTHORED
```

Closure does not require a satisfying culprit.

## Reopening

An investigation can reopen when new evidence appears.

```yaml
health_cluster_reopening:
  reopening_id: null
  prior_closure_id: null
  new_signal_refs: []
  rationale_refs: []
  reopened_at: null
  new_definition_ref: null
```

The old closure remains historically valid based on the evidence then available.

## Institutional memory

Long-term persistence can include:

- revised intake forms;
- a new reporting relationship between two clinics;
- a temporary observation desk that became permanent;
- a market changing supplier checks;
- a community event moving location seasonally;
- a wildlife team adding a recurring survey;
- a public notice becoming a local reference point;
- an old cluster file being taught to new staff;
- a neighborhood remembering an incorrect early rumor even after correction.

No automatic trust or reputation modifier follows without a separate social rule.

## Pokémon observations

Pokémon can be part of the evidence without being magical sensors or automatic culprits.

Valid observations:

- several persistent wild actors stopped using one feeding area;
- one clinic saw similar signs in multiple known Pokémon;
- a specific Pokémon repeatedly avoided a room;
- a working Pokémon's routine changed at a documented time;
- a collective returned after an environmental repair.

Invalid automatic inference:

- Poison-type present -> contamination source;
- Psychic-type present -> diagnosed everyone;
- Chansey present -> treatment succeeded;
- Absol appeared -> outbreak predicted;
- Steel-type unaffected -> universal immunity;
- wild Pokémon left -> disease confirmed.

Species, Move, Ability, Item or Feature effects require exact source support.

## Mystery grammar

Strong mysteries use chronology and scope rather than secret omniscience.

Patterns:

- one clinic counts six cases while another says four because their case definitions differ;
- apparent common food exposure disappears when batch history is checked;
- a cluster maps to one building but the shared event happened elsewhere;
- two symptom patterns initially grouped together later split into unrelated causes;
- a public notice remains technically accurate but becomes misleading after scope changes;
- an apparent monitoring lull overlaps a reporting outage;
- wildlife and human reports share geography but not timing;
- a suspected species is only present because the same environmental change displaced it.

## Quest grammar

Useful verbs:

- VERIFY_REPORT
- RECONCILE_RECORDS
- MAP_TIMELINE
- CHECK_LOCATION
- TRACE_SHARED_ACTIVITY
- DELIVER_PRIVATE_RECORD
- LOCATE_WITNESS
- INSPECT_ACCESS
- COMPARE_MAPS
- SUPPORT_FIELD_STATION
- RESTORE_REPORTING_LINK
- HANDOFF_SAMPLE_OR_RECORD
- PUBLISH_CORRECTION
- VERIFY_NOTICE_RECEIPT
- FOLLOW_UP

Do not generate `CURE_CLUSTER`, `STOP_INFECTION`, `DIAGNOSE_ALL`, `DISINFECT_AREA` or `QUARANTINE_ACTOR` unless the governing rule and authority actually support that action.

## Encounter 1 — Field Observation Site Withdrawal

Narrative premise:

A temporary observation site has collected useful records, but an unrelated legitimate Pokémon threat makes the immediate perimeter unsafe. Staff must withdraw while preserving already gathered evidence.

### Full intended version

The encounter can include protected withdrawing staff, multiple exits, an evidence handoff, Intercept around escape lanes and an AI objective that values withdrawal/protection rather than only defeat.

If the site contains an active exposure zone, that zone adds separate hazard/status dependencies and must have an exact governing PTU/Caelo rule.

### Capability dependencies

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL if withdrawal windows or phased access matter
- full stateful damage pipeline — PARTIAL if a verified environmental damage source exists
- status lifecycle — PARTIAL if a verified condition is used
- terrain/weather/hazards/zones/reactions — BLOCKING for generalized reaction/exposure-zone behavior
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW behavior
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

### Reduced version

Staff finish the evidence handoff and withdraw before BattleSpec. Private records and samples, if canonically present, are sealed in world state and removed from the grid. The battle occurs on a reviewed static perimeter with only explicit combatants. Victory can establish `IMMEDIATE_SITE_PERIMETER_SECURED`. It cannot classify a case, prove exposure, preserve a sample automatically or close the investigation.

## Encounter 2 — Clinic Annex Access Perimeter

Narrative premise:

A clinic annex handling increased intake has an unrelated active threat at an external service entrance. The goal is to restore safe physical access without turning patients into tactical objectives.

### Full intended version

A richer future encounter might use staff withdrawal, protected access lanes, reactions, temporary restricted cells and objective-aware opponents.

The health investigation itself remains outside combat. No illness or patient state is a battle hazard unless a governing mechanic explicitly says so.

### Dependencies

The full version uses the same permanent categories above. Complete movement remains PARTIAL; terrain/weather/hazards/zones/reactions, tactical policy and adapter/playback remain BLOCKING. Damage/status families are relevant only for exact verified effects.

### Reduced version

Patients and staff are moved behind an authored safe boundary before battle. The annex entrance becomes a static arena. Winning clears only the immediate access perimeter. Care decides whether the annex can resume service; the health investigation decides none of the clinical questions.

## Encounter 3 — Records Transfer Diversion

Narrative premise:

A courier transporting restricted investigation records or authored samples is forced to stop because a legitimate battle threat blocks a reviewed route.

### Full intended version

Could support escape/escort objectives, Intercept, multiple exit paths, protected cargo state, tactical AI and semantic playback.

### Reduced version

The courier reaches a secure off-grid holding point before combat. Cargo remains governed by Courier/Science/Cold Chain as applicable. AutoPTU resolves a static conventional fight. Victory opens the route for a later authoritative transfer; it does not complete custody or validate the material.

## Exploration — The Clinic Ledger That Changed the Map

Current profile: EXECUTABLE AS WORLD EXPLORATION.

Premise:

An old clinic's aggregate register, a market calendar, renovation records and route timetables show that several cases once thought to share a neighborhood actually overlapped at a temporary event site that no longer exists.

Current implementation needs:

- persistent locations and aliases;
- dated documents;
- public/private access rules;
- actor testimony;
- chronology;
- map overlays;
- explicit provenance.

It does not need infection mechanics, status effects, exposure zones or dynamic disease simulation.

## Long arc — A Town Learns How to Compare Notes

Status: NON-CANON proposal pattern.

Phase 1 establishes ordinary clinics, workplaces, schools/markets, wildlife teams and community routines before any cluster exists.

Phase 2 introduces small observations that remain local to their source systems.

Phase 3 creates a legitimate cross-source cluster candidate. Definitions and hypotheses change as evidence accumulates.

Phase 4 may identify a supported source, several unrelated causes or no common cause. Temporary actions alter routines and create new relationships.

Phase 5 restores ordinary operation system by system. Some temporary reporting links or community practices remain.

Months or years later, another signal causes staff to reopen the old archive. The useful legacy is better provenance and institutional relationships, not a global `health_readiness_level`.

## PTU/Caelo boundary

This extension never invents:

- generic disease checks;
- transmission distance;
- infection probability;
- incubation timers;
- contagiousness windows;
- automatic status conditions;
- environmental exposure damage;
- disease-based movement penalties;
- species/type immunity;
- diagnosis skill DCs;
- universal treatment actions;
- quarantine mechanics;
- illness-driven initiative effects;
- symptom-triggered AI behavior.

If a future authored condition requires any of these, the exact governing source and current engine implementation must be reviewed first.

## Minecraft/Cobblemon/Craftics boundary

Safe presentation can include facilities, field tents, desks, sealed containers, notice boards, NPC routines, queues, signs, barriers, Pokémon, particles and UI.

Unsafe authority includes:

- proximity-based infection from entity distance;
- Minecraft potion effects standing in for PTU disease/status;
- particle collision applying symptoms;
- Cobblemon healing deciding narrative case closure;
- native pathfinding deciding exposure history;
- chunk presence defining contacts;
- Minecraft damage proving illness severity;
- Cobblemon battle-state data choosing health classifications.

Ouros owns persistent investigation facts. PTU/AutoPTU own mechanical health and battle truth. Minecraft/Cobblemon/Craftics present the result.

## Canon approval questions

Before this becomes canon, human review must establish:

- whether Ouros has formal community-health institutions and what they are called;
- which actors may receive protected case information;
- whether any conditions are reportable and by whose authority;
- privacy expectations for humans, Trainers and Pokémon;
- whether wild-Pokémon health surveillance is institutionalized or local/ad hoc;
- what laboratories or testing institutions exist;
- whether quarantine/isolation powers exist anywhere in canon;
- how regional variation works;
- which historical health events, if any, actually occurred;
- what role Pokémon may legitimately play in detection, care or field work.

Until approved, all institution names and workflows remain proposed architecture only.

## Design outcome

This extension gives Ouros a durable way to tell health-investigation stories based on evidence, uncertainty, privacy and institutional coordination. It prevents a single clinic signal, Pokémon observation, product concern or Minecraft visual from becoming an omniscient diagnosis or contagion simulation, while still allowing meaningful quests, mysteries and long-term consequences.