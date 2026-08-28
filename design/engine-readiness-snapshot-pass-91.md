# Engine Readiness Snapshot — Pass 91

Status: implementation evidence snapshot, not canon.
Date: 2026-08-28

## Scope

Supports:
- `design/railway-operations-stations-network-continuity-extension.md`;
- `proposals/2026-08-28-railway-operations-network-seeds-91.md`.

Writable repository:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Internal project review

Before Pass 91, the complete recursive Narrative tree was inspected at head `ffc05aecf950793cc9c9d20f1b985d7c692a1f3b`; GitHub reported `truncated=false`.

Direct overlap review included:
- Travel/Transport/Expedition;
- Transit Hubs/Passenger Cohorts;
- Technology/Energy/Infrastructure;
- Facility Maintenance;
- Infrastructure Outage/Restoration;
- Public Notices;
- Interregional Mobility;
- Workplaces/Pokémon Work;
- Conservation;
- Cobblemon Runtime Authority Boundary;
- Pass 90 readiness evidence.

No rail-specific continuity layer existed. Travel already allowed rail/transit only when canon supports it, while Transit Hubs focused on passenger scenes. Pass 91 therefore owns only rail-specific operational topology and history and delegates all broader responsibilities to existing systems.

## Binding runtime authority

Ouros owns:
- whether any railway exists in canon;
- rail corridor/station/service world state;
- network revisions;
- explicit encounter composition;
- route/service consequences outside battle;
- which observed Pokémon become encounter participants.

AutoPTU owns:
- combatants and teams;
- target/action legality;
- tactical positions/movement;
- initiative/action economy;
- HP, statuses, stages and temporary effects;
- damage/healing;
- Moves, Abilities, Items and Trainer Features;
- Push/Pull/knockback/Intercept/forced movement/reactions;
- tactical AI;
- authoritative battle result.

Minecraft/Cobblemon/Craftics may present/adapt:
- stations, tracks, vehicles and platforms;
- lights/signs/doors/barriers/control panels;
- NPC/Pokémon models, forms, poses, animations and cries;
- particles/sounds;
- UI/networking/synchronization;
- timetable/notice projection;
- reviewed world interaction hooks;
- semantic playback of AutoPTU results.

Required direction:
`Ouros rail/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`.

Forbidden shortcuts:
- nearby Cobblemon entities becoming combatants automatically;
- Cobblemon BattleState/controller deciding participants or tactical state;
- Minecraft minecart/redstone physics deciding canonical rail service;
- moving train visuals creating automatic collision damage, forced movement or hazards;
- track power visuals creating PTU electricity effects.

## PTU/Caelo boundary

Pass 91 creates no:
- train-driving Skill;
- signalling Skill;
- railway Technology Education DC;
- vehicle speed/capacity calculation;
- braking-distance system;
- derailment/collision damage;
- moving-platform battle rules;
- boarding/disembarking combat action;
- train-car HP;
- powered-rail hazard;
- fare/pass price;
- Pokémon-powered traction formula;
- conductor/engineer Trainer Feature.

Exact mechanics require governing PTU/Caelo source review and implementation evidence. PTR2/PTR material surfaced in public search is not a governing rules source for this project.

## Live revisions inspected

AutoPTU-Java `main`:
`62108bb23fbaee3d64a0af50c6ae8581cfbedb60`

Latest relevant Java change:
`Fix intercept cleanup first-family semantics (#252)`

No newer Java tactical commit was present during Pass 91.

AutoPTU Python `main`:
`f4ecbc0e2c2c346883fbe3e57c7dccd70076f510`

Latest change:
`Career: fail closed when saved Full FX startup raster is unknown`

Recent Python changes after Pass 90 concern Career renderer/raster safety. They do not establish a new tactical capability family.

## Java evidence carry-forward

#252 remains the newest inspected Java slice. It corrects authoritative Intercept candidate cleanup to match Python first-family temporary-effect removal semantics and keeps cleanup in server-owned battle runtime state. Minecraft/Cobblemon does not perform this cleanup.

Earlier current slices still provide concrete evidence for:
- Shift/Jump movement legality;
- Push/Pull forced displacement;
- collisions, bounds and partial stops;
- position mutation;
- Intercept attempt policy;
- eligibility;
- check resolution;
- attack-line geometry;
- reaction movement commitment;
- a melee Intercept + Push 1 composition;
- candidate discovery/materialization from server-owned state/content;
- discovery-related expiry cleanup.

This remains substantial but incomplete evidence for the broad movement family.

## Permanent capability map

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Pass 91 makes no family-level promotion.

## Why complete movement remains PARTIAL

Positive evidence covers several real Push/Pull and Intercept slices.

