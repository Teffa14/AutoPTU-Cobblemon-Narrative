# Holder History Coverage Baseline Checkpoint Contract — Pass 406

Status: ACTIVE IMPLEMENTATION CONTRACT
Canon effect: NONE

Pass 405 established that a baseline issued after safe recovery begins future-facing holder-history coverage at that semantic cut. Pass 406 gives those certificates their own deterministic persistence boundary so a later recovery can prove which starting assertions actually survived.

`OUROS_HOLDER_HISTORY_COVERAGE_BASELINE_CHECKPOINT_V1` stores the semantic minute and one `HolderHistoryCoverageBaseline` per resource. Records use canonical resource/id order and are protected by SHA-256 over the complete payload. Restore rejects malformed identity, duplicate resource coverage, duplicate baseline IDs, non-canonical order, baselines later than the checkpoint cut, a checkpoint from the future, and digest mismatch.

This owner does not certify pre-baseline history. It only persists a certificate that was already validly issued by the Pass 405 post-restore boundary. A later recovery must still pair a restored baseline with holder transitions strictly after its `at_tick` and apply the bounded continuity rules from Pass 403.

The checkpoint is deliberately separate from `OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1`. The baseline states the authoritative starting holder at one cut. The transition journal records later holder mutations. Keeping them separate prevents a journal checkpoint from silently manufacturing a starting assertion and prevents a baseline checkpoint from pretending to contain later custody events.

Pass 406 does not yet add this owner to the outer persistent-world recovery manifest. That integration requires a new manifest generation because legacy manifests never selected this digest. Until then, callers may persist and restore the owner independently, but may not treat it as selected recovery evidence.

Regression coverage lives in `tests/test_global_npc_holder_history_coverage_baseline_checkpoint.py`.

The next safe seam is a recovery-manifest generation that selects this checkpoint together with the holder-transition checkpoint at one semantic cut, followed by cross-owner validation that the selected baseline predates or equals every transition used to derive bounded coverage.

Stable AutoPTU battle/session identity and authoritative recovery of in-flight tactical resolution remain a larger independent blocker.
