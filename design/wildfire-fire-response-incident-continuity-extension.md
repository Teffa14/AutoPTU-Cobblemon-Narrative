# Wildfire & Fire-Response Incident Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension gives Ouros persistent operational continuity for wildfire and structural/landscape fire incidents without turning Minecraft fire blocks or generic crisis flags into authoritative mechanics.

It owns incident-specific fire observations, sector/perimeter continuity, response assignments, operational attempts, evacuation/access-area references, residual-fire verification, reignition records and post-fire handoffs.

It connects to existing systems rather than replacing them.

## Authority boundaries

`crisis-rescue-recovery-layer.md` owns generic crisis activation, overall emergency lifecycle, shelters, missing persons, staging sites and multi-system recovery orchestration.

Weather/Seasonality owns observed weather and forecasts. This layer may reference wind, humidity, precipitation or visibility observations but never calculates them.

Forestry owns persistent woodland condition, interventions, burned-area forestry review and restoration history.

Conservation owns ecological interpretation, protected-area decisions, wildlife/habitat review and restoration objectives.

Travel/Road/Rail/Port/Aviation owner systems own actual route/service closure and reopening.

Facility Maintenance/Public Works own asset repair, testing and return-to-service.

Worksite Safety owns responder/worker safety restrictions, near misses and corrective action.

Pokémon Work owns individual Pokémon assignments and capability evidence.

Care owns injury/treatment.

Case Authority/Custody owns suspicious-cause investigation and evidence chain of custody.

Public Notices owns issued warnings, signs and distribution history.

This extension owns the persistent operational record connecting fire-specific observations and actions to those systems.

## 1. Fire incident identity

```yaml
fire_incident:
  incident_id: null
  crisis_ref: null
  location_scope_ids: []
  first_report_ids: []
  confirmed_fire_observation_ids: []
  incident_class_claims: []
  current_operational_state: REPORTED
  sector_ids: []
  access_area_refs: []
  response_assignment_ids: []
  suppression_operation_ids: []
  evacuation_refs: []
  route_closure_refs: []
  residual_heat_observation_ids: []
  reignition_event_ids: []
  cause_case_ref: null
  post_fire_handoff_ids: []
  unresolved_questions: []
  provenance_refs: []
  canon_status: proposed
```

A fire incident is an operational history object. It does not create PTU Fire damage, Burn, smoke penalties, tactical Weather or automatic ecological effects.

## 2. Report, observation and confirmation

Smoke, glow, heat, smell, alarm activation and witness testimony are evidence sources.

```yaml
fire_report:
  report_id: null
  source_actor_or_system_id: null
  reported_at: null
  claimed_location: null
  claimed_observation: null
  evidence_refs: []
  verification_state: UNVERIFIED
  linked_incident_candidates: []
```

```yaml
fire_observation:
  observation_id: null
  observer_ids: []
  observed_at: null
  location_ref: null
  observation_method_ref: null
  observed_fire_state_claims: []
  observed_smoke_claims: []
  observed_spread_claims: []
  observed_exposure_claims: []
  evidence_refs: []
  confidence: null
```

Hard rules:

- smoke does not prove one specific fire location;
- one fire may produce reports from multiple settlements;
- two reports may describe the same plume;
- lack of visible flame does not prove extinguishment;
- a Pokémon near an ignition area does not prove causation.

## 3. Cause status

Cause investigation remains separate from response.

```yaml
fire_cause_status:
  incident_id: null
  state: UNKNOWN
  cause_claim_refs: []
  evidence_case_ref: null
  confirmed_cause_ref: null
  updated_at: null
```

Suggested states:

- UNKNOWN
- UNDER_REVIEW
- MULTIPLE_PLAUSIBLE_CAUSES
- CONFIRMED_BY_OWNER_SYSTEM
- UNRESOLVED

The generator must not create an arsonist, negligent actor, wild Pokémon culprit or supernatural cause merely because an incident needs a mystery.

## 4. Incident sectors

Use sectors to preserve operational locality without simulating a continuous cellular automaton.

