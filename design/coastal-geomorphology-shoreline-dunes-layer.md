# Coastal Geomorphology, Shoreline & Dunes Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanic is established by this document.

Pass: 80

## Purpose

This layer gives open-coast physical change a persistent identity.

It owns shoreline revisions, beach and dune condition, barrier-island change, overwash, breaches, cliff retreat, coarse sediment movement and the provenance of restoration/nourishment work.

It exists between systems that already model the sea, weather, soil, geology, infrastructure, tourism and ecology.

## Authority boundary

This layer does not replace:

- Maritime for sea lanes, harbors, vessels, marine access and submerged locations;
- Estuaries for salinity, tidal wetlands, marsh migration and estuary-mouth state;
- Meteorology for storms, forecasts and atmospheric conditions;
- Geology for bedrock/substrate;
- Soil for terrestrial soil condition and erosion;
- Crisis for evacuation and emergency response;
- Conservation for stewardship decisions;
- Architecture/Public Works for structures and construction projects;
- Tourism for visitor pressure;
- Cartography for maps and survey products;
- AutoPTU for tactical terrain, movement, hazards, damage and combat resolution.

Minecraft/Cobblemon projects the current physical revision. Loaded blocks do not define the authoritative coast.

## Core separation

Do not collapse:

physical coastal segment -> current shoreline geometry -> beach profile -> dune state -> observed change -> inferred cause -> management response -> ecological response -> access consequence -> tactical battle state.

Examples:

- a shoreline can retreat without a storm being the proven cause;
- a dune can disappear without creating a PTU hazard;
- a beach can widen after nourishment without proving ecological recovery;
- an exposed ruin was not created by the storm that revealed it;
- a low-tide sandbar is not automatically permanent land;
- a Sandygast on a beach does not prove that it moved the shoreline.

## COASTAL_SYSTEM

```yaml
coastal_system_id: null
region_ids: []
maritime_region_ids: []
coastal_segment_ids: []
estuary_system_ids: []
settlement_ids: []
conservation_ids: []
public_works_ids: []
monitoring_network_ids: []
map_ids: []
history_refs: []
canon_status: proposed
```

A coastal system is a coordination object. It can span several settlements or jurisdictions.

## COASTAL_SEGMENT

```yaml
coastal_segment_id: null
coastal_system_id: null
segment_type: beach|dune_coast|barrier|rocky_shore|cliff|mixed|other
adjacent_segment_ids: []
landward_location_ids: []
seaward_location_ids: []
substrate_refs: []
beach_profile_ids: []
dune_system_ids: []
shoreline_revision_ids: []
access_revision_ids: []
habitat_refs: []
structure_ids: []
monitoring_station_ids: []
```

Segments are coarse world-state units, not Minecraft chunks.

## SHORELINE_REVISION

```yaml
shoreline_revision_id: null
coastal_segment_id: null
observed_at: null
geometry_ref: null
method_ref: null
source_refs: []
confidence: null
supersedes_id: null
change_class: stable|retreat|advance|reconfigured|unknown
```

Old revisions remain in history.

A changed geometry must never retroactively invalidate an older map that was correct at the time.

## BEACH_PROFILE_REVISION

```yaml
beach_profile_revision_id: null
coastal_segment_id: null
observed_at: null
profile_class: narrow|moderate|wide|steep|flat|barred|scarped|mixed|unknown
berm_state: null
sediment_character_ref: null
wrack_line_ref: null
access_state_ref: null
source_refs: []
supersedes_id: null
```

The qualitative profile is world-state metadata.

It does not create movement cost, cover or tactical modifiers.

## DUNE_SYSTEM

```yaml
dune_system_id: null
coastal_segment_id: null
dune_revision_ids: []
vegetation_unit_ids: []
access_path_ids: []
structure_ids: []
habitat_refs: []
restoration_project_ids: []
```

## DUNE_REVISION

```yaml
dune_revision_id: null
dune_system_id: null
observed_at: null
geometry_ref: null
condition_class: intact|scarped|lowered|breached|recovering|rebuilt|unknown
vegetation_state_ref: null
human_disturbance_refs: []
storm_event_refs: []
source_refs: []
supersedes_id: null
```

Dune condition may influence world access only through authored connection rules.

It cannot apply tactical sand, elevation, cover or protection automatically.

## OVERWASH_EVENT

```yaml
overwash_event_id: null
coastal_segment_id: null
source_storm_event_id: null
observed_at: null
inundation_footprint_ref: null
deposit_geometry_ref: null
affected_access_ids: []
affected_structure_ids: []
affected_habitat_ids: []
material_observation_refs: []
confidence: null
```

