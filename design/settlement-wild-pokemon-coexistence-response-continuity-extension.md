# Ouros Settlement / Wild Pokémon Coexistence Response Continuity Extension

Status: PROPOSED systems design. Not established Ouros canon.

## Purpose

Ouros already knows how to persist wild Pokémon and collectives, ecological relations, conservation policy, wildlife observations, facility state, public complaints, health cases, care, crisis response and Pokémon identity.

This extension preserves what happens when wild Pokémon and settlement activity repeatedly overlap and someone wants the situation investigated or changed.

Its core sequence is:

report -> verify observation -> resolve subject scope -> verify impact -> compare explanations -> hand causes/conditions to the correct owner -> record mitigation -> observe outcome -> revise, close or reopen.

The extension exists so the world does not reduce every urban or rural wildlife interaction to one of two bad shortcuts:

- "wild Pokémon present, therefore combat/capture";
- "problem solved once the encounter ends."

## Authority boundary

This extension owns:

- coexistence-case identity and chronology;
- bounded interaction reports;
- observation verification links;
- subject-identity confidence for the case;
- impact claims and verification state;
- competing causal explanations;
- stakeholder positions and tradeoffs;
- mitigation proposals and implementation references;
- outcome observations;
- recurrence/reopening history;
- owner-system handoffs;
- public-summary references;
- case legacy.

It does not own:

- species ecology, ecological relations or population pressure — Ecology;
- protected-area policy, habitat management or stewardship authority — Conservation;
- research methods and scientific conclusions — Science;
- individual Pokémon identity, custody, capture/partnership/release state — Pokémon Agency;
- tracking/tagging/re-identification programs — Wildlife Monitoring;
- placement, sanctuary or shelter admission — Pokémon Shelter/Sanctuary;
- building faults, openings, repairs or maintenance — Facility Maintenance;
- waste storage, sanitation, water, food, farms, parks, workplaces, roads or other service truth — their owner systems;
- medical diagnosis/treatment — Care;
- community-level health investigation — Community Health;
- immediate rescue/evacuation — Crisis/Rescue;
- allegations, culpability or evidence custody — Case/Authority;
- capture legality, restraint law, relocation authority, wildlife-control powers or enforcement — undecided unless canon establishes them;
- PTU battle legality or effects — PTU/Caelo + AutoPTU.

## Core invariants

`POKEMON_PRESENT != PROBLEM_CONFIRMED`

`REPORT_RECEIVED != REPORT_VERIFIED`

`NUISANCE_DESCRIPTION != MECHANICAL_STATUS`

`SPECIES_IDENTIFIED != INDIVIDUAL_IDENTIFIED`

`REPEAT_REPORT != SAME_INDIVIDUAL`

`CO_OCCURRENCE != CAUSE`

`DAMAGE_OBSERVED != POKEMON_CAUSED_DAMAGE`

`FEAR_REPORTED != AGGRESSION_CONFIRMED`

`CONFLICT_REPORTED != ECOLOGICAL_DYSFUNCTION`

`MITIGATION_PROPOSED != MITIGATION_AUTHORIZED`

`MITIGATION_IMPLEMENTED != MITIGATION_EFFECTIVE`

`SUBJECT_ABSENT_AFTER_ACTION != ACTION_CAUSED_ABSENCE`

`REMOVAL_FROM_SITE != PLACEMENT_COMPLETE`

`RELOCATION_COMPLETED != CASE_RESOLVED`

`NO_NEW_REPORTS != NO_CONTINUING_INTERACTION`

`CASE_CLOSED != CAUSE_KNOWN`

These distinctions are mandatory.

## 1. Coexistence case

```yaml
settlement_wild_pokemon_coexistence_case:
  case_id: null
  status: PROPOSED
  opened_at: null
  opened_by_ref: null
  location_scope_refs: []
  activity_scope_refs: []
  report_ids: []
  verified_observation_refs: []
  subject_scope_revision_ids: []
  impact_claim_ids: []
  cause_hypothesis_ids: []
  stakeholder_position_ids: []
  mitigation_action_ids: []
  owner_handoff_ids: []
  outcome_observation_ids: []
  public_summary_ref: null
  current_state: INTAKE
  closure_ref: null
  recurrence_refs: []
  canon_status: proposed
```

