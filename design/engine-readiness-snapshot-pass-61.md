# Engine Readiness Snapshot — Pass 61

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live evidence

Newest inspected AutoPTU-Java commit:

`55bdeb0cb9146054d4d80a0999bcd793275fe140` — Freeze canonical Chronicler profile metadata (#223).

This freezes metadata and parity for one Chronicler profile slice. It strengthens one exact Trainer Feature data-contract edge. It does not establish the complete Trainer Features/perks family or any new tactical execution family.

The current Java README still explicitly lists as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- move/ability/item/perk/Trainer Feature hook registries;
- semantic transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Newest inspected Python AutoPTU commit:

`57ee50adfaf1739e1f5d167ce530f1b1a072fe76` — Career: keep rivalry history out of combat modifiers (#158).

This is useful narrative-boundary evidence. Rival intensity/history remains available for continuity and callbacks but does not alter battle levels, preparation, recovery or contract protection. It therefore reinforces the rule that narrative relationship or rumor state cannot silently become tactical modifiers.

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

No Pass-61 evidence justifies a category promotion.

## Rumor and testimony non-inference gates

Repetition is not independent corroboration.

Credibility is not truth.

A local expert may know a narrow routine through repeated exposure. That does not grant broad species knowledge, institutional secrets or hidden world truth.

A correction does not erase the earlier claim, its transmissions or the consequences caused while people believed it.

Confirming a direct observation does not automatically confirm the witness's explanation, motive inference, species-wide conclusion or supernatural interpretation.

A deliberately planted claim spreading does not prove that every recipient believed it.

Widespread community belief cannot promote a claim into canon.

A rumor family cannot create automatic reputation, trust, fear, social success, Skill bonuses, Accuracy/Evasion changes, initiative effects, preparation bonuses or Trainer Feature effects.

Minecraft dialogue or signage showing a rumor does not prove that the server-side world fact matches it.

A battle against a Pokémon found near a rumor location can confirm presence at that battle time. It does not automatically establish responsibility for earlier unexplained events.

## Encounter review — Quarry Echo Search

Narrative premise: workers report recurring sounds near an inactive extraction face. Investigation confirms Pokémon are using part of the site, but the source of all earlier sounds remains a separate question.

Intended version may require:

- unstable tactical zones;
- falling-debris or site hazards;
- changing safe routes;
- forced displacement or knockback near unsafe edges;
- withdrawal/containment objectives;
- objective-aware AI;
- Minecraft playback that preserves site condition.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when displacement matters
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when instability is tactical
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Evacuate workers and close unstable space through world state before tactical resolution. Freeze one safe static arena. Run only legal combatants and individually verified mechanical slices. The authoritative battle result may establish that the encountered Pokémon were present; testimony and observation still determine whether they explain earlier sounds.

## Encounter review — Market-Lane Misidentification

Narrative premise: repeated local stories blame one Pokémon for damaged goods, but timestamps and direct observations indicate multiple actors used the lane during the relevant period.

Intended version may require:

- civilian movement during combat;
- narrow-lane interception;
- destructible or protected market props;
- escape/containment goals;
- forced displacement;
- objective-aware AI;
- synchronized Minecraft playback.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING if stalls, hazards or zones alter tactical resolution
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Clear civilians and movable goods before combat. Freeze the lane as a static map and run an ordinary legal encounter only if conflict occurs. Do not infer responsibility from the winner or defeated combatant. Resolve earlier damage through observation records, timestamps, custody/service records and testimony provenance.

## Noncombat readiness

The following Pass-61 structures can advance without additional tactical engine support:

- provenance-chain reconstruction;
- distinguishing first-hand from second-hand accounts;
- grouping related rumor families;
- linking contradictions and corrections;
- local-knowledge scope based on repeated exposure;
- comparing witness position/time with direct observation;
- identifying that multiple retellings share one original source;
- preserving an old belief after a correction through Public Memory;
- handing informal testimony into a formal case without changing its provenance.

These systems require authoritative world-state storage and eventual Minecraft/UI representation, but they do not need missing PTU combat families to exist as narrative state.

## Pass-61 outcome

Rumor and testimony continuity can advance now as noncombat world-state design. The key implementation requirement is provenance discipline: claims, transmissions, beliefs, observations, formal evidence, public memory and canonical truth must remain separately addressable.

Mechanically rich rumor-driven encounters should keep reduced static versions until complete movement, environmental interaction, tactical AI and Minecraft/Cobblemon/Craftics playback are verified.

Capability classifications remain unchanged from Pass 60.