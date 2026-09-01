# Engine Readiness Snapshot — Pass 191

Status: DESIGN EVIDENCE SNAPSHOT
Date: 2026-09-01
Narrative head before this pass: 9cfdd7e64f1f51e931f2d3097c9fa27847d8df25
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
AutoPTU-Java head 1acb773 routes forced-movement prevention through shared runtime dependencies and authoritative rule-content access. The repository tree also exposes dedicated interception contract/parity workflows, but current evidence does not establish the complete matrix of Push, Pull, Knockback, Interception, collisions, partial stops, chained displacement, footprint interactions, reaction ordering and terrain-mediated displacement as one complete family.

7. full turn/round lifecycle
Important lifecycle pieces and field-round workflows exist, but no current live evidence in this pass justifies treating the whole family as complete.

8. full stateful damage pipeline
Damage behavior has implemented coverage, but the full stateful pipeline and all interactions remain broader than the verified contracts.

9. status lifecycle
Representative status behavior exists. Do not assume complete application, duration, cure, immunity, interaction and cleanup coverage across all statuses.

10. move-specific behavior
Moves must be audited individually or by verified behavioral contract. Dataset presence or representative moves do not establish parity.

11. abilities
Abilities require exact implementation evidence. Presence in source data or one working Ability does not establish the family.

12. items
Items require exact implementation evidence. Narrative custody or post-loss effects systems cannot substitute for PTU item mechanics.

13. Trainer Features/perks
Trainer Features require exact authoritative implementation evidence. Narrative roles, caretaking, memorial practices and bereavement never grant mechanical Features.

### BLOCKING when the concept requires the full family

14. terrain/weather/hazards/zones/reactions
Do not place tactical dependency on darkness/fog phases, reaction timing, delayed zones, ability-created terrain, complex hazards, unstable ledges or similar behavior without specific verified contracts.

15. AI tactical policy
Legal-action generation does not establish intelligent corridor protection, autonomous withdrawal, grief-aware behavior, companion-protection strategy or role-aware tactics.

16. Minecraft/Cobblemon/Craftics adapter/playback support
No current live evidence establishes the complete authoritative adapter/playback family required for faithful execution of every AutoPTU event in Minecraft/Cobblemon/Craftics. Presentation must consume engine outcomes rather than duplicate PTU rule authority.

## Pass-191 encounter audit

Encounter: Night Visit at the Upper Marker.

Full version dependency set:

- targeting/footprints/range/LoS: VERIFIED for audited contracts, selected content still needs audit;
- base movement legality: VERIFIED for audited contracts;
- complete movement: PARTIAL and blocking if interception/displacement/collision/partial stops are required;
- core calculations: VERIFIED for audited contracts;
- action economy/initiative: VERIFIED for audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when selected content uses statuses;
- terrain/weather/hazards/zones/reactions: BLOCKING if darkness, fog, slopes, ledges, hazards or reactions become tactical;
- move-specific behavior: PARTIAL, audit selected roster;
- abilities: PARTIAL, audit selected roster;
- items: PARTIAL, audit selected battle items;
- Trainer Features/perks: PARTIAL, audit selected Trainers;
- AI legal-action infrastructure: VERIFIED for audited contracts;
- AI tactical policy: BLOCKING for autonomous retreat/protection behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for the full in-world version.

Disposition: FULL VERSION BLOCKED.

## Reduced version

Keep visitor, memorial, mourning context, access decision and noncombatant movement outside BattleSpec. Move the visitor to a safe world-state holding position first. If a wild actor still blocks the ordinary route, compile only an isolated supported combat on stable terrain.

Allowed tactical handoff:

`IMMEDIATE_ROUTE_THREAT_WITHDREW`

The world layer then decides whether the visit continues, ends or changes future access practice.

Battle victory cannot:

- resolve grief;
- identify a spirit;
- authorize burial;
- establish cause of death;
- transfer personal effects;
- transfer companion-Pokémon ownership;
- publish private information;
- erase or modify memorial records.

Disposition: NARRATIVE PREMISE CAN ADVANCE NOW; tactical slice is runnable only after roster/content audit against verified basic contracts.

## PTU death boundary

Public PTU 1.05 Core material explicitly defines mechanical death conditions and Coup de Grâce behavior. This proves that death is a real PTU rules concern.

However, this pass did not locate live AutoPTU-Java evidence sufficient to declare a complete verified death-resolution family or a canonical battle-event handoff for death.

Therefore:

- Fainted must never be promoted to death by Narrative;
- zero HP alone must never be promoted to death by Narrative;
- Minecraft entity death/removal must never author canonical death;
- any encounter whose premise requires a combatant actually dying is blocked until the relevant PTU death behavior is verified in the authoritative engine path;
- historical deaths may still exist as explicit human-authored/canon facts independent of a simulated battle.

This is an additional exact-mechanic gap inside the broader damage/lifecycle evidence, not a reason to invent a seventeenth permanent capability family.

## Minecraft authority boundary

The current canonical Marea map already states that Minecraft entity death, unload, pathing or duplication cannot author canonical NPC death. Pass 191 extends the same rule to post-loss world state:

- breaking a grave marker does not delete the death fact;
- despawning flowers does not erase a memorial;
- picking up an effect does not transfer ownership;
- a companion Pokémon following the player does not prove custody transfer;
- a Ghost-type spawning near a marker does not identify a deceased spirit.

## Live engine evidence

AutoPTU-Java head remains `1acb773545966affce865ec3f250ff02faccae57`.

Latest relevant commit evidence remains the shared runtime dependency work for forced movement. It strengthens ownership/composition of rule content but does not promote complete movement.

The repository tree additionally shows multiple interception workflows and field-round progression coverage. These are valuable representative contracts, but pass 191 keeps the permanent family classifications conservative because the requested full interactions are broader.

AutoPTU remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its latest commit is presentation-only viewport-coordinate synchronization and explicitly states that battle rules/outcomes do not change.

## Caelo gap

No newly located indexed Caelo source in the inspected repositories establishes funerary customs, death-record authority, inheritance, companion-Pokémon custody after a Trainer's death, burial practice, memorial privacy or Ghost/spirit doctrine.

Do not canonize those systems from Pokémon franchise precedent alone.

## Live-evidence conclusion

No permanent capability category is promoted in pass 191.

Verified for audited contracts:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

Partial:

- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

Blocking when full family is required:

- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Pass 191 adds one explicit caution inside existing families: mechanically simulated death is not considered verified end-to-end until live engine contracts prove it.