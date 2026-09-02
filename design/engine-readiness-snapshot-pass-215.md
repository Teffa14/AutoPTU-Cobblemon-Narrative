# Engine Readiness Snapshot — Pass 215

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-02

## Live evidence checked

AutoPTU-Java main remains `86aca6c86e5088bc58b8d5ffb688986693b741c7` — `Emit forced-movement Ability prevention semantics (#328)`.

The newest audited Java evidence still proves semantic Ability events for specific forced-movement-prevention cases. It does not prove complete push/pull/knockback/interception/forced movement, complete Ability coverage, dynamic battle reinforcement, or a full autonomous tactical-policy layer.

AutoPTU main remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`. The commit explicitly concerns presentation geometry and does not change rules or outcomes.

No newer live evidence promotes a permanent capability family beyond pass 214.

## Permanent capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited contracts.
2. base movement legality — VERIFIED within audited contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited contracts.
5. action economy/initiative — VERIFIED within audited contracts.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — BLOCKING for rich alarm-response branches that depend on interrupts, reactive attacks, environmental control or zone semantics.
10. move-specific behavior — PARTIAL.
11. abilities — PARTIAL.
12. items — PARTIAL.
13. Trainer Features/perks — PARTIAL.
14. AI legal-action infrastructure — VERIFIED within audited contracts.
15. AI tactical policy — BLOCKING for independent receiver decisions in the full signal-network encounter.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for full signal playback, participant transitions and battle/capture reconciliation.

`VERIFIED` remains contract-scoped. It never means the complete PTU family is implemented.

## Pass 215 rich encounter dependency

`Signal Chain at the Lower Shelf` introduces multiple autonomous wildlife receivers responding to partial information.

The full version may require:
- authoritative perception/LoS and footprint/range checks;
- legal withdrawal and repositioning;
- independent AI choice by each receiver;
- trapping, interception, hindrance or status-control tactics by the Trainer;
- Move, Ability, Item and Feature effects;
- reactive actions or environmental control;
- possible active-battle participant entry if the engine ever supports a responder joining after battle start;
- semantic playback and persistent writeback.

The last requirement is intentionally not treated as implemented. Existing action economy/initiative support does not prove that new combatants can be inserted into an active battle safely.

## New explicit blocker: active-battle reinforcement contract

Pass 215 exposes a contract that the permanent categories do not name separately: dynamic participant entry during an already-running encounter.

This remains represented through the existing permanent families rather than creating a seventeenth category.

It depends at minimum on:
- full turn/round lifecycle;
- action economy/initiative;
- participant state ownership;
- legal-action infrastructure;
- AI tactical policy where the arriving actor is autonomous;
- adapter/playback reconciliation.

Current status: BLOCKING / UNVERIFIED.

Narrative alarm signals therefore cannot currently mean `spawn responder into active AutoPTU battle`.

## Reduced version dependency

`Hear, React, Settle` remains viable with more basic verified capabilities.

The server can:
- derive the canonical Fletchling's behavior intent from species/context/individual state;
- emit a semantic world-level signal event;
- apply simple server-authored ALERT/WITHDRAW intent to future nearby world actors where source-backed ecology allows it;
- use authoritative world position/visibility for presentation;
- let Minecraft show orientation, movement or departure cues;
- start a normal audited BattleSpec only with the participants authorized at battle creation.

The reduced version must not:
- create free reactions;
- apply Status Afflictions from an alarm;
- grant Pack Mon or coordination bonuses;
- insert a responder after battle start;
- infer a social relationship from simultaneous movement;
- let Cobblemon entity AI decide PTU legality.

## PTU/Caelo/Kairos mechanics requiring exact review

The Kairos index continues to route:
- Skills, Edges and Features to Chapter 3;
- Pokémon/capture to pp. 340+ / 365–366;
- movement and positioning to pp. 382+;
- Status Afflictions to pp. 397+;
- hazards to p. 401;
- terrain/weather to pp. 404+;
- encounter creation to pp. 470+.

Pass 11 already identifies PTU `Pack Mon` as a real mechanical capability that must remain separate from narrative collective behavior.

Before implementing signal-network mechanics, exact source review is still required for:
- Pack Mon applicability to any proposed responder;
- communication/senses capabilities if mechanically relevant;
- Stealth/detection and perception rules;
- reactions/intercepts;
- trapping/restraining effects;
- effects that prevent fleeing or movement;
- Trainer Features/Edges that modify wild interaction or awareness;
- any rule allowing another wild Pokémon to enter an active encounter.

## Authority boundaries

A world-level alarm signal may alter behavioral intent. It does not alter HP, Stats, initiative, Status, Ability, Move legality or capture odds by itself.

A receiver can react only from information it plausibly received. It cannot inherit the caller's omniscient knowledge of the Trainer.

Species-grounded signaling tendency and local habituation remain policy inputs, not battle modifiers.

A Pokémon responding to an alarm is not automatically a member of the caller's flock/pack/collective.

Minecraft/Cobblemon can animate a call and nearby movement. It cannot decide that the call succeeded mechanically, that a responder joined battle, or that a coordinated bonus exists.

## Canon questions

1. Which Fletchling signaling behaviors are accepted from official/PTU/Caelo evidence?
2. Which next Sendero population can be canonized without inventing ecology for convenience?
3. Should `wild_signal_event` and `wild_signal_reception` be persistent world-state records or short-lived event records with selective promotion?
4. How long can area-level alarm remain after the original actor leaves?
5. What exact AutoPTU contract, if any, supports a new participant entering after battle start?
6. Which PTU Features/Edges/Skills can legitimately alter detection, calming, pursuit or response to warning activity?

## Canon effect

None. This snapshot records the current engine boundary for pass-215 research and proposals only.