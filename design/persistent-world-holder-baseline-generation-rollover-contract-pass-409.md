# Persistent World Holder Baseline Generation Rollover Contract — Pass 409

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE
Date: 2026-09-10

## Purpose

Pass 408 proves that a Recovery Manifest V4 generation can use a selected older holder-history baseline plus later `ResourceHolderTransition` records to validate current `WorldResource.holder_actor_id`, then issue a new same-cut baseline after successful reconciliation.

Pass 409 defines how that newly issued certificate survives into a later recovery generation without changing what it proves.

## Rollover rule

Given a safe post-restore validation at semantic minute T:

`SAFE RECOVERY AT T -> ISSUE BASELINE(at_tick=T) -> PERSIST THAT CERTIFICATE IN A LATER BASELINE CHECKPOINT -> RECOVER AT T+N -> REPLAY EVERY HOLDER TRANSITION AFTER T -> VALIDATE HOLDER AT T+N -> ISSUE BASELINE(at_tick=T+N)`

The baseline-owner checkpoint's `semantic_minute` may be later than the certificate's `at_tick`. These fields have different meanings.

The checkpoint semantic minute states when that baseline-owner generation is persisted for recovery selection. The baseline `at_tick` states the exact cut at which the holder fact was certified.

Rollover must never rewrite the baseline `at_tick` to the later checkpoint minute.

## Admission requirements

`carry_forward_issued_holder_history_baselines()` accepts only a `PersistentWorldPostRestoreValidation` whose resource reconciliation is safe to activate and whose validation actually issued holder-history coverage baselines.

Every issued baseline must begin at the validation's semantic minute. This prevents an arbitrary older certificate collection from being relabeled as the direct output of that recovery.

The requested checkpoint semantic minute must be an integer at or after the validated recovery cut.

## What rollover proves

Rollover proves only that the same certificate was durably preserved into a later owner checkpoint.

It does not prove the holder remained unchanged between the baseline cut and the later checkpoint. That fact must be derived by replaying the holder-transition journal during the later recovery.

It does not make history before the baseline complete.

It does not authorize a same-cut baseline to validate the catalog from which that baseline was issued.

It does not replace Recovery Manifest V4 generation selection.

## Failure behavior

The helper fails closed if the originating validation is unsafe, no baseline was issued, an issued certificate does not begin at the validated cut, or the requested checkpoint minute is before that cut.

At the next recovery, `derive_bounded_holder_history_coverage()` remains responsible for rejecting a journal transition whose `from_actor_id` does not match the holder produced by the prior certified state.

## Regression contract

`tests/test_global_npc_holder_history_generation_rollover.py` demonstrates:

- baseline at T=10 plus a valid handoff at 15 validates holder B at 20;
- safe validation at 20 issues a new baseline with `at_tick=20`;
- the baseline can be carried in a baseline-owner checkpoint whose semantic minute is 40 while preserving `at_tick=20`;
- a later valid handoff at 30 validates holder C at 40 and issues a new `at_tick=40` certificate;
- that certificate can be carried forward again;
- moving a certificate into a checkpoint earlier than its validated cut is rejected;
- a discontinuous next-generation journal fails closed.

## Authority boundary

This is persistent-world recovery evidence only. It changes no Ouros canon and no PTU rule.

AutoPTU-Java and AutoPTU remain read-only from this narrative task. Minecraft/Cobblemon/Craftics does not own holder-history truth merely because it displays or animates a carried resource.

## Next recovery seam

The next useful recovery improvement is to bind this rollover path to a complete later V4 manifest-generation fixture rather than only the post-restore owner contracts. That fixture should prove all five selected owner digests at T+N, restore the prior baseline certificate, replay the intervening holder journal, validate the new catalog, and only then produce the future-facing replacement baseline.

The larger independent blocker remains stable AutoPTU battle/session identity and authoritative recovery of tactical work that was in flight during a crash.
