# Ouros Science, Research & Discovery Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already stores observations, knowledge, field reports, evidence, claims, ecological state, archaeology, cases, institutional mandates and public information. This layer adds the process that turns those inputs into scientific work without confusing research consensus with canonical truth.

The system is intended to support:
- field ecology;
- Pokémon behavior studies;
- habitat and migration research;
- archaeology/paleontology research handoffs;
- technical investigations;
- medical/ecological pattern studies;
- urban Pokémon studies;
- long-running research programs;
- multiplayer contribution and replication;
- institutions that disagree for understandable reasons.

It does not create a parallel PTU skill system.

## Core separation

Keep these states distinct:

```text
world_truth
  -> observable phenomena
  -> observations / samples / measurements
  -> dataset
  -> hypothesis
  -> analysis
  -> research claim
  -> review / replication
  -> institutional position
  -> publication / public communication
  -> actor knowledge / public memory
```

A publication can be wrong.
A hypothesis can be useful without being true.
A null result can be valuable.
A famous professor can be mistaken.
A correct conclusion can remain unknown to most of the region.

## 1. Research Question

Research begins with a bounded question rather than a predetermined answer.

```yaml
research_question:
  question_id: null
  title: null
  subject_ids: []
  originating_gap_ids: []
  requester_ids: []
  institution_ids: []
  region_ids: []
  question_type: descriptive
  current_status: open
  priority: normal
  ethical_constraints: []
  world_state_dependencies: []
  related_question_ids: []
```

Suggested question types:
- descriptive;
- comparative;
- causal;
- distribution;
- behavioral;
- ecological;
- historical;
- technical;
- clinical_pattern;
- replication;
- anomaly_investigation.

The generator may propose a question from a real knowledge gap or anomaly. It must not silently create the answer.

## 2. Research Program

A program can contain several questions and survive individual missions.

```yaml
research_program:
  program_id: null
  institution_ids: []
  lead_actor_ids: []
  collaborator_ids: []
  scope: null
  active_question_ids: []
  completed_question_ids: []
  dataset_ids: []
  facility_requirements: []
  funding_or_resource_state: null
  field_sites: []
  publication_ids: []
  unresolved_disputes: []
  ethics_constraints: []
  status: active
```

Examples:
- long-term migration monitoring;
- urban adaptation study;
- cave microhabitat survey;
- historical fossil distribution project;
- post-crisis ecological recovery study;
- research into one recurring anomalous phenomenon.

Programs create continuity without requiring every field assignment to be part of the same plot.

## 3. Research Institution

Research institutions are persistent world actors.

```yaml
research_institution:
  institution_id: null
  name: null
  institution_type: null
  settlement_id: null
  mandates: []
  specialties: []
  staff_ids: []
  facility_ids: []
  archives: []
  active_program_ids: []
  partner_ids: []
  rival_ids: []
  access_policy_id: null
  review_model_id: null
  public_reputation: null
  resource_state: null
```

Possible institution types:
- professor_lab;
- field_station;
- university_department;
- museum_research_unit;
- conservation_lab;
- clinic_research_unit;
- civic_environment_office;
- private_research_group;
- club_or_amateur_society.

Institution type is worldbuilding metadata, not mechanical authority.

## 4. Staff Roles and Specialties

Do not make every scientist interchangeable.

```yaml
research_role:
  actor_id: null
  institution_id: null
  specialty_tags: []
  operational_roles: []
  access_scope: []
  mentorship_links: []
  field_authorization: []
  active_project_ids: []
```

Operational roles can include:
- principal investigator;
- field lead;
- observer;
- sample custodian;
- analyst;
- archivist;
- equipment specialist;
- lab technician;
- reviewer;
- research assistant;
- community liaison.

A role does not grant PTU Features. Mechanical capability must be read from the actor's authoritative character state.

## 5. Observation vs Measurement vs Sample

The observation system already stores what an actor saw. Science needs additional provenance when something is measured or physically collected.

```yaml
measurement:
  measurement_id: null
  subject_ids: []
  observer_ids: []
  location_id: null
  timestamp: null
  variable: null
  recorded_value: null
  unit_or_category: null
  method_id: null
  instrument_id: null
  uncertainty: null
  source_refs: []
```

