# Engine Readiness Snapshot — Pass 135

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live AutoPTU-Java and AutoPTU evidence relevant to toxicology, Poisoned/Badly Poisoned, environmental exposure and the Pass 135 encounter concepts. Both engine repositories remain read-only for this task.

A representative mechanic never promotes an entire capability family by itself.

## Inspected heads

AutoPTU-Java:

`9819146364b67da51d039c5d380c8a4aa3c378c5`

Latest inspected commit:

`Freeze pre-damage attack pipeline ordering (#165)`

The latest slice adds parity assertions around ordering between ordinary move resolution, pre-damage interrupts, shield-block checks, post-result handling, attacker item damage bonuses and HP mutation.

Immediately preceding Java head from Pass 134:

`ebfdf7b29da5cdde9b7df7bd6d193ae03f5203f7` — `Port Telepathy pre-damage reaction (#164)`

AutoPTU Python:

`2ec841a4bab8ce7de0698afaf37e0169ae61a277`

Latest inspected Python commit:

`CI: keep validated Career deploy artifact complete (#72)`

This Python change is Career deployment/provenance work and does not change the tactical classification below.

## Python poison/status evidence

Current Python repository evidence includes:

- `PHASE_COVERAGE.md` cites PTU Core 1.05 status timing;
- end-phase tests include `test_badly_poisoned_damage_doubles_each_round`;
- the public AutoPTU development record documents Toxic checking Poison/Steel immunity and Ability suppression before Badly Poisoned is applied;
- earlier parity work in Java has already frozen selected Status prevention paths such as Immunity -> Poison and several other Ability/Safeguard interactions.

Important boundary:

This demonstrates exact battle mechanics in tested paths. It does not demonstrate an overworld toxicology system, environmental dose model, gas concentration model, venom severity model, decontamination system or universal environmental Status application.

## Java README boundary

The current README still explicitly lists as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Minecraft/Cobblemon/Craftics remains a consumer of Java rules, not a second PTU authority.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Substantial parity-backed geometry coverage exists.

This can support exact targeting geometry for a validated Poison Gas, Toxic, Poison Fang or other Move when that Move's behavior is also ported.

It does not model toxic plume propagation in the overworld.

### base movement legality — VERIFIED

Ordinary Shift legality is verified for the ported scope.

Exposure state does not alter movement unless an exact PTU mechanic says so.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

Narrow reaction movement exists and Push/Pull instruction parsing exists, but complete forced movement/interception/collision behavior remains unfinished.

Pass 135 therefore cannot use toxic gas, panic, dizziness or evacuation fiction to push actors around the grid.

### core calculations — VERIFIED

Core calculations remain verified for their ported scope.

No generic toxicology dose, concentration or risk formula belongs here.

### action economy/initiative — VERIFIED

Action budgets and initiative infrastructure remain substantially verified.

Exposure does not change initiative unless the actual PTU effect changes it.

### full turn/round lifecycle — PARTIAL

Round transitions, selected Status timing, delayed hits, temporary effects and reaction slices exist.

Badly Poisoned timing exists in Python evidence, but complete Java lifecycle parity remains unfinished.

### full stateful damage pipeline — PARTIAL

The latest Java commit strengthens ordering around pre-damage/post-result/HP mutation.

The README still marks full damage incomplete.

Environmental toxicology cannot write HP damage directly.

### status lifecycle — PARTIAL

This is the key battle family for Pass 135.

Evidence exists for:

- Python Poisoned/Badly Poisoned behavior in concrete tests;
- selected Java Status application/removal and prevention paths;
- Ability suppression interacting with some prevention hooks;
- Safeguard and veil-style prevention slices from recent Java work.

The complete Status controller remains unfinished.

Environmental exposure therefore remains separate from mechanical Poisoned/Badly Poisoned.

### terrain/weather/hazards/zones/reactions — BLOCKING

Field-state and reaction slices exist, but the family remains incomplete.

A warehouse gas release, contaminated spring, venom residue or toxic plant does not become a custom hazard/zone automatically.

### move-specific behavior — PARTIAL

Representative Move contracts exist; the catalog remains incomplete.

Pass 135 specifically requires exact verification before using mechanics for Moves such as:

- Poison Gas;
- Toxic;
- Poison Fang;
- Toxic Spikes;
- Smog;
- Poisonpowder;
- Spore or other non-Poison biological aerosols when relevant.

Public PTU text alone does not prove Java execution parity.

### abilities — PARTIAL

Many individual Ability hooks have parity evidence.

Relevant examples include selected Status-prevention/suppression behavior.

This does not establish universal toxin immunity for Poison-type Pokémon or every Ability that mentions poison, gas, spores or status.

### items — PARTIAL

Item coverage remains incomplete.

Public PTU Core text defines equipment such as Gas Mask and consumables such as Antidote in exact contexts, but Java item execution must still be verified before relying on those effects inside a battle.

The narrative layer may record possession/equipment state but cannot execute the mechanic itself.

### Trainer Features/perks — PARTIAL

