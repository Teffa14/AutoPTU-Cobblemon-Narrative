# Persistent World Recovery Manifest V3 Contract — Pass 398

Status: EXECUTABLE CONTRACT
Canon impact: NONE

Pass 397 made `OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1` independently recoverable. Pass 398 binds that owner into the persistent-world generation selector instead of allowing current resource state and holder history to restore from different semantic moments.

## Selected generation

`OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V3` selects one exact SHA-256 generation for all four owners:

- `OUROS_NPC_WORLD_CHECKPOINT_V19` through the current global-NPC checkpoint schema;
- `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2`;
- `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1`;
- `OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1`.

All four checkpoints must report the same non-negative `semantic_minute`. A valid checkpoint from another minute, or another valid generation from the same minute, is rejected when its digest differs from the selected generation.

## Authority boundary

The manifest owns generation selection only. It does not copy or merge owner payloads.

The world-resource catalog remains authority for current mutable resource state. The holder-transition journal records explicit holder changes that passed through its wrappers. Reservation and handoff ledgers retain their existing responsibilities. Persistent evidence retains discovery and inference provenance. Global NPC recovery retains causal world-agent state.

A matching manifest cannot promote an incomplete holder journal into universal history. Future mutation paths still require audit before that claim can be made.

## Legacy recovery

V1 remains readable as a two-owner legacy selector and returns no resource-catalog or holder-transition digest.

V2 remains readable as a three-owner legacy selector and returns no holder-transition digest.

Neither migration manufactures a historical journal from current holder state, reservations, custody records or Minecraft presentation.

## Failure policy

V3 fails closed when:

- any owner has the wrong schema;
- any owner digest fails its own integrity check;
- semantic minutes differ;
- the manifest digest is invalid;
- a candidate owner digest differs from the selected digest;
- the holder-transition candidate is absent.

Owner-specific restore validation still runs after generation selection. Pass 395 post-restore validation should only consume holder-history evidence after the selected holder checkpoint has itself restored successfully.

## Next seam

The next safe step is to extend the Pass 394/395 reconciliation path so a restored holder-transition ledger can prove some current-holder relationships that previously had to remain `INDETERMINATE`. That integration must preserve `INDETERMINATE` whenever the journal does not actually contain the necessary causal transition.