```yaml
fire_sector:
  sector_id: null
  incident_id: null
  location_refs: []
  observed_condition_refs: []
  current_sector_state: ACTIVE_UNKNOWN_EDGE
  access_restriction_refs: []
  response_assignment_refs: []
  resource_need_refs: []
  last_verified_at: null
  provenance_refs: []
```

Possible authored broad states:

- UNVERIFIED
- ACTIVE_UNKNOWN_EDGE
- ACTIVE_OBSERVED_EDGE
- HOLDING_UNDER_CURRENT_OBSERVATION
- RESIDUAL_HEAT_REVIEW
- PATROL_REVIEW
- NO_ACTIVE_FIRE_OBSERVED
- POST_FIRE_ASSESSMENT

These are Ouros narrative labels, not imported real-world legal/technical definitions.

Do not create numeric spread rate, flame length, heat flux or containment percentage unless a future canonized simulation explicitly owns those measurements.

## 5. Operational state

The overall incident can use broad state transitions:

```text
REPORTED
→ CONFIRMED
→ ACTIVE_RESPONSE
→ SPREAD_HALTED_UNDER_CURRENT_EVIDENCE
→ RESIDUAL_FIRE_OPERATIONS
→ PATROL_OR_VERIFICATION
→ NO_ACTIVE_FIRE_VERIFIED
→ REENTRY_REVIEW
→ POST_FIRE_HANDOFF
→ CLOSED_OPERATIONALLY
```

Transitions require explicit evidence or owner decisions.

Important distinctions:

- forward spread halted does not mean the incident is out;
- no visible flames does not mean residual hot spots are absent;
- operational closure does not reopen roads or facilities;
- reopening does not equal ecological recovery;
- repaired infrastructure does not erase burn history.

## 6. Response assignments

```yaml
fire_response_assignment:
  assignment_id: null
  incident_id: null
  assigned_actor_ids: []
  pokemon_work_assignment_refs: []
  assigned_role: null
  sector_or_location_refs: []
  objective_refs: []
  capability_evidence_refs: []
  equipment_or_resource_refs: []
  start_time: null
  end_time: null
  status: PLANNED
  outcome_observation_refs: []
```

Possible narrative roles include:

- lookout/observation;
- public warning support;
- evacuation support;
- route/perimeter control;
- supply transport;
- water/resource delivery;
- suppression support;
- search support;
- communications;
- post-fire patrol/inspection;
- wildlife relocation support where authorized.

These labels create no PTU action or species capability.

## 7. Drills versus incidents

```yaml
fire_response_drill:
  drill_id: null
  organizer_refs: []
  location_id: null
  scenario_claims: []
  participant_assignment_refs: []
  observed_performance_refs: []
  equipment_readiness_refs: []
  followup_actions: []
  completed_at: null
```

A drill can establish that an actor practiced a role or that equipment was checked. It cannot establish that the same actor will succeed in an actual incident, and it never creates a hidden firefighting stat.

## 8. Operational attempts and verification

```yaml
fire_response_operation:
  operation_id: null
  incident_id: null
  sector_ids: []
  operation_type: authored
  responsible_actor_ids: []
  prerequisites: []
  started_at: null
  completed_at: null
  resource_refs: []
  claimed_action_refs: []
  resulting_observation_ids: []
  verification_state: PENDING
```

Possible operation labels:

- reconnaissance;
- evacuation sweep;
- access closure;
- suppression attempt;
- defensive preparation;
- resource delivery;
- line/perimeter preparation;
- residual-hotspot inspection;
- patrol;
- re-entry assessment.

Completing an operation records that work occurred. Verification decides what state changed.

No operation automatically modifies HP, status, terrain, weather or Pokémon condition.

## 9. Evacuation and access areas

The generic Crisis/Public Notice systems own warnings and evacuation authority. This extension references incident-specific spatial scopes.

```yaml
fire_access_area:
  area_id: null
  incident_id: null
  location_refs: []
  access_state_ref: null
  reason_claim_refs: []
  effective_from: null
  review_condition_refs: []
  notice_refs: []
  route_refs: []
  verified_at: null
```

