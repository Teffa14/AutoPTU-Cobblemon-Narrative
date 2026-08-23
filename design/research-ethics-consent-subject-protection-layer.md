# Ouros Research Ethics, Consent & Subject Protection Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

The Science layer owns research questions, methods, datasets, hypotheses, analyses, claims, replication and publication handoffs.

Pokémon Agency owns persistent Pokémon identity, associations, custody, observed cooperation/refusal and mechanical relationship boundaries.

Care owns treatment and welfare state. Conservation owns protected ecological state and stewardship. Psychic Information owns private mental information. Institutional Review owns bounded review procedures when an authored institution has mandate.

This layer connects those systems around one question:

What research activity is permitted to occur, on which subject/site/data/sample, under what scope, and what happens when that scope changes or must stop?

It does not create a universal ethics board, research law, animal-welfare statute, medical-research regime or Pokémon-consent mechanic.

## 1. Hard separations

The generator must preserve these distinctions:

- scientifically useful != authorized;
- scientifically valid != ethically acceptable;
- institution permits site access != participant consents;
- participant consents != every future use of data or samples;
- Trainer agrees != Pokémon mechanically or narratively consents;
- custodian agrees != ownership is established;
- ownership claim != unlimited research authority;
- capture legality != research authorization;
- access permission != collection permission;
- collection permission != destructive-analysis permission;
- observation != handling;
- handling != treatment;
- treatment != research;
- public place != unrestricted research site;
- public battle record != private medical data;
- observed cooperation != permanent consent;
- refusal != hostility;
- withdrawal != disobedience;
- protocol deviation != misconduct;
- adverse event != proof of negligence;
- successful procedure != acceptable procedure;
- publication != consent to publicity;
- null result != failed research;
- battle victory != research finding;
- mechanical Status != ethical harm assessment;
- narrative distress != PTU Status unless authoritative rules create one.

## 2. Research protocol

Science owns `research_method`. This layer adds the authorized procedure envelope around one or more methods.

```yaml
research_protocol:
  protocol_id: null
  project_or_program_ids: []
  research_question_ids: []
  lead_institution_id: null
  lead_researcher_ids: []
  current_version_id: null
  subject_class_refs: []
  site_refs: []
  method_refs: []
  intervention_class: observational
  planned_procedure_ids: []
  data_category_refs: []
  sample_category_refs: []
  participant_permission_model_ref: null
  pokemon_subject_protection_ref: null
  site_authorization_refs: []
  welfare_stop_condition_ids: []
  privacy_plan_ref: null
  sample_disposition_plan_ref: null
  publication_restriction_refs: []
  review_refs: []
  current_status: DRAFT
  canon_status: proposed
```

Suggested intervention classes are descriptive only:

- OBSERVATIONAL
- REMOTE_OBSERVATION
- INTERVIEW_OR_SELF_REPORT
- NONCONTACT_MEASUREMENT
- PASSIVE_SAMPLE_COLLECTION
- DIRECT_HANDLING
- INVASIVE_SAMPLE_COLLECTION
- ENVIRONMENTAL_MANIPULATION
- BEHAVIORAL_INTERVENTION
- CLINICAL_OR_CARE_LINKED
- PSYCHIC_OR_PRIVATE_INFORMATION
- EXPERIMENTAL_DEVICE
- PERMANENT_MODIFICATION
- OTHER_AUTHORED

These labels do not create mechanical effects or automatic review outcomes.

## 3. Versioned protocol

A protocol is not timeless.

```yaml
protocol_version:
  protocol_version_id: null
  protocol_id: null
  version_number: 1
  effective_from: null
  effective_until: null
  method_refs: []
  procedure_ids: []
  subject_classes: []
  site_scope_refs: []
  sample_scope_refs: []
  data_scope_refs: []
  stop_condition_ids: []
  approved_authorization_ids: []
  supersedes_version_id: null
  amendment_reason_refs: []
```

Old versions remain historical state.

A corrected protocol does not rewrite what researchers were authorized to do last year.

## 4. Procedure

