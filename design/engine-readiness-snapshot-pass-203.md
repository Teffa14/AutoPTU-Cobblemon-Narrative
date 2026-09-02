# Engine Readiness Snapshot — Pass 203

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02
Narrative head before pass: `f59ec778652a7d8b842a7d5d60c17311e097c26a`

Read-only engines inspected:
- AutoPTU-Java head: `f320aca406e3da87427eca32ab97943062c264ff`
- AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live engine delta

No engine head changed since pass 202.

AutoPTU-Java remains on `f320aca406e3da87427eca32ab97943062c264ff` — `Freeze forced-movement ability semantic contract (#324)`.

That commit freezes evidence around selected Ability-family prevention semantics, including pinned Python branches involving `push_immunity`, Suction Cups and Sumo Stance. It strengthens parity evidence for a specific family. It does not establish every Push/Pull/Knockback/Interception path, collisions, partial stops, chained displacement, terrain-mediated movement or all combinations with Moves, Abilities, Items, Features, statuses and temporary effects.

AutoPTU remains on `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head explicitly describes the change as presentation-only, synchronizing cached tactical screen dimensions after viewport resize without changing battle rules or outcomes.

No permanent capability category is promoted in pass 203.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING when the complete family is required

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Complete movement caution

A representative prevention contract is not full movement coverage.

Still unverified as one complete family:
- all Push paths;
- all Pull paths;
- all Knockback paths;
- Interception;
- collisions;
- partial displacement/stops;
- chained displacement;
- footprint interactions during movement;
- reaction ordering;
- terrain-mediated displacement;
- all Move/Ability/Item/Feature/status combinations;
- end-to-end adapter/playback parity.

`complete movement` remains PARTIAL.

## Pass 203 PTU/Caelo boundary

Public PTU 1.05 reference material places navigation, scouting, geology, geography and tracking under Survival.

Narrative may preserve:
- map and survey artifact identity;
- map edition/copy lineage;
- survey purpose and participants;
- source observations;
- represented feature assertions;
- explicit uncertainty;
- route-marker identity and observation history;
- actor-facing map provenance;
- historical map comparisons.

Narrative may not invent:
- a Cartography Skill;
- navigation or scouting DCs;
- map-quality mechanical bonuses;
- automatic Survival success;
- tracking bonuses;
- new Edges/Features;
- route movement legality;
- tactical terrain effects;
- canonical coordinate changes from a player-facing map.

A literal indexed `Caelo` search across Narrative, AutoPTU-Java and AutoPTU returned no source content in this run. Caelo-specific navigation, cartography, survey or route-marker modifications therefore remain unresolved.

## Overworld map versus BattleSpec

Pass 203 adds an explicit boundary:

`OVERWORLD_MAP != BATTLESPEC_GEOMETRY`

A Minecraft route, in-world map or canonical coordinate graph can establish narrative location/context. AutoPTU must still own tactical legality.

Battle assembly separately requires validated:
- legal cells;
- footprints;
- range/LoS;
- movement interactions;
- terrain/hazard mechanics where used;
- combatants;
- action legality.

A line drawn as a road on a map does not prove that every corresponding tactical cell is legal movement.

## Pass 203 rich encounter

Encounter: `Survey Line at Glass Bend`.

Narrative premise:
Ema and a small field party are checking a bounded discrepancy between a map/survey edition and a route-marker observation on Sendero del Vidrio. A localized wild confrontation interrupts the work and creates an immediate withdrawal problem.

The cartographic question remains outside battle authority.

### Full intended dependency matrix

- targeting/footprints/range/LoS: VERIFIED within audited contracts
- base movement legality: VERIFIED within audited contracts
- complete movement: PARTIAL; required if protected withdrawal, Interception, Push, Pull, Knockback or other displacement matters
- core calculations: VERIFIED within audited contracts
- action economy/initiative: VERIFIED within audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when selected content uses statuses
- terrain/weather/hazards/zones/reactions: BLOCKING if route conditions become tactical
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL where battle Items participate
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED within audited contracts
- AI tactical policy: BLOCKING when actors must prioritize withdrawal, territorial pressure, disengagement, observer safety or distance over KO
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful overworld -> battle -> world projection

Disposition: FULL RICH VERSION BLOCKED.

## Reduced encounter contract

Narrative retains:
- map/survey artifact identity;
- edition lineage;
- route-marker state/history;
- field-team purpose;
- observations already made;
- document/instrument custody;
- noncombatants;
- publication/revision consequences;
- route-state references.

Before combat:
- place noncombatants and semantic survey objects in a safe Narrative state where appropriate;
- identify one immediate actor still preventing withdrawal;
- select audited combatants and content;
- use stable geometry;
- omit unverified tactical weather/hazards/zones/reactions;
- avoid displacement objectives unless each selected interaction is separately contract-verified.

Allowed narrow handoffs:
- `IMMEDIATE_SURVEY_TEAM_CAN_WITHDRAW`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_SURVEY_SEGMENT_CLEAR_AT_TIMESTAMP`

