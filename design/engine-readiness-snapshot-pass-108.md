# Engine Readiness Snapshot — Pass 108

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `063bc4b6179483a0f9825cd3882d9d861d866908`

Latest inspected slice: `Compose Trainer Feature execution transaction (#142)`, committed 2026-08-22. Java now composes the generic Trainer Feature dispatch transaction in Python order: enabled/trigger checks, prerequisites, context, frequency, resources, concrete effect callback, resource consumption, then usage/cooldown mutation. The service explicitly keeps concrete Feature effect semantics behind an injected `FeatureEffect` implementation.

This materially strengthens the Trainer Features/perks infrastructure. It does not prove execution of the Feature catalog, target scopes, interrupts, movement effects, environmental effects, social effects or any specific Feature required by a narrative encounter.

AutoPTU `main`: `e386f3fe9eb83e181be77b1e2869459cdeff78d6`

Recent Python commits inspected in this run are Career/deployment/persistence oriented and do not justify changing the tactical capability map.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## Evidence discipline

The current Java README still lists core combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, full transcript parity, tactical AI and Minecraft/Cobblemon integration as unfinished.

Representative implementation remains representative only.

Specific non-inferences from the latest Java slice:
- a transactional Trainer Feature dispatcher does not prove any concrete Feature effect;
- generic resource/usage handling does not prove AP semantics unless the concrete path is tested;
- a Feature that later grants movement still depends on the relevant complete-movement family;
- a Feature that later creates terrain, Weather, hazards, zones or reactions still depends on that family;
- a Feature that changes AI priorities does not prove tactical policy;
- a Feature event cannot be rendered authoritatively in Minecraft until the adapter/playback contract exists.

## Pass 108 encounter dependency map

### Boundary Survey at Alder Field — FULL

Narrative objective:
Resolve a fresh survey while displaced wild Pokémon use the same corridor and several archived boundary descriptions disagree.

Requires:
- targeting / footprints / range / LoS: VERIFIED for ordinary combat targeting
- base movement legality: VERIFIED for ordinary static movement
- complete movement including interception / forced movement: BLOCKING if the encounter preserves a moving corridor, interception lane or dynamic withdrawal
- core calculations: VERIFIED
- action economy / initiative: VERIFIED
- full turn / round lifecycle: PARTIAL for combatants that use lifecycle-dependent effects
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when statuses are present
- terrain / weather / hazards / zones / reactions: BLOCKING only if an exact validated field effect enters the battle
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features / perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `CLEAR_ROUTE` or `PROTECT_SURVEY_GEAR`
- Minecraft / Cobblemon / Craftics adapter/playback: BLOCKING

Reduced version:
- resolve survey work and wildlife movement in overworld state;
- move surveyors/noncombatants to safety;
- freeze one static legal arena;
- open AutoPTU only for the actors/Pokémon actually remaining in conflict;
- preserve survey evidence separately from battle outcome.

A victory never decides the canonical boundary.

### Shared Meadow Waterpoint — FULL

Narrative objective:
Multiple legitimate seasonal users and wild Pokémon converge on the same waterpoint after a route disruption changes timing.

Requires:
- complete movement including interception / forced movement: BLOCKING for moving managed herds, crossing lanes or withdrawals
- terrain / weather / hazards / zones / reactions: BLOCKING only if water or ground has an exact validated tactical effect
- AI tactical policy: BLOCKING for `CROSS`, `WITHDRAW`, `PROTECT` or objective-aware de-escalation
- Minecraft/Cobblemon/Craftics playback: BLOCKING
- ordinary targeting, base movement, calculations and action economy remain usable at VERIFIED scope
- any concrete Move/Ability/Item/Feature remains independently gated by its PARTIAL family

Reduced version:
- resolve scheduling and temporary use arrangements in world state;
- resolve managed-herd and wild-population positions before battle;
- open AutoPTU only if a distinct confrontation remains;
- do not translate land-use priority into combat bonuses.

### Utility Corridor Reopening — FULL

Narrative objective:
A maintenance team has a narrow authored access permission through land otherwise closed during a conservation window.

