# Global NPC world/resource checkpoint integration contract — Pass 354

Status: IMPLEMENTED FOUNDATION
Canon authority: NONE

## Purpose

Pass 354 inserts the Pass 353 resource checkpoint payload into the same logical recovery unit as global NPC state.

The integration entrypoint is `tools/global_npc_world_resource_checkpoint.py`.

Its serialized schema is `OUROS_NPC_WORLD_CHECKPOINT_V6`.

## V6 ownership boundary

The world checkpoint remains owner of global NPC state, communication, knowledge, replanning and the registries already present in V5.

The Pass 353 resource codec remains owner of serialization for:

- Pass 339 `ReservationLedger`;
- Pass 342 `ResourceRequestLedger`.

Pass 354 composes those two owners. It does not reinterpret their records and does not replay their operations.

## Build behavior

`build_world_resource_checkpoint` first asks the existing V5 world checkpoint owner to build its canonical payload. The adapter then advances the outer schema to V6, attaches `resource_state`, and computes one digest over the combined payload.

The resulting digest therefore covers both world-agent state and resource history.

A caller cannot alter a persisted reservation or request without invalidating the global checkpoint digest.

## Restore behavior

V6 restore validates the global digest before reconstructing resource ledgers.

The nested resource payload must pass the Pass 353 schema and provenance checks.

Request creation and request-event times are then checked against the same `semantic_minute` stored by the world checkpoint.

The existing V5 restore path validates the world-agent portion after the V6-only resource field is removed and the base schema is reconstructed for the current owner.

## Backward compatibility

V1–V5 world checkpoints remain valid inputs through the existing world checkpoint restore path.

Because those schemas never serialized Pass 339/342 resource history, compatibility restore returns empty `ReservationLedger` and `ResourceRequestLedger` values.

The adapter must not infer old resource history from NPC memory, dialogue, current inventory, purpose references or later events.

`MISSING_HISTORY != EMPTY_WORLD_FACT`

The empty legacy ledger means only that the checkpoint cannot prove older resource records.

## Temporal invariants

Future reservations are allowed because reservations can describe future booking windows.

A resource request whose creation time is after the world checkpoint time is invalid.

A request transition whose event time is after the world checkpoint time is invalid.

This preserves Pass 353 semantics and prevents one component from restoring from a later causal moment than the world around it.

## Replay invariants

Restore reconstructs records.

Restore cannot:

- create a new reservation;
- submit a new request;
- accept, decline or cancel a request;
- move a resource;
- create a handoff;
- deliver a communication;
- wake an NPC because a business operation was replayed;
- create AutoPTU state;
- create or mutate a Minecraft entity as authority.

## Scope limitation

V6 currently includes only the resource owners frozen by Pass 353.

Passes 343–352 remain outside this resource bundle:

- handoff authorizations;
- failed handoff attempts;
- appointment notices;
- reschedule proposals/decisions;
- reschedule admission;
- allocation resolution;
- allocation application/displacement;
- allocation notice obligations and links;
- terminal communication provenance beyond what the existing world checkpoint already owns.

Those owners must be integrated incrementally with type-specific validation.

## Test surface

`tests/test_global_npc_world_resource_checkpoint.py` covers:

- V6 world/resource round-trip;
- V5 compatibility with non-invented empty resource ledgers;
- global-digest coverage of resource mutations;
- future request-event rejection after a correctly re-digested payload;
- unknown nested resource schema rejection;
- missing V6 resource payload rejection.

## Architectural consequence

For the first time, an Ouros save can prove from one logical checkpoint that an NPC world state and a reservation/request history coexisted at the same semantic time.

That is narrower than full resource durability, but it closes the first actual atomicity gap instead of maintaining two independently restorable clocks.
