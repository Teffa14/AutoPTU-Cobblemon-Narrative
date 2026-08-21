# Ouros Decomposition, Fungi, Deadwood & Nutrient Cycling Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.

## Purpose

This layer gives dead organic material and decomposer activity persistent world state.

It connects Soil, Flora, Wildfire, Conservation, Interspecies Ecology, Science, Material Culture, Travel and Minecraft presentation without turning ecological observations into PTU battle effects.

The design target is a forest, wetland, orchard or urban green space where a fallen tree can remain relevant for years and change function over time.

## 1. Core separation

Never collapse these concepts:

```text
physical dead organic material
→ observed decay state
→ decomposer observations
→ ecological interpretation
→ habitat/resource consequence
→ soil/flora/world-state consequence
→ optional Minecraft projection
→ optional AutoPTU battle snapshot
```

A mushroom block/model is presentation.

A fungal fruiting observation is evidence.

A PTU Move or Ability such as Spore or Effect Spore is mechanical state.

Those concepts only connect through validated contracts.

## 2. Dead organic material object

Use persistent objects for ecologically or narratively meaningful material.

```yaml
dead_organic_object:
  dead_organic_id: null
  source_entity_or_vegetation_ref: null
  material_class: null
  location_id: null
  geometry_ref: null
  origin_event_ref: null
  entered_dead_state_at: null
  standing_or_down: null
  current_decay_revision_id: null
  soil_unit_ids: []
  vegetation_unit_ids: []
  habitat_use_refs: []
  decomposer_observation_ids: []
  route_interaction_refs: []
  heritage_or_memory_refs: []
  material_recovery_refs: []
  public_disclosure_state: normal
```

Candidate material classes:

- standing dead tree/snags;
- down log;
- stump;
- branch accumulation;
- root mass;
- leaf-litter patch;
- storm-fall cluster;
- post-fire killed wood;
- orchard pruning pile;
- aquatic woody debris;
- buried organic layer;
- narratively significant individual tree remains.

Do not create one persistent record for every leaf or Minecraft log block.

## 3. Decay revision

Decay changes through versioned state.

```yaml
decay_revision:
  revision_id: null
  dead_organic_id: null
  valid_from: null
  valid_to: null
  structural_integrity_state: unknown
  moisture_state: unknown
  bark_retention_state: unknown
  cavity_state: unknown
  surface_softness_state: unknown
  incorporation_into_soil_state: unknown
  visible_fungal_fruiting_state: unknown
  visible_invertebrate_activity_state: unknown
  other_decomposer_signal_state: unknown
  evidence_refs: []
  confidence: null
  supersedes_revision_id: null
```

These fields describe world state. They do not create tactical HP, cover values, movement costs or collapse checks.

## 4. Decomposition observation

Preserve what was actually observed.

```yaml
decomposition_observation:
  observation_id: null
  subject_ref: null
  observed_at: null
  observer_ids: []
  observation_type: null
  measured_value: null
  measurement_unit: null
  weather_context_id: null
  season_context_id: null
  image_record_ids: []
  sample_object_ids: []
  method_ref: null
  notes: null
  provenance_refs: []
```

Useful observation types:

- FRUITING_BODY_PRESENT
- FRUITING_BODY_ABSENT
- WOOD_SOFTNESS
- CAVITY_PRESENT
- BARK_LOSS
- MOISTURE
- MASS_OR_VOLUME_ESTIMATE
- INVERTEBRATE_ACTIVITY
- FUNGAL_GROWTH_SIGNAL
- ROOT_ASSOCIATION_SIGNAL
- ODOR_SIGNAL
- COLOR_CHANGE
- SOIL_INCORPORATION
- SHELTER_USE
- FEEDING_USE
- NESTING_OR_ROOST_USE

Absence of visible mushrooms does not prove absence of fungi.

## 5. Fungal occurrence versus ecological role

```yaml
fungal_occurrence_record:
  fungal_occurrence_id: null
  location_id: null
  substrate_ref: null
  observed_morphology_ref: null
  identification_state: unknown
  probable_species_or_group_refs: []
  confirmed_species_or_group_refs: []
  fruiting_window_ref: null
  sample_refs: []
  image_refs: []
  role_hypothesis_ids: []
  evidence_refs: []
```

Possible role hypotheses include:

- SAPROTROPHIC_DECOMPOSER
- MYCORRHIZAL_ASSOCIATION
- PATHOGENIC_ASSOCIATION
- COMMENSAL_OR_NEUTRAL_ASSOCIATION
- POKEMON_ASSOCIATED
- UNKNOWN

A mushroom shape is not enough to identify the role.

## 6. Fungal/root association

