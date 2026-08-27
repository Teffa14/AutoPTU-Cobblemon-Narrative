# Engine Readiness Snapshot — Pass 80

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports `design/personal-records-oral-history-correspondence-extension.md` and the mechanically rich Pass 80 candidates.

The narrative repository is the only writable destination for this pass.

Read-only evidence repositories:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Authority boundary

The binding architecture remains:

- Ouros owns persistent world facts, record provenance, source access state and explicit encounter composition;
- AutoPTU owns combatants once instantiated, tactical legality, tactical state and battle resolution;
- Minecraft/Cobblemon provides overworld embodiment, entities, assets, interaction, networking and playback;
- Cobblemon battle-state/participant/controller logic never becomes authoritative for Ouros combat.

Required tactical flow:

`Ouros source/world state -> explicit encounter decision -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon projection`

A person or Pokémon does not become a combatant because it is physically present, loaded, nearby, interviewing, reading, guarding a room or represented by Cobblemon battle code.

Ouros selects participants. AutoPTU owns the tactical facts.

## Current revisions inspected

AutoPTU-Java `main`:

`0706679f4540a0f2249ccfa95fdc86dff0fcf7ea`

Latest inspected commit:

`Expose forced displacement collision stop reasons (#241)`

Immediately preceding movement commit:

`46b03107a566deba55b9f01d2bb571632870719b` — `Add forced displacement collisions and Push Pull execution (#240)`

AutoPTU Python `main`:

`dc1943d826637f4384a7955b78090b2027708c97`

Latest inspected merge:

`Career: keep featured rival history truthful`

The Python changes after Pass 79 concern Career presentation/history truthfulness. They do not establish a new tactical capability family.

## Current Java architecture evidence

The live Java README still establishes the governing architecture:

- AutoPTU-Java is the battle-rules core;
- Python AutoPTU remains the source oracle while parity is incomplete;
- AutoPTU-Java decides legal actions and battle results;
- Minecraft/Cobblemon/Craftics adapt world state and render resulting events.

The README also still lists broad forced movement as unfinished. The two newer commits inspected in Pass 80 provide more specific current evidence than that stale checklist line for one slice of the family.

Commit #240 adds:

- a server-authoritative stepwise forced-displacement resolver;
- collision checks against grid bounds;
- collision checks against blockers;
- collision checks against living combatant footprints;
- large-footprint legality;
- partial-stop behavior;
- Push/Pull execution through the shared resolver;
- authoritative mutation of the target combatant runtime position;
- tests for clear movement, partial stops, occupied cells, blockers, boundaries and large footprints.

Commit #241 adds explicit stop diagnostics:

- NONE;
- OUT_OF_BOUNDS;
- BLOCKER;
- OCCUPIED;
- attempted anchor;
- blocking tile;
- blocking combatant ID when applicable.

This is meaningful implementation progress for forced movement.

It does not establish the whole permanent capability family.

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

Pass 80 makes one category promotion:

`complete movement including push/pull/knockback/interception/forced movement: BLOCKING -> PARTIAL`

No other category changes state.

## Why complete movement is only PARTIAL

Current evidence proves a real authoritative slice:

- Push/Pull instructions can execute through shared forced displacement;
- collision and partial-stop semantics exist;
- runtime tactical position is mutated by AutoPTU-Java;
- large footprints, bounds, blockers and living combatant occupancy are covered;
- stop diagnostics are exposed and tested.

The family is still incomplete because current evidence does not establish all of:

- interception;
- complete knockback behavior across PTU call sites;
- every source of forced movement;
- all Move/Ability/Item/Trainer Feature integrations that can cause displacement;
- reaction interactions;
- terrain/hazard interactions with forced movement;
- collision consequences beyond stopping;
- end-to-end semantic transcript parity for all displacement events;
- Minecraft/Cobblemon playback of authoritative forced displacement;
- complete AI policy around positioning, displacement and interception.

A concept requiring only the exact verified Push/Pull displacement slice may depend on this PARTIAL category with an exact-behavior note.

A concept requiring interception or generic complete forced movement remains blocked on those exact behaviors.

## Other broad blockers remain

The live Java README still marks or structurally implies unfinished work in:

- core combatant/grid battle state;
- full damage resolution;
- complete StatusController coverage;
- terrain;
- hazards;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

Recent held-item work continues to justify Items as PARTIAL, not VERIFIED.

Recent lifecycle/status wiring continues to justify lifecycle/status as PARTIAL, not VERIFIED.

## Personal-record gameplay can mostly execute without tactical mechanics

Most Pass 80 gameplay is ordinary world-state interaction:

- read or inspect an authorized record;
- discover a fragment;
- record custody;
- compare versions;
- identify source dependencies;
- annotate a source;
- conduct or continue an oral-history session;
- preserve an incomplete interview;
- compare a diary with a later memoir;
- hand a record to an archive;
- cite a personal source in a research/public-memory object;
- record that a source was discovered late;
- revise a historical interpretation without rewriting earlier events.

These operations require no tactical capability family.

They can therefore advance before the battle adapter is ready.

## PTU/Caelo boundary for source research

Pass 80 creates no mechanical research subsystem.

If a scene requests a mechanical check for:

- recalling information;
- interviewing;
- detecting deception;
- translation;
- technical interpretation;
- repairing damaged media;
- identifying a Pokémon from a historical description;
- recognizing a Move/Ability/Feature in an old account;

that check must be validated against the governing PTU/Caelo material and current AutoPTU implementation.

The narrative layer stores provenance and evidence without inventing:

- a Truth score;
- a Memory stat;
- a Research bonus;
- an Oral History skill;
- automatic advantage from owning a notebook;
- combat bonuses from knowing an opponent’s historical record.

## Cobblemon reuse profile

SAFE_REUSE candidates:

- written books, lecterns, signs, containers, item frames and display blocks;
- NPC/Pokémon overworld entities as contextual scene participants;
- Cobblemon species/forms/models/textures;
- animations, poses and cries;
- UI surfaces for reading, comparing and annotating records;
- particles and sounds for interaction feedback;
- world coordinates/timestamps as observation context;
- networking/client synchronization;
- item/block/entity persistence hooks;
- exact visual presentation of a record’s physical condition where implementation supports it.

ADAPTER_REQUIRED:

- mapping a Minecraft item/block/display to an Ouros persistent record ID;
- preserving record identity across chunk unload/despawn/reload;
- enforcing access/redaction state in presentation;
- converting player interaction into an Ouros read/interview/annotation action;
- projecting archive/exhibit state back into the world;
- creating an AutoPTU BattleSpec only after Ouros explicitly decides a tactical encounter occurs;
- playing AutoPTU-owned movement and battle events through Minecraft/Cobblemon entities.

BATTLE_AUTHORITY_FORBIDDEN:

- Cobblemon choosing combatants;
- Cobblemon participant/side/controller authority;
- Cobblemon HP/status as historical truth;
- Cobblemon initiative/current turn as narrative evidence;
- a Cobblemon battle roster being treated as a historical witness list;
- a battle result authenticating a diary, correspondence bundle or interview;
- capture resolving an old ownership claim;
- an entity unloading changing a persistent personal-record fact.

## Encounter readiness — Field Notebook Recovery at the Cut Trail

Intended full version:

- a current field team begins near a probable source location;
- noncombatants withdraw through explicit routes;
- Ouros explicitly selects battle participants;
- territorial opponents may contest access;
- Push/Pull can matter where the chosen legal actions actually use the newly implemented slice;
- broader forced movement/interception can matter only after their exact behaviors are implemented;
- tactical AI reasons about WITHDRAW/CLEAR_ROUTE rather than pure KO;
- Minecraft/Cobblemon presents AutoPTU-owned state.

Dependency status:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if active environmental behavior is selected;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

The field team withdraws before battle. The notebook stays outside the grid. AutoPTU receives a reviewed static arena and exact selected combatants. Source recovery happens afterward as an Ouros world interaction.

## Encounter readiness — Reading-Room Evacuation

The full concept can require:

- base movement and LoS;
- moving noncombatants toward exits;
- interception/reactions;
- protect/access objectives;
- tactical AI;
- adapter playback.

Current state:

- basic spatial legality is VERIFIED;
- complete movement is PARTIAL because the Push/Pull slice exists but interception remains unverified;
- reactions/environment remain BLOCKING where selected;
- tactical AI remains BLOCKING;
- adapter/playback remains BLOCKING.

Reduced version:

Readers, staff and source objects leave or are secured through world state before the battle. A standard static encounter resolves elsewhere. Archives/Crisis/Maintenance decide reopening afterward.

## Encounter readiness — Interview Site Interruption

The primary narrative action is an oral-history session.

If a separate threat appears, the intended full version can involve withdrawal/protection.

Current reduced version is implementation-safe:

- stop the interview at an exact timestamp;
- store the session as partial;
- remove speaker/interviewer from the tactical area;
- instantiate only actual combatants chosen by Ouros;
- resolve a conventional AutoPTU battle;
- resume or reschedule the interview later through world state.

No tactical result changes what was already recorded in the interview.

## Promotion gates

Complete movement may move from PARTIAL to VERIFIED only after current tests/contracts establish the complete permanent family, not merely more Push/Pull representatives.

At minimum this requires current evidence for the remaining required behaviors used across the project, including interception and the other forced-movement pathways that the governing PTU/Caelo rules require.

AI tactical policy remains BLOCKING until policy/scoring over legal BattleChoices is authoritative and tested.

Adapter/playback remains BLOCKING until Minecraft/Cobblemon can consume AutoPTU-owned state/events without importing Cobblemon battle-state authority.

Terrain/weather/hazards/zones/reactions remains BLOCKING until those battlefield systems have authoritative runtime support.

## Unresolved mechanical questions for Pass 80

- Which existing PTU/Caelo Skills cover archival research, interviewing and historical reconstruction in the chosen rules interpretation?
- Which checks, if any, should apply to translation or damaged records?
- Which Trainer Features/perks interact with research/knowledge, and are those exact behaviors implemented in Java?
- Can a historical battle record legally inform opponent preparation, and what information boundary applies?
- How should authoritative Push/Pull events eventually appear in BattleTranscript and Minecraft playback?
- Which remaining forced-movement and interception behaviors are required before the permanent movement family can be VERIFIED?

No mechanical answer is invented by this snapshot.