```yaml
research_procedure:
  procedure_id: null
  protocol_version_id: null
  procedure_type: null
  target_subject_class: null
  equipment_refs: []
  mechanical_action_refs: []
  handling_required: false
  sample_created: false
  destructive: false
  expected_duration_band: null
  expected_disturbance_band: null
  privacy_categories_accessed: []
  prerequisites: []
  exclusion_conditions: []
  stop_condition_ids: []
  post_procedure_requirements: []
```

A mechanical action ref is a pointer to PTU/Caelo/AutoPTU behavior when required. The narrative layer cannot define that behavior itself.

## 5. Protocol authorization

Institutional permission must be bounded by authored mandate.

```yaml
protocol_authorization:
  authorization_id: null
  protocol_version_id: null
  authorizing_institution_id: null
  reviewing_body_id: null
  mandate_ref: null
  authorized_site_refs: []
  authorized_procedure_ids: []
  authorized_subject_classes: []
  valid_from: null
  valid_until: null
  conditions: []
  excluded_actions: []
  reporting_requirements: []
  status: PENDING
  decision_ref: null
```

Suggested states:

- PENDING
- MORE_INFORMATION_NEEDED
- AUTHORIZED
- AUTHORIZED_WITH_CONDITIONS
- NOT_AUTHORIZED
- SUSPENDED
- EXPIRED
- WITHDRAWN
- SUPERSEDED

A research institution does not receive this authority merely because it employs scientists.

If Ouros canon never establishes a formal review body for a type of project, the system can still require local site permission, participant permission and method constraints without inventing a bureaucracy.

## 6. Site authorization

Land Access, Conservation, Archives, Clinics, Workplaces or other domain layers own access to their spaces/resources.

This layer stores the research-specific handoff.

```yaml
research_site_authorization:
  site_authorization_id: null
  protocol_version_id: null
  site_id: null
  granting_authority_ref: null
  allowed_activity_refs: []
  prohibited_activity_refs: []
  access_windows: []
  supervision_requirements: []
  sensitive_zone_refs: []
  valid_from: null
  valid_until: null
  status: ACTIVE
```

Examples:

A reserve may allow camera observation but not baiting.

A museum may allow non-destructive imaging but not sampling.

A clinic may allow aggregate records analysis but not identifiable case access.

A cave permit may cover one mapped chamber and not a newly discovered extension.

## 7. Human participant permission

For PCs, participation in private or intrusive research must be an explicit player action.

```yaml
participant_permission:
  permission_id: null
  participant_actor_id: null
  protocol_version_id: null
  permitted_procedure_ids: []
  permitted_data_categories: []
  permitted_sample_categories: []
  secondary_use_scope: []
  publication_scope: []
  identity_visibility: private
  valid_from: null
  valid_until: null
  withdrawal_terms_ref: null
  given_via_event_id: null
  status: ACTIVE
```

Possible states:

- REQUESTED
- ACTIVE
- DECLINED
- PARTIAL
- PAUSED
- WITHDRAWN
- EXPIRED
- SUPERSEDED

The system must never infer PC consent from:

- being in the same party;
- accepting a quest;
- visiting a facility;
- having a relationship with a researcher;
- prior participation in another study;
- being photographed publicly;
- having public battle statistics;
- receiving treatment;
- being employed by an institution.

## 8. Pokémon subject boundary

Ouros should not implement one universal “Pokémon consent check.”

Pokémon species, individuals and communication capabilities differ too much, and PTU already has mechanical systems around Command, Loyalty and capabilities that this layer must not overwrite.

Instead, preserve the smallest defensible facts.

```yaml
pokemon_research_subject_record:
  subject_record_id: null
  pokemon_id: null
  protocol_version_id: null
  current_custodian_ref: null
  active_trainer_ref: null
  ownership_claim_refs: []
  communication_capability_refs: []
  explicit_permission_event_refs: []
  observed_assent_refs: []
  observed_refusal_refs: []
  handling_history_refs: []
  stop_condition_ids: []
  welfare_review_refs: []
  current_research_state: ELIGIBLE_FOR_OBSERVATION
```

Suggested research states:

