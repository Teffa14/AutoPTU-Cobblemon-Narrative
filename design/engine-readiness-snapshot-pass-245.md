# Engine readiness snapshot — Pass 245

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03
Purpose: Record the exact read-only engine evidence used by the deterministic ecology replay slice. No broad category is promoted from a representative mechanic.

## AutoPTU-Java live evidence

Repository: `Teffa14/AutoPTU-Java`
Observed main head: `cc247607ffa28969990465945e814ccd4545fa51`
Commit: `Freeze Naturewalk forced-movement trap block (#339)`

New evidence:
- the forced-movement landing test now covers Naturewalk interaction with a tile trap;
- the resolved semantic event can report a reduced `trap_block` result;
- the target moves to the landing tile while the trap remains unconsumed and Slowed is not applied;
- sensitive trap details are reduced in the blocked event payload (`coordinate` null, source/name blank, terrains empty in the tested block case).

Interpretation:
This improves the exact forced-movement + landing trap + Naturewalk contract and its semantic event surface. It does not prove complete forced movement, complete Naturewalk behavior in every path, complete terrain/hazard support, reaction timing, weather, zones or adapter playback. No family is promoted.

## AutoPTU Python oracle

Repository: `Teffa14/AutoPTU`
Observed main head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
Commit: `Career: keep battle coordinates synced after viewport resize (#237)`

Latest head remains presentation-only for this audit. No additional PTU rules capability is inferred.

## Permanent capability categories

| Capability | Pass 245 state | Boundary |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | Prior audited contracts; replay reducer does not execute this family. |
| base movement legality | VERIFIED | Prior audited contracts; reducer does not execute movement. |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | New Naturewalk forced-movement landing block is one tested slice only. |
| core calculations | VERIFIED | Prior audited deterministic arithmetic. |
| action economy/initiative | VERIFIED | Prior audited primitives. |
| full turn/round lifecycle | PARTIAL | No new broad lifecycle evidence. |
| full stateful damage pipeline | PARTIAL | Semantic KO can be consumed by Ouros; that does not prove the full pipeline. |
| status lifecycle | PARTIAL | Trap/status slices exist; full lifecycle remains incomplete. |
| terrain/weather/hazards/zones/reactions | MIXED/PARTIAL/BLOCKING | Naturewalk + trap landing improves one hazard seam only. |
| move-specific behavior | PARTIAL | Representative coverage only. |
| abilities | PARTIAL | Representative support only. |
| items | PARTIAL | Representative support only. |
| Trainer Features/perks | PARTIAL | Representative support only. |
| AI legal-action infrastructure | VERIFIED | Prior audited generation/validation contracts. |
| AI tactical policy | BLOCKING | Full wild tactical choice policy remains unverified. |
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING | Offline reducer now proves deterministic ecology replay, but production capture, suspension, battle playback and rematerialization remain unverified end-to-end. |

## Pass 245 implementation dependency

The new replay reducer deliberately depends on none of the incomplete PTU mechanics. It consumes already-resolved semantic events. Its main implementation dependency is the adapter/persistence boundary that must eventually emit and persist the same accepted event vocabulary.

A full ecological pursuit/escape encounter still depends on the exact families already marked incomplete: complete movement, lifecycle, relevant terrain/hazards/zones/reactions, move/ability/item/Feature behavior as selected, AI tactical policy and adapter/playback.

## New verified narrative-side integration evidence

Pass 245 now has:
- an executable deterministic reducer for the Pass 244 event stream;
- a frozen expected final ecology snapshot;
- tests for deterministic repeated replay;
- negative tests for wrong battle IDs, duplicate projection leases and direct battle resolution of ecology events;
- restart behavior that clears Minecraft UUID correlation while preserving persistent actor identity and lease ownership;
- CI execution of the replay reducer.

## Open mechanical/canon questions

1. Which semantic result event types are stable enough to freeze as a production cross-repo contract?
2. Should HP, Injury, persistent Status Afflictions or other battle-state fields ever persist into Ouros, and which AutoPTU contracts verify them today?
3. What exact event turns overworld flight into a structured tactical pursuit?
4. How will adapter event capture remain idempotent when Minecraft retries, chunks reload or entities are rematerialized?
5. What is the production event-store/versioning strategy?
6. How should late/out-of-order observations be handled without silently rewriting player knowledge or ecology history?
7. When multiple species are added to the end-to-end Marea ecosystem, which interspecies events need atomic population/resource updates?

## Next highest-value gap

Move from one-actor replay to a multi-species/resource integration trace. The next slice should include at least one second approved local species or an already-authorized resource interaction, then prove that one actor's projection/encounter history can change ecological pressure without incorrectly changing another population or resource ledger. This is required before the completion gate of a multi-species Marea ecosystem can be claimed.
