# Ouros Land Tenure, Boundaries, Commons & Access Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros already knows where homes, farms, forests, reserves, roads, public spaces, workshops and settlements are. Several systems also contain ownership claims, stewardship records, access policies and land-use proposals. What was missing was a shared model for the relationship between a persistent place and the actors or groups allowed to use it.

This layer exists so the world can answer questions such as:
- who currently occupies this place;
- who may enter it;
- who may cross it without stopping;
- who may farm, graze, gather, build, maintain or research there;
- who can make a land-use decision within an authored mandate;
- what boundary version each claim uses;
- when a permission starts and ends;
- what happens when two valid uses overlap;
- which parts remain unresolved.

It deliberately does not define universal Ouros property law.

## 1. Core separation

Keep these states distinct:

```text
physical place
  -> surveyed / mapped boundary versions
  -> occupancy and residence
  -> tenure / use relationships
  -> access and passage permissions
  -> resource-use permissions
  -> management / stewardship authority
  -> transfer claims where canon supports them
  -> implemented controls such as gates or signs
  -> actor knowledge and public belief
  -> dispute / agreement / review state
  -> Minecraft permission projection
```

No arrow means automatic authority over the next state.

A resident may not own the land.
An owner claim may not include every use.
A steward may manage access without having transfer authority.
A public route may cross land that is otherwise restricted.
A seasonal grazing permission may coexist with a research exclusion zone at another time of year.
A fence can exist on the wrong line.

## 2. Persistent land unit

A land unit is a stable narrative identity for a bounded or functionally coherent place.

```yaml
land_unit:
  land_unit_id: null
  location_refs: []
  current_boundary_revision_id: null
  land_unit_type: null
  structure_refs: []
  current_use_profile_ids: []
  active_tenure_relationship_ids: []
  active_access_policy_ids: []
  active_stewardship_refs: []
  dispute_case_ids: []
  historic_boundary_revision_ids: []
  source_refs: []
  canon_status: proposed
```

Candidate narrative types:
- residential_lot;
- farm_block;
- orchard_block;
- ranch_or_pasture;
- forest_unit;
- workshop_or_industrial_site;
- institutional_ground;
- public_space;
- route_corridor;
- shoreline_or_waterfront_unit;
- research_site;
- conservation_site;
- shared_use_area;
- unallocated_or_unknown_use;
- other_authored.

The label describes current organization. It grants no legal or PTU effect.

## 3. Boundary revisions

Minecraft geometry, survey geometry and remembered geometry can disagree.

```yaml
land_boundary_revision:
  boundary_revision_id: null
  land_unit_id: null
  geometry_ref: null
  effective_from: null
  effective_until: null
  survey_record_ids: []
  map_edition_refs: []
  marker_refs: []
  confidence: null
  supersedes_revision_id: null
  change_reason_ref: null
  unresolved_segments: []
  source_refs: []
```

Possible reasons for revision:
- new survey;
- subdivision or consolidation explicitly authorized in canon;
- shoreline or river movement;
- road realignment;
- structural redevelopment;
- correction of an old map;
- settlement expansion;
- unresolved historic boundary;
- restoration project;
- other authored cause.

Changing a boundary revision never rewrites prior maps or historic actions.

## 4. Boundary evidence and claims

A marker is evidence. It is not automatically truth.

```yaml
boundary_observation:
  observation_id: null
  observed_at: null
  observer_id: null
  location_ref: null
  observed_feature: null
  candidate_boundary_ids: []
  method: null
  evidence_refs: []
  interpretation_status: unresolved
```

Examples:
- old stone marker;
- fence line;
- hedge;
- survey stake;
- wall;
- creek;
- historic map line;
- trail edge;
- verbal description in an archive.

A fence may predate the current survey. A river can move. A historic description may use a landmark that no longer exists.

## 5. Tenure relationship

This layer uses `tenure_relationship` as a neutral systems term for an authored relationship between actors and a place. It does not import any real-world legal regime.

```yaml
tenure_relationship:
  tenure_relationship_id: null
  land_unit_id: null
  holder_actor_ids: []
  holder_group_ids: []
  relationship_type: null
  granted_scopes: []
  restricted_scopes: []
  responsibility_refs: []
  source_authority_ref: null
  source_agreement_ref: null
  source_record_refs: []
  valid_from: null
  valid_until: null
  season_conditions: []
  event_conditions: []
  geographic_scope_ref: null
  status: active
  certainty: authored_or_verified
```

