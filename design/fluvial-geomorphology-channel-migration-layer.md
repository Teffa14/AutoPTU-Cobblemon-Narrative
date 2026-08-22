# Fluvial Geomorphology & Channel Migration Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanical effect is established here.

Pass: 114

## Purpose

This layer gives Ouros a persistent model for rivers whose physical form changes over time.

Freshwater remains responsible for hydrological state: flow, level, floods, connectivity and water-control assets.

Fluvial Geomorphology owns persistent physical river-form history: active channel position, banks, bars, islands, side channels, cutoffs, abandoned channels, floodplain surfaces and migration corridors.

The same river can therefore remain the same named system while its geometry changes materially across years.

## Core separation

Never collapse these into one state:

- river identity;
- current active channel geometry;
- hydrological flow/level state;
- channel-migration history;
- erosion observation;
- deposition observation;
- sediment-source hypothesis;
- island/bar identity;
- abandoned-channel identity;
- map representation;
- property/access claim;
- ecological interpretation;
- Minecraft geometry;
- tactical PTU terrain/hazard state.

Examples:

- a flood can occur without a lasting channel shift;
- a channel can migrate gradually during otherwise ordinary years;
- a new gravel bar can form without becoming permanent land;
- an oxbow can remain part of the river’s history after losing direct flow;
- a map can be outdated while still accurately documenting a former channel;
- a bridge can remain structurally intact while no longer spanning the main channel;
- a Minecraft sandbar does not automatically create PTU Terrain.

## Persistent objects

### FLUVIAL_SYSTEM

Use the existing Freshwater river identity where possible rather than duplicating it.

```yaml
fluvial_system_id: null
freshwater_system_id: null
name: null
region_ids: []
reach_ids: []
channel_migration_zone_ids: []
history_refs: []
canon_status: proposed
```

### FLUVIAL_REACH

A reach is a coarse geomorphic segment. It is not a Minecraft chunk.

```yaml
fluvial_reach_id: null
freshwater_reach_id: null
current_channel_revision_id: null
migration_zone_id: null
bank_unit_ids: []
bar_ids: []
island_ids: []
side_channel_ids: []
abandoned_channel_ids: []
connected_floodplain_ids: []
```

### CHANNEL_GEOMETRY_REVISION

```yaml
channel_revision_id: null
fluvial_reach_id: null
valid_from: null
valid_to: null
geometry_ref: null
main_thread_geometry_ref: null
secondary_channel_geometry_refs: []
source_observation_refs: []
confidence: null
supersedes_revision_id: null
change_class: stable|migration|widening|narrowing|cutoff|avulsion|braiding_change|incision_expression|other
```

A revision records what the channel geometry was believed to be during a time interval.

Do not delete old revisions after a new survey.

### CHANNEL_MIGRATION_ZONE

```yaml
migration_zone_id: null
fluvial_system_id: null
geometry_ref: null
basis_refs: []
assessment_date: null
confidence: null
status: proposed|validated|superseded
```

This is a planning/science abstraction for where channel movement may occur over time.

It does not itself prohibit access, construction or use. Governance/Land Tenure must apply any policy separately.

### BANK_SEGMENT

```yaml
bank_segment_id: null
fluvial_reach_id: null
bank_side: left|right|other
geometry_ref: null
condition_revision_refs: []
observation_refs: []
```

Possible observed change classes:

- STABLE_OBSERVED
- ACTIVE_EROSION_OBSERVED
- RECENT_FAILURE_OBSERVED
- VEGETATED_NEW_BANK
- ENGINEERED_BANK
- UNKNOWN

These are observations, not tactical hazards.

### FLUVIAL_BAR

```yaml
bar_id: null
fluvial_reach_id: null
bar_type: point_bar|mid_channel_bar|gravel_bar|sand_bar|other
first_observed_at: null
current_geometry_ref: null
revision_refs: []
vegetation_state_ref: null
persistence_class: transient|seasonal|multi_year|unknown
```

A bar can later become vegetated, connect to a bank, split or disappear.

### FLUVIAL_ISLAND

```yaml
island_id: null
fluvial_system_id: null
first_observed_at: null
current_geometry_ref: null
revision_refs: []
origin_hypothesis_refs: []
habitat_refs: []
access_refs: []
land_tenure_refs: []
```

An island is a physical landform. Its ownership, public status or ecological importance are separate.

### ABANDONED_CHANNEL

```yaml
abandoned_channel_id: null
former_channel_revision_ref: null
cutoff_or_avulsion_event_ref: null
current_state: connected_backwater|seasonally_connected|oxbow_lake|wetland|dry_depression|filled|unknown
current_geometry_ref: null
hydrology_handoff_ref: null
ecology_refs: []
heritage_refs: []
```

The abandoned channel remains historically linked to the river even after the main flow leaves it.

### FLUVIAL_CHANGE_EVENT

```yaml
fluvial_change_event_id: null
fluvial_reach_ids: []
event_type: bank_migration|bar_growth|bar_loss|meander_cutoff|avulsion|island_formation|island_loss|side_channel_activation|side_channel_abandonment|other
start_time: null
end_time: null
trigger_hypothesis_refs: []
water_regime_event_refs: []
sediment_event_refs: []
observation_refs: []
resulting_revision_refs: []
confidence: null
```

