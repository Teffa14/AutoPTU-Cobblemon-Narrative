# Global NPC resource operational-readiness bridge — Pass 340

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-07

## Purpose

Connect Pass 338 resource availability and Pass 339 reservation/checkout state to the existing Maintenance and Shared Equipment owners without creating a second technical-maintenance system.

The global planner needs one narrow answer before it treats a physical resource as usable: has an authoritative owner currently cleared this resource for the authored kind of ordinary world work?

## Authority boundary

Facility Maintenance continues to own observations, faults, assessment, work orders, repair and verification.

Shared Equipment continues to own temporary entitlement, lending, checkout/return and its `readiness_record_ref` seam.

Pass 340 owns only a read-only adapter from an owner-supplied readiness conclusion into the generic `WorldResource` view consumed by Pass 338.

The adapter cannot inspect, calibrate, repair, diagnose, clear or retire equipment by itself.

## Core boundaries

`RESOURCE_EXISTS != RESOURCE_OPERATIONALLY_READY`

`RESOURCE_RESERVED != RESOURCE_OPERATIONALLY_READY`

`RESOURCE_HELD != RESOURCE_OPERATIONALLY_READY`

`RESOURCE_RETURNED != RESOURCE_OPERATIONALLY_READY`

`REPAIR_COMPLETED != VERIFICATION_PASSED`

`PRIOR_READINESS != CURRENT_READINESS`

`READINESS_SOURCE_RECORD != PLANNER_PROJECTION`

`WORLD_RESOURCE_READY != PTU_ITEM_EFFECT_LEGAL`

## Executable record

```yaml
OperationalReadinessRecord:
  record_id: readiness:stable-id
  resource_id: resource:stable-id
  status: READY_FOR_AUTHORED_USE
  source_record_ref: maintenance:verification:stable-id
  effective_from_tick: 0
  valid_until_tick: null
```

The record is a bridge fact, not a maintenance work order. `source_record_ref` must point back to the system that has authority to make the technical conclusion.

V1 statuses:

- `READY_FOR_AUTHORED_USE`
- `LIMITED`
- `INSPECTION_PENDING`
- `MAINTENANCE`
- `OUT_OF_SERVICE`
- `UNKNOWN`

`LIMITED` is blocking in V1. The global planner does not infer that a limitation is acceptable merely because the resource can perform some functions.

## Semantic time

A record applies only when `effective_from_tick <= now_tick` and, when supplied, `now_tick < valid_until_tick`.

When more than one applicable record exists, the latest effective record wins; stable record ID breaks a same-tick tie deterministically.

An expired READY record remains historical evidence. It does not silently extend itself.

## Projection

`project_readiness_onto_resources(...)` creates a planner-only copy of the resources.

A currently blocking readiness result projects to Pass 338's generic `UNAVAILABLE` state. This is intentionally lossy only inside the planner view; the returned `ReadinessProjectionResult` separately preserves the exact readiness status, source reference and blocking reason.

The source resource objects and readiness records remain unchanged.

A resource already `DEPLETED` or `RETIRED` remains so rather than being rewritten as a readiness failure.

## Explicit-readiness policy

Some ordinary resources need no technical record. The caller can therefore leave `require_explicit_readiness=False` and preserve resources for which no owner supplied a record.

For instrument- or safety-sensitive work, the caller can set `require_explicit_readiness=True`. Missing or expired evidence then projects to `RESOURCE_READINESS_UNKNOWN` and blocks the resource until an owner supplies a current conclusion.

Which capability requires explicit readiness must come from authored domain policy. Pass 340 does not decide that globally.

## Integration order

The intended chain is:

`authoritative resource records + reservation projection + authoritative readiness records + semantic time`

then

`Pass 340 readiness projection -> Pass 338 resource requirement assessment -> existing deterministic planner -> optional AutoPTU handoff`

A resource may therefore be physically local, reserved for the correct NPC and still fail before structured mechanics because its technical readiness is unresolved.

## Reason codes

V1 exposes narrow diagnostic reasons:

- `RESOURCE_READINESS_LIMITED`
- `RESOURCE_INSPECTION_PENDING`
- `RESOURCE_IN_MAINTENANCE`
- `RESOURCE_OUT_OF_SERVICE`
- `RESOURCE_READINESS_UNKNOWN`

These are planning explanations. They do not establish negligence, cause, legal responsibility or technical diagnosis.

## Reduced implementation

The reduced version is executable now. It requires stable IDs, semantic time, externally supplied readiness facts and the existing Pass 338 resource gate.

No battle simulation is required.

A blocked NPC can choose another already-ready intent through the existing planner. Future acquisition/request/replan layers may generate a richer response, but Pass 340 itself does not invent one.

## Rich implementation

Later integration can consume domain-specific readiness owners for instruments, vehicles, facility-linked equipment or shared kits. It can also add capability-scoped LIMITED semantics, inspection requests, maintenance-request intents and communication of newly changed readiness.

Those additions must continue to reference owner records rather than moving technical judgment into the agenda system.

## AutoPTU capability boundary

The readiness bridge itself has no combat-mechanics dependency.

If a rich story carries an instrument or other resource into structured play, the fixed audit applies exactly:

- targeting / footprints / range / LoS: VERIFIED for ordinary audited contracts; a targeted device requires its own implementation;
- base movement legality: VERIFIED for ordinary audited movement;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL for carrying, rescue, interception or displacement;
- core calculations: VERIFIED for ordinary audited arithmetic;
- action economy / initiative: VERIFIED for ordinary primitives; new use/pass/equip actions remain individually gated;
- full turn / round lifecycle: PARTIAL for timed or phase-sensitive equipment behavior;
- full stateful damage pipeline: PARTIAL for equipment damage or damage-affecting effects;
- status lifecycle: PARTIAL for persistent tactical conditions;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL and individually gated;
- Trainer Features / perks: PARTIAL and individually gated;
- AI legal-action infrastructure: VERIFIED for ordinary audited infrastructure, not invented equipment actions;
- AI tactical policy: BLOCKING for protect/transfer/withdraw/non-defeat resource objectives;
- Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

Minecraft inventory state, animations or a rendered green indicator cannot author technical readiness.

## Acceptance cases

1. An available local instrument with a current READY record remains available to Pass 338.
2. INSPECTION_PENDING blocks an otherwise available resource.
3. MAINTENANCE and OUT_OF_SERVICE block it.
4. LIMITED blocks conservatively in V1.
5. When explicit readiness is required, a missing or expired record blocks as UNKNOWN.
6. When explicit readiness is not required, ordinary resources without records preserve their existing state.
7. The latest currently applicable readiness record wins deterministically.
8. Projection preserves `source_record_ref` and never mutates the owner record or original resource.
9. A readiness-blocked structured intent cannot request AutoPTU.
10. A second ready resource can satisfy the existing Pass 338 requirement without changing the intent schema.

## Deferred work

The next useful slices remain resource-acquisition/request intents, institutional pools and authority, quantity reservations, waitlists/fairness, transfer/travel, consumable decrement, checkpoint persistence and capability-scoped LIMITED policy.

Maintenance-request generation should be integrated only after the agenda can reference an existing Maintenance owner without fabricating technical work.