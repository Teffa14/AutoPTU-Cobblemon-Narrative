# Food-Service Safety Assessment, Correction & Reopening Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Pass: 131

## Purpose

This extension gives Ouros a persistent operational history for food-service venue concerns without creating a universal food code or disease subsystem.

It covers the bridge from a venue-level concern to scoped assessment, evidence collection, operational adjustments, corrections, follow-up verification and service resumption.

It does not replace the owners that already control food, health, batches, utilities, facilities, care or formal authority.

## Ownership boundary

This extension owns only the continuity of a food-service operational-safety episode after a canon owner has enough mandate to assess or act.

It may reference:

- restaurants;
- cafés;
- market food counters;
- bakeries;
- community kitchens;
- school/institution canteens;
- festival kitchens;
- temporary food stalls;
- lodging kitchens;
- League/event hospitality sites;
- Pokémon-facing food-service sites if canon establishes them.

It does not create any of those institutions by itself.

### Existing owner handoffs

Food / Agriculture / Hospitality owns:
- venue identity;
- kitchen identity;
- menu and cuisine state;
- ingredient and food provenance;
- normal service operations;
- meal/service context.

Community Health owns:
- community health signals;
- cluster candidates;
- working case definitions;
- exposure hypotheses spanning people/places/time;
- health-investigation closure.

Care owns:
- individual observations;
- diagnosis;
- treatment;
- recovery.

Batch Traceability owns:
- affected product/batch scope;
- distribution traces;
- holds/recalls/recoveries;
- batch correction/disposition.

Cold Chain owns:
- temperature-controlled custody;
- excursions;
- acceptance/rejection within its canon mandate.

Drinking Water owns:
- water service and quality evidence.

Waste/Sanitation/Pollution owns:
- waste collection;
- sanitation infrastructure;
- pollution incidents;
- cleanup/remediation.

Facility Maintenance owns:
- equipment/building faults;
- work orders;
- repair completion;
- maintenance verification.

Building Safety owns:
- occupancy/use restrictions and reentry when that mandate exists.

Case & Authority / Adjudication / Governance own:
- formal investigative/legal authority;
- contested findings;
- review/appeal;
- institutional mandates.

This extension consumes their decisions and preserves references. It does not silently duplicate them.

## Core design principle

A food-service venue can have several simultaneous states.

Examples:

- dining room accessible while kitchen service is paused;
- bakery counter serving packaged goods while one preparation room is restricted;
- event kitchen closed while seating remains open;
- one station corrected while another remains under assessment;
- normal service resumed while Community Health still investigates a cluster;
- venue fully operational while public reputation remains damaged.

Ouros must therefore store state by service scope and time rather than one venue-wide `safe` boolean.

## Canon status model

Every record in this extension must carry one of:

- `CANON_APPROVED`: an approved setting fact or an event that occurred in play;
- `PROPOSED`: candidate material not yet accepted into canon;
- `UNCERTAIN`: evidence or interpretation remains unresolved;
- `REJECTED_OR_SUPERSEDED`: retained for provenance/history but no longer current.

Research-source content never becomes `CANON_APPROVED` merely because it appears in this design.

## Primary records

### FoodServiceSafetyEpisode

Fields:

- `episode_id`
- `venue_id`
- `opened_at`
- `opened_by_owner_ref`
- `trigger_refs[]`
- `authority_or_mandate_ref`
- `initial_scope_id`
- `current_scope_id`
- `status`
- `canon_status`
- `privacy_class`
- `related_health_investigation_refs[]`
- `related_batch_case_refs[]`
- `related_maintenance_case_refs[]`
- `related_water_case_refs[]`
- `related_waste_case_refs[]`
- `related_cold_chain_refs[]`
- `closure_record_id`

Possible `status` values are architectural labels, not legal categories:

- `OPEN_INTAKE`
- `ASSESSMENT_ACTIVE`
- `CORRECTION_ACTIVE`
- `FOLLOW_UP_PENDING`
- `SCOPED_SERVICE_RESUMED`
- `MONITORING`
- `CLOSED_NO_VENUE_PROBLEM_CONFIRMED`
- `CLOSED_CORRECTION_VERIFIED`
- `CLOSED_REFERRED_TO_OTHER_OWNER`
- `CLOSED_UNRESOLVED`
- `SUPERSEDED`

A region may use different public language.

### ServiceScopeVersion

A venue episode needs explicit scope.

Fields:

- `scope_id`
- `episode_id`
- `version`
- `effective_at`
- `supersedes_scope_id`
- `spatial_areas[]`
- `service_functions[]`
- `menu_or_process_refs[]`
- `time_windows[]`
- `equipment_refs[]`
- `evidence_basis_refs[]`
- `excluded_scope_notes[]`
- `uncertainty_notes[]`

Examples of spatial areas:

- receiving area;
- dry storage;
- chilled storage;
- preparation bench;
- cooking line;
- wash station;
- serving counter;
- dining room;
- outdoor seating;
- loading yard.

The architecture does not assign safety meaning to these locations automatically.

### ConcernRecord

Fields:

- `concern_id`
- `episode_id`
- `received_at`
- `source_type`
- `source_ref`
- `reported_scope`
- `reported_condition`
- `reported_time_window`
- `supporting_refs[]`
- `privacy_class`
- `verification_status`

Possible source types:

- customer report;
- worker report;
- owner observation;
- maintenance alert;
- Community Health referral;
- Batch Traceability referral;
- water/waste/cold-chain referral;
- authored routine review;
- other canon institution.

A concern record is evidence of a report, not evidence that the reported condition is true.

### AssessmentVisit

Fields:

- `assessment_id`
- `episode_id`
- `started_at`
- `ended_at`
- `assessor_refs[]`
- `mandate_ref`
- `scope_id`
- `methods_used[]`
- `observation_ids[]`
- `record_review_refs[]`
- `interview_refs[]`
- `sample_refs[]`
- `evidence_gaps[]`
- `follow_up_required`
- `canon_status`

Methods are descriptive evidence channels only:

- direct observation;
- interview;
- record review;
- equipment-state reference;
- sample collection;
- photograph/diagram;
- timeline reconstruction;
- cross-owner record comparison.

No method implies a universal Skill DC.

### VenueObservation

Fields:

- `observation_id`
- `episode_id`
- `assessment_id`
- `observed_at`
- `observer_ref`
- `scope_id`
- `subject_ref`
- `observation_type`
- `literal_observation`
- `media_refs[]`
- `related_owner_refs[]`
- `interpretation_status`

The literal observation must be separable from later interpretation.

Example:

`literal_observation = "cooling unit display was dark at 10:42"`

A later Maintenance record may show a power fault. Cold Chain may determine whether a controlled item experienced an excursion. Food may determine which menu items depended on that storage. The observation alone cannot make those conclusions.

### SampleReference

This extension does not own laboratory truth. It only tracks the venue-context link.

Fields:

- `sample_ref_id`
- `episode_id`
- `assessment_id`
- `collection_time`
- `collection_scope`
- `sample_subject_description`
- `custody_owner_ref`
- `external_result_ref`
- `result_received_at`
- `interpretation_owner_ref`

`SAMPLE_COLLECTED` does not imply `RESULT_AVAILABLE`.

### OperationalHypothesis

Fields:

- `hypothesis_id`
- `episode_id`
- `created_at`
- `question`
- `suspected_scope_id`
- `suspected_process_or_condition`
- `supporting_evidence_refs[]`
- `contradicting_evidence_refs[]`
- `unknowns[]`
- `status`
- `supersedes_hypothesis_id`

Possible statuses:

- `OPEN`
- `SUPPORTED`
- `WEAKENED`
- `NOT_SUPPORTED`
- `REFERRED`
- `UNRESOLVED`

Do not use `PROVEN_CAUSE` unless an authorized canon owner actually supports that semantics.

### OperationalAdjustment

Represents what the venue does while the episode is active.

Fields:

- `adjustment_id`
- `episode_id`
- `effective_at`
- `owner_ref`
- `authority_or_voluntary_basis_ref`
- `affected_scope_id`
- `adjustment_type`
- `reason_refs[]`
- `planned_review_at`
- `ended_at`

Examples:

- pause one preparation station;
- limit a menu subset;
- stop use of one equipment item;
- reroute receiving;
- move service to another room;
- operate packaged-only service;
- temporarily pause all food preparation;
- close customer seating while corrective work occurs.

The generic engine never decides which adjustment is legally required.

### CorrectiveAction

Fields:

- `correction_id`
- `episode_id`
- `created_at`
- `target_condition_ref`
- `responsible_owner_ref`
- `action_description`
- `affected_scope_id`
- `started_at`
- `reported_complete_at`
- `evidence_refs[]`
- `related_maintenance_work_order_ref`
- `related_batch_action_ref`
- `verification_required`
- `status`

Possible statuses:

