# Engine Readiness Snapshot — Pass 34

Status: read-only evidence snapshot for narrative encounter design.

## Repositories inspected

- `Teffa14/AutoPTU-Java`: read-only
- `Teffa14/AutoPTU`: read-only
- `Teffa14/AutoPTU-Cobblemon-Narrative`: writable destination

## Live Java head inspected

AutoPTU-Java head during this pass:

`48c3cb0b79bbdf3410c646d5232d7bc91ea416e1`

Commit:
`Add canonical status metadata state`

Relevant evidence from this commit:
- canonical status entries now carry language-neutral scalar metadata;
- status state is server-owned and keyed by stable combatant id;
- the implementation preserves deterministic insertion order;
- metadata such as `applied_round` and `source` can be represented canonically;
- Flinch metadata dependence is frozen against the Python phase oracle;
- the code explicitly states that Minecraft/Cobblemon may render this state but may not author rule metadata.

This is useful infrastructure for status lifecycle and future semantic playback.

It does not establish full status coverage.

## Other recent Java evidence

Immediately preceding bounded slices include:
- reusable ordered status-phase registry;
- Flinch START-phase handling with Python parity;
- Strange Tempo + Confusion START-phase interaction with Python parity.

These strengthen lifecycle/status/ability evidence but remain representative slices.

## Current Java README evidence

The Java README still states that Python AutoPTU remains authoritative while the port is incomplete.

It still marks the following as unfinished:
- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The project remains a Java battle-core library rather than a Minecraft mod.

## Live Python head inspected

Latest AutoPTU head observed during this pass:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Commit:
`Career: make roster recovery deterministic`

Recent Python commits around this head are Career-oriented and do not establish new Java tactical capability.

Python remains the source oracle where migration fixtures explicitly pin it. Python functionality must not be treated as Java/Minecraft readiness.

## Permanent capability classification

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items

### BLOCKING for mechanically rich encounter design

- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions
- Trainer Features/perks
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Delta from Pass 33

Java advanced from:
`48083562c03b50e2e6601b3c52101f7a91934cac`

to:
`48c3cb0b79bbdf3410c646d5232d7bc91ea416e1`

The new bounded evidence is canonical status metadata state.

This strengthens:
- status lifecycle: still PARTIAL;
- full turn/round lifecycle: still PARTIAL because metadata can support phase-aware behavior;
- semantic adapter boundary: architecture is clearer, but adapter/playback remains BLOCKING.

No permanent category is promoted to VERIFIED.

## Pass-34 maritime relevance

The maritime layer can safely advance a large amount of world state without tactical support:
- sea-lane records;
- harbor/service state;
- vessel location and journey state;
- navigation knowledge;
- submerged-location graphs;
- wreck provenance;
- salvage/custody records;
- marine habitat state;
- tide/current observations;
- fishing/research scheduling;
- rescue search areas;
- underwater-settlement infrastructure design;
- public notices and chart revisions.

These systems should remain coarse when off-screen.

## Aquatic movement boundary

Java README evidence explicitly includes base Shift movement legality for Overland/Swim/Sky, terrain costs, blockers and water landing rules.

This supports the category `base movement legality = VERIFIED`.

It does not prove:
- full underwater three-dimensional movement;
- drowning/suffocation;
- current-driven forced movement;
- water-pressure hazards;
- underwater visibility rules;
- changing tide inside battle;
- Surf/Dive overworld eligibility;
- passenger transport;
- vessel movement;
- aquatic rescue mechanics.

Those require other rule and adapter contracts.

## Status metadata boundary

The new canonical metadata store is valuable for marine encounters only when an actual PTU status or effect uses metadata.

It must not be repurposed to invent statuses such as:
- drowning;
- soaked;
- seasick;
- pressure sickness;
- current-pulled;
- oxygen-low.

No such mechanical state should be created unless PTU/Caelo and the Java port define it authoritatively.

## Marine environment boundary

Descriptions such as:
- strong current;
- rough swell;
- low visibility;
- storm surge;
- shallow reef;
- flooded compartment;
- unstable wreck;
- deep-water pressure;
- sharp coral;

remain world-state descriptions until exact mechanics are validated.

Minecraft must not convert them into PTU damage, Accuracy penalties, movement costs or forced movement while the terrain/weather/hazards/zones/reactions family remains BLOCKING.

## Encounter dependency table

### Reef Passage Disturbance

FULL version:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if currents/displacement matter
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING
- REACH_EXIT/WITHDRAW objective semantics: not verified

REDUCED version:
Use a fixed reef arena with static blockers and legal base Swim movement. No current, changing tide, moving hazard or escort objective. Resolve route consequence in world state after the encounter.

### Wreck Interior Search

FULL version:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED where the static arena uses supported modes
- complete movement/interception: BLOCKING when water flow or chokepoint control matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- SEARCH_OBJECT/ESCAPE/PROTECT_CONTEXT objective semantics: not verified

REDUCED version:
Evidence and salvage remain outside tactical state. Battle occurs in one stable static compartment. Objects may be static blockers only. Search and custody are resolved before or after combat.

### Harbor Evacuation Chokepoint

FULL version:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING if tactical evacuation uses them
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING when the incident has active hazards
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING when relied upon
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING
- CLEAR_ZONE/PROTECT/REACH_EXIT objective semantics: not verified

REDUCED version:
Keep workers/passengers off-grid. Use a conventional static encounter to clear a chokepoint. The crisis layer advances evacuation state after authoritative battle resolution.

## What this pass must not infer

- Swim slice proves full ocean simulation: false.
- status metadata proves all statuses: false.
- Strange Tempo proves Ability registry completion: false.
- Flinch proves status controller completion: false.
- Python Dive support proves Java Dive behavior: false.
- Minecraft water physics can stand in for PTU aquatic rules: false.
- Cobblemon aquatic species movement proves PTU travel eligibility: false.

## Mechanical questions to resolve later

- exact PTU/Caelo underwater movement and breath rules;
- Gilled capability behavior;
- exact Swim/Mountable/travel boundaries;
- Dive and other semi-invulnerable move behavior in Java;
- underwater LoS/visibility if governed mechanically;
- drowning/suffocation if present;
- weather/sea-state interaction;
- fishing and capture mechanics;
- objective contracts for ESCAPE, WITHDRAW, CLEAR_ZONE and PROTECT;
- adapter representation for submerged locations, vessels and aquatic encounters.
