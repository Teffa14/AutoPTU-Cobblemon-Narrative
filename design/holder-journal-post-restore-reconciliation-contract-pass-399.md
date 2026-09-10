# Holder Journal Post-Restore Reconciliation Contract — Pass 399

Status: EXECUTABLE CONTRACT
Canon impact: NONE
Date: 2026-09-10

Pass 398 bound the holder-transition checkpoint into the same recovery generation as global NPC state, persistent evidence and the current WorldResource catalog. This pass lets post-restore validation consume that successfully restored holder history without pretending the journal is universally complete.

## Recovery sequence

The safe activation sequence is now:

1. select one coherent recovery generation with `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V3`;
2. restore each selected owner under its own validation rules;
3. require the restored holder-transition owner to share the manifest semantic minute;
4. reconcile current WorldResource state against reservations, custody transfers and holder transitions;
5. fail closed on demonstrated contradictions;
6. keep unsupported gaps visible as `INDETERMINATE`;
7. activate the persistent world only after the cross-owner checks pass.

A V3 manifest that selected a holder checkpoint cannot proceed through the Pass 399 activation stage without the corresponding restored holder-transition owner. A legacy V1/V2 manifest cannot inject an unselected holder journal after recovery.

## Completeness gate

`ResourceHolderTransitionLedger` records only mutations routed through its wrappers. It is therefore evidence, but not automatically a complete event stream.

`reconcile_world_resource_history()` accepts an explicit `complete_holder_history_resource_ids` set. Membership is an assertion by the caller that all holder mutation paths relevant to that resource and recovery generation have been audited and journaled.

For an audited-complete resource:

- current holder equal to the latest journal target -> `CONFIRMED`;
- current holder different from the latest journal target -> `CONFLICT`;
- no holder transitions plus no current holder -> `CONFIRMED`;
- no holder transitions plus a current holder -> `CONFLICT`.

For a resource whose journal coverage has not been audited complete, the presence of holder transitions stays `INDETERMINATE`. Matching data does not silently upgrade the journal into universal truth.

## Current audit boundary

Repository call-site inspection found journal wrappers for ordinary checkout, return and authorized handoff. It also found a production bypass in `tools/global_npc_resource_handoff_rescheduling.py`: `execute_current_authorized_handoff()` still delegates directly to `execute_authorized_handoff()` after checking the current authorization.

Therefore Pass 399 does not declare holder history globally complete. A caller must not place resources that can traverse unaudited mutation paths into `complete_holder_history_resource_ids`.

Closing or explicitly journal-wrapping the rescheduled-handoff path is a future seam before broader completeness claims are safe.

## Temporal checkpoint hardening

`OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1` now rejects any transition whose `at_tick` is later than the checkpoint's own `semantic_minute`, both while snapshotting and while restoring a redigested payload.

A checkpoint represents a semantic cut. It may not contain future holder history merely because the outer SHA-256 is internally consistent.

## Authority boundary

The current WorldResource catalog remains authority for present mutable resource state.

Reservation history remains authority for its reservation records.

Resource handoff history remains authority for authorized custody transfers.

Holder-transition history remains authority only for explicit holder mutation records routed through that journal.

The reconciliation layer compares those owners. It does not rewrite them, create missing events, infer theft, infer deception, or mutate NPC knowledge.

## Narrative consequence

A documented mismatch can now have three meanings with different consequences:

- `CONFIRMED`: audited history proves the current holder relationship is coherent;
- `CONFLICT`: audited history proves two restored owners cannot both describe the selected generation;
- `INDETERMINATE`: the available records do not justify either conclusion.

Only the second category is a recovery-integrity failure. The third remains usable as legitimate uncertainty inside the world.

## Mechanical boundary

This contract adds no PTU battle rule, Skill check, Move effect, Ability, Item effect, Trainer Feature, movement permission, reaction, terrain effect or AI combat policy.

If a narrative scene turns resource recovery into tactical escort, forced movement, timed extraction, weather pressure or an objective-based fight, it must declare those capability dependencies separately and route structured combat to AutoPTU.

## Next seam

Audit and close remaining holder-mutation bypasses, beginning with rescheduled handoff execution. After coverage is actually universal for a resource class, the completeness assertion can be derived from an audited contract instead of supplied manually.

Stable AutoPTU battle/session identity and crash recovery remain separate unresolved work.