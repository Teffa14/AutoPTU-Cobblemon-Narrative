# Ecological resource-pulse world-event contract

Status: PROPOSED contract. Pass 265. This document does not promote a Marea/Sendero resource pulse to canon.

## Purpose

Represent short-lived changes in resource availability that can alter ecological activity and projection without silently mutating authoritative abundance, source identity or PTU battle state.

## Record

`RESOURCE_PULSE_EVENT_V1`

Required fields:

- `event_id`: stable Ouros event identity.
- `authority_class`: authority that may assert the resource-availability fact.
- `resource_class`: ecological resource category; may remain coarse when exact identification is uncertain.
- `scope`: one or more ecological site/window references.
- `phase`: `ONSET`, `PEAK`, `DECLINE`, `CLOSED` or `UNCERTAIN`.
- `clock_epoch` and semantic start checkpoint.
- `horizon_policy_ref`: Pass 261-compatible closure policy.
- `projection_effect`: bounded change to presentation/activity eligibility.
- `provenance_root`: source-backed or simulation-backed provenance.
- `canon_status`: canon/proposed/fixture-only as applicable.

Optional fields can describe a spatial wave, observation confidence, suspected cause and species-specific response-policy references. Optional fields may not strengthen authority beyond their provenance.

## Authority separation

A resource-availability event may directly write resource availability and event lifecycle state.

It may influence projection/activity eligibility through an explicit ecology policy.

It may generate public observations such as elevated feeding activity, repeated arrivals or temporary concentration when those observations are actually supported.

It may not directly write births, deaths, immigration, emigration, total population, new source identities, ownership, HP, Injury, status, stats, Moves, Abilities, Items, Trainer Features or tactical decisions.

A demographic effect requires a separate demographic transaction with its own authority and provenance. The invariant is:

`resource pulse != demographic event`

## Projection rule

Projection can select only sources already counted by the authoritative population/source ledger, unless another independently valid source-admission operation has occurred.

A pulse can change `where`, `when` or `how likely` an already-counted source is eligible for presentation. It cannot increase the counted population merely to produce a busier scene.

Public language must distinguish observable concentration/activity from abundance. “More Fletchling were visible at this site during the event” can be supported by observations. “The Fletchling population increased” requires separate demographic evidence.

## Species and individual response

No universal attraction multiplier exists. A future response policy can consider species ecology, individual disturbance history, access, current state, social context and competing stimuli.

A pulse record describes opportunity. It does not prove that every eligible individual detected, preferred or followed the resource.

## Spatial resource waves

A pulse may change scope across sites through explicit event transitions, for example `SITE_A -> SITE_B`.

That transition changes resource availability. It does not assert actor movement, teleportation, migration, pursuit, forced movement or target selection.

If the full encounter physically depicts actors moving to track a wave, their movement must be resolved through the appropriate movement/AI authority. The adapter cannot infer movement history from the fact that a later projection occurs near the new resource scope.

## Lifecycle

Pass 261 semantic-horizon rules govern event closure. Restart, chunk unload, despawn, day/night edits and non-detection are not expiry triggers.

Every phase/closure transition requires a transaction identity and provenance so replay remains idempotent.

A rollback of the ecological clock follows the Pass 261 quarantine/reconciliation rule and cannot create an early decline or closure.

## Battle boundary

Reduced ecological version: event state changes projection/activity only. No AutoPTU handoff is required.

Full contest version: actors physically approach, compete, defend access or react to each other. This requires exact capability evidence for each mechanic used. Targeting/LoS is required for spatial targeting; base movement for ordinary approach; complete movement for interception/push/pull/knockback/forced movement; action economy and lifecycle for tactical sequencing; terrain/weather/zones/reactions if the resource area has mechanical effects; move-specific behavior, Abilities, Items or Trainer Features when invoked; AI legal-action infrastructure for autonomous legal choices; AI tactical policy for deciding whether/how to approach or contest; adapter/playback for world presentation.

Damage/status aftermath additionally requires the full stateful damage pipeline and/or status lifecycle for the exact producing path.

## Fail-closed rules

If the system knows only that a visual cluster exists, it may record an observation but cannot create `RESOURCE_PULSE_EVENT_V1` without an admissible resource-authority source.

If the resource event is valid but species-response policy is unresolved, preserve the event and use conservative/no response instead of inventing attraction behavior.

If physical convergence would require unverified AI tactical policy, keep the narrative premise through reduced projection windows rather than implementing tactical decisions in Minecraft/Cobblemon.
