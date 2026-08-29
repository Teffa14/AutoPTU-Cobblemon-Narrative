# Ouros Construction, Renovation & Project Handover Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-29
Research basis: `research/2026-08-29-construction-renovation-project-handover-scan-130.md`

## Purpose

This extension preserves the physical execution history between an already-authored project basis and the point where completed work is handed to the system that will operate, maintain or use it.

It exists because current Ouros systems deliberately split responsibility:

- Civic Governance can authorize and sponsor public works but should not simulate every work package;
- Facility Maintenance owns faults and repairs after facilities exist, and explicitly avoids becoming a universal construction simulator;
- Building Safety owns scoped use/reentry assessment after damage, not ordinary project execution;
- Procurement owns sourcing and fulfillment, not field installation;
- Material Culture owns material identity and provenance, not construction progress;
- Workplace owns people, schedules and workplace facts, not physical completion;
- service owners decide whether the completed place actually begins operating.

This extension owns continuity for authored construction, renovation, demolition/redevelopment and physical handover. It does not invent engineering, building law, permits, property rights, procurement law, labor law, construction prices, schedules, structural calculations or inspection authority.

## Authority rule

A construction project requires an upstream basis.

For public works, that basis may be an approved Civic Governance project.

For a private, institutional, League, conservation, research, residential or other project, canon must establish the sponsor, site access and scope by some other valid world-state relationship.

This extension cannot create permission to build merely because a quest needs a worksite.

```yaml
construction_project:
  project_id: null
  upstream_project_or_authority_refs: []
  sponsor_actor_or_institution_ids: []
  project_type: authored
  site_location_ids: []
  predecessor_structure_ids: []
  intended_successor_structure_ids: []
  current_scope_version_id: null
  work_package_ids: []
  discovery_case_ids: []
  temporary_work_ids: []
  verification_requirement_ids: []
  handover_scope_ids: []
  residual_work_ids: []
  downstream_owner_refs: []
  current_execution_state: planned
  history_event_ids: []
  canon_basis_ids: []
```

Candidate project types are descriptive only:

- new construction;
- expansion;
- renovation;
- adaptive reuse;
- replacement;
- demolition and redevelopment;
- phased rebuild;
- site conversion;
- authored specialist project.

## Core invariants

The following distinctions are mandatory:

`PROJECT_AUTHORIZED != WORK_STARTED`

`WORK_STARTED != WHOLE_SITE_CLOSED`

`MATERIAL_DELIVERED != MATERIAL_INSTALLED`

`INSTALLED != VERIFIED`

`WORK_PACKAGE_COMPLETE != PROJECT_COMPLETE`

`PHYSICAL_COMPLETION != USE_AUTHORIZATION`

`USE_READY_FOR_SCOPE != SERVICE_OPERATIONAL`

`OPERATOR_HANDOVER != RESIDUAL_WORK_CLOSED`

`DEMOLITION_COMPLETE != SITE_HISTORY_DELETED`

`DISCOVERY_RECORDED != DISCOVERY_INTERPRETED`

`DRAWING_OR_SCOPE_REVISED != FIELD_CHANGE_COMPLETED`

`WORK_PAUSED != PROJECT_CANCELLED`

`BATTLE_WON != WORK_ACCEPTED`

These rules prevent the narrative generator, Minecraft adapter and battle engine from silently manufacturing project conclusions.

## 1. Scope versions

Physical projects change over time. Preserve each authored scope rather than rewriting the original plan.

```yaml
construction_scope_version:
  scope_version_id: null
  project_id: null
  version_label: null
  issued_at: null
  effective_from: null
  authored_by_refs: []
  spatial_scope_refs: []
  intended_output_refs: []
  included_work_package_ids: []
  excluded_scope_refs: []
  dependency_ids: []
  change_reason_refs: []
  source_record_ids: []
  supersedes_scope_version_id: null
  status: active
```