Suggested descriptive relationship types:
- OCCUPANCY;
- RESIDENCE_USE;
- FARMING_USE;
- GRAZING_USE;
- RESOURCE_GATHERING_USE;
- FORESTRY_USE;
- RESEARCH_USE;
- STEWARDSHIP_USE;
- PUBLIC_ACCESS;
- PASSAGE_ONLY;
- TEMPORARY_EVENT_USE;
- CONSTRUCTION_USE;
- SERVICE_OR_UTILITY_USE;
- CUSTODIAN_USE;
- TRANSFER_CLAIM;
- OWNERSHIP_CLAIM where canon actually establishes one;
- OTHER_AUTHORED_RELATIONSHIP.

The generator must not treat one type as containing all others.

## 6. Permission scopes

Permissions should be verbs.

Candidate scopes:
- ENTER;
- PASS_THROUGH;
- STAY_TEMPORARILY;
- RESIDE;
- CAMP;
- HOST_VISITORS;
- FARM;
- GRAZE_MANAGED_HERD;
- GATHER_SPECIFIED_RESOURCE;
- HARVEST_TIMBER;
- FISH;
- SURVEY;
- COLLECT_SAMPLE;
- MAINTAIN_INFRASTRUCTURE;
- OPERATE_SERVICE;
- BUILD_SPECIFIED_PROJECT;
- ALTER_SPECIFIED_FEATURE;
- HOLD_EVENT;
- STORE_MATERIAL;
- MANAGE_VISITOR_ACCESS;
- AUTHORIZE_SUBUSE;
- TRANSFER_SPECIFIED_RELATIONSHIP.

These scopes are narrative authority only. `FISH` does not define fishing mechanics. `ALTER_SPECIFIED_FEATURE` does not grant Groundshaper. `BUILD_SPECIFIED_PROJECT` does not bypass crafting, materials or Minecraft protections.

## 7. Access policy

Access can depend on time, actor, activity and world state.

```yaml
land_access_policy:
  access_policy_id: null
  land_unit_id: null
  issuing_authority_ref: null
  eligible_actor_ids: []
  eligible_group_ids: []
  default_access: restricted
  allowed_scopes: []
  prohibited_scopes: []
  supervision_requirements: []
  credential_requirements: []
  time_windows: []
  season_windows: []
  ecological_trigger_conditions: []
  crisis_override_refs: []
  route_or_passage_refs: []
  valid_from: null
  valid_until: null
  public_information_ref: null
```

Examples:
- public footpath through a farm during daylight;
- research access only during a survey window;
- seasonal closure around nesting;
- emergency utility access;
- festival use of a field for one week;
- visitor admission to a managed reserve;
- temporary construction access.

Minecraft door/gate state is an implementation of access, not the authority that created it.

## 8. Passage rights and route interfaces

Travel needs to know whether a physical connection is usable by a specific actor.

```yaml
passage_permission:
  passage_permission_id: null
  land_unit_ids: []
  route_segment_id: null
  eligible_actor_or_group_refs: []
  travel_modes_allowed: []
  stop_or_leave_route_allowed: false
  time_conditions: []
  closure_conditions: []
  source_ref: null
  status: active
```

A right to cross does not imply:
- a right to harvest;
- a right to camp;
- a right to battle or capture under local policy;
- a right to build;
- a right to enter nearby structures.

Travel remains responsible for route feasibility and transport.

## 9. Common-use areas

Ouros may eventually have shared-use land, forests, grazing grounds, docks, gardens, fishing reaches or courtyards. The layer must model who the participating community actually is.

```yaml
common_use_area:
  common_use_area_id: null
  land_unit_ids: []
  eligible_group_refs: []
  permitted_use_scopes: []
  allocation_or_schedule_refs: []
  stewardship_refs: []
  maintenance_responsibility_refs: []
  seasonal_conditions: []
  capacity_or_pressure_refs: []
  conflict_case_ids: []
  status: active
```

A common-use area is not automatically open to every actor on the server.

A public place is not automatically a common resource pool.

The exact social institution must be authored for Ouros.

## 10. Resource-use relationships

Resource access can be narrower than land access.

```yaml
land_resource_use_grant:
  use_grant_id: null
  land_unit_id: null
  resource_type_ref: null
  holder_refs: []
  permitted_action: null
  quantity_or_effort_limit_ref: null
  season_window_ref: null
  stewardship_condition_refs: []
  source_authority_ref: null
  active_from: null
  active_until: null
```

Examples may connect to:
- Food/Agriculture for crop production;
- Forestry for timber;
- Fisheries for aquatic harvest;
- Geology for extraction;
- Material Culture for gathered batches;
- Grasslands for managed grazing;
- Conservation for managed-use zones.

The specialized layer owns the actual production/harvest rules.

## 11. Occupancy, residence and land relation

Homes remains the authority on residences and households.

```text
land relationship -> permits or explains use of a place
residence -> records who actually lives there
household -> records shared residential use
home attachment -> records player/NPC-authored subjective home status
```

Occupancy does not create friendship, kinship, ownership or inheritance.

