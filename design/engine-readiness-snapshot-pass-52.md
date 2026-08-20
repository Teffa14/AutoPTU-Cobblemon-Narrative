# Engine Readiness Snapshot — Pass 52

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only Python oracle
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live heads

### AutoPTU-Java

Inspected head:

`260ca29699e34d56da8fb32d43d2b6de7dba6892`

Newest inspected change:

`Own canonical battle round in runtime state (#83)`

This moves the current battle-round value into the authoritative runtime state, synchronizes lifecycle processing with it and tests that ownership boundary.

Immediately preceding live change:

`d65c5714d465f87eca2e28e467a6f3a59600cfc9` — authoritative Aura Break blocker queries wired into Aura Storm with exact Python identity matching and parity coverage.

These changes strengthen evidence for:

- server-owned battle-state coherence;
- lifecycle access to canonical round state;
- selected Ability post-damage interactions;
- Python-oracle parity on the implemented slices.

Do not infer:

- complete battle lifecycle;
- complete Ability coverage;
- generic environmental cleanup timers;
- pollution spread;
- toxic-zone behavior;
- current/flow simulation;
- sanitation service clocks;
- complete environmental status application;
- tactical evacuation or worker objectives;
- Minecraft/Cobblemon world-state writeback.

The current Java README still identifies Python AutoPTU as authoritative while the port is incomplete and still lists unfinished work including:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic event/full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### Python AutoPTU

Inspected head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible Python changes remain Career roster-recovery work and do not justify promoting a Java tactical family.

Python project evidence available to this task includes selected battle hazards such as Toxic Spikes and poison application. That proves only those exact Python battle behaviors. It does not establish a generic environmental pollution system and does not prove Java hazard parity.

## Permanent capability map

### VERIFIED

#### targeting / footprints / range / LoS

Deterministic battle geometry evidence remains strong.

This does not verify environmental sampling radius, sanitation coverage, overworld wildlife perception or pollution spread.

#### base movement legality

Represented ordinary movement modes and base terrain/blocker legality remain verified.

This does not verify currents, drifting debris, evacuation paths, waste-pile movement, vehicle movement or contaminated-area traversal.

#### core calculations

Established PTU tables and calculation primitives remain verified.

#### action economy / initiative

Typed phases, action budgets and deterministic initiative ordering remain verified.

#### AI legal-action infrastructure

The engine can enumerate/filter deterministic legal battle choices.

This does not prove AI goals such as isolate a channel, withdraw from contamination, protect workers, cross a route, forage, avoid waste or investigate a resource.

### PARTIAL

#### full turn / round lifecycle

The new authoritative battle-round ownership adds another strong infrastructure slice. Actor/phase state, cleanup, delayed-hit infrastructure, histories and selected hooks also exist.

Complete lifecycle behavior remains unproven.

#### full stateful damage pipeline

Several calculation and post-damage hooks exist. The category remains incomplete.

#### status lifecycle

Selected status application, metadata and phase behavior exist. Complete controller behavior remains incomplete.

#### move-specific behavior

Move keyword parity and selected concrete behavior exist. Full move catalogue behavior remains incomplete.

#### abilities

Selected Ability contracts, including recent Aura Storm/Aura Break integration, have parity evidence. Full Ability coverage remains partial.

#### items

Held-item state and selected hooks exist. Full catalogue behavior remains partial.

#### Trainer Features / perks

Ordered infrastructure and selected concrete Features exist. Complete catalogue behavior remains partial.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Java still lists forced movement as unfinished.

Any encounter requiring live currents, drifting debris, escort interception, forced evacuation, moving containers or pushing actors through/away from contaminated space remains blocked on this family.

#### terrain / weather / hazards / zones / reactions

Broad environmental battlefield state remains unfinished.

World-state pollution, dirty water, waste piles or wastewater do not become battle hazards automatically.

A contaminated-water narrative state may only create a tactical zone/status when the exact PTU/Caelo mechanic and Java implementation are verified.

#### AI tactical policy