A revision can narrow, expand or reroute work only when an authorized project process produces that change.

The extension stores the revision. It does not invent who has authority to approve it.

## 2. Work packages

Large projects should advance through bounded work packages rather than one percentage meter.

```yaml
construction_work_package:
  work_package_id: null
  project_id: null
  scope_version_id: null
  spatial_scope_refs: []
  work_description: null
  prerequisite_ids: []
  material_delivery_refs: []
  equipment_or_asset_refs: []
  assigned_workplace_refs: []
  supporting_pokemon_refs: []
  access_condition_refs: []
  started_at: null
  completed_at: null
  current_state: planned
  evidence_refs: []
  verification_requirement_ids: []
  discovered_condition_ids: []
```

Suggested states:

- PLANNED
- READY
- WAITING_ON_DEPENDENCY
- MOBILIZING
- ACTIVE
- PAUSED
- PHYSICALLY_COMPLETE
- WAITING_FOR_VERIFICATION
- VERIFIED_FOR_DEFINED_SCOPE
- CORRECTION_REQUIRED
- HANDED_OVER
- CANCELLED_BY_AUTHORIZED_CHANGE
- SUPERSEDED

`PHYSICALLY_COMPLETE` only means the authored physical package reports completion. It does not prove safety, performance, legal acceptance or operational readiness.

## 3. Worksite spatial state

A worksite can remain partly accessible.

```yaml
construction_site_zone:
  site_zone_id: null
  project_id: null
  geometry_ref: null
  zone_role: authored
  current_access_state: unknown
  owner_system_access_refs: []
  active_work_package_ids: []
  temporary_work_ids: []
  public_route_refs: []
  hazard_claim_refs: []
  last_verified_at: null
```

Candidate narrative zone roles:

- active work area;
- material staging;
- equipment staging;
- temporary pedestrian route;
- temporary vehicle route;
- retained public access;
- completed-but-not-handed-over scope;
- handed-over scope;
- protected discovery area;
- inactive future phase.

These are world-state labels. They are not tactical terrain types.

A closed zone in the project record does not automatically become impassable in AutoPTU. Base movement legality and BattleSpec geometry remain engine-owned.

## 4. Physical progress evidence

Do not derive project state from Minecraft blocks alone.

```yaml
construction_progress_event:
  progress_event_id: null
  project_id: null
  work_package_id: null
  occurred_at: null
  progress_type: authored
  observed_by_refs: []
  evidence_refs: []
  installed_asset_refs: []
  removed_structure_refs: []
  unresolved_notes: []
  source_system_refs: []
```

Possible progress types:

- mobilization recorded;
- removal/demolition step recorded;
- installation step recorded;
- area made physically complete;
- temporary route activated;
- temporary route removed;
- correction completed;
- site cleaned for handover;
- record package updated.

No progress event implies engineering conformance unless a separate verification record says so.

## 5. Discovered conditions

Construction often exposes facts that another system owns.

```yaml
construction_discovered_condition:
  discovery_id: null
  project_id: null
  work_package_id: null
  site_zone_id: null
  discovered_at: null
  observer_refs: []
  observation_claim_ids: []
  evidence_refs: []
  affected_scope_refs: []
  immediate_project_effect: none
  referred_owner_system_refs: []
  interpretation_record_refs: []
  authorized_scope_change_refs: []
  status: open
```

Safe project effects include:

- NONE
- LOCAL_PAUSE
- PACKAGE_PAUSE
- ACCESS_RESTRICTION_PENDING_REVIEW
- WAITING_ON_OWNER_SYSTEM
- SCOPE_REVIEW_REQUESTED

The construction extension must not interpret the discovery when another owner exists.

Examples:

