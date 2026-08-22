# Kelp, Seagrass & Submerged Vegetation Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanic is established by this document.

Pass: 94

## Purpose

This layer represents persistent submerged vegetation as habitat, landscape structure and ecological history.

It owns kelp-forest identity, seagrass-meadow identity, submerged-vegetation extent revisions, vertical habitat bands, canopy state, bed density, recruitment observations, detached vegetation events, grazer-pressure observations, restoration cohorts and evidence-backed habitat use.

It does not own tides, shoreline geomorphology, open-ocean currents, estuarine salinity, reefs, generic water quality, battle terrain or Minecraft fluid physics.

## Authority boundary

This layer does not replace:

- Maritime for harbors, vessels, sea lanes and submerged travel locations;
- Open Ocean for pelagic state, offshore water masses and drifting habitat after it leaves the nearshore system;
- Estuaries for salinity gradients and tidal wetlands;
- Coral Reef for reef structure, coral condition and reef restoration;
- Intertidal for repeated exposure/submergence at the shoreline edge;
- Coastal Geomorphology for shoreline, substrate and sedimentary physical change;
- Fisheries for fishing effort, catches, stock assessment and aquaculture;
- Interspecies Ecology for persistent predator/prey/competition relationships;
- Conservation for stewardship, protected status and management decisions;
- Science for hypotheses, datasets and publication;
- AutoPTU for terrain, visibility, movement, hazards, damage, status and battle resolution.

Minecraft projects the current vegetation revision. Loaded blocks or entities never define authoritative habitat state.

## Core separation

Keep these distinct:

submerged habitat identity -> physical extent/structure revision -> observation -> ecological interpretation -> management/restoration action -> future revision -> Cobblemon projection -> battle snapshot.

Examples:

- dense visible kelp does not prove full ecological recovery;
- one juvenile Pokémon does not prove nursery function;
- a grazer species is not automatically harmful;
- detached kelp does not remain the same spatial object as the attached forest;
- seagrass near a harbor does not imply the harbor caused its decline;
- a Skrelp hidden among seaweed does not grant generic Stealth to all Pokémon there;
- a Dhelmise near wreck debris does not prove the debris created it;
- underwater vegetation does not create PTU Terrain until a verified mechanic says so.

## SUBMERGED_VEGETATION_SYSTEM

```yaml
submerged_vegetation_system_id: null
system_class: kelp_forest|seagrass_meadow|mixed_sav|macroalgal_bed|other|unknown
maritime_region_ref: null
coastal_segment_refs: []
estuary_refs: []
reef_refs: []
vegetation_unit_ids: []
monitoring_program_refs: []
conservation_refs: []
history_refs: []
canon_status: proposed
```

A system is a persistent ecological identity, not a PTU field effect.

## SUBMERGED_VEGETATION_UNIT

```yaml
submerged_vegetation_unit_id: null
system_id: null
substrate_ref: null
depth_band: shallow|mid_depth|deep_edge|variable|unknown
exposure_class: sheltered|moderate|exposed|variable|unknown
extent_revision_ids: []
structure_revision_ids: []
condition_observation_ids: []
recruitment_observation_ids: []
habitat_use_observation_ids: []
disturbance_event_ids: []
restoration_project_ids: []
```

A unit should be coarse enough to survive Minecraft block changes. It is not one plant, one chunk or one battle grid.

## VEGETATION_EXTENT_REVISION

```yaml
vegetation_extent_revision_id: null
unit_id: null
observed_at: null
footprint_ref: null
mapping_method: diver_transect|underwater_video|surface_canopy|remote_survey|player_survey|mixed|unknown
coverage_class: absent|trace|sparse|patchy|continuous|dense|unknown
source_refs: []
confidence: null
supersedes_id: null
```

Old revisions remain valid historical records.

## VEGETATION_STRUCTURE_REVISION

Kelp and seagrass need different structural vocabularies.

```yaml
vegetation_structure_revision_id: null
unit_id: null
observed_at: null
structure_class: canopy_forest|midwater_forest|low_bed|meadow|patches|barren|recovering|other|unknown
vertical_band_refs: []
canopy_presence: none|partial|continuous|unknown
bed_density_class: low|moderate|high|variable|unknown
holdfast_or_rhizome_condition_ref: null
source_refs: []
supersedes_id: null
```

Do not convert `dense` into cover, concealment or movement cost automatically.

## VERTICAL_HABITAT_BAND

```yaml
vertical_habitat_band_id: null
unit_id: null
band_class: surface_canopy|upper_water|midwater|understory|seafloor|meadow_blade_zone|other|unknown
geometry_ref: null
light_context_ref: null
water_movement_context_ref: null
observed_entity_refs: []
observed_collective_refs: []
source_refs: []
```

This is ecological verticality. It does not require a 3D tactical engine.

## CONDITION_OBSERVATION