Suggested states:

- INTAKE
- VERIFYING
- MONITORING
- IMPACT_REVIEW
- RESPONSE_PLANNING
- RESPONSE_ACTIVE
- FOLLOW_UP
- DORMANT_MONITORING
- CLOSED
- REOPENED

The case may close because:

- the claimed impact was unsupported;
- the subject was identified and no action was needed;
- an owner-system change reduced the interaction;
- a coexistence arrangement became stable;
- an authorized relocation/placement workflow completed and follow-up was satisfactory;
- the case was transferred elsewhere;
- evidence remained insufficient after a bounded review period;
- the interaction ended for reasons that remain uncertain.

## 2. Interaction reports preserve what someone actually said or observed

```yaml
coexistence_interaction_report:
  report_id: null
  case_id: null
  reporter_ref: null
  received_at: null
  reported_time_window_ref: null
  reported_location_ref: null
  reported_subject_description: null
  reported_behavior_tags: []
  reported_impact_tags: []
  supporting_media_refs: []
  direct_observation: unknown
  identity_claim_refs: []
  cause_claim_refs: []
  urgency_claim: null
  privacy_ref: null
  verification_state: UNREVIEWED
```

Do not normalize a witness statement into a stronger fact than the witness supplied.

Examples:

- "large dark Pokémon on the roof" remains a description until identification evidence exists;
- "same Pokémon again" is an identity claim;
- "it broke the bins" is a causal claim;
- "it is dangerous" is an impact/risk claim;
- "it comes every Tuesday" is a recurrence claim that requires chronology support.

Reports can be sincere, incomplete, mistaken or precise.

## 3. Subject scope is versioned

A case needs a subject scope that can become narrower or split over time.

```yaml
coexistence_subject_scope_revision:
  revision_id: null
  case_id: null
  parent_revision_id: null
  effective_at: null
  scope_type: UNKNOWN | SPECIES_CANDIDATE | SPECIES_SUPPORTED | INDIVIDUAL_CANDIDATE | INDIVIDUAL_SUPPORTED | COLLECTIVE_CANDIDATE | COLLECTIVE_SUPPORTED | MULTIPLE_SUBJECTS | DISPUTED
  pokemon_entity_refs: []
  monitoring_subject_refs: []
  collective_refs: []
  species_claim_refs: []
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  confidence_band: unknown
  limitations: []
```

A case may begin as one supposed recurring Pokémon and later split into three individuals using the same alley.

Earlier reports are not rewritten.

## 4. Impact claims

Presence and impact are separate.

```yaml
coexistence_impact_claim:
  impact_claim_id: null
  case_id: null
  impact_type: null
  affected_actor_or_system_refs: []
  location_scope_refs: []
  time_scope_ref: null
  observed_effect_refs: []
  claimed_severity: null
  verification_state: UNVERIFIED
  verified_effect_refs: []
  contradicting_evidence_refs: []
  owner_system_ref: null
  downstream_case_refs: []
```

Candidate descriptive impact types:

- ACCESS_INTERRUPTION
- MATERIAL_DAMAGE_CLAIM
- FOOD_OR_WASTE_DISTURBANCE
- NESTING_OR_ROOST_CONFLICT
- NOISE_OR_ODOR_COMPLAINT
- FEAR_OR_AVOIDANCE_REPORT
- SERVICE_DISRUPTION
- LIVESTOCK_OR_CROP_INTERACTION
- TRAFFIC_OR_ROUTE_INTERACTION
- PUBLIC_SPACE_CONFLICT
- WORKSITE_INTERACTION
- HEALTH_CONCERN_REFERRED
- POKEMON_WELFARE_CONCERN
- ECOLOGICAL_CONCERN_REFERRED
- UNKNOWN_OR_MIXED

These tags do not establish mechanical effects or blame.

## 5. Competing cause hypotheses

```yaml
coexistence_cause_hypothesis:
  hypothesis_id: null
  case_id: null
  statement: null
  candidate_mechanism_tags: []
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  related_owner_system_refs: []
  confidence_band: unknown
  current_state: ACTIVE | WEAKENED | SUPPORTED | REJECTED | UNRESOLVED
```

Useful hypothesis families include:

