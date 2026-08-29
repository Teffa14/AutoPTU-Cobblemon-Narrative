# Severe Wind, Windthrow, Debris & Impact Recovery Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension gives Ouros persistent continuity for the aftermath and operational consequences of damaging wind without turning generic world weather into PTU tactical Weather.

It exists between weather observation and the many owner systems that must deal with what the wind may have changed.

It owns:

- wind-impact episode identity;
- impact reports and verification state;
- spatial impact scopes;
- source/causal hypotheses for observed damage;
- wind-displaced object observations;
- windthrow/fallen-vegetation observations as incident evidence;
- residual-condition records after the strongest wind passes;
- evidence-preserving references when cleanup changes the scene;
- cross-owner handoffs;
- incident-level recovery coordination and closure history.

It does not own:

- weather forecasts or meteorological truth;
- generic crisis command;
- route closure/reopening;
- electrical isolation/restoration;
- structural safety decisions;
- forestry diagnosis/removal;
- park closure/reopening;
- facility repair;
- construction/reconstruction;
- ecological interpretation;
- Pokémon custody or relocation;
- PTU tactical Weather, wind push or environmental damage.

## Authority boundaries

`weather-forecast-preparedness-operational-extension.md` owns weather observations, forecasts, forecast revision and weather notices.

`crisis-rescue-recovery-layer.md` owns generic crisis lifecycle, evacuation, shelter, staging, search and multi-system recovery orchestration.

`roads-bridges-detours-operational-continuity-extension.md`, Rail, Aviation, Port, Ropeway and Travel owners decide actual route/service availability.

`electric-grid-generation-distribution-continuity-extension.md` owns electrical asset state, outage, isolation, repair and restoration.

`building-safety-occupancy-reentry-assessment-continuity-extension.md` owns technical assessment, restriction, occupancy/use authorization and reentry.

`forestry-managed-woodland-harvest-restoration-extension.md` owns woodland management and persistent tree/stand interventions.

`public-space-parks-commons-continuity-extension.md` owns park/common operating state.

`facility-maintenance-repair-inspection-extension.md` owns faults, repairs and verification for existing facilities.

`construction-renovation-project-handover-continuity-extension.md` owns construction/reconstruction scope and handover.

`settlement-wild-pokemon-coexistence-response-continuity-extension.md`, Ecology and Conservation own Pokémon/wildlife interpretation and management.

`pokemon-agency-partnership-release-layer.md` owns persistent individual Pokémon identity, partnership and custody facts.

This extension may reference all of those states. It cannot manufacture them.

## 1. Wind-impact episode

```yaml
wind_impact_episode:
  episode_id: null
  crisis_ref: null
  weather_observation_refs: []
  forecast_refs: []
  first_report_refs: []
  temporal_window_claims: []
  broad_spatial_scope_refs: []
  impact_scope_ids: []
  current_operational_state: REPORTED
  impact_report_ids: []
  verified_impact_ids: []
  displaced_object_ids: []
  vegetation_impact_ids: []
  owner_handoff_ids: []
  residual_condition_ids: []
  cleanup_evidence_refs: []
  unresolved_questions: []
  closure_record_id: null
  provenance_refs: []
  canon_status: proposed
```

An episode is an operational continuity object.

It does not imply a tornado, hurricane, cyclone, downburst or any other specific meteorological classification unless a canonized Weather owner establishes that classification.

Suggested broad operational states:

- REPORTED
- WEATHER_EVENT_LINK_UNDER_REVIEW
- ACTIVE_IMPACT_WINDOW
- ACCESS_LIMITED
- IMPACT_ASSESSMENT_ACTIVE
- OWNER_HANDOFFS_ACTIVE
- RESIDUAL_CONDITIONS_ACTIVE
- RECOVERY_COORDINATION
- INCIDENT_LEVEL_REVIEW
- CLOSED_OPERATIONALLY

These labels have no automatic legal or mechanical effect.

## 2. Report versus verified impact