Possible descriptive access states:

- NORMAL
- RESPONSE_ONLY
- EVACUATION_IN_PROGRESS
- CLOSED_TO_PUBLIC
- ESCORTED_ACCESS_ONLY
- REENTRY_REVIEW
- PARTIAL_REENTRY
- NORMAL_ACCESS_RESTORED

Authority and terminology require regional canon. These states do not imply law by themselves.

## 10. Re-entry

Re-entry is deliberately separate from fire suppression.

Potential prerequisites can reference:

- no-active-fire verification for the relevant area;
- facility inspection;
- road/trail inspection;
- utility state;
- air/smoke observation if canon supports the relevant assessment;
- unstable-tree/structure review;
- public notice update;
- local authority decision.

The absence of flames is insufficient by itself.

## 11. Residual heat and reignition

```yaml
residual_fire_observation:
  observation_id: null
  incident_id: null
  sector_id: null
  observed_at: null
  observer_ids: []
  observation_claims: []
  evidence_refs: []
  verification_state: RECORDED
```

```yaml
reignition_event:
  reignition_id: null
  incident_id: null
  first_report_refs: []
  confirmed_observation_refs: []
  affected_sector_refs: []
  new_response_operation_refs: []
  confirmed_at: null
```

A smoke report during patrol can remain unresolved. The story generator must not force reignition because tension has dropped.

## 12. Resources without suppression arithmetic

A response may need water access, pumps, tools, transport, communications, protective equipment, shelter capacity or trained personnel.

Represent these as resource availability and assignment records through the relevant systems.

Do not calculate:

- liters required per fire cell;
- Move damage converted to suppression power;
- Water-type effectiveness against a world fire;
- Rain Dance radius/duration as wildfire suppression;
- Fire-type immunity to heat;
- arbitrary equipment bonuses.

## 13. Pokémon work boundary

A Pokémon participates in fire response only through an explicit individual assignment with evidence for the exact task.

Potential evidence may eventually include validated:

- Movement Capabilities;
- Power/lifting capacity;
- exact Moves;
- exact Abilities;
- Skills where applicable;
- training history;
- relationship/Command requirements;
- equipment compatibility.

Type and species are insufficient.

A Water-type is not automatically a firefighter. A Fire-type is not automatically heat-safe. A Flying-type is not automatically a smoke lookout. A Psychic-type is not automatically authorized or capable of rescue extraction.

## 14. Wildlife and ecology

Wild Pokémon near an incident remain ordinary actors/collectives.

Possible observed responses:

- departure from one area;
- aggregation near water or clearings;
- use of roads/settlements;
- return after fire;
- altered nesting/foraging observations;
- occupancy of burned or unburned patches.

Conservation/Science owns interpretation.

Do not infer fear, injury, displacement cause, habitat loss, benefit or recovery without evidence.

## 15. Post-fire handoffs

```yaml
post_fire_handoff:
  handoff_id: null
  incident_id: null
  target_owner_system: null
  target_location_or_asset_refs: []
  source_observation_refs: []
  question_or_need_refs: []
  created_at: null
  receiving_record_refs: []
  status: OPEN
```

Potential receiving systems:

- Forestry for burn-scar/stand review;
- Conservation for habitat/ecological assessment;
- Care for treated actors;
- Roads/Travel for access inspection;
- Facility Maintenance/Public Works for assets;
- Geology for erosion/slope questions;
- Water Management for catchment/reservoir consequences;
- Material Culture for documented recovered material/evidence;
- Public Memory for later remembrance;
- Science for causal/environmental studies.

One incident can create several handoffs with different completion times.

## 16. Temporary fire-response infrastructure

Temporary state can outlive the active response:

- staging area;
- cleared access strip;
- temporary barrier;
- water point;
- observation post;
- supply cache;
- temporary shelter;
- rerouted trail/road access.

After incident closure, owner systems decide whether each disappears, remains, changes use or creates a restoration problem.