- food/access attractant;
- shelter/nesting opportunity;
- water access;
- seasonal movement;
- human disturbance/displacement;
- infrastructure opening or fault;
- waste-management condition;
- routine feeding by residents;
- route/corridor obstruction elsewhere;
- multiple unrelated subjects;
- mistaken identity;
- human-caused relocation/release;
- unknown.

A hypothesis never becomes ecological truth by repetition alone.

## 6. Stakeholder positions

Human-wild Pokémon conflict often includes disagreement between people about the desired outcome.

```yaml
coexistence_stakeholder_position:
  position_id: null
  case_id: null
  stakeholder_ref: null
  position_summary: null
  requested_outcomes: []
  unacceptable_outcomes: []
  supporting_evidence_refs: []
  interest_or_dependency_refs: []
  change_history: []
  visibility: PUBLIC | LIMITED | PRIVATE
```

Possible positions:

- leave the Pokémon alone;
- change waste/storage practice;
- restrict one area temporarily;
- preserve nesting access;
- require safe access for workers/residents;
- monitor before acting;
- request relocation review;
- oppose relocation;
- request Care/Conservation/Case review;
- accept a time-sharing arrangement;
- ask for a facility repair.

The system must not generate consensus simply because the quest needs closure.

## 7. Owner-system handoffs

The coexistence layer records the bridge, not the foreign work.

```yaml
coexistence_owner_handoff:
  handoff_id: null
  case_id: null
  target_system_ref: null
  target_record_ref: null
  question_or_action_requested: null
  evidence_refs: []
  requested_at: null
  response_ref: null
  status: REQUESTED | ACCEPTED | DECLINED | COMPLETED | SUPERSEDED
```

Examples:

- Waste: repeated container access may be linked to lid or collection-time changes.
- Maintenance: roof opening, broken screen, damaged gate or crawlspace access.
- Conservation: nesting buffer, corridor, stewardship or relocation review.
- Care: injured person or Pokémon.
- Community Health: only if aggregate health signals justify it.
- Roads/Travel: recurring crossing conflict.
- Housing: resident access/use consequences.
- Public Space: park operation changes.
- Agriculture/Ranch: crop/livestock interaction.
- Case/Authority: suspected deliberate release, cruelty, sabotage or another actual matter.

The coexistence record cannot mark the handoff complete merely because it created a request.

## 8. Mitigation action

```yaml
coexistence_mitigation_action:
  action_id: null
  case_id: null
  action_class: null
  proposed_by_refs: []
  authorized_by_ref: null
  authority_source_ref: null
  intended_mechanism: null
  implementation_owner_ref: null
  implementation_record_ref: null
  target_location_refs: []
  target_time_window_ref: null
  target_subject_scope_ref: null
  expected_indicators: []
  risk_or_tradeoff_refs: []
  started_at: null
  ended_at: null
  implementation_state: PROPOSED
  evaluation_ref: null
```

Candidate action classes are descriptive workflow categories only:

- OBSERVE_ONLY
- CHANGE_ACTIVITY_TIME
- CHANGE_HUMAN_ROUTE
- MODIFY_WASTE_OR_FOOD_ACCESS
- FACILITY_EXCLUSION_REPAIR
- TEMPORARY_BUFFER
- SIGNAGE_OR_INFORMATION
- STEWARDSHIP_CHANGE
- HABITAT_OR_CORRIDOR_HANDOFF
- SUPERVISED_ACCESS
- TEMPORARY_SERVICE_CHANGE
- RELOCATION_REVIEW
- OTHER_AUTHORED_ACTION

No class grants authority or mechanics.

## 9. Avoid generic deterrent mechanics

Do not create a generic `deterrent_strength` or `repel_species` stat.

A proposed deterrent must identify:

- exact physical or operational method;
- owner of the method;
- evidence that the method is available in canon;
- target scope;
- welfare/safety constraints when relevant;
- expected observable mechanism;
- follow-up evidence.

Moves, Abilities, Items, sound, light, smell, Type matchups or Minecraft blocks cannot become universal wildlife-control tools without exact governing rules.

## 10. Authorized relocation workflow

Relocation is optional and canon-sensitive.

If no institution or rule authorizes it, Ouros may record `RELOCATION_REQUESTED` or `RELOCATION_DISCUSSION`, but must stop there.

