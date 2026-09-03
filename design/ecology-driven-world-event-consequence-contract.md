# Ecology-driven world event and consequence contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Pass: 241
Canon effect: NONE unless a runtime event references approved canon inputs

## Purpose

Define how persistent ecological state creates world events, how those events become observable, how players and institutions can intervene, and how consequences return to ecology without quest flags or Minecraft presentation authoring hidden truth.

## Authority flow

```text
persistent ecology state
-> event condition evaluation
-> event instance
-> ecological pressure changes
-> observable symptoms
-> Pass 240 observation / claims / NPC knowledge
-> player or institutional intervention
-> world-state mutation through declared seams
-> ecology re-evaluation
-> optional AutoPTU handoff for structured conflict
-> semantic result
-> persistent consequence
```

Never permit:

```text
quest accepted -> ecology fixed
Minecraft actor count -> event population truth
combat KO -> ecological death
player entered area -> event exists
NPC dialogue branch -> hidden cause becomes true
```

## Event definition

Required fields:

```text
event_definition_id
event_family
scope
trigger_conditions
clear_conditions
minimum_active_duration
cooldown_or_hysteresis
observable_symptom_rules
allowed_interventions
consequence_rules
autoptu_dependency_profile
projection_profile
```

Definitions are reusable rules. They are not active instances.

## Event instance

Required fields:

```text
event_instance_id
definition_ref
opened_at
current_phase
scope_refs
driver_refs
pressure_snapshot
intervention_log
semantic_result_refs
last_evaluated_at
resolved_at nullable
resolution_state
```

Recommended phases:

`FORMING`
`ACTIVE`
`ESCALATING`
`STABILIZING`
`RESOLVED`
`TRANSFORMED`

`TRANSFORMED` means the original event ended but left a persistent ecological arrangement different from the pre-event baseline.

## Trigger rule

An event must be opened from persistent state evidence, not random encounter generation.

Example trigger expression:

```text
resource_window_remaining <= configured_threshold
AND local_activity_pressure >= configured_threshold
AND human_overlap_pressure >= configured_threshold
```

A seeded stochastic process may be used only when the ecological model explicitly defines a probabilistic event. Its seed and inputs must be replayable.

## Hysteresis

Opening and clearing conditions should normally differ.

Example:

```text
OPEN when disturbance_pressure >= 0.70
CLEAR only after disturbance_pressure <= 0.40 for N evaluations
```

This avoids event flicker when a variable oscillates around one threshold.

Exact numeric thresholds are data and remain unresolved unless explicitly approved.

## Event families

Initial taxonomy candidates:

`RESOURCE_WINDOW_SHIFT`
`MIGRATION_TIMING_MISMATCH`
`DISTURBANCE_THRESHOLD`
`NESTING_CONFLICT`
`PREDATOR_PRESSURE_SPIKE`
`ROUTE_BOTTLENECK`
`LOCAL_RECOLONIZATION`
`HABITAT_RECOVERY_WINDOW`
`ECOLOGICAL_INFORMATION_CASCADE`
`HUMAN_WILDLIFE_CONFLICT`

These names create no canon events.

## Observable symptoms

Events expose symptoms through Pass 240, never hidden fields directly.

Possible symptoms:

- unusual visible concentration;
- unusual silence or low detection;
- changed route use;
- feeding or guarding behavior;
- tracks at unexpected places/times;
- damaged or depleted resource patches;
- repeated alarm behavior;
- changed nesting attendance;
- human traffic conflicts;
- institutional measurements.

An observer can detect symptoms without knowing the correct cause.

## Intervention model

An intervention is a world-service action with declared inputs and effects.

Required fields:

```text
intervention_id
actor_ref
event_instance_ref
action_type
started_at
ended_at nullable
world_mutations
requires_authority
source_or_permission_ref nullable
```

Candidate action types:

`OBSERVE_ONLY`
`REDUCE_TRAFFIC`
`TEMPORARY_ROUTE_CLOSURE`
`RELOCATE_EQUIPMENT`
`RESTORE_RESOURCE`
`PROTECT_RESOURCE`
`CREATE_BUFFER`
`ESCORT_OR_GUIDE`
`COMMUNICATE_WARNING`
`STRUCTURED_DEFENSE`

Interventions mutate explicit pressures or infrastructure state. They do not select a scripted ending.

## Consequence rules

Consequences must be derived from post-intervention state.

Examples:

- lower human disturbance may reduce avoidance pressure;
- protected resource availability may extend a forage window;
- a route closure can displace human traffic elsewhere;
- failed intervention can increase disturbance;
- delayed intervention can allow an event to transform into a different local state;
- a tactical semantic result can change condition, displacement or access pressure if a declared world rule consumes it.

