# The Expedition That Left but Never Arrived — Pass 377

Status: PROPOSED / NON-CANON
Date: 2026-09-09
Canon approval: NONE

## Premise

A field team receives several legitimate obligations. Its planner selects a remote survey expedition. Unlike the Pass 376 case, the team really leaves camp: the first semantic travel edge begins and Pass 377 records that start.

The team later fails to reach the expected site.

An administrator can correctly prove that the expedition was selected. A camp worker can correctly prove that the group departed. A receiving station can correctly report that nobody arrived. The missing causal interval becomes the investigation.

No actor must be dishonest for those statements to coexist.

## Player-facing evidence sequence

The case should expose evidence gradually rather than announce an omniscient answer.

At the departure site, the player may find ordinary operational traces showing that equipment was issued and the route was actually entered. A later waypoint may show that no arrival was logged. Communications can contain incomplete or delayed information. Local witnesses may know only one segment of the chain.

Potential explanations remain separate until supported by evidence: voluntary reroute, blocked route, environmental disruption, assistance given to another traveler, Pokémon activity, equipment failure, institutional interruption or deliberate interference.

None is canonically true in this proposal.

## Reduced implementation

The reduced version runs entirely in the Ouros world-agent layer.

Required narrative systems:
- semantic time;
- Pass 375/V16 plan-selection provenance;
- Pass 377 action-start provenance;
- semantic world travel;
- communications and private knowledge when clues move between actors;
- ordinary world-level replanning.

The playable question is whether the group selected the expedition, departed, changed course, became delayed or failed to arrive. No tactical battle is required.

## Full encounter version

A richer version can place the missing interval on a dangerous route. The player may need to locate the team, protect personnel or equipment, reopen a path, escort an injured traveler, recover samples, or create a safe withdrawal corridor.

Wild Pokémon or hostile actors can create tactical pressure, but eliminating every combatant should not be the default victory condition. The narrative objective is recovery, contact, escort, route safety or evidence preservation.

## Engine capability dependency classification

Targeting/footprints/range/LoS: VERIFIED within audited ordinary contracts if the rich version uses standard ranged targeting. Any unusual footprint or bespoke visibility rule remains separately gated.

Base movement legality: VERIFIED within audited ordinary contracts for ordinary movement.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Any cliff shove, rescue drag, interception reaction, forced displacement or carrier movement must declare this dependency explicitly.

Core calculations: VERIFIED within audited deterministic contracts for ordinary arithmetic.

Action economy/initiative: VERIFIED for audited primitives.

Full turn/round lifecycle: PARTIAL. A timed multi-round rescue phase or round-bound objective cannot assume full lifecycle coverage from the currently verified round-start Ability seam.

Full stateful damage pipeline: PARTIAL. The reduced version does not require it. Any rich combat consequence using persistent injury/damage state depends on this family.

Status lifecycle: PARTIAL. Complex ongoing conditions remain gated.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanic. Rising water, unstable ground, delayed hazards, reaction zones or weather-phase behavior require explicit admission.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED. Java merge #414 improves one lifecycle dispatch seam only.

Items: INDIVIDUALLY GATED.

Trainer Features/perks: INDIVIDUALLY GATED.

AI legal-action infrastructure: VERIFIED for ordinary audited legal actions.

AI tactical policy: BLOCKING for rescue-first, protect-cargo, escort, route-clearing, objective-aware withdrawal, search behavior and disengage-after-objective unless a concrete policy contract proves the required behavior.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING for persistent route markers, cargo identity, rescue objectives, acknowledgement of non-KO victory conditions and authoritative end-to-end playback.

## Dependency-safe fallback

If rich tactical dependencies are unavailable, preserve the same premise and move the uncertain interval into semantic world travel. Resolve the investigation through route evidence, messages, witness knowledge and replanning. A simple admitted encounter may appear as pressure, but it must not be used to simulate missing forced movement, complex hazards or objective-aware tactical AI.

## Canon questions before promotion

The final location must be bound to approved Ouros/Caelo geography.

Any institution, survey purpose, communications technology, route regulation, species presence or environmental hazard needs source-backed regional approval before canon promotion.

The proposal introduces no canon location, faction, species table, NPC identity or PTU rule.
