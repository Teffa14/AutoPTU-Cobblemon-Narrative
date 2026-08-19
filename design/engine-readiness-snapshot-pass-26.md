# Engine Readiness Snapshot — Pass 26

Status: read-only evidence snapshot for narrative implementation planning. AutoPTU and AutoPTU-Java were not modified by this task.

## Evidence inspected

Python AutoPTU current `main` observed at:
- `54e4fa8ccbe0e555afef8b4b3713e7568608e5d3`

AutoPTU-Java current `main` observed at:
- `163710b089500f7c9e389ff42044210574ee7f2d`

The Java project still states that Python AutoPTU remains authoritative while the port is incomplete.

## New Java evidence since Pass 25

The latest Java commit adds server-owned active-turn state:
- active combatant identity is stored in `BattleTurnState`;
- current `TurnPhase` is stored by the battle core;
- `beginTurn` and phase transitions operate on authoritative state;
- `endTurn()` consumes the server-owned actor/phase pointer and clears it afterward;
- round start resets active actor and phase to the Python-compatible state;
- parity tests compare this lifecycle behavior against Python.

This is meaningful lifecycle progress. It removes another responsibility from future Minecraft adapters: they should not be able to invent which combatant currently owns the turn or spoof the current phase.

The same commit explicitly preserves Trainer Feature dispatch as a separate future slice. Therefore this evidence does not promote Trainer Features/perks or full lifecycle to complete.

## Permanent capability classification

### VERIFIED

#### targeting/footprints/range/LoS
Evidence remains strong for range, AoE geometry, footprints, target anchors and line of sight.

Narrative implication:
Can serve as a geometric foundation for static battle maps. It does not prove out-of-combat vision, hearing, guard awareness or stealth detection.

#### base movement legality
Java covers bounded shift/jump legality including Overland/Swim/Sky, terrain costs, blockers, Wallrunner, sprint, landing fit and jump path behavior in the currently ported slice.

Narrative implication:
Safe foundation for ordinary battle-grid traversal. It does not prove pursuit/interception or overworld movement semantics.

#### core calculations
Damage Base tables, type-effectiveness steps and several calculation primitives are ported with oracle contracts.

#### action economy/initiative
Typed action budget, turn phases, initiative and League/declaration ordering are ported. The new server-owned active actor/phase pointer strengthens this family’s runtime authority.

#### AI legal-action infrastructure
Java can enumerate legal battle choices under the currently represented rules.

Narrative implication:
This does not mean AI knows which choice is tactically good or how a security patrol should search for an intruder.

### PARTIAL

#### full turn/round lifecycle
Evidence now includes round transitions, lifecycle hooks, temporary-effect cleanup, damage/injury history rotation, delayed-hit scheduling/binding, turn-end boundaries and authoritative active actor/phase state.

Still incomplete:
- complete port of all lifecycle-triggered rule families;
- full Trainer Feature dispatch;
- full status/terrain/hazard/reaction lifecycle;
- complete semantic transcript parity.

Classification remains PARTIAL.

#### full stateful damage pipeline
Core math and selected state/history plumbing exist, but Java README still lists full damage resolution and remaining stateful accuracy modifiers as unfinished.

#### status lifecycle
Selected status/calculation behavior exists, but the complete status controller remains listed as unfinished.

#### move-specific behavior
Representative slices and delayed-hit plumbing exist. One or several implemented Move paths do not demonstrate the full Move library.

#### abilities
Representative ability behavior exists from earlier passes. Full registry coverage is not established.

#### items
Representative item behavior exists from earlier passes. Full registry coverage is not established.

### BLOCKING

#### complete movement including push/pull/knockback/interception/forced movement
Java README still lists forced movement and reactions among unfinished work.

Narrative implication:
Escort, tactical chase, interception, knockback hazards and forced displacement need reduced implementations.

#### terrain/weather/hazards/zones/reactions
Still listed among unfinished stateful battle systems.

Narrative implication:
Do not implement tactical darkness zones, smoke fields, guard reaction cones, security hazards or environmental stealth effects in Minecraft as substitute rules.

#### Trainer Features/perks
The generic lifecycle foundation is improving, but full perk/Trainer Feature registries and dispatch remain unfinished.

Narrative implication:
Rogue/Ninja/Mastermind or similar infiltration-oriented Features cannot be assumed executable in Java.

#### AI tactical policy
Legal choices exist; scoring/policy remains listed as unfinished.

Narrative implication:
Search patterns, pursuit, interception, suspicion responses, objective-aware guards and stealth patrol tactics are not verified battle AI behavior.

#### Minecraft/Cobblemon/Craftics adapter/playback support
The Java project remains a library rather than a Minecraft mod and explicitly defers the adapter until a parity-safe vertical slice exists.

