# Semantic horizon registry and world clock contract

Status: PROPOSED DESIGN CONTRACT. Does not change established species canon or PTU rules.

## Purpose

Pass 260 requires semantic retention horizons but leaves their evaluator model and restart-safe clock unresolved. This contract defines a typed registry and a fail-closed clock abstraction for ecological state.

The registry decides when already-authorized retained state should be reevaluated. It does not decide population, species behavior, player knowledge, PTU outcomes or identity promotion by itself.

## Core invariants

A horizon evaluation cannot create or remove a Pokémon.

`population total before == population total after`

A clock read cannot author ecology or PTU truth. Time may trigger an evaluation, but the evaluator still requires the state class, authority source and declared horizon policy.

Restart, chunk unload, renderer absence, failed detection, server lag, time-of-day changes and generic despawn cannot imply expiry.

Time-of-day is presentation/context input only. It cannot serve as the monotonic retention clock because day/night can be changed or frozen independently of elapsed world execution.

No horizon can upgrade public identity knowledge unless another explicit epistemic contract authorizes that change.

No horizon can convert Minecraft/Cobblemon presentation state into HP, injury, status, Move, Ability, item, ownership, capture or battle truth.

## Ouros ecological clock

The ecology layer consumes an abstract clock record:

`clock_domain`

`clock_epoch`

`monotonic_value`

`checkpoint_id`

`source_adapter`

`source_version`

`observed_raw_value`

`previous_committed_value`

`rollback_detected`

The intended ordering key is:

`(clock_epoch, monotonic_value)`

A production adapter may derive `monotonic_value` from a persisted Minecraft world-time counter only after the exact pinned runtime verifies the required persistence behavior.

The contract explicitly rejects time-of-day as the monotonic basis.

## Rollback and restore rule

If the adapter observes a raw time value lower than the last committed raw checkpoint, it must not evaluate normal duration expiry against that value.

Allowed fail-closed outcomes:

- create a new `clock_epoch` after an explicit world-restore/migration transaction; or
- mark the clock `ROLLBACK_QUARANTINED` and suspend horizon expiry until reconciliation.

Forbidden outcome:

- silently treating the lower value as evidence that a state expired, recovered, never occurred or moved backward in ecology history.

A backup restore may legitimately restore old world data. That operation requires explicit lineage/reconciliation rather than pretending history remained monotonic.

## Horizon registry entry

Each registered semantic horizon contains:

`horizon_type`

`applicable_state_classes`

`required_authority_sources`

`evaluator_kind`

`clock_domain`

`open_condition`

`close_condition`

`restart_policy`

`rollback_policy`

`on_reached_outcome`

`on_invalid_outcome`

`public_identity_effect`

`population_effect = NONE`

`ptu_state_authority = NONE` unless consuming an already-authoritative semantic result

## Evaluator kinds

### PROJECTION_LIFECYCLE_BOUND

Use for admission tokens, projection leases, save/load receipts and renderer reconciliation state.

The horizon closes from an authoritative projection/reconciliation lifecycle event, not from elapsed ecology time.

Typical outcome: drop short-lived private correlation while preserving duplicate-prevention audit state required by the owning projection contract.

### DURATION_SINCE_AUTHORITY_EVENT

Use only when the retained consequence has an explicitly approved duration model whose opening event is authoritative.

Examples can include a future species/context-specific disturbance recovery window.

The registry stores the duration policy reference, not a universal number.

Repeated qualifying events may extend or replace the horizon only when the state-class policy explicitly defines that behavior.

### CONDITION_STABLE_FOR

Use when closure requires a condition to remain satisfied continuously for a declared interval.

Example candidate: local disturbance pressure remains below a recovery threshold for a species/context-specific stable window.

A single low-pressure observation cannot complete this horizon if stability was required.

### VALIDITY_RECORD_BOUND

Use when another authoritative record owns validity.

Example: an approved diegetic marker remains valid until its registry entry becomes damaged, lost, retired or otherwise invalidated.

Clock time may prompt reevaluation, but the validity record owns the result.

### AUTHORITY_EVENT_BOUND

Use for one-time state whose closure occurs only when the owning subsystem emits a semantic event.

