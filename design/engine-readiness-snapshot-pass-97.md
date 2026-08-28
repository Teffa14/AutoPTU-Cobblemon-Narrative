# Engine Readiness Snapshot — Pass 97

Status: IMPLEMENTATION-READINESS EVIDENCE. This snapshot does not create PTU rules or setting canon.
Date: 2026-08-28

## Scope

Pass 97 adds managed-water continuity for dams, reservoirs, channels, diversions, gates and related operations. It classifies mechanically rich encounter concepts against live AutoPTU evidence.

Narrative baseline before Pass 97 writes: `5f2edad45722d90a8e60ae3d633976bfa0ed4aa1`.

Read-only engine evidence inspected:

- AutoPTU-Java head: `39b81222af080dd5b2db9b3efdfe742b746d5f5d`
- AutoPTU head: `cf8be250cbc557f32aa64dd03561ba824da45394`
- Pass 96 readiness snapshot
- AutoPTU-Java recent commit history through #255
- existing Cobblemon runtime authority boundary

## Live evidence assessment

AutoPTU-Java has not advanced beyond the head inspected in Pass 96. Commit #255 freezes parity against the Python oracle for a specific Intercept orchestration path, including candidate ordering, check flow, resource consumption, success branching, interceptor position commit, melee forced movement and target-anchor commit.

This is substantial evidence for a specific movement/reaction path. It does not prove family-wide completeness for:

- all reaction sources;
- competing reactions;
- generalized reaction ordering;
- broad knockback;
- every Push/Pull/forced-movement source;
- environmental displacement;
- terrain-triggered movement;
- all Move/Ability/Item/Trainer Feature hooks;
- objective-aware tactical behavior;
- full semantic transcript parity;
- Minecraft/Cobblemon playback.

AutoPTU Python remains at `cf8be250cbc557f32aa64dd03561ba824da45394` in the inspected evidence. Its current work concerns deferred Career local-persistence startup. It adds no tactical family evidence.

No permanent category is promoted in Pass 97.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Existing family-level contracts remain sufficient for Narrative readiness. This does not mean every Move-specific exception is implemented.

`base movement legality`

Base Shift/Jump legality, movement modes and established terrain-cost primitives remain verified. Dynamic hydraulic movement, moving gates, currents and collapsing banks are outside this classification.

`core calculations`

Existing stat, damage-base, type, stage and accuracy primitives remain verified at the current readiness level.

`action economy/initiative`

Typed action budget and deterministic initiative/order remain verified.

`AI legal-action infrastructure`

Deterministic legal-choice generation remains verified as infrastructure only.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. Intercept orchestration and Push/Pull evidence is increasingly strong, but broad end-to-end forced-movement and reaction coverage remains incomplete.

`full turn/round lifecycle`

PARTIAL. Typed phases and action budgets exist while broad authoritative lifecycle parity remains unfinished.

`full stateful damage pipeline`

PARTIAL. Core calculations exist, but complete authoritative mutation and interaction coverage is unfinished.

`status lifecycle`

PARTIAL. Representative status and temporary-effect behavior exists. Full lifecycle/controller coverage is not verified.

`move-specific behavior`

PARTIAL. Representative implementations cannot stand in for complete registry coverage.

`abilities`

PARTIAL. Representative Ability interactions do not establish family completeness.

`items`

PARTIAL. Representative Item interactions do not establish family completeness.

`Trainer Features/perks`

PARTIAL. Intercept-related Feature/perk work is meaningful but does not prove full hook coverage.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for mechanically rich managed-water encounters. Current, depth, wet surfaces, flood fronts, machinery, spillways, bank collapse, dynamic water levels, restricted work zones and similar concepts cannot gain tactical effects unless exact rules and engine contracts verify them.

`AI tactical policy`

BLOCKING. Legal actions can be enumerated, but objective-aware behavior for withdrawal, route clearing, protection, territorial avoidance and preserving access corridors is not complete.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING. Minecraft/Cobblemon may present water infrastructure and visual world state, but the authoritative adapter is unfinished and must not resolve PTU legality or outcomes.

## Pass 97 encounter readiness

### Gatehouse Withdrawal

Full version wants multiple withdrawal routes, Intercept/forced movement, route protection, restricted zones, potentially water-edge or machinery hazards, objective-aware AI and authoritative playback.

Current profile: REDUCED.

Safe reduced form:

- suspend all managed-water operations before combat;
- evacuate staff and ordinary bystanders;
- keep controls, gates and water outside tactical interaction;
- use a static dry arena;
- select participants explicitly in Ouros;
- AutoPTU resolves combat only;
- Water Management and Maintenance decide later testing/resumption.

### Canal Service Path Conflict

Full version wants route-clearance/withdrawal objectives, narrow-path tactical meaning, Intercept/forced movement and AI that values access rather than KO.

Current profile: REDUCED.

Safe reduced form:

- close the canal segment through world state before battle;
- keep workers outside combat;
- use an adjacent static clearing or dry service path;
- no current, slipping, bank-collapse or water-displacement mechanics;
- victory can secure the approach temporarily;
- blockage removal and service restoration remain separate operational actions.

### Emergency Diversion Perimeter

Full version may want route-control/protection objectives, reactions, complete movement, dynamic water/weather/hazard zones and tactical AI.

Current profile: REDUCED.

Safe reduced form:

- execute or suspend the diversion before combat through authoritative world state;
- exclude water-control equipment, staff and the active flow from the grid;
- use stable nearby terrain;
- no visual water block can cause tactical forced movement or damage;
- the battle result cannot change diversion state automatically.

## PTU/Caelo boundary

Current project source material supports PTU movement capabilities and environment-specific effects when explicitly defined. Pass 97 found no basis for a universal hydraulic simulation.

Still unresolved:

- current-strength mechanics;
- generic drowning rules as applied to these scenarios;
- reservoir/depth arithmetic;
- gate or dam structural HP;
- hydraulic pressure damage;
- flood-front mechanics;
- bank-collapse rules;
- engineering/operation Skill checks;
- hydropower generation formulas;
- irrigation yield modifiers;
- universal Pokémon water-control labor capabilities.

No unsupported rule is added.

## Minecraft/Cobblemon consequences

Safe reuse candidates include world geometry, water visuals, gates, fences, signs, particles, sounds, weather presentation, Pokémon overworld entities/models/forms/poses/cries, UI, networking, tracking and synchronization.

Adapter work is required for:

- stable binding between world geometry and Ouros water-system/asset IDs;
- projecting authoritative closures/restrictions into visible barriers/signage;
- representing broad reservoir state without letting block water become source-of-truth;
- converting reviewed dry geometry into AutoPTU cells;
- preserving identity across unload/reload.

Minecraft/Cobblemon must never decide:

- combatants from nearby entities;
- gate-operation success from redstone state;
- service restoration from water-block movement;
- PTU HP/status/position;
- flood/current/drowning damage;
- forced movement from visual water;
- ecological causation;
- battle result;
- reopening.

Authority remains:

`Ouros managed-water/world state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## Readiness conclusion

Pass 97 can ship noncombat continuity, operating-regime history, observation reconciliation, diversions, partial service and reduced encounters without any capability promotion.

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.