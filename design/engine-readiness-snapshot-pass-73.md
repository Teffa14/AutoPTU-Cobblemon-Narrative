# Engine readiness snapshot — pass 73

Status: implementation evidence only. This document does not expand canon or mechanically authorize narrative content.

## Repositories inspected

Narrative writable destination:
- `Teffa14/AutoPTU-Cobblemon-Narrative`
- working branch: `agent/pass-53-evolution-life-stage`

Read-only engine evidence:
- `Teffa14/AutoPTU-Java` main at `fe572021445fa0aa862db17514ca2b7e2cff3b18`
- `Teffa14/AutoPTU` main at `e4bb0ca38b7018710af476ce365d515a387de4e7`

Java head message:
`Project canonical Trainer initiative entries from runtime state`

The new Java slice stores/derives canonical Trainer initiative profile from runtime state and tests the authoritative projection. This strengthens the already-verified action-economy/initiative family. It does not provide desert, drought, dust, weather or terrain simulation.

Java README continues to list these major incomplete areas:
- core combatant/grid battle state expansion;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Permanent capability classification

### VERIFIED

Targeting / footprints / range / LoS

Evidence: Java README marks targeting range, areas, footprints, target anchors and line of sight complete.

Important non-inference for pass 73: LoS is geometry. It does not prove visibility penalties from dust, glare or darkness.

Base movement legality

Evidence: Java README marks Shift movement legality and Jump movement slices complete for their documented contracts.

Important non-inference: base movement does not prove loose-sand slowdown, dunes, quicksand, dust navigation or desert survival.

Core calculations

Evidence: PTU tables, calculation primitives, accuracy and combat-stat resolution are marked complete for their documented contracts.

Action economy / initiative

Evidence: typed turn flow, deterministic initiative ordering and the newer runtime-state initiative projection are parity-backed.

AI legal-action infrastructure

Evidence: deterministic autobattler action-space contract exists for currently represented legal choices.

### PARTIAL

Full turn / round lifecycle

Many lifecycle slices exist and initiative is increasingly authoritative, but the Java README still does not claim complete BattleSpec -> BattleTranscript lifecycle parity.

Full stateful damage pipeline

Several damage/Ability slices exist, but the Java README still lists the full damage pipeline as incomplete.

Status lifecycle

There is substantial status-phase infrastructure and specific statuses/Abilities, but the controller is not complete.

Move-specific behavior

Move metadata/contracts and representative behaviors exist; catalog-wide behavior is not complete.

Abilities

Representative Ability pipelines and parity-tested Abilities exist; the full registry is not complete.

Items

Representative held-item state/behavior exists from earlier slices; catalog-wide items remain incomplete.

Trainer Features / perks

Lifecycle infrastructure and representative Features exist; catalog-wide runtime mapping remains incomplete.

### BLOCKING

Complete movement including push / pull / knockback / interception / forced movement

No evidence promotes this family. Rich route/escape encounters must not depend on it unless a future slice verifies the required behavior.

Terrain / weather / hazards / zones / broad reactions

Java now owns some semantic environment state used by specific calculations, but the README still explicitly lists terrain, hazards and reactions as incomplete.

For pass 73 this family is the main tactical blocker. Drought, desert, dust or heat must never be converted automatically into battle Weather/Terrain.

AI tactical policy

Java can enumerate legal actions. It does not yet prove objective-aware tactical policy for retreat, refuge access, protection or route-clear goals.

Minecraft / Cobblemon / Craftics adapter and playback

Java README explicitly states it is not a Minecraft mod yet and the adapter is future work.

## Python-oracle evidence relevant to pass 73

Uploaded `battle_state.py` contains concrete START-phase Sandstorm behavior. In the inspected implementation, effective sand weather applies one Tick of damage to non-Ground/Rock/Steel combatants unless explicit Ability/effect protections apply. Named branches include Desert Weather, Sand Force, Sand Rush, Sand Veil, Sand Stream and Overcoat.

This proves an exact Python battle behavior. It does not prove Java parity for the whole Weather family and does not authorize overworld drought/dust to create Sandstorm.

The same Python file contains Wilderness Guide. Its desert/tundra branch grants explicit temporary weather-related effects under the actual Trainer Feature. This is evidence for that Feature in the oracle, not a generic desert-travel rule.

## Pass 73 encounter dependency matrix

### Ephemeral Basin Survey

Full version requires:
- targeting/range/LoS: VERIFIED
- base movement: VERIFIED
- complete movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- damage: PARTIAL
- statuses: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal actions: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced version is viable earlier because water phase, samples and wildlife movement remain world state and battle geometry is frozen before AutoPTU starts.

### Dust Road Closure

Full version additionally needs a visibility context separate from LoS. No verified Java contract currently proves dust visibility or Accuracy/Evasion consequences.

Reduced version keeps dust as route/world presentation and uses normal visibility inside any static battle.

### Refuge Waterhole Conflict

Full version needs non-KO goals, route/access decisions and objective-aware AI. Those are blocked mainly by complete movement, zones/reactions and tactical policy.

Reduced version resolves access and noncombatant movement outside AutoPTU, then opens a conventional battle only for actual combatants.

## Aridity-specific blockers outside the permanent battle categories

BLOCKING: `ARID_LANDSCAPE_STATE`
Persistent regional/subregional identity and version history do not yet exist as runtime services.

BLOCKING: `DROUGHT_DRYNESS_REVISION`
Ouros needs baseline-aware drought/dryness state that remains separate from Weather.

BLOCKING: `EPHEMERAL_WATER_STATE`
Pools, temporary channels and seasonal water need coarse persistent phases independent of Minecraft water blocks.

BLOCKING: `DROUGHT_REFUGE_STATE`
Scarce water/refuge pressure needs world-state ownership and provenance.

BLOCKING: `DUST_SOURCE_EVENT_GRAPH`
Dust source hypotheses, footprint versions and transport path need explicit data.

BLOCKING: `ARID_PHENOLOGY_WINDOW`
After-rain or seasonal biological windows need time-bounded state without guaranteeing spawns.

BLOCKING: `ARIDITY_TO_COBBLEMON_PROJECTION`
No safe anti-exploit contract exists for translating dryland/ecological state into spawn presentation.

BLOCKING: `ARIDITY_TO_BATTLE_PROJECTION`
No validated adapter currently converts world dryland state into an immutable PTU battle environment snapshot.

## Explicit non-inferences

- Weather data structures do not mean full Weather behavior is VERIFIED.
- A Java initiative resolver reading Weather/Terrain does not mean Weather/Terrain systems are complete.
- Python Sandstorm damage does not mean an overworld dust storm is PTU Sandstorm.
- Ground/Rock/Steel Sandstorm immunity does not imply immunity to environmental heat, dehydration or dust inhalation.
- Sandile/Trapinch/Hippopotas species lore does not grant Burrow, Arena Trap, group tactics or surprise mechanics unless authoritative state supports them.
- A Minecraft desert biome does not define PTU Terrain.
- A visible dry water block does not establish drought.

## Next mechanical checks

1. Extract exact PTU/Caelo Sandstorm Weather text and any Caelo modifications.
2. Extract Desert Weather, Naturewalk (Desert), Survival/harsh-environment guidance and any dehydration/heat rules.
3. Inspect Java `BattleEnvironmentState` and Weather consumers when a true Weather port slice lands.
4. Keep visibility separate from LoS when dust/light systems reach the adapter.
5. Do not promote the environment family from representative initiative modifiers.