Examples can include a future adjudicated migration arrival, dispersal settlement, treatment completion or battle consequence resolution.

Silence does not close it.

### MANUAL_REVIEW_REQUIRED

Use when current evidence cannot safely define automatic closure.

The state remains bounded/quarantined and visible to internal review tooling. It cannot be smeared into aggregate population state while unresolved.

## State-class mappings proposed by Pass 261

`PRESENTATION_CORRELATION -> PROJECTION_LIFECYCLE_BOUND`

`RECENT_SITE_USE -> DURATION_SINCE_AUTHORITY_EVENT` only when an approved site-use policy defines a horizon; otherwise manual/drop policy from Pass 260 applies.

`INDIVIDUAL_DISTURBANCE_RESPONSE -> CONDITION_STABLE_FOR` or `DURATION_SINCE_AUTHORITY_EVENT`, selected by the species/context response policy.

`ACTIVE_DIEGETIC_MARKER_LINK -> VALIDITY_RECORD_BOUND`

`AUTHORITATIVE_ONE_TIME_TRANSITION -> AUTHORITY_EVENT_BOUND` unless the owning semantic result declares another explicit horizon type.

`INFERRED_BEHAVIOR_LABEL -> MANUAL_REVIEW_REQUIRED` or uncertain-evidence expiry; never automatic latent-state promotion.

These mappings are design defaults, not species-specific canon.

## Evaluation transaction

Each evaluation must contain:

`evaluation_transaction_id`

`retained_state_id`

`horizon_type`

`registry_policy_id`

`clock_checkpoint_id`

`clock_epoch`

`evaluated_at_monotonic_value`

`authority_inputs`

`horizon_reached`

`result`

`population_delta = 0`

`demographic_event = false`

Evaluations must be idempotent. Replaying the same transaction with the same payload is a no-op. Reusing its ID with a different payload is rejected.

## Offline-time boundary

Pass 261 does not decide whether ecological time advances while no server process is running.

If future Ouros requires offline progression, add a separate declared clock domain such as `OUROS_CALENDAR_TIME`. Do not silently mix wall-clock elapsed time with Minecraft running-world ticks.

Cross-domain horizons must explicitly name which domain owns them.

## Interaction with AutoPTU

This contract never creates battle results.

A future AutoPTU semantic result may open or close a registered horizon only after the handoff proves that result came from the authoritative battle path. The imported record must remain typed and provenance-bearing.

A future injury horizon therefore depends on the full stateful damage pipeline and every other capability family actually used to produce that result. A timer cannot make an unverified injury authoritative.

## Marea/Sendero fixture policy

Pass 261 uses synthetic clock values and policy IDs only.

The fixture demonstrates:
- time-of-day mutation does not alter the monotonic ecology clock;
- a recent site-use horizon can close by an explicit duration policy;
- an active disturbance response survives restart when its condition is not yet stable long enough;
- a marker validity event closes a validity-bound state independent of elapsed ticks;
- a clock rollback suspends automatic expiry rather than fabricating recovery;
- population remains twelve and no AutoPTU handoff occurs.

No fixture duration becomes Fletchling canon.

## Engine capability boundary

The reduced clock/registry lifecycle needs no tactical AutoPTU category.

Production clock extraction, projection lifecycle correlation and visible ecological consequences depend on Minecraft/Cobblemon/Craftics adapter/playback support.

A richer scene that follows or intercepts an individual adds targeting/LoS, base movement, action economy/initiative, full turn/round lifecycle, AI legal-action infrastructure, AI tactical policy and adapter/playback. Complete movement is additionally required when interception, blocking, push/pull/knockback or forced movement occurs.

## Open questions

- Exact pinned Minecraft/Cobblemon/Craftics runtime and the persisted field/API that can safely back `OUROS_WORLD_TICK`.
- Whether production requires an offline-progressing `OUROS_CALENDAR_TIME` domain.
- Species/context-specific recovery policies and whether they are duration-bound, condition-stable or event-bound.
- How explicit world rollback/backup restore increments or reconciles `clock_epoch`.
- The typed semantic-result envelope for future AutoPTU-authored ecological consequences.
