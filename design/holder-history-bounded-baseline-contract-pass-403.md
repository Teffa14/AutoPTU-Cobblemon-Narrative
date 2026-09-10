# Holder-History Bounded Baseline Contract — Pass 403

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE

## Purpose

Pass 402 made the known production holder-mutation boundary continuously auditable. That still did not justify treating the entire lifetime of an older `WorldResource` as journal-complete.

Pass 403 adds an explicit bounded starting point.

`HolderHistoryCoverageBaseline` records:

- one resource identity;
- one semantic tick;
- the authoritative holder immediately after all holder mutations at that cut;
- a stable baseline identity;
- a provenance reference for the authoritative cut-state source.

`derive_bounded_holder_history_coverage()` replays only journaled holder transitions strictly later than that baseline through the requested semantic cut.

## Core invariant

A baseline proves continuity forward from its own cut. It does not rewrite or complete earlier history.

`BOUNDED_COVERAGE_AFTER_T != COMPLETE_LIFETIME_HISTORY`

This matters when an older resource existed before `ResourceHolderTransitionLedger` was introduced. An authoritative checkpoint can establish who held it at tick T. Later journal continuity can then prove holder state after T without pretending that every earlier checkout, return or handoff is known.

## Fail-closed conditions

Coverage derivation rejects:

- a baseline for a resource absent from the current catalog;
- duplicate baseline identity;
- multiple simultaneous baselines for the same resource in one derivation;
- a baseline later than the requested coverage cut;
- a later journal transition whose `from_actor_id` does not match the holder derived so far.

A baseline and the legacy `complete_holder_history_resource_ids` assertion cannot be supplied together to the same reconciliation call.

## Reconciliation behavior

`reconcile_world_resource_history()` now accepts `holder_history_coverage_baselines`.

When bounded coverage exists for a resource, reconciliation compares current catalog holder state with the holder derived from:

1. the authoritative baseline holder;
2. every journal transition after the baseline and through the current semantic minute.

A match emits `CURRENT_HOLDER_MATCHES_BOUNDED_HOLDER_HISTORY`.

A mismatch emits `CURRENT_HOLDER_CONFLICTS_BOUNDED_HOLDER_HISTORY` and fails restore closed.

Older journal entries before the baseline remain historical evidence, but they are not treated as complete coverage.

## Post-restore boundary

`validate_persistent_world_post_restore()` forwards bounded baselines into the existing reconciliation gate. V3 holder-transition ownership is still required before holder coverage can be used after recovery.

Pass 403 does not yet persist baseline certificates as a dedicated checkpoint owner. The baseline source must therefore be issued from an authoritative cut-state source whose provenance is retained by the caller.

## Remaining questions

The next recovery seam is to make baseline issuance deterministic from a coherent `WorldResource` catalog checkpoint and to persist enough provenance that a restored process can validate that the baseline belongs to the intended generation.

Stable AutoPTU battle/session identity remains a separate blocking seam for in-flight tactical recovery.
