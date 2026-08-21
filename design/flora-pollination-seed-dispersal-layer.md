# Ouros Flora, Pollination, Seed Dispersal & Vegetation Dynamics Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.

## Purpose

This layer gives vegetation its own persistent world state.

It sits between:

- Seasonality / Calendar / Phenology;
- Soil / Erosion / Restoration;
- Freshwater / Hydrology;
- Wildfire / Fire Ecology;
- Conservation / Stewardship;
- Food / Agriculture / Hospitality;
- Biosecurity / Introduced Species;
- Wild Collectives;
- Interspecies Ecological Relations;
- Science / Observation;
- Minecraft/Cobblemon presentation;
- AutoPTU battle projection.

The design target is a living landscape where flower availability, seed movement, disturbance, plant recruitment and Pokémon activity can create consequences over months and years without simulating every grass block.

## 1. Core separation

Never collapse these concepts:

```text
physical vegetation state
→ observed vegetation state
→ flowering/fruiting resource state
→ pollinator/visitor observations
→ seed-dispersal observations
→ ecological interpretation
→ management/restoration decision
→ world-state consequence
→ optional Cobblemon projection
→ optional AutoPTU battle snapshot
```

A Minecraft flower block is presentation.

A flowering resource patch is world state.

A PTU Grassy Terrain effect is battle state.

These are related only through validated contracts.

## 2. Vegetation unit

Do not model individual wild plants unless a specific plant is narratively important.

Use coarse persistent units.

```yaml
vegetation_unit:
  vegetation_unit_id: null
  location_id: null
  geometry_ref: null
  broad_community_type: null
  authored_species_refs: []
  uncertain_species_observations: []
  current_revision_id: null
  soil_land_unit_ids: []
  water_dependency_ids: []
  lightscape_ids: []
  fire_history_ids: []
  disturbance_ids: []
  management_project_ids: []
  sensitive_data: false
```

Examples:

- orchard block;
- meadow;
- riparian strip;
- wetland margin;
- roadside verge;
- woodland understory;
- alpine flower patch;
- urban garden;
- post-fire slope;
- abandoned field;
- dune vegetation band.

## 3. Vegetation revision

Vegetation changes through revisions rather than overwriting history.

```yaml
vegetation_revision:
  revision_id: null
  vegetation_unit_id: null
  valid_from: null
  valid_to: null
  structural_state:
    canopy: null
    shrub_layer: null
    herb_layer: null
    ground_cover: null
  broad_cover_state: null
  flowering_resource_state: null
  fruit_seed_resource_state: null
  recruitment_state: null
  disturbance_state: null
  confidence: null
  evidence_refs: []
```

These values are coarse on purpose.

Ouros should not maintain a per-block biomass simulation.

## 4. Plant community identity

A vegetation unit can contain multiple authored plant references or remain partially unidentified.

```yaml
plant_community_record:
  community_record_id: null
  vegetation_unit_id: null
  known_plant_refs: []
  probable_plant_refs: []
  unknown_morphotype_refs: []
  introduced_status_refs: []
  cultural_use_claim_ids: []
  ecological_role_claim_ids: []
  verified_at: null
```

Do not infer:

- native status from abundance;
- harmfulness from introduced status;
- medicinal effect from cultural use;
- PTU item identity from visual resemblance;
- Berry mechanics from a generic fruiting plant.

## 5. Flowering-resource window

```yaml
flowering_window:
  flowering_window_id: null
  vegetation_unit_id: null
  plant_refs: []
  expected_window_ref: null
  observed_start: null
  observed_peak: null
  observed_end: null
  nectar_resource_state: null
  pollen_resource_state: null
  evidence_refs: []
  anomaly_state: null
```

This integrates with Seasonality.

A late bloom is only anomalous if enough baseline exists.

## 6. Pollination interaction record

Pollination is an observed or inferred ecological interaction.

```yaml
pollination_interaction:
  interaction_id: null
  vegetation_unit_id: null
  plant_ref: null
  pokemon_entity_id: null
  pokemon_population_or_collective_id: null
  visitor_taxon_ref: null
  timestamp: null
  observation_type: null
  behavior_observed: null
  contact_with_flower_observed: null
  pollen_transfer_confirmed: null
  evidence_refs: []
  interpretation_refs: []
```

Possible observation types:

- NECTAR_FEEDING
- POLLEN_COLLECTION
- FLOWER_VISIT
- FLOWER_CONTACT
- POLLEN_CARRYING
- FRUIT_FEEDING
- UNKNOWN_VISIT

`FLOWER_VISIT` does not automatically mean successful pollination.

## 7. Pollination network

Use a graph when enough evidence accumulates.