Legal choices exist; sanitation/ecological objective selection does not.

The engine does not yet prove policy for:

- withdrawing from a zone;
- protecting workers;
- defending a food/waste resource;
- crossing or clearing a service route;
- isolating an interactable;
- prioritizing escape over damage;
- investigating or avoiding a material stream.

#### Minecraft / Cobblemon / Craftics adapter and playback

Java remains a rules-core library.

Waste containers, treatment state, visible pollution, water-quality variants, sanitation crews, collection schedules, dynamic debris and ecological writeback are not yet authoritative adapter features.

## Critical non-inference gate — contamination is not Poison status

Never infer from Pass 52 world state that:

- dirty water applies Poisoned;
- a bad smell applies a status;
- visible sludge causes damage;
- Poison-type Pokémon ignore every contaminant;
- Grimer/Garbodor generate or remove specific PTU hazards;
- cleanup removes an existing PTU status;
- water described as restored grants healing;
- a treatment facility creates battlefield terrain effects;
- storm debris causes forced movement or collision damage.

Exact rules plus implementation evidence are required.

## Critical non-inference gate — species association is not service capability

Official Pokémon material provides species associations with garbage and sanitation facilities.

Do not infer that an individual:

- is willing to work;
- is institutionally owned;
- has unlimited processing capacity;
- can consume every waste class;
- destroys matter without residue;
- has an unimplemented PTU capability;
- grants sanitation bonuses;
- is the pollution source merely because it is present.

## Encounter dependency — Overflow at Southworks

Reduced version:

Resolve treatment overflow, flow routing, contaminated downstream state and staff isolation actions in overworld/world state. If combat becomes necessary, instantiate only the immediate hostile subgroup on a dry static maintenance platform. Do not add environmental Poison.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when an exact verified status is used;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for WITHDRAW/PROTECT/ISOLATE priorities;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Encounter dependency — Transfer Station Jam

Reduced version:

Use static, explicitly nonhazardous piles/containers as blockers. Keep workers, vehicles, sorting and route-clearance operations outside the battle grid. Run a standard legal encounter only if a subgroup becomes hostile.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING for moving vehicles, gates, material or escorts;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL;
- stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if piles, spills or machinery become tactical state;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for FORAGE/WITHDRAW/CLEAR_ROUTE;
- adapter/playback — BLOCKING.

## Encounter dependency — River Boom Recovery

Reduced version:

Resolve current, floating debris, containment-boom repair and material recovery in overworld state. Use a stable bank/dock arena if combat occurs. Never apply drift or debris damage from narrative description alone.

Full-version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/forced movement/interception — BLOCKING for drift/current behavior;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL;
- stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic water/debris/weather;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for CROSS/WITHDRAW/PROTECT;
- adapter/playback — BLOCKING.

## Pass 52 world-state features that can advance without new battle mechanics

The following narrative systems can be authored now:

- waste-stream provenance;
- collection-service schedules and capacity bands;
- sanitation backlogs;
- treatment inputs/outputs/residues;
- wastewater flow state;
- contamination observations;
- pollution-source hypotheses and evidence;
- cleanup project phases;
- monitoring/verification records;
- recovered-material lineage;
- reuse/recycling records;
- waste-associated Pokémon observations;
- sanitation workplace roles;
- public notices and correction history;
- long-term ecology/service causal edges.

None of these should grant tactical bonuses or statuses.

## Unresolved implementation questions

- Which exact PTU/Caelo rules govern poisonous environments or environmental exposure?
- Which Technology Education, Survival, Medicine or other checks apply, if any?
- How should environmental world state request a battle hazard without duplicating PTU authority?
- Can the future adapter represent water-quality state without making rendering authoritative?
- How should collection/treatment clocks advance while chunks are unloaded?
- How can Cobblemon spawn/behavior state react to sanitation/ecology changes without creating exploitable rare-spawn manipulation?
- What semantic battle/world events are needed for encounters that end in withdrawal, route clearing or successful isolation rather than KO?