Requires:
- complete movement / interception / forced movement: BLOCKING for a true escort corridor
- AI tactical policy: BLOCKING for `REACH_OBJECTIVE`, `PROTECT`, `WITHDRAW` or corridor-preservation behavior
- Minecraft/Cobblemon/Craftics playback: BLOCKING
- terrain/weather/hazards/zones/reactions: BLOCKING only if the authored site has a mechanically validated field effect
- ordinary static combat primitives remain available at their current VERIFIED/PARTIAL scopes

Reduced version:
- validate the scoped access permission before entry;
- move technicians and equipment in overworld state;
- freeze one static arena if a battle genuinely occurs;
- resume maintenance only when battle/world state permits it afterward.

## New overworld blockers introduced by Pass 108

These belong outside AutoPTU-Java:

- `LAND_UNIT_IDENTITY`
- `LAND_BOUNDARY_REVISION_HISTORY`
- `BOUNDARY_OBSERVATION_PROVENANCE`
- `TENURE_RELATIONSHIP_STATE`
- `LAND_ACCESS_POLICY`
- `PASSAGE_PERMISSION_STATE`
- `COMMON_USE_AREA_STATE`
- `LAND_RESOURCE_USE_GRANT`
- `LAND_USE_PROFILE_HISTORY`
- `LAND_CLAIM_GRAPH`
- `LAND_ACCESS_CONTROL_PROJECTION`
- `LAND_TO_HOMES_HANDOFF`
- `LAND_TO_TRAVEL_HANDOFF`
- `LAND_TO_AGRICULTURE_FORESTRY_FISHERIES_GEOLOGY_HANDOFF`
- `LAND_TO_CONSERVATION_PUBLIC_WORKS_HANDOFF`
- `LAND_TO_MINECRAFT_PERMISSION_PROJECTION`
- `LAND_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 108

Do not infer:
- occupancy -> ownership;
- residence -> ownership or transfer authority;
- stewardship -> ownership;
- ownership claim -> unlimited authority;
- public access -> public ownership;
- common use -> open access to everyone;
- passage -> permission to harvest, build, fish, camp or enter nearby structures;
- mapped line -> canonical boundary;
- fence, sign or gate -> valid claim;
- open Minecraft door -> valid access permission;
- block placement -> ownership of the ground;
- long occupancy -> automatic ownership;
- historical use -> current authority;
- farm status -> Grassy Terrain or battle bonus;
- forest-use permission -> Naturewalk;
- road access -> movement bonus;
- water access -> Swim capability;
- boundary dispute -> criminal status;
- land relationship -> ownership of wild Pokémon;
- conservation designation -> capture legality or battle status;
- a successful battle -> resolution of a land claim.

## Current Trainer Feature evidence

The Java Trainer Feature sequence now has parity-backed primitives for:
- prerequisite gates;
- context gates;
- frequency/cooldown gates;
- generic resources;
- usage/cooldown bookkeeping;
- transaction ordering around an injected concrete effect.

This is stronger than Pass 107 and should be cited by future narrative passes when deciding whether generic Feature execution infrastructure exists.

The permanent family remains PARTIAL because:
- concrete effect coverage is incomplete;
- target scopes are not universally demonstrated;
- effect-specific mechanics still rely on other incomplete families;
- catalog coverage is not established;
- Minecraft semantic playback is absent.

## Mechanical/canon questions still unresolved

- Does Ouros have a region-wide concept analogous to land ownership, or only institution-specific use/occupancy relationships?
- Which settlements or institutions maintain authoritative boundary records?
- Which shared-use areas exist before campaign start?
- Can clubs, businesses or player groups receive scoped land-use permissions?
- Who may authorize temporary access during emergencies?
- How should shoreline, river and road movement interact with old boundaries?
- What is the canon relationship between long residence, inheritance and succession if those systems are later authored?
- Which resource uses require explicit permission?
- How should Minecraft expose boundaries without interrupting routine exploration with constant permission UI?
- Which exact PTU/Caelo rules govern physical land alteration through Moves, Capabilities or Trainer Features?
- Should any battle ever include a tactically protected passage/access zone, or should land access normally be resolved before combat?

The full primary Caelo corpus was not reliably accessible during this run. Super PTU Online Helper was not exposed as an invokable capability. No rule claims were invented from either source.
