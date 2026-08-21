# Estuaries, Tidal Wetlands & Salinity Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanic is established by this document.

Pass: 78

## Purpose

This layer models the transition between freshwater catchments and marine systems.

It owns persistent estuary identity, salinity structure, tidal wetland hydroperiod, estuary-mouth state, sediment/accretion history, marsh migration and saltwater-intrusion evidence.

It does not replace:

- Maritime for sea lanes, harbors, vessels and submerged sites;
- Freshwater for upstream catchments, river reaches, groundwater and reservoirs;
- Meteorology for rainfall, storms and forecasts;
- Soil for land-surface condition and erosion;
- Conservation for stewardship/management decisions;
- Fisheries for fishing effort and stock management;
- AutoPTU for battle mechanics.

## Core separation

Do not collapse these states:

- physical estuary geography;
- freshwater inflow;
- tidal stage;
- salinity observation;
- inferred salinity zone;
- water depth/access state;
- sediment/accretion state;
- wetland vegetation/habitat state;
- groundwater salinity state;
- ecological response;
- public interpretation;
- tactical PTU terrain/weather/hazard state.

A low tide can expose mud without creating Rough Terrain.

A saline well can exist without visible seawater at the surface.

A marsh can migrate inland without the original marsh having vanished completely.

A Pokémon population can shift without salinity being the proven cause.

## Persistent objects

### ESTUARY_SYSTEM

```yaml
estuary_system_id: null
name: null
region_ids: []
maritime_region_id: null
freshwater_system_ids: []
mouth_location_ids: []
tidal_wetland_ids: []
mudflat_ids: []
tidal_creek_ids: []
lagoon_ids: []
groundwater_connection_ids: []
harbor_ids: []
settlement_ids: []
fishery_ids: []
stewardship_ids: []
monitoring_network_ids: []
history_refs: []
canon_status: proposed
```

An estuary is a coordination object across existing systems. It does not imply one authority or one uniform salinity.

### ESTUARY_REACH

A reach is a coarse hydrologic/ecological segment, not a Minecraft chunk.

```yaml
estuary_reach_id: null
estuary_system_id: null
upstream_reach_ids: []
downstream_reach_ids: []
adjacent_wetland_ids: []
adjacent_upland_ids: []
normal_depth_class: unknown
normal_salinity_band: unknown
current_access_state: unknown
observation_ids: []
```

Suggested qualitative salinity bands for world state:

- FRESH_DOMINANT
- LOW_BRACKISH
- BRACKISH
- HIGH_BRACKISH
- MARINE_DOMINANT
- HYPERSALINE
- HIGHLY_VARIABLE
- UNKNOWN

These labels are narrative abstractions. Numeric measurements can coexist with them during research scenarios.

### TIDAL_STATE_REVISION

```yaml
tidal_state_revision_id: null
estuary_system_id: null
observed_or_predicted: observed
valid_from: null
valid_until: null
stage_class: low|rising|high|falling|exceptional|unknown
source_refs: []
confidence: null
```

Tidal state may affect world access only through authored connection rules.

It does not directly change PTU movement.

### SALINITY_OBSERVATION

```yaml
salinity_observation_id: null
estuary_reach_id: null
observed_at: null
observer_ids: []
location_ref: null
depth_band: surface|mid|bottom|well|unknown
value: null
units: null
qualitative_band: null
method_ref: null
tidal_state_ref: null
freshwater_inflow_ref: null
quality_flag: null
source_refs: []
```

One measurement must never rewrite the full estuary.

### SALINITY_FRONT_REVISION

```yaml
salinity_front_revision_id: null
estuary_system_id: null
valid_time_ref: null
reach_band_assignments: {}
evidence_refs: []
model_or_observation: null
confidence: null
supersedes_id: null
```

A front can move upriver or seaward over time.

Do not infer a cause solely from movement direction.

Potential drivers must be separate evidence-backed claims:

