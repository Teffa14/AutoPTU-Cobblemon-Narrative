# Engine readiness snapshot — pass 220

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-03

## Scope

This snapshot records the engine dependencies exposed by pass 220's wild feeding, baiting and anthropogenic provisioning concepts. AutoPTU-Java and AutoPTU were inspected read-only and were not modified.

Primary concept: `Bait at the Lower Shelf`.
Reduced form: `Place, Withdraw, Observe`.

## Live repository evidence

### AutoPTU-Java

Read-only head inspected:

`a4df700c4a9099448d5efbfccfd56214bc1f704c`

Head remains `Freeze generic tile-entry trap contract (#329)`.

The commit freezes an authoritative generic tile-entry trap contract with parity/oracle coverage and bounded Status consequence semantics. It is useful evidence for a specific hazard/trap path. It does not provide a general wild-food, Berry, Snack, Refreshment, bait, capture-preparation or autonomous provisioning-response contract.

A code search for combined food/Berry/Snack/Refreshment item-resolver terms did not surface a dedicated contract. Absence from that search is not proof that no item code exists; it means pass 220 has no live evidence sufficient to promote the `items` family or claim edible-item completeness.

### AutoPTU

Read-only head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head remains `Career: keep battle coordinates synced after viewport resize (#237)`. The commit explicitly states that it is presentation-only and changes no battle rules or outcomes. It provides no new mechanics authority for pass 220.

## PTU/Kairos evidence boundary

The project Kairos index routes capture to pp. 365–366 and Items/Gear/Crafting to pp. 495+ of the supplied Kairos core compilation. It also routes Skills/Edges/Features to Chapter 3 and Pokémon management to Chapter 5.

Public PTU 1.05 text confirms that food is already a rules-bearing domain: Snacks including Berries can grant Digestion/Food Buffs, Refreshments have defined consumption/healing rules, and Chef features can modify food effects. This is evidence against implementing a generic Minecraft-side `food -> wild bonus` shortcut.

Pass 220 therefore treats edible PTU Items as mechanically unavailable until their exact contract is verified. Ordinary authored world food may still exist as non-mechanical ecology/context.

## Permanent capability-family status

`VERIFIED` means verified inside existing audited contracts, not universally complete.

| Permanent family | Pass-220 status | Provisioning relevance |
| --- | --- | --- |
| targeting / footprints / range / LoS | VERIFIED in audited contracts | Needed for authoritative spatial placement, approach and observation. Food-specific detection semantics remain a content/behavior concern. |
| base movement legality | VERIFIED in audited contracts | Supports approach, withdrawal and ordinary traversal. |
| complete movement incl. push/pull/knockback/interception/forced movement | PARTIAL | Needed only if a resource contest uses blocking, interception or forced displacement. #329 does not complete this family. |
| core calculations | VERIFIED in audited contracts | Can host verified checks/calculations. Does not authorize a bait or capture modifier. |
| action economy / initiative | VERIFIED in audited contracts | Applies when a structured action sequence begins. |
| full turn/round lifecycle | PARTIAL | Needed for a complete multi-actor structured encounter. |
| full stateful damage pipeline | PARTIAL | Needed only if the scene becomes damaging combat. |
| status lifecycle | PARTIAL | Needed if control/capture tactics apply Status. #329 covers bounded trap consequences, not the full family. |
| terrain/weather/hazards/zones/reactions | PARTIAL/BLOCKING outside bounded contracts | Relevant only if the authored scene actually uses hazards, zones, reactions or weather mechanics. A food location is not automatically a tactical zone. |
| move-specific behavior | PARTIAL | Required only when a Move participates in lure/control/capture behavior. |
| abilities | PARTIAL | Required only when an Ability changes the interaction. |
| items | PARTIAL | Central blocker for mechanically meaningful Berries/Snacks/Refreshments/bait. No complete edible-item contract was verified in this pass. |
| Trainer Features/perks | PARTIAL | Chef or other relevant Features/Edges require exact source and implementation verification. |
| AI legal-action infrastructure | VERIFIED in audited contracts | Required before a wild actor can choose among legal actions. |
| AI tactical policy | BLOCKING as a complete family | Needed for competent selection among approach, inspect, consume, carry, guard, evade, engage and competing tactical goals. Simple behavior intent can precede full tactical AI. |
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING end-to-end | Must project placed resources and semantic outcomes without creating PTU effects or battle authority. |

## Full-version dependency trace

The full `Bait at the Lower Shelf` encounter does not automatically require all families.

Observation-only provisioning principally needs authoritative world state, spatial perception/placement, normal movement, individual wild behavior state and adapter playback. A Trainer who then attempts capture may activate Items, Features, capture calculations and structured timing. A fight can add lifecycle, damage and Status. Physical contests over the resource may add complete movement/interception. Environmental hazards or reactions become dependencies only if explicitly authored.

This conditional activation is important. Narrative content should not wait for every battle family when the reduced premise is already valid.

## Reduced-form readiness

`Place, Withdraw, Observe` can be represented as:

```text
authoritative provisioning event
+ existing site/world time
+ authoritative wild presence
+ normal traversal
+ simple behavior observation
+ provenance record
-> response observation
-> later ecological interpretation
```

The reduced form intentionally supplies no PTU Food Buff, healing, capture modifier, friendship, ownership, guaranteed spawn or off-screen combat.

Cobblemon remains responsible for native generic spawning and overworld projection where appropriate. Ouros remains responsible for canon population/identity, provenance, persistent intervention history and behavior context. AutoPTU becomes authoritative when an actual PTU mechanic is invoked.

## Adapter guardrail

An edible Minecraft/Cobblemon object is not sufficient evidence for a PTU Item effect.

The adapter may display or place a resource. It must not decide:

- that a wild Pokémon is mechanically allowed to consume it;
- that consumption grants healing or a Food Buff;
- that capture chance changes;
- that friendship/loyalty changes;
- that another wild Pokémon spawns;
- that a consumer becomes a battle participant;
- that a Trainer Feature applies.

Those facts require their owning systems and verified rules.

## Known adjacent blocker

Mid-battle participant insertion remains unverified/blocking. If a second wild Pokémon notices food after BattleSpec creation, it cannot simply join the active battle through overworld AI. Supporting that behavior would require lifecycle, initiative/participant ownership, legal-action generation, tactical policy and adapter support to agree on an explicit contract.

## Unresolved mechanical questions

Direct source and engine audits are still needed for:

- action type, range and targeting when offering/throwing an edible Item to a wild Pokémon;
- legal consumption by uncontrolled targets;
- Berries, Snacks, Refreshments and Food/Digestion Buff lifecycle;
- Chef and other relevant Trainer Features/perks;
- exact capture action and modifiers;
- whether any PTU/Kairos/Caelo rule explicitly models bait/luring;
- Item ownership/consumption writeback when a wild actor takes or carries an object;
- adapter persistence for a placed resource across unload/reload and multiplayer observation.

## Readiness conclusion

Pass 220 can advance immediately as world-state and observation gameplay. Its mechanically rich form remains constrained most directly by `items`, Trainer Features/perks, full AI tactical policy and end-to-end adapter support, with other families activated only when the player's chosen tactic actually invokes them.