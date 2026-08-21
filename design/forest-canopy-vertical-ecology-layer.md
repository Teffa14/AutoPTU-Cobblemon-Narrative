# Forest canopy, arboreal habitat & vertical ecology layer

Status: PROPOSED SYSTEM DESIGN. Not canon.

## Purpose

This layer gives forests persistent vertical structure without turning Minecraft leaves and logs into the authority for ecology or PTU movement.

It connects Flora, Wild Collectives, Interspecies Ecology, Decomposition, Light, Soundscapes, Wildfire, Soil, Travel, Cartography, Conservation, Architecture and future Minecraft projection.

The central separation is:

```text
forest stand / persistent trees
        ↓
vertical structure + cavities + gaps + branch connectivity
        ↓
observations / habitat use / access state
        ↓
player and institutional knowledge
        ↓
optional encounter projection
        ↓
validated AutoPTU battle snapshot
```

A tree rendered in Minecraft does not automatically create PTU cover, climbability, Rough Terrain or a legal elevation.

## Core objects

### FOREST_VERTICAL_UNIT

A coarse persistent forest unit.

```yaml
forest_vertical_unit_id: null
location_id: null
forest_type: null
vertical_profile_revision_id: null
persistent_tree_ids: []
canopy_gap_ids: []
branch_network_ids: []
cavity_ids: []
flora_unit_ids: []
deadwood_ids: []
lightscape_id: null
soundscape_id: null
wild_collective_refs: []
research_refs: []
canon_status: proposed
```

The unit can be one grove, old-growth patch, riparian strip, orchard edge or urban tree corridor. It should not be one object per chunk.

### VERTICAL_PROFILE_REVISION

A versioned description of forest structure.

```yaml
vertical_profile_revision_id: null
forest_vertical_unit_id: null
valid_from: null
valid_to: null
emergent_layer_state: unknown
upper_canopy_state: unknown
midstory_state: unknown
understory_state: unknown
forest_floor_state: unknown
canopy_closure_class: null
vertical_complexity_class: null
observation_refs: []
supersedes: null
```

These are ecological layers, not battle elevations.

### PERSISTENT_TREE

Only trees with narrative/ecological importance need individual identity.

```yaml
persistent_tree_id: null
location_id: null
species_or_type_status: unknown
first_recorded_at: null
condition_revision_ids: []
cavity_ids: []
branch_network_refs: []
nesting_refs: []
epiphyte_refs: []
landmark_refs: []
material_provenance_refs: []
chronicle_refs: []
current_state: STANDING
```

Suggested states:
- STANDING
- DAMAGED
- SNAG
- FALLEN
- REMOVED
- UNKNOWN

A tree can move from `FALLEN` into the Decomposition layer while retaining the same provenance lineage.

### CANOPY_GAP

A persistent opening created by tree fall, fire, construction, management or unknown cause.

```yaml
canopy_gap_id: null
forest_vertical_unit_id: null
created_at: null
cause_status: UNKNOWN
cause_refs: []
geometry_class: null
light_change_refs: []
regeneration_refs: []
invasive_pressure_refs: []
habitat_use_refs: []
closure_history: []
```

A gap is not automatically damage or a problem. Its consequences depend on baseline state.

### TREE_CAVITY

A persistent habitat/structure feature.

```yaml
tree_cavity_id: null
persistent_tree_id: null
height_class: null
size_class: null
origin_status: UNKNOWN
origin_refs: []
occupancy_observations: []
condition_history: []
access_notes: []
```

Possible origins include natural decay, branch loss, known species behavior or unknown processes. A cavity does not prove nesting, ownership or current occupancy.

### BRANCH_CONNECTIVITY_NETWORK

A coarse graph for arboreal route structure.

```yaml
branch_network_id: null
forest_vertical_unit_id: null
node_refs: []
edge_refs: []
version: null
observed_by: []
access_confidence: null
last_verified_at: null
```

Edges may represent neighboring crowns, rope bridges, platforms or authored natural connections. This graph is for world navigation and ecology. It is not directly a PTU movement graph.

