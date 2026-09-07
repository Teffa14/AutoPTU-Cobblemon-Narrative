# Survey control, mark recovery & spatial-decision contract — Pass 326

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-07
Canon effect: NONE

## Purpose

This contract defines a reusable world-state structure for survey marks, reference points, map revisions and spatial decisions where the physical reference, its recorded location, its current condition and institutional interpretation may diverge.

It is intended for persistent NPC/world-agent use and must remain separate from PTU tactical authority and Minecraft presentation.

## Core invariants

`MARK_IDENTITY != MARK_POSITION_RELIABILITY`

`MARK_RECOVERED != MARK_AUTHENTICATED`

`MARK_AUTHENTICATED != MARK_STABLE`

`HISTORICAL_RECORD != CURRENT_PHYSICAL_STATE`

`MAP_REVISION != WORLD_TRUTH`

`SPATIAL_DECISION != PERMANENT_CANONICAL_CERTAINTY`

## World-state objects

```yaml
survey_control_feature:
  feature_id: null
  feature_type: null
  physical_location_ref: null
  designation_claim_ids: []
  installation_event_id: null
  reference_relationship_ids: []
  condition_observation_ids: []
  recovery_event_ids: []
  status: UNKNOWN
```

Candidate feature types may include primary control mark, reference mark, natural landmark, built landmark, route reference, elevation reference or temporary field control. These logical types do not establish Ouros technology or law.

```yaml
survey_recovery_event:
  recovery_id: null
  feature_id: null
  observer_ids: []
  observed_at: null
  description_match_claim_ids: []
  condition_claim_ids: []
  photo_or_record_refs: []
  identity_assessment: UNRESOLVED
  stability_assessment: UNRESOLVED
  provenance_root_ids: []
```

```yaml
reference_relationship:
  relationship_id: null
  source_feature_id: null
  target_feature_id: null
  relationship_kind: null
  historical_record_id: null
  current_observation_id: null
  confidence_band: null
```

The contract stores authored relationships and observations. It does not run real-world geodesy.

## Spatial claim lineage

A map, maintenance plan or boundary interpretation must point to the evidence used at the time.

```yaml
spatial_claim:
  spatial_claim_id: null
  subject_feature_ids: []
  claim_kind: null
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  created_by_actor_or_institution_id: null
  created_at: null
  confidence_band: null
  supersedes_claim_id: null
  status: ACTIVE
```

Supersession preserves history. It does not mutate old reports.

## Actor knowledge boundary

NPCs may know:
- a direct recovery observation they made;
- a report delivered to them;
- an archive record they explicitly consulted;
- a public revision they actually received;
- a conclusion produced by their own authorized work.

They do not know:
- current hidden feature state merely because the server stores it;
- every recovery made by their institution;
- later corrections they never received;
- the true reason a marker moved unless supported by evidence available to them.

Archive lookup remains external evidence and must not rewrite private memory.

## Institutional decision boundary

A spatial decision consumes evidence and authority.

```yaml
spatial_decision:
  decision_id: null
  decision_type: null
  authority_actor_or_institution_id: null
  evidence_ids: []
  affected_feature_ids: []
  issued_at: null
  review_at: null
  state: ACTIVE
  supersedes_decision_id: null
```

Candidate decisions:
- OPEN_ROUTE_SEGMENT
- RESTRICT_WORK_AREA
- REQUIRE_REOBSERVATION
- TEMPORARY_ALIGNMENT
- REPLACE_OR_REESTABLISH_CONTROL
- PUBLISH_MAP_REVISION
- HOLD_DECISION_PENDING_EVIDENCE

These labels are narrative workflow states, not legal powers. Actual authority remains canon content.

## Consequence scoping

A decision affects only authored dependencies.

A disputed control point may block one construction cut while leaving a nearby road open. A corrected map may alter a work route without changing property ownership. A replacement marker may improve future surveying without erasing why the original decision was made.