When canon does establish authority, preserve separate milestones:

```yaml
coexistence_relocation_ref:
  relocation_ref_id: null
  case_id: null
  authority_ref: null
  subject_scope_revision_ref: null
  welfare_review_ref: null
  origin_location_ref: null
  destination_candidate_refs: []
  destination_acceptance_ref: null
  capture_or_restraint_mechanics_ref: null
  custody_transfer_ref: null
  departure_event_ref: null
  arrival_event_ref: null
  placement_or_release_ref: null
  post_release_monitoring_ref: null
  recurrence_at_origin_refs: []
  destination_effect_refs: []
  state: PROPOSED
```

`DEPARTED_ORIGIN` does not mean `ARRIVED_DESTINATION`.

`ARRIVED_DESTINATION` does not mean `PLACEMENT_ACCEPTED`.

`PLACEMENT_ACCEPTED` does not mean `NO_RETURN`.

## 11. Outcome monitoring

```yaml
coexistence_outcome_observation:
  outcome_observation_id: null
  case_id: null
  action_id: null
  observation_time_ref: null
  location_scope_ref: null
  observation_method_ref: null
  interaction_report_count_ref: null
  verified_impact_state_ref: null
  subject_detection_refs: []
  owner_system_state_refs: []
  unintended_effect_refs: []
  evidence_gap_refs: []
```

The evaluation asks what changed, not whether the quest was won.

Possible conclusions:

- impact reduced with subject still present;
- subject use changed in time or space;
- reports reduced but monitoring also declined;
- facility condition changed and interaction stopped;
- one subject left but another appeared;
- mitigation shifted impact elsewhere;
- intervention had no measurable effect;
- evidence insufficient;
- coexistence arrangement remained stable;
- case requires a different owner.

## 12. Recurrence and reopening

```yaml
coexistence_case_recurrence:
  recurrence_id: null
  prior_case_id: null
  new_report_refs: []
  similarity_claim_refs: []
  identity_link_state: UNKNOWN
  prior_action_refs: []
  changed_context_refs: []
  reopened_at: null
  decision: REOPEN_PRIOR | OPEN_LINKED_CASE | UNRELATED | MONITOR_ONLY
```

A report months later should not automatically resurrect the same Pokémon identity or causal explanation.

This allows meaningful callbacks:

- the same building, different Pokémon;
- the same Pokémon, different reason;
- the same impact after the original attractant was removed;
- a successful old intervention now failing after the neighborhood changed.

## 13. Public information and rumor

Public Notices owns publication/delivery.

The coexistence layer may provide a bounded summary containing:

- location/time scope;
- verified observations;
- current operational action;
- what remains uncertain;
- whom to contact;
- revision timestamp.

Do not publish:

- unsupported species blame;
- private resident records;
- sensitive nest/den coordinates when protection requires withholding them;
- exact location of a rare Pokémon merely because a complaint was filed;
- health conclusions from an ordinary coexistence case.

Rumor/Testimony may preserve public stories independently.

## 14. Pokémon agency guardrails

Wild Pokémon remain actors, not environmental props.

Record observable behavior:

- repeatedly opens one container;
- sleeps under one bridge;
- enters a loading bay before dawn;
- nests on one roof;
- follows a drainage channel;
- avoids a repaired gate;
- returns after relocation;
- stops appearing after a schedule change.

Do not infer internal states such as:

- "wants revenge";
- "knows it is trespassing";
- "likes causing trouble";
- "accepts relocation";
- "understands the notice";
- "belongs to the neighborhood."

Those can exist when authored and supported, but procedural continuity stores observations first.

## 15. Pokémon species guardrails

A local case does not create a regional species label.

Do not persist global tags such as:

- nuisance species;
- dangerous species;
- dirty species;
- invasive species;
- disease-carrying species;
- aggressive species;

unless an exact scientific/canon authority has established the relevant bounded claim and scope.

Prefer:

- `three Trubbish repeatedly observed at Market Lane waste point during Week 18`;
- `one Talonflame nesting pair linked to access conflict at roof stair`;
- `species identity unresolved for nocturnal drainage sightings`.

## 16. Narrative patterns enabled

### The wrong subject