- old masonry or artifacts → History/Archaeology owner;
- active nest or habitat feature → Ecology/Conservation;
- undocumented pipe/cable → relevant utility/infrastructure owner;
- unknown material/odor → Pollution/Waste or appropriate evidence owner;
- unexpected water flow → Water/Drainage;
- boundary discrepancy → Land/Boundary continuity;
- unstable existing structure → Building Safety/Facility assessment;
- suspicious object → Case/Evidence if the world facts justify that handoff.

A discovery can pause only the bounded affected scope while unaffected work packages continue.

## 6. Temporary works and temporary routes

Temporary construction changes can outlive their original purpose.

```yaml
construction_temporary_work:
  temporary_work_id: null
  project_id: null
  purpose: authored
  location_ref: null
  created_at: null
  intended_end_trigger: null
  current_state: active
  access_or_service_refs: []
  maintenance_owner_ref: null
  conversion_proposal_ref: null
  removed_at: null
  retained_as_permanent_ref: null
```

Examples can include temporary paths, barriers, platforms, offices, storage, access gates, service bypasses or public waiting areas where the established technology permits them.

If a temporary feature becomes useful socially, later retention is a new authored decision. The construction system does not make it permanent by inertia.

## 7. Demolition and predecessor history

Redevelopment must preserve what was there before.

```yaml
construction_structure_transition:
  transition_id: null
  project_id: null
  predecessor_structure_id: null
  successor_structure_ids: []
  site_location_id: null
  old_use_end_event_id: null
  removal_event_ids: []
  retained_component_refs: []
  successor_completion_refs: []
  archive_record_refs: []
  public_memory_refs: []
```

The predecessor structure remains queryable historically after demolition.

Valid future storytelling can reference:

- old entrances;
- former loading zones;
- foundations;
- retained walls;
- buried utility alignments;
- earlier place names;
- former workers or users;
- photographs and maps;
- artifacts moved elsewhere.

None of these is generated automatically. They require authored or observed evidence.

## 8. Verification requirement

Verification is scoped and evidence-based.

```yaml
construction_verification_requirement:
  verification_requirement_id: null
  project_id: null
  work_package_ids: []
  scope_refs: []
  verifying_institution_or_actor_refs: []
  authority_or_competence_basis_refs: []
  question_to_verify: null
  required_input_refs: []
  current_state: pending
  verification_record_ids: []
```

Possible states:

- PENDING
- READY_FOR_REVIEW
- IN_REVIEW
- PASSED_FOR_DEFINED_SCOPE
- CORRECTION_REQUIRED
- MORE_INFORMATION_REQUIRED
- SUPERSEDED
- NOT_APPLICABLE_BY_AUTHORED_SCOPE

No universal verification authority exists. Canon or an existing institutional system must supply the actor, competence and mandate.

## 9. Verification record

```yaml
construction_verification_record:
  verification_record_id: null
  requirement_id: null
  performed_at: null
  performer_refs: []
  scope_refs: []
  evidence_refs: []
  observations: []
  result: authored
  limitation_notes: []
  correction_work_refs: []
  followup_requirement_refs: []
```

An unfavorable result creates bounded correction or further review. It does not erase completed work history.

## 10. Commissioning boundary

Some authored facilities may require functional verification of installed systems before normal operation.

```yaml
construction_commissioning_record:
  commissioning_id: null
  project_id: null
  system_or_asset_refs: []
  governing_technology_or_facility_refs: []
  test_or_review_definition_refs: []
  performed_by_refs: []
  performed_at: null
  result_claim_ids: []
  deficiency_refs: []
  documentation_handoff_refs: []
  operator_training_or_orientation_refs: []
  status: authored
```

This object is allowed only when the relevant technology/facility canon already defines what can be tested or verified.

The generator must not invent voltages, pressures, structural loads, fire tests, medical validation, network throughput or other technical criteria.

`EQUIPMENT_INSTALLED != SYSTEM_VERIFIED`.

`SYSTEM_VERIFIED != SERVICE_LAUNCHED`.

## 11. Partial completion and scoped handover

A project can transfer one usable scope while other work remains active.

