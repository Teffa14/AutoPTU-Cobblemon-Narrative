# Engine Readiness Snapshot — Pass 59

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live evidence

Newest inspected AutoPTU-Java commit:

`149254ca0f54c6b8a35a25a57a7c872e50ce042e` — Port Focused Training Accuracy bonus resolution (#222).

This commit ports one exact Focused Training Accuracy resolver using authoritative runtime state, parity tests and regression coverage.

It strengthens evidence for one Trainer Feature/Accuracy slice. It does not establish the whole Trainer Features/perks family. The Java README still lists move, ability, item, perk and Trainer Feature hook registries as unfinished, together with core combatant/grid state, full damage resolution, status controller, terrain, hazards, forced movement, reactions, full transcript parity, AI scoring/policy and the Craftics/Cobblemon adapter.

Newest inspected Python AutoPTU commit:

`6f2072d308ee777b5574eb69d08bd23c85af58da` — Career: fail closed when API requests hang (#154).

This adds controlled browser API timeout behavior and explicitly does not change combat rules. It provides no new Java tactical capability evidence.

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

No Pass-59 evidence justifies a category promotion.

## Rivalry non-inference gates

Repeated battles do not prove friendship, hostility, mentorship or romance.

A formal or public battle record does not give a rival access to private team state, hidden Moves, inventory, future plans or current off-screen training.

A Pokémon or Move revealed in one prior battle does not prove it remains on the current legal roster.

Narrative rivalry history cannot grant Accuracy, damage, initiative, XP, Loyalty, Feature, Edge, perk or any other combat modifier.

A rival may adapt only from information they plausibly observed, received or accessed publicly. Hidden counter-picking is prohibited.

Team changes must come from authoritative character state, not invisible rubber-banding.

An NPC-vs-NPC battle that occurs off-screen needs an approved authoritative result source. The narrative generator must not invent PTU dice outcomes or transcripts to populate a bracket or rivalry history.

A recurring rival’s presence must be justified by world state, schedule, institution, route, event or another traceable cause.

A public narrative about a rivalry does not establish either participant’s private motives.

## Encounter review — Crossroads Rematch

Intended version may require:
- current authoritative legal teams;
- route terrain/weather entering tactical resolution;
- legal adaptation based on information observed in prior encounters;
- strategic switching or move selection;
- public spectators affecting record visibility without affecting mechanics;
- exact revealed-information events feeding later callbacks;
- Minecraft playback matching the selected route/venue state.

Dependency state:
- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when selected legal content requires it
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when route conditions enter the battle
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Freeze a static legal arena. Use only Pokémon and mechanical content individually verified for the current vertical slice. Do not treat route weather or terrain as tactical unless those exact families are implemented. Do not claim strategic rival adaptation merely because legal actions can be enumerated. Run the authoritative ordinary battle, then write its result and actual revealed information into rivalry history.

## Encounter review — Rival Team-Up Under Pressure

Intended version may require:
- two recurring competitors sharing a tactical side;
- protect, escape or containment objectives;
- interception and body-blocking;
- forced movement;
- dynamic hazards or zones;
- objective-aware allied coordination;
- knowledge-bounded tactical choices;
- adapter playback of the surrounding incident.

Dependency state:
- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Resolve evacuation, containment, route closure or other noncombat incident state before the battle. Instantiate only legal combatants in a static ordinary team battle. Do not script civilians, dynamic hazards, interception, forced movement or objective-aware coordination. The post-battle narrative may record that the rivals cooperated, but it must not infer friendship or reconciliation.

## Noncombat review — Competing Field Claim

This concept can run now as narrative/world-state content because it relies on:
- existing observations;
- timestamps;
- evidence provenance;
- actor knowledge;
- authored claims;
- institution policy only where already established;
- public-memory/media outputs when applicable.

The scene must keep observation, interpretation, priority claim, public belief and canonical truth separate.

It cannot invent research ownership, publication priority, misconduct rules, academic sanctions or institutional authority. A formal dispute hands off to the governing case, agreement or civic layer.

## Caelo Rivalry boundary

Existing Ouros research records that the supplied Caelo material contains a Rivalry framework with prerequisites.

Current live AutoPTU evidence inspected in Pass 59 does not establish that framework as an implemented authoritative runtime mechanic. A repository code search surfaced a PTR2e ability named Rivalry and unrelated references, which are not governing Caelo evidence for Ouros.

Therefore Rivalry remains narrative-only in this pass. Any future mechanical carry-over requires:
1. explicit approval of the relevant Caelo rule;
2. precise PTU/Caelo mechanical extraction;
3. source-oracle behavior evidence where applicable;
4. Java implementation/parity evidence;
5. adapter support if the effect must appear in Minecraft playback.

## Pass-59 outcome

Recurring rivalry can advance now through agenda-driven meetings, authoritative result references, knowledge-bounded callbacks, independent peer development, public/private state separation and nonblocking rematch structures.

Mechanically rich rival encounters should retain reduced static versions until tactical AI, complete movement, environmental interaction, broader lifecycle/content registries and Minecraft/Cobblemon/Craftics playback become verified.

Capability classifications remain unchanged from Pass 58.