Three reports look identical until camera timing shows two individuals.

### The correct subject, wrong cause

A known Pokémon repeatedly appears near damaged bins, but the bins are already being opened by a faulty latch before it arrives.

### The intervention moves the problem

A repaired opening ends one building interaction but the subject begins using an adjacent service yard.

### Stable coexistence

A market changes one storage practice and the Pokémon continues passing through without disrupting service.

### Social conflict after ecological success

A mitigation reduces crop loss but blocks a route that residents value for another reason.

### Return after relocation

A persistent individual reappears. The case asks whether the destination failed, the original attractant remains, identity was wrong, or the return is expected behavior.

## 17. Faction and NPC opportunities

This layer supports recurring roles without establishing regional institutions automatically:

- local steward who knows daily patterns but lacks decision authority;
- facility manager focused on uninterrupted service;
- researcher who refuses to overstate identity evidence;
- resident who documents every occurrence accurately but interprets motive incorrectly;
- shopkeeper who quietly feeds a recurring Pokémon;
- courier whose route creates repeated encounters;
- young trainer who views the Pokémon as a neighborhood character;
- maintenance worker who discovers the physical access mechanism;
- conservation staff member balancing welfare, habitat and public access;
- skeptical administrator who wants evidence before paying for a change.

NPC positions can change after outcomes are observed.

## 18. Longer-term arc grammar

A settlement-scale coexistence arc should usually start before the "problem."

Phase 1 — ordinary shared space
- wild Pokémon already use roofs, waterways, alleys, trees, fields or edges;
- residents have routines and opinions;
- no central quest exists.

Phase 2 — repeated impact
- one interaction becomes disruptive, visible or politically salient;
- reports do not perfectly agree;
- investigation begins.

Phase 3 — explanation competition
- multiple causes remain viable;
- player observations change confidence;
- one owner-system condition becomes important.

Phase 4 — bounded response
- one or more measures are attempted;
- some stakeholders accept them and others do not;
- the Pokémon may remain present.

Phase 5 — follow-up
- effects are observed over time;
- unintended consequences can appear;
- the case closes, changes owner or reopens.

Phase 6 — durable memory
- modified gates, bins, signs, paths, schedules, habits or reputations remain in the world;
- a later case can reference the old one without repeating it.

## 19. Encounter contract — Service Yard Withdrawal

Narrative premise:

A coexistence investigation is active around a service yard. A sudden unrelated hostile encounter begins while staff are still finishing withdrawal.

### Intended full version

Potential requirements:

- targeting/footprints/range/LoS — baseline required;
- base movement legality — required;
- complete movement including push/pull/knockback/interception/forced movement — required for active escort, Intercept or forced displacement;
- core calculations — required;
- action economy/initiative — required;
- full turn/round lifecycle — required for staged withdrawal windows;
- full stateful damage pipeline — required for governed combat effects;
- status lifecycle — required only for governed statuses;
- terrain/weather/hazards/zones/reactions — required if protected withdrawal corridors or crossing reactions are tactical;
- move-specific behavior — required for selected Moves;
- abilities — required for selected Abilities;
- items — required for selected Items;
- Trainer Features/perks — required for selected features;
- AI legal-action infrastructure — required;
- AI tactical policy — required for PROTECT/WITHDRAW behavior;
- Minecraft/Cobblemon/Craftics adapter/playback — required for semantic staff withdrawal, service-yard state and encounter playback.

### Reduced version

READY with current baseline.

Before BattleSpec creation:

- finish staff withdrawal in world state;
- secure records/equipment;
- move the wild Pokémon that is merely the subject of the coexistence case outside BattleSpec unless Ouros independently selects it as a legitimate combatant;
- use reviewed static geometry;
- pause service-yard operations.

AutoPTU then resolves a conventional battle among explicit combatants.

Victory may secure immediate access. It cannot identify the coexistence subject, prove cause, authorize removal, complete relocation or reopen the yard.

## 20. Encounter contract — Nesting Roof Access Perimeter

Narrative premise:

A roof has a recurring nesting/roost interaction. A separate hostile encounter threatens the access perimeter while the sensitive roof scope remains restricted.

### Intended full version

May require:

- complete movement — PARTIAL dependency for Intercept/forced displacement near edges;
- full lifecycle — PARTIAL if access changes by phase;
- terrain/weather/hazards/zones/reactions — BLOCKING for fall edges, changing exclusion cells or generalized crossing reactions;
- AI tactical policy — BLOCKING for PROTECT/AVOID_ZONE objectives;
- adapter/playback — BLOCKING for semantic roof restriction and withdrawal.

Any falling, unstable surface, wind, nesting reaction or environmental damage also requires exact governing rules. None are implied.

### Reduced version

READY.

The sensitive roof and nesting subject remain outside the combat arena. Use a static ground-level or interior access area already verified safe. Public access is closed before battle.

Winning secures the approach only. Conservation/Facilities decides subsequent access and the coexistence case remains open until follow-up evidence exists.

## 21. Encounter contract — Authorized Relocation Staging Diversion

Narrative premise:

Only if canon has already established a legitimate relocation workflow, a separate hostile encounter blocks the route near a staging site.

### Intended full version

Potential requirements:

- complete movement for escort/Intercept/forced displacement;
- lifecycle for timed departure;
- hazards/zones/reactions if protected carriers/enclosures are in grid;
- exact Items/Trainer Features if the relocation method depends on them;
- AI tactical policy for CLEAR_ROUTE/PROTECT/WITHDRAW;
- adapter/playback for semantic vehicle/enclosure/custody movement.

Carrying, restraint, sedation, capture authority and relocation mechanics remain UNKNOWN unless exact rules are established.

### Reduced version

READY only after the subject is safely outside BattleSpec and custody/staging is paused or completed through world state.

Resolve a static route-access battle separately.

Battle victory may clear immediate access. It does not authorize relocation, change custody, prove destination suitability or count as placement/release.

## 22. PTU / Caelo mechanical boundary

The internal source scan supports local jobs, wild encounters, social play, environmental identity and sandbox consequences. It does not establish a universal wildlife-control subsystem.

Remain UNKNOWN without exact governing evidence:

- generic calming action;
- generic capture-as-removal authority;
- restraint or carrying procedures;
- sedation/tranquilization;
- deterrent rolls;
- automatic aggression from territory/nesting;
- odor or garbage statuses;
- automatic disease/Poison from proximity;
- trap object rules;
- universal repellent effects outside their exact item rules;
- species-derived safe relocation method;
- Type-derived immunity to urban/environmental hazards;
- universal Ranger authority;
- Trainer Feature authority over wild-Pokémon placement.

When a specific rule exists, implement that exact effect and classify its dependency family separately.

## 23. Minecraft / Cobblemon boundary

Minecraft/Cobblemon may render:

- recurring wild Pokémon in alleys, roofs, drains, fields or service edges;
- damaged or repaired bins, gates, screens and openings;
- temporary barriers and signs;
- observation cameras/sensors when canon supports them;
- changed NPC schedules;
- closed or reopened spaces;
- alternate waste or food storage;
- nesting/roost visual state;
- vehicles/enclosures as presentation when an authorized workflow has already decided their state.

Minecraft does not decide:

- whether a Pokémon caused damage;
- whether it is the same individual;
- whether it is dangerous;
- whether a complaint is verified;
- whether capture or relocation is authorized;
- whether a destination is suitable;
- whether a mitigation worked;
- whether an ecological or health concern exists.

Entity proximity is an observation input at most. Despawn is not relocation. A changed spawn table is not evidence that a case succeeded. Barriers do not create PTU reaction rules. Cobblemon BattleState does not own coexistence truth, combatant selection, legality, HP/status, tactical positions or world outcomes.

## 24. Canon questions deliberately left open

- Which Ouros regions have formal wildlife/coexistence services, if any?
- Which institutions may investigate ordinary settlement interactions?
- Who can authorize exclusion, relocation, capture or placement?
- What welfare review applies to wild Pokémon intervention?
- What privacy applies to household complaints and sensitive nest locations?
- Which public spaces already have coexistence management traditions?
- Are there regional norms about feeding wild Pokémon?
- Which facilities were historically redesigned because of recurring Pokémon activity?
- Which persistent individual Pokémon are known neighborhood characters?
- What review/appeal path exists for disputed interventions?

The schema supports these answers later without selecting them now.