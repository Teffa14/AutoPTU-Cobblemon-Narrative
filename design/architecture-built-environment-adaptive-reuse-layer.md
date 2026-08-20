# Ouros Architecture, Built Environment & Adaptive Reuse Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.

Date: 2026-08-20

## Purpose

Ouros already models homes, neighborhoods, public works, infrastructure, transport, accessibility, conservation, archaeology and settlement change. This layer gives the physical built environment its own persistent identity.

A structure should be able to survive changes in use, ownership claims, institutions, damage, repairs, expansion and surrounding settlement form without losing its history.

The core rule is simple: Minecraft geometry represents current physical state. It does not become the authority for history, permissions or PTU mechanics.

## Core separation

Keep these states distinct:

```text
physical structure
  -> structure version
  -> current use
  -> condition
  -> access state
  -> occupants / steward institutions
  -> material and construction history
  -> architectural interpretation
  -> public memory
  -> tactical grid projection when battle begins
```

A visual style does not prove who built a structure.
A current occupant does not prove ownership.
A ruined building is not deleted history.
A narrow alley does not create a PTU movement penalty unless the tactical representation and rules support it.

## 1. Persistent structure identity

```yaml
built_structure:
  structure_id: null
  location_id: null
  settlement_id: null
  structure_type: null
  current_version_id: null
  current_use_ids: []
  condition_state: usable
  steward_ids: []
  occupancy_refs: []
  access_policy_refs: []
  infrastructure_refs: []
  heritage_refs: []
  source_refs: []
```

Suggested structure types are descriptive only: residence, civic building, market hall, station, warehouse, workshop, clinic, school, venue, tower, bridge, arcade, industrial building, religious/cultural site where canon supports it, ruin, fortification, service building, mixed-use block and other authored types.

## 2. Structure versions

Every important physical change creates a version instead of silently replacing the old state.

```yaml
structure_version:
  structure_version_id: null
  structure_id: null
  valid_from: null
  valid_until: null
  footprint_ref: null
  floor_count: null
  entrance_refs: []
  circulation_refs: []
  room_or_zone_refs: []
  material_refs: []
  accessibility_refs: []
  service_connection_refs: []
  visible_previous_layer_refs: []
  change_event_id: null
  confidence: confirmed
```

Possible changes include expansion, subdivision, fire damage, stabilization, reconstruction, conversion, demolition of one wing, new bridge connection, new courtyard, added public access, sealed basement, new roof use or removal of obsolete machinery.

Historical versions remain queryable.

## 3. Building use history

Use is separate from geometry.

```yaml
structure_use_period:
  structure_id: null
  use_type: null
  institution_or_actor_ids: []
  start_event_id: null
  end_event_id: null
  public_name: null
  evidence_refs: []
```

A depot can become a market without ceasing to have been a depot.
An old clinic can later become housing.
A warehouse can become a club headquarters.
A closed school can become a crisis shelter.

Adaptive reuse should preserve useful traces of prior functions where world state supports them.

## 4. Condition state

Condition is coarse world state, not automatic tactical damage.

Suggested states:

- intact;
- maintained;
- worn;
- degraded;
- partially_damaged;
- unsafe_pending_review;
- stabilized;
- abandoned;
- ruin;
- under_repair;
- under_conversion;
- reconstructed.

```yaml
structure_condition_record:
  structure_id: null
  observed_at: null
  condition_state: null
  affected_zone_refs: []
  observation_refs: []
  engineering_claim_refs: []
  access_change_refs: []
  repair_project_refs: []
```

A visible crack does not automatically prove structural danger.
A building marked unsafe by an institution is an institutional decision, not a PTU status effect.

## 5. Settlement morphology

Ouros should describe settlement form at a coarse level so places feel spatially different before decorative detail is added.

```yaml
settlement_morphology:
  settlement_id: null
  morphology_version_id: null
  street_pattern_tags: []
  block_pattern_tags: []
  density_band: null
  verticality_band: null
  public_space_refs: []
  major_landmark_ids: []
  edge_condition_refs: []
  terrain_relationship_tags: []
  district_refs: []
```

Possible authored tags:

- irregular_lanes;
- regular_grid;
- linear_harbor;
- terraced_slope;
- ridge_spine;
- dispersed_compounds;
- courtyard_blocks;
- arcaded_commercial_streets;
- canal_or_waterfront_edges;
- walled_core;
- radial_landmark_focus.

These tags guide Minecraft generation and navigation. They do not import real-world architecture wholesale.

## 6. District identity

Districts should emerge from use, morphology and history rather than only color palette.

```yaml
district_state:
  district_id: null
  settlement_id: null
  current_name: null
  prior_name_refs: []
  morphology_ref: null
  predominant_use_refs: []
  landmark_refs: []
  service_refs: []
  resident_group_refs: []
  ecological_edge_refs: []
  public_memory_refs: []
```

A district may gradually change from industrial to mixed-use, residential to institutional, or port-service to cultural without every building changing at the same time.

## 7. Landmarks and spatial memory

```yaml
landmark_identity:
  landmark_id: null
  structure_or_place_id: null
  recognition_scope: local
  current_name: null
  former_name_refs: []
  physical_state: null
  associated_event_refs: []
  navigation_role: null
  public_memory_refs: []
```

A landmark may survive physical transformation.

