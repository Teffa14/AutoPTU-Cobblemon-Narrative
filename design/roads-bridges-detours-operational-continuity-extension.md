# Ouros Roads, Bridges & Detours Operational Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. NON-CANON until explicitly approved. This extension does not establish that any particular Ouros region has paved roads, motor vehicles, drawbridges or specific transport law.

## Purpose

Travel already owns the regional connection graph and journeys. Civic/Public Works owns collective decisions and major projects. Facility Maintenance owns condition, faults, work orders, repair and verification. Pass 95 adds the persistent operational layer that translates those facts into what a traveler can actually use now.

The main questions are concrete:

- Which exact road section or crossing is affected?
- What access is currently authorized?
- Is the restriction total or limited to one approach, surface, direction, user class or time window?
- What detour is actually available?
- What evidence supports the restriction?
- What must happen before access changes?
- What downstream places and actors react to the disruption?
- What remains after the permanent route returns?

The extension avoids a universal traffic simulator. It stores durable facts only when they affect choices, continuity or consequences.

## 1. Authority boundary

Road Operations owns the traveler-facing operational state of authored road/crossing assets.

Travel owns:
- endpoints and regional topology;
- journey creation;
- mode viability;
- route selection;
- travel consequences.

Facility Maintenance owns:
- physical-condition observations;
- faults;
- technical assessment;
- work orders;
- repair progress;
- verification evidence.

Civic/Public Works owns:
- major public decisions;
- replacement/reroute proposals;
- approvals;
- project authority;
- budgets and competing priorities.

Cartography owns map/survey versions. Public Notices owns published information and signs. Conservation/Wildlife owns ecological interpretation. Weather owns weather truth. Worksite Safety owns crew-safety procedures. Technology owns controlled mechanisms where canon supports them.

Road Operations references those systems; it does not duplicate their authority.

## 2. Road corridor and segment identity

```yaml
road_corridor:
  corridor_id: null
  canonical_name_ref: null
  endpoint_location_ids: []
  travel_connection_ids: []
  segment_ids: []
  crossing_asset_ids: []
  operator_or_authority_refs: []
  historical_alignment_refs: []
  canon_reference_ids: []
```

```yaml
road_segment:
  segment_id: null
  corridor_id: null
  geometry_ref: null
  endpoint_refs: []
  surface_or_form: authored_or_unknown
  access_profile_id: null
  operational_state: UNKNOWN
  active_restriction_ids: []
  active_detour_ids: []
  maintenance_asset_refs: []
  notice_refs: []
  map_revision_refs: []
  ecology_overlap_refs: []
  history_event_ids: []
```

A segment survives changes in access, condition and naming. This lets the same road accumulate history rather than being deleted and regenerated whenever it closes.

## 3. Crossing asset

```yaml
road_crossing_asset:
  crossing_id: null
  corridor_id: null
  crossing_type: authored_or_unknown
  connected_segment_ids: []
  approach_ids: []
  usable_surface_refs: []
  maintenance_asset_id: null
  control_system_ref: null
  maritime_or_other_network_refs: []
  operational_state: UNKNOWN
  access_profile_id: null
  active_restriction_ids: []
  verification_refs: []
  history_event_ids: []
```

Possible authored forms include bridge, causeway, ford, tunnel approach, temporary crossing or another setting-supported solution. These labels describe world objects only. They grant no mechanical traversal rule.

A bridge can have multiple usable surfaces or approaches. One may remain available while another is closed.

## 4. Operational state

Suggested coarse states:

```text
UNKNOWN
OPEN
LIMITED_ACCESS
CONTROLLED_ACCESS
LOCAL_ACCESS_ONLY
TEMPORARY_CONFIGURATION
DETOUR_IN_EFFECT
CLOSED
DESTROYED_OR_IMPASSABLE
UNDER_WORK
TESTING_OR_VERIFYING
REOPENING
DECOMMISSIONED
```

These are world-state bands. They are not structural conditions, engineering ratings or PTU terrain types.

A structure may be physically sound but `CLOSED`. A repair may be physically complete while the crossing remains `TESTING_OR_VERIFYING`. A corridor can be `DETOUR_IN_EFFECT` while the original segment is still `UNDER_WORK`.