No consequence may silently change population abundance. Population change must use the Pass 238 demographic ledger.

## Player consequences

Consequences should be represented as persistent world changes where possible:

- route availability or delay;
- changed NPC schedules;
- research opportunities;
- institutional trust/credibility when such systems exist;
- changed access to an area;
- altered resource condition;
- changed observation probability;
- new follow-up evidence;
- later quest/event availability derived from state.

Rewards can exist but must not replace the ecological consequence.

## Pass 240 integration

Event truth and event knowledge are distinct.

An NPC can have:

```text
world event = ACTIVE
knowledge state = UNKNOWN
```

or:

```text
world event = RESOLVED
claim = STALE / still believed active
```

Event UIs and dialogue should query a holder's evidence/claim view unless the surface is explicitly administrative/debug authority.

## Pass 238/239 integration

Visible Pokémon during an event remain leases over real population members or unresolved pool slots.

An event may alter projection weights and activity windows but must not create extra population members.

`VISIBLE_CONCENTRATION != POPULATION_GROWTH`

`EVENT_DESPAWN != EMIGRATION_OR_DEATH`

## Marea Pass 241 reduced event

Definition candidate:

`ouros.event.sendero.forage_window_compression.v1`

Inputs reference only existing canon:

- `ouros.marea.wild.sendero_lower_shelf.fletchling.v1`
- Sendero del Vidrio lower shelf `(2056,77,2120)`
- seasonal crossing `(2072,79,2154)`
- Marea Field Office / Estación Mirador residents as knowledge/intervention holders where already canonized.

Premise:

A forage-resource window becomes shorter than expected. Existing Fletchling concentrate activity into a narrower window. Human route overlap raises disturbance pressure. The event can be detected through sightings, activity timing, resource evidence and traffic reports.

Reduced interventions:

- observation only;
- temporary traffic reduction;
- temporary route management;
- equipment relocation;
- warning/communication.

No new species, population size, resource species or fixed numeric thresholds are canonized.

## Full encounter version

A rich version may include active escort, defense, pursuit, territorial displacement or a tactical objective while the event remains active.

Dependency classification:

- targeting/footprints/range/LoS: REQUIRED if actors target, pursue or defend areas in structured play;
- base movement legality: REQUIRED for structured movement;
- complete movement including push/pull/knockback/interception/forced movement: REQUIRED only if the authored encounter uses those behaviors; currently PARTIAL;
- core calculations: REQUIRED for structured checks/damage as applicable; VERIFIED within audited contracts;
- action economy/initiative: REQUIRED for structured combat; VERIFIED within audited contracts;
- full turn/round lifecycle: REQUIRED for timed objectives/phases; currently PARTIAL;
- full stateful damage pipeline: REQUIRED if damaging combat is allowed; currently PARTIAL;
- status lifecycle: REQUIRED if statuses are used; currently PARTIAL;
- terrain/weather/hazards/zones/reactions: REQUIRED only for authored weather, hazard, zone or reaction mechanics; currently MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: validate every Move used; family PARTIAL;
- abilities: validate every Ability used; family PARTIAL;
- items: validate every Item used; family PARTIAL;
- Trainer Features/perks: validate every Feature used; family PARTIAL;
- AI legal-action infrastructure: REQUIRED for AI combatants; VERIFIED within audited contracts;
- AI tactical policy: REQUIRED for objective-aware wildlife such as flee/guard/escort prioritization; currently BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback: REQUIRED for end-to-end visible event projection and battle playback; currently PARTIAL/BLOCKING.

## Reduced version readiness

The reduced event can run without AutoPTU. It needs:

- persistent ecology state;
- event evaluation;
- Pass 240 observation/knowledge;
- world-service interventions;
- projection changes that do not author population truth.

The first runtime implementation can therefore validate the event contract before rich tactical dependencies are complete.

## Regression invariants

1. Event instances are caused by ecological state or declared seeded rules.
2. Acceptance of a quest cannot open or resolve ecological truth by itself.
3. Visible concentration cannot change population abundance.
4. Player/NPC knowledge can lag event truth.
5. Interventions mutate explicit pressures/resources/access state.
6. Consequences are re-evaluated from state after intervention.
7. Population changes require demographic ledger events.
8. Minecraft entity lifecycle never creates ecological resolution.
9. AutoPTU contributes only semantic tactical results after explicit handoff.
10. Event resolution retains historical cause, intervention and consequence records.

## Status

PROPOSED. This contract adds no new canon geography, species, population count, PTU rule adoption or fixed event threshold.