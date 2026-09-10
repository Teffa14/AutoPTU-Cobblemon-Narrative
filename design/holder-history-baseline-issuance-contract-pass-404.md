# Holder-History Baseline Issuance Contract — Pass 404

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE

## Purpose

Pass 403 introduced bounded holder-history coverage from an explicit authoritative cut. It still depended on callers constructing baseline objects correctly and preserving provenance manually.

Pass 404 makes baseline issuance deterministic from an already validated `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1` generation.

`tools/global_npc_holder_history_baseline_issuance.py` exposes `issue_holder_history_coverage_baselines_from_catalog_checkpoint()`.

## Authority boundary

The WorldResource catalog checkpoint remains authority for current operational resource state at its semantic cut.

The issuance layer derives a certificate for that cut. It does not become a new owner of resource state and it does not complete any holder history before the checkpoint.

Each baseline binds:

- resource identity;
- holder at the catalog semantic minute;
- exact catalog checkpoint SHA-256;
- deterministic baseline identity;
- checkpoint schema and digest provenance.

`BASELINE_FROM_CHECKPOINT != COMPLETE_PRECHECKPOINT_HISTORY`

## Deterministic issuance

The input checkpoint must pass the existing catalog restore validation before baselines are returned.

Resources use the canonical resource-id ordering already required by the catalog checkpoint.

Each baseline ID is derived from the checkpoint schema, exact catalog digest, semantic minute and resource ID. Reissuing from the same generation therefore produces the same baseline identities.

The baseline `source_ref` records the catalog checkpoint schema and exact digest. A restored caller can compare the digest selected by the outer recovery generation before trusting the baseline.

## Fail-closed behavior

Issuance rejects:

- a missing checkpoint SHA-256;
- a checkpoint whose content does not match its digest;
- an expected generation digest that differs from the supplied checkpoint;
- a checkpoint later than an explicitly supplied recovery semantic minute;
- any malformed catalog state already rejected by `restore_world_resource_catalog()`.

No baseline is emitted from an unvalidated or tampered catalog generation.

## Recovery integration boundary

Pass 404 supplies deterministic baseline certificates but does not yet persist them as an independent checkpoint owner.

The safer next step is to let the post-restore path reissue baselines from the exact WorldResource catalog snapshot selected by the recovery manifest and compare that digest with the manifest-selected catalog digest. That avoids storing another redundant owner when the certificate can be reproduced from an already authoritative generation.

If later requirements need long-lived baseline issuance independent of the original snapshot bytes, introduce a dedicated certificate checkpoint only with explicit generation provenance and restore validation.

## Mechanical boundary

This pass affects persistent world resource provenance only. It grants no PTU Skill, Edge, Feature, Item, move, ability, status, hazard, weather rule, movement rule or tactical outcome.

Stable AutoPTU battle/session identity and in-flight tactical recovery remain separate blockers.