## 5. Access profile

```yaml
road_access_profile:
  access_profile_id: null
  segment_or_crossing_ref: null
  effective_from: null
  effective_until_or_trigger: null
  allowed_authored_access_classes: []
  denied_authored_access_classes: []
  direction_constraints: []
  time_window_refs: []
  escort_or_service_requirements: []
  exception_refs: []
  basis_refs: []
  authority_ref: null
```

Access classes exist only if canon establishes them. Examples may include pedestrian, bicycle, cart, ordinary vehicle, service crew, emergency access, mounted travel or other local categories. The generator cannot create transport law from contemporary real-world assumptions.

An access profile changes Travel viability; it does not alter PTU movement statistics.

## 6. Restriction record

```yaml
road_operational_restriction:
  restriction_id: null
  affected_segment_or_crossing_ids: []
  restriction_kind: authored
  observed_or_effective_at: null
  basis_observation_refs: []
  maintenance_assessment_refs: []
  civic_or_authority_refs: []
  weather_refs: []
  ecology_refs: []
  allowed_access_profile_id: null
  public_notice_refs: []
  review_trigger: null
  status: ACTIVE
```

Possible high-level reasons include inspection pending, worksite, obstruction, structural concern, weather consequence, controlled crossing window, ecological mitigation, emergency response, test/verification or unknown cause.

Reason and cause must remain separate. `OBSTRUCTION` can be true while the cause is still disputed.

## 7. Detour as a real temporary connection

```yaml
road_detour:
  detour_id: null
  replaces_or_bypasses_segment_ids: []
  travel_connection_ids: []
  start_location_ref: null
  end_location_ref: null
  access_profile_id: null
  effective_from: null
  end_trigger: null
  map_revision_refs: []
  notice_refs: []
  capacity_or_use_notes: []
  ecology_overlap_refs: []
  settlement_effect_refs: []
  history_event_ids: []
  status: ACTIVE
```

A detour must be physically and socially grounded. It may use another existing road, a temporary bypass, a local path or a crossing created by an authorized project. If no alternate connection exists, the system reports that honestly.

A detour can create consequences of its own:
- more visitors through a quiet settlement;
- courier delay;
- changed storefront demand;
- congestion near a public space;
- wildlife crossing overlap;
- wear on a secondary road;
- altered emergency response;
- new local knowledge and signage.

Returning the main corridor does not erase those consequences.

## 8. Inspection, repair, verification and access change

Road Operations consumes evidence from Facility Maintenance instead of running its own engineering simulator.

Typical chain:

```text
condition observation
-> maintenance assessment
-> restriction or closure if authorized
-> work order / public works dependency
-> repair or mitigation
-> verification / test
-> authority/access review
-> Road Operations state revision
-> Travel graph availability update
-> notice/map updates
```

Each arrow can happen at a different time.

A passed repair inspection does not automatically remove a restriction if another dependency remains. Conversely, an operational restriction can be lifted without pretending every deferred maintenance item disappeared.

## 9. Controlled or movable crossing windows

If canon supports a crossing whose configuration changes over time:

```yaml
crossing_operation_window:
  window_id: null
  crossing_id: null
  configuration_state: authored
  active_from: null
  active_until_or_trigger: null
  road_access_profile_id: null
  linked_transport_operation_refs: []
  control_authority_ref: null
  observed_state_refs: []
```

Examples could include a movable bridge coordinated with vessel traffic or another controlled crossing. The exact mechanism, operator and timing must be authored.

Minecraft redstone or animation may present the configuration. Ouros stores the authoritative world state. A moving bridge never becomes a tactical rule solely because blocks moved visually.

## 10. Route truth, public information and actor knowledge

Three layers must stay distinct:

- actual operational state;
- published notice/map/sign state;
- what an actor currently knows.

This supports situations such as:

- a sign that has not been replaced yet;
- an app/map revision published before a physical sign changes;
- a local resident who knows a legal bypass;
- a courier still following yesterday’s restriction;
- a reopened crossing whose old closure notice remains cached;
- a temporary road everyone now treats as the ordinary route.

