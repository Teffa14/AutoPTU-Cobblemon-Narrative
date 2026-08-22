# Ouros Urban Wildlife, Synanthropy & Coexistence Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

Pass: 112.

## Purpose

This layer owns persistent relationships between wild Pokémon and human-built environments: repeated use of streets, roofs, parks, drains, markets, utility spaces and buildings; attractants; roosts/nests; habituation observations; food-conditioning evidence; conflict reports; coexistence measures; and follow-up outcomes.

It does not replace:

- Urban Public Space for shared-space identity and programming;
- Waste/Sanitation for refuse and treatment state;
- Architecture for buildings and physical revisions;
- Light for lightscape state;
- Soundscapes for acoustic state;
- Technology for electrical/mechanical assets;
- Road Ecology for road crossings;
- Diel Activity for activity timing;
- Conservation for management objectives;
- Wild Collectives for population/group identity;
- Pokémon Agency for persistent individual Pokémon identity;
- PTU/AutoPTU for battle mechanics.

It does not define nuisance law, capture legality, disease, feeding penalties, generic urban Terrain, crowd combat rules or universal deterrent mechanics.

## Core principle

Urban wildlife is a relationship among Pokémon, resources, structures, routines and people. The system should not encode a species as a permanent problem.

A useful separation is:

`URBAN HABITAT USE -> OBSERVATION -> ATTRACTANT/CONTEXT EVIDENCE -> BEHAVIORAL INTERPRETATION -> CONFLICT OR COEXISTENCE RESPONSE -> FOLLOW-UP`

Each step remains independently revisable.

## 1. Urban wildlife profile

```yaml
urban_wildlife_profile:
  profile_id: null
  settlement_id: null
  population_or_collective_ref: null
  species_ref: null
  known_individual_ids: []
  primary_use_zone_refs: []
  recurring_site_ids: []
  activity_profile_refs: []
  attractant_relation_ids: []
  habituation_observation_ids: []
  food_conditioning_observation_ids: []
  conflict_incident_ids: []
  coexistence_intervention_ids: []
  current_assessment_id: null
  provenance_refs: []
  canon_status: proposed
```

A profile may represent one local population, collective or recurring group. It must not silently merge every member of a species across a city.

## 2. Urban use sites

A site should persist even when no Pokémon are currently loaded there.

```yaml
urban_wildlife_use_site:
  site_id: null
  location_ref: null
  structure_ref: null
  public_space_ref: null
  site_type: null
  current_physical_revision_ref: null
  known_population_refs: []
  known_individual_refs: []
  observation_ids: []
  use_window_refs: []
  attractant_ids: []
  nesting_or_roost_refs: []
  disturbance_refs: []
  management_refs: []
```

Candidate site types:

- ROOFTOP
- LEDGE
- EAVE
- BRIDGE_VOID
- STATION_CANOPY
- MARKET_EDGE
- ALLEY
- PARK
- PLAZA
- DRAIN_OR_CULVERT
- UTILITY_ASSET_EDGE
- WASTE_TRANSFER_EDGE
- WATERFRONT
- VACANT_STRUCTURE
- STREET_TREE_CORRIDOR
- UNDERPASS
- OTHER_AUTHORED

Site type is descriptive. It does not create battle Terrain.

## 3. Attractants and resources

Human activity can produce resources that alter local Pokémon use.

```yaml
urban_attractant:
  attractant_id: null
  location_ref: null
  attractant_type: null
  source_ref: null
  availability_window_ref: null
  quantity_band: unknown
  persistence_band: unknown
  access_condition_refs: []
  observed_user_population_refs: []
  observed_individual_refs: []
  observation_ids: []
  mitigation_refs: []
  current_state: unknown
```

Candidate descriptive types:

- INTENTIONAL_FEEDING
- FOOD_SERVICE_RESIDUE
- HOUSEHOLD_FOOD
- WASTE
- COMPOST
- FRUITING_TREE
- INSECT_AGGREGATION
- ARTIFICIAL_LIGHT
- HEAT_SOURCE
- ELECTRICAL_SOURCE
- WATER_SOURCE
- SHELTER
- NESTING_STRUCTURE
- OTHER_AUTHORED

An attractant is not automatically harmful. Its consequences require observations.

## 4. Habituation observations

Habituation should never be a hidden global meter.

```yaml
habituation_observation:
  observation_id: null
  actor_or_population_ref: null
  location_ref: null
  observed_at: null
  observer_refs: []
  human_distance_band: null
  human_activity_context: null
  observed_response: null
  food_present: unknown
  repeated_exposure_context: unknown
  comparison_refs: []
  confidence_band: null
  source_refs: []
```

Possible observed responses:

- AVOIDS
- WITHDRAWS_LATE
- CONTINUES_ACTIVITY
- APPROACHES
- APPROACHES_ONLY_WITH_RESOURCE
- USES_STRUCTURE_WITH_PEOPLE_PRESENT
- UNKNOWN

