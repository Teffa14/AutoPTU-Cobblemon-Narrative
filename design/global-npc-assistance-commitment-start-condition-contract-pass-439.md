# Global NPC Assistance Commitment Start Condition Contract — Pass 439

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

## Purpose

Passes 437–438 made pre-start assistance viability durable and restart-safe. They intentionally stopped before deciding what happens when the accepted start minute arrives while a risk or blocker is still active.

Pass 439 adds a narrow factual seam for that moment.

`OUROS_ASSISTANCE_COMMITMENT_START_LEDGER_V1` can arm one semantic-time watch for a negotiated commitment and record whether the latest pre-start viability evidence is still `AT_RISK` or `BLOCKED` at the exact accepted start minute.

The result is evidence for later policy. It is not itself renegotiation, abandonment, cancellation, breach adjudication, travel or task execution.

## Durable watch

A start watch binds:

- one negotiated `commitment_id`;
- its `proposal_id`;
- requester and responder;
- the accepted `start_minute`;
- the minute the watch was armed;
- provenance;
- one deterministic `SCHEDULE_DUE` replan trigger.

The watch must be armed before the accepted start. It wakes only the responder that owns the commitment.

The wake does not imply that the work is feasible or that the responder begins it. It only ensures the existing planner has an event-driven opportunity to reconsider current state when the promised window actually opens.

## Start assessment

At the exact accepted start minute, the assessor reads the latest pre-start record from `OUROS_ASSISTANCE_COMMITMENT_VIABILITY_LEDGER_V1`.

If there is no viability record, or the latest record is `RESTORED`, no adverse start assessment is created.

If the latest record remains `AT_RISK`, the durable factual condition becomes `AT_RISK_AT_START`.

If the latest record remains `BLOCKED`, the durable factual condition becomes `BLOCKED_AT_START`.

The assessment copies the exact source observation identity, constraint kind, constraint reference, evidence reference and provenance root. It does not reinterpret the blocker.

## Agreement preservation

The accepted negotiated commitment remains unchanged.

A `BLOCKED_AT_START` assessment does not:

- erase the promise;
- change start/end time;
- change location, scope or alternative metadata;
- remove the commitment from the responder agenda;
- mark the requester as notified;
- mark the obligation as excused;
- declare fault;
- create a replacement appointment.

Those are separate causal facts or later policy decisions.

## Policy boundary

Pass 439 deliberately does not choose between:

- attempted fulfillment despite risk;
- waiting for a blocker to clear;
- communicating the problem;
- proposing new terms;
- explicit abandonment;
- a documented missed obligation;
- another world-level response.

The global planner must choose among admissible actions using current knowledge, permissions, schedule pressure, risk and other obligations. If another actor must learn about the problem, that information still travels through the ordinary communication system.

## Authority boundary

This owner must not:

- reserve or reroute travel;
- grant/revoke access;
- allocate or consume resources;
- mutate the accepted agenda record;
- execute an interaction objective;
- apply PTU battle effects;
- invoke AutoPTU.

The world can therefore remember both facts at once: the actor promised a window, and the window opened while the job was still blocked.

## Mechanical capability posture

The watch and assessment require no battle capability family.

A later scene may independently require targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

No capability family is promoted by this pass.

## Verification

`tests/test_global_npc_assistance_commitment_start.py` covers responder-only start wake-up, exact semantic-time assessment, distinct `AT_RISK_AT_START` and `BLOCKED_AT_START` states, restored/no-blocker behavior, agreement preservation, idempotent watch replay, conflicting identity rejection, snapshot/restore and a source guard against policy or tactical execution entering this owner.
