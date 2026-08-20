# Demography, Migration & Population Change Layer

Status: proposed systems design. Not established Ouros canon.

Date: 2026-08-20

## Purpose

Ouros already tracks individual residences, workplaces, visits, travel, tourism, crises, institutions and settlement growth. This layer adds the population context around those systems without simulating every unnamed resident.

It should answer:

- who normally lives here;
- who is present temporarily;
- who arrives daily for work or study;
- what population change has been observed;
- why the change is happening;
- which services are under pressure;
- which named actors are part of the change;
- what remains uncertain.

The layer must preserve individual agency and privacy while allowing settlements to feel populated and to change over years of world time.

## Core separation

Keep these concepts distinct:

```text
actor identity
  -> current physical presence
  -> residence association
  -> household membership
  -> regional association
  -> workplace/school/assignment
  -> migration event
  -> population cohort membership
  -> aggregate population estimate
  -> published demographic claim
```

A person can work in a town without living there.
A visitor can stay for months without becoming a resident.
An evacuee can be temporarily displaced without deciding to relocate permanently.
A resident can leave for a long expedition while still considering the settlement home.
An aggregate population estimate does not create or delete named NPCs.

## 1. Population profile

```yaml
population_profile:
  population_profile_id: null
  settlement_or_zone_id: null
  reference_time: null
  estimate_status: observed|estimated|published|revised|unknown
  usual_resident_estimate: null
  temporary_present_estimate: null
  commuter_inflow_estimate: null
  commuter_outflow_estimate: null
  seasonal_population_estimate: null
  displaced_population_estimate: null
  confidence: unresolved
  source_refs: []
  methodology_ref: null
  notes: []
```

This is an aggregate world-state object.

It does not replace individual NPC records.

## 2. Named actors and cohorts

Important NPCs remain individual entities.

Background population can use cohorts.

```yaml
population_cohort:
  cohort_id: null
  settlement_or_zone_id: null
  cohort_kind: residents|commuters|students|seasonal_workers|visitors|evacuees|expedition_staff|temporary_contractors|other_authored
  estimated_count: null
  active_window: null
  origin_context_refs: []
  destination_context_refs: []
  primary_driver_refs: []
  service_demand_tags: []
  housing_demand_tags: []
  mobility_pattern_refs: []
  confidence: unresolved
  provenance_refs: []
```

A cohort is not a faction.

Members do not automatically share beliefs, goals, culture or loyalty.

## 3. Residence state versus physical presence

Residence belongs to the housing layer.

This layer references residence and adds presence patterns.

```yaml
actor_presence_pattern:
  actor_id: null
  home_residence_ref: null
  usual_settlement_ref: null
  daytime_location_refs: []
  overnight_location_refs: []
  recurring_travel_refs: []
  temporary_absence_ref: null
  current_presence_state: present|away|traveling|unknown
  source_refs: []
```

Do not infer emotional attachment from presence frequency.

## 4. Migration event

```yaml
migration_event:
  migration_event_id: null
  actor_ids: []
  cohort_id: null
  origin_location_ref: null
  destination_location_ref: null
  movement_kind: relocation|temporary_assignment|seasonal_move|education_move|work_move|return_move|crisis_displacement|resettlement|unknown
  stated_reason_refs: []
  inferred_driver_refs: []
  departure_time: null
  arrival_time: null
  intended_duration: null
  actual_duration: null
  residence_change_ref: null
  status: planned|in_progress|completed|reversed|unknown
  provenance_refs: []
```

Stated reason and inferred driver are separate.

A person can say they moved for work while researchers later observe that housing cost or route access also mattered. The system should preserve both without deciding private motives.

## 5. Migration drivers

Large population changes should have explicit drivers.

Suggested driver categories:

- new employment;
- institution opening;
- institution closure;
- research discovery;
- archaeological boom;
- transport opening;
- transport closure;
- housing availability;
- housing damage;
- crisis displacement;
- recovery/reconstruction;
- seasonal work;
- education;
- tournament/festival;
- tourism boom;
- conservation access change;
- resource boom;
- public safety change;
- family/household move when explicitly authored;
- retirement;
- personal preference when explicitly authored;
- unknown.

Do not generate one hidden scalar called `attractiveness` and use it as universal causation.

## 6. Temporary presence

Temporary population must remain separate from resident population.

Examples:

- tournament competitors;
- spectators;
- seasonal workers;
- tourists;
- visiting researchers;
- emergency responders;
- evacuees;
- exchange students;
- performers;
- contractors;
- expedition crews.

Temporary presence can still affect:

- accommodation capacity;
- transport demand;
- clinic demand;
- food demand;
- waste generation;
- public-space pressure;
- staffing;
- rumors and media;
- wildlife disturbance;
- route congestion.

