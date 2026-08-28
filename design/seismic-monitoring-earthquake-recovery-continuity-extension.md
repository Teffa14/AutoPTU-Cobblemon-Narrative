# Ouros Seismic Monitoring & Earthquake Recovery Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension preserves the operational continuity of seismic observations, earthquake-event records, alerts/advisories, post-event assessment and staged access recovery.

It exists because the repository already knows how to model geology, rescue, repairs, roads, outages, communications and public notices, but did not have one persistent object linking observations of a seismic event to those downstream owner systems.

It does not define earthquake frequency, regional tectonics, prediction, magnitude scales, structural engineering, collapse mechanics or PTU environmental damage.

## Authority boundaries

Geology owns geological context and scientific interpretation of formations and site history.

Science/Research owns research claims and validation workflows.

Crisis/Rescue owns rescue, evacuation, casualty response and emergency coordination.

Facility Maintenance owns repair and technical inspection work on assets.

Roads/Bridges owns route restrictions, detours and reopening.

Infrastructure Outage owns multi-service cascades and restoration dependencies.

Communications/Public Notices own dissemination and receipt of warnings.

Housing, Commerce, Conservation and other domain systems own their downstream consequences.

This extension owns only seismic-event identity, observation provenance, monitoring availability, detection/revision history, alert/advisory handoffs and post-event assessment continuity.

## Seismic event

```yaml
seismic_event:
  event_id: null
  status: PROPOSED
  first_observation_time: null
  observation_ids: []
  detection_record_ids: []
  characterization_revision_ids: []
  affected_area_claim_ids: []
  alert_product_ids: []
  advisory_ids: []
  post_event_assessment_ids: []
  downstream_incident_refs: []
  legacy_event_refs: []
  current_review_state: UNCONFIRMED
  provenance_refs: []
  canon_status: proposed
```

Candidate review states:

- UNCONFIRMED
- DETECTED
- UNDER_REVIEW
- REVIEWED
- REVISED
- ARCHIVED

These states describe the event record. They do not state that a place is safe.

## Seismic observation

```yaml
seismic_observation:
  observation_id: null
  event_id: null
  observer_or_node_id: null
  observed_at_world_time: null
  location_id: null
  observation_kind: null
  qualitative_effect_claims: []
  raw_record_ref: null
  confidence_band: null
  superseded_by_observation_id: null
  provenance_refs: []
```

Candidate observation kinds:

- INSTRUMENT_READING
- HUMAN_FELT_REPORT
- POKEMON_BEHAVIOR_REPORT
- STRUCTURE_EFFECT_REPORT
- GROUND_EFFECT_REPORT
- SERVICE_ANOMALY_REPORT
- UNKNOWN_SOURCE_REPORT

A Pokémon-behavior report remains an observation. It does not grant prediction capability or establish causation.

## Monitoring node

```yaml
seismic_monitoring_node:
  node_id: null
  location_id: null
  operator_actor_ids: []
  method_refs: []
  current_operational_state: UNKNOWN
  communication_path_refs: []
  maintenance_ref_ids: []
  latest_observation_id: null
  outage_ref_ids: []
  provenance_refs: []
```

Candidate operational states:

- OPERATING
- DEGRADED
- OFFLINE
- ACCESS_BLOCKED
- DATA_DELAYED
- STATUS_UNKNOWN

`NODE_OPERATING != REGION_FULLY_OBSERVED`.

An offline node does not prove that no earthquake occurred.

## Detection and revision

```yaml
seismic_detection_record:
  detection_id: null
  event_id: null
  created_at_world_time: null
  source_observation_ids: []
  detection_state: DETECTED
  characterization_claim_ids: []
  reviewer_actor_ids: []
  revision_of_detection_id: null
  provenance_refs: []
```

A later revision may change an estimated event location, scope or interpretation while preserving the earlier record as historically correct for its time.