```yaml
research_sample:
  sample_id: null
  sample_type: null
  source_subject_ids: []
  source_location_id: null
  collection_event_id: null
  custody_history: []
  preservation_state: null
  destructive_analysis_allowed: false
  ownership_claim_ids: []
  cultural_or_ecological_constraints: []
  current_location_id: null
```

The existence of this schema does not authorize collection. Collection legality and mechanics require canon/rules support.

## 6. Method

A method records how evidence was produced.

```yaml
research_method:
  method_id: null
  description: null
  target_variable: null
  comparison_structure: null
  required_conditions: []
  exclusion_conditions: []
  equipment_refs: []
  skill_or_feature_refs: []
  disturbance_profile: null
  ethical_constraints: []
  known_limitations: []
  validation_status: proposed
```

Methods can fail because:
- the observation window was wrong;
- the subject was disturbed;
- equipment failed;
- the sample was contaminated;
- comparison conditions were not matched;
- the method cannot distinguish two explanations.

Failure should produce useful information when possible.

## 7. Dataset

A dataset groups provenance-bearing evidence.

```yaml
research_dataset:
  dataset_id: null
  question_ids: []
  contributor_ids: []
  observation_ids: []
  measurement_ids: []
  sample_ids: []
  excluded_record_ids: []
  exclusion_reasons: []
  independence_groups: []
  coverage_summary: {}
  quality_flags: []
  version: 1
  locked: false
```

### Independence rule

Ten observations copied from one report are one source chain, not ten independent confirmations.

The system should track correlated observations through provenance groups.

## 8. Hypothesis

```yaml
research_hypothesis:
  hypothesis_id: null
  question_id: null
  statement: null
  proposer_ids: []
  created_at: null
  predicted_observations: []
  supporting_evidence_ids: []
  conflicting_evidence_ids: []
  alternative_hypothesis_ids: []
  status: active
```

Suggested status values:
- active;
- weakened;
- provisionally_supported;
- unsupported;
- refuted_by_current_data;
- unresolved;
- superseded.

Avoid a single numeric truth meter.

## 9. Analysis Record

```yaml
analysis_record:
  analysis_id: null
  dataset_id: null
  analyst_ids: []
  method_id: null
  question_ids: []
  hypothesis_ids: []
  findings: []
  uncertainty_notes: []
  limitations: []
  reproducible_inputs: []
  outputs: []
  status: draft
```

Analysis can be re-run when datasets change.

## 10. Research Claim

A claim is a statement produced by analysis, not a mutation of world truth.

```yaml
research_claim:
  claim_id: null
  statement: null
  author_ids: []
  supporting_analysis_ids: []
  evidence_ids: []
  confidence_band: provisional
  scope_conditions: []
  contradictory_claim_ids: []
  review_status: unreviewed
  replication_status: unreplicated
```

Confidence bands are narrative labels, not mathematical probabilities unless an authored subsystem later defines them.

## 11. Replication

A strong discovery should be testable through independent routes where appropriate.

```yaml
replication_attempt:
  replication_id: null
  target_claim_id: null
  team_ids: []
  method_id: null
  site_ids: []
  dataset_id: null
  independence_from_original: null
  result: pending
  discrepancy_notes: []
```

Possible outcomes:
- consistent;
- partly_consistent;
- inconsistent;
- inconclusive;
- method_not_comparable.

Replication should create new story opportunities rather than act as a boring repeat button.

## 12. Review and Institutional Position

```yaml
research_review:
  review_id: null
  claim_id: null
  reviewer_ids: []
  institution_id: null
  review_type: internal
  concerns: []
  requested_followups: []
  disposition: pending
```

```yaml
institutional_position:
  institution_id: null
  claim_id: null
  position: no_position
  basis_ids: []
  adopted_at: null
  supersedes_position_id: null
```

Institutions may disagree because they have different data, methods, mandates or thresholds.

Scientific disagreement does not imply corruption.

## 13. Publication

Publication belongs to the existing media/information layer.

```yaml
research_publication:
  publication_id: null
  claim_ids: []
  author_ids: []
  institution_ids: []
  audience: professional
  access: public
  publication_channel_id: null
  released_at: null
  correction_ids: []
  embargo_reason: null
```

Possible access states:
- public;
- professional_only;
- internal;
- embargoed;
- restricted_for_stewardship;
- private_medical;
- sealed_case_evidence.

