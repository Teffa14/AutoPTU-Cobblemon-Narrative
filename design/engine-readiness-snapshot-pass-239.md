# Engine readiness snapshot — Pass 239

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03
Pass: 239

## Read-only repositories inspected

AutoPTU-Java `main`:
- `2ca8552c640c582c98e7a2cc4667a29426b8173a`
- latest evidence remains forced movement wired into shared landing consequences.

AutoPTU `main`:
- `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- latest change remains presentation-only viewport coordinate synchronization.

## Pass 239 interpretation

Persistent-member/spawn reconciliation is primarily an Ouros world-state + Minecraft/Cobblemon adapter concern.

The core lease lifecycle does not require PTU battle mechanics:

```text
canonical source slot
-> reserve lease
-> materialize visible actor
-> suspend/release/rematerialize
```

AutoPTU becomes relevant only after an explicit structured encounter handoff.

## Permanent capability categories

| Capability family | Pass 239 status | Interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Prior audited status retained. |
| base movement legality | VERIFIED | Prior audited status retained. |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | `2ca8552c...` improves forced-movement landing integration but does not prove the whole family. |
| core calculations | VERIFIED | Prior audited status retained. |
| action economy / initiative | VERIFIED | Prior audited status retained. |
| full turn / round lifecycle | PARTIAL | No new family-wide evidence. |
| full stateful damage pipeline | PARTIAL | No new family-wide evidence. |
| status lifecycle | PARTIAL | No new family-wide evidence. |
| terrain / weather / hazards / zones / reactions | MIXED / PARTIAL / BLOCKING | Verified slices exist; broad family remains incomplete. |
| move-specific behavior | PARTIAL | Representative Moves do not prove complete behavior. |
| abilities | PARTIAL | Representative Abilities do not prove family completeness. |
| items | PARTIAL | Representative Items do not prove family completeness. |
| Trainer Features / perks | PARTIAL | Representative Features do not prove family completeness. |
| AI legal-action infrastructure | VERIFIED | Prior audited status retained. |
| AI tactical policy | BLOCKING | No evidence of complete ecology-aware tactical policy. |
| Minecraft / Cobblemon / Craftics adapter / playback | PARTIAL / BLOCKING | Pass 239 directly exposes the missing persistent lease/reconciliation path. |

## New external technical evidence relevant to adapter status

Cobblemon's public changelog indicates that wild Pokémon can be saved to the world while still despawning over time. Current public issue reports also show discard/despawn edge cases. This reinforces the existing Ouros boundary: entity persistence cannot serve as canonical member persistence.

This evidence does not downgrade Cobblemon as a presentation platform. It identifies why the adapter needs an explicit lease/index layer above native entity lifecycle.

## Reduced implementation dependency

A safe first version requires:

- persistent Ouros member/population store;
- unresolved pool slot accounting from Pass 238;
- atomic presentation lease reservation;
- one-source/one-active-actor uniqueness;
- entity UUID correlation and repair;
- chunk unload/despawn/restart release/suspension handling;
- create-only battle blueprint handoff;
- idempotent semantic post-battle reconciliation.

This remains `Minecraft/Cobblemon/Craftics adapter/playback = PARTIAL/BLOCKING` until tested end-to-end.

## Structured battle dependency

A conventional encounter after lease lock can consume the verified families plus exact selected content support.

A rich ecology encounter still requires every family it invokes. Examples:

- physical interception/escort: complete movement;
- timed objectives: full turn/round lifecycle;
- weather/hazard corridors: terrain/weather/hazards/zones/reactions;
- retreat/guard priorities: AI tactical policy;
- synchronized visible return/removal: adapter/playback.

## Pass 239 blocking acceptance questions

1. Can the server atomically reserve a canonical source before Cobblemon materialization?
2. Can native spawn opportunities be intercepted or safely reconciled without allowing an unleased actor into authoritative combat?
3. Can a persistent member rematerialize with a new entity UUID after unload while retaining its Ouros identity?
4. Can an ENGAGED lease block all duplicate materialization until semantic battle resolution?
5. Can capture confirmation emit exactly one `CAPTURE_REMOVAL` event and remain idempotent across retry/restart?
6. Can stale entity correlations be repaired without deleting population/member state?
7. Can unresolved pool slot tokens survive restart without leaking or double-leasing capacity?

## Conservative rule

```text
COBBLEMON_ENTITY_PERSISTENCE != OUROS_MEMBER_PERSISTENCE
ENTITY_UUID != CANONICAL_MEMBER_ID
REPRESENTATIVE_FORCED_MOVEMENT_SLICE != COMPLETE_MOVEMENT_FAMILY
```

No capability family is promoted on Pass 239.