Examples:
- a tower loses its original function but remains the orientation point for a district;
- a burned hall survives only as foundations and a plaza name;
- an old bridge is replaced but its route remains the same crossing;
- a market relocates but residents still use the older building name for the block.

## 8. Adaptive reuse

Adaptive reuse is a first-class transformation.

```yaml
adaptive_reuse_project:
  project_id: null
  structure_id: null
  prior_use_refs: []
  proposed_use_refs: []
  retained_feature_refs: []
  removed_feature_refs: []
  new_feature_refs: []
  accessibility_changes: []
  infrastructure_changes: []
  heritage_constraints: []
  ecological_constraints: []
  civic_project_refs: []
  status: proposed
```

A reuse project can fail, stall, change scope or produce an unexpected new use.

## 9. Architecture as evidence

Built form may produce observations without automatically proving a historical theory.

Examples:
- blocked doorway;
- mismatched foundation;
- later masonry around an older opening;
- obsolete platform height;
- hidden service corridor;
- patched roofline;
- different construction phases.

Store observation separately from interpretation.

```yaml
architectural_observation:
  observation_id: null
  structure_id: null
  structure_version_id: null
  observed_feature: null
  location_ref: null
  evidence_refs: []
  interpretation_claim_ids: []
```

This connects to archaeology, archives, photography and case evidence.

## 10. Architecture and ecology

Buildings can create habitat edges without becoming generic Pokémon spawn machines.

Possible world-state relationships:

- nesting on roofs;
- roosting under bridges;
- drainage-channel habitat;
- abandoned industrial hall used as shelter;
- market waste attracting scavengers;
- green roofs or courtyards creating new cover;
- lighting changing nocturnal activity;
- demolition temporarily disturbing a local population.

Ecological effects must use evidence from the conservation, observation and wild-collective layers.

## 11. Accessibility and circulation

The built environment should reference the accessibility layer rather than invent movement penalties.

A structure can record:
- step-free route availability;
- elevator/lift operational state;
- stairs;
- narrow passages;
- alternate entrance;
- temporary obstruction;
- signage state;
- quiet/rest areas;
- emergency egress.

Minecraft collision and door state are presentation/enforcement tools. They are not a substitute for the authored access model.

## 12. Structure lifecycle

Suggested lifecycle:

```text
planned
  -> constructed
  -> occupied
  -> altered
  -> maintained / degraded
  -> repaired / expanded / converted
  -> abandoned / damaged
  -> stabilized ruin / demolished / reconstructed
```

The lifecycle can branch.

Demolition should write a successor state instead of deleting provenance.

## 13. Minecraft representation contract

Minecraft should represent:

- current geometry;
- visible retained layers;
- doors and passages consistent with current access state;
- signs and public names;
- construction/repair phases;
- district morphology;
- world-state variants;
- stable structure IDs attached to persistent records.

Minecraft should not independently decide:

- ownership;
- historical truth;
- structural safety;
- whether a ruin is archaeologically significant;
- whether an architectural style proves cultural origin;
- PTU cover or terrain effects;
- building-collapse damage;
- legal access.

## 14. Battle projection

When combat begins inside or around a structure, generate a tactical projection from a frozen world-state version.

```yaml
structure_battle_projection:
  structure_id: null
  structure_version_id: null
  battle_instance_id: null
  grid_geometry_ref: null
  blocker_refs: []
  entrance_exit_refs: []
  elevation_refs: []
  authored_terrain_effect_refs: []
  destructible_refs: []
  frozen_at: null
```

Only already-verified rules enter the tactical projection.

A staircase can become static walkable geometry if supported.
A wall can become a blocker.
A collapsing balcony cannot deal damage unless the hazard family is verified and the exact effect is legal.

## 15. Capability dependencies

Architecture-heavy encounters may depend on:

- targeting / footprints / range / LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- action economy / initiative;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

The permanent engine readiness snapshot remains authoritative for the current state.

## 16. Reduced-version policy

Narrative premises should survive missing tactical features.

Examples:

Full version:
A damaged arcade has falling debris, shifting blockers and civilians moving toward exits.

Reduced version:
Evacuation and structural movement resolve as overworld state before battle. AutoPTU receives one stable arena version with fixed blockers.

Full version:
A bridge repair encounter includes knockback danger near an open edge.

Reduced version:
Edge tiles are simply blocked during battle until forced movement and fall interactions are verified.

## 17. Generation rules

A generated architectural hook must come from existing state such as:

- building condition;
- use change;
- public works project;
- historic floor plan;
- accessibility failure;
- district growth;
- infrastructure connection;
- ecological occupation;
- land-use conflict;
- tourism pressure;
- crisis damage;
- adaptive reuse proposal.

Do not generate random condemned buildings, secret tunnels or collapsing floors merely because a quest needs drama.

## 18. Canon promotion questions

Before a regional architectural grammar enters canon, review:

- which settlement histories are authored;
- which construction traditions are regionally established;
- which materials exist and are commonly available;
- which landmarks predate player arrival;
- which ruins are preserved;
- how accessibility is represented;
- how much player building is allowed;
- which structures can change physically at runtime;
- which tactical properties are actually supported by PTU/AutoPTU.

## Conclusion

The built environment becomes durable narrative state rather than scenery.

Ouros can then remember that a station became a market, a burned tower became a civic landmark, a warehouse became habitat, a street widened after a crisis, or a village slowly became a city. Minecraft renders the current layer. The Chronicle preserves how it got there.