Embargo/restriction must have an authored reason and authority boundary.

## 14. Negative and Null Results

Research should preserve useful failure.

```yaml
null_result:
  result_id: null
  question_id: null
  method_id: null
  dataset_id: null
  finding: null
  rules_out: []
  remaining_possibilities: []
  followup_questions: []
```

Examples:
- no migration occurs under the predicted weather condition;
- a suspected route contains no evidence of passage;
- two habitats show no meaningful difference under the measured variable;
- an alleged anomaly cannot be reproduced.

Null results can close false leads and reduce future redundant quests.

## 15. Research Ethics and Stewardship

Research must not automatically trump care, custody, sacred-site stewardship or ecology.

```yaml
research_ethics_constraint:
  constraint_id: null
  subject_ids: []
  source_authority_ids: []
  constraint_type: null
  allowed_actions: []
  prohibited_actions: []
  consent_or_permission_refs: []
  expiration_state: null
```

Potential constraints:
- no destructive sampling;
- no capture for study;
- observation only;
- limited visitation window;
- anonymize medical records;
- community steward must be present;
- do not publish nesting coordinates;
- specimen cannot leave institution;
- return borrowed artifact after analysis.

The generator may respect constraints. It may not invent legal authority for them.

## 16. Discovery Event

A discovery becomes world state only in a bounded way.

```yaml
discovery_event:
  discovery_id: null
  claim_ids: []
  triggering_analysis_ids: []
  validated_fact_ids: []
  unresolved_interpretations: []
  institution_ids: []
  world_state_outputs: []
  publication_ids: []
  chronicle_event_id: null
```

Possible outputs:
- update regional guidance;
- alter research opportunity weights;
- open a new field site;
- close an unsafe or sensitive site;
- change a conservation recommendation;
- create a public debate;
- unlock a specialist service;
- start a new institutional project;
- update a museum display;
- generate a case or crisis follow-up.

A discovery should never silently modify Pokémon stats, Moves, Abilities, spawn rates or PTU mechanics.

## 17. Research Standing

Research standing should be separate from fame and combat rank.

Possible dimensions:
- reliability;
- field experience;
- archival contribution;
- replication history;
- collaboration record;
- stewardship trust;
- subject specialization.

The first implementation should use coarse authored bands, not exploitable hidden arithmetic.

Standing can affect:
- invitation to projects;
- access to archives;
- permission to handle sensitive material;
- mentorship opportunities;
- institutional trust;
- who asks the player for help.

It must not grant PTU levels or Features unless an explicit progression rule says so.

## 18. Research Jobs

Research jobs should come from state.

Candidate generators:
- knowledge gap;
- anomalous observation;
- contradictory datasets;
- failed replication;
- infrastructure change;
- ecological shift;
- public claim needing verification;
- new archaeological context;
- clinic pattern;
- disputed specimen provenance;
- missing longitudinal observation;
- outdated regional guide.

Examples of mission verbs:
- observe;
- photograph;
- map;
- compare;
- sample, only if authorized;
- escort field team;
- retrieve equipment;
- validate records;
- replicate;
- interview;
- monitor;
- archive;
- analyze;
- present findings.

## 19. Multiplayer Research

Player knowledge remains private/individual unless shared.

Research collaboration needs explicit contribution records:

```yaml
research_contribution:
  contribution_id: null
  contributor_id: null
  program_id: null
  contribution_type: null
  source_ids: []
  accepted_by: []
  attribution_visible: true
```

The system should support:
- several teams observing different sites;
- independent replication;
- shared equipment;
- division between field and lab roles;
- debate over interpretations;
- coauthored reports;
- later players extending older datasets.

No player can author another player's conclusion, quote or belief without evidence.

## 20. Minecraft Representation

Research should be visible physically without simulating every scientific procedure.

Potential world expressions:
- field stations;
- observation blinds;
- marked transects;
- weather/monitoring equipment;
- specimen cabinets where canon allows them;
- archives and map walls;
- lab benches;
- research notice boards;
- temporary expedition camps;
- changing exhibits;
- instrument repair states;
- restricted doors tied to institutional access;
- NPC teams arriving/leaving during projects.

A lab upgrade should correspond to concrete service/capability changes, not decorative level numbers alone.