The effect must be causal and linked to existing system state.

## 7. Commuters

A settlement can have more people present during the day than live there.

```yaml
commuter_flow:
  commuter_flow_id: null
  origin_ref: null
  destination_ref: null
  purpose: work|education|service|market|other
  usual_window: null
  estimated_volume: null
  transport_connection_refs: []
  disruption_refs: []
  confidence: unresolved
```

This is particularly useful for Minecraft because the server can change ambient population by time/window without changing housing records.

## 8. Settlement growth

Population growth should not directly spawn buildings.

Instead:

```text
population pressure
  -> housing/service demand
  -> civic/private proposals
  -> funding/resources/staffing
  -> construction/adaptive reuse
  -> new capacity
```

The architecture layer remains authoritative for physical structures.

Population pressure can generate a proposal. It cannot instantly build a district.

## 9. Settlement decline

Population decline can also be persistent.

Possible outcomes:

- vacant housing;
- reduced service hours;
- school consolidation;
- unused infrastructure;
- adaptive reuse;
- lower transit frequency;
- changed market days;
- ecological recolonization;
- preservation efforts;
- deliberate revitalization projects.

Do not automatically represent decline as moral failure or decay.

A smaller settlement can remain healthy and intentional.

## 10. Displacement and return

Crisis displacement must not silently become permanent migration.

```yaml
displacement_record:
  displacement_id: null
  actor_ids: []
  cohort_id: null
  source_crisis_ref: null
  origin_residence_refs: []
  temporary_destination_refs: []
  start_time: null
  safe_return_assessment_refs: []
  return_status: unknown|possible|started|completed|not_returning|mixed
  permanent_move_records: []
```

`not_returning` requires actual state, not an assumption that time away equals relocation.

## 11. Population estimates and censuses

Ouros may have census-like institutions only if canon establishes them.

Before that, use generic `population_observation` and `published_population_claim`.

```yaml
population_observation:
  observation_id: null
  location_ref: null
  observer_or_institution_ref: null
  method: registry|survey|housing_count|service_usage|transport_count|manual_estimate|other
  time: null
  measured_value: null
  uncertainty_notes: []
  source_refs: []
```

A population count can be wrong because of:

- commuters;
- tourists;
- people away temporarily;
- duplicate records;
- missing records;
- seasonal movement;
- damaged archives;
- outdated housing data.

Do not resolve every discrepancy as fraud.

## 12. Public demographic claims

Media, civic institutions and residents can publish different population claims.

These belong to the information/public-memory layers.

Examples:

- “the town doubled in size”;
- “everyone is leaving”;
- “the festival brought ten thousand visitors”;
- “this district is mostly newcomers.”

Such claims may be approximate, rhetorical or based on outdated data.

They must not overwrite aggregate state automatically.

## 13. Cultural continuity and migration

Origin and culture are not the same field.

Do not infer:

- language;
- religion;
- cuisine;
- ideology;
- accent;
- clothing;
- family structure;
- political position;
- Pokémon preferences

from region of origin alone.

Cultural practices belong to authored or observed cultural state.

Migration can create new cultural institutions or districts only through explicit worldbuilding.

## 14. Pokémon and human population separation

Human/NPC demography and wild Pokémon ecology remain separate models.

Possible causal links:

- more residents increase waste or food availability;
- development reduces habitat;
- conservation creates refuge;
- transport alters disturbance;
- abandoned structures create habitat;
- seasonal workers alter trail use.

Do not combine resident counts with wild spawn counts into one universal population value.

## 15. Named Pokémon living around settlements

Persistent Pokémon entities can have residence/presence patterns too, but ownership and wild status remain separate.

Examples:

- an institutional partner that commutes with staff;
- a released former partner that seasonally visits an orchard;
- a wild Pokémon that uses a neighborhood park;
- a Pokémon that lives at a workshop without being owned by it.

The Pokémon agency layer remains authoritative for partnership/custody semantics.

## 16. Minecraft projection

Minecraft should project demographic state selectively.

Possible projection tools:

- representative NPCs;
- variable crowd density;
- occupied/vacant building states;
- market stalls opening/closing;
- commuter flows near transit;
- temporary event tents;
- lodging occupancy indicators;
- construction pressure;
- changed service queues;
- dialogue and notice-board updates.

Do not spawn one entity per background resident.

The server should preserve population state even when chunks are unloaded.

## 17. Privacy

Exact residence, household and movement records can be sensitive in multiplayer.

Suggested visibility layers:

- public aggregate;
- institution-only;
- party-shared;
- player-private;
- authored GM/system-private.

A public population dashboard does not reveal private addresses.

## 18. Demographic event writeback

