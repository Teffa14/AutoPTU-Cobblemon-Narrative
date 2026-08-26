# Engine Readiness Snapshot — Pass 53

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only Python oracle
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live heads and relevant movement

### AutoPTU-Java

Newest inspected commit:

`b35f09bbcc4246b1846e57c5c4f9bb5771d474e8` — Materialize temporary Accuracy inputs from runtime state (#220).

Recent sequence also includes:
- authoritative seven-stat Combat Stage state;
- Accuracy and Evasion Combat Stage parity contracts;
- secondary Combat Stages through the authoritative mutation service;
- live generic secondary status move-special execution;
- area-target secondary status execution;
- temporary Accuracy bonus contracts and runtime materialization.

These changes strengthen evidence for specific combat-stage, accuracy and secondary-status slices.

They do not establish complete category coverage.

The current Java README still lists unfinished work including:
- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete move/ability/item/perk/Trainer Feature registries;
- semantic event/full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### Python AutoPTU

Newest inspected commit:

`f3f655d7365c698a577490110411ef2bfc3f3c93` — Career winner-label validation.

The newest visible Python changes are Career/persistence/deploy work. They do not justify promoting any tactical capability family for this narrative pass.

Python remains the source oracle while Java parity is incomplete.

## Permanent capability map

### VERIFIED

Targeting / footprints / range / LoS

Java README and parity work continue to support deterministic range, areas, footprints, target anchors and LoS.

Base movement legality

Ordinary represented movement, jump behavior, terrain costs, blockers and fit legality remain supported. This does not include forced displacement, currents, wind drift or rescue movement.

Core calculations

PTU calculation primitives remain supported. Recent Accuracy/Combat Stage work strengthens this family.

Action economy / initiative

Typed phases, action budgets and deterministic initiative ordering remain supported.

AI legal-action infrastructure

The engine can enumerate/filter legal battle choices. This is legality infrastructure, not tactical intent.

### PARTIAL

Full turn / round lifecycle

Authoritative runtime state and selected lifecycle slices exist. Full BattleSpec-to-transcript behavior remains incomplete.

Full stateful damage pipeline

Calculation and selected post-resolution hooks exist, but the README still marks full damage resolution unfinished.

Status lifecycle

Recent generic secondary-status execution is meaningful progress. Complete status-controller behavior is still explicitly unfinished.

Move-specific behavior

Generic move-special pipelines and selected concrete behaviors exist. Full move catalogue behavior remains incomplete.

Abilities

Selected hooks/contracts exist. Full registry coverage remains incomplete.

Items

Selected infrastructure exists. Full catalogue behavior remains incomplete.

Trainer Features / perks

Selected infrastructure exists. Full catalogue behavior remains incomplete.

### BLOCKING

Complete movement including push / pull / knockback / interception / forced movement

The Java README still lists forced movement among unfinished systems. Do not implement wind displacement, current drift, collapsing-ground displacement, escort interception or knockback-dependent rescue objectives as if the family were complete.

Terrain / weather / hazards / zones / reactions

The Java README still lists terrain, hazards and reactions as unfinished. Described wind, floodwater, narrow ledges, nesting areas, smoke, unstable ground or sacred boundaries cannot become tactical zones without exact implementation evidence.

AI tactical policy

Legal choices exist, but policy/scoring remains unfinished. Do not assume wild groups can reliably choose territory defense, nest protection, withdrawal, escort interception or non-damage objectives.

Minecraft / Cobblemon / Craftics adapter and playback

The Java README explicitly states the project is not yet the Minecraft mod and lists the adapter as future work. Route closures, barriers, rescued NPCs, visible hazard state and battle consequences are not yet authoritative adapter writeback.

## Pass-53 non-inference gates

Recent secondary-status work does not mean status lifecycle is complete.

Recent seven-stat Combat Stage work does not mean every Move, Ability, Item or Trainer Feature that modifies stages is implemented.

Verified base movement does not imply forced movement.

Verified battle geometry does not imply environmental hazard zones.

AI legal-action enumeration does not imply AI tactical goals.

A Minecraft-authored route scene must not duplicate missing PTU rules locally simply to make a narrative encounter work.

## Encounter review — Bellglass Stair Rescue

Full-version dependency state:
- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including forced movement/interception — BLOCKING;
- core calculations — VERIFIED;
- action economy / initiative — VERIFIED;
- full turn / round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain / weather / hazards / zones / reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features / perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:
Use world-state wind/closure and a static stable battle landing. No wind displacement, falling hazard, custom rescue action or environmental damage. Resolve stranded-NPC movement outside the battle grid.

## Encounter review — Quiet Basin Diversion

Full-version dependency state:
- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING if required;
- core calculations — VERIFIED;
- action economy / initiative — VERIFIED;
- full lifecycle — PARTIAL;
- stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for protected tactical zones/reactions;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for nest-defense/withdrawal priorities;
- adapter/playback — BLOCKING.

Reduced version:
Keep the nesting area as an overworld access restriction. If a battle occurs, use a neutral static arena outside the protected area and instantiate only the immediate hostile subgroup.

## Review outcome

No permanent capability family is promoted from Pass 52 to a higher status solely because of the Aug 25–26 combat-stage and secondary-status commits.

Those commits materially strengthen the evidence inside `core calculations`, `status lifecycle` and `move-specific behavior`, but the Java README still explicitly identifies the broader missing systems. Narrative design should continue to use reduced encounter forms for environment-dependent sacred-route scenes.