```yaml
root_fungal_association:
  association_id: null
  vegetation_unit_id: null
  plant_or_tree_refs: []
  fungal_group_refs: []
  observation_refs: []
  evidence_state: hypothesized
  nutrient_exchange_claim_ids: []
  water_exchange_claim_ids: []
  alternative_explanations: []
  review_due_at: null
```

Critical rule: ecological exchange is not telepathy.

This layer cannot create:

- shared thoughts;
- psychic communication;
- shared memories;
- Aura links;
- Pokémon command authority;
- faction-wide knowledge.

Those require the dedicated psychic/communications systems and exact governing mechanics.

## 7. Decomposer activity profile

Use coarse activity rather than simulating every organism.

```yaml
decomposer_activity_profile:
  profile_id: null
  location_id: null
  substrate_refs: []
  season_ref: null
  moisture_context_ref: null
  temperature_context_ref: null
  observed_activity_state: unknown
  fungal_activity_refs: []
  invertebrate_activity_refs: []
  pokemon_activity_refs: []
  evidence_refs: []
```

This state can help explain why the same material decays at different rates between places or years.

It is not a deterministic countdown to disappearance.

## 8. Nutrient-return record

Nutrient cycling should be represented as evidence-backed ecological state, not a free farming bonus.

```yaml
nutrient_return_record:
  record_id: null
  source_dead_organic_ids: []
  receiving_soil_unit_ids: []
  receiving_vegetation_unit_ids: []
  observation_refs: []
  assessment_refs: []
  nutrient_claims: []
  confidence: null
  valid_from: null
  valid_to: null
```

A record can support future Soil or Flora assessments.

It cannot directly:

- increase crop yield;
- restore HP;
- grant Food Buffs;
- produce Berries;
- create Grassy Terrain;
- change Pokémon stats.

## 9. Deadwood habitat use

A deadwood object can be a persistent ecological structure.

```yaml
deadwood_habitat_use:
  use_id: null
  dead_organic_id: null
  actor_or_collective_ref: null
  observed_use_type: null
  first_observed_at: null
  last_observed_at: null
  repeated_observation_count: null
  evidence_refs: []
  relation_edge_candidate_id: null
```

Candidate uses:

- SHELTER
- NESTING
- ROOSTING
- FORAGING
- FEEDING
- LOOKOUT
- HIDING
- CROSSING
- MOISTURE_REFUGE
- UNKNOWN

Repeated use may justify an Interspecies or habitat relation later. One observation does not prove dependence.

## 10. Deadwood management decision

Removing or retaining wood should be explicit.

```yaml
deadwood_management_record:
  management_id: null
  dead_organic_ids: []
  decision_actor_ids: []
  decision_type: null
  stated_reasons: []
  safety_assessment_refs: []
  ecological_assessment_refs: []
  route_or_access_refs: []
  cultural_or_memory_refs: []
  implementation_state: proposed
  outcome_observation_refs: []
```

Possible decisions:

- RETAIN_IN_PLACE
- PARTIAL_REMOVE
- RELOCATE_WITHIN_SITE
- REMOVE_FOR_SAFETY
- REMOVE_FOR_ACCESS
- TRANSFER_FOR_MATERIAL_USE
- CREATE_HABITAT_PILE
- LEAVE_FOR_RESEARCH
- UNKNOWN_OR_UNDECIDED

A visually tidy site is not automatically ecologically healthier.

## 11. Disturbance coupling

This layer consumes disturbance history from other systems.

Examples:

Wildfire → creates standing/down deadwood → decomposition starts → cavities appear → wildlife use changes → nutrient return changes → soil/flora observations change.

Storm → treefall → route blocked → Travel reroute → deadwood retained off-route → future habitat use.

Construction → selected removal → material transferred to Material Culture → remaining stump/root system persists ecologically.

Flood → aquatic woody debris relocates → Freshwater changes local geometry → later decomposition continues at new location.

No step should be inferred unless a state transition actually occurred.

## 12. Pokémon fungal ecology

Pokémon species can participate in this system through authored lore or observed behavior.

Examples supported by external research include mushroom-associated species occupying damp/dark forests, colonies, feeding relationships and spore-producing defenses.

The world layer may record:

- repeated occurrence near a substrate;
- colony location;
- feeding observations;
- cap/resource harvesting observations;
- response to moisture/season;
- interactions with other Pokémon.

It may not infer a Move, Ability or Status from visual resemblance.

## 13. Edible/harvestable fungal material

```yaml
fungal_harvest_observation:
  harvest_id: null
  occurrence_ref: null
  harvested_by_actor_id: null
  harvested_at: null
  amount_descriptor: null
  intended_use_claim: null
  custody_ref: null
  identification_state: unknown
  mechanical_item_ref: null
```

Unless `mechanical_item_ref` is resolved through authoritative PTU/Caelo/item rules, the object remains narrative material.

