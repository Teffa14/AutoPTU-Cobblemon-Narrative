# Ouros disturbance, succession and recovery contract

Status: PROPOSED DESIGN CONTRACT
Date: 2026-09-03
Pass: 237

## Purpose

Represent ecological disturbance as persistent world-state with branching recovery trajectories. The contract prevents the simulator from treating habitat change as a temporary spawn-table modifier that automatically resets after elapsed time, chunk unload or server restart.

## Authority invariants

1. Ouros owns disturbance, habitat, recovery and community-state truth.
2. Minecraft/Cobblemon projects authored environmental evidence and visible actors but cannot author recovery, death, emigration, recolonization or battle outcomes from entity/block state alone.
3. AutoPTU receives authority only after an explicit structured encounter handoff.
4. A habitat transition does not directly create PTU damage, Status Afflictions, stat stages, Move effects, Abilities or Trainer Feature effects.
5. Habitat recovery and population/demographic recovery are separate. Pass 238 owns population arithmetic.
6. Generic spawning cannot manufacture recolonization truth.
7. A species-specific restoration capability requires explicit species provenance plus Ouros regional/content authorization.

## Disturbance event model

Each event has identity, time and typed impacts.

```text
disturbance_event_id
site_id
source_type
start_tick
end_tick_or_null
severity:
  structure_loss
  resource_loss
  substrate_damage
  water_or_air_quality_loss
  route_obstruction
  shelter_loss
  mortality_pressure
  displacement_pressure
  contamination_pressure
repeat_event_group_or_null
source_persists_after_impact
```

`mortality_pressure` is ecological pressure only. It does not itself remove population members. An actual demographic transition must be authored by the appropriate population resolver or a semantic result returned from a real encounter.

## Ecological legacy snapshot

Immediately after a material disturbance, persist what survived.

```text
surviving_structure_legacy
surviving_resource_legacy
surviving_population_legacy
surviving_refuge_coverage
route_connectivity
substrate_integrity
water_or_air_quality
```

These legacies affect subsequent succession. They must survive server restart and chunk unload.

## Recovery stages

Recommended site stage enumeration:

```text
STABLE
IMPACT
ACUTE_AFTERSHOCK
EARLY_SUCCESSION
RECOVERING
TRANSIENT_REORGANIZATION
RECOVERED
PERSISTENT_REORGANIZATION
```

Transitions are evidence-driven. Time can be a prerequisite but never the sole proof that a transition occurred.

### STABLE

The current ecology reference condition is internally consistent. `STABLE` does not mean pristine or identical to historical baseline.

### IMPACT

A disturbance is currently applying its primary effects.

### ACUTE_AFTERSHOCK

The direct event has ended but immediate instability, displacement, poor access or resource loss still dominates.

### EARLY_SUCCESSION

Newly exposed resources, substrates or refuges begin to matter. Some pre-event resources can remain reduced while temporary opportunities increase.

### RECOVERING

Key functions are trending toward a compatible reference condition. Population abundance does not refill automatically.

### TRANSIENT_REORGANIZATION

Community/resource use differs materially from the prior state but available evidence still supports a plausible later return or further transition.

### RECOVERED

The site has regained the required ecological functions for its selected recovery target. This need not reproduce every pre-event value.

### PERSISTENT_REORGANIZATION

The site has crossed an authored threshold into a durable alternative configuration. Returning to the old configuration requires a new intervention/event rather than passive time.

## Recovery target

Every active recovery process must name what it is trying to recover.

```text
recovery_target_id
target_functions
target_resource_ranges
target_connectivity_ranges
target_quality_ranges
required_observation_window
```

Do not use a single hidden `habitat_health == 1.0` target.

## Succession pressure model

At each bounded ecology evaluation:

```text
current stage
+ surviving legacies
+ resource creation/loss
+ substrate/quality state
+ connectivity
+ current weather/season context
+ existing species/population pressures
+ human disturbance state
+ repeated disturbance load
= candidate transition pressures
```

Outputs can include:

```text
HOLD_STAGE
ADVANCE_RECOVERY
ENTER_EARLY_SUCCESSION
ENTER_TRANSIENT_REORGANIZATION
ENTER_PERSISTENT_REORGANIZATION
RETURN_TO_ACUTE
DECLARE_RECOVERED
```