```yaml
wind_impact_report:
  report_id: null
  reported_at: null
  reporter_ref: null
  claimed_location_ref: null
  claimed_impact_type: null
  claimed_subject_ref: null
  claimed_wind_link: null
  evidence_refs: []
  verification_state: UNVERIFIED
  duplicate_or_related_report_refs: []
  owner_candidates: []
  privacy_or_access_refs: []
```

Possible descriptive claims:

- tree or limb down;
- loose material displaced;
- sign or fixture damaged;
- roadway obstructed;
- trail obstructed;
- line/pole down;
- roof/façade/window damage reported;
- temporary structure displaced;
- vessel/vehicle/equipment displaced;
- wild Pokémon observed in unusual location;
- access unsafe or uncertain;
- unknown debris present.

A claim remains a claim until verified within its scope.

Hard boundaries:

`REPORT_RECEIVED != IMPACT_VERIFIED`

`MULTIPLE_REPORTS != MULTIPLE_DISTINCT_IMPACTS`

`VISIBLE_DAMAGE != WIND_CAUSE_CONFIRMED`

`WIND_OCCURRED_NEARBY != WIND_CAUSED_THIS_DAMAGE`

## 3. Impact scope

Wind episodes can be broad while meaningful impacts are spatially narrow.

```yaml
wind_impact_scope:
  scope_id: null
  episode_id: null
  scope_geometry_ref: null
  location_refs: []
  assessment_state: NOT_ASSESSED
  access_state_ref: null
  verified_impact_refs: []
  unresolved_report_refs: []
  owner_handoff_refs: []
  residual_condition_refs: []
  last_observed_at: null
  next_review_trigger_refs: []
  provenance_refs: []
```

Suggested assessment states:

- NOT_ASSESSED
- ACCESS_DEFERRED
- PARTIALLY_ASSESSED
- ASSESSED_WITH_GAPS
- ASSESSED_FOR_CURRENT_PURPOSE
- REASSESSMENT_REQUIRED
- INCIDENT_SCOPE_COMPLETE

`ASSESSED_FOR_CURRENT_PURPOSE` must always specify the purpose.

A street walked by a survey team is not proof that roofs, interiors, utility systems or adjacent private land were assessed.

## 4. Verified impact record

```yaml
verified_wind_impact:
  impact_id: null
  episode_id: null
  scope_id: null
  subject_type: null
  subject_ref: null
  observed_condition: null
  observed_at: null
  observer_refs: []
  evidence_refs: []
  immediate_access_consequence_ref: null
  cause_hypothesis_ids: []
  owner_handoff_ids: []
  superseded_or_revised_by: null
  provenance_refs: []
```

The observed condition should remain literal.

Good:

- mature tree lying across road surface;
- detached roof panel found in courtyard;
- signpost leaning after event;
- overhead line observed on ground;
- three upper-floor windows broken;
- fence section displaced from prior photographed position.

Avoid premature interpretation:

- dangerous tree caused by storm;
- tornado debris;
- unsafe building;
- live power line;
- malicious Pokémon damage.

Those require owner evidence.

## 5. Damage/source hypotheses

A key purpose of this extension is to preserve uncertainty.

```yaml
wind_impact_cause_hypothesis:
  hypothesis_id: null
  impact_id: null
  proposed_source_type: null
  proposed_source_ref: null
  proposed_chain: []
  supporting_evidence_refs: []
  conflicting_evidence_refs: []
  confidence_band: UNKNOWN
  owner_interpretation_ref: null
  state: OPEN
```

Candidate descriptive states:

- OPEN
- PLAUSIBLE
- COMPETING
- WEAKENED
- REJECTED
- CONFIRMED_BY_OWNER
- UNRESOLVED

Potential contributors can include only facts established by appropriate owners:

- observed strong wind;
- prior tree condition;
- saturated soil state;
- prior structural damage;
- loose unsecured object;
- collision/impact;
- earlier maintenance fault;
- concurrent construction;
- another hazard.

