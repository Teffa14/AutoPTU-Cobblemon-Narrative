# Ouros Coastal Navigation Aids, Lighthouses & Beacon Continuity Extension

Status: proposed systems design. Not established Ouros canon.
Date: 2026-08-28

## Purpose

The Maritime layer already allows sea lanes, harbors, navigation assets and navigation knowledge. Cartography owns map/chart representations. Technology owns technical assets and failures. Maintenance owns repair/inspection. Public Notices owns published changes. Weather owns atmospheric observations. Soundscapes owns acoustic evidence.

This extension coordinates the operational life of navigation aids across those systems.

It models:
- exact aid identity;
- intended characteristics;
- observed characteristics;
- position/history;
- notices and registry revisions;
- availability and degraded operation;
- temporary replacements and mitigations;
- inspection/restoration verification;
- public/technical access;
- ecology and heritage overlap;
- encounter handoffs.

It does not define navigation bonuses, fog penalties, light ranges, marine vehicle rules, electrical hazards or Pokémon work capabilities.

## 1. Core authority rule

Navigation aids provide information and landmarks. They do not move vessels or resolve journeys themselves.

Authority chain:

`aid observation / notice -> Maritime + Travel route/service decision`

Technology/Maintenance owns whether the asset functions technically.

Cartography owns charts and editions.

Public Notices/Communications owns dissemination.

Ouros world state owns the semantic facts.

AutoPTU owns all tactical battle facts.

Minecraft/Cobblemon presents the approved state.

## 2. Navigation aid

```yaml
navigation_aid:
  navigation_aid_id: null
  maritime_region_id: null
  location_ref: null
  aid_type: null
  physical_asset_ref: null
  operator_or_steward_ids: []
  registry_entry_id: null
  current_characteristic_id: null
  intended_characteristic_id: null
  current_position_ref: null
  position_history_ids: []
  current_operational_state: UNKNOWN
  public_access_profile_id: null
  technical_access_profile_id: null
  maintenance_record_ids: []
  observation_ids: []
  notice_ids: []
  ecology_overlap_ids: []
  heritage_refs: []
  pokemon_work_assignment_ids: []
  canon_reference_ids: []
```

Candidate `aid_type` values are descriptive only:
- LIGHTHOUSE
- FIXED_LIGHT
- DAYMARK
- BUOY
- BEACON
- RANGE_OR_ALIGNMENT_MARK
- SOUND_SIGNAL
- ELECTRONIC_OR_REMOTE_MARK
- TEMPORARY_MARK
- OTHER_REVIEWED_AID

No type implies a real-world standard or PTU modifier.

## 3. Aid registry entry

```yaml
aid_registry_entry:
  registry_entry_id: null
  navigation_aid_id: null
  registry_family_id: null
  stable_reference_code: null
  effective_from: null
  effective_to: null
  registered_position_claim: null
  characteristic_claim_id: null
  access_notes: []
  route_context_refs: []
  source_record_ids: []
  supersedes_id: null
  status: CURRENT
```

Suggested statuses:
- CURRENT
- SUPERSEDED
- TEMPORARY
- WITHDRAWN
- HISTORICAL
- DISPUTED

A registry entry is a published/administrative representation. It does not overwrite the physical asset.

## 4. Aid characteristic

A characteristic is the intended observable identity of an aid.

```yaml
aid_characteristic:
  characteristic_id: null
  navigation_aid_id: null
  characteristic_type: null
  expected_visual_profile: null
  expected_acoustic_profile: null
  expected_temporal_pattern: null
  expected_orientation_or_sector_ref: null
  expected_active_window_ref: null
  source_record_ids: []
  effective_from: null
  supersedes_id: null
```

This schema deliberately avoids assuming real-world colour, flash or sound standards.

The same physical tower may have several historical characteristics over time.

## 5. Observation

```yaml
navigation_aid_observation:
  observation_id: null
  navigation_aid_id: null
  observer_ids: []
  observed_at: null
  observer_location_ref: null
  visibility_condition_refs: []
  observed_position_claim: null
  observed_visual_profile: null
  observed_acoustic_profile: null
  observed_pattern: null
  operating_claim: null
  source_media_ids: []
  confidence_band: null
  discrepancy_ids: []
```

