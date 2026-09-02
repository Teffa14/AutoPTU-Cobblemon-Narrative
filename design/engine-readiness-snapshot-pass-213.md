# Engine Readiness Snapshot — Pass 213

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-02

## Live evidence checked

AutoPTU-Java main remains `86aca6c86e5088bc58b8d5ffb688986693b741c7` — `Emit forced-movement Ability prevention semantics (#328)`.

The current audited evidence includes semantic `AbilityEvent` output for verified forced-movement prevention subcases and preserves Ability provenance, including `[Errata]` identity. This strengthens playback for those prevention events. It still does not establish complete push, pull, knockback, interception or forced-movement coverage, nor full Ability coverage.

AutoPTU main remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`. The commit is presentation-only and states that battle rules and outcomes do not change.

No new engine evidence was found after pass 212 that justifies promoting any permanent capability family.

## Permanent capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited contracts.
2. base movement legality — VERIFIED within audited contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited contracts.
5. action economy/initiative — VERIFIED within audited contracts.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — BLOCKING for the rich retired-site encounter as a complete family.
10. move-specific behavior — PARTIAL.
11. abilities — PARTIAL.
12. items — PARTIAL.
13. Trainer Features/perks — PARTIAL.
14. AI legal-action infrastructure — VERIFIED within audited contracts.
15. AI tactical policy — BLOCKING for autonomous wildlife/objective choices in the rich encounter.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for full end-to-end execution.

`VERIFIED` is limited to audited contracts. It does not assert full PTU coverage inside that family.

## Pass 213 rich encounter dependency

`Annex Re-entry Under Shared Constraints` is intentionally capability-rich. Its full form can require interior LoS, constrained movement, optional objective lanes, autonomous wild behavior, disengagement, environmental danger, Move/Ability/Feature-driven forced movement, complete battle lifecycle and semantic objective reconciliation.

Therefore it touches all 16 permanent capability families.

The main blockers are:
- category 3 remains partial if the encounter relies on push/pull/knockback/interception beyond audited prevention subcases;
- categories 6-8 remain partial for complete encounter lifecycle/state mutation;
- categories 10-13 remain partial for arbitrary species/loadout execution;
- category 9 remains blocking if damaged floors, unstable structures or environmental zones are expected to have tactical mechanics;
- category 15 remains blocking if wild Pokémon must choose whether to defend space, withdraw, avoid an observer or protect a nest as tactical policy;
- category 16 remains partial/blocking for authoritative playback and reconciliation in Minecraft.

## Reduced version dependency

`Document the Safe Edge` avoids the blocked families without changing the story premise.

It can use:
- authenticated world access state;
- ordinary Minecraft traversal as presentation of world geometry;
- server-authoritative inspection interactions;
- persistent observation and site-history records;
- explicit player withdrawal/defer choices;
- visible wildlife driven by world state;
- separate audited BattleSpecs only when a battle is actually initiated.

It does not require tactical difficult terrain, collapse damage, forced movement, reactions, autonomous objective AI or off-screen combat simulation.

## Authority boundaries

A damaged block or model in Minecraft is visual/world representation. It does not create PTU difficult terrain, hazard damage, movement penalties, reactions or status effects unless an audited engine contract says so.

A wild Pokémon occupying a retired site is a persistent world actor. Its presence does not prove why the site was abandoned and does not imply aggression.

A memorial, plaque or archived claim is publication/public-memory state. It cannot author historical truth.

A site access restriction is world/administrative state unless a separate audited battle contract converts a defined area into tactical legality.

If an Ability or Move prevents forced movement in an authorized BattleSpec, Java remains authoritative and the adapter should consume semantic events rather than reimplement rule matching.

## Mechanical questions still open

Exact PTU/Caelo/Kairos validation remains necessary for:
- field inspection and technical assessment Skills;
- sensing hidden or hazardous physical conditions;
- climbing, balancing, lifting or obstacle traversal where a check is intended;
- Pokémon-assisted access to damaged structures;
- Ghost-type or supernatural perception if ever proposed;
- equipment used for surveying or stabilization;
- any Trainer Feature that interrupts movement or protects another actor;
- any Move-specific environmental interaction.

The project also still needs audited semantic-objective support if a battle must resolve inspect, escort, preserve-lane, withdraw, protect-observer or custody goals directly.

## Canon questions

Pass 213 proposes no canonical retired Mirador facility. Before implementation, canon review must decide whether such a predecessor structure exists, who stewards it, what is actually known about its closure and whether it has memorial, heritage, ecological or purely operational significance.

## Canon effect

None. This snapshot records current implementation evidence for pass-213 proposals only. It does not change any PTU rule, engine category, Marea location, resident history, wild population, access policy or Thin Delivery fact.