An overwash event is a physical world event. It does not imply drowning, forced movement, damage or Sandstorm.

## BREACH_EVENT

```yaml
breach_event_id: null
coastal_segment_id: null
opened_at: null
closed_at: null
source_event_refs: []
geometry_ref: null
water_connection_refs: []
travel_consequence_ids: []
ecology_consequence_ids: []
management_response_ids: []
status: open|closing|closed|stabilized|unknown
```

A breach may create or remove a connection, but Travel/Maritime remain authoritative for whether an actor can use it.

## CLIFF_EDGE_REVISION

```yaml
cliff_edge_revision_id: null
coastal_segment_id: null
observed_at: null
geometry_ref: null
retreat_class: none_observed|localized|ongoing|event_based|unknown
rockfall_event_ids: []
access_consequence_ids: []
structure_exposure_ids: []
source_refs: []
supersedes_id: null
```

Do not derive falling rules or push hazards from this state.

## SEDIMENT_BUDGET_REVISION

Ouros does not need a full sediment-transport simulator.

Use a coarse evidence-backed record:

```yaml
sediment_budget_revision_id: null
coastal_system_id: null
valid_period_ref: null
segment_tendency:
  segment_id: accreting|eroding|mixed|uncertain|unknown
known_source_refs: []
known_sink_refs: []
project_influence_refs: []
storm_refs: []
confidence: null
supersedes_id: null
```

This record supports causal stories without simulating every grain of sand.

## COASTAL_CHANGE_OBSERVATION

```yaml
coastal_change_observation_id: null
coastal_segment_id: null
observed_at: null
observer_ids: []
observation_type: shoreline|dune|cliff|beach_profile|overwash|breach|sediment|other
measurement_or_note_ref: null
photo_record_ids: []
map_ref: null
source_refs: []
quality_flag: null
```

An observation does not immediately create an interpretation.

## COASTAL_CAUSE_HYPOTHESIS

```yaml
coastal_cause_hypothesis_id: null
observation_ids: []
proposed_driver_refs: []
confidence: null
supporting_evidence_ids: []
contradicting_evidence_ids: []
status: proposed|supported|weakened|rejected|unresolved
```

Possible drivers include storms, wave climate, sediment supply, structures, dredging, nourishment, vegetation loss, cliff failure or multiple interacting causes.

Do not invent a single culprit because it makes a better quest.

## COASTAL_ACCESS_REVISION

```yaml
coastal_access_revision_id: null
access_id: null
coastal_segment_id: null
valid_from: null
valid_until: null
state: open|limited|rerouted|closed|seasonal|unknown
physical_reason_refs: []
institutional_reason_refs: []
alternative_access_ids: []
verification_event_id: null
```

Physical possibility and institutional permission remain separate.

## NOURISHMENT_OR_RESTORATION_PROJECT

```yaml
coastal_project_id: null
coastal_segment_ids: []
project_type: nourishment|dune_rebuild|vegetation|access_reroute|structure|monitoring|other
objective_refs: []
material_batch_ids: []
borrow_source_refs: []
work_event_ids: []
monitoring_plan_refs: []
maintenance_refs: []
ecology_refs: []
access_refs: []
public_works_ref: null
status: proposed|approved|active|paused|completed|monitoring|retired
```

Material provenance should link to Material Culture/Geology where relevant.

A completed project does not equal a successful outcome. Monitoring must be separate.

## Natural recovery

Post-storm recovery should be represented as a sequence of revisions rather than a timer that restores the old map.

Possible coarse states:

- immediate impact;
- beach reworking;
- early sand accumulation;
- vegetation/recruitment changes;
- dune rebuilding;
- long-term changed equilibrium;
- unresolved/non-recovery.

The correct end state may differ from the pre-storm coast.

## Persistence rule

Chunk/map reload must project current authoritative state.

Never implement:

```text
player leaves area
-> reload original coastline template
-> erased dune returns
-> washed-out boardwalk returns
-> closed breach disappears
```

Current-world projection should instead use:

```text
coastal system state
-> current physical revision
-> current structures/access
-> Minecraft projection
```

Historical versions remain available to maps, archives, photographs and Chronicle references.

## Archaeology and exposed material

Coastal change may expose:

- old foundations;
- fossils;
- wreckage;
- buried infrastructure;
- historic objects;
- previous shoreline markers.

Exposure creates a discovery opportunity only.

It does not decide ownership, custody, authenticity, age or archaeological interpretation.

