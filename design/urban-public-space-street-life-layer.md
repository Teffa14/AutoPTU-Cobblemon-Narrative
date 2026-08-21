# Ouros Urban Public Space & Street Life Layer

Status: proposed systems design. Not established Ouros canon.

Pass: 83.

## Purpose

This layer gives shared urban spaces persistent identity and use-history across Architecture, Homes/Neighborhoods, Demography, Travel, Tourism, Events, Social Bonds, Accessibility, Public Memory, Media, Light, Sound, Waste, Conservation and Wild Pokémon ecology.

`design/architecture-built-environment-adaptive-reuse-layer.md` remains authoritative for buildings and physical structure versions.

`design/demography-migration-population-change-layer.md` remains authoritative for resident/visitor/cohort population state.

`design/travel-transport-expedition-layer.md` remains authoritative for routes and transport services.

This layer owns how shared urban spaces are used, programmed, observed and remembered.

It does not define public ownership law, protest law, civilian combat rules, crowd collision, urban PTU Terrain, social Skill DCs, policing powers or spawn bonuses.

## 1. Shared-space identity

A shared urban place should persist independently of today's furniture, event or crowd.

```yaml
urban_public_space:
  public_space_id: null
  settlement_id: null
  district_id: null
  approved_name: null
  known_aliases: []
  space_type: null
  physical_structure_refs: []
  boundary_ref: null
  access_profile_ref: null
  frontage_ids: []
  amenity_ids: []
  time_program_ids: []
  use_observation_ids: []
  pokemon_use_observation_ids: []
  event_refs: []
  public_memory_refs: []
  current_projection_revision_id: null
```

Candidate `space_type` values:

- PLAZA
- PARK
- COMMUNITY_GREEN
- STATION_FORECOURT
- PEDESTRIAN_STREET
- SHARED_STREET
- WATERFRONT_PROMENADE
- LINEAR_PARK
- MARKET_SQUARE
- PLAYGROUND
- COURTYARD
- PUBLIC_STEPS
- ARCADE_PASSAGE
- PUBLIC_GARDEN
- TRANSIT_CONCOURSE
- OTHER_AUTHORED

The type describes spatial/social use. It does not establish legal ownership.

## 2. Access profile

Public use can be broad without being unrestricted.

```yaml
public_space_access_profile:
  access_profile_id: null
  public_space_id: null
  default_access_state: null
  active_hours_ref: null
  mobility_access_refs: []
  temporary_restriction_ids: []
  event_access_refs: []
  stewardship_refs: []
  credential_refs: []
  source_authority_refs: []
```

Useful states include:

- OPEN_SHARED_USE
- OPEN_WITH_TIME_LIMITS
- EVENT_CONTROLLED
- TEMPORARILY_RESTRICTED
- MAINTENANCE_CLOSURE
- ECOLOGICAL_RESTRICTION
- EMERGENCY_RESTRICTION
- UNKNOWN

“Public” never means a player can ignore closures, private subspaces, ecological restrictions or safety state.

## 3. Frontages and edges

Public life often depends on what touches the space.

```yaml
public_space_frontage:
  frontage_id: null
  public_space_id: null
  physical_ref: null
  frontage_type: null
  institution_or_venue_ref: null
  active_hours_ref: null
  access_points: []
  observation_refs: []
  current_state: null
```

Candidate frontages:

- CAFE
- RETAIL
- RESIDENTIAL
- TRANSIT
- CIVIC
- SCHOOL
- CLINIC
- WORKSHOP
- MARKET_STALL_ZONE
- WATERFRONT
- PARK_EDGE
- WILD_HABITAT_EDGE
- BLANK_WALL
- SERVICE_EDGE

A café beside a square can affect foot traffic without owning the square.

## 4. Time-programmed use

A place may change function repeatedly without changing geometry.

```yaml
public_space_time_program:
  program_id: null
  public_space_id: null
  effective_window_ref: null
  recurrence_ref: null
  activity_tags: []
  expected_cohort_refs: []
  service_refs: []
  event_refs: []
  setup_refs: []
  teardown_refs: []
  access_delta_ref: null
  provenance_refs: []
```

Example activity tags:

- COMMUTE
- SCHOOL_ARRIVAL
- LUNCH
- MARKET
- EXERCISE
- CASUAL_SOCIAL
- PERFORMANCE
- FESTIVAL
- EXHIBITION
- NIGHTLIFE
- RESEARCH
- TOURISM
- QUIET_HOURS
- MAINTENANCE

A program predicts likely use. It does not force every NPC to appear.

## 5. Use observations

Actual use remains observational.

```yaml
public_space_use_observation:
  observation_id: null
  public_space_id: null
  observed_at: null
  observer_ids: []
  cohort_refs: []
  activity_tags: []
  coarse_occupancy: null
  occupied_subarea_refs: []
  flow_direction_refs: []
  interruption_refs: []
  source_refs: []
  uncertainty: null
```

Coarse occupancy states:

- EMPTY
- LIGHT
- MODERATE
- BUSY
- VERY_BUSY
- UNKNOWN

These states are narrative/operational observations. They do not create tactical density modifiers.

## 6. Co-presence does not imply relationship

Two actors being in the same square is a fact of co-presence.

It does not prove:

- friendship;
- surveillance;
- conspiracy;
- a meeting;
- romance;
- rivalry;
- shared intent;
- knowledge transfer.

If a meaningful interaction occurs, the Social Bonds, Cases, Communications or Chronicle systems record it separately.

## 7. Routine encounter opportunities

Public spaces create intersections without requiring formal quests.

Possible low-pressure opportunities:

- a recurring vendor recognizes prior customers;
- a researcher returns to the same bench at a predictable time;
- a wild Pokémon uses a fountain edge repeatedly;
- a commuter asks about a changed route;
- a performer begins using a corner regularly;
- a club informally gathers before acquiring headquarters;
- a former NPC appears during a different activity months later;
- a player notices that an expected regular is absent.

The system should prefer callbacks grounded in existing schedule/history over random exposition NPCs.

## 8. Desire paths and informal circulation

Players and NPCs may repeatedly use routes the formal map does not emphasize.

```yaml
informal_path_observation:
  path_observation_id: null
  public_space_id: null
  geometry_ref: null
  first_observed_at: null
  recurrence_evidence_ids: []
  user_cohort_refs: []
  obstacle_refs: []
  formalization_project_ref: null
  closure_ref: null
```

A repeated shortcut can eventually become:

- a mapped footpath;
- an accessibility problem;
- a conflict with habitat;
- a public-works proposal;
- a maintenance route;
- a new entrance;
- a route that authorities deliberately close.

Do not infer a legal right-of-way.

## 9. Everyday use versus programmed events

An event temporarily reprograms a place.

```yaml
public_space_event_occupation:
  occupation_id: null
  public_space_id: null
  event_id: null
  setup_window_ref: null
  active_window_ref: null
  teardown_window_ref: null
  displaced_routine_ids: []
  temporary_asset_refs: []
  access_changes: []
  cleanup_refs: []
  after_state_refs: []
```

After an event, the world does not simply reset.

Possible after-state:

- litter or cleanup backlog;
- damaged landscaping;
- new public memory;
- new vendor relationships;
- repeated informal meeting point;
- changed wildlife use;
- media coverage;
- infrastructure improvements retained from temporary setup.

Mechanical Contest, battle or sport results remain owned by their respective systems.

## 10. Public-space pressure

Pressure is multi-dimensional.

```yaml
public_space_pressure_revision:
  pressure_revision_id: null
  public_space_id: null
  effective_at: null
  crowding_state: null
  noise_state: null
  waste_state: null
  lighting_state: null
  access_obstruction_state: null
  ecological_pressure_refs: []
  visitor_pressure_refs: []
  maintenance_refs: []
  observation_refs: []
```

These are world-state inputs to other systems. They are not penalties by themselves.

A busy plaza does not reduce Accuracy.

Noise does not inflict a Sonic effect.

Litter does not cause Poisoned.

Bright lighting does not alter LoS unless a verified battle rule and snapshot say so.

## 11. Pokémon use of urban public space

Wild or unowned Pokémon may use public spaces for many reasons.

```yaml
urban_pokemon_use_observation:
  pokemon_use_observation_id: null
  public_space_id: null
  observed_at: null
  pokemon_entity_ids: []
  species_refs: []
  collective_refs: []
  behavior_tags: []
  subarea_ref: null
  human_activity_context: null
  evidence_refs: []
  interpretation_refs: []
```

