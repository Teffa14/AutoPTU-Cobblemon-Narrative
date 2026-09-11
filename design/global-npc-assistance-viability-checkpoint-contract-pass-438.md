# Global NPC Assistance Viability Checkpoint Contract — Pass 438

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

## Purpose

Pass 437 established an append-only owner for pre-start viability observations on negotiated assistance commitments. Those observations could persist locally, but `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V3` did not include them in the same logical generation as the accepted proposal, negotiated commitment, world state and replan queue.

Pass 438 advances the assistance checkpoint to `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V4`.

V4 makes one restart boundary cover the accepted obligation and the later evidence about whether that obligation is currently viable.

## V4 generation

The checkpoint now carries:

- the world checkpoint and semantic minute;
- durable world-action intents;
- ordinary assistance commitments;
- assistance deferrals;
- structured counterproposals;
- negotiated counterproposal commitments;
- pre-start commitment viability observations;
- the ordinary replan queue that carries viability wake-ups.

The outer SHA-256 digest still protects the complete logical generation.

## Causal validation

Every restored viability observation must resolve to an existing negotiated commitment in the same checkpoint generation.

The observation must preserve the negotiated commitment's:

- `commitment_id`;
- `proposal_id`;
- requester;
- responder.

The responder remains the viability observer/owner. A requester or unrelated NPC cannot be introduced by snapshot mutation as the authority over another actor's execution viability.

The observation minute must remain before the negotiated start and no later than the checkpoint semantic minute.

## Wake-up coherence

Every viability observation was created together with an ordinary `EXTERNAL_EVENT` replan trigger. V4 therefore requires the corresponding trigger identity to exist in the restored replan queue as either pending or completed.

A pending trigger must preserve:

- the responder as the affected agent;
- `EXTERNAL_EVENT` as the reason;
- the observation minute as due time;
- the observation ID as source provenance.

A checkpoint cannot preserve the blocker while silently dropping the wake-up, nor preserve a wake-up that has been rebound to another actor.

## History coherence

Viability history remains append-only.

A restored `RESTORED` observation requires a preceding `AT_RISK` or `BLOCKED` observation for the same commitment inside the restored ledger. Restart cannot fabricate a cleared state without the earlier constraint history.

The accepted proposal and commitment stay unchanged. A blocker does not rewrite the promised window, location metadata, scope metadata, alternative metadata or decision provenance.

## Backward compatibility

V4 restores V1, V2 and V3 assistance checkpoints.

Older generations did not own viability observations, so their restored viability ledger is empty. The upgrader does not infer blockers by rereading messages, route state or other world evidence.

Absence of a viability ledger in a legacy checkpoint therefore means only that the older schema did not persist this owner.

## Authority boundary

This checkpoint validates and restores causal state. It does not decide what the blocker means operationally.

It must not:

- reserve or reroute travel;
- grant or revoke access;
- allocate or consume resources;
- cancel or reschedule the agreement;
- notify another actor without an information event;
- complete assistance work;
- apply battle effects;
- invoke AutoPTU.

Route, access, resource and tactical owners remain separate authorities.

## Mechanical capability posture

Checkpoint persistence itself requires none of the battle capability families.

A later field scene created by replanning must independently classify targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

No capability family is promoted by this persistence change.

## Verification

`tests/test_global_npc_assistance_world_checkpoint_v4.py` covers atomic restoration of viability plus its negotiated commitment, replan-trigger preservation, rejection of missing commitment bindings, rejection of a missing wake-up, fail-closed actor rebinding after valid redigest, V3 backward compatibility and a source guard against tactical or route/resource execution entering the checkpoint owner.
