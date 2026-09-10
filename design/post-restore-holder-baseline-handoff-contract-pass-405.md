# Post-Restore Holder Baseline Handoff Contract — Pass 405

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE

## Purpose

Pass 404 can issue deterministic `HolderHistoryCoverageBaseline` certificates from an exact validated WorldResource catalog checkpoint.

Pass 405 defines where those certificates may enter recovery.

## Same-cut circularity rule

A baseline created from catalog generation T must not be used to validate the holder state of that same catalog generation T.

Doing so would use current catalog state as evidence for current catalog state and could hide incomplete pre-T holder history.

Historical reconciliation therefore runs first without newly issued recovery baselines.

Only after the reconciliation report is safe may the selected catalog checkpoint issue new baselines. Those certificates begin bounded holder-history coverage at T for future semantic time.

## Selected-generation rule

When post-restore activation is asked to issue new baselines, the caller provides the raw `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1` snapshot retained from recovery selection.

The activation boundary validates:

1. checkpoint integrity through the catalog owner;
2. checkpoint semantic minute against the recovery cut;
3. checkpoint SHA-256 against `ReconciledPersistentWorldRecoveryManifest.world_resource_catalog_checkpoint_sha256`;
4. restored checkpoint contents against the `RestoredWorldResourceCatalog` that is about to activate.

A valid checkpoint from a different generation of the same minute is rejected.

## Compatibility boundary

A V3 caller that does not retain the raw selected catalog checkpoint may continue using conservative post-restore reconciliation. It receives no new holder-history baseline certificates.

Callers can no longer pass arbitrary `HolderHistoryCoverageBaseline` objects into `validate_persistent_world_post_restore()`.

Legacy `complete_holder_history_resource_ids` remains a separate compatibility input. It does not gain authority from Pass 405.

V1/V2 recovery paths do not issue the new holder baseline handoff because those manifests did not select the holder-transition owner.

## Result contract

`PersistentWorldPostRestoreValidation.issued_holder_history_coverage_baselines` contains the deterministic certificates emitted after successful V3 validation when the exact selected catalog checkpoint was supplied.

An unsafe reconciliation raises before any result containing baselines is returned.

The certificates record the restored holder at the recovery cut. They make no claim about holder history before that cut.

## Regression coverage

`tests/test_global_npc_post_restore_baseline_issuance.py` covers:

- successful deterministic issuance from the exact selected generation;
- rejection of a different catalog generation at the same semantic minute;
- rejection when the raw checkpoint digest differs from the outer manifest;
- preservation of pre-checkpoint journal uncertainty rather than circular confirmation;
- conservative V3 operation without raw checkpoint retention, which issues no baselines.

## Next seam

The next holder-history step is to carry the newly issued baseline into subsequent checkpoint/recovery generations as the start of a demonstrably covered interval, together with the holder-transition journal and the Pass 402 production mutation-callsite guard.

Stable AutoPTU battle/session identity and authoritative recovery of in-flight tactical resolution remain the larger independent recovery blocker.