### ARBOREAL_HABITAT_USE

An observation that an individual or collective used a vertical feature.

```yaml
arboreal_habitat_use_id: null
actor_or_population_ref: null
feature_ref: null
observed_at: null
use_type: null
observer_refs: []
evidence_refs: []
interpretation_status: OBSERVED
```

Possible `use_type` values:
- RESTING
- FORAGING
- NESTING_OR_DENNING
- TRANSIT
- DISPLAY
- SHELTER
- UNKNOWN

Observation of use must not infer ownership, kinship, permanent residence or desire to be captured.

### CANOPY_ACCESS_STATE

A world-facing access record.

```yaml
canopy_access_state_id: null
scope_ref: null
valid_from: null
access_type: null
physical_state: null
service_or_bridge_refs: []
known_route_refs: []
capability_validation_required: true
```

This can describe a maintained walkway, observation platform, rope bridge, ladder or research canopy tower. Natural traversal by Pokémon/Trainers requires authoritative capability checks.

## Causal integrations

### Flora → vertical structure

Flora owns plant identity, flowering, recruitment and succession.

This layer owns vertical arrangement and the forest-structure consequences of those changes.

A new sapling cohort does not immediately create midstory. A canopy tree falling can create a gap without deciding which species will replace it.

### Light → canopy response

Light owns lightscape state.

A canopy gap can change measured/observed light below. That may then affect Flora state over time. The layer must not jump directly from `gap created` to `seedlings grow`.

### Decomposition → tree lineage

A fallen persistent tree keeps identity/provenance while its physical role changes. Decomposition owns decay stages, fungi, deadwood and nutrient return.

### Wild Collectives → visible subgroup

A group in the upper canopy may be a foraging party or partial subgroup. Never assume the visible Pokémon are the whole local population.

### Soundscapes → vertical acoustic observations

Calls may be detected at one height or layer more strongly than another. Soundscape observations can help infer presence but do not create exact positions automatically.

### Travel → elevated infrastructure

Maintained canopy bridges and platforms are transport infrastructure. Travel owns service/route viability. Architecture owns constructed versions.

Natural branch travel remains separate and capability-gated.

### Cartography → multi-layer maps

Maps may contain ground routes, canopy walkways and observation points as separate layers. A ground map does not automatically reveal canopy connectivity.

### Conservation → habitat decisions

Cavities, old trees, snags and canopy gaps can become stewardship concerns. Conservation decides management designations; this layer provides structure/evidence.

### Wildfire / storm disturbance

Wildfire or severe weather can create canopy gaps, damaged crowns, snags and fallen trees. Those systems create the event; this layer records the structural result.

## Multi-height observation rule

A forest observation should record the layer where possible.

Example:

```yaml
observation:
  forest_vertical_unit_id: grove_07
  vertical_layer: UPPER_CANOPY
  species_or_actor_ref: unknown_small_flying
  observed_at: 06:10
  confidence: medium
```

One layer cannot be used as a proxy for all layers.

`no sightings at forest floor` does not mean `species absent from forest`.

## Persistent-tree rule

Most Minecraft trees remain scenery.

Promote a tree to `PERSISTENT_TREE` only when at least one condition applies:
- authored landmark;
- repeated habitat use;
- nesting/cavity importance;
- archaeological/cultural significance;
- player-caused structural change;
- infrastructure connection;
- long-term research value;
- major storm/fire damage;
- future callback value.

This prevents state explosion.

## Vertical-settlement rule

A settlement may occupy several height layers.

The world model should preserve:
- ground access;
- platforms/bridges;
- building elevation;
- public versus restricted routes;
- emergency egress;
- maintenance state;
- ecological impacts below/around the structures.

A treetop district should be a real settlement layer, not merely a visual skin.

## Minecraft projection

Minecraft can express:
- visible canopy density;
- landmark trees;
- platforms and bridges;
- cavities or hollows;
- fallen trees;
- observation towers;
- canopy gaps;
- layer-specific ambient Pokémon presentation.

