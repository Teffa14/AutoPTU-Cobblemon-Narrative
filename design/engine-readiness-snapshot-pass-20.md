# Engine Readiness Snapshot — Pass 20

Status: implementation evidence snapshot for narrative dependency planning. AutoPTU-Java and Python AutoPTU are read-only from this repository.

Reviewed AutoPTU-Java main evidence through commit:

`6111b6c5bcda851a1015ddc3ac4d5b578edc2c10` — Port authoritative delayed-hit scheduling state.

The Java README still states that the Python implementation remains the oracle while the port is incomplete, and still lists full battle state, full damage, status controller, terrain/hazards/forced movement/reactions, registries, tactical AI and Minecraft adapter work as incomplete.

## Classification rule

VERIFIED means the family has sufficiently broad parity-backed contracts/tests to use as a base dependency in narrative planning.

PARTIAL means meaningful authoritative slices exist, but an encounter cannot assume the whole family is available.

BLOCKING means current live evidence is insufficient for a narrative contract that requires the family as an authoritative engine feature.

A representative implementation never promotes the entire category by itself.

## Permanent capability families

| Capability family | Pass 20 state | Live evidence / interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Java README marks targeting, areas, footprints, target anchors and LoS complete. |
| base movement legality | VERIFIED | Shift, Overland/Swim/Sky, terrain costs, blockers, Wallrunner, sprint, jump and landing legality are documented complete. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | README still lists forced movement among pending combat-state work; no broad parity contract was found for this family. |
| core calculations | VERIFIED | Damage Base/type table, stages, accuracy stages, weather DB primitive, crit probability, Burn calculation, flat/scalar modifiers, rounding and stat resolution are documented. |
| action economy / initiative | VERIFIED | Typed turn flow, action budget, initiative, Trick Room, League ordering and declared-action ordering are documented complete. |
| full turn / round lifecycle | PARTIAL | Round lifecycle state, lifecycle hook registry, temporary-effect cleanup/payload state and now delayed-hit scheduling state exist. Full move execution through all lifecycle phases is not yet established. |
| full stateful damage pipeline | PARTIAL | Ordered damage hook infrastructure and selected modifiers exist. README still lists full damage resolution as incomplete. |
| status lifecycle | PARTIAL | Burn and some status interactions exist in calculations/tests, but README still lists status controller as incomplete. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Weather calculation primitives do not establish dynamic battlefield weather/terrain/hazard/reaction lifecycle. README lists terrain and hazards/reactions as pending. |
| move-specific behavior | PARTIAL | Selected move hooks and delayed-hit scheduling state exist. Delayed-hit resolution itself is explicitly a separate future slice in the latest commit. No complete Move library/registry parity exists. |
| abilities | PARTIAL | Mega Launcher has a parity-backed pre-damage hook and canonical ability identity support, but the complete Ability family is not ported. |
| items | PARTIAL | Held-item state and Pink Pearl parity exist, but the complete item registry/effect family is not ported. |
| Trainer Features / perks | BLOCKING | Python contains extensive Trainer Feature logic, but Java README still lists Trainer Feature/perk registry work as incomplete and no broad Java parity evidence was found in this pass. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal BattleChoice/action-space generation is documented complete. |
| AI tactical policy | BLOCKING | README still lists AI scoring/policy over legal choices as pending. |
| Minecraft / Cobblemon / Craftics adapter / playback support | BLOCKING | Repository explicitly remains a Java library rather than a Minecraft mod; adapter work is pending after a parity-safe vertical slice. |

## New evidence since Pass 19

### Delayed-hit scheduling state

Commit `6111b6c5bcda851a1015ddc3ac4d5b578edc2c10` adds:
- canonical delayed-hit entries;
- a server-owned queue;
- stable attacker/move/target/position/trigger-round/effect metadata;
- insertion-order preservation;
- due/future partition behavior;
- Python-oracle fixtures and CI parity.

The implementation comments explicitly separate scheduling from actual delayed move execution. Therefore this evidence strengthens `full turn/round lifecycle` and `move-specific behavior` as PARTIAL, but does not promote either to VERIFIED.

### Temporary effects and lifecycle hooks

Recent prior commits add:
- authoritative lifecycle hook registry;
- round-start temporary-effect cleanup;
- payload-bearing temporary-effect state.

These improve the state model needed for future phases, reactions and effects. They still do not demonstrate complete statuses, terrain/hazards, reactions or all move hooks.

### Ability and item representative hooks

Recent prior commits add:
- Mega Launcher pre-damage behavior with Python parity;
- Pink Pearl held-item damage behavior with Python parity.

These are evidence that the hook architecture can carry authoritative Ability and Item behavior. They are not evidence that all Abilities or Items exist.

## Narrative-authoring consequences

Safe to use as base assumptions in reduced encounter versions:
- static grids;
- legal targeting/range/LoS;
- legal Shift/Jump movement that does not require forced movement/interception;
- initiative and action-budget sequencing;
- core calculation primitives;
- legal-action enumeration;
- selected parity-backed move/ability/item slices only when the exact implementation is confirmed.

Still blocking for full encounter versions unless separately verified later:
- moving hazard fields;
- weather phases that alter battlefield state over time;
- reaction/interception objectives;
- push/pull/knockback near ledges or protected zones;
- escort/hold-zone/breakthrough victory logic that tactical AI understands;
- Trainer Feature interrupts;
- complete status-heavy bosses;
- arbitrary Ability-triggered terrain;
- Minecraft-side battle-state authority or rules duplication.

## Pass 20 civic encounter impact

`Riverside Survey Interruption` full version depends on terrain/hazards and tactical AI, both BLOCKING. Reduced static battle is feasible only after selecting exact Moves/Abilities/Items supported by current slices or constraining the roster accordingly.

`Depot Chokepoint` full version depends on complete forced movement/interception and tactical AI, both BLOCKING. The reduced version can use a static legal battle and write `route_access_restored` afterward.

`Pump House Shutdown` full version depends on tactical interactables plus zones/hazards and adapter support, all BLOCKING. The reduced version keeps pump interaction outside battle resolution.

`Public Hearing Security Incident` should keep civilians and evacuation in overworld state until protected-entity/objective mechanics and adapter support are verified.

## Verification discipline for later passes

Before promoting a category, inspect:
1. current main commit;
2. relevant Java implementation files;
3. Java tests;
4. Python-oracle fixture/exporter;
5. CI parity wiring;
6. whether the tested behavior represents the family or only one mechanic.

Narrative contracts should continue to name the exact capability families they require and preserve reduced versions where blocked families are not essential to the premise.
