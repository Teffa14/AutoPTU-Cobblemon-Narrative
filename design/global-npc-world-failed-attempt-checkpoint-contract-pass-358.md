# Global NPC world failed-attempt checkpoint contract — Pass 358

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-08

Purpose

Integrate Pass 357 failed handoff-attempt history into the same coherent world checkpoint that already persists NPC state, reservations, requests, handoff authorization and custody transfer.

Target chain

world state + reservation + request + authorization + failed attempt -> one checkpoint -> restore -> later retry/replan

Core boundaries

`WORLD_RESTORE != ATTEMPT_REPLAY`

`FAILED_ATTEMPT_RESTORED != CUSTODY_CHANGED`

`OLD_SAVE_WITHOUT_ATTEMPT_HISTORY != INFERRED_ATTEMPT_HISTORY`

`EARLIER_FAILURE + LATER_SUCCESS` may both remain true.

Executable primitive

`tools/global_npc_world_resource_checkpoint.py` advances to `OUROS_NPC_WORLD_CHECKPOINT_V8` and embeds `OUROS_NPC_RESOURCE_CHECKPOINT_V3`.

The global SHA-256 covers the complete nested resource payload, including failed attempt identity, participant, location, time, outcome and observation provenance.

Restore rules

V8 restores Pass 339 reservations, Pass 342 requests, Pass 343 handoffs and Pass 344 attempts. Cross-ledger validation remains delegated to the narrow resource codecs.

V7 restores its real handoff history and an explicitly empty attempt ledger.

V6 restores its real reservations/requests and empty handoff/attempt ledgers.

Older world-only saves restore all resource ledgers empty. No state is inferred from possession, memory, dialogue, travel or later world facts.

Time rule

Completed request events, custody transfers and failed attempts cannot originate after the checkpoint semantic minute. Future reservation windows and future authorization windows remain legal because they describe scheduled state.

No duplicated owners

Pass 358 does not decide why an attempt failed, whether retry is allowed, who replans, or whether a later transfer succeeds. It only makes the already-owned Pass 344 evidence part of coherent world recovery.

Reduced narrative version

No AutoPTU dependency. Resource ledgers, semantic time, world checkpointing, travel, communication and replanning are sufficient.

Mechanically rich version dependencies

Targeting/footprints/range/LoS: required for exact tactical selection/perception around a blocked rendezvous.

Base movement legality: required for ordinary tactical approach/repositioning.

Complete movement including push/pull/knockback/interception/forced movement: required for physical interception, rescue, carrier displacement or forced access denial.

Core calculations: required when PTU arithmetic determines tactical outcomes.

Action economy/initiative: required for explicit pickup/drop/handoff/guard actions inside combat time.

Full turn/round lifecycle: required for round-bound deadlines, delayed arrivals or phase changes.

Full stateful damage pipeline: required when actors or carried equipment take authoritative damage.

Status lifecycle: required for persistent conditions affecting access or transport.

Terrain/weather/hazards/zones/reactions: each exact family remains separately gated.

Move-specific behavior, abilities, items and Trainer Features/perks: each exact mechanic remains individually gated.

AI legal-action infrastructure: required for new cargo/handoff/objective actions.

AI tactical policy: required for delivery-first, retry, protect-carrier, retreat, interception and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback: presentation only. Client proximity or animation cannot create a historical attempt.

Acceptance

V8 round-trip preserves world state and attempt history. V7 migration creates no attempt history. V6 migration creates no handoff or attempt history. Global digest covers attempt provenance. Future attempts fail closed. Unknown nested schemas fail closed. Repeated restore does not duplicate attempts or transfers.