- ELIGIBLE_FOR_OBSERVATION
- OBSERVATION_ONLY
- PROCEDURE_AUTHORIZED
- PROCEDURE_PAUSED
- WITHDRAWN_FROM_PROCEDURE
- CARE_PRIORITY
- INELIGIBLE_CURRENTLY
- UNKNOWN

These are research-management states, not emotional or PTU mechanical states.

## 9. Assent/refusal observation

```yaml
pokemon_assent_observation:
  observation_id: null
  pokemon_id: null
  procedure_id: null
  actor_ids: []
  observed_at: null
  observed_behavior: approached|remained|cooperated|hesitated|avoided|withdrew|refused|unknown
  mechanical_resolution_ref: null
  context_refs: []
  interpretation_claim_ids: []
```

One approach event does not authorize every future procedure.

One refusal does not create a permanent hostile tag.

If PTU/Caelo mechanically resolves obedience or a related action, keep that result separate from the research interpretation.

## 10. Wild subjects

Wild Pokémon are not unowned research inventory.

Observation may be possible under site rules.

Handling, capture, tagging, relocation, sampling or temporary containment require their own valid authority/mechanics where applicable.

A successful mechanical capture does not retroactively validate a research protocol.

A wild Pokémon can be treated by Care and later released without becoming a research asset.

## 11. Eggs, nests and juveniles

Breeding/Nursery and Conservation remain authoritative for Egg and nesting state.

Research may consume those facts.

```yaml
sensitive_life_stage_condition:
  condition_id: null
  subject_or_site_ref: null
  life_stage_ref: null
  activates_restriction_ids: []
  activates_stop_condition_ids: []
  source_observation_ids: []
  effective_from: null
  effective_until: null
```

Examples:

- an unexpected Egg appears in a study area;
- a nest becomes active earlier than predicted;
- a juvenile begins using equipment as shelter;
- an individual evolves and a planned procedure no longer fits its physical form or current rules state.

The appropriate outcome can be protocol amendment or stopping work. It does not need to become an encounter.

## 12. Welfare stop conditions

A protocol should know in advance what makes the current procedure stop.

```yaml
welfare_stop_condition:
  stop_condition_id: null
  protocol_version_id: null
  subject_class_ref: null
  trigger_type: observed_behavior|health_state|environment|equipment|site_state|mechanical_state|permission|other
  trigger_refs: []
  required_action: pause
  escalation_refs: []
  resumption_requirements: []
```

Examples:

- participant withdraws permission;
- Pokémon repeatedly withdraws from a handling setup;
- Care marks treatment as higher priority than research;
- severe weather changes the site;
- an instrument fails calibration;
- a new nest is discovered;
- a mechanical PTU state makes the planned procedure invalid;
- an unexpected crowd forms around a sensitive site.

Stop conditions are not failure states. They are part of a valid protocol.

## 13. Research stop event

```yaml
research_stop_event:
  stop_event_id: null
  protocol_version_id: null
  procedure_id: null
  subject_refs: []
  site_ref: null
  triggered_condition_ids: []
  observed_at: null
  stopped_by_actor_ids: []
  immediate_actions: []
  care_handoff_refs: []
  incident_refs: []
  resumption_status: NOT_REVIEWED
```

Suggested resumption states:

- NOT_REVIEWED
- MAY_RESUME_SAME_PROTOCOL
- AMENDMENT_REQUIRED
- NEW_PERMISSION_REQUIRED
- NEW_SITE_AUTHORIZATION_REQUIRED
- CARE_CLEARANCE_REQUIRED
- PERMANENTLY_STOPPED

## 14. Protocol amendment

```yaml
protocol_amendment:
  amendment_id: null
  protocol_id: null
  from_version_id: null
  proposed_version_id: null
  reason_refs: []
  changed_procedure_ids: []
  changed_site_refs: []
  changed_data_scope: []
  changed_sample_scope: []
  participant_repermission_required: false
  pokemon_subject_review_required: false
  site_reauthorization_required: false
  review_refs: []
  status: PROPOSED
```

