# Engine Readiness Snapshot — Pass 212

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-02

## Live evidence checked

AutoPTU-Java main advanced to `86aca6c86e5088bc58b8d5ffb688986693b741c7` — `Emit forced-movement Ability prevention semantics (#328)`.

The inspected diff adds a semantic `AbilityEvent`, preserves matched Ability provenance including `[Errata]`, and emits `forced_movement_block` semantics for verified prevention sources such as Suction Cups, Sumo Stance and a temporary Anchor Field path. It extends observable authoritative output for a forced-movement prevention subfamily. It does not demonstrate full Ability coverage or full complete-movement coverage across push, pull, knockback, interception and every forced-movement interaction.

AutoPTU main remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`. That commit is presentation-only and explicitly changes no battle rules or outcomes.

## Permanent capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited contracts.
2. base movement legality — VERIFIED within audited contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL. Prevention resolution and semantic events cover meaningful subcases, not the complete family.
4. core calculations — VERIFIED within audited contracts.
5. action economy/initiative — VERIFIED within audited contracts.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — BLOCKING for the rich emergency encounter as a complete family.
10. move-specific behavior — PARTIAL.
11. abilities — PARTIAL. Pass 212 has stronger semantic evidence for forced-movement prevention Abilities only.
12. items — PARTIAL.
13. Trainer Features/perks — PARTIAL.
14. AI legal-action infrastructure — VERIFIED within audited contracts.
15. AI tactical policy — BLOCKING for autonomous evacuation/protection/objective choices.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for the full end-to-end rich encounter.

`VERIFIED` remains scoped to audited contracts. It does not mean every PTU interaction in a family exists.

## Pass 212 encounter dependency

`Last Crossing Before Closure` is intentionally a rich target design. Its complete form can involve several spatial objectives, movement lanes, optional wild pressure, interception or forced displacement, an environmental complication with actual mechanics, battle lifecycle and autonomous NPC decisions. Therefore it touches all 16 permanent categories.

Categories 3, 6-8 and 10-13 remain partial. Category 9 remains blocking because the narrative repository may not implement environmental damage, hazardous zones, reactions or weather phases as Minecraft-only rules. Category 15 remains blocking for autonomous actors deciding tactical rescue priorities. Category 16 remains partial/blocking for full authoritative playback and reconciliation.

`Account, Warn, Reopen` is the reduced implementation. It uses authoritative narrative/world records for incident state, accountability and access restrictions; ordinary world traversal; already-authorized inspections; explicit acknowledgements; and separate optional BattleSpecs. It needs no simulated weather damage, hazards, forced movement, tactical rescue AI or hidden combat.

## Authority boundaries

An `ACCESS_RESTRICTION` is a world/administrative record unless an audited PTU contract explicitly gives the affected area mechanical terrain semantics. A Minecraft barrier, particle effect, sound or sign can present the restriction but cannot create PTU difficult terrain, damage, status, reactions or legality.

An `ACCOUNTABILITY_RECORD` records confirmed knowledge. It cannot infer that a missing actor is injured, captured, dead, hostile or responsible for the incident.

If forced movement occurs during an authorized BattleSpec, the Java engine decides prevention and emits semantic events. The new AbilityEvent path is useful playback evidence; the adapter must consume the event rather than re-checking Ability names or PTU rules locally.

A rescue objective cannot translate battle victory directly into route reopening. Reopening requires the world-state inspection/review condition authored for the incident.

## Mechanical and canon questions still open

The project needs exact PTU/Caelo/Kairos validation for field medicine/triage, navigation, lifting/carrying, obstacle clearing, rescue assistance, sensing dangerous conditions and emergency equipment before those actions receive mechanical checks or effects.

A server-authoritative lifecycle is needed for incident creation, escalation, acknowledgement, accountability and recovery across unload/reload and multiplayer sessions.

If a future BattleSpec carries evacuation, escort, custody or protected-lane objectives, the engine needs an audited semantic-objective contract rather than narrative code inferring success from positions or HP.

The project also needs a clear distinction between authored access restrictions and mechanical terrain/weather states so narrative urgency never claims implementation of capability family 9.

## Canon effect

None. This file records live implementation evidence and constraints for proposed pass-212 material. It does not establish a disaster, close a canonical route, move any resident or wild Pokémon, alter Thin Delivery Season, or change rules authority.