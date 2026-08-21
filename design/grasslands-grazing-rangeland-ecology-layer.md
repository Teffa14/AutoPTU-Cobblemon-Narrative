# Grasslands, Grazing & Rangeland Ecology Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanic is established by this document.

Pass: 79

## Purpose

This layer models persistent grassland use by wild and managed herbivore groups.

It owns grazing/browsing pressure, herd-use history, grassland condition mosaics, congregation hotspots, range-use plans, forage observations, wallows/trails and long-term interactions among herbivores, vegetation, soil, water, fire and human management.

It does not replace:

- Wild Collectives for persistent group identity and subgroup membership;
- Flora for vegetation-unit state, flowering and succession;
- Soil for compaction, infiltration, erosion and restoration state;
- Agriculture for farms, crops and production systems;
- Conservation for stewardship designation and management decisions;
- Aridity for drought/dryness state;
- Wildfire for burn history and recovery;
- Freshwater for water points, streams and catchments;
- Workplaces for ranch staffing and professional roles;
- Material Culture for fleece, fiber, tools or product provenance;
- AutoPTU for battle mechanics.

## Core separation

Do not collapse these states:

- grassland physical extent;
- vegetation structure;
- forage availability observation;
- herbivore population/collective identity;
- visible subgroup presence;
- grazing/browsing use;
- trampling/congregation pressure;
- soil condition;
- water-point state;
- management intent;
- public interpretation;
- tactical PTU terrain/hazard state.

A grazed patch is not automatically damaged.

A heavily used patch is not automatically Rough Terrain.

A herd crossing a road does not create a stampede mechanic.

A managed herd is not automatically one Trainer's party.

A wild collective using a pasture does not become livestock.

## Persistent objects

### GRASSLAND_SYSTEM

```yaml
grassland_system_id: null
name: null
region_ids: []
landscape_type: prairie|steppe|savanna|meadow|alpine_meadow|pasture|mixed_range|other
vegetation_unit_ids: []
soil_land_unit_ids: []
water_point_ids: []
route_ids: []
settlement_ids: []
collective_ids: []
managed_herd_ids: []
stewardship_ids: []
fire_history_refs: []
drought_history_refs: []
condition_revision_ids: []
canon_status: proposed
```

A grassland system is a coordination object. It does not imply uniform vegetation, one owner or one management objective.

### GRAZING_UNIT

A coarse spatial unit used to store pressure and recovery history.

```yaml
grazing_unit_id: null
grassland_system_id: null
location_refs: []
vegetation_unit_ids: []
soil_land_unit_ids: []
water_access_refs: []
shade_or_shelter_refs: []
normal_use_class: unknown
current_use_class: unknown
rest_status: unknown
observation_ids: []
history_refs: []
```

Suggested use classes:

- UNUSED_OBSERVED
- LIGHT_USE
- MODERATE_USE
- HEAVY_USE
- CONCENTRATED_USE
- RECOVERING
- UNKNOWN

These are narrative/ecological summaries. They do not grant terrain tags or combat modifiers.

### HERBIVORE_USE_EVENT

```yaml
herbivore_use_event_id: null
grazing_unit_id: null
collective_or_herd_ref: null
observed_from: null
observed_until: null
use_type: grazing|browsing|resting|wallowing|crossing|watering|sheltering|unknown
intensity_class: null
observer_refs: []
evidence_refs: []
confidence: null
```

This records observed use, not assumed ecological consequence.

### MANAGED_HERD

This is an institutional/household management object linked to persistent Pokémon entities or cohorts.

```yaml
managed_herd_id: null
institution_or_household_ref: null
pokemon_entity_ids: []
cohort_refs: []
species_refs: []
handler_refs: []
workplace_ref: null
residence_or_range_refs: []
material_output_refs: []
care_refs: []
movement_plan_refs: []
ownership_claim_refs: []
custody_refs: []
```

Management does not imply one mechanical controller in battle.

Ownership, custody, residence and partnership remain separate.

### RANGE_USE_PLAN

```yaml
range_use_plan_id: null
grassland_system_id: null
actor_or_institution_ref: null
valid_from: null
valid_until: null
allowed_unit_ids: []
rest_unit_ids: []
water_access_refs: []
seasonal_constraints: []
drought_condition_refs: []
conservation_condition_refs: []
source_refs: []
status: proposed|active|paused|superseded|completed
```

A range-use plan is institutional intent. It does not rewrite actual herd movement.

### FORAGE_OBSERVATION

```yaml
forage_observation_id: null
grazing_unit_id: null
observed_at: null
observer_ids: []
vegetation_height_class: null
cover_class: null
litter_class: null
palatable_resource_class: null
flowering_resource_refs: []
method_ref: null
source_refs: []
```

Do not translate this into HP recovery, Food Buffs or automatic grazing capacity.

### GRAZING_PRESSURE_REVISION

```yaml
grazing_pressure_revision_id: null
grazing_unit_id: null
valid_from: null
valid_until: null
use_class: null
collective_refs: []
managed_herd_refs: []
evidence_refs: []
confidence: null
supersedes_id: null
```

