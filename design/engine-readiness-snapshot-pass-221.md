# Engine readiness snapshot — pass 221

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-03

## Scope

This snapshot records the engine dependencies exposed by pass 221's ecosystem-scale finite population model and the proposed `Finite Population Survey Window` encounter.

AutoPTU-Java and AutoPTU were inspected read-only and were not modified.

The population ledger itself is persistent world/ecology authority. It is not a new AutoPTU battle capability family.

## Live repository evidence

### AutoPTU-Java

Read-only head inspected:

`23965543f8f6a1d88a44ad5e96e6df6fb66aeb87`

Head: `Freeze forced-movement trap landing order (#330)`.

The commit adds a parity gate for the ordering between a forced-movement event and the tile-entry trap landing hook for forced-movement emitters. It builds directly on the bounded tile-entry trap work from #329.

This is useful live evidence that a specific interaction between forced movement and tile-entry traps is being frozen against the pinned Python oracle.

It does not prove completion of:

- arbitrary push/pull/knockback/interception semantics;
- all forced movement emitters and interruption cases;
- all hazards/zones/reactions;
- full Status lifecycle;
- full turn/round lifecycle;
- wild population state;
- ecosystem migration;
- bait/provisioning Item behavior;
- autonomous group tactical policy;
- Minecraft/Cobblemon population projection.

Therefore complete movement and terrain/weather/hazards/zones/reactions remain partial despite the new verified slice.

### AutoPTU

Read-only head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head: `Career: keep battle coordinates synced after viewport resize (#237)`.

The commit explicitly describes itself as presentation-only and says no battle rules or outcomes change. It provides no new mechanics authority for pass 221.

## PTU/Kairos/Caelo boundary

The project Kairos source index routes world population/ecosystem guidance to pp. 437+, Pokémon management to Chapter 5, movement/terrain to pp. 382+, Status to pp. 397+, hazards to p. 401, terrain/weather to pp. 404+, capture to pp. 365–366, and Items/Gear/Crafting to pp. 495+.

Those page references are routing aids, not automatic Ouros acceptance.

The user has established that project PGU/PTU-derived material includes species/type diet assignments. A parsed authoritative diet table was not found in repository code search during this pass. No individual diet value is promoted here without direct extraction and provenance.

## Permanent capability-family status

`VERIFIED` means verified inside existing audited contracts only.

| Permanent family | Pass-221 status | Ecosystem-survey relevance |
| --- | --- | --- |
| targeting / footprints / range / LoS | VERIFIED in audited contracts | Supports authoritative spatial interactions and observation geometry. |
| base movement legality | VERIFIED in audited contracts | Supports ordinary traversal among survey sites. |
| complete movement incl. push/pull/knockback/interception/forced movement | PARTIAL | #330 adds a bounded forced-movement → trap landing-order contract. Rich scenes using interception/displacement remain dependent on broader completion. |
| core calculations | VERIFIED in audited contracts | Can support verified checks/calculations; does not define population inference. |
| action economy / initiative | VERIFIED in audited contracts | Applies when structured PTU actions begin. |
| full turn/round lifecycle | PARTIAL | Required for complete structured battles and complex multi-actor sequencing. |
| full stateful damage pipeline | PARTIAL | Required if observation/capture escalates to damaging combat. |
| status lifecycle | PARTIAL | Required when Status is applied or persists through the encounter. |
| terrain/weather/hazards/zones/reactions | PARTIAL/BLOCKING outside bounded contracts | #329/#330 verify specific tile-entry trap interactions, not the whole family. Ecosystem geometry alone does not invoke tactical terrain effects. |
| move-specific behavior | PARTIAL | Required when a Move changes traversal, detection, control, capture or battle. |
| abilities | PARTIAL | Required when an Ability materially changes the scene. |
| items | PARTIAL | Required for mechanically meaningful bait, Berries, Snacks, capture tools or other rules-bearing Items. |
| Trainer Features/perks | PARTIAL | Required for source-verified Skills/Edges/Features affecting observation, handling, food or capture. |
| AI legal-action infrastructure | VERIFIED in audited contracts | Required before a wild participant selects among legal PTU actions. |
| AI tactical policy | BLOCKING as a complete family | Required for robust autonomous tactical decisions among multiple competing goals. |
| Minecraft/Cobblemon/Craftics adapter/playback support | PARTIAL/BLOCKING end-to-end | Must implement finite-ledger projection/reservation and playback without authoring PTU facts. |

## Pass-221 world-runtime dependencies

These are required architecture capabilities but are intentionally not added as permanent battle categories:

- authoritative ecosystem extent lookup;
- finite species/population ledger;
- atomic projection reservation/release;
- persistent wild identity ownership;
- migration transfer between ecosystem ledgers;
- demographic event ledger for capture/release/birth/hatch/death/immigration/emigration;
- source-backed diet/resource records;
- observation provenance distinct from ground truth;
- multiplayer-safe prevention of duplicate projection;
- unload/reload persistence;
- Cobblemon spawn-candidate interception/gating.

The most immediate implementation blocker for the reduced encounter is therefore adapter/world-runtime integration, not missing PTU damage rules.

## Full encounter dependency trace

`Finite Population Survey Window` can begin as exploration and only activate battle families when player choices invoke them.

Observation across multiple sites principally needs:

- world/ecosystem state;
- projection reservations;
- targeting/LoS where authoritative spatial observation is needed;
- normal movement;
- behavior state;
- Cobblemon/Minecraft playback.

A mechanically meaningful placed food or bait activates `items` and potentially Trainer Features/perks.

A capture attempt activates capture calculations, Item handling, structured timing and any relevant Status/Move/Ability families.

A confrontation activates lifecycle, damage and tactical policy.

Blocking, interception, knockback or forced movement activates complete movement. If forced movement lands on a tile-entry trap, #330 gives specific new evidence for the ordering contract, but the encounter must stay within that verified contract to claim support.

Weather, hazards, zones or reactions activate their family only when authored as mechanical effects rather than scenery.

## Reduced form readiness

`Reserve, Project, Observe` can advance before full combat completeness:

```text
finite ecosystem ledger
+ native Cobblemon spawn eligibility/context
-> Ouros reserves one available wild member
-> complete WILD blueprint exists before projection
-> Cobblemon actor appears as presentation
-> player observes/travels
-> provenance is recorded
-> actor unload releases presentation reservation according to identity policy
-> population total remains conserved
```

No battle result is invented.

No bait generates another member.

No Minecraft biome boundary creates another ecosystem automatically.

No actor unload means death or emigration.

No observation count overwrites ground truth.

## Integration with first Fletchling

Current canon already freezes `COBBLEMON_FLETCHLING_ENTITY != CANONICAL_WILD_POKEMON_STATE` and `ENTITY_DESPAWN != CAPTURED_OR_DEAD` for the first Sendero actor.

Pass 221 generalizes that direction into a population-level proposal. The current Fletchling canon remains unchanged.

If the first actor becomes a durable persistent individual, it must consume exactly one membership in its eventual ecosystem ledger and cannot simultaneously appear as a generic spawn elsewhere.

## Cobblemon boundary

Current Cobblemon documentation verifies rich natural spawn conditions and weights. Those facilities should be reused for candidate eligibility and presentation context.

The missing contract is the finite Ouros gate between `eligible native spawn candidate` and `canon-correlated projected wild member`.

A weight multiplier may make an eligible species more likely to be selected under rain, time, biome or another native condition. It must never be interpreted as a population multiplier.

## New #330 consequence for narrative design

Pass 221 itself does not need forced movement. However, mechanically rich ecological encounters may later use cliffs, traps, territorial displacement or environmental hazards.

The new engine evidence supports one precise ordering path: forced-movement emitters must reach the tile-entry trap landing hook in the frozen order. Narrative documents should still mark the complete-movement and hazard families as partial whenever the concept exceeds that path.

## Unresolved implementation questions

- where in the Cobblemon spawn pipeline Ouros can safely request/reserve a ledger member;
- whether rejected native candidates can be cancelled without presentation artifacts or excessive respawn churn;
- how anonymous reservations are persisted across chunk unload/reload;
- when an anonymous member becomes a persistent identity;
- exact authoritative capture result event needed to decrement the wild ledger once;
- exact release event needed to add or transfer membership once;
- authoritative death contract and separation from Minecraft entity death callbacks;
- atomic cross-ecosystem migration ownership;
- performance target for large 1:1 ecosystem extents and many unprojected members;
- source extraction for PGU/PTU/Caelo species diets;
- whether the current Marea coordinate skeleton needs a future explicit migration to satisfy final 1:1 geography.

## Readiness conclusion

The reduced ecosystem-population loop is primarily blocked by Minecraft/Cobblemon/Craftics world-runtime integration and persistent population reservation, not by AutoPTU combat completeness.

AutoPTU-Java #330 materially improves evidence for a specific forced-movement/trap ordering path, while the broader permanent capability statuses remain unchanged: five audited families are verified within scope, most rich mechanics remain partial, full tactical policy remains blocking, and end-to-end adapter support remains partial/blocking.