This gives the world visible history instead of instant reset.

## 17. Information and public memory

Preserve separate records for:

- first report;
- verified operational picture;
- public warning/advisory;
- later cause finding;
- responder report;
- resident testimony;
- scientific/ecological interpretation;
- later memorial narrative.

A later official account must not silently rewrite what actors knew at the time.

## 18. PTU/Caelo mechanical boundary

Current project evidence supports named PTU mechanics such as Burn, Fire-type attacks, Weather and individual Move/Ability effects. It does not establish a universal mapping from world fire to those mechanics.

This extension therefore does not define:

- environmental fire damage;
- smoke Accuracy or LoS modifiers;
- automatic Burn zones;
- ash/ember statuses;
- heat exhaustion;
- oxygen/smoke inhalation;
- tactical spreading flames;
- dynamic fire-front movement;
- wind-driven forced movement;
- collapse/falling-tree damage;
- water suppression formulas;
- firefighting Skill checks;
- universal rescue/carry actions;
- Pokémon job capability by Type/species.

Any mechanically rich encounter must declare the exact permanent capability families it needs and use a reduced version until those families are verified.

## 19. Minecraft/Cobblemon boundary

Strong reuse candidates:

- ordinary blocks/buildings/forest geometry;
- fire/smoke/ash-like particles and visual effects where safe and performant;
- barriers, signs, lights and temporary camps;
- day/night and weather presentation;
- Pokémon entities, models, forms, poses, animations and cries;
- NPC/entity positioning for already-authorized evacuations;
- UI, maps, notice boards and incident logs;
- networking, tracking and persistence hooks;
- controlled reversible block variants representing already-authorized world-state change.

Adapter-required surfaces:

- binding incident/sector/access-area IDs to reviewed world geometry;
- converting approved safe geometry into AutoPTU cells;
- projecting authoritative closures into barriers/signage;
- keeping persistent actor IDs stable across unload/reload;
- rendering authoritative AutoPTU battle events without battle-state authority leaking to Cobblemon;
- reconciling visible fire effects with incident state so particles never become source-of-truth.

Forbidden authority:

- Minecraft fire spread deciding Ouros incident spread;
- Minecraft fire ticks deciding PTU damage or Burn;
- water blocks extinguishing an Ouros incident by themselves;
- redstone deciding suppression success;
- nearby Pokémon becoming responders or combatants automatically;
- Cobblemon BattleState deciding participants, HP, statuses, positions, legality or result;
- client visuals deciding reopening or ecological recovery.

Required direction:

`Ouros fire/crisis world state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## 20. Encounter A — Ridge Fireline Withdrawal

Narrative premise:

A response crew has already withdrawn from an exposed sector, but one stable approach remains contested by wild Pokémon or another explicitly authored threat while the incident continues outside the tactical area.

Full intended version:

- multiple withdrawal/clear-route paths;
- live restricted sectors;
- Intercept and forced movement where legal;
- smoke/fire/heat zones only if exact PTU/Caelo rules exist;
- changing weather only through verified battlefield Weather handoff;
- objective-aware AI valuing exit, route denial or territorial retreat;
- authoritative adapter playback.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:

The crew and all ordinary civilians leave before combat. Ouros closes the active fire sector in world state. The encounter occurs in a reviewed static clearing/road approach with no flame, smoke, ember, heat, weather or collapse mechanics. AutoPTU receives explicit combatants only. Victory can secure the immediate approach; it cannot contain the fire, reopen the route or complete re-entry review.

## 21. Encounter B — Evacuation Junction Perimeter

Narrative premise:

An evacuation route junction must remain clear after evacuees have already passed. A distinct authored conflict threatens the access point while the fire itself remains outside the arena.

Full intended version:

- CLEAR_ROUTE/WITHDRAW/PROTECT-like objective semantics;
- competing movement/reactions;
- route-control positioning;
- possible changing access zones;
- objective-aware AI;
- complete playback.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic zones/reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:

Evacuees have completed movement before battle. The junction becomes a static legal arena. Road/fire closures remain world-state objects outside combat. No NPC escort, moving fire front or live vehicle interaction occurs. Battle outcome may allow responders to resume access-control work afterward, subject to owner-system verification.

## 22. Encounter C — Mop-Up Patrol Contact

Narrative premise:

During residual-fire patrol, responders encounter an independently motivated Pokémon group or other authored threat near a sector where active suppression has paused.

Full intended version:

- residual heat/smoke zones if verified;
- restricted-area reactions;
- withdrawal/territorial objectives;
- exact Move/Ability interactions with any validated fire environment;
- tactical AI and adapter playback.

Capability profile:

The same permanent map applies, with `terrain/weather/hazards/zones/reactions`, `AI tactical policy` and adapter/playback currently BLOCKING, while movement/lifecycle/damage/status/content families remain PARTIAL.

Reduced version:

The patrol exits the residual-hotspot area first. The tactical scene occurs on a verified cold/stable perimeter. The incident record remains in residual-fire review regardless of battle outcome. Winning cannot certify that hot spots are gone.

## 23. Noncombat investigation — Four Smoke Reports, Two Fires

Premise:

Four reports arrive from different locations over several hours. The map initially appears to show four incidents.

Playable evidence:

- report times;
- observer positions;
- sight lines/terrain claims;
- weather observations;
- photographs or sketches;
- responder verification;
- sector records;
- later patrol observations.

Possible outcomes:

- two reports saw the same plume from opposite valleys;
- one report was old smoke after spread had halted;
- one report described a separate small incident;
- evidence remains insufficient to reconcile all four.

No culprit or hidden single answer is required.

## 24. Noncombat investigation — The Reignition That Might Not Be

A patrol reports smoke from a sector previously assessed as having no active fire.

Potential explanations include:

- confirmed residual/reignited fire;
- smoke transported from another sector;
- dust/steam or another visible phenomenon;
- report location mismatch;
- observation timing mismatch;
- insufficient evidence.

The system records the report first and changes incident state only after verification.

## 25. Long-form arc — A Ridge Learns Its Firebreaks

Phase 1 establishes ordinary forest routes, nearby settlement routines, response drills and known access points.

Phase 2 begins with smoke reports whose scope is initially uncertain.

Phase 3 creates targeted closure/evacuation actions while responders verify sectors.

Phase 4 records one or more suppression/resource operations. Progress can be partial and differently timed by sector.

Phase 5 moves into residual-fire patrol and re-entry review while some routes/facilities remain closed.

Phase 6 sends post-fire questions to Forestry, Conservation, Travel, Public Works and Science.

Phase 7 returns months later. A temporary cleared strip may have become a familiar footpath, an erosion concern, habitat edge, emergency access route or restoration site. A resident may remember an old warning. A Pokémon group may use the burn mosaic differently. A repaired route may follow a changed alignment.

The ridge accumulates history. There is no abstract `fire_response_level`.

## 26. Generator rules

A fire incident candidate requires an authored or observed source signal. Do not spawn a fire solely because the region has been quiet.

Every generated incident should retain:

- initial evidence;
- uncertainty;
- affected place references;
- current operational state;
- who has authority to act;
- current access consequences;
- unresolved needs;
- exact source of any tactical premise;
- required capability categories;
- reduced fallback when rich mechanics are unavailable.

Do not silently assign blame. Do not require combat. Do not reopen an area because the dramatic scene ended.

## 27. Canon questions preserved

This extension intentionally leaves unresolved:

- which Ouros regions experience wildland fire and at what cadence;
- whether fire is a normal ecological process in any biome;
- response institutions and their mandates;
- warning/evacuation terminology and authority;
- firefighting technologies;
- water/resource infrastructure;
- role of Rangers or analogous organizations;
- whether and how Pokémon are trained for response work;
- investigation authority for suspicious causes;
- re-entry standards;
- cultural practices surrounding burns/firebreaks/prescribed fire;
- any prescribed-burning institution or rules.

Those require canon approval and, where mechanical, PTU/Caelo/AutoPTU validation.