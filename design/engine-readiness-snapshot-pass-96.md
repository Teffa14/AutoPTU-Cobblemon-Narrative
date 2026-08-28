# Engine Readiness Snapshot — Pass 96

Status: IMPLEMENTATION-READINESS EVIDENCE. This snapshot does not create PTU rules or setting canon.
Date: 2026-08-28

## Scope

Pass 96 adds port, berth, passenger and cargo-operation continuity. This snapshot classifies the tactical dependencies of the new mechanically rich encounter concepts against current live AutoPTU evidence.

Read-only evidence inspected during this pass:

- AutoPTU-Java current head: `39b81222af080dd5b2db9b3efdfe742b746d5f5d`
- AutoPTU current head at live recheck: `cf8be250cbc557f32aa64dd03561ba824da45394`
- Pass 95 readiness snapshot
- AutoPTU-Java recent commit history through #255
- AutoPTU latest Career diff
- existing Cobblemon runtime authority boundary

Narrative baseline before Pass 96 writes: `616d5bb3a070c8042ec2a938f7414b9e3972b79d`.

## AutoPTU-Java live evidence

AutoPTU-Java has not advanced beyond Pass 95's inspected head. The latest commit remains #255, `Freeze intercept orchestration control flow`.

That slice provides parity evidence for a specific Python `_attempt_intercept` path across meaningful checkpoints such as candidate ordering, Intercept check, temporary-resource consumption, success branching, interceptor position commit, melee forced movement and target-anchor commit.

It is genuine progress for Intercept orchestration. It still does not prove complete family coverage for:

- every Intercept source and trigger;
- competing reactions;
- generalized reaction ordering;
- broad knockback;
- every Push/Pull/forced-movement source;
- environmental forced displacement;
- terrain-triggered movement;
- complete Move/Ability/Item/Trainer Feature integration;
- objective-aware tactical movement;
- full semantic battle transcript parity;
- Minecraft/Cobblemon playback.

No permanent category is promoted.

## AutoPTU Python live evidence

AutoPTU advanced since Pass 95 to `cf8be250cbc557f32aa64dd03561ba824da45394`, merging `perf(career): defer local persistence from home startup`.

The inspected diff lazy-loads Career local persistence for home/startup and resume/save paths and adds route-splitting coverage around that behavior.

This is Career web startup/performance work. It supplies no new evidence for tactical movement, damage, status, reactions, terrain, AI or the Minecraft adapter.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Existing representative contracts remain sufficient for the established family-level Narrative readiness classification. This does not imply every Move-specific exception is complete.

`base movement legality`

Shift/Jump legality, movement modes and established terrain-cost primitives remain verified at the base family level. Dynamic dock edges, moving vessels, gangways and machinery are outside this classification.

`core calculations`

Established damage-base/type/stage/accuracy/stat primitives remain verified at the existing readiness level.

`action economy/initiative`

Typed action budget and deterministic ordering remain verified at the established family level.

`AI legal-action infrastructure`

The deterministic legal `BattleChoice` space remains verified as infrastructure. This does not provide tactical policy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. The engine has a substantial chain covering base movement, Push/Pull slices, collision/partial-stop behavior and increasingly complete Intercept orchestration. It still lacks broad end-to-end family coverage of all forced movement and reaction interactions.

`full turn/round lifecycle`

PARTIAL. Typed phases/action budgets exist, while broad authoritative lifecycle/state parity remains unfinished.

`full stateful damage pipeline`

PARTIAL. Core calculation primitives exist, but complete authoritative state mutation for damage remains unfinished.

`status lifecycle`

PARTIAL. Representative status and temporary-effect handling exists, including Intercept-related state. The full controller/lifecycle is not verified.

`move-specific behavior`

PARTIAL. Representative Move behavior cannot stand in for registry-wide completeness.

`abilities`

PARTIAL. Representative Ability interactions do not establish family-wide readiness.

`items`

PARTIAL. Representative Item interactions do not establish family-wide readiness.

`Trainer Features/perks`

PARTIAL. Intercept-related Feature/perk work is meaningful but does not prove complete hook coverage.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for rich port encounters. Dock edges, water, gangways, cranes, moving machinery, wind, rain, current, restricted work zones and similar environmental concepts cannot receive tactical effects unless exact rules and engine contracts verify them.

`AI tactical policy`