Narrative implication:
Overworld patrols, observer FOV, disguise presentation, access checkpoints, alarm propagation and physical stealth remain design targets, not verified runtime features.

## Pass 26 infiltration-specific evidence

### What Python evidence establishes

Current Python project material contains Stealth and Guile as recognized skills in authoritative data/runtime contexts and includes source/audit material for special capabilities such as Dead Silent and other concealment-related concepts.

This does not prove that Python has one complete authoritative out-of-combat stealth simulator. The narrative layer must not convert skill names or capability definitions into a new detection engine without explicit contracts.

### What Java LoS does not establish

Battle LoS answers whether battle geometry permits a line of sight under the ported targeting rules. It does not establish:
- NPC vision distance in Minecraft;
- hearing;
- social recognition;
- disguise detection;
- observer confidence;
- patrol search policy;
- alarm propagation;
- surprise or concealment outside battle.

Treat those as separate world/adapter authority concerns.

### What the new active-turn pointer changes

The server-owned active actor and phase pointer is valuable for future reaction and interruption work because the battle core now owns another part of temporal authority.

It does not yet verify:
- reaction registries;
- Trainer Feature interrupts;
- detection interrupts;
- overwatch/security zones;
- pursuit AI;
- tactical stealth.

## Capability requirements for Pass 26 encounter concepts

### Archive Night Shift
FULL:
- targeting/footprints/range/LoS — VERIFIED foundation;
- base movement legality — VERIFIED foundation;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- Trainer Features/perks — BLOCKING if specialist effects are used;
- terrain/weather/hazards/zones/reactions — BLOCKING if darkness/reaction mechanics are used.

REDUCED:
Resolve access and stealth in overworld/quest state with validated PTU/Caelo rules; use static ordinary combat only after escalation.

### Depot Cover Story
FULL:
- targeting/footprints/range/LoS — VERIFIED foundation;
- base movement legality — VERIFIED;
- complete movement/interception — BLOCKING for tactical pursuit;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- Trainer Features/perks — BLOCKING if applicable.

REDUCED:
Handle cover, observation and tailing through actor knowledge, access and route state. Battle remains a separate static encounter.

### Willing Insider Extraction
FULL:
- complete movement/interception/forced movement — BLOCKING;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING if reaction chokepoints exist;
- full turn/round lifecycle — PARTIAL if timed/delayed effects are used.

REDUCED:
Keep the insider off-grid and resolve one or more ordinary static encounters around the extraction route.

### Authorized Security Exercise
FULL:
- targeting/footprints/range/LoS — VERIFIED geometry only;
- base movement legality — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- Trainer Features/perks — BLOCKING when relevant.

REDUCED:
Use validated world-state checks and a separate ordinary battle drill. Do not invent a stealth-score subsystem.

## Current summary table

| Permanent category | State |
|---|---|
| targeting/footprints/range/LoS | VERIFIED |
| base movement legality | VERIFIED |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING |
| core calculations | VERIFIED |
| action economy/initiative | VERIFIED |
| full turn/round lifecycle | PARTIAL |
| full stateful damage pipeline | PARTIAL |
| status lifecycle | PARTIAL |
| terrain/weather/hazards/zones/reactions | BLOCKING |
| move-specific behavior | PARTIAL |
| abilities | PARTIAL |
| items | PARTIAL |
| Trainer Features/perks | BLOCKING |
| AI legal-action infrastructure | VERIFIED |
| AI tactical policy | BLOCKING |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING |

## Non-inference rules

- Server-owned active actor/phase does not mean full lifecycle is complete.
- One lifecycle hook does not mean all Trainer Features work.
- Battle LoS does not mean overworld stealth works.
- Recognized Stealth/Guile data in Python does not mean Java has those rules.
- One Ability or Item implementation does not establish full registry coverage.
- Delayed-hit scheduling does not establish every delayed Move.
- Legal-action enumeration does not establish tactical AI.
- A Minecraft NPC that can walk does not establish PTU interception, reaction or detection rules.

## Next evidence that would justify promotion

Full lifecycle could approach VERIFIED only after the remaining lifecycle-triggered rule families and transcript contracts are covered by representative oracle tests with no known major family gaps.

Trainer Features/perks need authoritative registry/state plus representative Feature parity across distinct trigger types.

AI tactical policy needs scoring/decision contracts and tests over materially different tactical goals.

Minecraft adapter needs server-authoritative DTO boundaries and playback tests proving the adapter renders rather than recalculates PTU state.

A tactical stealth capability would need a separate explicit contract defining observer state, perception inputs, visibility/awareness semantics, PTU interaction and Minecraft authority. It must not be inferred from targeting LoS alone.