- `PLANNED`
- `IN_PROGRESS`
- `REPORTED_COMPLETE`
- `VERIFICATION_PENDING`
- `VERIFIED_FOR_SCOPE`
- `NOT_VERIFIED`
- `SUPERSEDED`

A repair should normally remain owned by Maintenance. This record references that work and preserves why it mattered to the food-service episode.

### VerificationRecord

Fields:

- `verification_id`
- `episode_id`
- `performed_at`
- `verifier_ref`
- `mandate_ref`
- `scope_id`
- `correction_refs[]`
- `evidence_checked_refs[]`
- `result`
- `residual_issue_refs[]`
- `follow_up_required`

Possible results:

- `VERIFIED_FOR_DEFINED_SCOPE`
- `PARTIALLY_VERIFIED`
- `NOT_VERIFIED`
- `INSUFFICIENT_EVIDENCE`
- `REFERRED_TO_OTHER_OWNER`

Verification must state what was checked. It cannot silently inherit the whole venue.

### ServiceDecision

Fields:

- `service_decision_id`
- `episode_id`
- `decided_at`
- `decision_owner_ref`
- `mandate_ref`
- `scope_id`
- `decision`
- `evidence_basis_refs[]`
- `conditions_or_limits[]`
- `review_time`
- `supersedes_decision_id`

Possible generic decisions:

- `SERVICE_CONTINUES`
- `SERVICE_LIMITED`
- `SERVICE_PAUSED`
- `SERVICE_RESUMED_FOR_SCOPE`
- `SERVICE_FULLY_RESUMED`

These labels describe world state. They do not create government powers.

### FollowUpCheckpoint

Fields:

- `checkpoint_id`
- `episode_id`
- `scheduled_or_triggered_at`
- `trigger_type`
- `scope_id`
- `evidence_refs[]`
- `outcome`
- `reopen_episode`

Triggers can include:

- planned follow-up;
- new complaint;
- new Community Health evidence;
- Batch Traceability update;
- new Maintenance fault;
- water-service update;
- later sample result;
- recurrence of the same observation.

### EpisodeClosure

Fields:

- `closure_id`
- `episode_id`
- `closed_at`
- `closed_by_owner_ref`
- `closure_type`
- `final_scope_id`
- `verified_corrections[]`
- `unresolved_questions[]`
- `open_handoff_refs[]`
- `monitoring_refs[]`
- `public_summary_ref`

A closure can coexist with open Community Health, Batch, Maintenance or Care work.

## Mandatory invariants

The following distinctions must survive every implementation:

`CONCERN_RECEIVED != CONDITION_VERIFIED`

`VENUE_MENTIONED != VENUE_CAUSAL`

`CUSTOMER_BECAME_ILL != VENUE_CAUSED_ILLNESS`

`HEALTH_CLUSTER_OPEN != FOOD_SERVICE_EPISODE_CONFIRMED`

`VISIBLE_MESS != FOOD_SAFETY_FAILURE`

`POKEMON_PRESENT != CONTAMINATION`

`ODOR_REPORTED != HAZARD_IDENTIFIED`

`EQUIPMENT_FAULT != FOOD_AFFECTED`

`MAINTENANCE_REPAIR_COMPLETE != FOOD_SERVICE_VERIFICATION_COMPLETE`

`BATCH_HELD != VENUE_CLOSED`

`BATCH_RELEASED != VENUE_REOPENED`

`WATER_SERVICE_RESTORED != KITCHEN_READY`

`SAMPLE_COLLECTED != SAMPLE_RESULT`

`SAMPLE_RESULT != CAUSAL_INTERPRETATION`

`CORRECTION_REPORTED != CORRECTION_VERIFIED`

`ONE_AREA_VERIFIED != WHOLE_VENUE_VERIFIED`

`SERVICE_RESUMED != MENU_FULLY_RESTORED`

`SERVICE_RESUMED != HEALTH_INVESTIGATION_CLOSED`

`EPISODE_CLOSED != PUBLIC_REPUTATION_RECOVERED`

`NO_RECURRENCE_OBSERVED != CAUSE_PROVEN`

## Multi-cause support

The architecture must allow more than one true operational issue.

Example:

- a cooling unit actually failed;
- the affected batch was never served because staff moved it in time;
- a separate customer complaint referred to a different item;
- Community Health later finds the illness cluster does not share the venue exposure.

All four facts can remain true simultaneously.

The system must not force every evidence branch into one culprit.

## Scope and time model

Every material conclusion must include:

- place or operational scope;
- time window;
- evidence version;
- owner/source;
- uncertainty where relevant.

