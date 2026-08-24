# Engine Readiness Snapshot — Pass 148

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-24

## Live revisions inspected

AutoPTU-Java main: `52f9194e47cae95e36165b6606f7a88cf430669d` — `Add generic PRE-damage follow-up move seam (#176)`.

Immediately preceding relevant Java slices include Sway, Parry and Perception/Perception Errata PRE-damage reaction contracts. The new #176 seam exposes a runtime-owned synchronous follow-up Move request/result path to PRE-damage hooks. This is useful evidence about reaction ordering and authoritative ownership. It does not prove the full reactions family, complete movement or the complete Move/Ability/Feature catalog.

AutoPTU Python main: `e1feb915fe3497cd099a0b447212755300dff1d8` — `Career: require club selection before decisions (#86)`.

The inspected recent Python changes remain Career/state-resilience work and do not justify a tactical capability promotion.

The AutoPTU-Java README still states that the Python implementation remains authoritative while the Java port is incomplete and explicitly lists full combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, full transcript parity, AI scoring/policy and Minecraft/Cobblemon integration as unfinished families.

## Permanent capability classification

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

### BLOCKING as complete families

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter / playback support

The recent PRE-damage reaction contracts and follow-up seam add meaningful evidence inside the reactions/lifecycle/move-specific area. They do not promote `terrain/weather/hazards/zones/reactions` as a complete family. Likewise, a reaction that moves one actor under a frozen contract does not promote complete movement.

## Pass 148 encounter dependency map

### Lost Hiker at Marker Seven — FULL

Requires:
- complete movement: BLOCKING
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- terrain/weather/hazards/zones/reactions: BLOCKING only when a tactical environmental effect is part of the incident

The currently verified targeting/base movement/action-space infrastructure is insufficient for search, escort and non-hostile objective behavior.

### Lost Hiker at Marker Seven — REDUCED

Search, route knowledge, missing-person state and escort are resolved by overworld authorities. If combat remains, a static battle can use verified targeting/base movement/core calculations/action economy/legal-action infrastructure. It still inherits the normal PARTIAL state of lifecycle, full damage, statuses, Moves, Abilities, Items and Trainer Features whenever those specific rules are exercised.

### Rescue at the Vanished Ford — FULL

Requires:
- complete movement: BLOCKING
- terrain/weather/hazards/zones/reactions: BLOCKING for changing water/current/mud or tactical crossing effects
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

### Rescue at the Vanished Ford — REDUCED

Freshwater/River Geomorphology/Travel/Wayfinding resolve the safe crossing before battle. The battle gets a frozen static geometry. No current, drowning, mud, falling or forced movement is invented.

### Wildlife Crossing at Temporary Detour — FULL

Requires:
- complete movement: BLOCKING
- AI tactical policy: BLOCKING for CROSS/WITHDRAW/non-hostile route behavior
- adapter/playback: BLOCKING
- terrain/weather/hazards/zones/reactions only if the protected corridor has an actual verified tactical effect

### Wildlife Crossing at Temporary Detour — REDUCED

Wildlife/civilians move outside the grid first. AutoPTU only receives a static independent confrontation.

### Signage Dispute

No battle dependency by default. It depends on persistent Wayfinding, Travel, Cartography, Languages, Accessibility and maintenance-record state. It can remain unresolved.

## New overworld blockers introduced by Pass 148

- `WAYFINDING_NETWORK_STATE`
- `JUNCTION_IDENTITY_HISTORY`
- `GUIDANCE_ASSET_HISTORY`
- `ROUTE_GUIDANCE_REVISION`
- `LANDMARK_IDENTITY_HISTORY`
- `DETOUR_NOTICE_STATE`
- `NAVIGATION_OBSERVATION_LEDGER`
- `NAVIGATION_ATTEMPT_HISTORY`
- `ACTOR_ROUTE_KNOWLEDGE`
- `GUIDANCE_CONFLICT_CASES`
- `WAYFINDING_TO_MINECRAFT_PROJECTION`
- `WAYFINDING_TO_BATTLE_HANDOFF`

## Explicit non-inferences

- Verified battle LoS is not route-finding or landmark visibility.
- Verified Shift legality is not route knowledge, navigation, escort or pathfinding AI.
- A generic PRE-damage reaction seam is not a generic overworld reaction system.
- Sway/Parry/Perception contracts do not prove push/pull/interception/forced movement as a complete family.
- A Survival or Perception rule name in PTU data does not prove a Java runtime navigation subsystem.
- Minecraft signs, maps, coordinates and entity paths are not authoritative route guidance.
- Loaded Cobblemon movement does not prove population route knowledge or safe access.
- A missing marker does not create a hazard Status or mechanical penalty.

## PTU/Caelo source status

The file-library search in this run did not recover a reliable primary Caelo navigation passage. No generic navigation DC, lost condition, map modifier, compass rule or route-familiarity mechanic is claimed.

Super PTU Online Helper was not available as an invocable capability in this runtime.

## Questions to resolve before implementation

1. Exact PTU/Caelo handling of Survival/Perception for navigation and getting lost.
2. Whether route familiarity has any rules expression or remains purely Chronicle/world knowledge.
3. How player-published route guidance is moderated and versioned.
4. How guidance visibility is projected without turning Minecraft renderer state into authority.
5. Whether objective-aware search/escort belongs in tactical AI or should remain an overworld concern for most encounters.
6. Which regional marker traditions and maintaining institutions are canon in Ouros.
