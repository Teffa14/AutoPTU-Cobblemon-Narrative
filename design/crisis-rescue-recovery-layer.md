# Crisis, Rescue & Recovery Layer

Status: proposed systems architecture. Not established Ouros canon.

## Purpose

This layer gives Ouros a durable way to represent emergencies that alter normal world operation. It is designed for storms, fires, collapses, eruptions, floods, blackouts, hazardous leaks, route failures, missing-person incidents and similar crises.

The core rule is simple: a crisis is not a quest. It is a changing world-state object that can generate many quests, encounters, social scenes, logistical problems and later recovery projects.

## Relationship to existing Ouros layers

This system should connect to, not duplicate:
- `world-agency-layer.md` for faction and institutional actions;
- `observation-settlement-time-layer.md` for clocks, settlement capabilities and time progression;
- `travel-transport-expedition-layer.md` for route and service disruption;
- `wild-collective-agency-layer.md` for ecological displacement and group response;
- `case-authority-custody-layer.md` when a crisis has a suspicious or investigated cause;
- `public-memory-event-legacy-layer.md` for later remembrance and institutional narrative;
- `material-culture-economy-crafting-layer.md` for supply, repair and workshop consequences;
- `mission-dungeon-grammar.md` for operational task composition.

## Core data model

```yaml
crisis:
  crisis_id: null
  status: SIGNAL
  crisis_type: null
  origin_state: []
  affected_regions: []
  affected_locations: []
  hazard_fronts: []
  forecasts: []
  verified_reports: []
  rumors: []
  clocks: []
  active_impacts: []
  secondary_impacts: []
  response_actors: []
  shelters: []
  staging_sites: []
  blocked_routes: []
  disrupted_services: []
  missing_actor_cases: []
  displaced_collectives: []
  resource_needs: []
  completed_actions: []
  unresolved_needs: []
  recovery_projects: []
  chronicle_refs: []
  public_memory_refs: []
  mechanics_review_required: true
```

## Lifecycle

A crisis can move through these phases. Not every event must use every phase.

### SIGNAL

Evidence exists that something may happen or may already be developing.

Examples:
- tremors increase;
- unusual migration is observed;
- a storm forecast changes;
- a dam inspection finds damage;
- smoke is seen beyond a ridge;
- communications fail in one district.

The event is not yet fully understood.

### PREPARE

Actors can reduce exposure or improve later options.

Possible player actions:
- warn residents;
- move supplies;
- verify routes;
- relocate vulnerable Pokémon;
- stage transport;
- prepare shelters;
- inspect infrastructure;
- coordinate institutions;
- cancel or reroute events.

Preparation should never guarantee safety automatically. It changes state only in ways that the simulation and authored scenario support.

### IMPACT

The hazard causes direct state changes.

Examples:
- route becomes blocked;
- bridge becomes unavailable;
- power fails;
- structure becomes unsafe;
- settlement sub-area becomes inaccessible;
- wild collective disperses;
- transport service stops;
- NPCs become stranded;
- a workshop loses critical equipment.

### RESPONSE

Immediate operational problems dominate.

Common objectives:
- locate missing actors;
- escort or extract;
- deliver critical supplies;
- clear access;
- restore communication;
- establish shelter;
- survey new hazards;
- contain a local problem;
- stabilize a service.

### STABILIZE

The main danger may still exist, but the region is no longer deteriorating rapidly.

Possible state:
- evacuation largely complete;
- critical roads reopened;
- temporary clinic established;
- wildfire front contained;
- communications partially restored;
- dangerous area perimeter known.

### RECOVERY

The emergency becomes a rebuilding and adaptation problem.

Examples:
- repair infrastructure;
- rehome residents;
- reopen businesses;
- restore habitat;
- recover lost records;
- rebuild transport capacity;
- assess contamination;
- support damaged institutions.

### AFTERMATH

The immediate recovery is mostly complete, but the event remains in world history.

Possible durable effects:
- changed settlement layout;
- memorial;
- revised emergency plan;
- different route alignment;
- new local profession or institution;
- permanent habitat change;
- changed public trust;
- new myth or rumor;
- unresolved cause investigation.