Still missing for VERIFIED:
- broad live Intercept trigger integration;
- competing-reaction ordering/conflict resolution;
- complete knockback coverage;
- every forced-movement source;
- broad Move/Ability/Item/Trainer Feature integration;
- environment-driven displacement;
- moving-platform/vehicle interaction if ever required;
- complete semantic transcript events;
- tactical AI handling;
- Minecraft playback.

A railway encounter therefore cannot assume that a passing vehicle, platform edge or moving door produces tactical displacement.

## Why terrain/weather/hazards/zones/reactions remains BLOCKING

Railway full encounters might eventually want:
- track exclusion zones;
- electrified or powered infrastructure;
- moving-vehicle danger;
- narrow-edge/fall consequences;
- smoke/steam/weather visibility;
- interactable gates or signals during battle;
- reactions around protected workers;
- environment-driven damage or movement.

None of those are established family-wide. They stay visual/world/static state in reduced encounters.

## Encounter capability profile — Trackside Withdrawal

Full dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:
- isolate the rail section in world state;
- stop all train movement before battle;
- remove workers/equipment from the grid;
- exclude unsafe geometry through static map design;
- let Ouros choose exact combatants;
- run a static AutoPTU encounter;
- resume inspection/reopening afterward.

## Encounter capability profile — Station Concourse Evacuation

Full version additionally wants civilian withdrawal, multiple exits, CLEAR_ROUTE/WITHDRAW/PROTECT intent, possible Intercept/reactions and objective-aware AI.

Major blockers:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- adapter/playback;
- broad complete-movement behavior remains PARTIAL.

Reduced version:
Transit Hubs evacuates passengers before battle. Service is suspended. Important property remains outside tactical targeting. AutoPTU resolves a static arena with explicit combatants only.

## Encounter capability profile — Decommissioned Cutting Wildlife Conflict

Full version wants territorial/escape behavior, route-control intent and possibly constrained/environment-sensitive tactical movement.

Current reduced version:
- surveyors leave first;
- ecological observations remain world state;
- Ouros selects one reviewed tactical subgroup;
- static geometry is used;
- battle outcome cannot authorize reopening or negate wildlife evidence.

## Noncombat profile — Control Log Reconciliation

No battle capability is required.

Inputs can include:
- signal/control indications;
- run records;
- station clocks;
- direct observations;
- staff claims;
- maintenance records;
- public timetable revisions;
- network revision history.

Any exact Skill check remains subject to PTU/Caelo review.

## Python evidence

The current Python head `f4ecbc0e2c2c346883fbe3e57c7dccd70076f510` merges a Career fix that fails closed when saved Full FX startup raster information is unknown. Nearby commits similarly harden renderer fallback behavior on hostile/unknown viewport signals.

This is presentation robustness. It does not change battle legality, movement, statuses, terrain, AI or adapter readiness.

## Railway adapter implications

Strong candidates for Minecraft/Cobblemon reuse:
- station/world geometry;
- rails and related block presentation where appropriate;
- doors/gates/barriers/lights/signs;
- sounds and particles;
- vehicle models/animations if available through the eventual integration stack;
- NPC/Pokémon entities, forms, poses, animations and cries;
- public information boards;
- UI/network sync;
- persistent changed structures.

Adapter work still required for semantic events such as:
- run start/stop/arrival/departure;
- authoritative station/service-state projection;
- network revision projection;
- switch/control interaction tied to Ouros state;
- working-Pokémon assignment projection;
- transition from world incident to explicit BattleSpec;
- AutoPTU semantic playback.

Minecraft/Cobblemon BattleState cannot fill any missing authority.

## Unresolved mechanical questions

- Does the governing PTU/Caelo source set map operating a train or rail machinery to an existing Skill, and under what circumstances?
- Which Skills govern technical signalling/control diagnosis versus ordinary vehicle operation?
- Are moving vehicles/platforms represented by any adopted PTU rules?
- How would boarding/disembarking interact with combat if ever required?
- Are vehicle collision/fall consequences defined in governing sources?
- Which Moves/Capabilities can legitimately assist rail work, shunting, clearing or inspection?
- How should an individually assigned working Pokémon interact with Command/Loyalty rules when a mechanical check is actually needed?
- What exact semantic events would a future adapter require for moving trains without ceding tactical authority to Minecraft physics?

## Unresolved canon questions

- Does Ouros contain any railway, subway, monorail or maglev system?
- Which regions or settlements would support it?
- What technical eras and traction systems exist?
- Who operates and maintains a line?
- What station architecture and accessibility practices are normal?
- Do passes, tickets, reservations or free public services exist?
- Are there freight, passenger, institutional or heritage operations?
- Which lines or stations are historic/decommissioned?
- Have old alignments become habitats or public spaces?
- Do Pokémon work in rail operations, and if so in which individually validated tasks?
- What information about operations is public versus internal?

None of these are promoted to canon by Pass 91.