Observation examples:
- light not visible;
- light visible with expected pattern;
- light visible with unexpected pattern;
- buoy seen displaced from registered position;
- expected sound not heard;
- signal heard from uncertain direction;
- aid visually obscured although monitoring reports normal operation.

An observation does not establish cause.

## 6. Discrepancy

```yaml
navigation_aid_discrepancy:
  discrepancy_id: null
  navigation_aid_id: null
  expectation_ref: null
  observation_refs: []
  discrepancy_type: null
  current_explanation_state: UNRESOLVED
  explanation_claim_ids: []
  confirmed_cause_ref: null
  operational_response_ids: []
  notice_ids: []
  opened_at: null
  resolved_at: null
```

Candidate discrepancy types:
- NOT_OBSERVED
- WRONG_CHARACTERISTIC
- OFF_STATION
- WRONG_POSITION_IN_PUBLICATION
- INTERMITTENT
- VISIBILITY_OBSCURED
- SOUND_NOT_CONFIRMED
- MONITORING_DISAGREEMENT
- DUPLICATE_OR_CONFUSED_IDENTITY
- UNKNOWN

Do not default to sabotage.

## 7. Operational state

Use readable state distinct from physical condition.

```yaml
navigation_aid_operational_state:
  navigation_aid_id: null
  state: NORMAL
  effective_from: null
  active_fault_refs: []
  active_discrepancy_refs: []
  active_mitigation_refs: []
  monitoring_state: UNKNOWN
  verification_ref: null
```

Suggested states:
- NORMAL
- DEGRADED
- INTERMITTENT
- UNRELIABLE
- OUT_OF_SERVICE
- TEMPORARILY_REPLACED
- TESTING
- DECOMMISSIONED
- UNKNOWN

A light can be physically intact and operationally unreliable.

A tower can remain open to visitors while the aid is out of service.

## 8. Navigation notice handoff

This extension produces notice facts; Public Notices/Communications owns publication/delivery.

```yaml
navigation_change_packet:
  change_packet_id: null
  navigation_aid_id: null
  effective_from: null
  change_type: null
  expected_duration_ref: null
  affected_route_refs: []
  source_evidence_ids: []
  authority_or_issuer_ref: null
  public_notice_ref: null
  chart_update_recommendation_ref: null
  superseded_by_id: null
```

Candidate changes:
- TEMPORARILY_UNLIT
- CHARACTERISTIC_CHANGED
- OFF_STATION
- RELOCATED
- TEMPORARY_MARK_INSTALLED
- RESTORED
- DECOMMISSIONED
- POSITION_CORRECTED
- VISIBILITY_RESTRICTED
- OTHER_REVIEWED_CHANGE

A notice can be current, stale, delayed or unknown to a particular actor.

## 9. Route consequence handoff

The aid layer never sets journey success directly.

```yaml
navigation_route_advisory:
  advisory_id: null
  source_change_packet_ids: []
  maritime_lane_ids: []
  observed_condition_refs: []
  advisory_scope: null
  recommendation_claim: null
  owner_system: MARITIME_TRAVEL
```

Maritime/Travel may decide:
- no change;
- caution/limited operation;
- daylight-only service if canon supports it;
- reroute;
- local guide/pilot mitigation if canon supports it;
- temporary suspension;
- emergency-only use.

Pass 92 defines none of those policies automatically.

## 10. Temporary aid or mitigation

```yaml
navigation_mitigation:
  mitigation_id: null
  affected_aid_ids: []
  mitigation_type: null
  deployed_at: null
  physical_asset_refs: []
  operator_ids: []
  intended_scope: null
  current_state: null
  verification_ids: []
  withdrawal_event_id: null
```

A temporary mark should not silently replace the permanent asset's identity.

## 11. Inspection and restoration

Maintenance owns the actual work order. Pass 92 receives the result.

```yaml
navigation_verification:
  verification_id: null
  navigation_aid_id: null
  performed_at: null
  verifier_ids: []
  maintenance_ref: null
  observed_characteristic_ref: null
  position_check_ref: null
  monitoring_check_ref: null
  result: UNKNOWN
  limitation_notes: []
  followup_refs: []
```

