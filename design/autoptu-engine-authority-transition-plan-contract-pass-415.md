# AutoPTU Engine Authority Transition Plan Contract — Pass 415

Status: DESIGN / EXECUTABLE CONTRACT — NOT CANON
Date: 2026-09-10

## Purpose

Pass 414 validates external AutoPTU authority reports against a restored Ouros session identity. Pass 415 adds the next conservative boundary: translate an already validated reconciliation into explicit follow-up intents without mutating tactical truth.

The planner consumes only the Pass 414 reconciliation plus a set of result references that a separate semantic-result admission path has already accepted.

## Transition meanings

`ACTIVE` produces `HOLD_ENGINE_BOUND`.

`COMPLETED` produces `HOLD_PENDING_RESULT_ADMISSION` unless the exact `authoritative_result_ref` is present in the admitted-result set. Only an exact admitted reference produces `RECORD_ADMITTED_RESULT`.

`UNKNOWN` produces `QUARANTINE_FOR_ENGINE_UNKNOWN`. This is an isolation intent, not a battle outcome.

`EXPLICITLY_ABANDONED` produces `HOLD_PENDING_ABANDONMENT_POLICY`. The authorization reference remains evidence. Pass 415 does not interpret abandonment as a win, loss, draw, forfeit, void, retirement or result.

## Safety invariants

A report claiming completion is insufficient to write battle truth.

An unrelated admitted result cannot unlock another session.

Every reported session must receive exactly one transition intent.

The planner does not mutate `AutoPTUSessionLedger`, release an `AUTOPTU_BOUND` world agent, change Minecraft state or synthesize a semantic battle payload.

A future executor may call `record_authoritative_result()` only for a `RECORD_ADMITTED_RESULT` intent and only after preserving the exact session/result binding proved here.

## Engine capability boundary

This contract adds no PTU mechanic. It changes no readiness classification for targeting/footprints/range/LoS, base movement legality, complete movement, core calculations, action economy/initiative, turn/round lifecycle, stateful damage, statuses, terrain/weather/hazards/zones/reactions, Moves, Abilities, Items or Trainer Features.

AI legal-action infrastructure and AI tactical policy are also unchanged. Minecraft/Cobblemon/Craftics remains presentation/playback only and cannot author the transition.

## Live AutoPTU-Java evidence

Inspected head: `befea9488953a07e510b5ad9152abaa314ae1332`, merge PR #438, `Register parity-safe Ball Fetch post-entry handler`.

That change registers a parity-tested Ball Fetch post-entry handler in the production switch path and leaves other post-entry families pending. It strengthens the narrow Ball Fetch/switch seam. It does not provide durable engine-session lookup, result recovery, complete switching, complete Abilities, complete movement or full lifecycle coverage.

AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest change is presentation-only.