The resolver must provide reasons/evidence for a transition so testing and observation can distinguish cause from elapsed time.

## Temporary resource pulses

A disturbance can create resources while destroying others. Candidate resources include exposed substrate, fallen structure, temporary pools, new cavities, edge habitat, open sightlines or short-lived forage access.

A temporary pulse record should include:

```text
resource_pulse_id
resource_type
availability
created_by_event_id
start_tick
expected_decay_model
beneficiary_filters
harm_or_risk_context
```

Beneficiary filters propose availability. They do not authorize a species for the region.

## Repeat disturbance and resilience debt

A second event during incomplete recovery must read the current site state rather than the original pre-event snapshot.

Repeated disturbance can:

- reduce surviving legacies;
- reset or redirect succession;
- increase reorganization pressure;
- produce a different resource pulse;
- create longer route or shelter disruption.

`REPEAT_EVENT != FIRST_EVENT_REPLAYED`

## Relationship to Pass 236

Human-disturbance memory remains population/individual behavioral state. Pass 237 consumes those pressures when relevant but owns habitat/community trajectory.

Example:

```text
repeated human pursuit
-> Pass 236 harmful exposure / avoidance memory
-> if physical habitat/resource damage occurs, author a Pass 237 disturbance event
-> Pass 237 changes site succession/recovery state
```

Behavioral avoidance alone does not create a habitat succession event.

## Relationship to Pass 238

Pass 237 can change carrying conditions, connectivity, occupancy pressure and recolonization opportunity. It does not independently increase/decrease canonical member counts.

Pass 238 should later consume these outputs as demographic context.

## Minecraft/Cobblemon projection

Safe outputs:

- authored debris or changed vegetation presentation;
- route restrictions and warning surfaces;
- visibility eligibility changes for persistent populations;
- hiding/avoidance/activity presentation inherited from ecology;
- temporary resource-point presentation;
- environmental evidence such as damaged cover, disturbed ground or recovery markers.

Unsafe authority leaks:

- restoring blocks means ecological recovery is complete;
- a generic entity spawning means recolonization occurred;
- despawn means emigration/death;
- vanilla damage supplies canonical ecological mortality;
- chunk generation supplies a new pre-disturbance baseline.

## Observation and quests

Players and NPCs can observe evidence such as route reopening, resource use, visible return latency, damaged/recovering cover, persistent contamination or use of a temporary refuge.

Observed evidence can support hypotheses including:

```text
RECOVERY_PROGRESSING
RECOVERY_STALLED
SOURCE_STILL_ACTIVE
TEMPORARY_BENEFICIARY_PRESENT
REPEAT_DISTURBANCE_RISK
POSSIBLE_REORGANIZATION
```

Hidden simulator fields remain uncertain until evidence supports them.

## Structured encounter handoff

### Reduced version

Available without rich environmental combat mechanics. Ouros selects explicit combatants only after escalation. AutoPTU receives a conventional bounded battle with verified movement/targeting/core arithmetic/action-economy seams and individually validated Moves/Abilities. Habitat recovery remains frozen or abstracted during the battle and receives a semantic result afterward.

### Intended rich version

A restoration/containment encounter may involve collapsing terrain, spreading contamination, escape corridors, defended refuges, timed stabilization goals, reaction zones or forced relocation.

Permanent dependency audit:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

Rich mechanics must remain disabled or reduced until the exact required family is verified by current tests/contracts.

## Implementation acceptance

A deterministic fixture must prove at minimum:

1. impact can alter habitat/resource state without changing canonical population count by itself;
2. chunk unload/reload preserves the recovery stage and legacies;
3. early succession can create a temporary resource pulse while another resource remains degraded;
4. elapsed time alone cannot declare `RECOVERED`;
5. a repeat disturbance reads the current recovering state and can increase reorganization pressure;
6. generic Cobblemon spawn/despawn never changes recovery or demographic truth;
7. battle handoff is explicit;
8. a persistent alternative state is representable without silently overwriting the old reference record.

## Canon status

PROPOSED. This contract does not canonize a disturbance at Sendero del Vidrio, does not alter its approved Fletchling population, and does not authorize Shaymin or any other new species for Marea.