```yaml
construction_handover_scope:
  handover_scope_id: null
  project_id: null
  spatial_scope_refs: []
  work_package_ids: []
  verification_record_refs: []
  residual_work_ids: []
  proposed_receiving_owner_refs: []
  handover_event_id: null
  current_state: preparing
  use_readiness_ref: null
```

Suggested states:

- PREPARING
- WAITING_ON_VERIFICATION
- USE_READY_FOR_DEFINED_SCOPE
- HANDOVER_OFFERED
- HANDED_OVER
- HANDOVER_DEFERRED
- RETURNED_FOR_CORRECTION
- SUPERSEDED

A scope can be handed over while another floor, route section, wing or adjacent parcel remains under work.

## 12. Handover event

```yaml
construction_handover_event:
  handover_event_id: null
  project_id: null
  handover_scope_id: null
  occurred_at: null
  transferring_actor_or_institution_refs: []
  receiving_owner_refs: []
  asset_refs: []
  documentation_refs: []
  known_residual_work_refs: []
  operating_condition_refs: []
  maintenance_handoff_refs: []
  service_activation_handoff_refs: []
  evidence_refs: []
```

Handover changes the project/owner relationship only to the extent established by canon.

It does not itself:

- authorize every use;
- open a business;
- start a train/ferry/clinic/school;
- create staff;
- clear an unrelated safety restriction;
- erase defects;
- complete financial closeout;
- establish ownership if ownership was not already defined.

## 13. Residual work

Small remaining tasks can coexist with use when the receiving owner and any relevant safety authority permit it.

```yaml
construction_residual_work:
  residual_work_id: null
  project_id: null
  handover_scope_id: null
  description: null
  spatial_scope_ref: null
  responsible_workplace_or_actor_refs: []
  access_condition_refs: []
  blocks_use: false
  blocks_service: false
  completion_evidence_refs: []
  current_state: open
```

`RESIDUAL_WORK_OPEN` is not automatically a safety problem.

Whether it blocks use comes from the proper owner and assessment state.

## 14. Project record closeout

Physical work can be over while the record remains open.

```yaml
construction_project_closeout:
  closeout_id: null
  project_id: null
  physical_completion_refs: []
  handover_refs: []
  residual_work_state_refs: []
  archive_package_refs: []
  unresolved_claim_refs: []
  downstream_owner_confirmation_refs: []
  closed_at: null
  current_state: open
```

This is a narrative archive state only. It does not model real-world financial or contractual closeout unless a separate canon system explicitly does so.

## 15. Change lineage

Never overwrite a superseded project state.

A project may accumulate:

```text
scope v1
→ discovery
→ local pause
→ specialist interpretation
→ scope v2
→ work resumes outside protected area
→ package A completes
→ package A verified
→ package A handed over
→ package B corrected
→ project archive closes later
```

Each step remains visible to Chronicle, Evidence Graph and Public Memory according to access rules.

## 16. Construction and service continuity

The service owner always gets the final say about service state.

Examples:

```text
clinic wing handed over
→ Care/Facility owner decides staffing, readiness and opening

new station platform handed over
→ Rail service layer decides whether trains serve it

market building handed over
→ Commercial/Public Space owner decides vendor activation

research building handed over
→ Science institution decides equipment/staff/program launch

habitat crossing handed over
→ Conservation/Ecology decides monitoring and operational effect

new road segment handed over
→ Roads/Travel decides route availability and restrictions
```

Construction never writes `SERVICE_OPERATIONAL=true` by itself.

## 17. Construction and Facility Maintenance boundary

During active project execution, correction work that belongs to incomplete construction remains a construction work package or residual item.

After a handed-over asset enters ordinary operation, later faults and ordinary repair move to Facility Maintenance.

A latent problem discovered later can reference the original project history without reopening every old work package.

## 18. Construction and Building Safety boundary

Building Safety decides scoped use/reentry authorization where its authority is relevant.

