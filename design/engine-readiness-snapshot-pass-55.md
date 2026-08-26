# Engine Readiness Snapshot — Pass 55

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live evidence

Newest inspected AutoPTU-Java commit:

`b35f09bbcc4246b1846e57c5c4f9bb5771d474e8` — Materialize temporary Accuracy inputs from runtime state (#220).

The Java README still says the port is not yet a Minecraft mod and that Python AutoPTU remains authoritative while parity work is incomplete. It still lists full damage resolution, the status controller, terrain, hazards, forced movement, reactions, complete hook registries, full transcript parity, AI scoring/policy and the Craftics/Cobblemon adapter as unfinished.

Newest inspected Python AutoPTU main commit:

`0ea4f8b9b5a2cb98fec40974e088f4238b480c52` — presentation-boundary hardening for persisted combatant status, ability, move and final-status collections.

That Python change improves presentation robustness. It does not provide evidence for promoting any incomplete Java capability family.

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

No Pass-55 concept justifies changing those classifications.

## Event-operation non-inference gates

Crowd pressure can exist as world state without becoming difficult terrain or a tactical modifier.

A temporary barrier can exist in the overworld without gaining a PTU effect that has not been validated.

Observed rain can change event operation without automatically creating battlefield Weather.

Visitor evacuation can be resolved before a battle so civilians do not need unsupported escort or protection rules.

A returning wild group can create an ecological conflict without gaining custom territorial AI or bonuses.

A performer, vendor, volunteer or event worker does not receive a Trainer Feature because of their occupation.

A festival activity does not invent Contest, catching, racing, Skill-check, reward or item mechanics.

## Encounter review — Crowdline Breakout

Intended version may require active evacuation, changing barriers, pursuit/escape objectives, forced displacement and objective-aware opponent behavior.

Dependency state:
- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when temporary zones have tactical effects
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:
Resolve visitor evacuation and zone closure in event state first. Instantiate only actual combatants on a fixed legal map. Do not model crowd tiles, moving barriers, forced displacement or objective-aware pursuit. Apply event consequences after authoritative battle resolution.

## Encounter review — Closing-Time Wildlife Return

Intended version may require dynamically changing occupied areas, territorial or withdrawal-oriented AI, equipment zones and environmental interaction.

The same BLOCKING families apply to forced displacement, dynamic zones, tactical environment behavior, AI tactical policy and adapter/playback. Lifecycle, damage, statuses, move behavior, abilities, items and Trainer Features remain PARTIAL.

Reduced version:
Pause teardown and clear staff/visitors from the relevant space. If a battle is still required, run it on a fixed perimeter map with legal combat participants only. Resume teardown after authoritative result handoff.

## Noncombat review — Opening Gate Dependency Check

This scene needs no PTU battle resolution. It can query event state plus staffing, delivery/vendor, transit, accessibility, sanitation, site-condition and communication records. The host or another established authority makes the opening decision.

A fully embodied dynamic Minecraft site still depends on the BLOCKING adapter/playback family, but the scene can run through narrative/server UI state before that integration exists.

## Pass-55 outcome

Capability classifications remain unchanged from Pass 54. Temporary event content is currently strongest when it uses schedules, setup, teardown, service availability, investigations, relationships and persistent world consequences. Mechanically rich event encounters should keep a reduced static version until the missing PTU families are implemented.