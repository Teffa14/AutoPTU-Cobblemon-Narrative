# Global NPC Assistance Start Checkpoint V5 Contract — Pass 441

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

Purpose

Pass 439 made an adverse start factual. Pass 440 made the responder's immediate disposition durable. Those two owners still restored independently from the assistance checkpoint generation.

Pass 441 adds `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V5` as an atomic envelope over the existing V4 assistance checkpoint plus `OUROS_ASSISTANCE_COMMITMENT_START_LEDGER_V1` and `OUROS_ASSISTANCE_COMMITMENT_DISPOSITION_LEDGER_V1`.

Causal guarantees

A restored start watch must still name an existing negotiated commitment, the same proposal, requester, responder and accepted start minute. Its `SCHEDULE_DUE` trigger must still exist in the restored replan queue as pending or completed.

A restored adverse-start assessment must still name its durable watch, negotiated commitment and exact viability observation. Constraint kind, constraint reference, evidence reference and provenance root must equal the preserved viability evidence. The assessment minute must equal the accepted start minute and cannot come from the future relative to the checkpoint.

A restored disposition must still name the exact adverse-start assessment and negotiated commitment. The actor must remain the responder who owns the commitment. Its semantic minute must be within the accepted assistance window and cannot be later than the checkpoint generation.

Backward compatibility

A V4 checkpoint is accepted by the V5 restore API and restores empty start/disposition ledgers because V4 never owned those ledgers. No attempt is made to infer historical watches, assessments or choices from messages or agenda state.

Authority boundary

Checkpoint V5 preserves causal state only. It does not reserve a route, consume an item, grant access, move an NPC, send a renegotiation request, adjudicate fault, record relationship change, execute an objective or invoke AutoPTU.

Battle capability posture

This pass adds no battle mechanic and promotes no permanent capability family. Any later rich encounter remains individually gated for targeting/footprints/range/LoS; base movement legality; complete movement including forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

Verification

`tests/test_global_npc_assistance_world_checkpoint_v5.py` covers atomic restoration, disposition actor tampering after a valid outer redigest, V4 backward compatibility and a source guard against policy/tactical execution entering the checkpoint owner.