This remains observation. It does not assert friendliness, tameness, aggression or capture difficulty.

## 5. Food-conditioning evidence

Food conditioning needs stronger evidence than simple tolerance.

```yaml
food_conditioning_case:
  case_id: null
  actor_or_population_ref: null
  attractant_refs: []
  repeated_observation_ids: []
  approach_behavior_refs: []
  alternative_explanations: []
  current_assessment: uncertain
  reviewed_at: null
  reviewer_refs: []
```

Candidate assessment states:

- INSUFFICIENT_EVIDENCE
- POSSIBLE
- SUPPORTED
- NOT_SUPPORTED
- SUPERSEDED

Never infer `FOOD_CONDITIONED` from one feeding scene.

## 6. Roosts, nests and juvenile presence

A nest or roost has identity separate from the currently visible occupants.

```yaml
urban_roost_or_nest:
  roost_id: null
  site_ref: null
  builder_or_user_claims: []
  species_claims: []
  known_individual_refs: []
  first_observed_at: null
  last_observed_at: null
  activity_windows: []
  juvenile_observation_ids: []
  maintenance_or_building_work_refs: []
  disturbance_ids: []
  current_status: unknown
```

Candidate status values:

- ACTIVE_CONFIRMED
- ACTIVE_POSSIBLE
- INACTIVE_CURRENTLY
- ABANDONED_SUPPORTED
- DESTROYED
- UNKNOWN

A juvenile observed alone does not establish abandonment.

## 7. Conflict incident

A conflict is an event, not a species trait.

```yaml
urban_wildlife_conflict_incident:
  incident_id: null
  occurred_at: null
  location_ref: null
  involved_population_refs: []
  involved_individual_refs: []
  human_actor_refs: []
  conflict_type: null
  observed_harm_refs: []
  reported_harm_claims: []
  attractant_refs: []
  infrastructure_refs: []
  evidence_refs: []
  response_refs: []
  case_refs: []
  current_status: open
```

Candidate conflict types:

- FOOD_ACCESS
- PROPERTY_DAMAGE
- UTILITY_INTERACTION
- ROOST_OR_NEST_CONFLICT
- TRAFFIC_OR_TRANSIT_CONFLICT
- CROWD_AGGREGATION
- NOISE_CONFLICT
- LIGHT_ASSOCIATION
- WASTE_ASSOCIATION
- MARKET_OR_EVENT_CONFLICT
- PET_OR_MANAGED_POKEMON_INTERACTION
- OTHER_AUTHORED

Do not infer culpability from a complaint alone.

## 8. Coexistence intervention

Interventions need scope, target and follow-up.

```yaml
coexistence_intervention:
  intervention_id: null
  incident_or_profile_refs: []
  intervention_type: null
  target_resource_or_site_refs: []
  responsible_actor_refs: []
  authorized_by_refs: []
  started_at: null
  ended_at: null
  intended_outcome: null
  implementation_refs: []
  follow_up_observation_ids: []
  observed_outcome: unknown
  unintended_effect_refs: []
```

Candidate intervention types:

- ATTRACTANT_REMOVAL
- WASTE_CONTAINMENT
- FEEDING_PRACTICE_CHANGE
- LIGHTING_CHANGE
- STRUCTURE_ACCESS_CHANGE
- ROUTINE_CHANGE
- TEMPORARY_SITE_BUFFER
- ALTERNATIVE_HABITAT_SUPPORT
- DETERRENCE_AUTHORED
- MONITORING_ONLY
- OTHER_AUTHORED

The intervention does not automatically work.

## 9. Public perception

Public perception is separate from ecological or behavioral state.

A population can be:

- widely loved but genuinely causing an infrastructure problem;
- widely disliked while causing little measurable harm;
- newly visible because observation effort increased;
- blamed for a problem that began before it arrived;
- celebrated as part of district identity while still needing practical coexistence measures.

Media/Public Memory owns public narratives. This layer only links those narratives to the relevant wildlife observations and incidents.

## 10. Time and persistence

Urban relationships should evolve across months and years.

Examples:

- a new market creates food residue;
- a Pidove aggregation grows around feeding behavior;
- sanitation and outreach reduce the attractant;
- the flock redistributes to several ordinary feeding sites;
- a new light installation attracts nocturnal Pokémon;
- a building renovation closes an old roost;
- a nearby park gains a new recurring group;
- residents who once complained later treat the population as part of neighborhood identity.

None of these transitions require a quest generator.

## 11. Multiplayer privacy and agency

Player feeding, photography or observation can be recorded as actions if performed.

Do not infer from those actions that a PC:

- loves the species;
- wants to capture it;
- supports a management policy;
- fears it;
- accepts property damage;
- has bonded with a specific Pokémon.

Irreversible actions affecting another player's Pokémon remain governed by Pokémon Agency and multiplayer consent rules.

## 12. Minecraft projection

Minecraft may display:

- recurring wild Pokémon at coarse approved sites;
- nests/roosts as blocks or structure markers;
- secured/unsecured waste presentation;
- lighting changes;
- signs or public information;
- temporary buffers;
- camera traps or survey assets.

