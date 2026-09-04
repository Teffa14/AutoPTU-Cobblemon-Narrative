# Provisional ecology retention policy contract

Status: PROPOSED DESIGN CONTRACT. Does not change established species canon or PTU rules.

## Purpose

Pass 259 defines bounded provisional state on an already-counted anonymous source. This contract decides what that state may do across time, observation gaps and restart.

The retention decision is semantic. It is not based on file lifetime, chunk lifetime, renderer presence, number of sightings or an arbitrary global timeout.

## Core invariants

A retention decision cannot change population abundance.

`population total before == population total after`

A retention decision cannot create a persistent actor. Persistent identity is created only by the Pass 258 counted-source resolution transaction after admissible lineage proof exists.

A retention decision cannot author PTU mechanical truth. Minecraft damage, animation, despawn, velocity, movement pattern or generic Cobblemon state cannot create HP loss, injury, status, Move, Ability, item, ownership, capture state or combatant state.

Public observation history and private ecological state are separate records. Expiring private linkage must not erase a valid historical observation. Retaining private state must not upgrade player knowledge.

## Retention classes

### PRESENTATION_CORRELATION

Examples: projection admission token, save/load receipt, short-lived render correlation.

Default outcome: `DROP_PRIVATE_KEEP_REQUIRED_RECONCILIATION_GUARD` after the owning projection/reconciliation lifecycle closes.

This class may survive a server restart only when an existing projection/save-load contract explicitly requires it to prevent duplicate or uncorrelated presentation.

It never creates durable identity pressure by itself.

### OBSERVATION_PROVENANCE

Examples: provenance root, observation timestamp, public uncertainty state, observer/report lineage.

Default outcome: preserve the historical observation record independently from provisional source linkage.

The observation may remain after `EXPIRED_TO_AGGREGATE`. Its existence does not keep an anonymous source pinned as an individual.

### RECENT_SITE_USE

Examples: one recent perch/use episode or location association.

Default outcome: `RETAIN_UNTIL_SEMANTIC_HORIZON`, then `DROP_PRIVATE_KEEP_PUBLIC_HISTORY` unless another admissible continuity basis exists.

Same-site recurrence, time-of-day recurrence or compatible ordinary behaviour cannot extend retention indefinitely by themselves and cannot serve as lineage proof.

### INDIVIDUAL_DISTURBANCE_RESPONSE

Examples: the Pass 256 individual-specific response trajectory and a still-active recovery/decay horizon.

Default outcome: `RETAIN_UNTIL_SEMANTIC_HORIZON` across restart while the consequence can still change this source's future projection/behaviour contribution.

If the consequence remains active after the bounded provisional window and aggregation would risk applying it to another individual, classification becomes `DURABLE_CANDIDATE`. If admissible internal continuity is also present, Pass 259 may classify `PROMOTION_REQUIRED` and delegate to Pass 258.

A response state does not imply tame, friendly, hostile, obedient or battle AI policy.

### ACTIVE_DIEGETIC_MARKER_LINK

Examples: an approved active field marker under the Pass 254 marker contract.

Default outcome: `PROMOTE_OR_QUARANTINE` when the marker carries continuing individual consequence.

If the marker is fixture-only, uncertain, damaged, lost or lacks admissible internal lineage, it cannot force promotion. Public confirmation rules remain governed by the marker/recognition contracts.

### AUTHORITATIVE_ONE_TIME_TRANSITION

Examples: a future explicitly adjudicated semantic event whose occurrence should not be forgotten merely because observations stop. Candidate examples include dispersal, a lasting injury or another one-time state transition.

Default outcome: preserve the event record. If an ongoing consequence must remain attached to one biological individual, use `PROMOTE_OR_QUARANTINE`.

The event is admissible only when it came from the subsystem that owns that truth. PTU mechanical consequences require an authoritative AutoPTU/Ouros semantic result or an explicitly adopted equivalent. A Minecraft presentation event is not sufficient.

### INFERRED_BEHAVIOR_LABEL

Examples: "foraging", "guarding", "migrating" or another state inferred only from movement/site-use patterns.

Default outcome: `DROP_OR_RETAIN_AS_UNCERTAIN_EVIDENCE`.

It cannot become authoritative latent state without a separately valid basis. This protects against over-interpreting movement or repeated location data.

## Retention outcomes

### DROP_PRIVATE_KEEP_PUBLIC_HISTORY