The generator must not force a single cause where evidence supports several contributors.

## 6. Wind-displaced objects

```yaml
wind_displaced_object_observation:
  observation_id: null
  episode_id: null
  object_description: null
  current_location_ref: null
  prior_location_claim_refs: []
  identity_state: UNKNOWN_OBJECT
  custody_owner_ref: null
  hazard_claim_refs: []
  evidence_refs: []
  found_at: null
  owner_handoff_refs: []
```

Possible identity states:

- UNKNOWN_OBJECT
- OBJECT_CLASS_IDENTIFIED
- UNIQUE_OBJECT_IDENTIFIED
- ORIGIN_CANDIDATE
- ORIGIN_CONFIRMED_BY_OWNER

A roof panel found three blocks away should not automatically be assigned to the nearest damaged roof.

A sign, awning, crate, temporary barrier or personal object can become a provenance puzzle after relocation.

If ownership/custody matters, use Found Property, Logistics, Construction or another appropriate owner.

## 7. Vegetation impact and windthrow

```yaml
wind_vegetation_impact_observation:
  observation_id: null
  episode_id: null
  location_ref: null
  plant_or_tree_ref: null
  observed_state: null
  prior_condition_refs: []
  obstruction_refs: []
  damage_to_other_asset_refs: []
  forestry_or_public_space_handoff_ref: null
  evidence_refs: []
```

Observed states can remain descriptive:

- uprooted;
- trunk failed;
- major limb down;
- canopy damage observed;
- leaning changed from previous record;
- debris field present;
- prior state unknown.

Do not infer:

- health before the event;
- disease;
- wind threshold;
- structural risk of remaining trees;
- removal authority;
- ecological significance.

Those conclusions belong to Forestry, Public Space, Conservation or a future governing system.

## 8. Cleanup versus evidence preservation

Cleanup may begin before a full incident review.

```yaml
wind_cleanup_evidence_record:
  record_id: null
  episode_id: null
  impact_ref: null
  pre_change_evidence_refs: []
  cleanup_or_clearance_owner_ref: null
  work_started_at: null
  work_completed_at: null
  physical_scene_changed: true
  remaining_evidence_refs: []
  unresolved_questions: []
```

This record does not authorize cleanup.

It preserves the fact that another owner changed the scene for operational reasons.

Useful chronology:

```text
07:20 branch reported across route
07:31 photograph logged
07:45 Road owner begins emergency clearance
08:05 branch removed from carriageway
10:20 Forestry receives condition inquiry
13:00 later survey cannot inspect original resting position
```

The world should retain both the original observation and later cleared state.

## 9. Owner handoff

```yaml
wind_impact_handoff:
  handoff_id: null
  episode_id: null
  impact_ref: null
  receiving_owner_system: null
  question_or_need: null
  evidence_packet_refs: []
  sent_at: null
  acknowledgement_ref: null
  owner_case_or_work_ref: null
  resulting_state_ref: null
  status: SENT
```

Candidate owner questions:

Road:
- is the route obstructed;
- is inspection required;
- what state can be restored?

Grid:
- what is the electrical condition;
- is isolation required;
- what repair/restoration record applies?

Building Safety:
- what scope requires assessment;
- is use restriction required;
- can reentry be authorized?

Forestry/Public Space:
- what is the condition of remaining vegetation;
- what intervention is appropriate;
- can the area reopen?

Maintenance:
- what facility component failed;
- what repair and verification are required?

Ecology/Coexistence:
- is unusual Pokémon presence consistent with displacement;
- what evidence exists about recurrence or welfare?

The wind layer never answers those owner questions itself.

## 10. Residual conditions

The end of damaging wind does not equal incident closure.

```yaml
wind_residual_condition:
  residual_id: null
  episode_id: null
  scope_ref: null
  condition_type: null
  observed_at: null
  evidence_refs: []
  owner_system_ref: null
  current_state: OPEN
  review_trigger_refs: []
  resolution_ref: null
```

Potential descriptive conditions:

- debris remains;
- vegetation obstruction remains;
- hanging/loose object reported;
- asset assessment pending;
- route inspection pending;
- utility status unresolved;
- temporary access route active;
- displaced Pokémon report unresolved;
- signage missing;
- public-space review pending;
- evidence gap remains after cleanup.

These labels create no tactical hazard by themselves.

## 11. Incident-level closure

```yaml
wind_impact_closure_record:
  closure_id: null
  episode_id: null
  closed_at: null
  closed_scope_refs: []
  unresolved_owner_case_refs: []
  durable_change_refs: []
  public_memory_refs: []
  lessons_or_review_refs: []
  closure_basis_refs: []
```

Incident-level closure means the specialized coordination object no longer needs active handling.

It does not require every downstream consequence to be complete.

A building repair, forestry restoration, household displacement case or business closure can continue long afterward.

Hard boundary:

`WIND_EPISODE_CLOSED != EVERY_OWNER_RECOVERED`

## 12. Time and revision history

Every impact record should be timestamped.

An early map and a later map can both be correct relative to evidence available at each time.

Use revision edges rather than silent mutation:

```yaml
impact_scope_revision:
  revision_id: null
  prior_scope_ref: null
  replacement_scope_ref: null
  changed_dimensions: []
  new_evidence_refs: []
  revised_at: null
  author_or_owner_ref: null
```

This supports fair questions:

- why was one street absent from the 08:00 map?
- was the object removed before the survey arrived?
- did the Grid owner know about the tree before the line fault?
- did a shelter open because of wind damage or because another crisis state already existed?
- was a wild Pokémon observed before or after the park reopened?

## 13. Worldbuilding uses

### Daily life before an incident

Wind should exist first as normal place identity.

Examples:

- ridge paths with local timing customs;
- sheltered courtyards;
- wind-powered infrastructure where canon supports it;
- market stalls designed for normal breezes;
- trees shaped by habitual exposure;
- Pokémon routines associated with ordinary updrafts or sheltered edges;
- old buildings whose doors or awnings are secured in locally familiar ways.

This prevents every windy day from becoming a crisis.

### During a limited event

Useful story beats:

- a forecast changes after an outdoor event has already begun packing up;
- one exposed street receives damage while a nearby sheltered lane remains intact;
- a tree blocks a service road but does not damage the facility behind it;
- several objects are found displaced and one origin remains uncertain;
- a Pokémon population appears in an unfamiliar courtyard after the event;
- a line-down report creates a Grid handoff while road access remains a separate question.

### Recovery

Recovery can happen on independent clocks:

- Road clears access;
- Grid isolates then repairs;
- Building Safety assesses one façade;
- Maintenance replaces a fixture;
- Forestry reviews remaining trees;
- Public Space reopens one section;
- Coexistence follows up on displaced Pokémon;
- residents keep using a temporary path even after the original route returns.

## 14. Quest hooks

Candidate hooks remain NON-CANON until authored into a region.

- verify three apparently duplicate obstruction reports before crews are sent twice;
- recover pre-cleanup photographs from residents after the scene changed;
- identify the origin of a displaced object without assuming theft;
- carry an evidence packet between owners after communications are degraded;
- compare two impact maps produced at different times;
- escort an assessor only after active wind has ended and a route owner has approved access;
- investigate why the same corner repeatedly accumulates displaced material during moderate events;
- follow a post-storm Pokémon movement report without assuming capture is the solution;
- document which temporary path became the neighborhood's preferred route.

## 15. Mystery grammar

Wind aftermath is well suited to provenance mysteries.

Good mystery questions:

- Did the object come from the damaged building everyone assumes?
- Was the tree already compromised?
- Were two obstruction reports actually the same fallen limb seen from opposite sides?
- Did the route reopen before the public notice was updated?
- Was the Pokémon population displaced by the storm, or was it already using the area at night?
- Why does an old photograph show the sign on a different corner?

Avoid defaulting to:

- sabotage;
- negligence;
- supernatural weather;
- villain-caused storm;
- Pokémon culpability;
- institutional conspiracy.

Those can exist only when evidence and authored canon support them.

## 16. Faction and NPC roles

These are role archetypes, not canon institutions.

### The First Mapper

Builds the first practical impact map from incomplete reports. Their early map should remain queryable rather than retroactively corrected.

### The Route Operator Who Cleared Too Soon for the Survey

Made a legitimate operational choice that changed the evidence landscape. This creates tension without requiring wrongdoing.

### The Resident With Before-Photos

Possesses mundane evidence that becomes valuable only later.

### The Forestry Specialist Who Refuses the Easy Cause

Distinguishes observed failure from a conclusion about why the tree failed.

### The Shopkeeper Using the Temporary Door

A short-term access change becomes habitual and may persist after recovery.

### The Pokémon Watcher

Knows local individual or group routines well enough to notice that a post-event sighting is unusual, while still lacking authority to infer cause.

## 17. Long-term arc: A Ridge Learns Which Side Takes the Wind

Status: NON-CANON ARC CANDIDATE.

Phase 1 establishes ordinary wind as part of local life rather than danger. Residents know sheltered streets, exposed corners and common Pokémon routines.

Phase 2 introduces a forecast with uncertainty. Different owner systems make ordinary preparedness decisions.

Phase 3 brings a limited damaging-wind episode. Impacts are uneven: a few trees fall, one route is obstructed, a facility loses a fixture, a grid fault occurs and displaced material appears elsewhere.

Phase 4 focuses on evidence and handoffs. Some apparent duplicate reports collapse into one impact. One object has an unexpected origin. One tree's pre-event condition complicates the simple storm explanation.

Phase 5 shows staggered recovery. Routes, power, buildings and parks return on different clocks. A temporary walking path becomes popular.

Phase 6 revisits the district months later. New securing practices, changed tree cover, altered Pokémon routines and the retained path show that recovery changed the place.

The arc can recur years later without repeating the same disaster. Historical records provide baseline evidence for a later event.

## 18. Encounter concept: Assessment Team Withdrawal

### Narrative premise

An assessment team is already on an approved post-event route after the strongest wind has passed. New observed conditions make the team withdraw from one scope while an independent hostile encounter threatens the retreat path.

The battle does not assess the site.

### Intended full version dependencies

- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL, needed for active escort, Intercept and wind displacement if represented;
- core calculations — VERIFIED baseline;
- action economy/initiative — VERIFIED baseline;
- full turn/round lifecycle — PARTIAL, needed for staged withdrawal windows;
- full stateful damage pipeline — PARTIAL if ordinary attacks occur;
- status lifecycle — PARTIAL if ordinary statuses occur;
- terrain/weather/hazards/zones/reactions — BLOCKING for active wind, flying-debris cells, protected lanes or generalized reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for WITHDRAW/PROTECT/CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic projection.

Full version status: BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

Ouros first ends or pauses active field assessment and moves assessors, records and equipment outside BattleSpec through world state.

The independent hostile encounter then occurs on a static, already-inspected access area with explicit combatants.

No live wind push, flying debris, collapsing objects or protected-civilian reactions are represented.

Victory can secure immediate access only.

After combat, the owner decides whether assessment can resume.

## 19. Encounter concept: Debris-Origin Chokepoint

### Narrative premise

A displaced object important to an investigation has already been documented and moved to safe custody. An independent battle occurs at the route chokepoint investigators need to traverse to continue tracing its origin.

### Intended full version dependencies

Rich form would need controlled-object custody on-grid, Intercept, forced movement, debris hazards, reaction windows, tactical protection policy and semantic playback.

Those dependencies cross PARTIAL and BLOCKING families.

Full version status: BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

The evidence object remains outside BattleSpec in existing custody state.

Investigators and noncombatants withdraw first.

AutoPTU receives static geometry and explicit combatants.

Victory only clears the immediate chokepoint. It does not identify the object, prove its origin or validate a cause hypothesis.

