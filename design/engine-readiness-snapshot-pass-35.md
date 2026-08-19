# Engine Readiness Snapshot — Pass 35

Status: read-only evidence snapshot for narrative design. This file does not change AutoPTU-Java or AutoPTU.
Date: 2026-08-19

## Live repositories inspected

AutoPTU-Java head inspected:
`b7a71bc6e8a4f6b03f8b0a10cca2a15b915a4e53`

Latest observed Java change:
`Port Flinch round-boundary expiry (#62)`

Python AutoPTU head inspected:
`e4bb0ca38b7018710af476ce365d515a387de4e7`

Recent Python changes are Career/roster recovery work and do not by themselves change the tactical capability classification used by the narrative repository.

## New Java evidence since Pass 34

The current Java line now includes several bounded status/lifecycle slices beyond the earlier canonical status-metadata store:

- reusable ordered status phase effect registry;
- Flinch START phase behavior through that registry;
- Strange Tempo + Confusion START branch parity against Python;
- canonical status metadata bound to runtime state;
- Flinch round-boundary expiry using `applied_round` metadata;
- parity tests freezing those concrete behaviors against the Python oracle.

The newest commit specifically shows that metadata-bearing Flinch can expire after its applied round, remove the status and emit a semantic `status_ends` event without producing another skip. During the applied round, Flinch still produces its pending skip behavior.

This is meaningful progress for `full turn/round lifecycle` and `status lifecycle`.

It is not evidence that the full status family is complete.

## Permanent capability map

### VERIFIED

#### targeting/footprints/range/LoS
Verified by existing Java contracts and tests for target anchors, areas, footprints, direct targets and line of sight.

#### base movement legality
Verified for the currently ported base movement slice: Overland/Swim/Sky, terrain costs, blockers, Wallrunner, sprint, jump and landing-fit behavior.

This does not include forced movement/interception.

#### core calculations
Verified for the bounded calculation primitives already ported: Damage Base tables, type effectiveness, stages, accuracy, crit probability, Burn calculation branches, modifiers and rounding primitives.

This does not mean the full stateful damage pipeline is complete.

#### action economy/initiative
Verified for typed turn flow, action budget, deterministic initiative ordering, League ordering and declared-action ordering.

#### AI legal-action infrastructure
Verified for construction/filtering of legal BattleChoice options over the currently supported action space.

This is not tactical decision quality.

### PARTIAL

#### full turn/round lifecycle
Evidence is stronger than earlier passes: authoritative actor/phase ownership, START/COMMAND/ACTION/END transitions, lifecycle hooks, round history rotation, delayed-hit queue infrastructure, pending status skips and bounded status phase behavior all exist.

Still PARTIAL because the Java README continues to describe core battle state and semantic transcript parity as incomplete, and representative lifecycle hooks do not establish every feature/interrupt/delayed effect branch.

#### full stateful damage pipeline
Calculation primitives and selected runtime history/writeback exist, but the Java README still lists full damage resolution as unfinished.

#### status lifecycle
Now includes a reusable status-phase registry plus concrete Flinch and Strange Tempo/Confusion slices with Python parity. Still PARTIAL because this is representative coverage, not a complete status controller.

No inference rule:
`Flinch expiry works` does not mean `all status expiry/Save Checks/interactions work`.

#### move-specific behavior
Selected move slices exist and delayed-hit infrastructure has advanced, but there is no complete move registry or full BattleSpec -> BattleTranscript parity.

#### abilities
Selected Ability behavior such as Mega Launcher and Strange Tempo-related interaction has evidence. The whole Ability category remains PARTIAL.

#### items
Selected held-item behavior has parity evidence from earlier passes. The item registry remains incomplete.

### BLOCKING

#### complete movement including push/pull/knockback/interception/forced movement
The Java README still lists forced movement and reactions under unfinished battle-state work.

#### terrain/weather/hazards/zones/reactions
Base terrain movement cost is not a terrain/hazard engine. Dynamic zones, weather phases, hazards and reactions remain BLOCKING.

#### Trainer Features/perks
The Java README still lists perk and Trainer Feature hook registries as unfinished.

#### AI tactical policy
Legal choices exist. Scoring/policy over those choices is still explicitly unfinished.

#### Minecraft/Cobblemon/Craftics adapter/playback support
The Java repository remains a standalone rules library. Its README explicitly says it is not a Minecraft mod yet and that the adapter comes after a parity-safe vertical slice.

## Java README authority

The current README still lists these large items as unfinished:
- core combatant/grid battle state;
- full damage resolution;
- status controller, terrain, hazards, forced movement and reactions;
- move/ability/item/perk/Trainer Feature registries;
- semantic event emission and full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Narrative design must keep using the conservative family-level classification above even when individual slices land.

## Pass 35 encounter implications

### Archive Evacuation

FULL version needs:
- complete movement/interception/forced movement: BLOCKING;
- terrain/weather/hazards/zones/reactions for dynamic structural danger: BLOCKING;
- AI tactical policy for objective-aware enemies: BLOCKING;
- adapter/playback: BLOCKING.

REDUCED version can keep evacuation and archive selection outside the grid and use a stable legal encounter.

### Reunion Route Breakdown

If the route problem is resolved before combat, the battle can rely mostly on VERIFIED baseline categories plus whatever PARTIAL move/status/ability/item behaviors the chosen combatants legally require.

If the battlefield itself shifts during combat, terrain/hazard dependencies become BLOCKING.

### Legacy Exhibition

A standard legal exhibition can already use VERIFIED targeting, base movement, calculations and action economy. The selected Pokémon/Trainer build must still be checked against the PARTIAL move/status/ability/item families. Autonomous rival adaptation requires BLOCKING tactical AI.

## Family-layer non-inference

Nothing in the live battle engine adds mechanical meaning to human kinship.

Do not create:
- family/sibling combat bonuses;
- inherited Features;
- automatic shared initiative;
- guardian reactions;
- bloodline abilities;
- inherited Pokémon obedience;
- shared action economy.

If future PTU/Caelo sources explicitly define a relevant mechanical effect, it must receive its own engine contract and parity evidence.

## Current conclusion

Pass 35 can safely advance kinship, generational records, family archives, public legacy, household links and consent state as narrative/world data.

Combat-heavy family scenarios should continue using reduced versions until forced movement, hazards, objective-aware AI and Minecraft playback become real engine capabilities.