Construction may say:

- physical work is complete;
- a verification record exists;
- a correction is done;
- handover is offered.

It may not say:

- the public may occupy the building;
- every floor is safe;
- a post-hazard restriction is lifted.

Those conclusions come from the correct safety/use owner.

## 19. Construction and Procurement boundary

Procurement owns supplier selection, orders, delivery obligations and supplier fulfillment.

Construction consumes delivery events and records whether material/asset instances were installed into a project scope.

`ORDER_FULFILLED != INSTALLED`.

`DELIVERED_TO_SITE != ACCEPTED_INTO_WORK`.

`INSTALLED != VERIFIED`.

## 20. Construction and Land/Boundary boundary

The project references site geometry and access claims established elsewhere.

A fence, survey marker or Minecraft chunk boundary cannot create building rights.

If excavation or layout exposes a discrepancy, the project records a discovery and waits on Land/Boundary or the relevant canon authority.

## 21. Construction and History/Archaeology boundary

An old structure, artifact or buried feature discovered during work is evidence.

Construction may protect the bounded area and pause work. History/Archaeology or another established owner interprets significance and future treatment.

Do not generate a universal archaeology-stop-work law.

## 22. Construction and Ecology/Conservation boundary

Pokémon presence, nesting, migration or habitat observations do not automatically stop construction.

If an authored conservation process establishes a restriction, construction consumes that restriction as a dependency.

Species identity alone cannot create environmental authority.

## 23. Pokémon workplace participation

Construction work may include individual Pokémon only when existing Pokémon Agency/Work state establishes the relationship and exact capabilities support the described task.

Forbidden inference examples:

- Fighting type means construction worker;
- Rock type means excavation specialist;
- Steel type means structural specialist;
- Electric type means electrician;
- Psychic type means crane substitute;
- Flying type means certified lifting support;
- Strength means unlimited cargo capacity;
- Dig means safe excavation of any foundation;
- Rock Smash means controlled demolition;
- any species flavor grants engineering judgment.

When a Move, Ability, Skill, Capability or Trainer Feature matters mechanically, use the exact PTU/Caelo rule and current engine support.

## 24. NPC roles without invented authority

Possible authored roles can include:

- project coordinator;
- site supervisor;
- craft worker;
- equipment operator;
- material receiver;
- inspector/verifier where canon defines one;
- facility representative;
- service owner representative;
- local historian;
- conservation liaison;
- neighboring resident or vendor;
- temporary-route coordinator.

A title never creates legal authority by itself.

## 25. Narrative event types

Useful event grammar:

- PRECONSTRUCTION_SITE_WALK
- WORKSITE_OPENED
- PACKAGE_STARTED
- ACCESS_CHANGED
- MATERIAL_DELIVERED
- INSTALLATION_RECORDED
- DISCOVERY_RECORDED
- LOCAL_PAUSE_STARTED
- SPECIALIST_HANDOFF_CREATED
- SCOPE_REVISION_ISSUED
- PACKAGE_RESUMED
- PACKAGE_PHYSICALLY_COMPLETE
- VERIFICATION_STARTED
- CORRECTION_REQUIRED
- CORRECTION_COMPLETED
- USE_READY_FOR_SCOPE
- HANDOVER_COMPLETED
- SERVICE_OWNER_HANDOFF
- TEMPORARY_WORK_RETAINED_BY_NEW_DECISION
- RESIDUAL_WORK_COMPLETED
- PROJECT_RECORD_CLOSED

These event names do not imply a universal procedure.

## 26. Quest grammar

Construction stories should usually arise from a real project state rather than a generic fetch quest.

Quest-generating conditions include:

- a missing dependency blocks a work package;
- a discovery needs evidence delivered to the correct owner;
- two records disagree about which scope version is active;
- a temporary route creates an unexpected social/ecological pattern;
- a completed package waits on bounded verification;
- a partial handover changes how a district moves;
- a predecessor structure has an unresolved historical trace;
- material arrived at the project but custody/installation history is unclear;
- residual work intersects an already-open service;
- a later fault requires reconstructing project history.

