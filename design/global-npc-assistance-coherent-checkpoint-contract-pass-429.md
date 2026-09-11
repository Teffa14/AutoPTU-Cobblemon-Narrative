# Global NPC Assistance Coherent Checkpoint Contract — Pass 429

Status: PROPOSED EXECUTABLE INFRASTRUCTURE

Pass 429 closes the persistence gap left by Pass 428 for the assistance chain.

## Authority boundary

`OUROS_ASSISTANCE_WORLD_CHECKPOINT_V1` is an outer logical checkpoint generation that contains:

- the existing `OUROS_NPC_WORLD_CHECKPOINT_V5` world checkpoint;
- `OUROS_WORLD_ACTION_INTENT_LEDGER_V1`;
- `OUROS_ASSISTANCE_COMMITMENT_LEDGER_V1`;
- one outer semantic minute and digest binding those payloads together.

The wrapper does not replace the existing world checkpoint. It composes it with assistance causal state.

## Generation invariant

A checkpoint build fails closed when:

- a world-action intent comes from after the checkpoint semantic minute;
- an action references an agent absent from the world generation;
- a commitment references a missing request or response action;
- request/responder identities no longer match;
- the commitment provenance root is not the response action;
- the responder agenda does not contain the exact scheduled commitment represented by the commitment ledger.

This prevents a snapshot from claiming that an ACCEPT created a durable obligation while the responder agenda in the same live generation has already lost it.

## Restore invariant

Restore validates the outer digest, restores the existing world checkpoint, restores both assistance ledgers, materializes assistance commitments into the responder agenda, and then reruns the causal-generation validation.

A supplied agenda with the same commitment ID but different schedule content fails closed.

The restored commitment comes from the commitment ledger, not from replaying messages. Communication history therefore remains evidence of how the obligation arose, while the commitment record remains the durable owner of the scheduled window.

## Deliberate limits

Pass 429 does not persist every agenda source in the project. Existing goals, needs and unrelated commitments still belong to their established owners and caller-provided agenda configuration.

Pass 429 does not execute assistance, travel, route reservation, resource allocation, relationship changes or PTU mechanics.

No Minecraft or Cobblemon presentation state becomes authoritative through this checkpoint.

## PTU/Caelo boundary

The checkpoint stores narrative-world causality only. It does not imply support for targeting, movement, initiative, damage, statuses, terrain, weather, reactions, moves, abilities, items or Trainer Features.

A restored commitment marked `requires_structured_mechanics=True` still requires the ordinary AutoPTU handoff when the world planner selects that work.
