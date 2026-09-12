# Global NPC Assistance Renegotiation Proposal Decision Dispatch Contract — Pass 448

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

Purpose

Pass 447 owns the requester's durable outcome for exact replacement terms. This pass transports a conscious acceptance or rejection back to the responder through the existing information network.

The owner is `schedule_assistance_renegotiation_proposal_decision_reply(...)` in `tools/global_npc_assistance_renegotiation_proposal_decision_dispatch.py`.

Causal boundary

The chain is now:

`original commitment -> adverse condition -> reopen request -> delivered permission -> replacement terms -> delivered replacement terms -> requester decision -> decision reply in transit -> responder receipt`

Each fact remains independently queryable. A private `ACCEPT_REPLACEMENT_TERMS` does not create shared knowledge. Only terminal `DELIVERED` materializes the responder's `REPORT` claim.

The reply payload preserves the replacement proposal identity, prior commitment/proposal lineage, exact requester outcome, decision rationale/time, replacement window, location/scope/alternative, expiry and proposal provenance.

`EXPIRED_UNANSWERED` is not dispatchable through this owner. It records an observed timeout rather than a communicative act by the requester. A later explanatory message, if authored, must be represented as its own communication.

Validation boundary

Dispatch fails closed when the decision, proposal, actor bindings, prior proposal delivery, REPORT evidence, provenance, timing, communication channel or event identity is inconsistent. Exact replay is idempotent; conflicting reuse of an event id is rejected.

Ownership exclusions

This pass does not create a replacement `ScheduledCommitment`. It does not mutate or erase the original commitment or replacement proposal. It does not reserve travel, grant access, allocate resources, move actors, alter relationships, adjudicate blame, complete a quest or invoke AutoPTU.

Quest and story boundary

A quest episode may react to the responder actually learning an acceptance or rejection, but transport itself owns no quest completion or social consequence. The old promise remains available for later accountability even if a future owner creates replacement terms.

Mechanics boundary

The reduced interaction needs no AutoPTU battle family. It uses semantic time, private knowledge, durable decision state and the existing information network.

If the accepted replacement later becomes a structured encounter, admit dependencies individually:

- targeting/footprints/range/LoS — VERIFIED only in audited scopes;
- base movement legality — VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only in audited scopes;
- action economy/initiative — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by requested behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features/perks — individually gated;
- AI legal-action infrastructure — specialized verbs require explicit admission;
- AI tactical policy — BLOCKING for specialized nonstandard objectives unless separately verified;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

Live engine evidence checked 2026-09-12

AutoPTU-Java `main` is `62f7f3671fd4176c49b359c8625e245905b19e2f` (PR #451). The new evidence freezes `check_guard -> arm_guard -> dispatch_quick_switch` for one Quick Switch ally-faint trigger path. It strengthens that narrow trigger contract only. It does not verify generic reactions/interrupts, complete action economy or the Trainer Features family.

AutoPTU Python `main` remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head is explicitly presentation-only and does not alter battle rules or outcomes.

Next seam

A delivered `ACCEPT_REPLACEMENT_TERMS` reply can become evidence for a separate replacement-commitment owner. That owner must verify both proposal and received acceptance, create a new commitment with explicit lineage, suppress future execution of the superseded schedule without deleting it, and leave accountability/social consequences to separate evidence-driven systems.