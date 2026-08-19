# Ouros Geology, Excavation & Resource Frontier Layer

Status: Proposed systems design. Not established canon.

## Purpose

This layer models subsurface places and geological resources as persistent world state.

It does not define PTU excavation rules, mining yields, fossil revival mechanics, geological hazard damage or Minecraft block-mining balance.

Its job is to preserve context so caves, mines, quarries, fossil beds and resource frontiers can generate connected stories across exploration, science, ecology, workplaces, infrastructure, governance and battle encounters.

## 1. Geological site

```yaml
geological_site:
  site_id: null
  location_id: null
  site_type: null
  access_state: unknown
  depth_bands: []
  formation_refs: []
  known_resource_refs: []
  fossil_context_ids: []
  habitat_overlap_ids: []
  heritage_overlap_ids: []
  water_system_ids: []
  infrastructure_ids: []
  stewardship_claim_ids: []
  extraction_project_ids: []
  observation_ids: []
  public_disclosure_state: limited
  current_condition: unknown
```

Candidate site types:
- CAVE_SYSTEM
- MINE
- QUARRY
- FOSSIL_BED
- CLIFF_EXPOSURE
- TUNNEL_NETWORK
- VOLCANIC_FIELD
- SUBTERRANEAN_WATERWAY
- ABANDONED_WORKING
- EXCAVATION_SITE
- NATURAL_SHAFT
- GEOTHERMAL_SITE

Site type is descriptive world state. It grants no mechanical effects.

## 2. Geological context and interpretation are separate

```yaml
geological_context:
  context_id: null
  site_id: null
  depth_band: null
  formation_label: null
  observed_material_refs: []
  observed_fossil_refs: []
  structural_observations: []
  relative_age_claims: []
  environmental_observations: []
  recorder_ids: []
  confidence: null
  source_event_ids: []
```

The world may contain a true geological history that players do not know.

A scientist's interpretation belongs in the science layer.

A miner's practical label may be useful without being scientifically exact.

A local traditional name may be culturally authoritative for that community without becoming a geological classification.

## 3. Resource body

```yaml
resource_body:
  resource_body_id: null
  site_id: null
  mechanical_resource_ref: null
  context_ids: []
  known_extent_state: unknown
  extraction_state: unknown
  access_constraints: []
  disturbance_links: []
  survey_claim_ids: []
  extraction_history_ids: []
  provenance_batch_ids: []
```

Recommended extraction states:
- UNKNOWN
- IDENTIFIED
- SURVEYED
- ACTIVE
- PARTIALLY_EXTRACTED
- DEPLETED
- SUSPENDED
- INACCESSIBLE
- FLOODED
- COLLAPSED
- CLOSED
- RESTORING
- REPURPOSED

Narrative state should usually remain coarse. Do not simulate every ore block as a unique economic asset.

## 4. Excavation project

```yaml
excavation_project:
  project_id: null
  site_id: null
  purpose: null
  operator_ids: []
  sponsor_ids: []
  scientific_partner_ids: []
  stewardship_actor_ids: []
  current_phase: proposed
  target_context_ids: []
  equipment_asset_ids: []
  staffing_requirement_refs: []
  access_claim_ids: []
  safety_observation_ids: []
  recovered_object_ids: []
  recovered_batch_ids: []
  disturbance_event_ids: []
  review_event_ids: []
```

Candidate purposes:
- SCIENTIFIC_SURVEY
- FOSSIL_RECOVERY
- RESOURCE_EXTRACTION
- INFRASTRUCTURE_CONSTRUCTION
- HAZARD_STABILIZATION
- HERITAGE_INVESTIGATION
- RESCUE_ACCESS
- WATERWORKS
- ROUTE_CREATION

Purpose can change after discovery.

A tunnel started as infrastructure may expose a fossil bed. A mine may become a protected research site. A quarry may close and become a habitat.

## 5. Fossil context

A fossil should not become only an inventory token at discovery time.

```yaml
fossil_context:
  fossil_context_id: null
  site_id: null
  context_id: null
  specimen_object_id: null
  observed_species_claims: []
  completeness_claims: []
  extraction_state: in_context
  finder_ids: []
  extraction_event_id: null
  preparation_record_ids: []
  analysis_record_ids: []
  custody_record_ids: []
  ownership_claim_ids: []
  public_disclosure_state: limited
  revival_status: unresolved
```

Recommended extraction states:
- IN_CONTEXT
- EXPOSED
- PARTIALLY_EXTRACTED
- RECOVERED
- DAMAGED
- LOST_CONTEXT

`LOST_CONTEXT` means scientific contextual information was lost. It does not automatically mean the fossil object was damaged.

## 6. Fossil revival boundary

Narrative generation may propose that an institution wants to evaluate or revive a recovered fossil.

It may not decide:
- that a fossil is revivable;
- revived species;
- level;
- Nature;
- Ability;
- Moves;
- loyalty/ownership;
- revival duration;
- revival cost;
- mechanical side effects.

Those require PTU/Caelo rules plus implementation data.