## 12. Land-use profile

A place can support overlapping functions.

```yaml
land_use_profile:
  land_use_profile_id: null
  land_unit_id: null
  valid_from: null
  valid_until: null
  active_uses: []
  inactive_legacy_uses: []
  compatible_use_refs: []
  conflict_refs: []
  infrastructure_dependency_refs: []
  ecological_dependency_refs: []
  public_service_refs: []
  change_event_id: null
```

Possible overlapping use example:
- orchard production;
- public walking route;
- pollinator monitoring;
- seasonal festival;
- utility maintenance corridor;
- nesting buffer on one edge.

No single use becomes the “true purpose” unless canon explicitly establishes exclusivity.

## 13. Land-use change

Land-use change must be causal and versioned.

```text
world need / actor proposal
  -> evidence and affected-use review
  -> authority / agreement check
  -> resource and implementation dependencies
  -> physical or policy change
  -> updated land-use profile
  -> downstream consequences
```

Examples of downstream handoffs:
- Agriculture;
- Demography;
- Architecture;
- Public Works;
- Road Ecology;
- Freshwater;
- Soil;
- Flora;
- Conservation;
- Tourism;
- Markets;
- Workplaces.

A land-use decision does not directly spawn a quest. Consequences create world facts from which later objectives may emerge.

## 14. Disputed claims

Conflicting claims do not choose a winner automatically.

```yaml
land_claim_record:
  claim_id: null
  claimant_refs: []
  land_unit_or_boundary_refs: []
  claimed_scope: null
  supporting_record_refs: []
  opposing_claim_refs: []
  current_status: unresolved
  case_id: null
  agreement_id: null
  review_id: null
  public_visibility: limited
```

Use:
- Cases for evidence and allegations;
- Cartography for surveys/maps;
- Archives for historic records;
- Agreements for negotiated outcomes;
- Governance for authored collective decisions;
- Institutional Review where a legitimate reviewing body exists.

Never create a court, title registry, adverse-possession rule or property crime solely because a dispute exists.

## 15. Physical controls

```yaml
land_access_control:
  control_id: null
  land_unit_id: null
  control_type: gate
  world_object_ref: null
  implementing_actor_ref: null
  policy_ref: null
  installed_at: null
  operational_state: functional
  access_effect: null
```

Examples:
- gate;
- fence;
- sign;
- staffed checkpoint;
- temporary barrier;
- marked trail;
- seasonal rope line;
- locked door;
- bridge access control.

Physical control and valid authority remain separate. A broken gate does not revoke a policy. A locked gate does not prove the locker had legitimate authority.

## 16. Wild Pokémon boundary

Human land relationships do not define Pokémon ownership.

Rules:
- a wild Pokémon entering a farm does not become farm property;
- a Pokémon nesting inside a structure does not automatically gain or erase human tenure;
- a managed Pokémon living on a ranch uses Pokémon Agency/custody state;
- release does not transfer a Pokémon into land ownership;
- habitat use is ecological evidence, not a deed;
- a Trainer cannot claim every wild Pokémon in an area by acquiring the land relationship.

## 17. Multiplayer safeguards

Irreversible shared-space changes require explicit authority.

The server should distinguish:
- player can physically place/break blocks;
- player has permission to modify their residence;
- player has a project authorization for a shared site;
- player is temporarily helping under another actor’s authorization;
- player has no valid authority even if a Minecraft permission bug allows the action.

Player-created organizations should not receive land powers automatically. Those powers require explicit world-state grants.

## 18. Minecraft projection

Minecraft needs a projection service, not a duplicate property engine.

Possible outputs:
- boundary visualization for authorized users;
- doors/gates/containers permissions;
- build-zone permissions;
- route access state;
- public/private room presentation;
- signs and notices;
- temporary construction barriers;
- event-use overlays.

The source of truth remains server-side narrative/world state.

Chunk loading must never determine whether a claim exists.

## 19. Battle boundary

Land authorization is resolved before AutoPTU unless a specific tactical objective explicitly involves access.

A farm, reserve or private site does not grant:
- terrain effects;
- cover;
- initiative;
- Accuracy changes;
- capture modifiers;
- Trainer Feature bonuses;
- AI behavior;
- forced movement;
- protected-zone mechanics.

Those require exact PTU/Caelo rules and implemented engine support.

## 20. Encounter implementation contracts

### Boundary Survey at Alder Field

Narrative premise:
Two archived maps disagree about where a public passage crosses a working field. A fresh survey is interrupted by displaced wild Pokémon using the same corridor.