A new version can invalidate old permissions for only the newly changed procedures while leaving completed legitimate work intact.

## 15. Protocol deviation

A deviation is an observed mismatch between the authorized plan and what actually happened.

```yaml
protocol_deviation:
  deviation_id: null
  protocol_version_id: null
  procedure_id: null
  occurred_at: null
  observed_difference: null
  reason_claim_ids: []
  subject_refs: []
  site_refs: []
  immediate_consequence_refs: []
  adverse_event_refs: []
  review_required: true
  current_status: RECORDED
```

Do not infer misconduct.

Possible benign or mixed explanations include:

- flooding forced a sensor relocation;
- a participant left early;
- a wild Pokémon interacted with equipment unexpectedly;
- the intended route closed;
- a sample container broke;
- a site changed between planning and arrival.

Concealment, falsification or intentional scope violations require separate evidence.

## 16. Adverse research event

```yaml
adverse_research_event:
  event_id: null
  protocol_version_id: null
  procedure_id: null
  subject_refs: []
  site_refs: []
  event_type: null
  observed_effects: []
  mechanical_state_refs: []
  care_case_refs: []
  emergency_action_refs: []
  causation_claim_ids: []
  review_refs: []
  status: OPEN
```

An adverse event is not automatically caused by misconduct or even by the research procedure. Causation remains a claim requiring evidence.

## 17. Data-use permission

Collection and later use are separate.

```yaml
data_use_permission:
  data_use_permission_id: null
  data_or_dataset_refs: []
  source_permission_ids: []
  permitted_analysis_types: []
  permitted_recipient_ids: []
  permitted_publication_scope: []
  deidentification_requirement: null
  geographic_redaction_refs: []
  expires_at: null
  status: ACTIVE
```

Examples:

A participant can permit aggregate use but not publication of their name.

A rare-species survey can permit regional statistics while withholding exact nest coordinates.

A clinic can contribute deidentified aggregate signals without exposing medical case records.

## 18. Sample-use permission

Material Culture/Case Custody/Science retain the physical sample and custody history.

This layer stores what analyses are allowed.

```yaml
sample_use_permission:
  permission_id: null
  sample_id: null
  authorized_analysis_refs: []
  destructive_analysis_allowed: false
  maximum_consumption_scope: null
  transfer_conditions: []
  return_or_disposition_ref: null
  expires_at: null
  current_status: ACTIVE
```

A researcher possessing a sample does not automatically have permission to consume it.

A fossil, Egg-shell fragment, tissue sample or historic material can be physically accessible while destructive analysis remains prohibited.

## 19. Secondary-use request

```yaml
secondary_use_request:
  request_id: null
  requester_ids: []
  data_or_sample_refs: []
  original_protocol_refs: []
  proposed_question_ids: []
  proposed_method_refs: []
  requested_scope: []
  new_permission_required: null
  review_refs: []
  status: PENDING
```

This supports old datasets becoming useful years later without pretending the original permission covered every future question.

## 20. Psychic, dream and Aura studies

Psychic Information remains authoritative for mental/private information.

Research must not use a scientific context to bypass that layer.

Hard rules:

- a PC's thoughts, dreams, trauma, memories, attractions, fears or private motives are never procedurally generated as study data;
- participation in a dream study does not expose unrelated dreams;
- telepathy capability does not create blanket permission to inspect mental content;
- a participant-submitted dream report is data because the participant supplied it, not because the system inferred a hidden truth;
- shared-dream research must keep each participant's private view separate unless explicitly shared.

## 21. Clinical and rehabilitation research

Care remains primary whenever a Pokémon or person needs treatment.

A research objective cannot delay urgent care merely because completing the protocol would produce better data.

```yaml
care_priority_handoff:
  handoff_id: null
  research_subject_ref: null
  research_protocol_ref: null
  care_case_ref: null
  triggered_at: null
  research_state: PAUSED
  resumption_requirements: []
```

Mechanical healing, Injuries, Status removal and treatment remain PTU/Caelo/AutoPTU responsibilities.

## 22. Sensitive sites and publication

