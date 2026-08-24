# Inland Waterways, Canals, Locks & Navigation Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Pass: 154

## Purpose

This layer models the operational side of inland water transport: navigable rivers, canals, lock complexes, maintained navigation reaches, ferry/barge operation, lockage events, queues, closures, restrictions and resilience.

It does not replace Freshwater/Hydrology, Travel, Maritime, Supply Chains, Road/Rail Transit, Emergency Services or ecological layers.

Its purpose is to answer a narrower question:

Given the current physical water state, infrastructure state and operating constraints, what inland navigation movement is actually possible now, and what happened when a vessel or service attempted it?

## Authority boundary

Keep these states independent:

1. physical water regime;
2. navigation-reach condition;
3. navigation-clearance assessment;
4. lock/dam/control-asset condition;
5. lockage operating state;
6. vessel condition/location;
7. transport-service state;
8. passenger/cargo state;
9. journey result;
10. tactical PTU state.

Examples:

- A river may have normal flow but a navigation reach may be restricted by debris or insufficient clearance.
- A lock may be mechanically available while the ferry serving it is suspended.
- A vessel may be waiting even though the channel is open because another lockage has priority.
- A ferry may complete its trip while a cargo barge remains held upstream.
- A river level change may matter to navigation without creating Water Terrain or forced movement in battle.

## Relationship to existing layers

### Freshwater / Hydrology

Freshwater owns:

- water-body identity;
- flow/level observations;
- floods and seasonal drying;
- reservoirs and water-control consequences;
- catchment connectivity;
- water-quality observations.

This layer reads those records. It does not independently create water levels or flows.

### Travel

Travel owns:

- traveler intent;
- journey planning;
- origin/destination connections;
- route knowledge;
- successful/failed travel legs.

This layer supplies `navigation_operability` and inland transport-service events.

### Maritime

Maritime owns coastal/open-sea lanes, harbors and marine vessel context. A river mouth or river port may hand off between the two layers.

### Supply Chains / Postal / Markets

These layers own cargo identity, consignments, parcels and commercial transactions. Navigation may delay, reroute or strand them, but never creates/deletes them by inference.

### Crisis / Emergency Services

These layers own incident response, evacuation and rescue coordination. Navigation may provide or lose a response route.

### Ecology

Migration, Fisheries, Conservation, Urban Wildlife and other ecology layers own wildlife state. Navigation can react to ecological observations; a navigation closure does not establish population truth.

## Persistent objects

### INLAND_WATERWAY_SYSTEM

A persistent operational network linked to one or more Freshwater systems.

```yaml
inland_waterway_system_id: null
name: null
freshwater_system_refs: []
region_ids: []
navigation_reach_ids: []
lock_complex_ids: []
landing_ids: []
transfer_node_ids: []
service_ids: []
operator_ids: []
public_information_ids: []
history_refs: []
canon_status: PROPOSED
```

This object does not imply a single owner, operator or government.

### NAVIGATION_REACH

A reach used for operational navigation decisions.

```yaml
navigation_reach_id: null
waterway_system_id: null
freshwater_reach_refs: []
upstream_navigation_reach_ids: []
downstream_navigation_reach_ids: []
maintained_channel_ref: null
navigation_state: UNKNOWN
restriction_ids: []
clearance_assessment_ids: []
landing_ids: []
lock_approach_ids: []
alternate_transfer_ids: []
last_verified_at: null
```

Candidate states:

- OPEN
- OPEN_WITH_RESTRICTIONS
- QUEUED
- LOW_CLEARANCE
- BLOCKED
- MAINTENANCE_CLOSED
- ECOLOGY_HOLD
- EMERGENCY_ONLY
- UNKNOWN

These are operational world-state labels, not PTU Terrain.

### NAVIGATION_CLEARANCE_ASSESSMENT

A scoped claim about whether a particular class of vessel can use a particular reach at a particular time.

```yaml
assessment_id: null
navigation_reach_id: null
assessed_at: null
vessel_profile_ref: null
water_state_refs: []
survey_refs: []
bridge_or_overhead_refs: []
channel_geometry_refs: []
debris_refs: []
result: PASSABLE | RESTRICTED | NOT_PASSABLE | UNKNOWN
conditions: []
confidence: null
source_refs: []
```

A PASSABLE result for one shallow-draft ferry does not prove passability for a loaded barge.

### MAINTAINED_NAVIGATION_CHANNEL

A versioned operational representation of a maintained channel.

```yaml
maintained_channel_id: null
navigation_reach_ids: []
revision_id: null
survey_refs: []
nominal_dimension_claims: []
dredging_or_maintenance_event_refs: []
known_constraint_ids: []
valid_from: null
valid_to: null
```

Exact depths/widths are authored or measured. Do not generate arbitrary engineering numbers.

### LOCK_COMPLEX