## Hazard truth versus information

Crisis generation must separate reality from what people think is happening.

```yaml
hazard_truth:
  actual_location: []
  actual_severity: null
  actual_direction: null
  actual_secondary_risks: []

forecast:
  source_id: null
  issued_at: null
  predicted_location: []
  predicted_severity: null
  confidence: null

report:
  source_id: null
  observed_at: null
  location: null
  claim: null
  verification_state: UNVERIFIED

rumor:
  source_id: null
  content_summary: null
  spread_scope: []
  reliability: UNKNOWN
```

The generator must never convert a rumor or forecast directly into canonical hazard truth.

## Crisis clocks

A crisis can have several clocks instead of one universal timer.

Examples:
- storm_arrival
- fire_spread
- structural_failure_risk
- shelter_capacity
- fuel_reserve
- medical_supply
- route_clearance
- communications_repair
- evacuation_completion

Clocks should advance because of explicit world-time rules, events or actions. They must not advance invisibly only to force drama.

## Cascading effects

One impact may create another.

Example chain:

```text
landslide
→ road closed
→ supply vehicle delayed
→ clinic shortage
→ transport demand rises
→ alternate route becomes crowded
→ wild habitat disturbed
→ new encounter behavior
```

Cascades should be traceable through the world graph.

Suggested edge:

```yaml
caused_by:
  source_state_id: null
  target_state_id: null
  causal_confidence: CONFIRMED
```

Do not create chains solely because they are dramatic. Each step requires an authored rule or supported simulation relationship.

## Operational job generation

A crisis should emit jobs from unresolved needs.

```yaml
crisis_job_candidate:
  source_crisis_id: null
  source_need_id: null
  activity_types: []
  location_ids: []
  beneficiary_ids: []
  response_actor_ids: []
  objective_verbs: []
  urgency: null
  known_constraints: []
  unknowns: []
  completion_conditions: []
  failure_forward_states: []
  mechanics_review_required: true
```

Good task verbs:
- SEARCH
- LOCATE
- ESCORT
- EVACUATE
- EXTRACT
- DELIVER
- CLEAR
- SURVEY
- SIGNAL
- RECONNECT
- SHELTER
- RESTORE
- REOPEN
- STABILIZE
- CONTAIN
- REUNITE

## Search and rescue state

Missing actors should remain world objects rather than becoming generic quest counters.

```yaml
search_subject:
  actor_id: null
  last_verified_location: null
  last_verified_time: null
  intended_route: []
  known_dependencies: []
  known_pokemon_companions: []
  communication_state: UNKNOWN
  mobility_state: UNKNOWN
  health_state: UNKNOWN
  located: false
  extraction_required: UNKNOWN
```

The system should not invent injury, death, panic or survival status before evidence or scenario rules establish it.

## Shelters and safe zones

A shelter is a temporary service node.

```yaml
shelter:
  shelter_id: null
  location_id: null
  operator_ids: []
  status: OPEN
  intended_population: []
  capacity_state: NORMAL
  resource_needs: []
  access_routes: []
  pokemon_accommodation: []
  communications_state: null
```

Avoid reducing shelters to numerical capacity optimization unless a specific scenario calls for it. Narrative use can focus on access, supply, communication, reunification and roleplay.

## Staging sites

Response organizations may establish temporary bases closer to an incident.

Possible functions:
- information intake;
- supply distribution;
- temporary healing/support;
- route coordination;
- missing-person registry;
- Pokémon holding/relocation coordination;
- volunteer assignment;
- transport dispatch.

A staging site can later disappear, become permanent, or evolve into a new local institution if world history supports it.

## Response actors and mandates

Different groups may act for different reasons.

Possible response actors:
- local residents;
- Gym staff;
- Rangers or analogous Ouros institutions if established;
- researchers;
- transport operators;
- medical teams;
- clubs;
- factions;
- independent Trainers;
- municipal workers;
- volunteer groups.

The system must not invent legal authority merely because a group is helping.

For each actor:

```yaml
response_actor:
  actor_id: null
  mandate: []
  available_resources: []
  known_information: []
  operational_area: []
  current_assignment: null
  coordination_links: []
```