```yaml
sensitive_site_restriction:
  restriction_id: null
  site_ref: null
  reason_refs: []
  applies_to_protocol_ids: []
  prohibited_public_fields: []
  coordinate_precision_limit: null
  allowed_recipient_ids: []
  review_at: null
  authority_ref: null
  status: ACTIVE
```

Candidate reasons can include:

- active nesting;
- vulnerable habitat;
- archaeological context;
- sacred/restricted cultural knowledge;
- private residence/base;
- ongoing enforcement/case work;
- biosecurity concern;
- temporary rehabilitation site.

The reason must come from another authoritative layer. This layer does not invent restrictions by itself.

## 23. Field-impact ledger

Do not simulate every footprint.

Use coarse, meaningful state for repeated research impact.

```yaml
field_impact_ledger:
  ledger_id: null
  protocol_id: null
  site_id: null
  visit_event_ids: []
  handling_event_ids: []
  collection_event_ids: []
  equipment_deployment_ids: []
  bait_or_attractant_refs: []
  light_or_sound_disturbance_refs: []
  habitat_disturbance_refs: []
  cleanup_or_restoration_refs: []
  current_impact_assessment_ref: null
```

No universal numeric disturbance score is required.

Repeated low-impact visits may still become relevant when world state shows a real effect.

## 24. Lower-impact alternative methods

A project should be able to change methods without treating the safer option as lesser content.

Possible method classes include:

- archival research;
- existing dataset analysis;
- remote photography;
- acoustic recording;
- environmental samples;
- non-contact visual measurement;
- opportunistic observations;
- voluntary self-report;
- observation from existing public infrastructure.

Whether a specific method is scientifically valid belongs to Science.

Whether the method is mechanically possible belongs to the relevant world/PTU subsystem.

## 25. Experimental devices and permanent modification

Artificial creation, permanent biological alteration, control devices, forced behavioral manipulation and similar high-impact research must never be generated as routine procedural activities.

If canon authors such a project, record at least:

- subject identity;
- intervention provenance;
- responsible institution/actors;
- intended purpose;
- known physical modifications;
- control/restraint history;
- observed adverse effects;
- current subject agency/custody;
- access restrictions on the procedure;
- institutional review/history.

Do not create rules for cloning, gene editing, personality modification, obedience control or augmentation without authoritative project mechanics.

## 26. Research sponsor pressure

Finance can fund research. Funding never controls research truth.

Sponsor expectations may create:

- deadline pressure;
- requests for more sites;
- requests for a public demonstration;
- concern about a null result;
- requests for a protocol amendment;
- threatened non-renewal.

The research team may comply, negotiate, decline, pause or seek alternative funding according to authored agreements and player choices.

A sponsor cannot retroactively authorize an unapproved procedure.

## 27. Data breach and premature publication

Digital Systems/Media own transmission and publication state.

This layer can create a subject-protection incident when restricted research information is disclosed outside its permitted scope.

Do not infer hacking, malice or a perpetrator from the breach alone.

Possible causes include:

- wrong recipient;
- stale access grant;
- publication redaction error;
- lost physical notebook;
- duplicated dataset with old permissions;
- compromised account;
- deliberate leak when evidence supports it.

## 28. Multiplayer privacy

Private research information must not become party-global by default.

Possible visibility levels:

- SUBJECT_ONLY
- RESEARCH_TEAM
- CARE_TEAM
- AUTHORIZED_REVIEWERS
- INSTITUTION_INTERNAL
- DEIDENTIFIED_RESEARCH
- PUBLIC_SUMMARY
- PUBLIC

A party member can help with logistics without receiving another player's private research data.

## 29. Chronicle and withdrawal

The Chronicle may preserve that:

- participation was requested;
- permission existed for a defined period;
- a participant withdrew;
- a protocol was paused;
- an amendment occurred;
- a sample was destroyed or returned;
- a publication was corrected or restricted.

It must not expose restricted research content merely because the event itself is historical.

History of permission and permission to use the underlying data are separate.

## 30. Institutional Review integration

Institutional Review owns formal review proceedings when an authored body has the mandate.

This layer supplies:

- protocol/version;
- permissions;
- deviations;
- adverse events;
- stop events;
- site authorizations;
- sample/data-use state.

Institutional Review supplies:

- mandate checks;
- evidence considered;
- reviewers;
- findings;
- decisions;
- remedies;
- appeal/review history.

An ethics review does not become a criminal proceeding unless Ouros separately authors such a system.

## 31. Researcher role and PTU mechanics

`researcher`, `field lead`, `ethics reviewer`, `technician`, `participant liaison` and similar labels are world roles.

They do not grant:

- Education Skill ranks;
- Researcher Trainer Class;
- Features;
- Items;
- Command authority;
- access to psychic information;
- handling bonuses;
- sample collection bonuses;
- capture bonuses;
- medical abilities.

Mechanical capability must come from the authoritative character state.

## 32. Encounter contract — Nest Survey Withdrawal

Narrative premise:

A field survey operating under an observation protocol discovers that a nesting site became active earlier than expected. A separate disturbance or threat makes the team withdraw while protecting the site from further intrusion.

FULL version:

- researchers and any noncombatants occupy explicit protected routes;
- wild Pokémon can withdraw toward/away from the nesting site according to tactical policy;
- the objective can include WITHDRAW, PROTECT_AREA and DO_NOT_ENTER;
- environmental terrain/weather effects exist only when authoritative mechanics define them;
- the nest/Eggs remain world entities, not generic battle targets.

Capability dependencies:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for full dynamic withdrawal/interception;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if the site uses active tactical environment;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:

The server resolves the protocol stop, moves researchers/visitors out of the sensitive zone and keeps Eggs/nest outside the battle grid. If an unrelated confrontation remains, AutoPTU receives a static legal arena with only real combatants. After combat, the research protocol remains paused and world state records the early nesting observation.

Narrative premise preserved: the important decision is respecting the stop condition, not winning a nest-defense battle.

## 33. Encounter contract — Research Annex Emergency Shutdown

Narrative premise:

An experimental instrument produces an unexpected Pokémon response or facility incident. The procedure stops. Staff must secure the site and determine what happened.

FULL version:

- shutdown controls can be tactical interactables only after an authoritative objective/interactable contract exists;
- any zones, Status applications, forced movement or device-generated effects require exact validated mechanics;
- staff movement/evacuation requires objective-aware AI and complete movement support;
- post-battle causal conclusions remain outside AutoPTU.

Capability dependencies:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for evacuation/interactive movement;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING for any live instrument hazard/zone;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:

The device enters `SAFE_SHUTDOWN` in overworld state before any battle begins. Staff leave the room. AutoPTU receives a static arena if a real combat threat remains. The post-event investigation separately records equipment logs, Pokémon behavior, deviations and care state. No invented device damage, Status or field effect is used.

## 34. Encounter contract — Consent Withdrawal During Handling

Narrative premise:

A planned handling procedure no longer has valid participation/assent conditions. Research stops.

Default implementation:

This is deliberately a non-combat encounter.

The player may:

- stop the procedure immediately;
- call a caretaker/research lead;
- switch to observation-only;
- document the stop condition;
- propose a protocol amendment;
- end the session.

No Skill check can force continued participation.

No battle is generated solely because a Pokémon withdraws or a PC declines.

If a separate threat occurs afterward, that threat receives its own encounter contract and does not retroactively validate the interrupted procedure.

## 35. AutoPTU authority boundary

AutoPTU owns battle mechanics.

This layer may consume battle outputs such as:

- authoritative transcript;
- mechanical HP/Injury/Status state;
- action history;
- legal combat outcomes.

It must not infer:

- consent from a successful command;
- harm solely from a Status label;
- ethical acceptability from move legality;
- research validity from victory;
- permission from Trainer ownership/custody;
- research purpose from a battle transcript.

## 36. Current engine capability map used by this layer

Current evidence remains conservative.

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

The latest Java evidence adds generic Trainer Feature `apply_status` and `remove_status` handlers backed by parity cases, including refresh/stack/remove behavior. This strengthens status mutation and Trainer Feature infrastructure. It does not demonstrate the complete status controller or complete Feature catalog.