## 27. Environmental storytelling

Visible project evolution can be one of Ouros' strongest long-term continuity tools.

Candidate visuals:

- survey stakes and string during early layout;
- excavation or cleared footprint where canon supports it;
- partial foundations or structural frames;
- staged material areas;
- temporary fences and gates;
- alternate pedestrian routes;
- partial façade completion;
- completed wing beside active work;
- old structure fragments retained in redevelopment;
- temporary kiosks that later remain under a new decision;
- archived project boards or photographs;
- new signage after handover;
- removed construction overlay with subtle scars left behind.

The visual progression must project authoritative construction state. It cannot be the authority itself.

## 28. Minecraft/Cobblemon adapter boundary

Minecraft/Cobblemon may display:

- project zones;
- scaffold-like authored structures;
- temporary paths;
- material props;
- workers and known Pokémon participants;
- progressive structure variants;
- closed/open gates;
- signage;
- machinery animations if canon supports the technology;
- handover/opening visual changes.

Minecraft must not determine:

- work-package completion from block counts;
- structural adequacy from block type;
- access authority from a door state;
- installation acceptance from item placement;
- inspection results from player proximity;
- project progress from chunk load state;
- Pokémon worker competence from entity type;
- safe occupancy from collision geometry.

Cobblemon BattleState remains outside combatant selection, legality, HP/status, tactical positions and project outcomes.

## 29. Offline advancement

Routine construction can advance while players are away only through explicit project clocks and satisfied dependencies.

Safe coarse progression:

`READY → ACTIVE → PHYSICALLY_COMPLETE → WAITING_FOR_VERIFICATION`

or

`ACTIVE → DISCOVERY_RECORDED → PAUSED`

Offline advancement must not silently:

- resolve a major historical/ecological discovery;
- decide a contested scope revision;
- approve a use authorization;
- declare a disputed verification passed;
- force a player-owned material/item transfer;
- invent a Pokémon capability;
- complete an irreversible demolition important to an active player promise without authored permission.

## 30. Long-term world-state value

A completed project should become ordinary infrastructure while retaining project history for later stories.

Years later the engine may validly ask:

- which section was original and which was added later;
- why the road bends around one old foundation;
- why two floors use different numbering;
- why a temporary path became a neighborhood shortcut;
- who remembers the predecessor building;
- which correction was made before handover;
- which area opened months before the rest;
- which archived drawing predates a scope change.

This turns construction into world history instead of scenery that disappears after a quest.

## 31. Encounter contract — Worksite Withdrawal

Narrative premise:

An active worksite must be cleared after an unrelated battle-capable threat enters the perimeter. The construction crew's objective is safe withdrawal and preservation of already-secured project evidence, not defeating the threat themselves.

Full intended version:

- workers and any lawful noncombatant Pokémon withdraw through defined exits;
- Intercept may protect a withdrawing actor;
- forced movement can matter near restricted edges;
- equipment or temporary lanes can change available routes only if exact mechanics exist;
- environmental hazards such as falling material, moving machinery, unstable surfaces or dust exist only if exact governing mechanics and engine support exist;
- allied/enemy AI understands PROTECT/WITHDRAW/CLEAR_ROUTE priorities;
- adapter playback shows the worksite pausing and actors leaving.

Permanent capability classification:

- targeting/footprints/range/LoS — VERIFIED baseline only;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic worksite hazards, protected lanes and generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for PROTECT/WITHDRAW/CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version: READY.

Before BattleSpec creation, Ouros pauses the work package, powers down or secures authored equipment through world state, withdraws workers/noncombatants, moves controlled materials and project records outside the tactical grid and selects a static reviewed perimeter.