If revival occurs through an authoritative system, the resulting Pokémon should become a persistent Pokémon entity linked back to the fossil provenance chain.

## 7. Discovery event

```yaml
discovery_event:
  discovery_id: null
  site_id: null
  discoverer_ids: []
  discovery_type: null
  object_or_context_ids: []
  evidence_ids: []
  validation_state: unverified
  disclosure_state: private
  institution_notified_ids: []
  publication_ids: []
  public_memory_ids: []
  consequence_ids: []
```

Candidate discovery types:
- FOSSIL
- NEW_PASSAGE
- RESOURCE_BODY
- WATER_SOURCE
- RUIN_EXPOSURE
- HAZARD
- POKEMON_HABITAT
- OLD_WORKING
- TECHNICAL_ASSET
- GEOLOGICAL_ANOMALY

A discovery can remain private, disputed, restricted or unpublished.

## 8. Discovery boom

A sufficiently important public discovery can create a temporary regional state.

```yaml
discovery_boom:
  boom_id: null
  trigger_publication_ids: []
  affected_site_ids: []
  visitor_pressure: low
  commercial_pressure: low
  research_pressure: low
  theft_risk_state: low
  transport_load_ids: []
  lodging_load_ids: []
  stewardship_response_ids: []
  media_packet_ids: []
  rumor_ids: []
  current_phase: emerging
```

Suggested phases:
- EMERGING
- PEAK_INTEREST
- REGULATED
- DECLINING
- NORMALIZED

This is world-state pressure, not a guaranteed crisis.

## 9. Site disturbance

```yaml
site_disturbance:
  disturbance_id: null
  site_id: null
  cause_claim_ids: []
  observed_change_ids: []
  affected_context_ids: []
  affected_habitat_ids: []
  affected_infrastructure_ids: []
  severity_claims: []
  response_project_ids: []
  validated_mechanical_effect_refs: []
```

A disturbance can come from:
- excavation;
- natural erosion;
- flooding;
- seismic activity;
- Pokémon activity;
- infrastructure work;
- player construction;
- prior collapse;
- unknown causes.

Do not infer blame from temporal sequence alone.

## 10. Underground occupancy

Subsurface places may be active worlds before the player arrives.

```yaml
underground_occupancy:
  occupancy_id: null
  site_id: null
  actor_or_collective_ids: []
  occupancy_type: null
  core_area_ids: []
  observed_route_ids: []
  resource_dependency_ids: []
  disturbance_history_ids: []
  interaction_history_ids: []
```

Candidate occupancy types:
- WILD_HABITAT
- NESTING
- ROOSTING
- FORAGING
- HUMAN_WORKSITE
- RESEARCH_CAMP
- ABANDONED_INFRASTRUCTURE
- TEMPORARY_SHELTER

A Pokémon group occupying a cave is not automatically guarding human treasure.

## 11. Subsurface connection graph

Underground routes need their own connection state because entrances can change independently of surface roads.

```yaml
subsurface_connection:
  connection_id: null
  from_site_id: null
  to_site_id: null
  access_state: unknown
  known_to_actor_ids: []
  route_observation_ids: []
  support_asset_ids: []
  water_intersection_ids: []
  collapse_event_ids: []
  traversal_requirement_refs: []
```

This can support:
- forgotten shafts;
- flooded passages;
- mine-cart corridors;
- caves intersecting basements or dungeons;
- emergency exits;
- geological shortcuts.

Traversal requirements must use validated PTU/Caelo capabilities and future Minecraft support.

## 12. Worksite versus dungeon

A mine or quarry does not become a dungeon because it has enemies.

A worksite can have:
- shifts;
- equipment;
- restricted zones;
- staff handoffs;
- maintenance;
- storage;
- evacuation routes;
- active production.

A dungeon state machine is appropriate when the place has persistent exploration progression, locked access, hazards, puzzle state, encounter progression or significant return-state memory.

A place may be both, but the two layers remain separate.

## 13. Geological profession hooks

Potential narrative roles:
- surveyor;
- miner;
- quarry worker;
- paleontology researcher;
- fossil preparator;
- museum technician;
- cave guide;
- geotechnical inspector;
- rescue specialist;
- infrastructure engineer;
- underground ecologist;
- conservation steward.

These are narrative roles only.

They do not grant Skills, Edges, Features or bonuses without governing PTU/Caelo rules.

## 14. Site knowledge

Different actors can know different underground maps.

```yaml
site_knowledge:
  actor_id: null
  site_id: null
  known_connection_ids: []
  known_resource_claim_ids: []
  known_hazard_claim_ids: []
  known_context_ids: []
  source_refs: []
  last_updated: null
```

An old mine map may be accurate for the year it was made and still be dangerous today.

Knowledge should become stale when collapse, flooding, construction or excavation changes the site.

## 15. Ownership, access and claims boundary

Do not assume modern mineral rights, private-property law, public ownership or claim-staking systems.

Represent claims separately:

```yaml
site_claim:
  claim_id: null
  claimant_id: null
  site_or_resource_id: null
  claim_type: null
  source_record_ids: []
  recognized_by_ids: []
  disputed_by_ids: []
  current_state: asserted
```

Canon must later define what kinds of claims exist in each region.

## 16. Restoration and repurposing

Closed extraction sites can become:
- research reserves;
- water storage;
- museums;
- public routes;
- Pokémon habitat;
- emergency shelters;
- heritage sites;
- training grounds;
- permanently closed dangerous areas.

Restoration should preserve history rather than reset the location to an untouched state.

## 17. Anti-grind policy

Narrative geology must not become mandatory repetitive mining.

Compress routine extraction when:
- site is known and stable;
- authorization/access is settled;
- nothing meaningful changes;
- mechanical harvesting is already resolved elsewhere.

Expand into playable content when:
- a new context is discovered;
- site conditions change;
- access becomes contested;
- habitat is disturbed;
- equipment or staffing fails;
- an unusual fossil/resource appears;
- a scientific question emerges;
- a route opens/closes;
- a public discovery boom starts;
- player decisions can cause persistent consequences.

## 18. Minecraft representation

Potential world expressions:
- marked geological layers;
- persistent excavated chambers;
- scaffolding/support structures;
- mine carts/rails;
- survey markers;
- museum displays;
- fenced research areas;
- blocked shafts;
- flooded tunnels;
- abandoned equipment;
- visible restoration/revegetation;
- NPC work crews;
- wild Pokémon reclaiming old workings.

Narrative state should not require preserving every mined block forever if that is technically expensive.

High-significance contexts and access changes deserve persistence first.

## 19. Encounter contract requirements

Any underground encounter that depends on environmental mechanics must declare exact capability dependencies.

Never turn Minecraft blocks into PTU rules scripts merely because the engine family is missing.

### Encounter A — Collapsed Survey Gallery

Narrative premise:
A survey team exposes a new chamber shortly before part of the access gallery fails. Players must determine whether the chamber can be reached safely while wild Pokémon displaced by the disturbance remain nearby.

FULL version dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if unstable edges or rescue movement are tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for collapse zones, debris or changing footing
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- RESCUE/REACH_SAFE_ZONE objective semantics: not verified

REDUCED version:
The unstable gallery is resolved as overworld state before battle creation. AutoPTU receives a fixed legal arena in a stable chamber. Any displaced Pokémon encounter uses ordinary combat/capture resolution. Access to the deeper context changes only after the authoritative encounter result plus a separate world-state decision.

### Encounter B — Fossil Bed Disturbance

Narrative premise:
A newly exposed fossil bed overlaps an active wild habitat. Different actors want immediate recovery, scientific documentation or temporary closure.

FULL version dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING only if interception/escort becomes tactical
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if fragile-context zones have tactical effects
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- PROTECT_CONTEXT/WITHDRAW objective semantics: not verified

REDUCED version:
The fossil context is outside the battle grid and cannot be damaged by battle simulation. Players resolve a standard encounter in an adjacent stable area. Documentation, closure and recovery choices happen as overworld/world-state decisions afterward.

### Encounter C — Flooded Lower Working

Narrative premise:
Water has entered an old lower mine level. A maintenance crew needs access to inspect a pump and determine whether the route can reopen.

FULL version dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED for supported tactical movement modes only
- complete movement/forced movement/interception: BLOCKING if currents or rescue movement matter
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for rising water, currents or pump-state zones
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- ACTIVATE_OBJECT/ESCAPE objective semantics: not verified

REDUCED version:
Water level and pump condition remain overworld state. The actual battle happens in a fixed dry platform/chamber. After battle, the maintenance decision can reopen, keep closed or escalate the site based on noncombat world-state evidence.

## 20. Permanent rules boundary

The narrative layer may record desired experiences such as:
- unstable cave;
- flooding;
- falling rocks;
- narrow ledges;
- poor air;
- geothermal heat;
- excavation machinery;
- fossil recovery;
- damaged supports.

It must not invent the mechanical implementation of those experiences.

Before entering AutoPTU they require authoritative validation for the exact PTU/Caelo rules and live engine categories involved.

## 21. No-inference rules

- A cave is not automatically a dungeon.
- A mine is not automatically environmentally harmful.
- A conservation restriction is not automatically correct or corrupt.
- A valuable deposit does not automatically belong to the finder.
- A fossil does not automatically belong to the person who excavated it.
- A fossil is not automatically revivable.
- A revived fossil Pokémon is not automatically owned by the discoverer.
- A rare mineral does not automatically have mechanical value.
- A collapse does not automatically imply negligence or sabotage.
- Wild Pokémon in a mine are not automatically pests.
- Pokémon near a fossil are not automatically guarding it.
- Digging capability in flavor text does not prove legal excavation mechanics.
- Ground-type or Rock-type does not grant mining permissions or hazard immunity.
- Java terrain-cost movement does not prove cave hazards.
- Status-phase progress does not prove gas, drowning, cave-in or environmental status handling.
