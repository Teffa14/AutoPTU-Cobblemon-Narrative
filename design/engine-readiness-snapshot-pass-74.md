# Engine readiness snapshot — pass 74

Status: implementation evidence only. This document does not expand canon or mechanically authorize narrative content.

## Repositories inspected

Narrative writable destination:
- `Teffa14/AutoPTU-Cobblemon-Narrative`
- working branch: `agent/pass-53-evolution-life-stage`

Read-only engine evidence:
- `Teffa14/AutoPTU-Java` main at `4bab1de9abcc28dc1257af8ad7aa4b803dfaa9c3`
- `Teffa14/AutoPTU` main at `e4bb0ca38b7018710af476ce365d515a387de4e7`

Java head message:
`Execute canonical Trainer initiative slots`

The latest Java slice allows canonical initiative order to contain server-owned Trainer turns as well as Pokémon turns, validates actor identities fail-closed and freezes the relevant contract against Python. This strengthens the already-VERIFIED action-economy/initiative family. It does not add vertical movement, elevation, climbing, forest visibility or canopy hazards.

Java README still states that these broad areas remain incomplete:
- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Permanent capability classification

### VERIFIED

Targeting / footprints / range / LoS

Evidence: Java README marks range, areas, footprints, target anchors and line of sight complete for the documented 2D contracts.

Pass-74 non-inference: 2D LoS does not prove vertical LoS, foliage concealment, canopy visibility, height advantage or line tracing across elevations.

Base movement legality

Evidence: Java README marks Shift movement and Jump slices complete for their documented contracts, including Overland/Swim/Sky and fit predicates.

Pass-74 non-inference: this does not prove generic tree climbing, branch traversal, swinging, gliding between crowns, perch legality, falling or multi-level adjacency.

Core calculations

Evidence: PTU tables, calculation primitives, accuracy and combat-stat resolution are marked complete for their documented contracts.

Action economy / initiative

Evidence: typed turn flow, deterministic ordering and the latest canonical Trainer initiative-slot execution are parity-backed.

AI legal-action infrastructure

Evidence: deterministic legal `BattleChoice` generation exists for currently represented action types and geometry.

### PARTIAL

Full turn / round lifecycle

Many lifecycle slices exist, including initiative rollover and canonical Trainer/Pokémon slots, but the README does not claim complete BattleSpec -> BattleTranscript lifecycle parity.

Full stateful damage pipeline

Representative damage/Ability hooks exist; the README still lists the full pipeline as incomplete.

Status lifecycle

Specific statuses and phase infrastructure exist, but the controller is incomplete.

Move-specific behavior

Metadata and representative move behaviors exist; catalog-wide behavior remains incomplete.

Abilities

Multiple parity-tested Ability slices exist; the complete registry remains incomplete.

Items

Representative held-item behavior exists; catalog-wide item support is incomplete.

Trainer Features / perks

Representative Features and lifecycle infrastructure exist; catalog-wide support is incomplete.

### BLOCKING

Complete movement including push / pull / knockback / interception / forced movement

No current evidence promotes this family. For pass 74 it also includes the absence of a verified multi-elevation traversal contract.

Terrain / weather / hazards / zones / broad reactions

Java owns some semantic environment state for specific calculations, but terrain/hazards/reactions remain explicitly incomplete.

A tree, branch, canopy gap or foliage layer must not become PTU Terrain, cover, hazard or reaction source merely because Minecraft renders it.

AI tactical policy

Legal-action enumeration exists. Objective-aware choice for reach-exit, protect, withdraw, use-alternate-height or avoid-fall goals is not verified.

Minecraft / Cobblemon / Craftics adapter and playback

Still future work per Java README.

## Python-oracle evidence relevant to pass 74

Available project `battle_state.py` evidence shows:
- `forest` as a recognized terrain-context label;
- Naturewalk labels matched against terrain context;
- explicit Sky/Levitate/Swim/Burrow capability checks;
- specific named effects that can use forest/tree tiles, such as Forest Lord origins.