Behavior tags can include:

- CROSSING
- FORAGING
- RESTING
- SHELTERING
- PERCHING
- DRINKING
- OBSERVING
- FOLLOWING_ROUTE
- TEMPORARY_AGGREGATION
- UNKNOWN

Observed behavior never means “wants to be caught” or “belongs to the plaza.”

## 12. Human–Pokémon coexistence decisions

A public-space issue can be handled by different layers depending on cause.

Examples:

- repeated wild crossing → Conservation / Wild Collectives;
- food waste attracting scavengers → Waste / Food;
- lighting changing nocturnal activity → Light;
- road redesign affecting a crossing → Civic Public Works;
- a Pokémon repeatedly entering a market → observation first, then possible case if actual harm occurs;
- public concern after a media story → Media/Public Memory;
- crowd pressure around a rare sighting → Tourism/Conservation.

The public-space system is the intersection surface, not the authority for every consequence.

## 13. Informal and player-created places

A location can gain meaning before it becomes an institution.

Possible emergent place types:

- meetup corner;
- memorial bench;
- community notice spot;
- informal training patch;
- street-performance corner;
- small garden;
- recurring trading table;
- photo spot;
- club gathering point.

Promotion to a durable named place requires enough Chronicle/use evidence or explicit player/institutional action.

Player-created structures still use Architecture, ownership/permission and server-authoritative persistence.

## 14. Public-space memory

A square can remember events without becoming a museum.

```yaml
public_space_memory_link:
  memory_link_id: null
  public_space_id: null
  event_id: null
  memory_expression_type: null
  physical_marker_ref: null
  recurring_practice_ref: null
  public_record_ref: null
  current_visibility: null
```

Memory expressions may be temporary or durable:

- annual gathering;
- renamed corner;
- plaque;
- recurring photograph angle;
- repaired scar;
- changed tree planting;
- story told by regulars;
- archived event without physical marker.

Public memory remains distinct from world truth.

## 15. Accessibility and participation

Public-space state must link to the existing Accessibility layer.

Examples:

- step-free entrance currently blocked;
- alternate path longer but open;
- temporary event seating obstructing a route;
- captioned public display offline;
- quiet-area availability;
- crowding making an otherwise accessible route impractical;
- visual-only announcement lacking an equivalent channel.

Do not encode disability as a battle Status.

## 16. Coarse crowd cohorts

Minecraft should not simulate every background person.

```yaml
public_space_presence_projection:
  projection_id: null
  public_space_id: null
  source_program_id: null
  source_observation_ids: []
  representative_cohorts: []
  named_actor_ids: []
  representative_npc_budget: null
  ambient_activity_tags: []
  pokemon_projection_refs: []
  generated_at: null
```

Named important NPCs can persist individually.

Background presence should use coarse cohorts and representative entities.

Loaded NPC count is never demographic truth.

## 17. Offline advancement

Routine programs can advance while chunks are unloaded.

Do not simulate every pedestrian step.

Offline advancement may update:

- event windows;
- venue opening state;
- coarse use expectations;
- maintenance state;
- known recurring actor schedules;
- cleanup progress;
- temporary closure expiry;
- public-space pressure from an authored event.

Player-critical encounters should not silently resolve against an absent PC.

## 18. Minecraft projection

Useful representations include:

- representative pedestrians;
- benches and tables;
- market stalls;
- temporary banners;
- event barriers;
- maintenance fencing;
- Pokémon using selected micro-sites;
- street performers;
- public notice boards;
- lighting changes;
- cleanup state;
- path reopening;
- seasonal planting;
- crowd ambience.

Minecraft renders the current public-space revision.

It must not calculate reputation, population truth, access legality, crowd penalties or PTU effects.

## 19. Battle snapshot boundary

Before any battle starts in a shared urban space, the server resolves the noncombat context.

Questions include:

- which civilians have left the bounded combat area;
- which physical objects are present in the chosen static snapshot;
- which paths are blocked as geometry;
- which combatants are actually involved;
- whether the encounter should be moved to a safer area;
- which world-state assets must remain outside the grid.

