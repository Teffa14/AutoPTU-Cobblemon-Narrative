# Persistent World V4 Baseline Reconciliation Contract — Pass 408

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE
Date: 2026-09-10

## Purpose

Pass 407 made `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V4` select the holder-history coverage baseline checkpoint as a fifth persistent-world owner. Pass 408 connects that selected owner to post-restore holder reconciliation without allowing circular proof.

## Authority boundary

The current WorldResource catalog remains the operational owner of current resource state.

A restored `OUROS_HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_V1` provides bounded historical evidence only when all of the following are true:

- the V4 recovery manifest selected its exact SHA-256 generation;
- its checkpoint semantic minute matches the recovery generation;
- the checkpoint passes its own integrity and canonical-order validation;
- an individual baseline begins strictly before the current recovery semantic minute;
- subsequent holder transitions replay continuously from the holder certified by that baseline.

A baseline whose `at_tick` equals the current recovery semantic minute is not admitted as evidence for that same cut. Such a certificate can be valid future-facing evidence for a later recovery generation, but using it to prove the catalog that produced it would be circular.

## Post-restore sequence

The activation boundary performs these operations in order:

1. verify current catalog and recovery semantic minute;
2. verify the selected holder-transition owner when V3/V4 requires it;
3. restore and verify the exact V4-selected baseline checkpoint;
4. admit only baselines whose cut is strictly earlier than the current recovery cut;
5. reconcile current WorldResource holder state against each admitted baseline plus later holder transitions;
6. fail closed on a continuity break or current-holder contradiction;
7. only after historical reconciliation succeeds, optionally issue fresh deterministic baselines from the exact selected WorldResource catalog checkpoint for future generations.

`CURRENT_CUT_BASELINE != CURRENT_CUT_PROOF`

## Replay rule

For an admitted baseline at tick T, holder replay consumes only transitions with `at_tick > T` through the current semantic minute.

Every transition must begin at the holder produced by the previous evidence step. A mismatch in `from_actor_id` is a continuity failure. Reconciliation must never skip a discontinuity and must never infer a missing holder mutation from custody, reservations, Minecraft presentation, or the current catalog.

## Compatibility

V1, V2 and V3 recovery manifests did not select the holder-history baseline owner. Their callers cannot inject a baseline checkpoint into post-restore validation.

The legacy `complete_holder_history_resource_ids` compatibility input remains separate. It cannot be combined with restored historical baselines in one reconciliation call.

## Recovery outcome

A bounded holder history can confirm the current holder only for the interval beginning at its authoritative baseline. It makes no claim about holder history before that cut.

A same-cut baseline selected in a V4 checkpoint remains preserved, but it is ignored for current-cut proof and becomes useful only at a later recovery cut if continuity can then be demonstrated.

## Remaining integration seams

The next persistent-world seam is generation advancement: carry a previously selected baseline into a later coherent recovery generation and prove that its later transition interval remains continuous while a new current-cut baseline is issued for the following generation.

An independent blocker remains stable AutoPTU battle/session identity plus authoritative recovery of tactical resolution that was in flight when a crash occurred. Persistent-world state and Minecraft presentation must not infer that outcome.
