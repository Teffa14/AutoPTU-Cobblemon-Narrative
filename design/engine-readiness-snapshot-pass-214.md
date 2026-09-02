# Engine Readiness Snapshot — Pass 214

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-02

## Live evidence checked

AutoPTU-Java main remains `86aca6c86e5088bc58b8d5ffb688986693b741c7` — `Emit forced-movement Ability prevention semantics (#328)`.

The newest audited Java evidence still covers semantic Ability events for specific forced-movement-prevention cases, including provenance. It does not establish complete push, pull, knockback, interception or forced movement, and it does not establish full Ability coverage.

AutoPTU main remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`. That change is presentation-only and explicitly does not alter battle rules or outcomes.

No newer live evidence justifies promoting any permanent capability family since pass 213.

## Permanent capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited contracts.
2. base movement legality — VERIFIED within audited contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited contracts.
5. action economy/initiative — VERIFIED within audited contracts.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — BLOCKING for rich wildlife-control branches that rely on this family.
10. move-specific behavior — PARTIAL.
11. abilities — PARTIAL.
12. items — PARTIAL.
13. Trainer Features/perks — PARTIAL.
14. AI legal-action infrastructure — VERIFIED within audited contracts.
15. AI tactical policy — BLOCKING for full capability-aware autonomous wildlife choice.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for full end-to-end wildlife behavior, capture and reconciliation.

`VERIFIED` remains limited to audited contracts and never means complete PTU coverage by category.

## Pass 214 rich encounter dependency

`Lower Shelf Containment Attempt` deliberately exposes the difference between behavior interpretation and mechanical execution.

The intended full version can use spatial detection, footprints/range/LoS, movement and escape lanes, capture attempts, status/control tactics, trapping, interception, forced movement, Moves, Abilities, Items, Trainer Features and capability-aware AI selection. When environmental control is allowed, terrain/hazards/zones/reactions may also matter. Battle/capture results must reconcile into the persistent wild actor.

Therefore the full branch can touch all 16 permanent capability families.

Main blockers and partial dependencies:

- complete movement is PARTIAL if the Trainer or wild Pokémon relies on interception, push/pull/knockback or unaudited forced movement;
- full lifecycle/damage/status remain PARTIAL for arbitrary escalation paths;
- move-specific behavior, abilities, items and Trainer Features remain PARTIAL, so no representative implementation is generalized to all tactics;
- terrain/weather/hazards/zones/reactions is BLOCKING when concealment, zones or environmental control are meant to carry PTU tactical effects;
- AI tactical policy is BLOCKING for the full version because the wild actor must choose among legal withdrawal, evasion, guard/control and engagement options using species/individual intent;
- adapter/playback remains PARTIAL/BLOCKING for semantic behavior cues plus authoritative battle/capture reconciliation.

## Behavior-policy decomposition

Pass 214 does not need every tactical family to make progress.

Behavior interpretation can be implemented as a world/server policy consuming authored species/population priors, persistent individual state, actual mechanical capabilities, observed Trainer actions and local context. It produces an intent/state such as tolerant, alert, warning, withdrawing, evading, guarding or engaging.

AI legal-action infrastructure then exposes only engine-legal actions. Full AI tactical policy is responsible for selecting among them. AutoPTU resolves any mechanic. Minecraft/Cobblemon only plays back the semantic state/result.

This separation prevents a blocked tactical-policy category from forcing all wildlife to remain binary or inert.

## Reduced version dependency

`Approach, Warn, Withdraw or Battle` avoids unavailable control mechanics.

It can use server-authored tolerance context, authoritative world position/visibility, explicit player approach/withdraw choices, visible warning/departure presentation, and a normal audited BattleSpec if an actual combat begins.

It must not simulate or award missing Stealth modifiers, trapping, capture bonuses, statuses, reactions, interception or forced movement. It also must not infer PTU legality from Cobblemon animation or Minecraft geometry.

## PTU/Caelo/Kairos mechanics still requiring exact review

The Kairos source index routes capture to pp. 365–366, Skills/Edges/Features to Chapter 3, movement/tactical positioning to pp. 382+, Status Afflictions to pp. 397+, terrain/weather to pp. 404+, and encounter creation to pp. 470+. The first-wild canon routes Fletchling mechanics to supplied PTU 1.05 Pokédex p. 95 and records Caelo as comparative ecology evidence.

Exact source-text verification remains required before assigning mechanical effects to Stealth/detection, Charm, Command, Intuition, Survival, approach/handling Features or Edges, capture modifiers, Poké Ball action/range, trapping/restraint, movement hindrance, statuses used for capture/control, interception/reactions, or any Caelo/Kairos override.

## Authority boundaries

Species behavior and local habituation are world-policy inputs. They do not modify PTU stats by themselves.

An individual Pokémon's HP, Injuries, statuses, Moves, Ability and movement capabilities come from authoritative state and can constrain its choices; the narrative layer cannot fabricate weakness or courage to force a scene.

A Trainer capability is not treated as an action until activation, visibility and legality are established. Owning a trapping Move or Feature does not mean it has been used or perceived.

Minecraft entity AI cannot choose PTU actions, apply statuses, declare a trap, decide capture success or author the reason a Pokémon fled.

## Canon questions

Pass 214 does not canonize a Sendero tolerance value. Canon review still needs to decide whether routine human traffic is sufficient to define a local habituation band, which source-backed Fletchling behavior traits are accepted, and whether the first persistent Fletchling has any authored interaction history.

## Canon effect

None. This snapshot records live implementation evidence and the dependency boundary for pass-214 proposals only.