"Looks edible" does not create Food Item state.

## 14. Disease/outbreak boundary

Fungal occurrence does not create disease state.

If plants, Pokémon or people show symptoms:

1. Care/Outbreak layers record observations.
2. Science records hypotheses.
3. Pass 72 records fungal occurrence if observed.
4. A causal link requires evidence.
5. Mechanical disease/status effects require governing rules.

This protects against automatic "mushroom = infection" stories.

## 15. Seasonality

Fruiting bodies may be strongly seasonal even when the underlying fungal organism persists.

Therefore:

```text
fruiting body absent today
≠ fungus absent
≠ decomposition stopped
```

Seasonality owns expected calendar windows. Pass 72 owns observations and substrate-linked occurrence state.

## 16. Minecraft projection

Minecraft can present:

- fallen logs;
- standing snags;
- stump variants;
- mushrooms/fungal clusters;
- cavities;
- leaf litter;
- decayed texture variants;
- habitat piles;
- temporary scientific markers;
- protected/deadwood-retention signs.

The server-side Ouros state remains authoritative.

Loaded blocks must not become the sole source of truth for age, decay history, fungal identity or ecological function.

## 17. Battle projection

Battle projection must be frozen before AutoPTU starts.

Safe early projection:

- stable fallen logs as static blockers if geometry rules permit;
- fixed passable gaps;
- fixed arena boundaries;
- Pokémon already selected as combatants.

Do not project without verified mechanics:

- collapsing logs;
- spreading spores;
- automatic Sleep/Poison/Paralysis;
- evolving fungal zones;
- dynamic terrain costs;
- decomposer swarms entering mid-round;
- rotten floor collapse;
- toxic clouds;
- healing mushrooms;
- weather/terrain generated by fungal abundance.

## 18. PTU / Caelo boundary

Known project evidence exposes concrete mechanics named `Spore` and `Effect Spore`.

Those mechanics demonstrate the opposite of a generic environmental rule: when spores have a battle effect, the effect comes from an authored Move/Ability contract.

Primary Caelo text for fungal ecology was not reliably available during Pass 72. No Caelo-specific rule is added here.

## 19. Encounter implementation contracts

### Rot Log Passage

Narrative premise:
A frequently used forest trail is partly blocked by a large decaying trunk that has also become habitat. Players need to understand the site before deciding whether to clear, reroute or retain it.

FULL version:
- unstable sections may collapse only under verified environmental/hazard rules;
- wildlife can attempt withdrawal through alternate paths;
- changing obstruction state can alter legal routes;
- fungal effects can occur only if a specific Move/Ability/hazard contract authorizes them.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. forced movement/interception — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL if any actual damage exists
- status lifecycle — PARTIAL if a verified status effect is invoked
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:
Resolve trail assessment and management choice in overworld state. Freeze the trunk as static geometry. If combat occurs, use a legal static arena with no collapsing wood or ambient spore mechanics.

### Hollow Trunk Refuge

Narrative premise:
Several wild Pokémon repeatedly use a hollow dead tree during severe weather. A separate disturbance forces players to decide how to protect access to the refuge.

FULL version:
Requires protect/withdraw objective semantics, wildlife tactical policy, complete movement, zones/reactions and adapter playback.

REDUCED version:
Resolve refuge occupancy and evacuation outside battle. If a confrontation happens, keep noncombatants outside the grid and fight on fixed nearby terrain.

### Fruiting Survey

Narrative premise:
An unusually large mushroom fruiting event appears after a wet period. Researchers want observations before tourism and foraging erase the evidence.

FULL version:
Could eventually include validated environmental visibility/status effects only if exact PTU mechanics exist, plus moving visitors/wildlife and objective-aware AI.

REDUCED version:
Treat mushrooms, samples, visitors and survey targets as world state. Use an ordinary static encounter only if wild or hostile combatants independently create one. No ambient mushroom applies a battle status.

## 20. Long-term data flow

```text
disturbance event
→ persistent dead organic object
→ decay revisions
→ decomposer/fungal observations
→ habitat use / scientific interpretation
→ soil + flora + interspecies consequences
→ management choice
→ later observations
→ Chronicle callback
```

This gives Ouros long-term environmental memory without turning decomposition into a background simulator that runs every block every tick.

## 21. Promotion gate

Before any Pass 72 proposal becomes canon:

1. confirm the location and ecological premise fit Ouros;
2. verify any named Pokémon species against authored regional ecology;
3. review scientific claims and uncertainty;
4. resolve PTU/Caelo mechanics if any battle effect exists;
5. classify AutoPTU-Java dependencies;
6. verify Minecraft projection can preserve identity/history;
7. ensure no fungal observation is being used to invent telepathy, disease, Food Items or statuses;
8. keep original research provenance attached.