```yaml
lock_complex_id: null
waterway_system_id: null
location_id: null
upper_navigation_reach_id: null
lower_navigation_reach_id: null
upper_freshwater_ref: null
lower_freshwater_ref: null
chamber_ids: []
gate_asset_ids: []
valve_asset_ids: []
control_asset_ids: []
operator_ids: []
operational_state: UNKNOWN
maintenance_state: UNKNOWN
queue_id: null
public_notice_ids: []
history_refs: []
```

Candidate operational states:

- AVAILABLE
- OPERATING
- LIMITED
- MANUAL_OPERATION
- INSPECTION
- DEWATERED
- MAINTENANCE
- OUT_OF_SERVICE
- EMERGENCY_ONLY
- UNKNOWN

A lock state never writes Freshwater level state by itself.

### LOCKAGE_EVENT

A persistent record for one attempted passage through a lock.

```yaml
lockage_event_id: null
lock_complex_id: null
chamber_id: null
requested_at: null
started_at: null
completed_at: null
direction: UPBOUND | DOWNBOUND
vessel_ids: []
service_journey_refs: []
entry_reach_id: null
exit_reach_id: null
water_state_refs: []
operating_step_events: []
priority_or_queue_ref: null
outcome: COMPLETED | DELAYED | ABORTED | CANCELLED | DIVERTED | UNKNOWN
reason_refs: []
operator_record_refs: []
```

Routine successful lockages may be aggregated after retention rules allow it. Significant ones remain individually accessible.

### LOCKAGE_QUEUE

```yaml
queue_id: null
lock_complex_id: null
observed_at: null
waiting_vessel_ids: []
known_priority_claims: []
estimated_wait_band: null
public_estimate_ref: null
```

A public estimate may become stale without rewriting the actual queue history.

### INLAND_NAVIGATION_ASSET

```yaml
navigation_asset_id: null
asset_type: FERRY | BARGE | TOW | WORKBOAT | RESEARCH_CRAFT | RESCUE_CRAFT | PASSENGER_BOAT | OTHER
owner_or_custody_refs: []
operator_ids: []
home_landing_id: null
current_location_ref: null
service_role: null
operational_state: UNKNOWN
capacity_claim_refs: []
maintenance_refs: []
journey_refs: []
```

No capacity, speed or vehicle combat statistic is generated without canon/rules evidence.

### INLAND_WATER_SERVICE

A Travel-compatible transport service tied to the navigation network.

```yaml
service_id: null
service_type: FERRY | CARGO | MIXED | RESEARCH | MAINTENANCE | RESCUE | CHARTER
operator_ids: []
landing_ids: []
navigation_reach_ids: []
lock_complex_ids: []
asset_ids: []
service_state: UNKNOWN
schedule_ref: null
current_disruption_ids: []
passenger_policy_refs: []
cargo_policy_refs: []
```

Travel remains authoritative for passenger journeys.

### NAVIGATION_RESTRICTION

```yaml
restriction_id: null
scope_refs: []
restriction_type: LOW_WATER | HIGH_WATER | DEBRIS | MAINTENANCE | STRUCTURAL | WILDLIFE | VISIBILITY | CONGESTION | EMERGENCY | OTHER
starts_at: null
ends_at: null
source_refs: []
operational_effect: null
review_at: null
status: PROPOSED | ACTIVE | LIFTED | EXPIRED | UNKNOWN
```

`WILDLIFE` means an operational response to an ecological situation. It never labels the Pokémon as hostile.

### WATER_USE_NAVIGATION_DECISION

A record for choices where navigation interacts with other uses of managed water.

```yaml
navigation_decision_id: null
water_control_asset_refs: []
navigation_need_refs: []
other_water_use_refs: []
forecast_refs: []
observation_refs: []
decision_actor_ids: []
decision_summary: null
effective_window: null
follow_up_refs: []
```

This is a provenance object, not a morality score.

## Lockage state machine

A conceptual lockage may pass through:

REQUESTED
→ QUEUED
→ CALLED
→ APPROACH_AUTHORIZED
→ CHAMBER_ENTRY
→ CHAMBER_SECURED
→ LEVEL_TRANSITION
→ EXIT_AUTHORIZED
→ EXITED
→ COMPLETED

Alternative outcomes can branch to:

- DELAYED;
- ABORTED;
- CANCELLED;
- DIVERTED;
- EMERGENCY_HOLD.

Do not require the player to watch every ordinary step. The state machine exists for causality and exceptional cases.

## Routine compression

Normal inland transport should usually compress to a journey result.

Expand operational detail when at least one of these is true:

- a route choice matters;
- a closure creates a meaningful alternative;
- cargo/passengers have time sensitivity;
- wildlife/ecology requires a decision;
- a lock/asset failure creates consequences;
- a crisis changes priority;
- a water-use trade-off is being decided;
- a repeated location has accumulated history relevant to the player.

Do not create lock maintenance quests simply because a lock exists.

