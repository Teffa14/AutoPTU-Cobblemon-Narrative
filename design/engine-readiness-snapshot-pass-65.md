# Engine Readiness Snapshot — Pass 65

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live Java evidence

Newest inspected AutoPTU-Java commit:

`c5ef1d72c8a997144d215423e2aab60d706905a9` — Port Chronicler Accuracy bonus resolution (#226).

This parity-backed change ports a specific targeted-profiling/Chronicler Accuracy resolver. It is meaningful progress within a Trainer Feature and Accuracy interaction. It does not establish complete Chronicler behavior, complete Trainer Features/perks, or a general research/knowledge mechanic.

The current Java README still reports implemented slices for:
- targeting, areas, footprints, target anchors and LoS;
- Shift and jump movement legality;
- Damage Base/type tables and calculation primitives;
- invariant d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow/action budget;
- deterministic initiative;
- legal autobattler action-space generation.

The same README still explicitly leaves unfinished:
- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Live Python evidence

Newest inspected AutoPTU commit:

`2976b6047702d2e86d367fdad3d648e35ced4145` — Career: reject coerced recovery decision progress (#164).

This hardens persisted Career recovery/decision counters against malformed coerced values. It improves runtime/persistence safety but does not add movement, environment, tactical AI, battle-item, Trainer Feature, or Minecraft adapter capability.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

Pass 65 does not promote any category.

## Publication-specific interpretation

A book, guide, manual, annotation, catalog record or edition is narrative/world information until an exact rule says otherwise.

Reading a work does not grant a Skill Rank, Edge, Feature, Tutor Move, Move, Ability, AP, XP or combat bonus.

Owning a rare copy does not make it a PTU battle item.

A printed Move name does not teach the Move.

A printed Ability description does not expose a Pokémon's private Ability state.

A species field guide does not grant omniscient Pokédex or battle knowledge.

A correction or erratum does not change combatant state.

A library membership or reading-room permission does not modify initiative, Accuracy, damage, action economy or AI.

The newly ported Chronicler Accuracy slice must not be generalized into “reading/research gives Accuracy.” Its eligibility, timing, ownership and effect remain governed by the exact Chronicler contract in AutoPTU.

## Work, edition and copy state are outside tactical authority

These narrative objects may determine:
- which claim an actor plausibly encountered;
- whether an old or revised statement was available at a given time;
- where a significant physical copy currently is;
- which institution or actor has custody;
- whether a copy is under repair, checked out or restricted;
- whether an annotation or insert exists in one copy;
- what research question or social consequence follows.

They do not determine:
- combat legality;
- item effects;
- damage;
- status;
- movement costs;
- targeting;
- Trainer Feature activation;
- AI tactical decisions.

## Environmental library shortcuts that remain unsafe

A fallen shelf does not automatically become difficult terrain.

Smoke, water, broken glass, unstable stacks or fire do not become tactical hazards without governing PTU/Caelo rules and implementation support.

A narrow aisle does not create an interception rule by narrative declaration.

A moving book cart does not create forced movement.

A protected manuscript does not gain custom HP/objective rules without a supported encounter contract.

Minecraft blocks cannot be used as a parallel combat rules engine for these effects.

## Encounter review — Closed-Stacks Evacuation

Narrative premise:

A normally nonpublic storage/reading area must be evacuated during a Pokémon disturbance. Staff prioritize people before collection handling.

Intended full version may require:
- evacuation/clear-route objective;
- narrow routing and changing access;
- protected fragile zones or objects;
- forced displacement/interception near aisles;
- environmental hazards where exact rules support them;
- objective-aware escape behavior;
- adapter playback preserving civilian evacuation and collection state.

Dependency state:
- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Evacuate readers and staff before tactical resolution. Secure/remove significant collection objects from the grid through narrative world state. Run an ordinary battle in a reviewed static adjacent area with no live evacuation, fragile-object HP, changing hazards, forced movement or protection objective. Facility/Archive/Circulation state handles inspection and reopening afterward.

AutoPTU's battle result cannot prove an annotation authentic, establish provenance or correct a catalog record.

## Encounter review — Special-Collection Transfer Interruption

Narrative premise:

A significant copy is in an authorized transfer when a route disturbance blocks the handoff.

Intended full version may require:
- moving transfer party;
- protect/escape/break-through objective;
- interception and forced movement;
- terrain/weather if the route state maps to supported PTU mechanics;
- objective-aware AI;
- synchronized Courier/Circulation/battle playback.

Dependency state:
- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Keep the copy and custodian outside tactical targeting. Freeze the transfer state and run a standard static encounter at a route chokepoint. The authoritative battle outcome only determines whether the route threat is resolved. Courier/Circulation state separately decides whether the transfer continues, reroutes or returns.

No custom cargo HP, escort action or interception behavior is invented.

## Noncombat readiness

Pass-65 structures that can advance before new tactical families include:
- authored-work identity;
- edition lineage;
- revision/errata history;
- copy identity for significant copies;
- circulation transactions;
- copy-specific annotation and insert provenance;
- work-versus-copy availability;
- reading/reference sessions;
- citation/source-use relationships;
- actor knowledge of different editions;
- library wing/service state;
- research questions created by written claims;
- correction and public-memory handoffs.

These need persistent narrative state and eventual UI/adapter surfaces, but they do not need AutoPTU to simulate reading.

## Adapter implications

Safe future representations include:
- representing a shelf bank as one collection zone rather than hundreds of persistent book entities;
- materializing only significant named copies;
- showing a returned/repaired copy reappear in a known place;
- displaying current edition/errata availability in UI;
- keeping restricted/closed areas synchronized with authoritative library/facility state;
- allowing staff dialogue to point toward available references based on actual catalog/circulation state;
- showing an annotation or insert only when the authoritative copy state contains it;
- retaining loan/transfer state across chunk unloads and server restarts.

Unsafe shortcuts include:
- using vanilla bookshelf contents as source of truth;
- deleting work knowledge when a bookshelf is broken;
- granting PTU mechanics when a Minecraft book is opened;
- randomly generating canon lore from shelf loot;
- making book-item possession prove legal ownership;
- resetting circulation state on respawn/chunk load;
- using Minecraft text alone to overwrite actor knowledge or canon claims;
- treating a battle win as automatic recovery/repair of a significant copy.

## PTU/Caelo mapping requirement for mechanically effective knowledge

Before a written source causes a mechanical effect, implementation must identify:
- the exact PTU/Caelo rule source;
- the Feature/Edge/Skill/Move/Item/Ability involved;
- eligibility and ownership;
- action/timing requirements;
- duration/expiry;
- stacking;
- target scope;
- transcript events;
- AI implications;
- adapter representation;
- parity tests.

A representative Chronicler Accuracy resolver is insufficient evidence for unrelated knowledge mechanics.

## Pass-65 outcome

Ouros can now model the slow life of written knowledge without creating an omniscient library database. Works can persist across revisions, actors can remember different editions, significant copies can accumulate copy-specific history, and corrections can change future access without silently rewriting the past.

The full versions of evacuation/transfer encounters still require reduced implementations because complete movement, environmental hazards/zones/reactions, tactical AI and Minecraft/Cobblemon/Craftics playback remain blocking.

The current Chronicler Accuracy work is genuine engine progress but remains one representative Trainer Feature slice. The permanent capability map therefore remains unchanged.