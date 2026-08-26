# Engine Readiness Snapshot — Pass 64

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live Java evidence

Newest inspected AutoPTU-Java commit:

`c5ef1d72c8a997144d215423e2aab60d706905a9` — Port Chronicler Accuracy bonus resolution (#226).

This is newer than Pass 63's inspected commit. It ports another specific Chronicler/Accuracy behavior through parity-backed work. It strengthens evidence inside the Trainer Feature/Accuracy surface but does not establish an entire new capability family.

The current Java README still reports implemented slices for:
- targeting, areas, footprints, anchors and LoS;
- Shift and jump movement legality;
- Damage Base/type charts and calculation primitives;
- invariant accuracy resolution;
- combat-stat resolution;
- typed turn flow/action budget;
- deterministic initiative;
- legal action-space generation.

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

`e9c4173e066da999046818d9ca066bd013f26431` — Career: keep ranked guard ahead of persistence reads (#163).

Recent Python changes preserve rollback/persistence boundaries around ranked Career state. They are robustness work and do not add movement, environment, tactical AI or Minecraft adapter capability.

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

Pass 64 does not promote any category.

## Infrastructure-specific interpretation

A network outage is world state, not a PTU condition.

A dark tile does not impose Accuracy penalties.

A powered machine does not create electrical damage.

Water in a service corridor does not become difficult terrain, forced movement, drowning, damage or a hazard without an exact governing rule and implementation contract.

A backup generator does not grant a combat bonus.

A service priority decision does not alter initiative or action economy.

A Pokémon standing near a failed asset does not prove it caused the failure.

Electric typing does not authorize powering or repairing machinery.

Water typing does not authorize pumping, drainage or safe traversal.

Physical size does not authorize lifting unless governing capability evidence supports the action.

Infrastructure state may determine why a battle happens, where a safe static arena is placed, which NPCs have evacuated, or what services remain available afterward. AutoPTU still owns battle legality and results.

## Encounter review — Switchyard Access Restoration

Narrative premise:

A distribution node remains isolated after an outage. Operators need safe access before restoration can continue, while Pokémon activity blocks the approach.

Intended full version may require:
- reach/protect objective;
- changing powered/unpowered zones;
- interactable control points;
- electrical/machinery hazards where rules support them;
- interception and forced displacement around narrow access;
- objective-aware AI;
- synchronized network/battle presentation in Minecraft.

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

Complete network isolation before tactical resolution. Evacuate operators from the combat space. Instantiate a reviewed static access arena with no live electricity, switch objects, escort objective or forced movement. AutoPTU resolves only the combat. The infrastructure system then records operator access, switching and restoration checkpoints.

## Encounter review — Flooded Conduit Isolation

Narrative premise:

A service corridor has taken on water while a Pokémon incident prevents inspection.

Intended full version may require:
- active water/terrain state;
- changing safe zones;
- withdrawal/protection objective;
- forced movement/current rules if governing material supports them;
- interactable isolation controls;
- objective-aware AI;
- adapter playback for both infrastructure and battle state.

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

Evacuate workers, close the affected corridor and keep water condition in world state. If combat remains necessary, move it to an adjacent static legal arena. Inspection, pumping and restoration happen afterward through infrastructure/facility state.

## Noncombat readiness

Pass-64 structures that can advance without new tactical families include:
- service-zone state;
- authored dependency edges;
- outage incident extent;
- service availability observations;
- cascade packets;
- backup activation/restriction state;
- restoration plans and revisions;
- restoration checkpoints;
- downstream service handoffs;
- outage/report discrepancy investigations;
- after-action review;
- archived restoration history;
- ecological handoff when a shutdown changes habitat use.

These need persistent world-state and eventual Minecraft/UI surfaces, but none require the adapter to simulate PTU hazards.

## Adapter implications

Safe future representations include:
- visibly darkening only zones whose authoritative service state is offline;
- showing a building on backup while nearby zones are dark;
- keeping a lift closed after power returns until its facility state verifies reopening;
- displaying temporary control-room boards or outage notices;
- changing technician locations based on actual restoration steps;
- restoring lights/services in stages;
- retaining barriers around areas still under verification;
- showing old utility corridors as habitat when ecology state supports it.

Unsafe shortcuts include:
- using vanilla redstone as the authoritative regional utility graph;
- letting visual block power decide service state;
- Minecraft lightning independently creating PTU electrical effects;
- water blocks independently creating PTU terrain or status effects;
- resetting outages when chunks unload;
- treating a successful battle as automatic technical repair;
- reopening all downstream services when one upstream node returns.

## PTU/Caelo mapping requirement for rich technical hazards

Before an infrastructure environment affects tactical resolution, implementation must identify:
- exact PTU/Caelo rule source;
- exact environmental state and lifecycle owner;
- movement consequences;
- damage/status consequences if any;
- relevant Moves/Abilities/Items/Trainer Features;
- reaction/interrupt behavior;
- transcript events;
- tactical AI implications;
- adapter representation;
- parity tests.

Until then, outage/restoration state remains narrative/overworld state.

## Pass-64 outcome

Infrastructure can now become more legible after failure without adding a second engineering simulator. Outage extent, backups, cross-network cascades, staged restoration and downstream verification can all persist as world state today.

Mechanically rich switchyard/conduit encounters still require reduced static versions because complete movement, environmental hazards/zones/reactions, tactical AI and Minecraft/Cobblemon/Craftics playback remain blocking.

The new Chronicler Accuracy work is real engine progress, but it remains a representative Trainer Feature slice and does not justify promotion of the whole Trainer Feature/perk family.