AutoPTU resolves only the conventional battle. Victory can mark the immediate perimeter secure enough for the owner systems to reassess. It cannot complete work, verify equipment, authorize reentry or hand over the project.

## 32. Encounter contract — Partial Handover Corridor

Narrative premise:

One finished project scope is ready for transfer while adjacent construction remains active. An encounter blocks the static corridor linking the receiving operator to the handed-over area.

Full intended version:

- protected corridor objective;
- Intercept and forced displacement around corridor edges;
- phased movement of receiving staff;
- boundary-crossing reactions if exact reaction infrastructure exists;
- AI policy values the corridor rather than only KOs;
- semantic playback distinguishes handed-over and active-construction scopes.

Capability classification matches Worksite Withdrawal. Complete movement remains PARTIAL; generalized zones/reactions, tactical policy and adapter/playback remain BLOCKING.

Reduced version: READY.

Receiving staff remain outside BattleSpec. The handover is paused before combat. AutoPTU receives a static approach arena with no live construction effects. After battle, Construction and the receiving owner separately decide whether handover resumes.

A victory never means `HANDED_OVER` automatically.

## 33. Encounter contract — Discovery Protection Perimeter

Narrative premise:

A work package exposes an unexpected feature. Work stops locally and a specialist owner is requested. Before interpretation occurs, a battle-capable threat makes the static perimeter unsafe.

Full intended version can require:

- PROTECT/EXCLUDE objective;
- dynamic restricted zones;
- forced movement around protected evidence;
- reactions to entering a protected area;
- objective-aware AI;
- semantic playback of barriers, evidence and specialist arrival.

Reduced version: READY.

The discovery object and all records remain outside BattleSpec and cannot be targeted. Workers and specialists withdraw. AutoPTU resolves a conventional battle on nearby static geometry. Success merely permits the specialist owner to return later.

The battle cannot identify, authenticate, classify, excavate, destroy, preserve or authorize treatment of the discovery.

## 34. Optional full-version environmental dependencies

Do not include any of these until exact PTU/Caelo rules and engine contracts verify them:

- falling-object attacks or debris zones;
- collapsing scaffold or floor cells;
- dust clouds affecting LoS/accuracy;
- moving vehicle/machinery collision;
- conveyor or crane forced movement;
- wet concrete or adhesive restraint;
- electrical exposure;
- open excavation fall rules;
- unstable slopes;
- heat from active work;
- noise-induced statuses;
- load-bearing destructible objects;
- protective equipment effects.

Each concept must name its exact capability families and governing rules when implemented.

## 35. Permanent capability map used by this extension

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

No family is promoted from a single Intercept path or visual frontend fix.

## 36. Current implementation-safe pattern

For a mechanically rich construction scene today:

1. resolve project scope, work-package state and authority in Ouros;
2. pause active work when combat would overlap the site;
3. withdraw workers, controlled materials, records and noncombatants;
4. preserve discoveries outside tactical ownership;
5. choose static reviewed geometry;
6. select combatants explicitly in Ouros;
7. let AutoPTU execute only currently supported battle mechanics;
8. return a bounded tactical result;
9. let Construction decide whether the worksite can be reassessed;
10. let specialist/service/safety owners decide their own downstream facts.

## 37. Canon promotion questions

Before any concrete Ouros construction regime becomes canon, decide only where needed:

- which institutions sponsor or execute projects;
- how private/institutional/public project authority differs, if at all;
- what construction technologies exist by region;
- which trades, professions and specialist roles are established;
- how site access is authorized;
- what verification or inspection institutions exist;
- whether partial handover is common or exceptional;
- which project records are public, private or institutional;
- how archaeological/ecological/utility discoveries are referred;
- how demolition and adaptive reuse are decided;
- which individual Pokémon have documented construction roles;
- which completed or abandoned projects already shape Ouros history;
- which exact PTU/Caelo mechanics may ever apply to worksite hazards.

No answer is assumed by this extension.