Minecraft must not be authoritative for:
- actual tree age;
- cavity occupancy history;
- ecological layer classification;
- branch route legality;
- nesting status;
- PTU climb/jump/fall rules;
- concealment or battle visibility;
- current population abundance.

Loaded entities are presentation, not population truth.

## Battle projection boundary

Before AutoPTU starts, the world server may produce an immutable encounter projection containing only validated features.

Possible future projection fields:

```yaml
battle_projection:
  map_id: null
  frozen_geometry_version: null
  elevation_tags: []
  static_blockers: []
  validated_climb_or_jump_edges: []
  validated_environment_tags: []
  source_world_state_refs: []
```

Until Java has authoritative elevation/vertical movement semantics, the recommended reduced version is a 2D arena representing one selected forest layer.

## PTU/Caelo guardrails

Do not infer mechanics from ecology or visuals.

A Pokémon being seen in a tree does not automatically grant:
- Sky movement;
- Levitate;
- Wallrunner;
- Naturewalk;
- extra Jump;
- fall immunity;
- cover;
- concealment;
- surprise;
- branch-to-branch movement.

A Trainer being physically able to reach a canopy walkway does not prove combat movement between elevations.

The Python oracle contains exact named interactions involving forest terrain, Naturewalk labels and some forest-specific effects. Those remain narrow rule implementations and cannot be generalized.

Exact climbing, falling, elevation, Naturewalk (Forest), Jump, Sky, Levitate, Wallrunner and vertical-LoS rules require PTU/Caelo validation before implementation.

## Encounter implementation contracts

### Canopy Bridge Failure

Narrative premise: an elevated public route is damaged while wild Pokémon continue using nearby crowns.

Full version intends:
- several elevations;
- bridge gaps;
- safe/unsafe crossing edges;
- rescue/protect or reach-exit objectives;
- Pokémon able to use legal alternative movement modes;
- possible falling/forced movement consequences only if exact rules exist;
- objective-aware AI.

Permanent capability dependencies:
- targeting/footprints/range/LoS: VERIFIED baseline, but vertical LoS unverified;
- base movement legality: VERIFIED baseline;
- complete movement incl. forced movement/interception: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full lifecycle: PARTIAL;
- damage: PARTIAL;
- statuses: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal actions: VERIFIED;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

Reduced version: resolve bridge damage, evacuation and route choice in overworld state. Select one stable platform/clearing as a static battle map if combat occurs. Do not simulate falling.

### Hollow Tree Care Call

Narrative premise: repeated activity around a large cavity leads to a care/investigation scene.

Full version intends layered access, cavity occupancy, non-KO protection/withdrawal goals and potentially limited vertical traversal.

Reduced version: reach the cavity through overworld exploration; determine occupancy and care state outside battle; if a defensive encounter happens, freeze a single ground/platform arena and keep the patient/nest outside the grid.

### Gap Survey After Storm

Narrative premise: a storm-created canopy gap changes light, access and observed wildlife use.

Full version could later include elevated observation positions and multiple traversal levels.

Reduced version is primarily research/exploration. Any battle uses a static clearing with no invented canopy buffs, falling branches or concealment penalties.

## Anti-exploit rules

- Breaking a Minecraft tree does not automatically change regional encounter tables.
- Placing leaf blocks does not create canopy habitat.
- Building a tower does not grant valid survey data.
- Repeatedly loading/unloading chunks does not create cavity occupancy or migration.
- Players cannot farm rare spawns by creating artificial canopy gaps unless a future authored ecology rule explicitly supports that causal chain.

## Open questions

- Which Ouros regions contain forests with strong vertical identity?
- Which trees are old enough or culturally important enough to be persistent entities at game start?
- Will any settlement use maintained canopy infrastructure?
- How should Minecraft store branch/crown connectivity without per-leaf canonical state?
- Does the future tactical engine remain one 2D layer per encounter, support discrete elevations, or eventually support true 3D adjacency?
- What exact PTU/Caelo rules govern climbing, jumping, falling and vertical attacks?
- Which Pokémon species have authored canopy-layer associations in each region rather than generic type-based assumptions?