Battle output cannot determine:
- map accuracy;
- historical marker position;
- why a marker moved;
- route permanence;
- future route safety;
- publication or withdrawal of a map edition;
- canonical coordinates;
- institutional route-closure authority;
- Thin Delivery Season cause;
- whether a personal annotation is true.

Disposition: REDUCIBLE USING AUDITED BASIC BATTLE CONTENT.

## AI tactical-policy caution

Legal-action infrastructure proves only that the engine can reason over currently supported legal actions. It does not prove objective policy for:
- territorial withdrawal;
- disengagement;
- observer protection;
- avoiding survey equipment;
- choosing not to pursue;
- corridor control;
- preserving distance rather than maximizing damage.

The full version therefore remains dependent on AI tactical policy.

## Terrain/hazard caution

Sendero del Vidrio canon includes seasonal watercourses and exposed stone shelves. Those narrative facts do not automatically grant tactical terrain semantics.

If a future encounter uses:
- slippery ledges;
- unstable ground;
- water-flow displacement;
- weather phases;
- hazard zones;
- reactions caused by terrain;

then `terrain/weather/hazards/zones/reactions` is an explicit dependency and remains BLOCKING until the exact family is verified.

The reduced version keeps such conditions descriptive/non-tactical or chooses stable geometry.

## Adapter/playback caution

Minecraft/Cobblemon presentation must not author cartographic truth.

Required boundaries:
- rendered trail != canonical connection migration;
- visible sign != current route authority;
- missing block != canonical marker loss;
- minimap reveal != actor knowledge;
- waypoint != world fact;
- entity unload != survey completion;
- map item texture != authoritative edition state;
- battle arena extraction != automatic BattleSpec legality.

If the Minecraft build disagrees with frozen canonical anchors, that is implementation drift unless canon is explicitly migrated.

## Narrative repository state for this pass

Pass 203 writes only to Narrative.

New files:
- `research/2026-09-02-cartography-survey-route-marker-scan-203.md`
- `design/cartography-survey-route-marker-continuity-layer.md`
- `proposals/2026-09-02-marea-cartography-survey-route-marker-seeds-203.md`
- `design/engine-readiness-snapshot-pass-203.md`

No AutoPTU-Java or AutoPTU write is authorized or performed.

## Implementation recommendation

Prototype `Two Maps, One Bend` first.

It requires:
- no battle;
- no new NPC;
- no new institution;
- no new species;
- no new location;
- no new canonical coordinate;
- no new Skill or DC;
- no new economy rule;
- no route-state retcon.

It directly tests whether Ouros can preserve two legitimate spatial representations, compare them with one bounded field observation and publish a correction without allowing the map artifact or Minecraft projection to rewrite canonical geography.