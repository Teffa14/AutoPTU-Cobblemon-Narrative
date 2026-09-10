# Persistent World Exact V4 Holder Generation Contract — Pass 410

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE
Date: 2026-09-10

## Purpose

Pass 409 proved that a holder-history certificate can retain its original certification cut while it is carried inside a later baseline-owner checkpoint.

Pass 410 binds the next recovery step to an exact `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V4` generation instead of allowing the holder recovery caller to start from an already-reconciled manifest assembled elsewhere.

`validate_exact_v4_holder_history_generation()` is the narrow coordinator for this boundary.

## Required order

The coordinator performs these stages in order:

1. reconcile the supplied recovery manifest against the five supplied owner checkpoints;
2. require that the manifest actually selected the holder-history baseline owner, which distinguishes V4 from legacy generations;
3. restore the exact selected WorldResource catalog at the manifest semantic cut;
4. restore the exact selected holder-transition checkpoint at the same cut;
5. pass the selected catalog, transition history and baseline checkpoint into the existing post-restore reconciliation;
6. issue fresh same-cut holder baselines only after the recovered current holder is proven safe.

Generation selection therefore precedes historical proof.

## Five-owner boundary

A V4 generation selects:

- global NPC checkpoint;
- persistent-world evidence checkpoint;
- WorldResource catalog checkpoint;
- ResourceHolderTransition checkpoint;
- HolderHistoryCoverageBaseline checkpoint.

Every supplied owner must match the manifest-selected digest. A valid checkpoint from another generation is not interchangeable merely because its schema and semantic minute are valid.

## Temporal meaning

A baseline stored in a checkpoint at T+N may still have `at_tick=T`.

The checkpoint minute records when the certificate collection was persisted for recovery selection. The baseline cut records when the holder fact was certified.

At recovery T+N, the system must replay every holder transition after T before comparing the derived holder to the recovered catalog.

A baseline issued at T+N after successful recovery is future-facing. It cannot be used as historical proof for the catalog that produced it.

## Regression contract

`tests/test_global_npc_holder_history_full_v4_rollover.py` exercises two later generations through real V4 manifest construction and reconciliation.

The regression starts from an earlier certified holder, carries the certificate forward, selects all five owner digests at a later semantic cut, restores the holder journal, replays intervening handoffs, validates the current catalog and only then emits the next baseline. It repeats that process for another later V4 generation.

A second regression supplies a valid baseline checkpoint from the wrong generation and requires rejection at the manifest digest boundary before holder reconciliation.

## Authority boundary

This contract changes persistent-world recovery plumbing only. It adds no Ouros canon and no PTU mechanic.

AutoPTU-Java and AutoPTU remain read-only. Minecraft/Cobblemon/Craftics cannot own or repair persistent holder history merely because it renders an item or actor.

## Remaining recovery seam

The holder-history path now has an exact V4 generation coordinator. The next useful persistence improvement is durable storage/selection orchestration for successive complete V4 generations rather than additional holder semantics.

The larger independent gap remains stable AutoPTU battle/session identity and authoritative recovery of tactical work that was in flight during a crash.
