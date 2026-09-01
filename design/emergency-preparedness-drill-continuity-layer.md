# Emergency preparedness, drill, and continuity layer

Status: PROPOSED DESIGN. No canon facts are created by this file.
Pass: 184

## Purpose

This layer gives Ouros a persistent way to model preparation before an incident: current plans, rehearsals, muster assumptions, staged supplies, alert distribution, corrective work, and plan revision. It connects existing systems instead of creating a second emergency, quest, knowledge, or authority stack.

Institutional delegation remains authoritative for who may approve or activate a plan. Communications remains authoritative for who received which notice or correction. Shared-resource access remains authoritative for closures and restricted spaces. Field-search/wayfinding remains authoritative if a person becomes genuinely unaccounted for. Persistent-site aftermath remains authoritative for physical damage and recovery. Local knowledge remains authoritative for what individual actors believe about an incident.

## Core records

### preparedness_plan

A plan is versioned operational knowledge, not world truth.

Suggested fields:

- `plan_id`
- `plan_version`
- `status`: draft / approved / superseded / suspended / retired
- `scope_location_ids`
- `covered_scenarios`
- `planning_assumptions`
- `activation_authority_role_ids`
- `participant_role_ids`
- `notification_channels`
- `primary_muster_site_id`
- `fallback_muster_site_ids`
- `primary_route_segment_ids`
- `fallback_route_segment_ids`
- `staged_resource_ids`
- `access_restrictions`
- `companion_pokemon_considerations`
- `accessibility_considerations`
- `approval_record`
- `effective_from`
- `review_due_at`
- `supersedes_plan_version`
- `unresolved_assumptions`

The record must preserve older versions. A printed notice, copied checklist, or NPC memory can still refer to a superseded version.

### drill_run

A drill is an observed test of a specific plan version.

Suggested fields:

- `drill_id`
- `plan_id`
- `plan_version_tested`
- `scenario_id`
- `announced_state`
- `started_at`
- `ended_at`
- `participant_actor_ids`
- `observer_actor_ids`
- `expected_steps`
- `observed_steps`
- `timing_observations`
- `communication_observations`
- `route_observations`
- `muster_observations`
- `resource_observations`
- `accessibility_observations`
- `companion_pokemon_observations`
- `deviations`
- `evidence_refs`
- `after_action_item_ids`
- `closed_at`

A drill may be partially successful. Avoid a single readiness percentage.

### preparedness_cache

This record links physical resources to custody and inspection.

Suggested fields:

- `cache_id`
- `physical_site_id`
- `custodian_role_id`
- `inventory_refs`
- `last_inspected_at`
- `next_inspection_due_at`
- `borrowed_item_refs`
- `condition_notes`
- `availability_state`
- `seal_or_marker_state`
- `evidence_refs`

The Minecraft object is presentation of the cache. The server-owned record decides whether contents are available.

### after_action_item

A finding becomes useful when it has an owner and a corrective path.

Suggested fields:

- `item_id`
- `source_drill_id_or_incident_id`
- `observation`
- `supporting_evidence_refs`
- `affected_plan_id`
- `affected_plan_version`
- `responsible_role_id`
- `corrective_action`
- `status`
- `target_date`
- `completion_evidence_refs`
- `requires_retest`
- `retest_drill_id`

Closing an item should require evidence appropriate to the action. Editing a sign can close a signage issue. It cannot prove an entire evacuation plan effective.

## Alert and operational posture

Implementation may need a generic server state for a location or plan. Proposed engine-neutral values are NORMAL, WATCH, PREPARE, RESTRICTED_OPERATIONS, RELOCATE, SHELTER, and ALL_CLEAR.

These names are schema vocabulary only. They are not canon Marea or Caelo terminology. Promotion requires setting evidence and authority rules.

A posture transition should record issuer/authority, trigger evidence, scope, time, affected plan version, distributed notices, and any superseded posture. The visible bell, sign, light, NPC animation, or chat message projects that state. It does not create it.

## Permanent invariants

`DRILL_COMPLETED != READY_FOR_ALL_HAZARDS`

`PLAN_PRESENT != AUTHORITY_GRANTED`

`ALERT_SIGNAL_OBSERVED != HAZARD_CONFIRMED`

`MUSTER_POINT_DESIGNATED != MUSTER_POINT_CURRENTLY_SAFE`

`CACHE_OBJECT_PRESENT != CACHE_CONTENTS_AVAILABLE`

`OLD_PLAN_FOUND != CURRENT_PLAN`

`BATTLE_VICTORY != ALL_CLEAR`

`NPC_AT_MUSTER_POINT != ACCOUNTED_FOR_WITHOUT_IDENTITY_EVIDENCE`

`NOT_AT_MUSTER != MISSING_CONFIRMED`

`MINECRAFT_SIGN_STATE != AUTHORITATIVE_ALERT_STATE`

`COBBLEMON_ENTITY_DESPAWN != EVACUATED`

`PLAYER_ABSENT != PREPAREDNESS_FROZEN`

`POKEMON_COMPANION != CARGO`

A companion Pokémon may have mobility, care, stress, size, communication, custody, or medical needs. Those needs must be represented through existing character/Pokémon state and authored rules rather than an inventory shortcut.

## Activation flow

A safe generic flow is:

`OBSERVATION / FORECAST / INCIDENT REPORT`
`-> AUTHORITY CHECK`
`-> CURRENT PLAN VERSION RESOLUTION`
`-> POSTURE OR PLAN ACTIVATION`
`-> NOTICE DISTRIBUTION`
`-> ACCESS / ROUTE CHANGES`
`-> ACCOUNTING / TASK ASSIGNMENT`
`-> EVENT OR DRILL EXECUTION`
`-> AFTER-ACTION OBSERVATIONS`
`-> CORRECTIVE ITEMS`
`-> PLAN REVISION`
`-> RETEST`

The first observation does not have to prove the hazard. A watch or preparation posture can be justified by attributed uncertainty if setting/canon allows that authority.

## Muster and accounting

Muster accounting should consume actual expected-presence records, work schedules, ferry arrivals where legitimate, voluntary check-ins, and direct observations. It must not read omniscient entity coordinates.

An unmatched expected person produces an ACCOUNTING_UNRESOLVED state first. Verification may resolve it as a schedule change, duplicate record, visitor departure, alternate muster, communications failure, or a genuine missing-person concern. Only the existing field-search layer should open and manage the latter.

Visitors and temporary workers need explicit provenance. Privacy policy remains an unresolved canon/setting question.

## Routes and access

Preparedness plans reference physical route segments already known by the world model. The plan does not make a route passable. Current site condition, closures, access permits, weather/terrain authority, and aftermath state remain independent inputs.

A fallback route may become primary during one event and return to fallback afterward. Preserve that event history rather than rewriting the plan retrospectively.

## Drills as ordinary world activity

A drill can run without the player. Named residents can rehearse a checklist, inspect a cache, move records, test a communications chain, time a route, or discover a blocked doorway. The player can participate, observe, arrive halfway through, or only encounter the corrective work later.

Useful drill failures are mundane and attributable: an old map, a locked gate, a borrowed cart, a notice sent to the wrong recipient, a large companion unable to use a narrow route, an inaccessible step, a roster that still lists someone absent, a cache whose contents were used and not replenished, or two institutions using different plan versions.

Do not manufacture a catastrophe to justify every exercise.

## After-action continuity

An after-action review produces evidence-backed findings. The repository should retain both successful and unsuccessful observations. The next plan version links to the previous version and to the corrective items that caused the change.

This permits visible persistence. A relocated cache, widened access lane, corrected map, revised contact list, new sign, changed muster point, or reassigned responsibility can remain in the Minecraft world after the quest text is gone.

## Battle handoff rule

Preparedness authority stays outside AutoPTU. If an incident includes combat, Narrative compiles a BattleSpec only for the tactical facts AutoPTU owns. The battle outcome returns narrow physical consequences. It cannot emit emergency authority, plan approval, all-clear status, evacuation completion, cause of the hazard, institutional promotion, or readiness certification.

## Mechanically rich reference encounter: Mirador Safe-Down Under Live Pressure

Full intended version: a planned Mirador safe-down drill is interrupted by genuine wild activity and worsening environmental conditions. Nerea and Ema must preserve a minimal observation record while residents and companion Pokémon move toward safe positions. A temporary access lane matters. Wild actors may contest or cross that lane. Equipment must not become tactical loot merely because it is present.

Capability dependencies for the intended version:

- targeting/footprints/range/LoS — REQUIRED
- base movement legality — REQUIRED
- complete movement including push/pull/knockback/interception/forced movement — REQUIRED if lane protection, displacement, interception, forced retreat, collision, or partial stops are represented tactically
- core calculations — REQUIRED
- action economy/initiative — REQUIRED
- full turn/round lifecycle — REQUIRED
- full stateful damage pipeline — REQUIRED
- status lifecycle — REQUIRED for any selected roster/environment that can apply statuses
- terrain/weather/hazards/zones/reactions — REQUIRED if deteriorating conditions or safety lanes have tactical effects
- move-specific behavior — REQUIRED and roster-audited
- abilities — REQUIRED and roster-audited
- items — REQUIRED if any selected actor/item enters BattleSpec
- Trainer Features/perks — REQUIRED if any selected Trainer uses them
- AI legal-action infrastructure — REQUIRED
- AI tactical policy — REQUIRED for context-sensitive hostile/allied decisions
- Minecraft/Cobblemon/Craftics adapter/playback support — REQUIRED for faithful live in-world presentation

Current readiness: BLOCKED for the full version because several complete capability families remain partial or blocking.

Reduced executable version: the safe-down, accounting, equipment custody, route decision, and companion relocation occur as authoritative world-state actions before BattleSpec. Civilians, records, caches, and instruments remain outside the battle. If a wild threat prevents withdrawal, an audited ordinary battle occurs later on stable terrain with a mechanically vetted roster and no unsupported environmental effects.

Allowed battle handoffs are narrow, for example `IMMEDIATE_ACCESS_CORRIDOR_CLEAR` or `IMMEDIATE_WILD_THREAT_WITHDREW`. Narrative separately decides whether the drill continues, whether the real incident posture changes, whether equipment was damaged, whether every actor is accounted for, and when an all-clear is authorized.

This reduced version preserves the premise: a community discovers whether its preparation works when conditions stop matching the checklist.

## Minecraft/Cobblemon projection

Useful projections include physical plan boards, dated map copies, labeled cache containers, inspection tags, assembly markers, route signs, temporary barriers, NPC movement, companion movement, bells/lights if canon later permits them, and after-action work orders.

Projection must display authoritative state and may lag only when the design explicitly models stale information. Destroying, moving, or duplicating a visual object cannot alter authority unless the relevant world verb validates the action and writes server state.

## Canon boundary

This layer creates no Marea emergency hierarchy, alarm vocabulary, shelter, disaster history, formal rescue service, medical doctrine, or Caelo law. All location-specific examples remain proposals until promoted.