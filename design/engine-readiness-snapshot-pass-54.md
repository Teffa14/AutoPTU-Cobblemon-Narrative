# Engine Readiness Snapshot — Pass 54

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source oracle context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live Java evidence

Newest inspected AutoPTU-Java commit:

`b35f09bbcc4246b1846e57c5c4f9bb5771d474e8` — Materialize temporary Accuracy inputs from runtime state (#220).

Relevant recent work still centers on:
- seven canonical Combat Stages;
- Accuracy and Evasion stage projection;
- authoritative secondary Combat Stage mutation;
- live generic secondary-status move-special execution;
- area-target secondary statuses;
- temporary Accuracy bonus contracts and runtime materialization.

The current Java README still states that the repository is not yet a Minecraft mod and lists unfinished work including:
- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful Accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full semantic battle-event/transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

No Pass-54 narrative concept justifies promoting a permanent capability family from the Pass-53 map.

## Permanent capability map

### VERIFIED

Targeting / footprints / range / LoS

Deterministic targeting geometry, areas, footprints, anchors and line of sight remain supported by the Java parity work.

Base movement legality

Represented ordinary shift/jump legality, movement modes, blockers, terrain costs and fit predicates remain supported. This does not include forced displacement or interception.

Core calculations

PTU calculation primitives remain supported, with recent Accuracy/Combat Stage work providing additional evidence.

Action economy / initiative

Typed phases, action budgets and deterministic initiative ordering remain supported.

AI legal-action infrastructure

The engine can enumerate and filter legal battle choices. This does not imply tactical intent.

### PARTIAL

Full turn / round lifecycle

Selected typed lifecycle/state exists, but full BattleSpec-to-BattleTranscript behavior remains unfinished.

Full stateful damage pipeline

Calculation and selected runtime hooks exist, while the README still marks full damage resolution unfinished.

Status lifecycle

Secondary-status execution has advanced materially, but a complete status controller remains explicitly unfinished.

Move-specific behavior

Selected generic/concrete move behavior exists. Full catalogue behavior does not.

Abilities

Selected contracts/hooks exist. Full registry coverage remains incomplete.

Items

Selected infrastructure exists. Full catalogue behavior remains incomplete.

Trainer Features / perks

Selected infrastructure exists. Complete hook/registry coverage remains incomplete.

### BLOCKING

Complete movement including push / pull / knockback / interception / forced movement

Forced movement remains explicitly unfinished. Do not make sliding cargo, rough-water displacement, fall movement, protective interception or crowd displacement authoritative in a transit encounter.

Terrain / weather / hazards / zones / reactions

Terrain, hazards and reactions remain explicitly unfinished. A damaged deck, crowded platform, smoke, rough water or loose cargo may exist as world facts but cannot become unsupported tactical modifiers or reaction windows.

AI tactical policy

Legal-action enumeration exists, but scoring/policy remains unfinished. Do not assume wild Pokémon can reliably prioritize withdrawal, civilian avoidance, nest defense, escape routes or containment objectives.

Minecraft / Cobblemon / Craftics adapter and playback

The Java README still states that the project is not yet the Minecraft mod and lists the adapter as future work. Passenger cohorts, service disruptions, boarding state, barriers and battle consequences cannot yet be treated as authoritative in-world playback from Java.

## Pass-54 non-inference gates

A crowded terminal does not create difficult terrain.

Loose cargo does not create forced movement or damage.

A frightened wild group does not automatically use withdrawal-oriented AI.

A passenger standing nearby does not become a protect/escort combat objective.

A nurse, craftsperson, researcher or other professional does not gain unsupported Trainer Features or item behavior because the narrative needs them.

A vehicle changing position in Minecraft does not grant battle movement behavior unless the adapter and battle engine explicitly support it.

## Encounter review — Broken-Deck Containment

Full-version dependency state:
- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING;
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
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING.

Reduced version:
Resolve passenger evacuation and cargo securing as overworld/narrative state before battle instantiation. Run any battle on a static legal deck/platform with only true combat participants. Do not model civilians, sliding cargo, collapsing sections, forced displacement, environmental damage or custom protection reactions. Update service state only after authoritative result handoff.

## Scene review — Last-Leg Witness Window

This scene does not require PTU combat resolution by premise.

Required narrative/world systems:
- journey departure/arrival clock;
- Case-layer claim/evidence separation;
- persistent actor promotion for relevant witnesses;
- privacy and information-state rules;
- Chronicle/contact persistence when a witness remains relevant.

Minecraft / Cobblemon / Craftics adapter/playback is still BLOCKING for fully embodied onboard execution.

Reduced version:
Run the scene through narrative state/UI with a bounded arrival clock and only the relevant named witnesses. Record testimony as claims. Allow unresolved follow-up after arrival.

## Scene review — Unscheduled Ecological Stop

This scene can remain noncombat.

If ecology only changes route/service state, no tactical environment capability is required.

If the full version attempts to model rough water, weather penalties, territorial zones, reaction movement, currents or dynamic environmental damage during a battle, `terrain/weather/hazards/zones/reactions` and potentially `complete movement` become BLOCKING.

Reduced version:
Keep ecological restriction and schedule change in overworld state. Observation, stewardship and rerouting remain narrative interactions. If a battle occurs for another reason, move it to a static legal arena that does not inherit unsupported environmental modifiers.

## Review outcome

Pass 54 creates no capability promotion.

The safest near-term transit content is social, investigative, observational and service-state driven. Combat-capable transit incidents should use the same reduced-version discipline already established elsewhere in Ouros: keep civilians and environmental complications in world state, instantiate only legal battle participants, and let AutoPTU own every tactical rule it actually implements.