A statement such as `kitchen verified` is too broad unless the authoring institution explicitly defines that phrase.

Prefer:

`prep_station_2 / 2026-08-29 09:00–11:30 / correction C-14 / verified by owner X using evidence refs ...`

Earlier states stay in Chronicle history.

## Public communication and rumor

Public messages belong to Communications/Public Information owners where those exist.

This extension may reference:

- venue notice;
- menu limitation notice;
- temporary closure notice;
- correction-completed notice;
- service-resumption notice;
- rumor or social report.

A public statement cannot overwrite internal evidence.

Useful conflict:

A sign says `OPEN` because the dining room is accessible while internal service records show that hot-food preparation remains paused. Both can be correct if their scopes differ.

## Privacy

Food-service episodes can touch health, employment and commercial records.

The generic Chronicle should expose only:

- public venue state;
- public notices;
- player-observable conditions;
- properly authorized evidence;
- aggregate or redacted references where necessary.

It should not copy:

- individual health records;
- private employee information;
- protected commercial recipes/processes;
- private laboratory details;
- unpublished regulatory records;
- personally identifying complaint data.

## Pokémon participation

An individual Pokémon can be authored as:

- kitchen partner;
- delivery assistant;
- customer;
- venue mascot;
- maintenance helper;
- agricultural supplier partner;
- trained sensory assistant if canon and mechanics explicitly support it.

The architecture never infers professional competence from species.

Examples of prohibited automatic reasoning:

- Fire type => safe cooking heat;
- Ice type => valid refrigeration;
- Water type => potable water;
- Poison type => contamination source;
- Psychic type => truthful interview;
- canine appearance => contamination detection;
- Bug type in kitchen => pest classification.

Any mechanical action needs exact PTU/Caelo authority and engine support.

## Quest grammar

### Intake without predetermined guilt

Player-facing opening:

- a familiar venue changes its menu unexpectedly;
- a counter closes while the dining room stays open;
- a worker asks for an old equipment log;
- a Community Health referral mentions the venue as one exposure among several;
- a supplier asks whether a specific delivery was used;
- a regular customer reports that two notices show different dates.

The quest should not announce the cause.

### Evidence convergence

At least two independent evidence routes should usually exist:

- service timeline;
- maintenance history;
- ingredient/batch provenance;
- staff observation;
- venue layout;
- photographs;
- water/cold-chain reference;
- public receipt/menu history;
- Community Health handoff.

One route may remain unavailable without making the quest unwinnable.

### Correction as consequence

Resolution should change the location:

- station physically replaced;
- counter moved;
- storage layout changed;
- menu temporarily narrower;
- opening hours adjusted;
- records posted differently;
- worker routine changed;
- temporary serving window becomes permanent;
- former kitchen room becomes storage;
- equipment memorialized as an old mistake or training example.

Later sessions can encounter those traces.

## Encounter contracts

Combat remains optional and independent from the safety determination.

### Encounter A — Kitchen Service Withdrawal

Narrative premise:
An unrelated hostile event reaches a venue while service is operating. Staff and customers must leave the affected service area so the episode can continue later.

Full intended version:

- explicit staff/customer withdrawal;
- Intercept protecting departing actors;
- potential forced movement around narrow exits;
- phased departure windows;
- protected corridor zones;
- reactions when hostile actors approach noncombatants;
- AI priorities `PROTECT`, `WITHDRAW`, `CLEAR_ROUTE`;
- semantic adapter playback for evacuation and service interruption.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL when damage is involved;
- status lifecycle — PARTIAL when status effects are involved;
- terrain/weather/hazards/zones/reactions — BLOCKING for protected corridor/reaction semantics;
- move-specific behavior — PARTIAL as selected combatants require it;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version — READY:

1. Ouros pauses service before BattleSpec creation.
2. Customers, workers, food, samples, records and controlled equipment are removed or secured through world state.
3. The battle begins only after a static exterior/service-access area has been declared safe enough to use as geometry.
4. Only explicit combatants enter BattleSpec.
5. Tactical victory records `immediate access/perimeter secured` only.
6. The food-service episode remains pending assessment/correction as applicable.

### Encounter B — Receiving Dock Diversion

Narrative premise:
A delivery or evidence-sensitive receiving operation is interrupted by a separate hostile event.

Full intended version:

- escort/withdrawal of workers;
- Intercept around a narrow receiving lane;
- controlled-object movement;
- potential spill/obstacle zones;
- timed handoff interruption;
- tactical AI protecting the route;
- semantic playback of custody pause.

