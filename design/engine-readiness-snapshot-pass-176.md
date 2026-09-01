# Engine Readiness Snapshot — Narrative Pass 176

Status: READ-ONLY EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-09-01
Purpose: gate narrative encounter designs against current AutoPTU evidence without changing either engine repository.

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only

## Current heads observed

### AutoPTU-Java

Observed head: `7cbc5aafb50a5221d4493518297f24ff3e4a960a`

Commit title:
`Freeze composite forced movement prevention guard (#313)`

Relevant recent lineage:

- `7cbc5aa...` freezes a composite forced-movement prevention guard and associated oracle assertions;
- `8e5204b...` binds Shadow Tag through generic forced-movement step constraints and compares displacement outcomes against the oracle;
- `cc5522b...` freezes combatant/footprint distance geometry used by that work;
- earlier commits cover status/temporary-state prevention branches and forced-movement observable contracts.

Interpretation:
This is meaningful progress in the forced-displacement implementation. It demonstrates composition of particular prevention constraints and candidate-step geometry. It does not establish that the permanent category `complete movement including push/pull/knockback/interception/forced movement` is complete.

The following remain distinct obligations unless current tests/contracts explicitly cover them: Push, Pull, Knockback, interception, arbitrary forced displacement, collisions, obstacle interactions, partial stops, multi-step termination, chained effects and interactions with other movement modifiers.

### AutoPTU

Observed head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit title:
`Career: keep battle coordinates synced after viewport resize (#237)`

The latest visible work is Career/presentation and roster recovery. It provides no new read-only evidence in this pass for promotion of the tactical capability families below.

## PTU source availability check

Repository code search located PTU 1.05 source material under AutoPTU, including:

- `files/rulebook/PTU changelog 1.05.txt`;
- `files/rulebook/PTU 1.05/PTU changelog 1.05.txt`;
- `audit_sources/PTU May 2015 Playtest Packet.txt`;
- PTU 1.05 trainer/data sheets;
- data-driven move/item/ability inputs used by AutoPTU.

This supports continued rule-level cross-checking. It does not by itself prove engine implementation parity.

A literal code search for `Caelo` across Narrative, AutoPTU-Java and AutoPTU returned no results during this pass. Therefore no Caelo-specific mechanic, historical premise, institution or setting fact is asserted here. This is an unresolved source-location question, not a declaration that Caelo material is absent from the broader project.

## Permanent capability classification

The labels below are conservative narrative gates. `VERIFIED` means current project evidence supports the covered contracts already tracked by the project; it does not mean every imaginable use of that family is automatically safe. `PARTIAL` means substantial implementation exists but the complete category cannot be assumed. `BLOCKING` means a narrative concept requiring the complete family should not rely on it until live evidence changes.

### VERIFIED for covered contracts

1. targeting/footprints/range/LoS
2. base movement legality
4. core calculations
5. action economy/initiative
14. AI legal-action infrastructure

### PARTIAL

3. complete movement including push/pull/knockback/interception/forced movement
6. full turn/round lifecycle
7. full stateful damage pipeline
8. status lifecycle
10. move-specific behavior
11. abilities
12. items
13. Trainer Features/perks

### BLOCKING as complete families

9. terrain/weather/hazards/zones/reactions
15. AI tactical policy
16. Minecraft/Cobblemon/Craftics adapter/playback support

## Narrative implications for Pass 176

The persistent aftermath layer itself does not require BattleSpec. Site restriction, repair, recovery, archival trace, custodial authority and calendar progression can remain world-state/narrative systems.

The proposed `The Shelf After the Slide` full version becomes mechanically rich only if unstable terrain, dynamic hazards, forced movement, reactions, weather phases or tactical opponent choices are compiled into combat.

Full-version category requirements if all proposed mechanics remain:

- targeting/footprints/range/LoS — VERIFIED for covered contracts;
- base movement legality — VERIFIED for covered contracts;
- complete movement — PARTIAL and therefore a blocker for rich forced-movement/interception use;
- core calculations — VERIFIED for covered contracts;
- action economy/initiative — VERIFIED for covered contracts;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if selected Moves/statuses use it;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL and must be audited per selected Move;
- abilities — PARTIAL and must be audited per selected Ability;
- items — PARTIAL when relevant;
- Trainer Features/perks — PARTIAL when relevant;
- AI legal-action infrastructure — VERIFIED for covered contracts;
- AI tactical policy — BLOCKING for unscripted tactical behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING as a complete family for faithful rich presentation.

Conclusion: full version remains BLOCKED.

## Reduced-version gate

The reduced variant can preserve the narrative premise while avoiding unsupported tactical claims:

- unstable route cells are authored world state, not combat terrain;
- movement through the inspection sequence uses fixed safe points outside BattleSpec;
- no push/pull/knockback/interception objective is required;
- no active weather/hazard phase is compiled;
- no civilian/crew escort unit participates in tactical initiative;
- any optional fight uses a stable bounded arena;
- exact Moves, Abilities, Items and Trainer Features are audited before that fight is enabled;
- battle result can clear an immediate corridor but cannot author repair, cause, reopening or ecological conclusion;
- Minecraft presentation reads canonical state but cannot decide it.

Conclusion: narrative reduced version is NOT blocked by the rich terrain/forced-movement premise, but any actual battle inside it remains subject to exact per-encounter audit.

## No category promotion from representative mechanics

Permanent guard for future narrative passes:

- Shadow Tag support does not imply all forced movement;
- one Knockback test would not imply Push/Pull/interception;
- one status does not imply status lifecycle;
- one weather Move does not imply weather phases;
- one Ability does not imply Abilities as a family;
- one Trainer Feature interrupt does not imply Trainer Features/perks;
- one legal-action selector does not imply tactical AI policy;
- one Cobblemon animation does not imply adapter/playback parity.

Narrative documents should continue to list the exact family whenever a concept depends on it.

## Unresolved evidence questions

- Locate the project’s intended Caelo source material, if it exists outside currently indexed repository paths.
- Continue tracking complete Push/Pull/Knockback/interception/collision/partial-stop evidence rather than promoting movement from Shadow Tag work.
- Identify the first authoritative terrain/weather/hazard/reaction contract before designing a combat where environmental phases are mandatory.
- Audit exact Moves/Abilities/Items/Trainer Features for any proposed Marea encounter before promotion.
- Keep Minecraft/Cobblemon/Craftics as presentation/adaptation until the project has explicit parity evidence for the required playback surface.