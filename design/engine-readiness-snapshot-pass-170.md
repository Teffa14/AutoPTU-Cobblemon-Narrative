# Engine Readiness Snapshot — Pass 170

Status: evidence snapshot for narrative dependency planning. Not a rules source and not canon.
Date: 2026-08-25
Narrative focus: astronomical observation, observatories, celestial-event follow-up and public observing incidents.

## Read-only engine evidence inspected

AutoPTU-Java main head inspected: `7cd765e87fa4254789eb40e8d14f91e1251631ad` — `Freeze generic move-special secondary status contract (#204)`.

Recent Java slices since Pass 169 include stacked Stat Stratagem effect-roll bonuses, move-special roll-penalty state, Hardened crit/effect bonus behavior, runtime-derived move-special effect-roll inputs and a generic secondary-status parser contract. The latest slice freezes parser parity for a generic move-special secondary Status boundary.

This is useful evidence for narrow pieces of move-special execution, effect-roll inputs and status-effect parsing. It does not demonstrate the complete Move catalog, full status lifecycle, environmental astronomy rules or adapter support.

AutoPTU-Java README still explicitly leaves these major families incomplete:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- remaining move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

AutoPTU Python main head inspected: `87df4bcae3200324f50b71ce5438bebd62b955b9` — Career hardening for legacy season-roster rendering. The commit states that authoritative Career mechanics are preserved and provides no basis for a battle-readiness promotion.

## Permanent capability map

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No permanent category is promoted in Pass 170.

## Why astronomy remains world state

AutoPTU may resolve an independent confrontation at an observatory, recovery perimeter or festival. It cannot determine:

- whether a celestial event occurred;
- astronomical target identity;
- orbit/ephemeris solution;
- observing-window prediction;
- uncertainty of a celestial solution;
- whether two observations refer to one target;
- whether a candidate is an artifact;
- meteor versus meteorite linkage;
- sky brightness or cloud truth;
- cultural meaning of an eclipse/comet/shower;
- whether Minior or Lunatone behavior is causally linked to an event;
- scientific validity of a telescope observation.

## Encounter dependency matrix

### Observatory Dome Evacuation During Storm — FULL

Targeting/footprints/range/LoS: VERIFIED for ordinary combat.

Base movement legality: VERIFIED for ordinary legal shifts.

Complete movement: BLOCKING. Required if visitors, staff or Pokémon must evacuate or withdraw dynamically through threatened space, or if interception matters.

Core calculations: VERIFIED for supported ordinary calculations.

Action economy/initiative: VERIFIED.

Full turn/round lifecycle: PARTIAL when complete lifecycle state matters.

Full stateful damage pipeline: PARTIAL when damage is used.

Status lifecycle: PARTIAL for any exact Status.

Terrain/weather/hazards/zones/reactions: BLOCKING if storm, damaged dome, exposed roof, falling equipment or protected corridors alter tactical legality.

Move-specific behavior: PARTIAL whenever a particular Move beyond verified generic behavior is essential.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features/perks: PARTIAL.

AI legal-action infrastructure: VERIFIED.

AI tactical policy: BLOCKING for `EVACUATE`, `PROTECT_TECHNICIAN`, `WITHDRAW` or `CLEAR_ROUTE`.

Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED: terminate the observing session and evacuate visitors via world state. Secure the dome and freeze a safe static arena nearby. Run an ordinary battle only if an independent confrontation remains. No custom storm, dome, telescope or sky-event mechanics are created.

### Meteorite Recovery Perimeter — FULL

Ordinary VERIFIED/PARTIAL battle categories remain as above.

Complete movement: BLOCKING for moving searchers, civilians, wildlife withdrawal or interception.

Terrain/weather/hazards/zones/reactions: BLOCKING only if debris, fire, unstable ground, protected evidence cells or other environmental state has tactical effects.

AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_RESEARCHER`, `CLEAR_ROUTE`, `REACH_EXIT`.

Adapter/playback: BLOCKING.

REDUCED: conduct search, custody and candidate-rock assessment in world state. Remove researchers/specimens from the grid. Run a static battle only for a separate confrontation. Geology/Material Culture, not battle victory, decides meteorite linkage.

### Stargazing Festival Crowd Surge — FULL

Complete movement: BLOCKING for crowd evacuation, wildlife withdrawal or interception.

Terrain/weather/hazards/zones/reactions: BLOCKING only if darkness, slopes, temporary barriers or weather have actual tactical consequences.

AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `PROTECT_VISITOR`, `CLEAR_ROUTE`.

Adapter/playback: BLOCKING.

REDUCED: Public Events/Wayfinding reroute visitors and wildlife before battle. Freeze a static encounter space. The astronomical event proceeds independently of battle outcome.

### Two Observatories Disagree — NON-COMBAT

No battle capability required. Timekeeping, Metrology, Meteorology, Lightscapes, Astronomy and Science can reconcile or leave the claim `UNRESOLVED`.

## Recent Java evidence must not be over-generalized

`7cd765e8...` freezes a generic move-special secondary-status parser contract. Together with the immediately preceding effect-roll work, it does not prove:

- full secondary-effect execution;
- full status controller;
- all Moves;
- all Abilities/Items/Trainer Features;
- environmental Status application;
- Gravity as world physics;
- Moonlight as a world-state effect;
- meteor impacts;
- weather phases;
- general reactions/forced movement;
- objective-aware AI;
- Minecraft sky integration.

Verified battle LoS cannot be reused for telescope visibility. Astronomical visibility depends on target geometry, observing site, horizon, time, weather, lightscape, instrument and method state.

## PTU/Caelo cross-check guardrails

Accessible project research confirms PTU 1.05 is the project’s public baseline, but the requested Caelo primary files were not recovered reliably from the available File Library search for astronomy.

Official Pokémon species lore for Minior and Lunatone can inform authored behavior, but species flavor does not create PTU rules.

Do not infer:

- `Gravity` Move -> celestial mechanics;
- `Moonlight` -> lunar illumination/healing in world state;
- `Meteor Mash` / `Comet Punch` names -> meteor/comet simulation;
- Minior -> every meteor;
- Lunatone -> global full-moon modifiers;
- Psychic/Occult Education -> astronomy expertise;
- telescope -> PTU Item bonus;
- Minecraft moon phase -> authoritative Ouros astronomy.

Super PTU Online Helper was not available as an invocable capability during this run. No output is invented.

## Pass 170 world-state blockers

These are outside current AutoPTU parity:

- astronomical observing-program persistence;
- observatory/site state;
- target/event identity and candidate linkage;
- session/coverage records;
- follow-up requests;
- astronomical solution revisions;
- visibility predictions;
- meteor/meteorite handoff;
- public-notice revision history;
- long-baseline archives;
- community-observer provenance;
- Timekeeping/Metrology/Meteorology/Lightscapes integration;
- Minecraft projection without vanilla-sky authority.

## Mechanical guardrails

Do not create:

- celestial Weather/Terrain/zones;
- lunar buffs/debuffs;
- eclipse Status;
- meteor collision damage;
- radiation rules;
- telescope Accuracy/Initiative bonuses;
- automatic Legendary encounters;
- Minior spawn schedules;
- cosmic evolution triggers;
- observational capture modifiers;
- astronomical Surprise;
- Psychic/Occult bonuses from celestial events.

## Promotion decision

No permanent capability category changes state in Pass 170.