Additional boundary:
The battle engine must never decide whether a food shipment remains acceptable. Food/Batch/Cold Chain owners handle that after the scene.

Reduced version — READY:

- receiving stops before combat;
- the shipment is placed outside BattleSpec under its existing custody owner;
- workers depart;
- BattleSpec uses a static dock perimeter;
- victory can permit the operational owner to reassess reopening of the receiving route;
- victory never marks delivery accepted, cold-chain valid, batch released or food safe.

Capability status is the same as Encounter A for rich escort/zone behavior.

### Encounter C — Follow-Up Visit Perimeter

Narrative premise:
A follow-up assessment is scheduled after corrections, but a separate conflict makes the site perimeter unsafe.

Full intended version:

- assessor withdrawal;
- protected evidence/equipment zones;
- Intercept/reactions;
- delayed access windows;
- objective-aware AI;
- semantic playback.

Reduced version — READY:

- the follow-up visit is suspended before combat;
- assessors, samples, logs and equipment leave BattleSpec;
- AutoPTU receives an ordinary static arena;
- after tactical resolution, the authorized owner may decide whether and when assessment resumes;
- combat cannot produce `VERIFIED_FOR_DEFINED_SCOPE`.

## Why reduced versions preserve narrative premise

The premise of each scene is operational interruption under pressure. It does not require the battle engine to simulate food safety.

By resolving noncombatant withdrawal and evidence custody before BattleSpec construction, Ouros preserves:

- the same location;
- the same reason the conflict matters;
- the same downstream consequences;
- the same Chronicle history;
- the same opportunity for later inspection/correction/reopening scenes.

Only unsupported tactical complexity is removed.

## Engine authority map — live Pass 131 evidence

Read-only AutoPTU-Java head checked during this pass:
`80f08b5d66f3451f70743ac0d4717f3a3dd21a0b`.

Verified local evidence includes a concrete Intercept PRE-target path plus server-owned derivation for Acrobatics/Athletics, Coaching and exact `Justified [Errata]` bonus on that route. Terrain remains an explicit input without a frozen generalized environment contract.

Read-only AutoPTU head checked during this pass:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its current change is viewport-resize presentation synchronization and does not alter tactical rules or outcomes.

Permanent categories therefore remain:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

## Minecraft/Cobblemon presentation contract

Minecraft may present facts already decided by Ouros:

- a counter closed with barriers;
- changed menu boards;
- replacement equipment;
- cleaned/rearranged storage;
- staff schedules;
- public reopening notice;
- removed seating;
- alternate entrance;
- delivery route rerouting;
- archived inspection/correction signage if canon allows it.

Minecraft must not infer authoritative facts from visuals.

Examples:

- dirty-looking texture does not create contamination;
- clean-looking blocks do not verify sanitation;
- fire blocks do not implement cooking-temperature rules;
- water blocks do not prove potable water;
- ice blocks do not prove refrigeration;
- entity proximity does not create cross-contamination;
- a Pokémon despawning does not prove removal;
- chest inventory does not prove batch custody;
- a door opening does not authorize reopening.

Cobblemon BattleState remains subordinate to the authoritative battle contract for combatants, legality, HP/status, positions and outcomes.

## Long-term continuity hooks

A closed episode can continue shaping the setting through:

- new equipment retained permanently;
- a service window introduced during correction that customers prefer;
- menu items retired or renamed;
- a supplier relationship changed;
- workers developing new routines;
- a former temporary prep room becoming permanent;
- public rumor lasting after formal closure;
- an old complaint becoming relevant to a later maintenance failure;
- a previous assessment making later chronology easier to reconstruct;
- a venue's reopening becoming part of neighborhood memory.

## Explicit UNKNOWN mechanical/canon questions

Mechanics remain UNKNOWN unless a governing source is later found for:

- generic food contamination;
- foodborne illness;
- allergen effects;
- spoilage;
- kitchen heat/steam/fire/spill hazards;
- cooking or cooling thresholds;
- sanitation/cleaning checks;
- food-service inspection Skill DCs;
- universal Chef safety certification;
- species-derived detection or sanitation;
- cooking/refrigeration/potable-water effects inferred from Type;
- specialized Moves/Abilities/Items/Trainer Features used as safety controls.

Canon remains open for:

- institutions and professions;
- mandates;
- inspection/review procedures;
- public/private records;
- service restriction authority;
- reopening authority;
- venue rating systems;
- festival/temporary-site rules;
- known historic incidents;
- professional Pokémon roles.

No answer to those questions is implied by this proposal.