## Multiplayer crisis design

A good multiplayer emergency should support parallel contribution.

Example distribution:
- one player surveys a blocked route;
- another escorts residents;
- another investigates displaced Pokémon;
- another restores a communication node;
- another negotiates access to private equipment.

These tasks should write to the same crisis object.

Players do not need to be in one party at all times for their actions to affect the shared state.

## Preparedness and mitigation

Preparedness should be playable before visible disaster.

Potential systems:
- inspections;
- drills;
- emergency caches;
- alternate route mapping;
- habitat relocation plans;
- warning networks;
- shelter maintenance;
- transport contingencies;
- mutual-aid agreements.

Preparedness should create explicit state that later scenarios can read.

Example:

```yaml
preparedness_asset:
  asset_id: null
  location_id: null
  purpose: null
  readiness: null
  last_checked_at: null
  owner_or_operator_id: null
```

## Warning credibility

Warnings may have a social history.

Potential state:
- trusted source;
- disputed source;
- outdated alert system;
- frequent false alarms;
- recent successful warning;
- local knowledge versus centralized forecast.

This should influence dialogue and voluntary NPC behavior only through explicitly authored rules. Do not silently manipulate NPC compliance with opaque hidden formulas.

## Ecological crisis response

The wild-collective layer should receive crisis signals independently.

Possible outputs:
- temporary aggregation;
- dispersal;
- migration;
- changed home range;
- nesting abandonment;
- unusual urban presence;
- resource competition;
- avoidance of damaged route;
- return during recovery.

No emotional interpretation is required.

Example:

```yaml
collective_crisis_response:
  collective_id: null
  crisis_id: null
  observed_behavior_changes: []
  inferred_causes: []
  confidence: null
```

## Infrastructure state

Infrastructure should be modeled by function, not only by blocks.

Examples:
- bridge
- power substation
- water pump
- clinic
- harbor
- tunnel
- rail segment
- communication tower
- shelter
- warehouse

```yaml
infrastructure_asset:
  asset_id: null
  location_id: null
  functions: []
  status: OPERATIONAL
  dependencies: []
  dependents: []
  repair_requirements: []
  temporary_workarounds: []
```

Minecraft visuals can reflect this state, but the underlying functional state should remain authoritative.

## Crisis dungeon conversion

An existing location can temporarily behave like a dungeon.

Examples:
- cave after collapse;
- city district during blackout;
- flooded underground facility;
- damaged ship;
- forest during fire response;
- mountain route after avalanche.

The map may remain physically familiar while these change:
- accessible exits;
- safe zones;
- visibility;
- NPC distribution;
- hazard zones;
- encounter behavior;
- objectives;
- communications.

This allows emergency content without creating one-use locations.

## Tactical battle boundary

A crisis can motivate or alter a battle, but this layer does not define combat mechanics.

Potential narrative battle objectives:
- protect evacuees;
- hold a path open;
- stop a panicked Pokémon from entering danger;
- disable a hazardous machine;
- escape before an area becomes inaccessible;
- survive while another actor completes a rescue task.

Before implementation, AutoPTU must explicitly support the selected objective and all relevant hazard mechanics.

This layer does not invent:
- hazard damage;
- status conditions;
- forced movement;
- terrain penalties;
- round timers;
- carrying rules;
- rescue actions;
- escape rules;
- weather effects;
- new Pokémon capabilities.

## PTU/Caelo interaction

Caelo already demonstrates environmental areas with direct mechanical effects and distinguishes Jobs, Encounters, Raids and Social play. PTU exposes terrain and movement capabilities that may be relevant.

Any crisis action involving those systems must query authoritative state.

Examples requiring validation:
- whether a Pokémon can cross deep water;
- whether a Pokémon can carry a Trainer;
- whether Groundshaper can alter the relevant terrain;
- whether a movement action is legal in the current grid;
- whether weather has an existing battle effect;
- whether a Skill Check is appropriate and what DC applies.

## Recovery projects

Recovery should be represented as persistent projects.

