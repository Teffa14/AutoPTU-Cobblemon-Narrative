# Global NPC AI readiness snapshot — Pass 428

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT
Date: 2026-09-11

Repository baseline

Pass 428 starts from Narrative `main` `f20fe3f9215a9e648809ccb7d6559406b8506d90`, after Pass 427.

The recursive tree was inventoried before writing. `CURRENT_FOCUS.md`, all canon paths in the tree, the global goal/need/schedule contract and executable scheduler, the Pass 422–427 assistance chain, world-action intent persistence, world-event coordination, coherent checkpoint surfaces, recent research/proposals and PTU/Kairos boundaries were checked. No canon file is changed.

Implemented seam

`tools/global_npc_assistance_acceptance_commitment.py` turns one terminally delivered `ACCEPT_ASSISTANCE_REQUEST` into one explicit `ScheduledCommitment` owned by the responder.

The helper preserves the response action as provenance, validates request/response/envelope/claim binding, refuses retroactive time reservation and adds the commitment to the responder's existing global agenda. It does not move an NPC, allocate a route/resource, complete assistance or call AutoPTU.

`OUROS_ASSISTANCE_COMMITMENT_LEDGER_V1` gives the causal commitment record deterministic local snapshot/restore and exact-replay idempotency. Coherent world-checkpoint integration remains pending.

Regression

`tests/test_global_npc_assistance_acceptance_commitment.py` covers successful materialization, ordinary agenda selection, no location mutation, structured-mechanics handoff, non-ACCEPT/non-delivered rejection, invalid windows, replay, conflict, local snapshot durability and provenance tampering.

Research and proposal

New research anchors are `I Was a Teenage Exocolonist` for finite-calendar opportunity cost, public `Pathologic 2` community observations for expiring objective windows, and a PTU exploration discussion for keeping travel/field activity separate from a simple agreement to help.

The non-canon proposal `The Yes Occupies Real Time` makes an accepted request consume an explicit future agenda window without implying travel or completion.

Live engine evidence

AutoPTU-Java `main` was inspected read-only at `0415392b3391aed7329a062da159c882e0e2d43e`, merged PR #444, `Harden replacement initiative caller policy contract`. This strengthens one caller-policy seam around replacement initiative only. Action economy/initiative remains PARTIAL as a family.

AutoPTU Python `main` was inspected read-only at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head remains explicitly presentation-only and does not alter battle rules or outcomes.

Neither engine repository is modified.

Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited scopes.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: VERIFIED only for audited ordinary actions; specialized rescue/escort/protect/retrieve/carry/interact/brace/extract actions need explicit admission.
AI tactical policy: BLOCKING for specialized objective-aware policies.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative specialized objective state, specialized non-KO completion and in-flight recovery.

Reduced narrative availability

The new pattern is fully usable at world level with private knowledge, communication, semantic time, durable actions and schedules. No tactical capability is required merely to make an accepted assistance request occupy time.

Mechanically rich version

If the scheduled work later becomes escort, rescue, retrieval, protection or extraction, exact capability gates remain in force. Forced displacement depends on complete movement. Exact arrival/turn timing depends on action economy/initiative and possibly full turn/round lifecycle. Persistent damage/status consequences depend on their respective pipelines. Hazard or reaction phases depend on terrain/weather/hazards/zones/reactions. Specialized objective choices depend on explicit AI legal-action and tactical-policy support.

Open boundaries

`OUROS_ASSISTANCE_COMMITMENT_LEDGER_V1` and `OUROS_WORLD_ACTION_INTENT_LEDGER_V1` are still outside the coherent persistent-world checkpoint generation. DEFER still needs a future-condition/window contract. COUNTERPROPOSE still needs structured proposal payload. Route reservation, resource reservation, actual travel and AutoPTU resolution remain separate. AutoPTU `UNKNOWN`, `EXPLICITLY_ABANDONED`, persistent Injury and persistent Status remain unresolved outside this slice.