```yaml
submerged_vegetation_condition_observation_id: null
unit_id: null
observer_id: null
observed_at: null
observation_type: canopy_extent|blade_condition|density|breakage|sediment_cover|epiphyte_load|grazing_sign|detachment|other
raw_value: null
method_ref: null
weather_ref: null
water_quality_ref: null
media_refs: []
source_refs: []
confidence: null
```

Condition observations are facts about what was measured or seen. Cause belongs in Science hypotheses.

## RECRUITMENT_OBSERVATION

```yaml
recruitment_observation_id: null
unit_id: null
observed_at: null
target: kelp|seagrass|other_sav|associated_species|unknown
life_stage: propagule|seedling|juvenile|young_plant|unknown
count_or_density_ref: null
method_ref: null
source_refs: []
confidence: null
```

A planted unit is not recovered until later recruitment/survival evidence supports that claim.

## HABITAT_USE_OBSERVATION

```yaml
submerged_habitat_use_observation_id: null
unit_id: null
observed_at: null
entity_refs: []
collective_refs: []
use_type: shelter|foraging|resting|spawning|juvenile_use|ambush|transit|territorial|unknown
life_stage_ref: null
vertical_band_ref: null
media_refs: []
source_refs: []
confidence: null
```

Do not infer emotional or tactical motives beyond observable behavior.

## NURSERY ASSESSMENT

```yaml
nursery_assessment_id: null
unit_id: null
valid_period_ref: null
target_population_refs: []
evidence_refs: []
assessment: supported|possible|unsupported|insufficient_data|unknown
reviewer_ref: null
supersedes_id: null
```

Nursery is an evidence-backed ecological function, not a default property of every underwater plant bed.

## GRAZER_PRESSURE_OBSERVATION

```yaml
grazer_pressure_observation_id: null
unit_id: null
observed_at: null
grazer_population_refs: []
feeding_sign_refs: []
density_observation_refs: []
vegetation_response_refs: []
predator_context_refs: []
source_refs: []
```

A grazer can be normal, overabundant, recovering or simply present. Avoid moral categories.

## HABITAT_STATE_TRANSITION

```yaml
submerged_habitat_transition_id: null
unit_id: null
from_revision_ref: null
to_revision_ref: null
observed_between: null
transition_class: canopy_loss|fragmentation|bed_expansion|barren_shift|recruitment|storm_damage|sediment_burial|recovery|other|unknown
cause_hypothesis_refs: []
evidence_refs: []
```

The transition can be factual while its cause remains disputed.

## DETACHED_VEGETATION_EVENT

```yaml
detached_vegetation_event_id: null
source_unit_id: null
occurred_at: null
estimated_material_class: low|moderate|large|unknown
cause_hypothesis_refs: []
drift_path_ref: null
open_ocean_habitat_ref: null
stranding_event_ref: null
source_refs: []
```

Once detached material becomes a drifting habitat, Open Ocean may own its current location and trajectory.

## RESTORATION PROJECT

```yaml
submerged_vegetation_restoration_project_id: null
unit_ids: []
started_at: null
objective_refs: []
baseline_refs: []
intervention_class: transplant|outplant|seed|grazer_management|access_management|water_quality_support|mixed|other|unknown
cohort_ids: []
monitoring_schedule_ref: null
followup_observation_ids: []
status: proposed|approved|active|paused|complete_intervention|monitoring|closed|unknown
outcome_assessment_ref: null
```

`complete_intervention` must not be treated as `restored`.

## RESTORATION COHORT

```yaml
restoration_cohort_id: null
project_id: null
source_provenance_ref: null
placement_ref: null
placed_at: null
quantity_or_area_ref: null
survival_observation_ids: []
recruitment_observation_ids: []
loss_observation_ids: []
```

Cohorts preserve provenance and allow several restoration methods to be compared without collapsing them into one success value.

## WATER QUALITY AND LIGHT HANDOFF

This layer consumes, but does not own:

- turbidity / water-clarity observations;
- pollution or nutrient hypotheses;
- sedimentation events;
- heat-stress context;
- local light availability;
- current/wave context.

The system may record correlation. Science remains responsible for causal claims.

## SPECIES LORE GUARDRAILS

### Skrelp

May seed authored hypotheses or local observations around drifting seaweed, concealment and storm displacement.

Never infer:
- universal kelp dependency;
- Stealth bonus;
- Poisoned environment;
- guaranteed Dragalge presence.

### Dragalge

May support authored territorial or ambush observations where the species is present.

Never infer:
- automatic zone control;
- seaweed cover modifier;
- environmental poison damage.

### Dhelmise

May connect seaweed habitat with wreck/debris provenance and a persistent individual Pokémon.

Never infer:
- wreck ownership;
- forced movement from anchor imagery;
- automatic spawn around every shipwreck.

### Lileep / Cradily

May support paleobiological comparison with ancient marine habitat.

Never infer that a fossil-restored Pokémon recreates the ancient ecosystem or that Suction Cups creates world physics.

## MINECRAFT PROJECTION