## 37. New overworld blockers

Research ethics depends on world systems outside AutoPTU:

- `RESEARCH_PROTOCOL_STATE`
- `PROTOCOL_VERSION_HISTORY`
- `PROTOCOL_AUTHORIZATION_STATE`
- `PARTICIPANT_PERMISSION_STATE`
- `POKEMON_SUBJECT_PROTECTION_STATE`
- `RESEARCH_STOP_CONDITION_STATE`
- `PROTOCOL_AMENDMENT_HISTORY`
- `PROTOCOL_DEVIATION_HISTORY`
- `ADVERSE_RESEARCH_EVENT_STATE`
- `DATA_USE_PERMISSION_STATE`
- `SAMPLE_USE_PERMISSION_STATE`
- `SENSITIVE_SITE_RESTRICTION_STATE`
- `FIELD_IMPACT_LEDGER`
- `RESEARCH_ETHICS_TO_CARE_HANDOFF`
- `RESEARCH_ETHICS_TO_CONSERVATION_HANDOFF`
- `RESEARCH_ETHICS_TO_PSYCHIC_PRIVACY_HANDOFF`
- `RESEARCH_ETHICS_TO_INSTITUTIONAL_REVIEW_HANDOFF`
- `RESEARCH_ETHICS_TO_MINECRAFT_PRESENTATION`

None belong inside the battle core.

## 38. Minecraft presentation

Minecraft can present:

- research stations;
- field equipment;
- marked observation boundaries;
- protocol status boards;
- consent/participation UI visible only to the relevant player;
- sample containers;
- care handoff areas;
- restricted-coordinate redaction;
- stopped/paused equipment;
- staff leaving a site;
- non-interactive nest protection boundaries.

Minecraft must not decide:

- whether consent exists;
- whether a Pokémon consents;
- whether a procedure is ethically acceptable;
- whether a site permit is valid;
- whether a protocol violation occurred;
- whether a sample can be destroyed;
- whether private data can be viewed;
- whether a procedure applies a PTU Status.

## 39. Generation rules

A generated research objective must be traceable to current world state such as:

- an open research question;
- a protocol needing amendment;
- a new sensitive life-stage observation;
- a pending secondary-use request;
- an instrument problem;
- a participant withdrawal;
- a site authorization conflict;
- a sample-use limitation;
- a field-impact concern;
- an adverse event requiring review;
- a lower-impact alternative becoming available;
- a sponsor request conflicting with current scope.

Do not generate procedural paperwork merely to slow the player.

If every permission is valid and no meaningful choice exists, compress the administration.

## 40. Explicit prohibitions

Do not procedurally generate:

- forced participation of PCs in research;
- mind-reading as a research convenience;
- permanent Pokémon modification;
- cloning;
- genetic engineering;
- obedience implants or control devices;
- research-induced Status effects without validated mechanics;
- sample collection damage;
- sedative/anesthetic rules;
- vivisection;
- destructive analysis of protected/unique material without authored authorization;
- Egg collection because a nest is accessible;
- capture because a specimen is rare;
- Loyalty changes from study participation;
- Researcher Feature effects;
- universal ethics law;
- universal researcher credentials;
- universal Pokémon ownership rights;
- legal punishment for protocol deviations;
- hidden private beliefs for PCs.

## Open canon questions

Ouros still needs authored decisions on:

- which institutions can authorize which research procedures;
- whether regional research ethics bodies exist at all;
- how formal field-research permissions are in each region;
- how Pokémon capable of explicit language/telepathy express participation choices;
- which decisions a Trainer/custodian can make for a Pokémon and which require separate evidence;
- how clinics handle research use of treatment data;
- how long permissions and samples persist;
- what secondary-use rules exist;
- whether some methods are prohibited outright;
- how modified/artificial Pokémon are treated institutionally;
- which sites require restricted publication;
- what parts of research history are publicly discoverable.

The primary Caelo corpus and Super PTU Online Helper were not available as reliable invocable sources during this pass. No rules are attributed to them.