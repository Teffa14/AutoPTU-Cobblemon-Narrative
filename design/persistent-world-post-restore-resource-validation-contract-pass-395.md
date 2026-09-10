# Persistent World Post-Restore Resource Validation Contract — Pass 395

Status: DESIGN / EXECUTABLE CONTRACT. Not canon.
Date: 2026-09-10

## Purpose

Pass 393 binds global-NPC state, persistent evidence and the current WorldResource catalog to one recovery generation. Pass 394 compares restored current resource state against reservation and handoff history. Pass 395 makes that comparison an explicit post-restore activation gate.

The executable owner is `tools/global_npc_persistent_world_post_restore.py`.

## Order of operations

Recovery proceeds in four distinct stages.

1. `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2` selects one coherent generation.
2. Each owner restores and validates its own schema, digest and semantic-time constraints.
3. Pass 395 compares cross-owner facts that become meaningful only after those restores exist.
4. The world may activate only when the post-restore report contains no explicit conflict.

The gate does not replace any earlier owner.

`COHERENT_GENERATION_SELECTION != CROSS_OWNER_SEMANTIC_VALIDATION`

`INDETERMINATE_HISTORY != RECOVERY_FAILURE`

`EXPLICIT_CONFLICT != SAFE_ACTIVATION`

## Inputs

Pass 395 consumes an already reconciled V2 recovery manifest, an already restored `RestoredWorldResourceCatalog`, the restored `ReservationLedger`, and the restored `ResourceHandoffLedger`.

The resource catalog semantic minute must exactly match the selected manifest minute. Legacy V1 manifests cannot use this stage because they do not bind a resource-catalog owner.

## Conflict handling

Pass 394 remains the authority for classifying resource-history findings.

If that report contains `CONFLICT`, Pass 395 fails closed before world activation. The exception carries stable reason codes so operators and regression tests can identify the contradiction.

The gate does not repair the catalog, clear reservations, rewrite custody history or invent a missing transition.

## Indeterminate handling

`INDETERMINATE` findings remain visible in the returned report. They do not block activation by themselves.

Examples include an active reservation not projected into current catalog state, a current holder that cannot be derived from known handoffs, or historical references to a resource absent from the current catalog.

These are incomplete-history diagnostics. Treating them as corruption would manufacture certainty the project does not possess.

## Narrative consequence

Recovery can preserve ordinary institutional ambiguity. A field team may possess a resource while an older desk record still names a previous holder. A dispatcher may have an active reservation record before the catalog projection has been applied. NPCs may disagree because they possess different records, while the server still rejects combinations that are explicitly impossible.

## PTU / AutoPTU boundary

This stage is persistent-world infrastructure only. It introduces no PTU action, Skill check, Trainer Feature, Item effect, movement rule or battle result.

Narrative scenes built on resource disagreement can run entirely as world-state investigation. If combat, hazards, escort, forced movement or timed objectives are added, their exact permanent capability families must be declared separately.

## Deferred work

A complete holder-transition journal can later turn some current `INDETERMINATE` holder findings into stronger confirmations or conflicts. Pass 395 does not infer that journal from checkout, return or handoff consequences.

Recovery of an in-flight AutoPTU session also remains a separate seam. Neither this gate nor Minecraft may infer that a tactical session completed because world state resumed.