Generic Feature gates/transactions and selected concrete effects exist; the catalog remains incomplete.

No toxicology certification, Medicine expertise or Poison-specialist Feature is inferred from occupation or narrative role.

### AI legal-action infrastructure — VERIFIED

Legal battle-choice construction/filtering is substantially implemented for the ported scope.

It does not understand toxicology investigation, evacuation priorities or exposure avoidance as strategic goals.

### AI tactical policy — BLOCKING

No complete objective-aware policy exists for Pass 135 goals such as:

- `EVACUATE`;
- `WITHDRAW`;
- `CLEAR_ROUTE`;
- `REACH_SAFE_ZONE`;
- `PROTECT_RESPONDER`;
- `PROTECT_TECHNICIAN`;
- `AVOID_EXPOSURE_AREA`;
- `REACH_EXIT`.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists.

Minecraft must not infer toxicity, dose, PTU Status, source identity, safe concentration or immunity from block/particle/entity state.

## Pass 135 encounter dependencies

### Warehouse Exposure Alarm — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING for live evacuation/interception;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL if combat damage occurs;
- status lifecycle — PARTIAL if an exact PTU Status mechanic occurs;
- terrain/weather/hazards/zones/reactions — BLOCKING if a toxic area is meant to have tactical effects;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED:

Resolve alarm, exclusion area, evacuation, protective equipment and exposure opportunities in world state. Remove civilians/noncombatants. Freeze a safe static arena. If confrontation remains, run a conventional battle. Sampling and toxicology assessment resume afterward. No custom poison zone is created.

### Venomous Bite Field Survey — FULL

Requires:

- targeting/range/LoS — VERIFIED;
- base movement — VERIFIED;
- complete movement — BLOCKING for pursuit/interception/withdrawal;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL;
- damage — PARTIAL;
- status lifecycle — PARTIAL if the authoritative attack applies Poisoned/Badly Poisoned;
- environment/reactions — BLOCKING only if invoked;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:

Record the bite/exposure event before combat. Evacuate the affected subject through world state. Any remaining confrontation is a static battle. Care/Toxicology own post-event assessment. The battle transcript does not infer venom dose.

### Suspect Spring Closure — FULL

The narrative premise is primarily overworld investigation.

If a confrontation occurs while investigators protect sampling access, dependencies include:

- targeting/range/LoS — VERIFIED;
- base movement — VERIFIED;
- complete movement — BLOCKING for live route-control objectives;
- action economy/initiative — VERIFIED;
- lifecycle/damage/status — PARTIAL if invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING if contaminated water is meant to have tactical effects;
- move-specific behavior/abilities/items/Features — PARTIAL as applicable;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:

Close the spring in Travel/Land Access state. Sample outside combat. If a battle occurs, use a nearby static arena without toxic-water mechanics. Winning does not establish the source or lift the closure.

## Pass 135 overworld blockers

The following are new world-state requirements outside AutoPTU-Java:

- `TOXIC_AGENT_PROFILE` persistence;
- toxic source-event history;
- exposure-opportunity graph;
- subject-specific exposure records;
- route-of-exposure state;
- qualitative/validated magnitude estimates;
- toxicology sample provenance/custody;
- source-attribution hypotheses;
- decontamination records;
- exposure advisories;
- Toxicology -> Care handoff;
- Toxicology -> Outbreak/Health Surveillance handoff;
- Toxicology -> Cases handoff;
- source systems -> Toxicology handoff;
- toxicology world state -> battle snapshot gate.

None belongs inside the Minecraft renderer or the battle engine by default.

## Explicit non-inferences

Pass 135 forbids:

- Poison-type -> environmental toxin immunity;
- Poison/Steel battle immunity -> immunity to all toxic agents;
- Gas Mask -> universal gas immunity outside exact PTU text;
- Antidote -> universal cure;
- contaminated air/water/soil/food -> Poisoned;
- Poisoned -> environmental source known;
- visible gas -> tactical zone;
- venomous species nearby -> exposure confirmed;
- exposure confirmed -> diagnosis known;
- source confirmed -> wrongdoing proven;
- decontamination completed -> mechanical Status removed;
- battle victory -> scene safe;
- battle LoS/range -> plume or exposure radius.

## Unresolved mechanical/canon questions

- Exact PTU/Caelo Poisoned and Badly Poisoned rules as used by this project.
- Exact Gas Mask, Antidote and Medicine interactions.
- Whether Caelo defines environmental toxins, smoke/gas exposure or special protections.
- Which Poison/Steel immunities apply only to PTU Status and which, if any, have broader authored setting meaning.
- Java parity for Poison Gas, Toxic, Poison Fang, Toxic Spikes and relevant Items/Abilities.
- Whether Ouros should ever model dose numerically outside rules-authored mechanics.
- Which institutions can diagnose, sample, decontaminate or issue advisories.
- How multiplayer privacy applies to toxicology/clinical records.

Super PTU Online Helper was not exposed as an invocable capability during this run. The complete primary Caelo corpus was not reliably accessible. No output or rules are attributed to either source.