No narrative generator may invent real-world-style magnitude values unless Ouros canon later establishes a governing measurement system.

## Alert product and handoff

```yaml
seismic_alert_product:
  alert_id: null
  event_id: null
  issuer_actor_or_institution_id: null
  authored_at_world_time: null
  scope_ids: []
  current_state: DRAFTED
  handoff_packet_ids: []
  superseded_by_alert_id: null
  expires_at_world_time: null
  provenance_refs: []
```

Candidate states:

- DRAFTED
- AUTHORIZED
- HANDED_OFF
- SUPERSEDED
- EXPIRED
- CANCELLED

`DETECTED != ALERT_AUTHORIZED`.

`ALERT_AUTHORIZED != HANDED_OFF`.

`HANDED_OFF != DELIVERED`.

`DELIVERED != RECEIVED_BY_EVERY_ACTOR`.

Communications and Public Notices own the actual dissemination and receipt evidence.

## After-event advisory

```yaml
after_event_advisory:
  advisory_id: null
  event_id: null
  authored_at_world_time: null
  valid_from_world_time: null
  valid_until_world_time: null
  uncertainty_band: null
  recommendation_refs: []
  source_observation_ids: []
  supersedes_advisory_id: null
  provenance_refs: []
```

An advisory expresses uncertainty. It never schedules a guaranteed secondary event.

If Ouros canon does not support formal probabilistic forecasting, advisory language should stay qualitative.

## Post-event assessment

```yaml
seismic_post_event_assessment:
  assessment_id: null
  event_id: null
  location_or_asset_id: null
  owner_system_ref: null
  assessment_state: PENDING
  observation_ids: []
  restriction_ref_ids: []
  inspection_ref_ids: []
  reassessment_due_ref: null
  assessed_at_world_time: null
  provenance_refs: []
```

Candidate states:

- PENDING
- ACCESS_BLOCKED
- IN_PROGRESS
- SPECIALIST_REVIEW_REQUIRED
- VERIFIED_FOR_LIMITED_ACCESS
- VERIFIED_FOR_NORMAL_ACCESS
- REASSESSMENT_REQUIRED
- STATUS_UNKNOWN

This record does not perform a building inspection or road reopening. It references the owner system that does.

`SHAKING_ENDED != ASSESSED`.

`ASSESSED != REPAIRED`.

`REPAIRED != VERIFIED`.

`VERIFIED != REOPENED`.

## Event timeline provenance

A single event can legitimately have several important times:

- first report;
- first monitoring-node observation;
- first detection record;
- alert authorization;
- first known receipt;
- end of locally observed shaking;
- start of rescue work;
- first inspection;
- restricted reopening;
- normal reopening.

Do not collapse these into one `earthquake_time` or `recovery_time` when the distinction matters.

## Actor knowledge

```yaml
seismic_event_knowledge:
  actor_id: null
  event_id: null
  known_observation_ids: []
  known_alert_ids: []
  known_advisory_ids: []
  believed_cause_claim_ids: []
  known_restriction_refs: []
  last_updated_world_time: null
  provenance_refs: []
```

An actor can hold an outdated but historically reasonable interpretation.

Rumor systems may preserve unsupported causal claims without promoting them to world truth.

## Pokémon behavior boundary

A wild collective or individual Pokémon may have an authored observation record such as leaving a ridge, refusing a den or changing a route before or after an event.

That fact can seed investigation and folklore.

It cannot establish:

- earthquake prediction;
- seismic detection capability;
- supernatural causation;
- species-wide behavior;
- Trainer ownership;
- tactical bonuses.

Any such rule needs explicit PTU/Caelo and implementation evidence.

## Legacy event memory

```yaml
seismic_legacy_event:
  legacy_id: null
  event_id: null
  changed_route_refs: []
  changed_building_refs: []
  changed_habitat_refs: []
  memorial_or_archive_refs: []
  temporary_asset_refs: []
  policy_change_refs: []
  recurring_actor_refs: []
  later_story_refs: []
```