## Navigation and ecology

Wildlife may create or respond to navigation state.

Examples:

- a migration wave crosses an approach reach;
- a large individual blocks a narrow passage;
- a nesting site changes towpath access;
- fish movement affects a temporary operation window;
- a floating habitat mass moves into a canal reach.

Required separation:

wildlife observation
→ ecological assessment
→ optional navigation restriction
→ service consequence.

Never:

wild Pokémon visible
→ navigation enemy
→ capture/KO required.

## Navigation and infrastructure history

A lock or canal may accumulate generations of equipment and operating practice.

Versionable changes:

- manual to powered gates;
- local to remote controls;
- added sensors;
- duplicate chamber added/removed;
- old landing decommissioned;
- towpath repurposed;
- canal widened or partly abandoned;
- service changes from cargo-heavy to recreational/passenger-heavy.

The location remains persistent across these revisions.

## Alternate-route resilience

A closure can activate alternatives without deleting the water connection.

Possible handoffs:

- another lock route;
- road haulage;
- rail transfer;
- ferry at another landing;
- portage around a short obstruction;
- temporary passenger shuttle;
- emergency-only craft.

The corresponding layer remains authoritative for the alternate mode.

## Public information and actor knowledge

Public navigation information may include:

- current restriction;
- expected reopening band;
- queue estimate;
- service cancellation;
- landing change;
- alternate connection;
- maintenance window.

Publication is not world truth. A notice can lag actual conditions.

Actor knowledge should retain source and freshness.

## Minecraft/Cobblemon projection

Minecraft may render:

- canal geometry;
- lock chamber and gates;
- visible water-level revision;
- control house;
- ferry/barge models;
- waiting vessels;
- towpaths;
- signage;
- temporary barriers;
- maintenance equipment.

Minecraft must not determine:

- authoritative water level;
- lock operational state;
- queue priority;
- vessel capacity;
- service availability;
- collision consequences;
- currents;
- drowning;
- forced movement;
- cargo ownership;
- navigation clearance.

A piston moving a gate does not create a completed lockage record. A boat entity disappearing does not mean a vessel sank or left the network.

## Battle boundary

Inland navigation is overworld/world-state first.

The narrative layer must not invent:

- vessel initiative;
- collision damage;
- moving-platform movement rules;
- current knockback;
- drowning;
- wave damage;
- deck slipping;
- cargo cover;
- lock-gate crushing;
- automatic Water Terrain;
- navigation-related Accuracy penalties.

When conflict occurs, prefer a stable handoff to AutoPTU.

### Static handoff principle

Before battle when possible:

1. stop or secure the vessel;
2. halt lock movement;
3. evacuate noncombatants;
4. resolve water-control state in world state;
5. freeze a legal static arena;
6. pass only actual combatants and validated environment state to AutoPTU;
7. resume navigation afterward according to world-state consequences.

## Cross-layer event examples

### Low-water restriction

Freshwater observation
→ navigation clearance becomes RESTRICTED
→ cargo service delays a journey
→ Supply Chains marks consignment delayed
→ Market receives reduced availability later.

No battle is required.

### Wildlife passage hold

Migration episode
→ approach reach temporarily held
→ lockage queue grows
→ passenger ferry misses a connection
→ Travel offers alternate route
→ Public Information publishes update.

No Pokémon becomes an enemy.

### Lock outage during emergency

Technology/Infrastructure fault
→ lock OUT_OF_SERVICE
→ Emergency Services selects another crossing
→ Postal/Supply Chain shipments reroute
→ later repair project begins
→ reopening produces a historical lock revision.

## Mechanical non-inferences

Do not infer:

- Swim from living near a canal;
- carrying capacity from being large;
- vessel towing from Strength;
- current resistance from Water type;
- navigation expertise from Fisherman/Sailor flavor;
- lock operation from Electric-type presence;
- water purification from Water-type presence;
- forced movement from visible current;
- Rough Terrain from towpath condition;
- bridge/lock fall damage from architecture;
- battle Water Terrain from being inside a lock;
- priority in a queue from player status;
- ownership from operating or repairing a vessel.

## Canon boundary

Human review must establish before canon promotion:

- which inland waterways exist;
- whether canals/locks exist technologically in Ouros;
- who operates them;
- which settlements depend on them;
- which ferry/cargo services are active at campaign start;
- whether any Pokémon participate institutionally and under what agency rules;
- what information about traffic/service is public;
- how much infrastructure change may happen offline;
- whether players can own/operate vessels or services.

## Implementation outcome

A successful inland navigation layer makes water transport feel like infrastructure with memory rather than fast travel or scenery.

The same canal can carry commuters, cargo, researchers, responders and migrating wildlife across years of Chronicle. Its locks can be modernized, closed, reopened, bypassed or repurposed while the hydrology, transport service and tactical engine retain their own authorities.
