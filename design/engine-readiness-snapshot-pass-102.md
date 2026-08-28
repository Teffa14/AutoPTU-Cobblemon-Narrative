# Engine Readiness Snapshot — Pass 102

Status: IMPLEMENTATION-READINESS EVIDENCE. This snapshot creates no PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 102 adds proposed continuity for road passenger services: taxis, fixed-route buses/shuttles, local carriers, hired rides and canon-approved Pokémon-assisted public transport.

Narrative baseline before Pass 102 writes: `7b5dd013657dd3b2983db1ac84f8693bbdf05686`.

The complete recursive Narrative repository inventory was inspected at baseline and returned `truncated=false`. Relevant content reviewed directly included Travel/Transport, Roads/Bridges, Transit Hubs, prior Aviation/PTU mount research, Performance and Care to avoid false gaps, and Pass 101 readiness.

## Live engine evidence

AutoPTU-Java head inspected: `df3833964e1ec7596791cf6f07dec08122598f68`.

Recent Java evidence includes #256, which moved the Intercept d20 check onto authoritative battle RNG, and #257, which preserves Python-oracle mutation ordering for Intercept attempts including failed attempts and resource mutation before the success branch.

This strengthens one Intercept orchestration path. It does not verify the whole `complete movement including push/pull/knockback/interception/forced movement` family. Competing reactions, broad knockback, every forced-movement source, environmental displacement, complete Move/Ability/Item/Trainer Feature integration, tactical objective policy and semantic Minecraft playback remain outside verified coverage.

AutoPTU Python head inspected: `1f5c99d51f8f823dd077653bdd756bc2f0edbf18`. Its current change guards Career training-preference browser-storage access. This is Career/client stability work and adds no tactical battle-family evidence.

No permanent capability category is promoted in Pass 102.

## PTU/Caelo transport boundary

Prior project research verified that PTU has individual movement capabilities and mounted-transport constraints. Species/type alone is not authority for passenger transport.

No inspected governing evidence establishes a general taxi/bus/road-vehicle subsystem, traffic simulation, vehicle combat, dispatch checks, collision rules, road-service capacity math, or public-Pokémon transit qualification.

Road passenger continuity therefore remains world state. Any tactical scene starts only after Ouros explicitly composes participants and a reviewed arena.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS` — verified for reviewed static arenas.

`base movement legality` — verified for ordinary static movement; does not create boarding, evacuation or route-protection semantics.

`core calculations` — verified primitives remain available; no road-vehicle semantics are implied.

`action economy/initiative` — verified typed action budget/order remains available.

`AI legal-action infrastructure` — verified legal-action enumeration; it does not choose service objectives or civilians.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement` — PARTIAL. Java #256/#257 strengthen Intercept RNG and mutation-order parity, but family-wide forced movement/reactions remain incomplete.

`full turn/round lifecycle` — PARTIAL.

`full stateful damage pipeline` — PARTIAL. No vehicle/collision/passenger damage is introduced by this pass.

`status lifecycle` — PARTIAL. Delay, panic, crowding or travel sickness are not PTU statuses unless governing rules explicitly say so.

`move-specific behavior` — PARTIAL. A Move cannot be generalized into driving, towing, clearing traffic or public transport work.

`abilities` — PARTIAL. An Ability does not automatically qualify a Pokémon for passenger service.

`items` — PARTIAL. Tickets, signs, vehicles and stop equipment are world objects unless authoritative item rules apply.

`Trainer Features/perks` — PARTIAL. No broad driving/dispatch/transit Feature family is established.

### BLOCKING

`terrain/weather/hazards/zones/reactions` — BLOCKING for live traffic, vehicle hazards, moving roadsides, generalized protective reactions or dynamic service-area hazards.

`AI tactical policy` — BLOCKING for withdrawal, route protection, territorial retreat, civilian avoidance and service-area objectives.

`Minecraft/Cobblemon/Craftics adapter/playback support` — BLOCKING for authoritative service/run/stop bindings and semantic battle presentation.

## Encounter readiness

### Stop Evacuation Withdrawal

Full intended form requires protective withdrawal, multiple routes, Intercept/forced movement, generalized reactions, objective-aware AI and playback; live traffic/work zones additionally require the environmental family.

Current profile: REDUCED.

Safe form: suspend service first; remove passengers, staff, vehicles and nonparticipant Pokémon; Ouros selects combatants; AutoPTU receives a static roadside arena. Victory secures only the immediate area. Service restoration remains a world-state decision.

### Disabled Shuttle Perimeter

Full intended form may require protected routes, reactions, forced movement, hazards/zones, objective-aware AI and playback.

Current profile: REDUCED.

Safe form: Maintenance isolates the disabled asset and removes workers before battle. The asset is not a tactical target. Victory only restores access for later diagnosis; no repair or service restart is inferred.

### Rerouted Pickup Conflict

Full intended form may require reviewed terrain, route-protection/withdrawal objectives, reactions and tactical AI.

Current profile: REDUCED.

Safe form: passengers remain outside the tactical area, service is suspended at the pickup during combat, and Ouros sends only explicit combatants to a static arena. A separate operational review decides whether pickup resumes.

## Noncombat readiness

Usable immediately as proposed narrative state:
- persistent services and stops;
- fixed-route and request-based patterns;
- run/dispatch lifecycle;
- delayed, rerouted, short-turned and cancelled service history;
- temporary stop relocation;
- passenger boarding/alighting provenance;
- dependency-driven suspension;
- recurring operators and passengers;
- service restoration in stages;
- stale notices versus current service truth;
- ecology/infrastructure consequences without invented mechanics.

## Minecraft/Cobblemon consequence

Binding architecture remains:

`Ouros world/service state -> explicit encounter composition -> AutoPTU authoritative BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Safe presentation reuse includes roads, stops, shelters, signs, barriers, decorative vehicles where available, Pokémon models/forms/poses/animations/cries, NPCs, sounds, particles, UI, networking, tracking and persistence hooks.

Adapter work is required for stable service/stop/run identity, boarding/alighting intent, authoritative state projection, entity/world-record binding, arena conversion and semantic playback.

Minecraft/Cobblemon must never decide that:
- a run completed because an entity moved;
- a passenger boarded because entities are close;
- a Pokémon is a worker because it stands at a stop;
- a species can carry passengers because its model allows riding;
- a service restarted because redstone or pathfinding works;
- a collision caused PTU damage;
- everyone at a stop is a combatant;
- Cobblemon BattleState/controller logic owns combatant selection or battle truth.

## Readiness conclusion

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

- Which road passenger services exist in Ouros and in which regions?
- Which service forms are public, cooperative, private, institutional or informal?
- Which road-vehicle technologies, if any, exist?
- Are any public services Pokémon-powered, and which exact individuals/roles are canon-approved?
- Who defines stops, schedules and public service information?
- How are accessibility, privacy, fares and denied boarding handled culturally/institutionally?
- Which services connect small settlements that lack rail/air/port infrastructure?

## Unresolved mechanical questions

- exact PTU/Caelo mounted-transport requirements for any proposed individual Pokémon service worker;
- whether any governing source defines road vehicles, driving or passenger capacity;
- boarding/alighting during tactical time, if ever needed;
- vehicle collision/crash/towing mechanics, if ever adopted;
- traffic or moving-vehicle hazards;
- whether any Move/Ability/Item/Trainer Feature can explicitly support road passenger operations;
- adapter handling for moving transport presentation without giving Minecraft battle authority.

No answer is invented by this snapshot.