Minecraft may show:

- canopy density variants;
- seagrass-bed footprint;
- sparse/barren/recovering visual states;
- restoration markers;
- underwater survey stakes;
- detached mats;
- wreck-kelp overlap;
- visitor buoys or protected zones.

Minecraft must not decide:

- nursery status;
- cause of decline;
- movement cost;
- concealment;
- combat cover;
- oxygen or suffocation;
- current strength;
- Poisoned/Burned/Slowed/Stuck;
- rare-spawn multipliers;
- restoration success.

## COBBLEMON PROJECTION

The habitat layer may produce coarse ecological opportunity weights after server validation.

Rules:

- loaded entity count is never population truth;
- placing kelp blocks cannot directly raise rare-spawn chance;
- restoration cannot directly spawn a rare Pokémon as reward;
- observed species use can influence authored opportunity only through controlled ecology projections;
- persistent important Pokémon keep their entity IDs across habitat changes.

## BATTLE SNAPSHOT POLICY

Before AutoPTU begins, the server freezes only supported battle geometry and rule state.

A kelp/seagrass snapshot may safely provide static blockers or water tiles only where the existing battle contract already supports them.

Do not dynamically create from prose:

- concealment;
- entanglement;
- current zones;
- kelp pull;
- wave push;
- oxygen depletion;
- salinity effects;
- poison clouds;
- dynamic canopy collapse;
- vegetation healing;
- Grass Terrain;
- Water Terrain;
- Accuracy penalties.

## ENCOUNTER CONTRACT — Kelp Transect Recovery

Premise:
A long-term monitoring transect stops reporting after a storm. The players recover equipment, verify which canopy segments were lost and determine whether a visible barren is new or older than the storm.

FULL VERSION dependencies:

- targeting/footprints/range/LoS: VERIFIED for static combat geometry;
- base movement legality: VERIFIED;
- complete movement: BLOCKING if moving kelp/current displaces actors;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- lifecycle: PARTIAL;
- damage pipeline: PARTIAL;
- statuses: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING for current, entanglement or dynamic vegetation;
- move-specific behavior: PARTIAL;
- abilities/items/Trainer Features: PARTIAL as needed by actual combatants;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for WITHDRAW / PROTECT_DIVER / REACH_TRANSECT;
- adapter/playback: BLOCKING.

REDUCED VERSION:
The server resolves storm damage, route safety and equipment recovery in overworld state. If combat occurs, the party enters a fixed underwater arena with supported Swim movement and static geometry. Kelp remains visual unless a verified PTU mechanic is explicitly projected.

## ENCOUNTER CONTRACT — Seagrass Nursery Survey

Premise:
A shallow meadow thought to be important juvenile habitat shows fewer observations during one survey season. Several explanations remain plausible.

FULL VERSION dependencies:

- static targeting and base movement: VERIFIED;
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where used;
- terrain/weather/hazards/zones/reactions: BLOCKING if blade density, turbidity or shallow-water state changes combat;
- tactical AI: BLOCKING for AVOID_JUVENILES / WITHDRAW / PROTECT_SAMPLE_SITE;
- adapter/playback: BLOCKING.

REDUCED VERSION:
Survey work and nursery inference stay outside battle. Any confrontation is moved to a fixed adjacent patch that does not assign mechanical effects to the meadow.

## ENCOUNTER CONTRACT — Barren Restoration Watch

Premise:
A restoration plot begins showing new vegetation after a long barren period. Players monitor the site while conflicting groups argue over what caused the shift and whether intervention should continue.

FULL VERSION dependencies:

- static combat geometry: VERIFIED;
- complete movement: BLOCKING for moving swimmers or protective corridors;
- terrain/weather/hazards/zones/reactions: BLOCKING for grazer zones or vegetation-driven field state;
- tactical AI: BLOCKING for NONLETHAL_WITHDRAW / PROTECT_PLOT;
- adapter/playback: BLOCKING;
- all specific Move/Ability/Feature interactions: require their own parity evidence.

REDUCED VERSION:
The ecological debate, monitoring and restoration remain world-state actions. A conventional static battle occurs only if an independent conflict actually requires it.

## Long-term story support

The same habitat can create stories over years:

storm -> canopy loss -> changed juvenile observations -> fisheries concern -> restoration trial -> grazer/predator monitoring -> partial recovery -> tourism interest -> new management pressure.

Every arrow requires actual stored state or evidence. The generator may propose connections but cannot rewrite them as truth.

## Canon promotion requirements

Before any specific kelp/seagrass region becomes canon, define:

- physical location and system identity;
- initial extent/structure revision;
- authored regional species associations;
- monitoring or stewardship institutions, if any;
- historical disturbance/restoration already established;
- relation to ports, fisheries, reefs, estuaries and settlements;
- which information is public, uncertain or undiscovered;
- any exact PTU/Caelo mechanics that are allowed to project into battle.

Until then, this layer remains a reusable systems proposal.