A public-space snapshot may contain legal walls, blockers and static geometry using VERIFIED targeting/base-movement surfaces.

It may not create unsupported moving crowds, civilian collision, improvised cover bonuses, trampling, dynamic stalls, panic movement or zone reactions.

## 20. Encounter contract A — Station Forecourt Rush

### Narrative premise

A transport interruption causes two commuter flows to converge in a station forecourt just as a wild Pokémon conflict reaches the same area.

### FULL version

Desired behavior:

- civilians move toward safe exits;
- Pokémon can withdraw rather than fight to KO;
- players can hold open a corridor;
- actors may intercept movement toward crowded areas;
- temporary barriers change route choice;
- tactical AI values separation and exit access.

Required permanent categories:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if used;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

### REDUCED version

The overworld resolves commuter diversion first. The station closes one forecourt segment and moves noncombatants out of the tactical boundary. AutoPTU receives a static plaza with fixed blockers and only actual combatants. Any retreat/separation after the battle is handled through authoritative world state rather than improvised tactical AI.

Narrative premise preserved: the incident occurs because transport and wild movement intersected at a crowded node.

## 21. Encounter contract B — Park Edge Wildlife Conflict

### Narrative premise

Repeated evening gatherings in a park edge coincide with wild Pokémon using the same narrow crossing between two habitat patches.

### FULL version

Desired behavior:

- wild actors attempt to cross or withdraw;
- spectators can be cleared from danger;
- players can protect a route without KO as the only objective;
- habitat edge and crowd line may be distinct tactical zones;
- AI understands crossing versus fighting.

Critical dependencies:

- complete movement family — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING;
- move/status/Ability/Feature families remain PARTIAL when invoked.

### REDUCED version

The server clears the park edge and selects one stable subarea. The habitat crossing remains world state. If combat occurs, it uses normal legal battle resolution on a static arena. Afterward, ecology/park schedules update from the authoritative outcome and observation records.

## 22. Encounter contract C — Night Market Chokepoint

### Narrative premise

A temporary night market narrows a pedestrian route. A separate dispute or wild encounter reaches the chokepoint while stalls and visitors are still present.

### FULL version

Desired behavior could include moving noncombatants, destructible/interactable stalls, protected exit lanes and AI that values evacuation or disengagement.

This requires complete movement, zones/reactions, tactical AI and adapter/playback. Any stall-specific PTU effects would additionally require exact Item/Terrain rules.

### REDUCED version

Market staff close one lane, move visitors out and secure goods before battle begins. The tactical snapshot contains fixed blockers only. Damage to market assets is not inferred from attack visuals unless the battle engine later exposes authoritative object interactions.

## 23. Capability summary for Pass 83

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Pass 83 adds no promotion to those permanent categories.

## 24. Public-space-specific implementation blockers

Outside the battle core, these remain unimplemented contracts:

- `PUBLIC_SPACE_IDENTITY_AND_BOUNDARY`;
- `PUBLIC_SPACE_TIME_PROGRAM`;
- `PUBLIC_SPACE_USE_OBSERVATION`;
- `PUBLIC_SPACE_FRONTAGE_GRAPH`;
- `INFORMAL_PATH_HISTORY`;
- `PUBLIC_SPACE_PRESSURE_REVISION`;
- `URBAN_POKEMON_USE_OBSERVATION`;
- `PUBLIC_SPACE_COHORT_PROJECTION`;
- `PUBLIC_SPACE_TO_MINECRAFT_PROJECTION`;
- `PUBLIC_SPACE_TO_BATTLE_SNAPSHOT`.

These belong to server/world-state architecture, not AutoPTU-Java.

## 25. Canon questions still open

Ouros still needs authored decisions about:

- which settlements have plazas, parks, promenades or pedestrian streets;
- whether shared-space access has common regional conventions;
- who operates markets and temporary event permits;
- what public uses are normal at different hours;
- which urban Pokémon relationships predate the players;
- what public-space changes players can propose or build;
- how much crowd presence should be physically represented in Minecraft;
- which PTU/Caelo Skills or Features govern any actual urban stunt or social check;
- whether future battles ever include civilians or instead always clear a tactical perimeter first.

Until those are authored, proposals remain intentionally non-canon.