```yaml
recovery_project:
  project_id: null
  source_crisis_id: null
  target_asset_or_location_id: null
  objective: null
  required_world_states: []
  responsible_actor_ids: []
  contributions: []
  status: PROPOSED
  completion_effects: []
  long_term_tradeoffs: []
```

Potential project categories:
- repair;
- replacement;
- relocation;
- habitat restoration;
- redesign;
- memorialization;
- investigation;
- policy or institutional change;
- route rerouting;
- service rebuilding.

## Recovery tradeoffs

Returning to the pre-crisis state should not always be the only option.

Examples:
- rebuild bridge in the same location;
- reroute road to avoid habitat;
- abandon damaged facility;
- convert temporary clinic into permanent service;
- restrict rebuilding in a hazardous area;
- preserve ruins as a memorial or research site.

These choices can connect recovery to factions, economy, ecology and public memory.

## Chronicle writeback

Meaningful crisis actions should record:
- what was done;
- where;
- when;
- by whom;
- who witnessed it;
- what state changed;
- what remained unresolved.

Do not summarize contribution as a single hero score.

## Public memory

Later public memory may distinguish:
- official account;
- resident recollections;
- institutional records;
- disputed responsibility;
- memorial traditions;
- later historical interpretation.

The crisis truth itself remains separate from later narrative about it.

## Generator rules

The generator may create a crisis candidate only when it can explain the source state.

Valid sources include:
- authored event schedule;
- weather/world system state;
- infrastructure condition;
- faction action;
- ecological state;
- dungeon state;
- travel incident;
- established regional clock;
- explicit human-authored story arc.

It must not roll arbitrary disasters merely because the world has been quiet.

For every generated crisis candidate, record:
- source cause;
- affected systems;
- uncertainty;
- likely first-order impacts;
- possible secondary impacts;
- player-facing signals;
- what can be prepared;
- what mechanics need validation.

## Anti-frustration rules

1. Do not destroy important player property without authored rules and clear risk context.
2. Do not invalidate completed progress solely to create drama.
3. Do not use invisible timers that players could not reasonably detect.
4. Do not make every crisis lethal.
5. Do not force all players into the same emergency content.
6. Do not punish players for failing to respond to events they never received information about.
7. Let some preparation succeed visibly.
8. Preserve recovery opportunities after partial failure.
9. Avoid endless repeated disasters in the same region without causal justification.
10. Keep crisis frequency low enough that normal life in Ouros remains meaningful.

## Minecraft/Cobblemon expression

Possible overworld manifestations:
- closed roads;
- barriers;
- smoke, rain or other visual states where technically feasible;
- damaged building variants;
- temporary camps;
- emergency notice boards;
- redirected NPC spawns;
- transport cancellation signage;
- relocated wild Pokémon;
- repair crews;
- supply depots;
- changed shop/service availability;
- reopened infrastructure after recovery.

Any destructive block transformation should be controlled and reversible where appropriate. Canonical infrastructure state should not depend only on arbitrary chunk damage.

## Minimum viable implementation

A first implementation does not need full disaster simulation.

MVP:
1. CRISIS object with lifecycle phase.
2. Manual/admin-authored impact events.
3. Route/service state changes.
4. Missing-person and shelter objects.
5. Operational jobs generated from unresolved needs.
6. Recovery projects.
7. Chronicle writeback.
8. Clear PTU mechanics review flag.

Later versions can add hazard propagation, preparedness simulation and cross-region cascading effects.

## Open implementation questions

- Which environmental hazards are already modeled in AutoPTU?
- Can battle objectives query external crisis state?
- Can AutoPTU return outcomes such as protected, escaped, evacuated or route-cleared instead of only victory/defeat?
- How should world clocks progress when no players are online?
- Which Minecraft blocks/entities represent infrastructure function versus decoration?
- How will Cobblemon spawns react to temporary displacement state?
- Can NPC pathfinding use temporary safe/unsafe areas reliably?
- Which PTU/Caelo rules govern carrying, drowning, suffocation, falling, harsh weather and rescue-relevant Skill Checks?
- How much crisis state should be visible to players versus only inferred from reports?
- How are multiplayer contributions merged when players act simultaneously in different locations?