Do not infer a trigger from timing alone.

A flood that happened immediately before a cutoff may be relevant evidence without proving it was the sole cause.

### FLUVIAL_GEOMORPHOLOGY_OBSERVATION

```yaml
observation_id: null
observed_at: null
observer_ids: []
location_or_reach_id: null
observation_type: bank_position|channel_centerline|bar_extent|island_extent|erosion|deposition|sediment_texture|wood_accumulation|abandoned_channel_state|other
value: null
method_ref: null
source_media_refs: []
quality_flag: null
```

Potential methods:

- field survey;
- repeated map comparison;
- photography;
- aerial observation;
- old bridge/structure alignment;
- vegetation age;
- sediment observation;
- local testimony;
- instrument/sensor data.

Different methods can disagree legitimately.

### SEDIMENT_SOURCE_CLAIM

```yaml
sediment_source_claim_id: null
material_description: null
source_hypothesis: upstream_bank|tributary|landslide|construction|dam_release|wildfire_runoff|coastal_backwater|unknown|other
supporting_refs: []
contradicting_refs: []
confidence: null
status: proposed|supported|rejected|superseded
```

This layer should use coarse causal claims, not simulate every sediment grain.

## Physical revision rules

### 1. River identity persists

A named river does not become a different river merely because it changes course locally.

### 2. Geometry is versioned

Every meaningful physical revision should preserve the prior state.

Useful downstream consequences include:

- Cartography marks old editions as historically valid;
- Travel revalidates crossings;
- Land Tenure reviews claims tied to physical features;
- Infrastructure inspects exposed foundations;
- Conservation evaluates new/abandoned habitats;
- Archaeology reviews newly exposed surfaces;
- Public Memory can preserve former channels as local landmarks.

### 3. Hydrology triggers but does not directly write form

Freshwater can emit a flood pulse or altered flow regime.

This layer decides, from validated observations/models, whether that event produced:

- no persistent form change;
- bank migration;
- bar growth/loss;
- cutoff;
- avulsion;
- channel widening/narrowing;
- side-channel activation;
- other physical change.

### 4. Geomorphic change can lag the initiating event

Allow sequences such as:

```text
large flood
→ overflow channel scoured
→ smaller later events continue erosion
→ vegetation establishes on old bar
→ new route captures more flow
→ main channel shifts years later
```

The generator should not require the most dramatic visible change to happen during the first event.

### 5. Newly exposed land is not free land

New gravel/sand bars, islands, old channels and exposed floodplain do not create automatic ownership, public access or resource rights.

Use Land Tenure/Commons.

## Cartography and historical geography

Every map should reference a physical-state date or revision where practical.

Examples:

- 12-year-old map: bridge crosses active channel;
- current map: bridge ends over a dry former channel;
- archival map: island absent;
- later survey: island appears and then joins the bank;
- property sketch: “east bank” meaning remains legally unresolved after migration.

Maps can therefore disagree without one being fabricated.

## Ecology and succession

Fluvial landforms can create habitat trajectories:

new bar → pioneer vegetation → shrub establishment → young woodland;

abandoned channel → backwater → oxbow → marsh/wetland;

new side channel → aquatic movement corridor;

bank erosion → fallen wood → habitat structure;

floodplain deposition → changed soil surface.

Each transition should be handed to the appropriate ecology layer and observed over time.

Do not equate geomorphic dynamism with ecological damage.

## Infrastructure interaction

Structures can become misaligned with the active river:

- bridge spans old channel;
- ferry landing silts up;
- intake becomes too shallow;
- levee protects a former bank but not the new one;
- culvert no longer receives the same flow;
- road ends at a migrated bank;
- utility crossing becomes exposed.

Infrastructure consequences require inspection. They are not automatic failure flags.

## Player and NPC memory

NPC claims can reflect different historical states.

Example:

An older ferryman says, “the island used to be on the other side.”

A younger surveyor says the modern chart is correct.

Both can be accurate relative to different dates.

The Chronicle should preserve this temporal context.

## Minecraft projection

The server-authoritative world model owns the current geomorphic revision.

Minecraft may project:

- current channel blocks;
- bars/islands;
- old channels;
- exposed bridge piers;
- erosion scars;
- temporary construction/access works.

Loaded chunks do not become truth merely because their blocks exist.

A reload must never restore an obsolete channel geometry.

Physical edits by players should enter a review pipeline if they affect a tracked reach. They should not silently mutate authoritative channel history.

## Battle projection boundary

A fluvial scene can create a frozen battle map only after world state is validated.

Possible future tactical projections include:

- shallow/deep water zones;
- fixed islands/bars;
- bank edges;
- validated current zones;
- unstable bank hazards;
- changing routes during an avulsion/flood.

None are mechanically authorized by this design document.

### Hard non-inferences

Do not infer:

- riverbank -> Rough Terrain;
- wet bank -> Slowed/Tripped;
- eroding bank -> falling damage;
- high flow -> forced movement;
- gravel bar -> cover;
- island -> safe zone;
- floodplain -> Water Terrain;
- oxbow -> Wetlands mechanical tag;
- new side channel -> Swim requirement without validated geometry/rules;
- bridge pier -> cover;
- sediment plume -> Accuracy penalty;
- bank collapse -> damage;
- river migration -> automatic structure destruction;
- new land -> ownership;
- river-boundary wording -> boundary automatically moves;
- Pokémon near erosion -> cause of erosion;
- Ground-type Move -> regional channel migration;
- Water-type Move -> flood-scale geomorphic change;
- Minecraft water update -> authoritative fluvial revision.

## Encounter contracts

### 1. Cutoff Bend Survey — FULL

Narrative premise:
A rapidly evolving meander has opened a shortcut channel. Surveyors need observations from both old and new banks before the next high-flow window.

Intended mechanics:

- multiple route options;
- side channel geometry that may become impassable/passable by phase;
- wildlife with withdrawal objectives;
- protected survey points;
- possible interception on narrow crossings.

Capability dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:
Resolve the high-flow window and active crossing state before combat. Freeze one validated bank/bar geometry. Surveyors remain outside the grid. If a confrontation occurs, AutoPTU receives only actual combatants on that static snapshot.

### 2. Oxbow Reconnection — FULL

Narrative premise:
A former channel reconnects during a seasonal high-water event. Researchers and conservation staff want to document movement between the main stem and the oxbow without trapping wildlife.

Intended mechanics:

- REACH_EXIT/WITHDRAW goals;
- temporary water connection;
- protected observation area;
- movement across changing shallow-water routes.

Dependencies:

- base verified combat families as above;
- complete movement: BLOCKING;
- terrain/weather/hazards/zones/reactions: BLOCKING if reconnection affects grid movement;
- AI tactical policy: BLOCKING for wildlife withdrawal;
- adapter/playback: BLOCKING.

Reduced version:
The server advances the reconnection outside combat. Observers withdraw. If conflict remains, use one fixed shoreline arena; the oxbow connection remains narrative/world state only.

### 3. Bridge on the Old Channel — FULL

Narrative premise:
A bridge still spans the former main channel while a newer thread now carries most flow beside it. A route dispute and wildlife movement overlap during an inspection.

Intended mechanics:

- civilians/inspectors moving through constrained space;
- two distinct crossing routes;
- possible route-clear/protect objectives;
- fixed water/landform differences with tactical meaning only if validated.

Dependencies:

- targeting/range/LoS: VERIFIED;
- base movement: VERIFIED;
- complete movement/interception: BLOCKING for escort/protection;
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked;
- environment family: BLOCKING if bank/water state matters tactically;
- AI legal actions: VERIFIED;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

Reduced version:
Inspection and route allocation happen before battle. Civilians leave the area. Freeze a dry/static work perimeter adjacent to the old bridge and resolve only the remaining combat.

## Suggested long-term simulation cadence

Do not update channel geometry every tick or every Minecraft day.

Suggested coarse triggers:

- validated major flood/high-flow event;
- seasonal survey window;
- engineering intervention;
- wildfire/sediment pulse handoff;
- dam/removal/operation change;
- landslide or tributary sediment event;
- explicit scientific survey;
- authored long-term migration step.

Most reaches should remain unchanged on most updates.

## New overworld blockers introduced by Pass 114

- `FLUVIAL_SYSTEM_GEOMORPHIC_STATE`
- `CHANNEL_GEOMETRY_REVISION_HISTORY`
- `CHANNEL_MIGRATION_ZONE_STATE`
- `BANK_SEGMENT_HISTORY`
- `FLUVIAL_BAR_IDENTITY_AND_REVISION`
- `FLUVIAL_ISLAND_IDENTITY_AND_REVISION`
- `SIDE_CHANNEL_IDENTITY_AND_STATE`
- `ABANDONED_CHANNEL_IDENTITY_AND_SUCCESSION`
- `FLUVIAL_CHANGE_EVENT_GRAPH`
- `FLUVIAL_GEOMORPHOLOGY_OBSERVATION_PROVENANCE`
- `SEDIMENT_SOURCE_CLAIM_GRAPH`
- `FRESHWATER_TO_FLUVIAL_GEOMORPHOLOGY_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_CARTOGRAPHY_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_TRAVEL_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_LAND_TENURE_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_CONSERVATION_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_INFRASTRUCTURE_HANDOFF`
- `FLUVIAL_GEOMORPHOLOGY_TO_MINECRAFT_PROJECTION`
- `FLUVIAL_GEOMORPHOLOGY_TO_FROZEN_BATTLE_SNAPSHOT`

## PTU/Caelo boundary

Potentially relevant exact rules still require primary-project validation before use:

- Swim;
- Naturewalk;
- Groundshaper;
- terrain tags;
- currents;
- falling;
- forced movement;
- bridge/structure interaction;
- shallow/deep water movement;
- environmental damage.

No rule is created by this layer.