# Engine Readiness Snapshot — Pass 37

Status: read-only evidence snapshot for narrative design. No changes are made to AutoPTU-Java or AutoPTU.
Date: 2026-08-19

## Repositories inspected

AutoPTU-Java head: `5860d75dd4690a9244269aea70e343cba0005755`

Python AutoPTU head: `e4bb0ca38b7018710af476ce365d515a387de4e7`

The latest Java work since Pass 36 adds two bounded pieces of parity-backed lifecycle infrastructure:

1. an ordered Ability phase registry with a concrete Lancer END-phase behavior frozen against Python;
2. a combatant phase-effect dispatcher that preserves Python's broad execution order: STATUS -> ABILITY -> PERK, including the single pending-status-skip replacement semantics.

These are meaningful architectural advances. They still do not prove complete coverage of Abilities, statuses, perks/Trainer Features or lifecycle.

No-inference rules:
- Lancer phase parity does not prove the Ability family.
- The Ability phase registry does not prove non-phase Ability triggers.
- STATUS -> ABILITY -> PERK ordering does not prove all three family implementations.
- The presence of a PERK slot does not mean Trainer Features/perks are ported.
- Generic hook infrastructure does not prove semantic correctness for unported rules.

The AutoPTU-Java README still lists core battle state, full damage, status controller, terrain/hazards/forced movement/reactions, complete registries, tactical AI and Minecraft/Cobblemon/Craftics integration as unfinished.

The latest Python AutoPTU commits inspected are Career/API work. They do not change the tactical capability classification used here.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

Caveats:
- verified base movement does not include push/pull/knockback/interception/forced movement;
- core calculation primitives do not equal the full stateful damage pipeline;
- legal action enumeration does not imply tactical decision quality.

### PARTIAL

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items

Lifecycle evidence is stronger than Pass 36 because Java now owns cross-family phase-effect ordering and an ordered Ability phase registry on top of existing actor/phase state, phase transitions, cleanup/history rotation, delayed-hit infrastructure, status phase hooks and pending skip semantics.

Status evidence remains bounded: Flinch, expiry, metadata, status application prevention, Strange Tempo/Confusion and generic phase/application registries do not establish all statuses or Save Check interactions.

Ability evidence now includes several representative slices plus the new Lancer phase behavior and generic phase registry. The category remains PARTIAL.

Items remain PARTIAL based on prior held-item representative slices; no new evidence in this pass promotes the family.

### BLOCKING

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- Trainer Features/perks
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

The new phase dispatcher includes a PERK family position, but that is orchestration infrastructure, not proof that Trainer Features/perks are implemented. Therefore the permanent category remains BLOCKING.

## Pass 37 mortality boundary

Pass 37 must not use battle state as a death oracle.

Current read-only Python evidence contains explicit distinctions among Fainted state, HP and Injury-driven Features. For example, False Strike can leave a fainted wild target at 1 HP, and Perseverance can prevent a triggering Injury gain. Those bounded mechanics reinforce that Fainted/HP/Injury are independent mechanical concepts.

This snapshot does not establish the exact PTU/Caelo rule that converts any mechanical state into confirmed death.

Therefore:
- Fainted -> DECEASED_CONFIRMED is forbidden.
- Injury -> DECEASED_CONFIRMED is forbidden.
- 0 HP -> DECEASED_CONFIRMED is forbidden without an explicit governing rule result.
- battle transcript absence -> death is forbidden.

Narrative mortality state can advance only from authored canon, human canon review, or a future authoritative mechanical death output whose governing PTU/Caelo rule and parity path are explicit.

## Pass 37 encounter dependencies

### Memorial Garden Night Disturbance

FULL version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING when protection/escape positioning matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING for mechanical fog, fragile zones or changing site effects
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — BLOCKING as a complete family
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version: investigate in overworld; use a cleared static arena for any battle; keep memorial beds/markers outside tactical interaction; update world damage only through explicit world-state actions.

### Cemetery Perimeter Evacuation

FULL version depends on:
- objective handling for protect/clear-route/withdraw;
- complete movement/interception/forced movement;
- AI tactical policy;
- Minecraft playback;
- terrain/hazards if the evacuation danger is mechanical.

Those requirements remain BLOCKING.

REDUCED version: evacuate visitors through overworld logic before combat; execute a normal static battle with combatants only.

### Old Tower Night Watch

FULL version may depend on:
- dynamic light/visibility zones;
- interactable objectives;
- objective-aware AI;
- phase-driven environmental effects;
- Minecraft state playback.

Those requirements remain BLOCKING unless the authored version removes them.

REDUCED version: lights, doors, switches and observation remain overworld state; AutoPTU receives a fixed legal map and standard battle when needed.

## Ghost / supernatural non-inference

Nothing in the current Java capability evidence authorizes a narrative conclusion that a Ghost-type combatant is a deceased spirit.

A Ghost Pokémon remains a Pokémon entity with authoritative species/Ability/Move state.

Any `postmortem_claim` is a narrative evidence object unless a separately authored canon fact or governing mechanic proves identity.

Do not implement "spirit damage", "exorcism", possession, afterlife travel, resurrection or soul-state effects as encounter mechanics unless the corresponding PTU/Caelo rule family is explicitly extracted and ported.

## Conclusion

Pass 37 can safely advance mortality truth boundaries, missing-versus-deceased separation, memorial site state, remembrance actions, stewardship, public markers, survivor-Pokémon custody questions and Ghost-ecology separation entirely as narrative/world state.

The new Java phase-family infrastructure strengthens lifecycle architecture, but it does not change the permanent capability classification. Rich tactical memorial encounters should continue using reduced forms until movement objectives, dynamic hazards/zones, complete Trainer Feature hooks, tactical AI and Minecraft playback are parity-safe.
