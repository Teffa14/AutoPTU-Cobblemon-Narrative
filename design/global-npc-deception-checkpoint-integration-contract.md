# Global NPC deception checkpoint integration — Pass 297

Status: PROPOSED EXECUTABLE INFRASTRUCTURE
Date: 2026-09-05

Pass 296 made deceptive statements travel through the same semantic communication machinery used by ordinary information. Pass 297 closes the recovery boundary that remained open: a restart must preserve the pending deceptive statement, its evidence basis, receiver attribution state, delivery status and coordinator idempotency guard as one coherent world-agent checkpoint.

The checkpoint schema advances to `OUROS_NPC_WORLD_CHECKPOINT_V2`. V2 records the concrete information-queue kind. `STANDARD` restores `InformationEventQueue`; `DECEPTION` restores `DeceptionInformationEventQueue` with its statements, event-to-statement mapping and `SourceAttributionStore`. Legacy V1 checkpoints remain readable as standard-queue checkpoints.

A deceptive delivery cannot survive restart as an ordinary truthful retransmission. Its authored assertion, real immediate speaker, private evidence basis and subjective declared source must remain distinguishable after restore. A delivery already materialized before the checkpoint cannot wake the receiver again after restart.

Unknown queue kinds fail closed. Digest validation still occurs before reconstruction. Queue-specific restore then validates its own child schema and statement references before the coordinator is returned.

This remains logical checkpoint atomicity. Physical crash-safe persistence, storage transactions, Minecraft acknowledgement durability and AutoPTU tactical-session reconciliation remain separate integration responsibilities.

No PTU, Caelo or Kairos rule is adopted by this contract. It governs Ouros world-agent persistence only.

Reduced narrative use requires no tactical engine capability. A false warning may be authored, queued, checkpointed, restored, delivered and investigated entirely in world state. Any later structured encounter inherits only the capability families it actually invokes.