## Ecology connection

Physical change may affect:

- nesting access;
- shelter;
- foraging substrate;
- wrack availability;
- freshwater/saltwater connection;
- vegetation establishment;
- human disturbance;
- wild movement corridors.

Ecology layers must own the biological interpretation.

No direct `shoreline retreat -> species spawn multiplier` rule is allowed.

## Tourism and public memory

A famous beach may change shape without losing its cultural identity.

Tourism can react to:
- a widened or narrowed beach;
- closures;
- exposed history;
- changed access;
- reconstruction;
- a famous photograph no longer matching the landscape.

Public Memory can preserve names, stories and old images even when the physical place changes.

## Species-specific sand interactions

Sandygast/Palossand can support authored observations and quests where sand matters.

Do not infer:
- shoreline control;
- dune creation;
- sediment-budget change;
- ownership of sand;
- Water Compaction trigger;
- tactical Sandstorm;
- Groundshaper;
- Rough Terrain.

Any exact Move/Ability/Capability interaction remains PTU/Caelo + AutoPTU authority.

## Minecraft projection

A projection may use:
- changed beach width;
- revised dune geometry;
- boardwalk/access variants;
- exposed/covered structures;
- overwash deposits;
- cliff-edge variants;
- vegetation variants;
- temporary closure markers.

The projection should be coarse and authored/validated. Do not run block-by-block erosion every tick.

## Battle projection contract

Before a coastal battle begins:

1. Resolve the current coastal revision in world state.
2. Select a stable tactical projection.
3. Validate geometry and access.
4. Freeze that battle snapshot unless exact dynamic-terrain mechanics are supported.
5. Let AutoPTU own legality and outcome.
6. Write back only supported semantic consequences.

Minecraft must not improvise wave knockback, cliff falls, sand penalties or storm damage.

## Encounter contract A — Dune Breach Evacuation

Narrative premise: a storm opens a gap through a dune ridge while people and Pokémon are being moved inland.

FULL version requires:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle if exact effects are used;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks when used;
- AI legal-action infrastructure;
- AI tactical policy for retreat/protection;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version:
- resolve breach, evacuation lanes and civilians in world state;
- move noncombatants out before battle;
- select one safe inland/static shoreline arena;
- run only a legal conventional battle if conflict remains;
- update access/evacuation state afterward.

## Encounter contract B — Cliff Path Survey

Narrative premise: surveyors investigate a coastal trail after a section of cliff retreats.

FULL version needs dynamic edge hazards, falling/forced movement rules, push/knockback interactions, objective-aware AI and playback.

Reduced version:
- close unsafe path before combat;
- use survey/skill/world-state resolution outside AutoPTU;
- if combat occurs, use a stable inland section with blockers marking the unsafe edge;
- no automatic falling or cliff damage.

## Encounter contract C — Storm-Wrack Recovery

Narrative premise: post-storm material along a beach includes natural wrack, lost cargo and items with uncertain provenance.

FULL version could eventually include moving water/debris, protected retrieval zones and withdrawal objectives.

Reduced version:
- classify/search/custody happens in world state;
- static beach grid is used only for a discrete combat encounter;
- recovered material remains under Case/Custody/Material Culture authority.

## Capability dependency summary

Current planning status based on Pass 80 live evidence:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED for the implemented static surface;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

## Non-inference rules

Do not infer:

- visible sand = `desert` tactical terrain;
- beach = ocean tactical terrain;
- dune = cover/elevation;
- wet sand = Slow/Rough Terrain;
- cliff = falling hazard;
- wave = forced movement;
- storm surge = damage;
- overwash = Water terrain;
- Sandygast/Palossand = geomorphology controller;
- seawall = successful protection;
- nourishment = ecological success;
- beach loss = permanent coastline retreat;
- wide beach = safe beach;
- Minecraft block count = authoritative sediment volume.

## Canon questions

Before promotion, Ouros must decide:

- which coastlines are major authored geographic anchors;
- which barrier islands, dunes and cliffs exist at campaign start;
- which old storms or engineering projects are historical canon;
- which institutions survey shorelines;
- which settlements maintain coastal defenses/access;
- whether players can materially reshape shorelines and at what scale;
- which cultural traditions are tied to particular beaches;
- how frequently long-term coastal revisions advance offline;
- exact PTU/Caelo rules for sand, water, cliffs, falling, Groundshaper, Naturewalk and environmental hazards;
- how the Minecraft adapter versions and rebuilds coastline chunks without duplicating rules.