This proves narrow Python mechanics. It does not establish a generic arboreal traversal engine.

The project Pokédex material exposes explicit movement/capability fields, reinforcing that traversal must be capability-driven rather than inferred from species appearance or narrative behavior.

The primary Caelo corpus was not reliably retrievable during this pass. No new Caelo-specific climbing, falling, forest, elevation or canopy rule is claimed.

## Pass 74 encounter dependency matrix

### Canopy Bridge Failure

Full version requires:
- targeting/footprints/range/LoS: VERIFIED baseline; vertical LoS specifically unverified
- base movement legality: VERIFIED baseline
- complete movement / forced movement / interception: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full lifecycle: PARTIAL
- full stateful damage: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal actions: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version is viable earlier because route damage, evacuation and vertical access remain world state. Combat uses one stable static layer and does not simulate falling.

### Hollow Tree Care Call

Full version additionally needs reliable non-KO protection/withdrawal goals and any vertical traversal used by defenders or rescuers.

Reduced version keeps the cavity, patient/nest and care interaction outside battle. A defensive encounter can occur on one static ground/platform map.

### Gap Survey After Storm

Full version may eventually use multiple observation heights and a visibility system separate from geometric LoS.

Reduced version is primarily exploration/research. Any combat uses a frozen clearing with normal visibility and no invented foliage modifiers.

## Pass-74 blockers outside the permanent battle categories

BLOCKING: `FOREST_VERTICAL_UNIT_STATE`
No runtime service yet owns coarse persistent canopy/midstory/understory/floor structure.

BLOCKING: `PERSISTENT_TREE_IDENTITY`
Minecraft trees are not yet linked to durable tree entities with condition and provenance history.

BLOCKING: `CANOPY_GAP_HISTORY`
Gap creation, closure and regeneration need versioned world state.

BLOCKING: `TREE_CAVITY_STATE`
Cavity origin, size/height class, occupancy observations and condition are not yet persistent services.

BLOCKING: `BRANCH_CONNECTIVITY_GRAPH`
No server-owned graph currently represents natural crown-to-crown or maintained elevated connections.

BLOCKING: `VERTICAL_VISIBILITY_CONTEXT`
Current VERIFIED LoS is not a vertical visibility/concealment system.

BLOCKING: `FOREST_TO_COBBLEMON_PROJECTION`
No safe anti-exploit contract maps vertical habitat state to presentation/spawn behavior.

BLOCKING: `FOREST_TO_BATTLE_PROJECTION`
No validated adapter converts vertical forest world state into an immutable legal battle environment.

## Explicit non-inferences

- A Pokémon observed in a tree does not automatically have Sky, Levitate, Wallrunner, Naturewalk or enhanced Jump.
- Sky movement legality does not prove branch landing/perching or 3D pathing.
- Naturewalk matching in Python does not grant universal forest traversal.
- A Minecraft tree block does not establish cover, Rough Terrain, concealment or climbability.
- A canopy gap does not automatically create Sun/Weather/Terrain.
- A falling tree in world state does not create battle damage unless exact mechanics are validated.
- A cavity does not prove nesting, ownership, kinship or current occupancy.
- Upper-canopy absence at one observation point does not establish population absence.
- Latest Trainer initiative parity does not affect any forest/environment capability category.

## Next mechanical checks

1. Extract exact PTU/Caelo text for climbing, falling, Jump, Sky, Levitate, Wallrunner and Naturewalk (Forest).
2. Confirm whether PTU defines vertical range/LoS or elevation modifiers usable by AutoPTU.
3. Inspect Java movement architecture before designing any multi-elevation tactical format.
4. Keep world branch-connectivity graphs separate from battle movement graphs.
5. Define a future `visibility_context` independently from LoS before foliage or height affects perception.
6. Keep reduced forest encounters on one frozen tactical layer until those contracts exist.