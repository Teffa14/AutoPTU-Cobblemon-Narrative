# Global NPC assistance deferral checkpoint contract — Pass 431

Status: IMPLEMENTED / NON-CANON ARCHITECTURE
Date: 2026-09-11

## Scope

This pass closes the persistence seam left by Pass 430. Assistance deferrals now participate in the same logical checkpoint generation as world state, world-action intents and accepted assistance commitments.

The checkpoint preserves causality and wake identity. It does not choose a new assistance response, consume an expired window, create a commitment, reserve travel/resources, resolve a quest or execute AutoPTU mechanics.

## Schema

Current outer schema: `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V2`.

The generation contains:

- the existing global `OUROS_NPC_WORLD_CHECKPOINT_V5` snapshot;
- `OUROS_WORLD_ACTION_INTENT_LEDGER_V1`;
- `OUROS_ASSISTANCE_COMMITMENT_LEDGER_V1`;
- `OUROS_ASSISTANCE_DEFERRAL_LEDGER_V1`;
- one outer SHA-256 digest covering the full logical generation.

Legacy `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V1` snapshots remain readable and restore an empty deferral ledger because V1 never stored that family.

## Deferral coherence requirements

Every stored deferral must still reference an existing assistance request and an existing `DEFER_ASSISTANCE_REQUEST` response.

Requester/responder bindings must match both durable world-action records.

The provenance root must remain the DEFER response action ID.

The response may not come from a semantic minute later than the checkpoint.

The reconsideration minute must remain later than the response. Optional expiry may not precede reconsideration.

The durable trigger ID must remain `replan:assistance-deferral:<deferral_id>`.

The world checkpoint's replan queue must know that trigger. The trigger must be either still pending or already completed. A deferral record with no corresponding queue history fails closed.

If the trigger is pending, its responder, reason, due minute, source action and priority must exactly match the deferral record.

## Restore behavior

A pending future reconsideration remains pending after restart. Processing before its due minute yields no wake. Processing at or after its due minute follows the ordinary replan queue and can wake only the named responder.

If the wake was already completed before the checkpoint, restore preserves the completed trigger identity and does not replay it.

Deferral history is restored directly from its durable ledger. It is not reconstructed from communication logs, planner output or inferred from an absent commitment.

## Failure behavior

The outer digest rejects mixed-generation mutation.

A validly re-digested payload still fails if deferral/action bindings, provenance or pending trigger fields disagree.

Unknown assistance checkpoint schemas fail closed.

## Expiry boundary

Pass 431 preserves optional expiry but does not assign executable late-processing behavior to it. If a runtime resumes after expiry while a due wake remains unprocessed, a later owner must decide the reviewed transition. Persistence must make enough state available for that decision without fabricating an outcome.

## PTU and adapter boundary

Checkpointing a deferral exercises no battle capability. It grants no permission to infer support for targeting, movement, damage, statuses, terrain/weather/hazards/reactions, Moves, Abilities, Items or Trainer Features.

A later tactical response must pass the existing explicit `REQUEST_AUTOPTU` boundary and capability admission checks. Minecraft/Cobblemon/Craftics remains presentation/playback and may not rewrite the restored world-agent decision history.

## Canon boundary

This is region-neutral world-agent architecture. It introduces no canon facts, locations, NPC obligations, factions, quests or outcomes.