After an arc, record only demonstrated changes.

Example:

```yaml
demographic_writeback:
  source_event_id: null
  location_id: null
  resident_delta_estimate: null
  temporary_presence_delta_estimate: null
  cohort_changes: []
  named_actor_moves: []
  housing_pressure_changes: []
  service_pressure_changes: []
  evidence_refs: []
  confidence: unresolved
```

A successful festival may increase temporary presence without adding permanent residents.

A rebuilt route may increase commuters before any household relocates.

## 19. Quest generation hooks

Demographic state can generate grounded hooks when it creates a real mismatch.

Examples:

- housing exists but a water network cannot support the new district;
- a clinic is sized for old resident numbers;
- a ferry carries many commuters after another route closes;
- a research boom creates temporary lodging shortages;
- evacuees return but a school has not reopened;
- a shrinking district has unused buildings that could support adaptive reuse;
- a seasonal workforce arrives before transport capacity expands;
- a settlement count is wrong because one cohort was double-counted.

The hook comes from state mismatch, not from demographic identity itself.

## 20. Battle boundary

Population state does not create battle mechanics.

Never infer:

- crowd cover;
- morale bonuses;
- mob attacks;
- stampede damage;
- panic status;
- escort rules;
- civilian initiative;
- population-scaled enemy levels;
- automatic faction reinforcements.

If a demographic scenario becomes combat, use an encounter contract with explicit engine dependencies.

## 21. Full / reduced encounter contracts

### Station Rush — FULL

Premise:
A transport outage causes two commuter flows to converge at one station while a separate Pokémon disturbance blocks one route.

Full version needs:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including interception/forced movement if moving civilians or Pokémon share the grid;
- action economy/initiative;
- lifecycle;
- terrain/zones/reactions if station lanes dynamically open/close;
- tactical AI that understands `CLEAR_ROUTE`, `REACH_EXIT` or equivalent;
- Minecraft/Cobblemon/Craftics playback.

Reduced version:

Resolve commuters and station-flow changes in overworld state first. Evacuate noncombatants from the tactical projection. Freeze one legal arena and run a conventional encounter only with actual combatants. After battle, update route/service/population-flow state.

### Temporary Camp Perimeter — FULL

Premise:
A temporary population camp created after a crisis overlaps with a wildlife corridor.

Full version needs:

- moving noncombatants or protected zones;
- autonomous wildlife withdrawal behavior;
- complete movement;
- terrain/zones/reactions;
- tactical AI;
- playback.

Reduced version:

Camp residents remain outside the battle grid. World state determines which corridor is open. If conflict occurs, AutoPTU receives only a static legal map and combatants. No invented panic, crowd or escort mechanics.

### Boomtown Survey — FULL

Premise:
A fast-growing settlement is surveying a future road while wild Pokémon repeatedly cross the work area.

Full version needs:

- objective-aware movement;
- moving wildlife groups;
- route-control goals;
- possible forced movement/interception;
- terrain/hazard support if construction terrain matters;
- tactical AI;
- Minecraft playback.

Reduced version:

Survey progress and wildlife crossings resolve as overworld observations. If a battle occurs, freeze construction state and use basic legal combat. No construction hazard or movement objective is simulated unless verified.

## 22. Integration with existing layers

Housing owns residences and households.

Workplaces owns jobs, staffing and shifts.

Interregional Mobility owns visits and host-region context.

Travel owns connections and transport services.

Tourism owns visitor pressure and attractions.

Crisis owns hazard lifecycle and emergency displacement triggers.

Architecture owns physical settlement growth and reuse.

Civic Governance owns public decisions and projects.

Media owns published demographic claims.

This layer owns aggregate population context, cohorts, migration events, presence patterns and demographic writeback.

## 23. PTU / Caelo guardrails

Do not invent:

- Skill DCs for migration or crowd management;
- Trainer Feature effects;
- social modifiers based on origin;
- crowd combat rules;
- mass-battle rules;
- settlement bonuses;
- legal residence/citizenship rules;
- Pokémon obedience rules;
- experience/reward scaling from population state.

The primary PTU/Caelo corpus must be consulted before any such mechanic is authored.

## 24. Promotion checklist

Before demographic material becomes canon:

1. Confirm the settlement and region already exist in canon or are approved additions.
2. Confirm population change has a causal driver.
3. Separate named actors from background cohorts.
4. Verify privacy boundaries.
5. Confirm housing/service/transport capacity changes in linked systems.
6. Avoid inferred culture or motivation.
7. Preserve provenance for estimates and published claims.
8. Validate any battle mechanics separately against PTU/Caelo and engine evidence.
9. Define Minecraft projection without requiring one entity per resident.
10. Keep all uncertain counts explicitly estimated.