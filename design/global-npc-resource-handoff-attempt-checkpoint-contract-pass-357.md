# Global NPC resource handoff attempt checkpoint contract — Pass 357

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-08

Purpose

Persist Pass 344 failed handoff attempts across restart without replaying the attempt, deleting the parent authorization or fabricating custody transfer.

Target chain

request -> authorization -> failed attempt -> checkpoint -> restore -> later retry/replan OR later successful transfer

Core boundaries

`ATTEMPT_RESTORED != ATTEMPT_REEXECUTED`

`FAILED_ATTEMPT != TRANSFER`

`FAILED_ATTEMPT != AUTHORIZATION_DELETED`

`ABSENCE != REFUSAL`

`EARLIER_FAILURE + LATER_SUCCESS` may both remain true.

`TERMINAL_REFUSAL + LATER_TRANSFER_UNDER_SAME_AUTHORIZATION` is rejected as inconsistent history.

Executable primitive

`tools/global_npc_resource_attempt_checkpoint.py` introduces `OUROS_NPC_RESOURCE_CHECKPOINT_V3` as a narrow wrapper over the existing V2 resource checkpoint. It serializes the Pass 344 attempt ledger with stable attempt ID, authorization ID, actor, location, semantic time, outcome and optional observation provenance.

Restore validation

Each attempt must reference an existing Pass 343 authorization. Location, valid window and participant identity must match that authorization. Provider and recipient refusal retain role-specific attribution.

An earlier ordinary failure may coexist with a later successful transfer. An attempt occurring after the completed transfer fails closed. A terminal refusal followed by transfer under the same authorization also fails closed because Pass 344 defines refusal as terminal.

Time boundary

Future authorization windows remain legal. Completed handoff attempts are historical observations, so `validate_attempt_checkpoint_time()` rejects any attempt whose semantic tick is later than the restored world time.

Backward compatibility

V1 and V2 resource checkpoints restore with an explicitly empty `ResourceHandoffAttemptLedger`. The loader does not infer a failed attempt from memory, travel, communication, resource position or later custody.

No owner duplication

Pass 357 does not alter `record_handoff_attempt()`, authorization-state derivation, replanning policy, resource custody or request ownership. The checkpoint stores and validates facts owned by Pass 344.

Narrative use

A field worker can remember that a pickup failed before a restart, then retry later. Another investigator can distinguish an earlier no-show from a later successful handoff instead of seeing only the final holder. An old save that never stored failed attempts remains historically incomplete rather than retroactively repaired by inference.

Reduced version

No AutoPTU dependency. Semantic time, resource request, handoff authorization, Pass 344 attempt provenance, checkpoint persistence, communication, travel and replanning are sufficient.

Rich version capability dependencies

Targeting / footprints / range / LoS: required only for exact tactical perception/selection around a blocked pickup or carrier.

Base movement legality: required for ordinary tactical approach and repositioning.

Complete movement including push/pull/knockback/interception/forced movement: required for physical interception, rescue, carrier displacement or forced access denial.

Core calculations: required for deterministic PTU arithmetic if battle occurs.

Action economy / initiative: required for explicit tactical pickup/drop/handoff/guard interactions.

Full turn / round lifecycle: required for round-bound pickup windows, delayed arrivals or staged objective changes.

Full stateful damage pipeline: required if actors or carried equipment can take authoritative battle damage.

Status lifecycle: required for persistent conditions that affect the scene.

Terrain / weather / hazards / zones / reactions: required by each exact environmental or reactive mechanic used.

Move-specific behavior: each exact Move remains individually gated.

Abilities: each exact Ability remains individually gated.

Items: each exact Item effect remains individually gated.

Trainer Features/perks: each exact Feature remains individually gated.

AI legal-action infrastructure: required for any new pickup, cargo, handoff or objective interaction action.

AI tactical policy: required for delivery-first, protect-carrier, retry, retreat, interception and disengage-after-objective choices.

Minecraft/Cobblemon/Craftics adapter/playback: presentation only; client proximity or animation cannot manufacture an attempt or transfer.

Live engine evidence

AutoPTU-Java head inspected read-only: `93d90167ae73191e38916c6a64914c66fd3c3e84`, merge PR #406. It strengthens Intimidate parity for four target-owned prevention Abilities but leaves spatial prevention, reflection and post-apply reactions open.

AutoPTU Python head inspected read-only: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its current head remains presentation-only.

Acceptance cases

V3 round-trip preserves failed attempts exactly. V2 restore creates no attempt history. Unknown authorizations fail closed. Location/window/participant mismatches fail closed. Refusal attribution survives restart. Ordinary failure may precede a later successful transfer. Attempts after transfer fail closed. Terminal refusal plus later transfer fails closed. Duplicate IDs fail closed. Future attempts fail closed. Snapshot ordering is deterministic.

Deferred work

World checkpoint integration remains separate so V7 is not changed in the same slice. Pass 345–352 still require their own codecs and cross-ledger validation. Travel-derived arrival evidence, trust consequences, cargo inventory binding and Minecraft acknowledgement remain separate owners.
