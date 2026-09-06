# Global NPC AI readiness snapshot — Pass 297

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-05

Narrative repo head before this pass: `138760fa2f0f15ab4ffa72079a097f09d79a2a3c`.

Read-only engine evidence checked during this pass:

- AutoPTU-Java `722fadbd908eb13cb3bfd2c2ad834426655adaae` — PR #375 adds a typed immutable `BorrowMoveEndedEvent`, registers a dedicated semantic event kind, normalizes ordered borrowed-move identities, and tests stable-key/validation behavior. This improves authoritative adapter-facing event semantics for one temporary-move expiry seam. It does not prove the move corpus, Trainer Features, lifecycle or adapter playback complete.
- AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — head remains presentation-only and explicitly states that battle rules and outcomes do not change.

Capability classification retained conservatively:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

Pass 297 deception-checkpoint integration has no tactical dependency in its reduced form. It preserves world-agent evidence, statements, subjective attribution, queue state and wake-up idempotency across logical restart.

If a later consequence enters structured battle, it inherits only the exact capability families exercised. One typed borrowed-move expiry event is narrow evidence and does not promote any family.