Recovery should preserve history instead of resetting a location to its pre-event state.

A temporary sensor, alternate path, repaired wall, relocated household or new gathering place can remain narratively important years later.

## Minecraft/Cobblemon boundary

Reusable presentation can include:

- monitoring huts and instruments;
- warning lights or signs when canon supports them;
- cracks and repaired masonry as authored scenery;
- barriers and inspection markers;
- temporary observation posts;
- changed roads and paths;
- NPC crews;
- Pokémon models, forms, poses, animations and cries;
- sound, particles, UI, networking, tracking and persistence hooks.

Minecraft must not decide seismic facts.

A screen shake does not create PTU forced movement.

A falling block does not apply PTU damage.

A cracked block does not prove structural failure.

A redstone signal does not authorize an alert.

A Pokémon moving away from an area does not prove prediction or causation.

Cobblemon battle-state/controller logic does not choose combatants, legality, HP/status, positions or outcomes.

## Encounter A — Monitoring Ridge Withdrawal

Narrative premise:

A monitoring ridge has just experienced a seismic episode. Field staff and nearby Pokémon need a clear withdrawal corridor while another conflict develops near the access path.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL; required for tactical withdrawal/interception and any environmental displacement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for active shaking, unstable ground, falling debris or reaction windows
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for protection/withdrawal behavior
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
- explicit WITHDRAW/PROTECT objective semantics: not verified

REDUCED version:

The active shaking has ended before BattleSpec creation. Staff, equipment and nonparticipants leave the tactical area. Unstable slopes are excluded from the grid. AutoPTU receives a reviewed static clearing with explicit combatants. Victory secures immediate access only. It does not restore monitoring, certify the ridge or predict another event.

## Encounter B — Post-Event Plaza Perimeter

Narrative premise:

A public plaza has already been evacuated and inspected for immediate access, but a conflict now threatens the controlled perimeter while assessment teams work elsewhere.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including forced movement/interception: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if loose debris, structural zones or secondary shaking are mechanically active
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for perimeter/protection objectives
- adapter/playback: BLOCKING

REDUCED version:

Casualty extraction and structural isolation occur first. The battle takes place in a reviewed open part of the plaza with no dynamic debris or collapse. The result can preserve access for inspectors but cannot mark any building repaired, safe or reopened.

## Encounter C — Sensor Vault Diversion

Narrative premise:

An old monitoring vault contains event records needed to reconcile conflicting reports. A conflict occurs outside while specialists attempt to recover access.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including forced movement/interception: PARTIAL when route denial/interception matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL; required for any delayed timed event
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for active equipment hazards, collapse or aftershock zones
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- technical-object protection semantics: not verified

REDUCED version:

The vault and instruments are inert and outside the grid. Combat occurs at the exterior access path. Event records become available only through a separate exploration/records workflow after the encounter. Winning never repairs a sensor or validates its data.

## Permanent capability rule

Mechanically rich seismic scenes must declare every relevant family. Active shaking alone does not justify environmental displacement. A delayed aftershock needs turn/round lifecycle support plus environmental-zone behavior. Falling debris needs a governing hazard/damage contract. Reactions need generalized reaction support. Structural failure needs an authored mechanical object/hazard contract.

Until those exist, preserve the narrative premise with static reviewed battle spaces and world-state consequences outside combat.

## Canon questions

Unresolved:

- which Ouros regions experience notable seismic activity;
- whether any region has formal monitoring networks;
- technologies and observation methods;
- who may issue alerts or advisories;
- how warnings are disseminated;
- whether formal intensity/magnitude systems exist;
- what historical events changed settlements or routes;
- what temporary monitoring sites became permanent;
- whether any individual Pokémon have canon-supported seismic sensing roles;
- privacy and access rules for event/inspection records.

No answer is implied by this extension.