This is an assessment derived from observations, not a direct count of loaded Minecraft entities.

### CONGREGATION_HOTSPOT

```yaml
congregation_hotspot_id: null
grazing_unit_id: null
feature_ref: null
feature_type: water|shade|feeding_point|gate|salt_or_mineral_site|shelter|route_chokepoint|other
use_event_refs: []
soil_observation_refs: []
vegetation_observation_refs: []
runoff_or_erosion_refs: []
status: active|seasonal|inactive|unknown
```

A hotspot can be much more disturbed than the surrounding range.

### HERD_ROUTE_REVISION

```yaml
herd_route_revision_id: null
collective_or_herd_ref: null
valid_from: null
valid_until: null
route_trace_ref: null
stopover_or_water_refs: []
season_ref: null
source_refs: []
confidence: null
supersedes_id: null
```

Routes can change because of forage, water, fences, roads, settlement growth, fire, drought or disturbance.

Do not infer motive without evidence.

### WALLOW_OR_DISTURBANCE_SITE

```yaml
disturbance_site_id: null
grassland_system_id: null
location_ref: null
origin_claim_ref: null
observed_at: null
surface_state_ref: null
water_retention_refs: []
vegetation_response_refs: []
use_event_refs: []
```

This can represent a persistent depression, churned patch or repeatedly disturbed microsite.

It has no combat effect unless an authored PTU terrain rule is separately validated.

### RANGE_CONDITION_ASSESSMENT

```yaml
range_condition_assessment_id: null
grazing_unit_ids: []
assessment_date: null
assessor_refs: []
vegetation_evidence_refs: []
soil_evidence_refs: []
water_evidence_refs: []
herbivore_use_refs: []
fire_refs: []
drought_refs: []
conclusion: null
confidence: null
supersedes_id: null
```

Two assessments can disagree because they sampled different patches, dates or criteria.

## Wild collectives versus managed herds

A single species can appear in both systems.

Example:

```text
Bouffalant species
→ wild collective A
→ visible subgroup A3
→ current grassland use event

Wooloo species
→ managed herd B
→ individual persistent Pokémon entities/cohorts
→ workplace/material-culture relationships
```

Never merge them because they occupy the same pasture.

A wild Pokémon entering a managed range does not become owned.

A released former partner joining a wild collective keeps its persistent Pokémon identity.

## Grazing mosaics

Grasslands should preserve spatial heterogeneity.

A simple state can be:

```yaml
mosaic_revision:
  light_use_units: []
  moderate_use_units: []
  heavy_use_units: []
  recovering_units: []
  unused_units: []
```

This is more useful than one global `grassland_condition` number.

Possible world consequences, only after evidence:

- different vegetation height/cover;
- changed litter accumulation;
- changed flowering resources;
- changed soil exposure;
- different use by small Pokémon;
- altered fire fuel structure;
- changed water-point pressure;
- changed travel visibility.

None of these becomes a PTU effect automatically.

## Fire–grazing interaction

Wildfire owns burn state.

Grasslands may consume burn/recovery revisions as drivers of forage use.

Flow:

```text
burn patch authored/observed
→ Flora records regrowth
→ Grassland layer records changed herbivore use
→ Soil/Flora record follow-up observations
→ later condition assessment
```

Never use:

```text
recent burn
→ herd gets buff
```

## Drought–grazing interaction

Aridity owns drought state.

Grasslands may alter range-use assessments when:

- water points fail;
- forage availability changes;
- dry-season concentration increases;
- ground cover becomes more vulnerable;
- recovery time lengthens.

A drought does not automatically make grazing harmful. The evidence must be location- and time-specific.

## Water-point pressure

Freshwater owns the water source.

Grasslands own use/congregation around it.

A water point can create:

- a predictable herd stop;
- trampling concentration;
- competition among groups;
- a wildlife observation location;
- a disease-surveillance sampling site;
- a route dependency;
- a conservation conflict.

Do not infer aggression simply because multiple groups use one water source.

## Managed herd livelihoods

A managed herd may connect to:

- workplaces;
- material production;
- care;
- breeding/nurseries;
- finance;
- food systems;
- local culture;
- public events;
- transport or land access.

The layer stores those relationships but does not define yields.

Example:

```text
Wooloo herd
→ seasonal shearing event
→ material batch provenance
→ local workshop
→ garment commission
```

Mechanical item effects remain separate.

## Herd leadership and social interpretation

Leadership must be species- or observation-supported.

Allowed states:

- observed follower behavior;
- repeated route initiation;
- species-authored hierarchy evidence;
- handler-reported leadership;
- uncertain social structure.

Prohibited shortcuts:

- biggest Pokémon = leader;
- highest Level = leader;
- strongest battle performance = leader;
- first spawned entity = leader;
- captured individual = owner of the group.

## Grassland use and public belief

Residents may describe a field as:

- overgrazed;
- abandoned;
- healthy;
- ruined;
- restored;
- invaded;
- underused.

These remain claims until tied to observations/assessments.

A visually short grassland may be a normal heavily used patch, a seasonal state, a restoration treatment, drought stress or actual degradation.

## Minecraft/Cobblemon projection

Minecraft can render coarse state:

- vegetation variants;
- worn paths;
- temporary fences/gates;
- troughs/water points;
- wallow depressions;
- herd presence;
- signs/closures;
- ranch facilities;
- seasonal material-production events.

Loaded entity count must not become the population or grazing-pressure authority.

Preferred flow:

```text
authoritative grassland state
→ projection policy
→ representative Cobblemon entities / vegetation / props
→ player observations
→ state updates only through validated systems
```

## PTU/AutoPTU authority boundary

Available Python AutoPTU evidence recognizes `grassland` as an environment label and contains specific authored mechanics tied to it.

That proves only those exact interactions.

It does not prove:

- generic herd movement;
- stampede;
- trampling;
- grazing;
- grass-height cover;
- pasture capacity;
- forage healing;
- animal handling;
- mounted herding;
- group retreat;
- fence collision;
- herd morale;
- grassland weather;
- population scaling.

Naturewalk, Pack Mon, Mountable, Run Away, Sap Sipper and similar capabilities/Abilities must be validated individually before any mechanical use.

## Encounter implementation contracts

### 1. Waterpoint Crossing — FULL

Premise:

A persistent wild herd reaches a shared water point during a period of unusually concentrated use. A managed herd is expected to cross the same access corridor shortly afterward. The player objective is to prevent escalation and keep a passage open without treating either group as disposable enemies.

Intended full version:

- several moving groups with distinct goals;
- protected/crossing lane;
- retreat and avoidance behavior;
- possible interception if combat begins;
- dynamic occupancy around the water point;
- tactical AI that understands EXIT/CROSS/AVOID rather than only KO.

Required capability categories:

- targeting/footprints/range/LoS — VERIFIED for geometry;
- base movement legality — VERIFIED for current static modes;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if real statuses appear;
- terrain/weather/hazards/zones/reactions — BLOCKING for protected/dynamic zones;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

Resolve group movement and separation in overworld state before battle. If a combat encounter occurs, use one static shoreline/grassland arena with only the combatants actually involved. Other herd members remain off-grid. No stampede, trampling or herd morale mechanic is inferred.

### 2. Burn Patch Survey — FULL

Premise:

A recently burned grassland patch is attracting heavy use. Researchers want observations while a wild collective moves through the area.

Intended full version:

- spatial mosaic of burned/recovering/ungrazed patches;
- moving wildlife with withdrawal goals;
- possible dynamic fire-remnant hazards only if PTU rules support them;
- observation objective that can succeed without combat.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED for static geometry;
- complete movement — BLOCKING if movement objectives/interception matter;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle/damage/status/move/Ability/item/Feature families — PARTIAL as applicable;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:

Fire and vegetation state are resolved before combat. Use a static map. The survey objective remains overworld/research state. AutoPTU is invoked only for a conventional conflict.

### 3. Broken Fence at Dusk — FULL

Premise:

A managed herd and several wild Pokémon are using a gap in a boundary near a road. The problem is restoring safe movement and custody, not defeating every Pokémon.

Intended full version:

- herd members trying to leave or return;
- road/vehicle timing state;
- dynamic gate/fence interactable;
- handlers and civilians with protection goals;
- withdrawal/surrender options;
- tactical AI aware of escape and containment.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- damage/status/move/Ability/item/Feature families — PARTIAL;
- terrain/hazards/zones/reactions — BLOCKING for dynamic gate/road zones;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:

Resolve animal positions, road closure and fence repair outside battle. Any hostile encounter occurs separately on a fixed map. Do not use forced movement or containment mechanics.

## Promotion gate for any grassland encounter

Before moving a proposal toward canon or implementation:

1. Identify exact persistent grassland/collective objects involved.
2. Separate ecological observation from interpretation.
3. Identify which actors are wild collectives versus managed herds.
4. Validate ownership/custody for managed Pokémon.
5. Validate any PTU capability/Feature/Ability used.
6. List every battle capability family required by the FULL version.
7. Provide a REDUCED version whenever blocked families are non-essential to the premise.
8. Keep Minecraft representation downstream of authoritative world state.
9. Do not infer spawn rarity, item yield, status, terrain or combat bonuses from narrative grazing state.

## Canon questions still open

- Which Ouros regions contain major grassland systems?
- Which herd species and ranching traditions are established before player arrival?
- Which species-specific social structures are canon versus merely observed?
- How are managed herds represented legally: ownership, custody, workplace association or another model?
- Which PTU/Caelo rules apply to Pack Mon, Naturewalk (Grassland), Mountable, Run Away and herd handling?
- How should offline herd-route advancement work?
- How should wild collectives and managed herds coexist without every encounter becoming a capture opportunity?
- How much grassland vegetation change should be projected physically into Minecraft?