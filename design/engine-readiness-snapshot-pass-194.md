# Engine Readiness Snapshot — Pass 194

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-01
Narrative head before this pass: `d6d714045e918f1c6b6108946d78680d443cf546`

Read-only engine repositories:
- AutoPTU-Java head inspected: `c34e10a57a7c3f93dd184c09a03d87fb9a014a34`
- AutoPTU head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live-engine delta

No new AutoPTU-Java commit appeared after the head inspected in pass 193.

The latest Java evidence remains commit `c34e10a57a7c3f93dd184c09a03d87fb9a014a34`, which preserves Python defender-prevention precedence for forced movement, separates status and temporary-effect prevention paths, preserves first-blocker provenance, and prevents a resolution from simultaneously representing movement and prevention.

That is meaningful forced-movement parity evidence. It still does not demonstrate the complete movement family as one closed matrix.

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its current head is presentation-only viewport-coordinate synchronization and explicitly does not change battle rules or outcomes.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains scoped to audited contracts. It does not claim universal content completion.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING when the complete family is required

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted because one representative mechanic, hook, test, or data file exists.

## Why ecological data does not change readiness

Read-only AutoPTU search in this pass found:
- species habitat fields in audited Pokédex material;
- habitat-table/configuration code in bundled Foundry/PTR2E material;
- source material that can reference terrain related to natural habitat;
- wild-Pokémon distinctions in Trainer content;
- Survival as a wilderness-oriented Skill in bundled rules material.

These findings help constrain worldbuilding. They do not constitute an implemented end-to-end ecology simulator and do not promote any permanent battle capability.

No inspected contract verifies:
- seasonal migration generation;
- local abundance simulation;
- nesting/breeding windows;
- outbreak causation;
- a regional habitat-population lifecycle;
- dynamic encounter-table authority derived from ecology records.

Narrative therefore owns authored ecological continuity while PTU/AutoPTU owns any mechanical consequences that actually enter battle.

## Pass 194 rich encounter disposition

Encounter: `Passage at the Seasonal Crossing`

Full version dependencies:

- targeting/footprints/range/LoS: VERIFIED for audited contracts;
- base movement legality: VERIFIED for audited contracts;
- complete movement: PARTIAL and blocking when corridor protection needs interception, Push, Pull, Knockback, collisions, partial stops, or other forced movement;
- core calculations: VERIFIED for audited contracts;
- action economy/initiative: VERIFIED for audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when roster/content uses statuses;
- terrain/weather/hazards/zones/reactions: BLOCKING if route edges, seasonal water, weather, zones, hazards, or reactions enter tactical rules;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED for audited contracts;
- AI tactical policy: BLOCKING for objective-aware wild behavior such as withdrawal, corridor continuation, spacing, and threat response;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful end-to-end projection and return to persistent world state.

Disposition: FULL VERSION BLOCKED.

## Complete-movement caution

The current forced-movement work must not be generalized into full movement readiness.

Still not demonstrated as a single complete verified matrix by current live evidence:
- all Push behavior;
- all Pull behavior;
- all Knockback behavior;
- all Interception behavior;
- collision handling;
- partial stops;
- chained displacement;
- footprint interactions during displacement;
- reaction ordering across all relevant effects;
- terrain-mediated displacement;
- all combinations with Moves, Abilities, Items, Trainer Features, statuses, and temporary effects.

Category remains PARTIAL.

## Reduced encounter viability

The reduced version is viable without pretending missing mechanics exist.

Narrative world state retains:
- ecological-window identity and timing;
- the larger population's presence/passage;
- observers and noncombatants;
- observation records;
- route-use advice/access state;
- safe withdrawal before combat;
- hypotheses about cause and recurrence.

If one specific actor still creates an immediate confrontation, compile a separate ordinary audited BattleSpec on stable geometry using only verified/supported content.

Allowed narrow outputs:
- `IMMEDIATE_CROSSING_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`
- `IMMEDIATE_FIELD_TEAM_CAN_WITHDRAW`

Battle output must not establish:
- total population size;
- migration status;
- ecological-window end state;
- breeding/nesting behavior;
- weather causation;
- Thin Delivery causation;
- capture law/permission;
- permanent route safety.

## AI-specific caution

This pass makes AI tactical policy especially visible.

A wild Pokémon participating in a passage/gathering scene may rationally prefer:
- leaving the threat zone;
- continuing through a corridor;
- maintaining distance;
- protecting space;
- avoiding unnecessary engagement.

AI legal-action infrastructure can constrain legality. It does not prove that the policy layer can choose those objectives competently.

Until a verified objective-aware tactical policy exists, reduced encounters should avoid claiming sophisticated ecology-driven combat behavior from the engine.

## Minecraft/Cobblemon projection boundary

The adapter must eventually project ecological state without becoming its authority.

Required principles:
- visible actor count may be lower than narrative population scope for performance;
- chunk unload cannot end an ecological window;
- despawn cannot prove departure;
- spontaneous Cobblemon spawn placement cannot author a new Marea population fact;
- battle removal/KO state cannot automatically disperse the larger group;
- return from BattleSpec must preserve the narrative window unless an authorized world transition changes it.

This remains BLOCKING for faithful end-to-end implementation.

## PTU/Caelo mechanical uncertainty

No live source inspected this pass establishes a generic PTU/Caelo subsystem for:
- migration seasons;
- spawning ecology;
- population abundance;
- breeding windows;
- wildlife corridors;
- seasonal capture restrictions;
- conservation closures.

Species habitat metadata must remain evidence about general habitat association, not a local spawn command.

No indexed Caelo material was found in the three project repositories during this pass, so Caelo-specific ecology remains unresolved.

## Implementation recommendation

Implement the noncombat candidate `Two Counts, Two Methods` first.

It tests:
- observer provenance;
- method-specific evidence;
- compatible versus incompatible counts;
- uncertainty persistence;
- longitudinal revision;
- Mirador/Nerea/Ema canon reuse.

It requires no new battle capability and creates infrastructure needed before any seasonal population event can be represented honestly.