## 21. AutoPTU Boundary

Most science play is overworld/world-state logic. Battle-facing research encounters must use encounter implementation contracts.

Narrative research may say:
- protect a field station;
- reach a sensor site;
- observe before disturbing a group;
- retreat with collected records;
- keep combat away from fragile equipment;
- investigate a Move/Ability phenomenon after seeing it legally occur.

It may not say:
- a sensor provides +2 Accuracy;
- a scientist identifies every hidden Ability automatically;
- a research badge grants damage bonuses;
- an observation cancels weather;
- a sample reveals illegal move data;
- a lab device creates a custom status.

## 22. Encounter Contracts

### A. Field Station Disturbance

Narrative premise:

A long-running monitoring station sits near an active wild habitat. A sudden change in local activity threatens equipment and staff, and the players need to determine whether the station caused the disturbance or merely happened to be present.

Full version dependencies:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement, only if the arena uses equipment lanes or displacement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle where selected Pokémon require it;
- terrain/weather/hazards/zones/reactions if environmental state changes during the fight;
- move-specific behavior for selected legal Moves;
- abilities for selected legal Abilities;
- items if any held items are active;
- Trainer Features/perks if field staff mechanically participate;
- AI legal-action infrastructure;
- AI tactical policy for protect/avoid-equipment behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:

Field analysis determines why the station is at risk before combat. Fragile instruments remain outside the tactical grid. AutoPTU runs a standard legal encounter on a static arena; equipment damage and evacuation are resolved as overworld state before/after battle. This preserves the premise without inventing PROTECT_OBJECT or hazard mechanics.

### B. Remote Sensor Retrieval

Narrative premise:

A sensor array contains data from an unusual migration night. The site is now inside a temporarily occupied wild-Pokémon area. The objective is to retrieve the records with minimal disturbance.

Full version dependencies:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception/forced movement if retreat/pursuit matters;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle as required by selected combatants;
- terrain/weather/hazards/zones/reactions if the site has active environmental state;
- move-specific behavior;
- abilities;
- items;
- AI legal-action infrastructure;
- AI tactical policy for territory/retreat priorities;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:

The retrieval itself occurs through exploration/observation outside battle. If a legal encounter triggers, AutoPTU resolves an ordinary static fight or the player withdraws through existing supported overworld logic. The sensor is not a tactical objective token.

### C. Replication at the Weather Platform

Narrative premise:

Two research teams disagree about whether a repeated Pokémon behavior is associated with a particular environmental condition. Players help run an independent observation at a weather platform.

Full version dependencies if battle occurs during the test:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle as required;
- terrain/weather/hazards/zones/reactions for authoritative battlefield weather state;
- move-specific behavior;
- abilities;
- items;
- AI legal-action infrastructure;
- AI tactical policy if actors respond to observation zones/objectives;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:

Weather is world-state context only. The research outcome comes from observations and valid rules-backed field actions. Any battle uses a static legal arena without claiming the test condition changed battle rules. The replication may still succeed, fail or remain inconclusive narratively based on collected evidence.

## 23. Promotion Gates

A research-derived fact may enter future canon only when:

1. its world subject already exists or is separately approved;
2. its evidence/provenance is retained;
3. the claimed result does not contradict established canon;
4. any PTU mechanic used to obtain it was validated;
5. multiplayer/private information boundaries were respected;
6. cultural, medical, custody and stewardship constraints were checked;
7. the fact is scoped correctly and does not overgeneralize from one observation;
8. any resulting Minecraft or AutoPTU behavior is feasible or explicitly deferred.

## Unresolved design questions

- What research institutions actually exist in Ouros canon?
- Are professors formally credentialed, locally recognized, university-affiliated or diverse by region?
- Which PTU/Caelo Researcher/Scientist branches and Education Skill rules will be used?
- What counts as a legal research sample?
- Can research standing unlock areas independently of Trainer Level/Badges?
- How are sensitive habitat coordinates protected in multiplayer?
- Does research time advance while players are offline?
- Which measurements can be read directly from Cobblemon/AutoPTU state?
- Can players propose free-text hypotheses, and if so how are they sandboxed from canonical mutation?
- How should conflicting institutions resolve disputes without a universal truth UI spoiling mysteries?