- changed freshwater discharge;
- tides;
- wind;
- drought;
- storm surge;
- estuary-mouth restriction;
- pumping/groundwater effects;
- infrastructure operation;
- measurement/model error.

### TIDAL_WETLAND

```yaml
tidal_wetland_id: null
estuary_system_id: null
location_id: null
wetland_type: salt_marsh|brackish_marsh|tidal_flat|mangrove|tidal_creek|lagoon_edge|other
hydroperiod_profile_id: null
vegetation_unit_ids: []
soil_land_unit_ids: []
ecology_refs: []
nesting_or_nursery_refs: []
access_refs: []
stewardship_refs: []
condition_revision_ids: []
```

### HYDROPERIOD_REVISION

```yaml
hydroperiod_revision_id: null
tidal_wetland_id: null
valid_from: null
valid_until: null
inundation_frequency_class: null
inundation_duration_class: null
drainage_state: null
source_refs: []
confidence: null
```

Hydroperiod describes world state. It does not create drowning, Slow Terrain or other tactical effects.

### MARSH_EDGE_REVISION

```yaml
marsh_edge_revision_id: null
tidal_wetland_id: null
observed_at: null
geometry_ref: null
method_ref: null
source_refs: []
supersedes_id: null
```

This supports multi-year accretion, erosion, drowning and inland migration without rewriting old maps.

### SEDIMENT_BALANCE_EVENT

```yaml
sediment_balance_event_id: null
estuary_system_id: null
reach_ids: []
event_type: deposition|erosion|dredging|storm_deposition|upstream_change|restoration|unknown
start_time: null
end_time: null
source_refs: []
observed_effect_refs: []
```

A dredging operation, upstream flood or storm may alter sediment state. The causal link must remain evidence-based.

### ESTUARY_MOUTH_STATE

```yaml
estuary_mouth_state_id: null
estuary_system_id: null
observed_at: null
state: open|restricted|shifted|closed|breached|unknown
channel_geometry_ref: null
navigation_effect_refs: []
salinity_effect_claim_refs: []
flood_effect_claim_refs: []
source_refs: []
```

A mouth opening or closure can change circulation, but individual effects require observations/models before world mutation.

### COASTAL_GROUNDWATER_SALINITY_CASE

This extends Freshwater groundwater state without transferring aquifer authority into this layer.

```yaml
case_id: null
aquifer_or_groundwater_ref: null
coastal_connection_ref: null
well_observation_ids: []
surface_water_observation_ids: []
possible_pathway_claim_ids: []
management_response_ids: []
status: open|monitoring|stabilized|resolved|unknown
```

Do not treat salinity in one well as proof of a regional marine flood.

### ESTUARY_ECOLOGY_OBSERVATION

```yaml
observation_id: null
estuary_system_id: null
reach_or_wetland_id: null
observed_at: null
pokemon_entity_ids: []
species_refs: []
observation_type: presence|absence|abundance_class|behavior|nesting|juvenile_use|movement|mortality|other
salinity_observation_refs: []
tidal_state_ref: null
weather_ref: null
freshwater_ref: null
source_refs: []
interpretation_status: none
```

Observation and explanation remain separate.

## Tidal access windows

Some locations may be physically present but only practically accessible during certain world states.

Examples:

- exposed mudflat survey point;
- low-tide cave entrance;
- marsh boardwalk crossing;
- shallow wreck approach;
- tidal-creek ford;
- research instrument station.

Access flow:

```text
current authoritative world state
→ authored location access rule
→ travel/permission/capability validation
→ overworld access result
```

Never use:

```text
Minecraft block is exposed
→ therefore PTU access is legal
```

## Salinity and Pokémon distribution

The system may record correlations.

Example:

```text
three years of observations
→ Shellos form A increasingly observed in lower estuary
→ upper-estuary salinity also changed
→ research hypothesis created
```