FULL version requires:
- complete movement including interception / forced movement if actors must preserve a moving passage corridor: BLOCKING;
- terrain/weather/hazards/zones/reactions only if an exact validated environmental effect is authored: BLOCKING;
- AI tactical policy for WITHDRAW / CLEAR_ROUTE / PROTECT survey gear: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:
- survey and wildlife movement resolve in overworld state;
- observers move to safety;
- freeze a legal static arena;
- battle only the Pokémon/actors actually remaining in conflict;
- preserve survey evidence independently of battle outcome.

### Shared Meadow Waterpoint

Narrative premise:
Several legitimate seasonal users arrive at the same waterpoint after a route closure changed normal timing. Wild Pokémon also use the site.

FULL version requires:
- complete movement for moving herds / withdrawal: BLOCKING;
- AI tactical policy for CROSS / WITHDRAW / PROTECT: BLOCKING;
- environment family only if a validated water/terrain effect enters battle: BLOCKING;
- playback: BLOCKING.

REDUCED version:
- resolve managed-herd and wild-population positioning before combat;
- use Agreements/Governance if users need a temporary schedule;
- open a static battle only if a distinct confrontation remains.

### Utility Corridor Reopening

Narrative premise:
A maintenance team has a narrow authored right to access a relay across land otherwise closed during a conservation window.

FULL version requires:
- complete movement / interception for a true escort corridor: BLOCKING;
- AI tactical policy for REACH_OBJECTIVE / PROTECT / WITHDRAW: BLOCKING;
- playback: BLOCKING;
- terrain/weather/hazards/zones/reactions only when separately validated.

REDUCED version:
- validate permission before entry;
- move technicians and equipment outside the grid;
- if wildlife or hostile actors create a real battle, freeze one static encounter space;
- maintenance resumes only after the battle/world state allows it.

## 21. Permanent engine capability categories

Narrative concepts must use the project-wide categories without inference inflation.

VERIFIED at the Pass 108 inspection:
- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

BLOCKING:
- complete movement including push / pull / knockback / interception / forced movement;
- terrain / weather / hazards / zones / reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter and playback.

The latest Java Trainer Feature transaction composes generic gating/resource/usage infrastructure but leaves concrete Feature effect semantics behind an injected effect implementation. It strengthens the PARTIAL assessment; it does not prove the catalog.

## 22. New overworld blockers

These do not belong inside AutoPTU-Java:

- `LAND_UNIT_IDENTITY`
- `LAND_BOUNDARY_REVISION_HISTORY`
- `BOUNDARY_OBSERVATION_PROVENANCE`
- `TENURE_RELATIONSHIP_STATE`
- `LAND_ACCESS_POLICY`
- `PASSAGE_PERMISSION_STATE`
- `COMMON_USE_AREA_STATE`
- `LAND_RESOURCE_USE_GRANT`
- `LAND_USE_PROFILE_HISTORY`
- `LAND_CLAIM_GRAPH`
- `LAND_ACCESS_CONTROL_PROJECTION`
- Land -> Homes handoff
- Land -> Travel handoff
- Land -> Agriculture/Forestry/Fisheries/Geology handoff
- Land -> Conservation/Public Works handoff
- Land -> Minecraft permission projection
- Land -> frozen battle snapshot contract

## 23. Hard non-inferences

Do not infer:
- occupancy -> ownership;
- ownership claim -> unlimited authority;
- residence -> transfer rights;
- stewardship -> ownership;
- public access -> public ownership;
- common use -> open access to everyone;
- passage -> harvest/build/camp permission;
- map line -> canonical boundary;
- fence/sign/gate -> valid claim;
- unlocked Minecraft door -> permission;
- wild Pokémon presence -> ownership;
- land ownership -> Pokémon ownership;
- conservation designation -> PTU capture rule;
- farm -> Grass Terrain;
- forest-use permission -> Naturewalk;
- road access -> movement bonus;
- water access -> Swim legality;
- boundary dispute -> criminal act;
- historical use -> current authority;
- long occupation -> automatic ownership;
- building something -> ownership of the ground;
- player block edit permissions -> narrative land authority.

## 24. Open canon/mechanical questions

- Does Ouros use any region-wide concept analogous to property ownership, or should relationships remain institution-specific?
- Which settlements maintain authoritative land/boundary records?
- Are some uses governed by community practice rather than formal institutions?
- Which common-use areas exist before campaign start?
- Can player clubs/businesses receive scoped land-use grants?
- What happens when a river, shoreline or road physically moves across a historic boundary?
- How are long-term residence, inheritance and succession handled if canon later establishes them?
- Who may authorize temporary access during emergencies?
- Which resource uses require explicit permission?
- How should Minecraft expose boundaries without turning exploration into permission popups everywhere?
- What PTU/Caelo rules govern physical land alteration when a Trainer actually uses a Move/Feature/Capability?

The primary Caelo corpus was not reliably accessible during this pass. Super PTU Online Helper was not available as an invokable tool. No rules were fabricated from either source.