Use existing decision-dependency and selective-consequence-repair patterns where available.

## Information propagation integration

Recovery reports and map revisions flow through the existing global NPC information architecture.

Expected path:

`observation -> authored report/claim -> explicit recipient resolution -> channel scheduling -> delivery -> receiver knowledge -> optional replan`

Publication never implies receipt. Faction membership never implies shared knowledge. A correction is a new event with its own audience.

## Travel integration

Route geometry and route knowledge remain separate.

A new spatial decision may:
- open or close one route edge;
- create a maintenance-only edge;
- change a waypoint used by future route planning;
- trigger work or inspection obligations.

The travel planner must consume authoritative route state, not Minecraft marker placement.

## AutoPTU boundary

Most survey-control gameplay requires no battle mechanics.

If a scene escalates into structured combat, the world system must issue the normal explicit AutoPTU handoff. Survey observations, map interpretations and institutional decisions remain outside AutoPTU unless an exact tactical contract says otherwise.

Reduced encounters should use static geometry and already verified ordinary combat families.

Rich encounter additions must declare exact dependencies:
- specialized visibility/fog: targeting/LoS extension beyond ordinary VERIFIED contracts;
- climbing, special traversal or uncertain ledges: base movement only when exact legality is verified;
- shove/fall/rescue/interception: complete movement, currently PARTIAL;
- timed inspection/weather/work phases: full turn/round lifecycle, currently PARTIAL;
- environmental/falling damage: full stateful damage pipeline, currently PARTIAL;
- persistent mechanical conditions: status lifecycle, currently PARTIAL;
- wind, unstable ground, debris, hazard boundaries or reactions: terrain/weather/hazards/zones/reactions, currently MIXED/PARTIAL/BLOCKING;
- each Move: move-specific behavior, individually gated;
- each Ability: abilities, individually gated;
- mechanical survey equipment: items, individually gated;
- specialist Feature effects: Trainer Features/perks, individually gated;
- ordinary supported tactical action enumeration: AI legal-action infrastructure, VERIFIED within audited contracts;
- escort/protect/objective tactics: AI tactical policy, BLOCKING for general autonomous rich-objective reasoning;
- dynamic visual/state synchronization: Minecraft/Cobblemon/Craftics adapter/playback, PARTIAL/BLOCKING end-to-end.

## Minecraft/Cobblemon boundary

Minecraft may display:
- a marker model;
- survey stakes;
- changed fences or walls;
- work closures;
- map interfaces;
- field notebooks;
- crews visiting locations.

Visual placement cannot author:
- authoritative coordinates;
- mark authenticity;
- stability;
- route legality;
- institutional authority;
- NPC knowledge;
- PTU movement or hazard rules.

## PTU/Caelo guardrail

The narrative source inventory observed during Pass 326 exposes `sources/kairos` and no adopted `sources/caelo` directory. The repository README requires exact validation for navigation checks, movement capabilities, Trainer Feature effects, device bonuses and environmental mechanics.

Do not invent:
- Survival/Education/Technology DCs;
- navigation or survey bonuses;
- Topographer/Researcher/Survivalist effects;
- climbing or fall rules;
- weather penalties;
- Pokémon sensing privileges;
- communication-device effects;
- battle utility for survey tools.

## Reduced implementation packet

A minimum playable version needs only:
- persistent feature IDs;
- authored historical records;
- recovery observations with provenance;
- explicit NPC receipt;
- spatial claim lineage;
- feature-scoped decisions;
- route-state consequences;
- optional static AutoPTU encounter;
- visible Minecraft markers as presentation.

No new tactical rule is required.

## Promotion gate

Before a specific survey dispute becomes canon, resolve:
- region and place;
- responsible institution;
- technology and recordkeeping level;
- what the original control was used for;
- current land/route authority;
- exact historical evidence;
- actual cause of discrepancy;
- downstream consequences;
- whether any PTU mechanic is required;
- whether the reduced version is sufficient.