It must not silently promote that correlation to species law.

Species-specific habitat relationships require authored canon or sufficiently reviewed evidence.

## Nursery and juvenile habitat

Estuaries can support temporary juvenile or nursery use.

Ouros should represent this through ecology/population state rather than direct spawn bonuses.

```yaml
nursery_use_window:
  habitat_id: null
  species_refs: []
  expected_window_ref: null
  observed_use_state: unknown
  observation_refs: []
  disturbance_refs: []
  stewardship_refs: []
```

Do not infer breeding, Eggs or parentage from juvenile presence unless separately observed.

## Marsh migration

Wetlands may move inland over long world time if hydrology and terrain allow.

Potential chain:

```text
relative water level changes
→ hydroperiod shifts
→ vegetation zones change
→ marsh edge revision moves
→ upland transition becomes important
→ road/housing/conservation conflict appears
```

This is a slow world process. It should rarely run at player-minute resolution.

Migration needs geometry and history. Do not replace it with `marsh_expanded=true`.

## Sediment and channel memory

Mudflats, tidal creeks and channels can shift.

Map editions should preserve old states.

A channel that disappears can remain important as:

- historical navigation route;
- drainage feature;
- buried infrastructure corridor;
- archaeological boundary;
- former habitat;
- source of a public-memory dispute.

## Infrastructure interactions

Relevant assets may include:

- tide gates;
- sluices;
- levees;
- culverts;
- drainage channels;
- pumping stations;
- harbor works;
- dredged channels;
- boardwalks;
- monitoring stations.

Infrastructure operation does not directly author hydrologic truth.

Example:

```text
gate closes
→ expected circulation claim
→ observations collected
→ salinity/depth revision confirmed
→ ecology/access changes considered
```

## Restoration model

Estuary restoration should use baseline + intervention + verification.

```yaml
estuary_restoration_project:
  project_id: null
  target_ids: []
  baseline_refs: []
  intervention_type: null
  construction_or_action_refs: []
  expected_outcome_claims: []
  monitoring_plan_refs: []
  observed_outcome_refs: []
  unintended_effect_refs: []
  status: proposed|active|monitoring|complete|revised
```

A visually greener marsh is not automatically restored.

## Multiplayer knowledge

Players may hold different valid knowledge:

- fisher observations;
- research salinity profiles;
- harbor charts;
- conservation surveys;
- historic maps;
- local route knowledge.

Sharing one map or reading one bulletin does not grant all underlying datasets.

Sensitive nesting locations can use the existing information/redaction layer.

## Minecraft projection

Minecraft may render:

- coarse tide variants;
- exposed or inundated flats;
- marsh vegetation variants;
- shifted boardwalk access;
- monitoring posts;
- salinity/sample UI;
- historical channel markers;
- closed/open tidal gates;
- mudflat wildlife clusters;
- public warnings.

Minecraft must not calculate:

- salinity-induced PTU damage;
- movement penalties;
- drowning;
- current push;
- mud entrapment;
- type interactions;
- Pokémon capability legality;
- encounter rarity.

## Cobblemon ecology projection

Estuary world state may eventually provide coarse habitat weights to a controlled spawn adapter.

Required protections:

1. authoritative estuary state is server-side;
2. local block placement cannot instantly rewrite the salinity front;
3. tide changes cannot be farmed as a deterministic rare-spawn toggle;
4. population state and loaded entities remain separate;
5. individual persistent Pokémon retain identity across projections;
6. observation events come from actual projected presence, not the other way around.

## PTU/Caelo mechanical boundary

Available project evidence confirms that Python AutoPTU recognizes wetlands/marsh/mud contexts for selected authored effects and has Swim/Naturewalk capability handling.

This does not authorize generic mechanics for salinity, tide or mud.

Future rules review must extract exact authoritative behavior for any intended use of:

- Swim;
- Naturewalk (Wetland or related labels);
- water movement;
- difficult/rough/slow terrain;
- sinking or mud;
- visibility;
- Weather/Terrain interactions;
- environmental status effects;
- underwater/shoreline capability gates.

## Encounter contracts

### Tidal Creek Crossing — FULL

Premise:

A research route across a tidal creek becomes time-sensitive while a wild collective uses the same corridor.

Intended full version:

- water depth changes during the encounter;
- some crossing tiles become unavailable;
- wildlife attempts to reach a safe side rather than defeat every combatant;
- players can prioritize withdrawal, observation or protection;
- route geometry and objective state update semantically.

Required capability families:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including forced movement/interception if currents or blocking are used;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline if attacks occur;
- status lifecycle if any authored status appears;
- terrain/weather/hazards/zones/reactions for changing water/depth zones;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy for withdrawal/route choice;
- Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version:

Resolve tidal stage before battle. Freeze one safe, static creek geometry for the encounter. Resolve wildlife crossing in overworld state before or after a conventional battle. No current, changing water, mud penalty or salinity effect exists inside AutoPTU.

### Marsh Boardwalk Breach — FULL

Premise:

A boardwalk section fails during a monitoring visit while Pokémon occupy adjacent tidal flats.

Intended full version:

- unstable/closed tiles;
- protected evacuation lane;
- noncombatants move toward an exit;
- wild Pokémon may withdraw away from disturbance;
- restoration/inspection state persists after the incident.

Full dependencies:

- targeting — required;
- base movement — required;
- complete movement/interception — required for moving evacuees/route denial;
- initiative — required;
- lifecycle — required;
- terrain/hazards/zones/reactions — required for unstable/closed areas;
- tactical AI — required for evacuation/withdrawal;
- adapter/playback — required;
- other combat families as used by actual legal combatants.

Reduced version:

Evacuate visitors in overworld state. Freeze the failed section as static blockers. Any encounter uses a validated dry/stable arena. Repair decisions occur afterward.

### Salinity Station Recovery — FULL

Premise:

A monitoring station stops transmitting while different groups disagree about whether the estuary is changing.

Intended full version:

The main scenario is investigation, not combat. A battle may occur only if actual Pokémon behavior creates one.

If combat does occur, a future full version could include water-level zones and objective-aware retreat.

Reduced version:

Retrieve the station and samples in overworld state. Use a static encounter only if necessary. Measurements update evidence; they never create battle effects by themselves.

## Promotion gates

No encounter may promote a tidal/marsh mechanic from presentation to tactical execution until:

1. PTU/Caelo rule text for the intended effect is identified;
2. Python oracle behavior is frozen where applicable;
3. Java has parity-tested implementation for the exact family;
4. BattleSpec owns the relevant environment input;
5. transcript emits semantic environment events;
6. Minecraft only renders the result;
7. reduced version remains available if any dependency regresses.

## Long-term integration targets

- Freshwater → estuary freshwater inflow
- Maritime → sea state/harbor/navigation
- Meteorology → rain/storm/wind inputs
- Soil/Geology → sediment and coastal substrate
- Conservation → stewardship/restoration
- Fisheries → nursery/fishing use
- Agriculture/Settlement → water supply and saltwater-intrusion consequences
- Cartography → channel/marsh map editions
- Science → observations/models
- Cobblemon → controlled ecological projection
- AutoPTU → frozen tactical snapshot only after validation

## Open canon questions

- Which Ouros regions have estuaries, deltas, tidal marshes, mangroves or lagoons?
- Are any important settlements built directly around an estuary?
- Which historical channels, levees, gates or reclamation works predate the players?
- Which Pokémon–estuary relationships are authored regional canon?
- Does any region use formal salinity monitoring?
- Which nursery habitats are culturally or economically important?
- How much marsh migration should occur during normal campaign timescales?
- How will coastal groundwater and settlement water supply be represented without excessive simulation?
