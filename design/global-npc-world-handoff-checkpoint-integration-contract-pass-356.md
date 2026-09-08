# Global NPC world handoff checkpoint integration contract — Pass 356

Status: IMPLEMENTED / NON-CANON INFRASTRUCTURE
Date: 2026-09-08

## Purpose

Pass 355 validated `OUROS_NPC_RESOURCE_CHECKPOINT_V2` for reservations, requests, handoff authorizations and completed custody transfers. Pass 356 makes that V2 resource history part of the coherent world recovery unit.

The new world schema is `OUROS_NPC_WORLD_CHECKPOINT_V7`.

## Ownership boundary

The world-resource checkpoint composes existing owners. It does not become a resource rules engine.

Pass 339 remains owner of reservations. Pass 342 remains owner of requests. Pass 343 remains owner of authorization and custody-transfer semantics. The base world checkpoint remains owner of NPC state, memory, information, replanning and related durable world-agent state.

Restore reconstructs ledgers only. It never executes a handoff, mutates a `WorldResource` holder or sends a communication.

## V7 atomic contents

V7 embeds the validated V2 resource payload inside the same global SHA-256 boundary as the ordinary world checkpoint.

The coherent recovery unit therefore covers:

- semantic world time;
- managed world-agent state and existing durable world subsystems;
- reservations;
- resource requests and transitions;
- handoff authorizations;
- completed custody transfers.

Changing any embedded handoff record without recomputing the global digest is detected as checkpoint tampering.

## Compatibility

`OUROS_NPC_WORLD_CHECKPOINT_V6` remains restorable.

V6 can prove reservations and resource requests because it serialized the V1 resource bundle. It cannot prove Pass 343 handoff history. V6 therefore restores an explicitly empty `ResourceHandoffLedger`.

World-only V1–V5 checkpoints restore all resource ledgers empty because those schemas never serialized resource history.

No compatibility path infers a missing transfer from current possession, memory, location, dialogue or later scheduling records.

## Semantic-time rules

Resource requests and request events cannot originate after the checkpoint semantic minute.

A future authorization window remains legitimate because a pickup can be planned in advance.

A completed custody transfer cannot be dated after the checkpoint semantic minute. Such a record fails closed.

## Cross-ledger rules

V7 delegates Pass 355 cross-ledger validation to `restore_resource_state_with_handoffs()` before exposing restored state.

That validation includes request existence, provider identity, accepted resource identity, authorization timing, transfer-to-authorization identity, single-use authorization and handoff-window validity.

The world checkpoint adds the coherent-time check and global integrity boundary. It does not duplicate those semantics.

## Deterministic restart

Repeated restore of the same V7 checkpoint produces the same resource ledgers. A completed transfer remains one historical transfer. Restart cannot consume the authorization a second time or create another custody event.

## Narrative consequence

A later investigation can recover one coherent snapshot in which NPC knowledge, scheduling state and the physical handoff history all correspond to the same semantic moment.

That permits a distinction between:

- an authorized future pickup;
- an authorization that expired unused;
- a completed transfer;
- a current holder without provable historical transfer in an older save.

The absence of historical evidence remains uncertainty rather than retroactive canon.

## AutoPTU boundary

This pass changes no PTU battle rule.

A rich courier or recovery encounter still depends only on the capability families it actually uses. Tactical reach uses targeting/footprints/range/LoS. Ordinary positioning uses base movement legality. Interception, push/pull/knockback and forced carrier displacement require complete movement. Tactical pickup/drop/handoff actions require action economy and legal-action support. Round deadlines require full turn/round lifecycle. Damage to carrier or cargo requires the full stateful damage pipeline. Persistent conditions require status lifecycle. Terrain, weather, hazards, zones and reactions retain their own gates. Moves, Abilities, Items and Trainer Features/perks remain individually gated. Objective-aware escort or delivery behavior requires AI tactical policy. Minecraft/Cobblemon/Craftics remains a presentation/playback boundary and may not invent missing PTU semantics.

## Deferred durability work

Passes 344–352 remain outside V7. Failed handoff attempts, appointments, reschedules, allocation admission/decision/application and notice provenance require incremental codecs with their own cross-ledger validation before they join the coherent checkpoint.