```yaml
pollination_network:
  network_id: null
  region_or_site_id: null
  time_window: null
  plant_nodes: []
  visitor_nodes: []
  observed_edges: []
  inferred_edges: []
  resource_gaps: []
  confidence: null
```

This supports questions like:

- Which flowering resource disappears between early and late summer?
- Which Pokémon groups depend on a single corridor?
- Did restoration close a resource gap?
- Are two orchards relying on the same wild visitors?

It must not calculate crop yield unless a future validated rule/service explicitly owns that calculation.

## 8. Seed source and dispersal

```yaml
seed_source:
  seed_source_id: null
  plant_ref: null
  source_vegetation_unit_id: null
  source_batch_id: null
  provenance_state: null
  collection_event_id: null
  restoration_project_id: null
  genetic_or_locality_claim_ids: []
  custody_ids: []
```

```yaml
seed_dispersal_observation:
  dispersal_observation_id: null
  source_candidate_ids: []
  destination_vegetation_unit_id: null
  vector_type: null
  pokemon_entity_id: null
  pokemon_collective_id: null
  weather_event_id: null
  water_event_id: null
  human_transport_ref: null
  observed_seed_ref: null
  confidence: null
  evidence_refs: []
```

Candidate vector types:

- WIND
- WATER
- POKEMON
- HUMAN
- VEHICLE
- RESTORATION_PLANTING
- UNKNOWN

A newly established patch should not be assigned a source without evidence.

## 9. Recruitment and establishment

```yaml
plant_recruitment_event:
  recruitment_event_id: null
  vegetation_unit_id: null
  plant_ref: null
  first_observed_at: null
  establishment_state: null
  source_hypothesis_ids: []
  disturbance_context_ids: []
  soil_context_ids: []
  water_context_ids: []
  management_context_ids: []
  evidence_refs: []
```

Suggested states:

- NEW_OCCURRENCE
- GERMINATING
- ESTABLISHING
- ESTABLISHED
- DECLINING
- FAILED_TO_ESTABLISH
- UNKNOWN

Do not equate establishment with ecological benefit or harm.

Biosecurity handles introduced-status and impact assessment.

## 10. Vegetation disturbance

```yaml
vegetation_disturbance:
  disturbance_id: null
  vegetation_unit_id: null
  started_at: null
  ended_at: null
  disturbance_type: null
  cause_claim_ids: []
  verified_cause_ref: null
  physical_change_summary: null
  severity_state: null
  affected_layers: []
  followup_needed: true
```

Candidate disturbance types:

- FIRE
- FLOOD
- DROUGHT
- CONSTRUCTION
- TRAMPLING
- CUTTING
- GRAZING_OR_BROWSING
- STORM
- SEDIMENT_DEPOSITION
- EROSION
- POLLUTION
- FROST
- UNKNOWN

A disturbance can create habitat for some species while reducing it for others.

## 11. Succession trajectory

Do not use a deterministic ladder.

```yaml
succession_trajectory:
  trajectory_id: null
  vegetation_unit_id: null
  origin_disturbance_id: null
  baseline_revision_id: null
  observed_revision_ids: []
  candidate_future_states: []
  limiting_factor_refs: []
  intervention_ids: []
  trajectory_status: null
```

Candidate statuses:

- PASSIVE_RECOVERY
- ACTIVE_RESTORATION
- STALLED
- DIVERGING_FROM_EXPECTATION
- NOVEL_STABLE_STATE
- UNDER_REVIEW

Two sites with the same fire history may diverge because seed sources, water, soil, browsing or management differ.

## 12. Restoration project

Use the existing Conservation/Public Works project patterns but add plant-specific state.

```yaml
vegetation_restoration_project:
  project_id: null
  target_unit_ids: []
  baseline_revision_ids: []
  objective_refs: []
  seed_or_plant_source_ids: []
  planting_event_ids: []
  maintenance_schedule_refs: []
  pollinator_resource_objectives: []
  erosion_control_objectives: []
  habitat_objectives: []
  monitoring_plan_ref: null
  followup_revision_ids: []
  success_claim_ids: []
  review_state: null
```

A project is not successful merely because planting occurred.

Track follow-up.

## 13. Plant–Pokémon association

```yaml
plant_pokemon_association:
  association_id: null
  plant_or_community_ref: null
  pokemon_entity_or_population_ref: null
  relation_type: null
  evidence_refs: []
  region_ids: []
  season_refs: []
  confidence: null
```

Candidate relation types:

- NECTAR_USE
- POLLEN_USE
- SEED_DISPERSAL
- FRUIT_USE
- SHELTER
- NESTING_SUBSTRATE
- BROWSING
- TERRITORIAL_ASSOCIATION
- CULTIVATION_OR_GARDENING
- UNKNOWN

Do not humanize the relationship automatically.

## 14. Pokémon as ecological indicators

