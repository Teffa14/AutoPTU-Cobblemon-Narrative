# Engine readiness snapshot — Pass 238

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03
Pass: 238

## Read-only repositories inspected

AutoPTU-Java `main`:
- `2ca8552c640c582c98e7a2cc4667a29426b8173a`
- commit message: `Wire forced movement into shared landing consequences (#336)`

AutoPTU `main`:
- `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- latest change remains presentation-only viewport coordinate synchronization.

## New AutoPTU-Java evidence

The Java commit adds/wires a shared runtime movement-landing application and routes forced movement through shared landing consequences. It also adds tests/parity work around stateful landing consequence order and trap landing integration.

This is meaningful evidence for a specific forced-movement -> landing-consequence seam.

It does not prove the complete movement family. In particular this snapshot does not infer complete support for every push, pull, knockback, interception, partial stop, collision, forced relocation, movement-trigger reaction or multi-actor lifecycle merely because one shared landing path is now wired.

## Permanent capability categories

| Capability family | Pass 238 status | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Keep prior audited status. |
| base movement legality | VERIFIED | Keep prior audited status. |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | Improved by `2ca8552c...` forced-movement landing wiring; family not complete. |
| core calculations | VERIFIED | Keep prior audited status. |
| action economy / initiative | VERIFIED | Keep prior audited status. |
| full turn / round lifecycle | PARTIAL | No new evidence promotes family. |
| full stateful damage pipeline | PARTIAL | No new evidence promotes family. |
| status lifecycle | PARTIAL | Landing consequences can apply through shared status boundaries, but full lifecycle remains broader. |
| terrain / weather / hazards / zones / reactions | MIXED / PARTIAL / BLOCKING | Trap/landing slice exists; broad family remains incomplete. |
| move-specific behavior | PARTIAL | No family-wide proof. |
| abilities | PARTIAL | No family-wide proof. |
| items | PARTIAL | No family-wide proof. |
| Trainer Features / perks | PARTIAL | No family-wide proof. |
| AI legal-action infrastructure | VERIFIED | Keep prior audited status. |
| AI tactical policy | BLOCKING | No evidence of complete ecology-aware tactical policy. |
| Minecraft / Cobblemon / Craftics adapter / playback | PARTIAL / BLOCKING | No end-to-end proof for demographic projection/reconciliation. |

## Pass 238 dependency interpretation

The population/demography resolver itself is an Ouros world-state system and does not need AutoPTU for births, stage transitions, immigration, emigration, ecological mortality ledger entries, local extirpation or recolonization bookkeeping.

A conventional battle can be attached only after explicit population-member selection/lease and normal AutoPTU handoff.

A richer encounter that physically escorts a dispersal group through hazards or hostile interception depends on the exact rich families it uses:
- complete movement;
- full turn/round lifecycle for timed traversal;
- terrain/weather/hazards/zones/reactions if route hazards are mechanical;
- move-specific behavior, abilities, items and Trainer Features only when selected content requires them;
- AI tactical policy for retreat/escort/corridor priorities;
- Minecraft/Cobblemon/Craftics adapter/playback for authoritative visible synchronization.

## Conservative rule

`REPRESENTATIVE_FORCED_MOVEMENT_LANDING_SLICE != COMPLETE_MOVEMENT_FAMILY`

No Pass 238 encounter should be upgraded to its rich version until current tests/contracts verify every exact capability family it consumes.

## Engine questions still open for ecology

1. What semantic post-battle result contract will distinguish KO from capture/removal, retreat, local emigration and return-to-population?
2. Can a persistent population member be leased into battle and returned idempotently without duplicate world actors?
3. Which movement/reaction tests are still required before corridor escort/interception can be treated as complete movement?
4. What server-authoritative adapter contract will bind a population member to a Cobblemon presentation actor across chunk unload/reload?
5. How will ecological world-state consequences be serialized independently from tactical battle snapshots?