Minecraft loaded entities are not population truth.

A chunk reload must not:

- reset habituation history;
- recreate a removed attractant;
- duplicate a persistent Pokémon;
- repopulate an abandoned nest as active;
- clear conflict history;
- manufacture a rare spawn because a player repeatedly manipulates food, light or blocks.

## 13. Cobblemon projection

Spawn/presence projection must be coarse, server-authoritative and exploit-resistant.

Player actions such as dropping food, placing torches or exposing trash do not directly modify rare-spawn tables.

If a long-term urban response is ever allowed, the flow should be:

`validated world-state change -> reviewed ecological/behavioral response -> bounded population/presence projection -> Cobblemon presentation`

## 14. Battle boundary

This layer must never invent tactical mechanics.

Examples of forbidden automatic conversions:

- urban site -> Urban Terrain;
- feeding site -> capture bonus;
- habituated Pokémon -> reduced Evasion;
- flock -> Pack Mon;
- roost -> defensive zone;
- trash -> Poisoned hazard;
- outlet use -> Electric hazard;
- bright light -> accuracy modifier;
- resident complaint -> hostile AI;
- deterrent -> Fear/Flinch/status;
- crowding -> initiative modifier.

When combat occurs, AutoPTU receives only a validated battle snapshot using mechanics already supported by PTU/Java.

## 15. Encounter contracts

### Rooftop Roost Maintenance Conflict — FULL

Premise: scheduled building maintenance overlaps with an active urban roost and an unrelated disturbance causes a confrontation while workers must withdraw safely.

Intended full version:

- workers move toward safe exits;
- wild Pokémon can withdraw to alternate roost access;
- protected subareas remain noncombat objectives;
- tactical AI understands `WITHDRAW`, `PROTECT_ROUTE`, `CLEAR_WORK_ZONE`;
- Minecraft shows the roof, workers, roost and changing operational state.

Reduced version:

Pause maintenance in world state. Move workers out before battle. Freeze one legal rooftop arena that excludes the nest/roost object. Run only the actual combatants. Resume assessment after battle. Victory does not decide whether the roost remains active or whether maintenance may continue.

### Market Feeding Surge — FULL

Premise: repeated visitor feeding has concentrated a large urban group around a market, and a new incident requires dispersal without treating the whole population as enemies.

Intended full version:

- noncombat Pokémon move toward/away from attractants;
- civilians and stalls create changing route constraints;
- tactical AI can withdraw/disperse instead of seeking KO;
- world state updates attractant and feeding practices independently of battle.

Reduced version:

Close the food-service section and evacuate civilians through world state. Resolve ordinary background Pokémon as population movement outside the grid. If a smaller subset remains in real conflict, use one static battle. Afterwards update the attractant/intervention record rather than declaring the flock defeated.

### Utility Alcove Joltik Investigation — FULL

Premise: recurring electrical anomalies and repeated Joltik observations overlap at a utility alcove, but causality remains unproven.

Intended full version:

- technicians inspect interactable infrastructure;
- wild Pokémon may retreat through small access routes;
- power-state changes can be represented only if validated mechanics exist;
- tactical AI understands `WITHDRAW` and `PROTECT_TECHNICIAN`.

Reduced version:

Inspect and isolate the electrical asset in world state first. Freeze power state before combat. If confrontation occurs, AutoPTU receives a normal static arena with no electrical floor hazard. Technical diagnosis occurs after battle and may still find a non-Pokémon cause.

## 16. Longer-term world arcs

### The Pidove Square Years

Year 1: a small plaza becomes known for casual feeding.

Year 2: observations show larger aggregations during specific windows.

Year 3: the city changes waste bins and feeding guidance; media overstates the effect before follow-up data exists.

Year 4: the population redistributes across several nearby blocks rather than disappearing.

Year 5: the square's public identity now includes both the historical feeding culture and a more deliberate coexistence practice.

The arc can remain completely noncombat.

### The Night-Lights Experiment

A district installs brighter lighting, after which nocturnal Pokémon observations shift. Researchers, residents, businesses and astronomers disagree about what matters most. Several blocks test different lighting revisions over multiple years. Results vary by species and site. No universal `best light` is produced.

### The Buildings That Became Habitat

A warehouse district gradually changes use. Empty buildings, renovations, rooftop gardens and new transit produce successive roost/nest opportunities. Persistent Pokémon and local groups move among structures. Architecture, Public Space, Demography and Wildlife histories become readable together after a decade of world time.

## 17. Canon gates

Before any candidate becomes canon, decide:

- which urban Pokémon populations already exist at campaign start;
- which associations with specific structures are authored;
- which behaviors come from species canon versus local observations;
- which institutions monitor or respond to conflicts;
- what access/management authority exists;
- how much population state advances offline;
- what data is public;
- which coexistence interventions are culturally normal in each region.

Until then, all generated examples remain proposals.