No discrepancy forces deception or incompetence. Provenance and timestamps decide what can be concluded.

## 11. Ecology and roads

A road can intersect habitat without Road Operations becoming the ecology authority.

```yaml
road_ecology_overlap:
  overlap_id: null
  segment_or_detour_id: null
  observation_refs: []
  conservation_case_refs: []
  wildlife_monitoring_refs: []
  managed_use_policy_refs: []
  operational_mitigation_refs: []
  status: OBSERVED
```

Possible world-state responses, when authorized, include timing changes, temporary restriction, crossing monitoring, route shift or no operational change.

The presence of Pokémon near a road never proves a migration corridor, hazard, culpability or encounter. Conservation/Wildlife systems interpret evidence.

## 12. Legacy alignments and decommissioned crossings

```yaml
legacy_road_alignment:
  legacy_id: null
  former_corridor_or_segment_refs: []
  retired_at: null
  current_use_refs: []
  remaining_physical_refs: []
  public_access_state: null
  ecology_refs: []
  heritage_refs: []
  reactivation_proposal_refs: []
```

Old roads can become paths, service access, habitat edges, public space, heritage traces or inaccessible ruins. A future reopening proposal must respect the state accumulated since retirement.

## 13. World history events

Useful event types:

```text
RESTRICTION_POSTED
ACCESS_PROFILE_CHANGED
SEGMENT_CLOSED
DETOUR_ACTIVATED
TEMPORARY_CROSSING_OPENED
WORK_STARTED
WORK_COMPLETED
TESTING_STARTED
VERIFICATION_RECORDED
PARTIAL_REOPENING
FULL_REOPENING
DETOUR_RETIRED
ALIGNMENT_DECOMMISSIONED
CONTROL_WINDOW_CHANGED
ECOLOGY_MITIGATION_APPLIED
```

Events preserve history after cones, barriers and temporary signs disappear.

## 14. Pokémon participation boundary

Pokémon may assist road work, inspection, escort, transport or clearing only when governing PTU/Caelo state or explicit Ouros canon supports that exact role.

Do not infer:
- lifting from body size;
- cutting from claws;
- demolition from Rock/Ground typing;
- electrical control work from Electric typing;
- bridge sensing from species flavor;
- traffic direction from intelligence flavor;
- hauling eligibility from apparent strength;
- legal mount access from species shape.

The Pokémon Work layer owns an individual’s established work role. Any tactical use must pass through AutoPTU.

## 15. Encounter contract — Bridge Approach Withdrawal

Narrative premise:

A crossing is already under restriction when a hostile or territorial situation develops near an approach. Workers or travelers must be removed from the immediate area while the tactical conflict is contained.

Full intended version may include:
- multiple withdrawal routes;
- Intercept and forced displacement;
- protected access zones;
- terrain/hazard effects only if authored and mechanically supported;
- actors whose policy favors withdrawal or route denial over KO;
- authoritative Minecraft playback.

Permanent capability requirements:

```yaml
requirements:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Current authoring profile: REDUCED.

Reduced version:

Close the crossing completely in world state before combat. Remove workers, travelers, vehicles/equipment and nonparticipating Pokémon. Use a reviewed static arena on a safe approach or abutment. Rails, drops, water, moving mechanisms and unstable surfaces remain scenery or excluded geometry. Ouros selects combatants explicitly; AutoPTU resolves the battle. The result can establish that the immediate approach is secure. Maintenance/authority evidence still decides inspection and reopening.

## 16. Encounter contract — Detour Wildlife Crossing

Narrative premise:

A temporary bypass begins intersecting an observed wildlife-use area. The full encounter could involve keeping a route clear long enough for people to withdraw while wild actors seek territory, escape or separation rather than knockout.

Full intended version particularly depends on:
- complete movement;
- terrain/zones/reactions where crossing space matters;
- objective-aware AI tactical policy;
- adapter/playback;
- exact Move/Ability/Item/Feature behavior used by participants.

Current authoring profile: REDUCED.

Reduced version:

Road Operations closes the bypass temporarily before tactical resolution. Travelers and wildlife not selected for the battle stay outside the grid. Run a static encounter on a nearby safe verge or authored clearing. Winning does not prove the corridor is ecologically safe. Conservation/Wildlife reviews observations afterward; Travel then chooses whether the bypass remains closed, reopens, changes timing or is replaced.

## 17. Encounter contract — Controlled Crossing Service Window

Narrative premise:

If canon supports a movable or scheduled crossing, a disturbance occurs during a planned operational window.

The mechanically rich version would require dynamic configuration, route-control objectives, reaction behavior, possibly environmental zones and faithful playback.

Current authoring profile: REDUCED / CONDITIONAL CANON.

Reduced version:

Freeze the crossing configuration before battle. Road and any linked maritime/service state are paused. Clear all ordinary traffic. Instantiate a static legal arena away from moving machinery. The crossing cannot change configuration during tactical resolution. After AutoPTU finishes, Road Operations and the linked service systems determine whether the next operating window proceeds.

## 18. Noncombat investigation — Three Closures, One Physical Problem

Several records appear to describe repeated road failures.

The playable investigation compares:
- exact segment IDs;
- dates and times;
- inspection/assessment references;
- map revisions;
- notices;
- traveler reports;
- work orders;
- photographs;
- detour periods.

The result may show three notices covering one continuous restriction, two independent issues, a stale notice or unresolved ambiguity. No hidden truth score is required.

This structure is executable as world-state content now.

## 19. Long-term continuity pattern — A Road Learns Its Crossing

Stage 1 establishes ordinary use, nearby settlements, local travelers and known wildlife observations.

Stage 2 introduces a limited restriction rather than immediate destruction.

Stage 3 activates a real detour. Shops, couriers, residents, visitors and ecology react to changed movement.

Stage 4 produces maintenance/inspection or civic evidence and a visible work phase.

Stage 5 enters testing or limited reopening. Old public information can coexist temporarily with the new state.

Stage 6 restores or replaces the main connection, but the bypass and changed habits leave traces.

Stage 7 revisits the same corridor later when an old alignment, former detour, recurring observer or changed wildlife route makes the earlier event relevant again.

The road gains history without an abstract `road_level`.

## 20. Minecraft/Cobblemon boundary

Likely SAFE_REUSE candidates, subject to concrete API review:
- blocks, slabs, paths and decorative road geometry;
- bridges, barriers, gates and signs as presentation;
- lamps and signals as presentation;
- particles, sounds and weather visuals;
- Pokémon overworld entities, models, forms, poses and cries;
- map/UI surfaces;
- world coordinates;
- networking, entity tracking and synchronization.

Likely ADAPTER_REQUIRED behavior:
- projecting authoritative restriction state into physical barriers;
- mapping reviewed road geometry into a BattleSpec;
- maintaining stable segment/crossing identifiers across world loads;
- syncing authoritative opening/closure state to clients;
- converting exact safe static geometry to AutoPTU cells.

BATTLE_AUTHORITY_FORBIDDEN behavior includes:
- using nearby Minecraft entities to select combatants;
- using block collision to decide PTU forced movement or damage without reviewed mapping;
- treating a redstone mechanism as authority for route or battle state;
- allowing a falling block, moving piston, minecart or vehicle simulation to resolve tactical damage/displacement;
- using Cobblemon BattleState to decide HP, statuses, positions, participants or result.

Binding direction remains:

`Ouros road/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

## 21. Canon safeguards

This extension does not establish:
- road ownership;
- transport ministries or road authorities;
- legal vehicle classes;
- licensing;
- road pricing/tolls;
- motorized vehicles;
- speed limits;
- bridge engineering standards;
- inspection qualifications;
- public liability;
- right-of-way law;
- drawbridge technology;
- emergency exemptions;
- Pokémon road labor practices.

All require authored canon or governing source evidence.

## 22. Implementation value

The extension gives familiar geography memory. A route can be open, partially restricted, rerouted, under work, testing, reopened and later remembered without replacing the location. It also gives Travel, Courier, Commerce, Public Works, Conservation and Minecraft presentation a shared durable reference for why movement changed.

Mechanically rich road scenes remain reduced until the exact AutoPTU families they need are verified rather than inferred from adjacent Intercept progress.
