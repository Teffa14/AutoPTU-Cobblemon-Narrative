# Global NPC Assistance Renegotiation Proposal Decision Contract — Pass 447

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

Purpose

Pass 446 can carry responder-authored replacement assistance terms through the existing information network. This pass owns the next durable fact: what the requester does with the exact terms that were actually received.

The owner is `OUROS_ASSISTANCE_RENEGOTIATION_PROPOSAL_DECISION_LEDGER_V1` in `tools/global_npc_assistance_renegotiation_proposal_decision.py`.

The ledger recognizes three outcomes:

- `ACCEPT_REPLACEMENT_TERMS`
- `REJECT_REPLACEMENT_TERMS`
- `EXPIRED_UNANSWERED`

An acceptance or rejection requires the proposal event to have reached terminal `DELIVERED`. The requester must possess the delivered `REPORT`, its parent/source claim must still exist, subject/value/provenance must match, and the serialized terms must equal the durable Pass 445 proposal record exactly.

`EXPIRED_UNANSWERED` is available only when the offer has a real `expires_minute` and semantic time has advanced beyond it. An offer is still actionable at its exact expiry minute. After that minute the same proposal cannot be accepted or rejected through this owner.

The old negotiated commitment remains history. The replacement proposal also remains an offer. Recording `ACCEPT_REPLACEMENT_TERMS` does not yet create a new `ScheduledCommitment`, cancel the old one, reserve travel, grant access, allocate resources, move either actor, alter relationships, adjudicate blame or invoke AutoPTU.

Causal chain after this pass

`original commitment -> adverse condition -> reopen request -> delivered permission -> replacement terms -> delivered replacement terms -> exact requester outcome`

Every arrow remains independently queryable. A delivered offer does not imply agreement. A requester's private decision does not imply that the responder knows the answer.

Validation boundary

The owner fails closed when:

- the event is missing or not terminal `DELIVERED`;
- the deciding actor is not the delivered requester;
- source or received claim is absent;
- the received claim is not a `REPORT`;
- parent/provenance/subject/value lineage differs from the authored proposal;
- serialized terms differ from the Pass 445 proposal record;
- the decision predates actual receipt;
- acceptance/rejection occurs after expiry;
- expiry is asserted before the deadline passes or when no expiry exists;
- a `decision_id` is reused with conflicting content.

Snapshot/restore is deterministic and append-only at the record level. Exact replay is idempotent.

Quest and story boundary

This owner is compatible with the canonical quest graph because it records a world decision that later quest episodes may read. It does not own quest completion. A quest episode may use the result as an eligibility, failure/transformation or aftermath input under `canon/questline-taxonomy-v2.md`.

Mechanics boundary

No AutoPTU family is required for the reduced interaction. It uses semantic time, private knowledge, information delivery and durable world-agent state.

If an accepted replacement later becomes a structured encounter, dependencies must be admitted individually:

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

Live engine evidence checked for this pass

AutoPTU-Java `main` remains at `f859888213385e313df923678b62374ac6919b22` (PR #449). That evidence freezes the side-effect order of one Quick Switch path. It does not verify complete action economy, generic reactions/interrupts or the Trainer Features family.

AutoPTU Python `main` remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head is explicitly presentation-only and does not alter battle rules or outcomes.

Next seam

A private `ACCEPT_REPLACEMENT_TERMS` outcome still does not establish a replacement commitment. The answer must first travel back to the responder. Only after receipt should a separate owner be allowed to create a new negotiated commitment with lineage to both commitments/proposals while preserving the original promise for accountability and history.