BLOCKING. Legal actions can be enumerated, but objective-aware behavior for evacuation, protection, route clearing, withdrawal, territorial avoidance and preserving access corridors is not complete.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING. The authoritative adapter remains unfinished. Minecraft/Cobblemon may present port geometry and world state but may not resolve PTU legality or outcomes.

## Pass 96 encounter readiness

### Berth Evacuation Withdrawal

Intended full behavior wants:

- multiple withdrawal routes;
- Intercept and forced movement;
- route protection/denial;
- meaningful dock-edge or work zones where exact rules support them;
- non-KO tactical policy;
- authoritative playback.

Current profile: REDUCED.

Safe reduced form:

- suspend port movement before combat;
- evacuate workers, passengers and ordinary bystanders first;
- remove cargo, vehicles and machinery from tactical interaction;
- use a static land/quay arena away from water edges;
- choose combatants explicitly in Ouros;
- AutoPTU resolves combat only;
- operational systems decide later reopening/resumption.

### Cargo Transfer Interruption

Intended full behavior wants:

- route-clearing/protection objectives;
- complete movement and reaction handling;
- possible staging zones;
- objective-aware AI;
- exact selected Move/Ability/Item/Trainer Feature interactions;
- adapter/playback.

Current profile: REDUCED.

Safe reduced form:

- freeze the transfer at its last verified custody event;
- take cargo and handling equipment out of the tactical arena;
- use a static nearby battle location;
- no battle result changes ownership, custody, manifest truth or delivery state;
- port/courier systems reconcile the transfer afterward.

### Harbor Entrance Diversion

Intended full behavior wants:

- route-control/withdrawal objectives;
- complete movement;
- potentially water/shore terrain and weather/hazard behavior;
- tactical AI;
- synchronized adapter/playback.

Current profile: REDUCED.

Safe reduced form:

- hold all vessels outside the encounter through world state before battle;
- use a static shore/breakwater/land approach arena;
- no moving craft, current, drowning, collision or weather mechanics;
- AutoPTU receives only explicitly selected participants;
- Maritime/Port/Travel determines whether calls wait, divert or resume afterward.

## PTU/Caelo boundary for ports

Current project source inventory supports the existence of PTU movement capabilities and location-specific mechanical identity. It does not provide evidence for a universal port simulation system.

Pass 96 therefore leaves unresolved:

- vessel movement statistics;
- docking/pilotage checks;
- tug operations;
- berth capacity math;
- loading/crane statistics;
- cargo weight physics;
- vehicle/ship HP;
- collision damage;
- gangway/fall rules;
- drowning/current behavior;
- maritime licensing or legal procedure;
- passenger/cargo manifest rules;
- universal Pokémon labor capabilities.

Narrative world state can model operational continuity without fabricating any of those mechanics.

## Minecraft/Cobblemon authority consequences

Minecraft/Cobblemon can be reused aggressively for presentation candidates such as waterfront geometry, blocks, stairs, fences, gates, lamps, signs, terminal displays, water visuals, particles, sounds, Pokémon entities/models/forms/poses/cries, UI, entity tracking, networking and synchronization, subject to concrete API review.

Adapter work is required when presentation must reflect authoritative identity or tactical geometry, including:

- binding world locations to stable `port_id`/`berth_id` identities;
- projecting authoritative closures into physical barriers/signage;
- mapping reviewed geometry into AutoPTU cells;
- linking a visual vessel representation to an Ouros maritime asset without transferring authority;
- preserving identity across chunk unload/reload.

Minecraft/Cobblemon must never decide:

- combatants from nearby entities;
- berth operational state from block/redstone state;
- vessel-call completion from entity movement;
- cargo custody from item-entity movement;
- passenger authorization;
- PTU HP/status/position;
- collision/fall/current/machinery damage;
- Push/Pull/Intercept outcomes;
- weather mechanical effects;
- battle outcome;
- port reopening.

Authority remains:

`Ouros port/world state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## Readiness conclusion

Pass 96 requires no capability promotion to ship its noncombat port continuity, berth history, manifest reconciliation, passenger/cargo handoffs, partial operation and reduced encounters.

The permanent map remains unchanged from Pass 95:

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

Rich port encounters remain blocked primarily by the same broad missing families. Reduced versions preserve the narrative premise without giving Minecraft or Narrative authority over unfinished PTU mechanics.