Possible results:
- VERIFIED_NORMAL
- VERIFIED_DEGRADED
- FAILED_VERIFICATION
- PARTIAL_VERIFICATION
- INCONCLUSIVE

Repair completion and service restoration are separate events.

## 12. Public access and tourism

```yaml
navigation_site_access_profile:
  site_id: null
  public_area_refs: []
  restricted_area_refs: []
  technical_area_refs: []
  current_public_access_state: null
  current_technical_access_state: null
  access_notice_ids: []
```

A lighthouse can be:
- operational and closed to visitors;
- out of service but open as a heritage site;
- technically restricted while the grounds remain public;
- undergoing repair while an alternate aid continues the navigation function.

Tourism owns visitor effects.

## 13. Staffed, automated and remote operation

No universal model is assumed.

Possible canon patterns:
- resident keeper;
- rotating technical crew;
- remote monitoring with periodic visits;
- hybrid local/remote operation;
- community stewardship;
- Pokémon-assisted operation with an explicit individual assignment;
- historic/non-operational landmark.

An automated aid still produces:
- monitoring observations;
- faults;
- inspections;
- component replacement;
- access episodes;
- outage history.

## 14. Pokémon-assisted navigation aid boundary

A Pokémon may participate only when all of the following are explicit:
- individual Pokémon identity;
- relationship/custody/partnership state where relevant;
- work assignment;
- task requirement;
- capability evidence;
- supervision/authorization;
- welfare/availability state;
- PTU/Caelo mechanical review if a capability is mechanically relevant.

Forbidden shortcuts:
- Electric type -> lighthouse worker;
- Ampharos species -> legal beacon;
- glowing animation -> verified signal range;
- entity standing on platform -> assignment;
- Cobblemon pose -> completed work.

## 15. Ecology overlap

A navigation aid can become ecological structure.

Examples:
- nesting/roosting on tower exterior;
- marine Pokémon sheltering around a buoy mooring;
- a decommissioned light becoming habitat;
- maintenance timing intersecting seasonal presence;
- illumination affecting an observed behavior pattern.

Conservation and Interspecies Ecology own interpretation/policy.

Pass 92 records overlap and handoff only.

## 16. Heritage continuity

A technical function and heritage function may diverge.

```yaml
navigation_heritage_link:
  navigation_aid_id: null
  historical_characteristic_ids: []
  interpretation_refs: []
  public_memory_refs: []
  archival_refs: []
  preserved_component_refs: []
  current_operational_relation: null
```

A decommissioned lighthouse can remain a landmark.

A modern replacement does not delete the old aid's history.

## 17. Actor knowledge

```yaml
navigation_aid_knowledge:
  holder_id: null
  navigation_aid_id: null
  known_registry_entry_ref: null
  known_characteristic_ref: null
  known_notice_ids: []
  last_direct_observation_id: null
  freshness_state: null
  uncertainty_notes: []
```

Different actors can possess different legitimate versions.

A fisher using yesterday's knowledge may be wrong today without being careless or dishonest.

## 18. Failure families

Potential causes remain claims until supported:
- power/supply loss;
- component wear;
- incorrect configuration;
- physical displacement;
- storm/environmental damage;
- monitoring failure;
- publication error;
- maintenance error;
- deliberate interference;
- wildlife interaction;
- access obstruction;
- unknown.

Case/Antagonist systems take over deliberate interference only when evidence supports it.

## 19. Minecraft/Cobblemon presentation

Strong reuse targets:
- lighthouse geometry, stairs, platforms and windows;
- lamps, glass, redstone-adjacent visuals and mechanical props;
- buoy/beacon structures;
- bells/horns/ambient sound presentation;
- particles and visible beam approximations;
- books/signs/maps/display blocks;
- Pokémon models/forms/poses/cries;
- world coordinates, networking and synchronization;
- public viewpoint/tourism dressing;
- weather/day-night visuals.

The semantic state comes from Ouros.

The adapter maps semantic state to visuals and reports player intent/observations.

Minecraft block power is not canonical operational authority.

## 20. Performance policy

Do not keep every offshore mark loaded.

Persist semantic state for the network.

Materialize:
- aids near players;
- a reviewed subset visible from shore;
- aids involved in current interaction;
- navigation assets needed for a scene.

