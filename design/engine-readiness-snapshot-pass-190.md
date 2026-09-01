# Engine Readiness Snapshot — Pass 190

Status: DESIGN EVIDENCE SNAPSHOT
Date: 2026-09-01
Narrative head before this pass: cf2cc23188aec8a37c28f7d3fe58adfa60934b1c
AutoPTU-Java inspected read-only head: 1acb773545966affce865ec3f250ff02faccae57
AutoPTU inspected read-only head: 729bae2d424963ff9bb3f4159c9a7ac9152128a7

No engine files were modified.

## Classification rule

A representative implementation does not promote an entire permanent capability family. A family changes state only when current tests/contracts establish the behavior needed by the encounter being designed.

## Permanent capability categories

### VERIFIED for audited contracts

1. targeting/footprints/range/LoS
Current evidence supports the audited targeting and geometry contracts already accepted by prior snapshots. This does not imply every move-specific targeting exception exists.

2. base movement legality
Current evidence supports the audited base movement legality contracts. This excludes the complete forced/displacement/interception family.

3. core calculations
Current evidence supports the audited core calculation contracts already accepted by the engine project.

4. action economy/initiative
Current evidence supports the audited action/initiative contracts already accepted by prior snapshots.

5. AI legal-action infrastructure
Current evidence supports infrastructure for filtering/selecting legal actions within covered contracts. This does not establish strong tactical policy.

### PARTIAL

6. complete movement including push/pull/knockback/interception/forced movement
AutoPTU-Java head 1acb773 strengthens runtime composition through BattleRuntimeDependencies and authoritative combatant rule-content access in forced-movement prevention. It does not establish the complete matrix of Push, Pull, Knockback, Interception, collisions, partial stops, chained displacement, footprint interactions, reaction ordering and terrain-mediated displacement.

7. full turn/round lifecycle
Important lifecycle pieces exist, but no current live evidence in this pass justifies treating the whole family as complete.

8. full stateful damage pipeline
Damage behavior has implemented coverage, but the full stateful pipeline and all interactions remain broader than the verified contracts.

9. status lifecycle
Representative status behavior exists. Do not assume complete application, duration, cure, immunity, interaction and cleanup coverage across all statuses.

10. move-specific behavior
Moves must be audited individually or by verified behavioral contract. Dataset presence or representative moves do not establish parity.

11. abilities
Abilities require exact implementation evidence. Presence in source data or one working Ability does not establish the family.

12. items
Items require exact implementation evidence. Narrative inventory/custody systems cannot substitute for PTU item mechanics.

13. Trainer Features/perks
Trainer Features require exact authoritative implementation evidence. This is especially important in pass 190 because PTU Mentor is a real mechanical Trainer Class. Ordinary fictional instruction must never emulate Mentor Features, Lessons, Tutor Points, Skill Rank prerequisites or their Effects.

### BLOCKING when the concept requires the full family

14. terrain/weather/hazards/zones/reactions
Do not place tactical dependency on changing weather phases, reaction timing, delayed zones, ability-created terrain, complex hazards or similar behavior without specific verified contracts.

15. AI tactical policy
Legal-action generation does not establish intelligent tactical adaptation, protected-corridor behavior, mentoring behavior, rival learning or role-aware strategy.

16. Minecraft/Cobblemon/Craftics adapter/playback support
No current live evidence establishes the complete authoritative adapter/playback family required for faithful execution of every AutoPTU event in Minecraft/Cobblemon/Craftics. Presentation must consume engine outcomes rather than duplicate PTU rule authority.

## Pass-190 encounter audit

Encounter: Supervised Field Lead at Glass Bend.

Full version dependency set:
- targeting/footprints/range/LoS: VERIFIED for audited contracts, but selected content still needs audit;
- base movement legality: VERIFIED for audited contracts;
- complete movement: PARTIAL and therefore blocking if interception/displacement/collision/partial stops are required;
- core calculations: VERIFIED for audited contracts;
- action economy/initiative: VERIFIED for audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when selected content uses statuses;
- terrain/weather/hazards/zones/reactions: BLOCKING if field conditions are tacticalized;
- move-specific behavior: PARTIAL, audit selected roster;
- abilities: PARTIAL, audit selected roster;
- items: PARTIAL, audit selected battle items;
- Trainer Features/perks: PARTIAL, and especially sensitive for any supervision/training fiction;
- AI legal-action infrastructure: VERIFIED for audited contracts;
- AI tactical policy: BLOCKING for competent autonomous corridor/protection behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for the full in-world version.

Disposition: FULL VERSION BLOCKED.

Reduced version:
Keep supervision, field procedure, noncombatant movement, retreat choice, competency evidence and scope review outside BattleSpec. Compile only an isolated supported combat after noncombatants are safe. Use narrow tactical handoffs. Do not let battle victory write competency, promotion, authority, procedure certification or PTU Features.

Disposition: NARRATIVE PREMISE CAN ADVANCE NOW; battle slice is runnable only after roster/content audit against the verified basic contracts.

## PTU-specific pass-190 boundary

Public PTU material confirms Mentor as a mechanical Trainer Class with concrete Effects involving Tutor Points, Moves, Move List capacity, Nature, Poké Edges and Abilities. Therefore:
- narrative mentoring is ordinary fiction unless a character sheet says otherwise;
- a competency observation cannot grant Mentor;
- a supervisor cannot teach a mechanical Move unless PTU rules and engine state authorize that effect;
- an operational scope grant cannot alter battle legality;
- a Minecraft lesson animation cannot create a Tutor Point transaction.

## Caelo gap

No newly located indexed Caelo source in the inspected repositories establishes apprenticeship, certification, licensing or supervision rules. Keep all pass-190 role progression proposed until Caelo material or explicit canon approval resolves the relevant authority.

## Live-evidence conclusion

No permanent capability category is promoted in pass 190. AutoPTU-Java and AutoPTU heads are unchanged from pass 189. The new Narrative layer is intentionally useful without requiring engine completion: most supervised-practice quests can run as world-state, records, schedules, dialogue and physical procedure interactions, while combat-heavy variants remain dependency-gated.