## 20. Encounter concept: Displaced Pokémon Perimeter

### Narrative premise

After a wind episode, wild Pokémon are observed in a settlement-edge area. Coexistence/Ecology has not yet established whether they were displaced by the storm. A separate threat makes the observation perimeter unsafe.

### Intended full version dependencies

Rich form could require:

- moving noncombatants;
- Intercept/protection;
- multiple reaction windows;
- active wind or changing environmental cells;
- objective-aware AI;
- semantic distinction between observed wild Pokémon and actual battle participants.

Full version status: BLOCKED FOR RICH SEMANTICS.

### Reduced version

Status: READY.

Observation staff withdraw first.

The Pokémon under observation remain outside BattleSpec unless Ouros independently selects specific individuals as legitimate combatants.

Combat occurs on static safe geometry.

Victory does not prove displacement, aggression, ownership, capture legality or ecological risk.

## 21. Full versus reduced implementation principle

The narrative premise should survive reduction.

Full version:

- active environment may matter mechanically;
- escort and protection may happen inside initiative;
- specialized AI must understand objectives;
- adapter must render semantic hazards correctly.

Reduced version:

- Ouros resolves environmental safety and noncombatant movement before battle;
- BattleSpec contains only explicit combatants and verified static geometry;
- no invented environmental mechanics enter AutoPTU;
- post-battle world-state decisions remain with Ouros owners.

This lets the worldbuilding exist now without making Minecraft recreate missing PTU rules.

## 22. Mechanical assumptions that remain UNKNOWN

Do not author universal mechanics for:

- generic wind push;
- gust forced movement;
- wind-based knockback distance;
- flying-debris damage;
- falling-branch damage;
- tree-fall timing;
- unstable-sign or roof-element reactions;
- wind-based accuracy penalties;
- ranged-attack deviation;
- Flying-type wind immunity;
- Ground/Rock/Steel-type wind resistance;
- weight-based wind resistance;
- size-based wind resistance;
- generic bracing actions;
- generic shelter bonuses;
- universal Acrobatics/Athletics checks against gusts;
- environmental reaction windows;
- generic airborne status;
- automatic weather-triggered Abilities outside their exact PTU rules;
- species-derived storm prediction;
- species-derived structural safety sensing;
- Trainer Features that create wind-response authority.

## 23. Minecraft/Cobblemon/Craftics boundary

Minecraft/Cobblemon may present already-decided world state:

- fallen trees;
- removed branches;
- temporary barriers;
- damaged or replaced signs;
- boarded openings;
- changed NPC routes;
- repair crews;
- temporary access paths;
- wild Pokémon using unusual authored locations;
- weather visuals chosen by Ouros.

Native simulation does not become authority.

Forbidden inference examples:

- entity pushed by Minecraft wind/mod physics => PTU forced movement;
- block broken => wind damage confirmed;
- leaf decay => tree health conclusion;
- redstone line inactive => Grid outage truth;
- open door => building cleared;
- mob pathfinding around debris => route legally reopened;
- Pokémon spawn after storm => displacement confirmed;
- Minecraft thunderstorm => PTU battle Weather;
- Cobblemon BattleState => combatant selection or narrative outcome.

Ouros decides world facts. AutoPTU decides tactical battle facts. Minecraft/Cobblemon/Craftics presents them.

## 24. Canon questions left open

- Which Ouros regions regularly experience damaging wind?
- What locally counts as unusual or exceptional wind?
- Which forecasting technologies exist in each region?
- Which institutions issue notices, if any?
- Who performs post-event impact surveys?
- What records are public?
- Which tree-management institutions exist?
- What authority governs emergency debris removal?
- How do route owners coordinate with Grid and Building Safety?
- Do any settlements have historic wind shelters or architectural adaptations?
- Which wind-related infrastructure already exists?
- Are there documented individual Pokémon with trained observation, search or work roles?
- Which historic wind episodes, if any, are established canon?

None of these questions are answered silently by this extension.