Close the private correlation. Keep legitimate historical observation/provenance records. Preserve source contribution to the population. Do not create a demographic event.

### RETAIN_UNTIL_SEMANTIC_HORIZON

Store an explicit horizon descriptor and authoritative clock basis. Examples can be recovery window end, active marker validity end or projection-reconciliation completion.

A horizon is semantic metadata. It must not be a universal "seen recently" timeout.

At horizon evaluation the layer must choose a declared next outcome. Silence or non-detection cannot be interpreted as death, emigration, recovery or identity loss.

### PROMOTE_OR_QUARANTINE

If aggregation would misattribute a continuing individual consequence, request Pass 259 promotion evaluation.

If admissible lineage proof exists, Pass 259 can become `PROMOTION_REQUIRED` and Pass 258 performs the zero-demography representation swap.

If lineage proof does not exist, quarantine the individual-specific consequence from aggregate application. Do not smear it across the population and do not invent a persistent actor.

### REJECT_UNAUTHORIZED_STATE

Reject the proposed retained state when its authority source is invalid. Preserve any legitimate observation as observation only.

This is mandatory for inferred PTU mechanical consequences from Minecraft/Cobblemon presentation.

## Retention record

A provisional retained-state record must contain at minimum:

`state_class`

`source_ref`

`authority_source`

`provenance_root`

`opened_at_world_time`

`retention_outcome`

`semantic_horizon` when applicable

`last_evaluated_world_time`

`transaction_id`

`public_identity_effect = NONE` unless another explicit epistemic contract authorizes a change

It may hold compact references to existing state. It must not clone a PTU combatant or full actor record.

## Restart rules

Restart does not imply expiry.

A retained state survives restart only when all of the following are true:

1. its retention outcome permits restart survival;
2. its source is still an active already-counted source or has been atomically resolved through Pass 258;
3. its authority/provenance record remains valid;
4. its semantic horizon has not been authoritatively completed or invalidated;
5. no contradictory transaction has retired the state.

World time used for horizons must be monotonic or otherwise restart-safe. Wall-clock assumptions remain implementation-specific until the production persistence layer defines them.

## Expiry rules

Expiry is an explicit transaction. It cannot be inferred from renderer absence, chunk unload, failed detection or generic despawn.

Expiry preserves population total, source count contribution, demographic history and public observation history.

The same expired state cannot be resurrected by reusing an old transaction ID or by observing a superficially similar Pokémon later.

## Interaction with Pass 258 and Pass 259

Pass 260 decides retention pressure only.

Pass 259 owns provisional classification and determines whether durable identity pressure plus admissible continuity reaches `PROMOTION_REQUIRED`.

Pass 258 alone performs the representation swap:

`anonymous sources -1`

`persistent sources +1`

`population total +0`

## Marea/Sendero fixture policy

The Pass 260 fixture uses the existing twelve-Fletchling population with fixture-only counted anonymous sources.

One source carries `RECENT_SITE_USE` and expires safely while observation history remains.

One source carries `INDIVIDUAL_DISTURBANCE_RESPONSE` with an active fixture-only recovery horizon and survives restart without changing abundance or public identity.

One source receives a Minecraft-only damage presentation event. Attempting to retain `PERSISTENT_INJURY` from that event must return `REJECT_UNAUTHORIZED_STATE` because no AutoPTU/Ouros-authoritative injury result exists.

No fixture source becomes a canon actor.

## Engine capability boundary

The reduced retention lifecycle needs no tactical AutoPTU category. Production observation/projection still depends on Minecraft/Cobblemon/Craftics adapter/playback support.

If an authoritative one-time transition enters from combat, the encounter itself must declare every capability family it used. A future injury imported from AutoPTU depends on the full stateful damage pipeline and relevant lifecycle/status semantics being verified for that path; Pass 260 cannot substitute for them.

Following or intercepting an individual adds targeting/LoS, base movement, action economy/initiative, full turn/round lifecycle, AI legal-action infrastructure, AI tactical policy and adapter/playback. Complete movement is additionally required for interception, blocking, push/pull/knockback or forced movement. Other families are required only when the encounter invokes them.

## Open implementation questions

The production persistence layer still needs a restart-safe world-time basis and a registry of semantic-horizon evaluators. Species-specific recovery windows remain content policy rather than universal constants. Future AutoPTU semantic imports need an explicit signed/typed handoff so the ecology layer can distinguish authoritative injury/status/consequence records from Minecraft presentation noise.