# Ecology event replay contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Pass: 245
Canon effect: NONE

## Purpose

Define the minimum deterministic reducer boundary needed to reconstruct Ouros ecology state from ordered semantic events without duplicating PTU mechanics or trusting Minecraft entity state.

## Authority

Ouros owns ecological identity, population truth, persistent encounter memory, observation/knowledge state and ecology-event state.

AutoPTU owns structured PTU adjudication. Ouros may consume only stable semantic result events from AutoPTU. Ouros does not replay attacks, damage formulas, statuses, forced movement, reactions, Abilities or other tactical mechanics to reproduce a battle.

Minecraft/Cobblemon/Craftics owns presentation and realtime interaction. Entity UUID, animation, despawn, vanilla damage and chunk lifecycle are not canonical ecological events by themselves.

## Reducer rule

Given the same initial state and the same ordered accepted event sequence, Ouros must produce the same canonical ecology snapshot.

```text
initial ecology snapshot
+ ordered accepted domain events
= deterministic ecology snapshot
```

The reducer must be a pure semantic state transition layer with respect to PTU. It may validate authority and event order, but it may not call a tactical rules implementation to infer missing outcomes.

## Event classes in the first replay slice

Presentation lifecycle:
- `LEASE_RESERVE`
- `LEASE_MATERIALIZE`
- `LEASE_REMATERIALIZE`
- `LEASE_SUSPEND`
- `LEASE_INDEX_RECONCILE`
- `SERVER_RESTART`

Observation and overworld:
- `OBSERVATION_RECORDED`
- `OVERWORLD_INTERACTION`

Ecology:
- `ECOLOGY_EVENT_EVALUATION`
- `ECOLOGY_EVENT_REEVALUATION`
- `ECOLOGY_PRESSURE_DELTA`
- `ENCOUNTER_HISTORY_APPEND`

Structured encounter seam:
- `BATTLE_MANIFEST_FREEZE`
- `STRUCTURED_BATTLE_HANDOFF`
- `AUTOPTU_SEMANTIC_RESULT`

These names are fixture vocabulary. Production schema/versioning remains unresolved.

## Required ordering constraints

- a projection lease must exist before materialization;
- one persistent actor cannot have two active leases;
- a battle manifest must freeze before structured handoff;
- one active battle must receive a result for the same battle ID and persistent actor;
- semantic result processing must complete before post-battle ecological writeback that depends on it;
- server restart may invalidate transient entity correlation but may not delete persistent identity or ecological history.

## Snapshot ownership

Canonical replay snapshot fields may include:
- persistent actor identity;
- population membership and abundance information authorized by population events;
- persistent encounter-history counters/references;
- ecological pressure values;
- ecology-event state;
- projection lease ownership/state;
- currently valid presentation correlation when available.

The following are not authored by this reducer:
- PTU HP calculation;
- status application/removal;
- attack legality;
- targeting or range;
- initiative;
- forced movement;
- Ability resolution;
- Item resolution;
- Trainer Feature resolution;
- tactical AI decisions.

## Crash/restart rule

Transient presentation correlation may be discarded and rebuilt. Persistent identity and accepted ecology events survive.

For the Pass 245 trace, restart clears the Minecraft entity UUID and leaves the lease `SUSPENDED` for reconciliation. This is proposed implementation behaviour, not a global persistence-storage decision.

## Replay and correction

The first acceptance gate is forward replay only. Retroactive insertion, deletion or reordering of production events is not authorized by this contract.

Any future correction system must preserve:
- original provenance;
- auditability;
- deterministic rebuilt state;
- explicit migration/version handling;
- separation between corrected ecology truth and player-visible knowledge.

## Battle dependency classification

The replay reducer itself:
- targeting/footprints/range/LoS: NOT REQUIRED for ecology replay;
- base movement legality: NOT REQUIRED;
- complete movement: NOT REQUIRED;
- core calculations: NOT REQUIRED;
- action economy/initiative: NOT REQUIRED;
- full turn/round lifecycle: NOT REQUIRED;
- full stateful damage pipeline: NOT REQUIRED;
- status lifecycle: NOT REQUIRED;
- terrain/weather/hazards/zones/reactions: NOT REQUIRED unless the semantic result vocabulary later carries an already-resolved ecological consequence;
- move-specific behavior: NOT REQUIRED;
- abilities: NOT REQUIRED;
- items: NOT REQUIRED;
- Trainer Features/perks: NOT REQUIRED;
- AI legal-action infrastructure: NOT REQUIRED;
- AI tactical policy: NOT REQUIRED;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for production event capture and rematerialization, but not for deterministic offline replay.

Any full encounter that produces the semantic result still depends on its exact AutoPTU capability families. The reducer does not change their readiness.

## Full and reduced encounter versions

Full version: a wild actor can move, warn, flee, be intercepted, interact with terrain/hazards and enter a tactical encounter whose stable semantic results return to Ouros. This remains dependent on complete movement, lifecycle, relevant hazards/reactions, tactical policy and adapter/playback support as required by the encounter.

Reduced version: the encounter uses only an already-supported structured handoff and narrow semantic result such as `TACTICAL_KO_CONFIRMED`. Ecological state changes afterward are resolved by Ouros from that semantic result and existing world state.

## Acceptance

Pass 245 is successful when CI proves all of the following:
- the Pass 244 trace validates;
- the trace replays to the frozen Pass 245 snapshot;
- two replays produce identical per-window and final snapshots;
- wrong battle IDs fail;
- duplicate leases fail;
- direct battle resolution of an ecology event fails;
- restart removes transient UUID correlation without losing the persistent actor.