Pokémon behavior may provide evidence without providing certainty.

Examples:

- Cutiefly activity near a pre-bloom site;
- Butterfree concentrating around a remaining flower corridor;
- Eldegoss seed dispersal observed after a disturbance;
- Combee abandoning one foraging route;
- Budew opening earlier than the local historical range.

Store observation first.

Interpret later.

## 15. Agriculture integration

The Food/Agriculture layer already owns cultivated sites and production cycles.

This layer owns ecological vegetation processes around them.

Example:

```text
orchard cultivation cycle
+ wild flowering verge
+ observed Combee/Cutiefly visits
+ adjacent restored meadow
+ seasonal flowering gap
```

can create a field-research story.

It does not create a numerical crop-yield modifier unless an authoritative subsystem is added later.

## 16. Wildfire integration

Fire produces a disturbance record.

This layer tracks:

- surviving plant patches;
- seed-source distance;
- early recruitment;
- flowering return;
- competing trajectories;
- restoration plantings;
- later pollinator use.

Wildfire remains responsible for fire-event history and severity.

## 17. Soil integration

Soil condition can constrain vegetation establishment.

Vegetation can also affect:

- cover;
- erosion risk;
- organic input;
- infiltration context.

Do not automatically convert vegetation cover into PTU terrain.

## 18. Freshwater integration

Riparian and wetland vegetation can depend on water-regime events.

Hydrology owns water state.

This layer stores vegetation response.

Example:

```text
floodplain reconnection
→ seed transport event
→ new recruitment observations
→ flowering resource change next season
→ changed visitor activity
```

## 19. Light integration

Lightscape changes can alter flowering/phenology or pollinator activity only through authored/evidence-backed ecological transitions.

Minecraft block light must not directly alter plant state.

## 20. Biosecurity integration

A newly observed plant occurrence can open a Biosecurity case.

This layer stores:

- occurrence;
- recruitment;
- spread observations.

Biosecurity determines introduced/established/spreading/impact assessments.

## 21. Material and cultural use

Plants may become:

- food inputs;
- dyes;
- fibers;
- medicines where canon/rules establish them;
- ceremonial materials;
- craft materials;
- research specimens.

Provenance remains mandatory for significant instances.

Cultural meaning must be authored independently. Do not infer cultural use from real-world analogues.

## 22. Minecraft projection

Minecraft may render:

- coarse vegetation variants;
- flower density bands;
- regrowth stages;
- orchard rows;
- burned/recovering patches;
- restoration plots;
- seasonal appearance;
- seedling clusters;
- protected areas.

Minecraft must not own:

- ecological truth;
- plant provenance;
- pollination success;
- succession trajectory;
- crop yield;
- PTU terrain state;
- species rarity.

Loaded blocks/entities are a projection of server-owned state.

## 23. Cobblemon projection

Vegetation state may influence encounter/spawn projections only through a controlled server policy.

Forbidden direct mappings:

- add flowers → rare Bug/Fairy spawn;
- remove flowers → delete all pollinators;
- plant one tree → spawn nesting Pokémon;
- use bone meal → advance ecosystem state;
- torch field → force bloom;
- capture one pollinator → reduce regional pollination.

Allowed future flow:

```text
validated vegetation revision
→ validated ecological association
→ coarse population response
→ bounded encounter/spawn projection
```

## 24. PTU mechanical boundary

The narrative layer must not invent:

- Grassy Terrain;
- Grass-type bonuses;
- healing from flowers;
- pollen Status effects;
- Honey generation;
- Berry yields;
- Seed Bomb ammunition;
- Flower Veil effects;
- Harvest behavior;
- Naturewalk benefits;
- plant-generated cover;
- entanglement;
- Rough/Slow Terrain;
- poison from pollen;
- plant HP;
- wildfire resistance.

Any such effect requires exact PTU/Caelo/AutoPTU authority.

## 25. Engine capability dependencies

Permanent categories remain the only engine-wide labels.

For vegetation encounters, common dependencies are:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter & playback — BLOCKING

A field of flowers is not mechanically Grassy Terrain unless an authoritative battle projection says so.

## 26. Reduced-version policy

When the full concept requires dynamic vegetation or ecological objectives, use this order:

1. resolve vegetation/ecology state before combat;
2. freeze a legal static battle map;
3. include only actual combatants;
4. keep nests, seedlings, equipment and civilians outside the grid unless supported;
5. apply no plant-derived bonuses or hazards without exact rules;
6. write battle results back to world state conservatively.

## 27. Encounter contract — Bloom Corridor Disturbance

Narrative premise:

A flowering corridor used by multiple Pokémon groups is disrupted during a short seasonal window.

Full version requires:

- targeting/range/LoS — VERIFIED
- base movement — VERIFIED
- complete movement/interception — BLOCKING if actors attempt to cross/withdraw
- core calculations — VERIFIED
- initiative — VERIFIED
- lifecycle — PARTIAL
- damage — PARTIAL
- statuses — PARTIAL if exact effects appear
- terrain/weather/zones/reactions — BLOCKING if flowers become mechanical terrain or weather changes the fight
- move behavior — PARTIAL
- abilities/items/Features — PARTIAL
- legal-action AI — VERIFIED
- tactical AI — BLOCKING for protect/cross/withdraw goals
- adapter/playback — BLOCKING

Reduced version:

Resolve corridor access and noncombatant movement in overworld. Freeze one static map with flowers as visual scenery only. If a battle starts, use ordinary legal combat. Update the vegetation disturbance record afterward based only on explicit actions.

## 28. Encounter contract — Seed Bank Recovery

Narrative premise:

After a disturbance, researchers try to recover documented seed material while wild Pokémon also use the site.

Full version:

Requires interactable objectives, protected items, movement goals and tactical AI. These are not broadly verified.

Reduced version:

Keep seed samples and custody outside the grid. Resolve search/collection before or after battle. If a confrontation occurs, fight on a static legal arena and do not let attacks automatically destroy samples.

## 29. Encounter contract — Orchard Edge Foraging Conflict

Narrative premise:

Wild flower/nectar users shift toward an orchard edge after another resource patch declines.

Full version:

Could eventually use dynamic withdrawal, protected crop zones, goal-aware wild AI and validated environmental interactions.

Reduced version:

Use world state to determine where the animals are and why. Allow social/observation/relocation solutions first. If combat occurs, project only combatants onto a static arena. Do not apply crop damage or pollination bonuses automatically.

## 30. Chronicle writeback

After relevant events, Chronicle may store:

- vegetation revisions;
- flowering anomalies;
- observed visitor interactions;
- seed-source hypotheses;
- restoration interventions;
- recruitment events;
- disturbance causes when confirmed;
- changes in public or institutional interpretation;
- future callback hooks.

Do not write an inferred ecological relationship as fact without sufficient evidence.

## 31. Human review gates

Human/canon review is required before defining:

- major regional plant communities;
- culturally important plants;
- rare/endemic flora;
- sacred or protected plant sites;
- economically dominant crops;
- medicinal effects;
- PTU mechanical effects;
- Legendary/Mythical causes;
- permanent ecosystem transformations with regional scope.

## 32. Implementation blockers outside battle core

```text
OVERWORLD_VEGETATION_UNIT_STATE = BLOCKING
OVERWORLD_VEGETATION_REVISION_HISTORY = BLOCKING
OVERWORLD_FLOWERING_RESOURCE_WINDOWS = BLOCKING
OVERWORLD_POLLINATION_OBSERVATION_GRAPH = BLOCKING
OVERWORLD_SEED_SOURCE_PROVENANCE = BLOCKING
OVERWORLD_SEED_DISPERSAL_GRAPH = BLOCKING
OVERWORLD_PLANT_RECRUITMENT_STATE = BLOCKING
OVERWORLD_SUCCESSION_TRAJECTORY = BLOCKING
OVERWORLD_RESTORATION_MONITORING = BLOCKING
OVERWORLD_FLORA_TO_SEASONALITY = BLOCKING
OVERWORLD_FLORA_TO_SOIL = BLOCKING
OVERWORLD_FLORA_TO_FRESHWATER = BLOCKING
OVERWORLD_FLORA_TO_BIOSECURITY = BLOCKING
OVERWORLD_FLORA_TO_COBBLEMON = BLOCKING
OVERWORLD_FLORA_TO_BATTLE = BLOCKING
OVERWORLD_FLORA_TO_MINECRAFT = BLOCKING
```

These belong to the persistent-world layer, not AutoPTU-Java battle rules.

## 33. Anti-exploit rules

Players must not be able to force ecological state by cheap block manipulation.

Examples:

- planting hundreds of Minecraft flowers does not create a verified restored meadow;
- harvesting/replacing blocks does not reset provenance;
- bone meal does not fast-forward succession;
- moving a hive-like decorative block does not move a wild collective;
- despawning an Eldegoss does not erase a seed-dispersal event;
- clearing loaded vegetation does not instantly remove regional habitat state.

## 34. Design principle

Vegetation should create stories because it changes over time and connects other systems.

The important question is rarely “how many flowers are here?”

Better questions are:

- Which resources exist now that did not exist last season?
- What failed to bloom?
- Which species stopped visiting?
- Where did this new patch come from?
- Did a restoration project actually establish?
- Which old disturbance is still shaping the site?
- What does the community believe about the change?
- What evidence would change that belief?