Remote aids remain database/world state until relevant.

## 21. Noncombat investigation — Two Lights, One Chart

Premise:
A crew reports seeing two lights where its chart shows one aid.

Inputs:
- chart edition;
- registry entry;
- direct observations;
- timestamps;
- weather/visibility;
- harbor lighting records;
- temporary notices;
- photographs if any.

Possible explanations:
- temporary aid;
- unrelated harbor light;
- chart predates relocation;
- duplicate observation;
- reflection/line-of-sight effect;
- evidence insufficient.

No combat required.

## 22. Encounter contract — Beacon Head Withdrawal

Narrative premise:
A maintenance team at a remote beacon site encounters a wild group while leaving a restricted headland.

Intended full version:
- workers withdraw along multiple safe routes;
- possible narrow-edge positioning;
- Intercept/forced displacement if supported;
- territorial/withdrawal-aware wild AI;
- weather/visibility state if mechanically defined;
- exact semantic playback into Minecraft.

Full dependencies:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:
- maintenance team withdraws before battle;
- cliff edge/restricted machinery are excluded from the tactical map;
- weather remains visual/world state;
- Ouros chooses explicit combatants;
- AutoPTU resolves a static arena;
- Maintenance/Conservation decide site access afterward.

Battle victory cannot verify the beacon or reopen the site.

## 23. Encounter contract — Buoy Maintenance Window

Narrative premise:
A small maintenance operation reaches a navigation mark during a short safe access window and encounters territorial Pokémon.

Full version wants:
- water-sensitive movement;
- WITHDRAW/CLEAR_ROUTE intent;
- moving/service craft interaction only if authoritative;
- Intercept/forced movement;
- possible current/weather effects;
- territorial AI;
- adapter playback.

Reduced version:
- maintenance craft is narratively secured outside the tactical grid;
- workers and buoy are not tactical targets;
- use one static legal shoreline/platform/water arena;
- Ouros selects combatants;
- AutoPTU result only resolves the immediate conflict;
- actual buoy inspection occurs separately afterward.

## 24. Encounter contract — Fog-Signal Station Perimeter

Narrative premise:
A sound signal station reports inconsistent operation while a nearby wild group complicates inspection access.

Full version wants:
- reduced-visibility rules only if PTU/Caelo defines them and Java supports them;
- sound/zone interaction only if authoritative;
- route denial/withdrawal AI;
- possible reactions/Intercept;
- semantic playback.

Reduced version:
- fog and sound remain presentation/world observations;
- inspection team leaves the grid;
- static combat resolves access to the perimeter;
- Soundscapes + Maintenance investigate the inconsistent signal afterward.

## 25. Capability-aware authoring rule

For any new navigation-aid encounter:
- visual fog is not tactical Weather;
- a lighthouse beam is not an Accuracy buff;
- a cliff is not fall damage until the governing mechanic exists;
- a wave/current is not forced movement until authoritative support exists;
- a horn/siren is not a sound-based status or zone unless PTU/Caelo and AutoPTU support it;
- an electrical cabinet is not a hazard because Minecraft renders sparks;
- a Pokémon worker does not get a combat bonus from its job.

## 26. Long-term continuity

The same aid should accumulate history:
- characteristic revisions;
- outages;
- repairs;
- temporary replacements;
- keeper/operator changes;
- public-access changes;
- chart corrections;
- ecology overlap;
- heritage reinterpretation;
- decommissioning or replacement.

Do not replace the aid with a new quest object each time.

## 27. Canon review gates

Before any specific navigation network enters canon, establish:
1. maritime geography;
2. operating institution/stewardship;
3. technology available;
4. aid types and local standards;
5. chart/notice publication practice;
6. maintenance responsibility;
7. public access policy;
8. any Pokémon work practice;
9. ecology/heritage constraints;
10. Cobblemon presentation feasibility.

## 28. Explicit non-canon statement

This document establishes a reusable architecture only.

It does not establish that Ouros has:
- any lighthouse;
- any buoyage system;
- any standardized light colours/patterns;
- any lighthouse keeper profession;
- any navigation authority;
- any Pokémon-powered signal;
- any foghorn;
- any maritime technology standard.

All concrete examples remain proposals until reviewed.