# Global NPC atomic world checkpoint contract — Pass 292

Status: PROPOSED EXECUTABLE INFRASTRUCTURE
Date: 2026-09-05

Pass 291 added durable per-NPC knowledge-ledger snapshots. Pass 292 closes the next boundary: several individually restorable components can still form an impossible world if they are saved from different causal moments.

`RESTART != WORLD_STATE_SPLIT`

`LOGICAL_CHECKPOINT != DURABLE_STORAGE_TRANSACTION`

`OUROS_NPC_WORLD_CHECKPOINT_V1` packages one semantic minute, managed `NpcAgentState`, all `KnowledgeLedger` snapshots, `InformationEventQueue`, `NpcReplanQueue`, the coordinator materialized-delivery idempotency guard, and an optional versioned publication-runtime child snapshot.

Static communication-channel definitions and authored agenda profiles remain configuration inputs during restore. They are not mutable checkpoint facts.

The checkpoint carries SHA-256 over canonical JSON for the full payload excluding the digest field. Restore validates schema and digest before constructing live objects. After component restoration it validates that pending/local-ack envelopes reference existing sender/receiver ledgers and an existing sender source claim. It also rejects materialized coordinator event IDs that the information queue does not record as delivered.

The digest detects accidental mismatch or corruption. It is not an authenticity signature and does not replace a storage transaction.

A pending message remains pending and keeps its semantic delivery time. A delivered claim remains in the receiver ledger and managed-agent knowledge refs. A completed materialization does not become a second wake-up after restart. A delivery never completed cannot appear in the coordinator guard. A restart never becomes in-fiction forgetting, teleportation, publication, delivery, correction or tactical resolution.

Publication/revision runtime snapshots may be embedded, but their own runtime class remains responsible for reconstruction after the coordinator exists. This avoids circular ownership.

The checkpoint preserves `active_autoptu_binding` references already present on world-agent state. It does not serialize AutoPTU battle state and cannot author or repair a tactical outcome. Production recovery still needs reconciliation with the authoritative AutoPTU session store.

Physical crash-safe commit remains a storage-adapter responsibility. The selected backend must eventually provide an atomic transaction, journal/commit protocol, atomic replace or equivalent so that one validated checkpoint becomes durable as a unit.

The checkpoint itself requires no tactical capability family. Any later scene inherits only the mechanics it actually uses. Push/pull/knockback/interception needs complete movement. Mechanical weather/hazards/zones/reactions need that capability family. Delayed or phase-sensitive effects need relevant lifecycle/status plus the owning Move/Ability/Item/Trainer Feature family. Autonomous combat choice needs AI tactical policy. Visible authoritative execution needs Minecraft/Cobblemon/Craftics adapter/playback.

Acceptance evidence: queue a warning, checkpoint before delivery, restore without early knowledge, deliver once, checkpoint after delivery, restore again without replay, and keep an uninvolved bystander unaffected. Corrupt digest and impossible materialization-guard state must fail closed.
