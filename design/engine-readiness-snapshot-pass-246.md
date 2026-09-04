# Engine readiness snapshot — Pass 246

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03
Purpose: Record engine evidence used by the shared-resource multi-population integration slice. Representative mechanics never promote a whole category.

## Live read-only engine evidence

AutoPTU-Java main remains `cc247607ffa28969990465945e814ccd4545fa51`, `Freeze Naturewalk forced-movement trap block (#339)`.

The tested slice proves a forced-movement landing can expose a reduced `trap_block` semantic event when Naturewalk blocks the landing trap; the target still reaches the tile, the trap remains, and Slowed is not applied. This is useful semantic-event evidence only. It does not prove complete forced movement, complete Naturewalk, complete terrain/hazards, reactions, zones, weather, or playback.

AutoPTU Python main remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, `Career: keep battle coordinates synced after viewport resize (#237)`. That head is presentation-only for this audit.

## Permanent capability categories

| Capability | Pass 246 state | Boundary |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | Prior audited contracts. |
| base movement legality | VERIFIED | Prior audited contracts. |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | Naturewalk forced-movement trap block is one slice. |
| core calculations | VERIFIED | Prior audited arithmetic. |
| action economy/initiative | VERIFIED | Prior audited primitives. |
| full turn/round lifecycle | PARTIAL | No new broad evidence. |
| full stateful damage pipeline | PARTIAL | No new broad evidence. |
| status lifecycle | PARTIAL | Representative trap/status behavior only. |
| terrain/weather/hazards/zones/reactions | MIXED/PARTIAL/BLOCKING | One landing trap seam does not close the family. |
| move-specific behavior | PARTIAL | Representative coverage only. |
| abilities | PARTIAL | Representative coverage only. |
| items | PARTIAL | Representative coverage only. |
| Trainer Features/perks | PARTIAL | Representative coverage only. |
| AI legal-action infrastructure | VERIFIED | Prior audited generation/validation. |
| AI tactical policy | BLOCKING | Resource-access/withdraw/contest goals are not verified as a complete policy. |
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING | Offline replay works; production event capture and faithful multi-actor projection remain unverified end-to-end. |

## Pass 246 dependency

The new reduced shared-resource replay runs entirely in Ouros ecology state and intentionally requires no PTU tactical family.

The full contested-patch encounter would additionally require complete movement, lifecycle, relevant terrain/zones/reactions, exact selected Move/Ability/Item/Feature behavior, tactical AI and adapter/playback. Damage/status families become required only if the encounter actually escalates into attacks using them.

## New narrative-side evidence

Pass 246 adds deterministic replay across two population ledgers, one persistent actor and one finite resource; a frozen final snapshot; idempotent resource transaction IDs; negative overdraw and duplicate-transaction tests; proof that resource use does not mutate population abundance; proof that actor encounter history does not leak into another population; and restart persistence for the coupled ecology state.

The second population and resource are fixture-only. Passing tests does not approve them as Marea canon.

## Open questions

1. Approve/reject Squawkabilly as Marea's second wild species.
2. Author the actual lower-Sendero shared resource before activating the relation.
3. Decide resource renewal semantics and whether renewal is pulse-, season-, weather-, or management-driven.
4. Define production atomic-group semantics for events that legitimately update both source and destination populations.
5. Define idempotency keys and persistence ordering for adapter retries.
6. Decide when repeated shared use becomes evidence of competition rather than simple co-use.
7. Determine which aggregate pressures are recalculated from primary events versus stored as durable state.

## Next highest-value gap

Connect the resource ledger to the existing world-event/observation chain: scarcity should produce an ecology event, imperfect NPC/player evidence, and later recovery/renewal without population fabrication. Once a second species and physical resource are canon-approved, replace fixture-only IDs with real authored ledgers rather than promoting this test data silently.
