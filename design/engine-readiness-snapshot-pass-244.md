# Engine readiness snapshot — Pass 244

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03
Purpose: Record the exact AutoPTU dependency state used by the Pass 244 persistent-actor cross-fixture trace. This file does not promote broad capability families from representative mechanics.

## Read-only engine heads inspected

### AutoPTU-Java

Repository: `Teffa14/AutoPTU-Java`
Observed `main` head: `6c11964003956e761b4b3e5b4f4be29bb1758859`
Commit: `Expose forced movement landing hazard events (#338)`

New evidence in this head:

- public `TerrainHazardEvent` was added to the battle-event contract;
- terrain-hazard events are exposed to adapters instead of requiring adapters to re-evaluate trap rules;
- landing semantic payload is preserved through ordered battle events;
- forced-movement results can expose landing events after authoritative movement/landing resolution;
- tests/gates cover the public forced-movement landing event bridge.

Interpretation for Ouros:

This materially improves one exact adapter-facing seam: a resolved terrain/trap consequence can travel as a semantic battle event. It does not establish complete terrain/weather/hazards/zones/reactions support, complete movement support, complete damage/status support, or end-to-end Minecraft playback. Pass 244 therefore does not promote any broad family.

### AutoPTU Python oracle

Repository: `Teffa14/AutoPTU`
Observed `main` head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
Commit: `Career: keep battle coordinates synced after viewport resize (#237)`

The latest Python head remains presentation-only for this audit. No new PTU rules evidence is inferred from it.

## Permanent capability categories

| Capability | Pass 244 state | Evidence / boundary |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | Previously audited deterministic contracts. Pass 244 uses only ordinary structured targeting assumptions. |
| base movement legality | VERIFIED | Previously audited base movement contracts. |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | Forced movement and landing integration have continued to improve, but the whole family is not verified. |
| core calculations | VERIFIED | Previously audited deterministic arithmetic contracts. |
| action economy/initiative | VERIFIED | Previously audited action/initiative primitives. |
| full turn/round lifecycle | PARTIAL | Representative lifecycle primitives exist; full lifecycle remains incomplete. |
| full stateful damage pipeline | PARTIAL | KO/damage semantics exist in slices; full pipeline remains incomplete. |
| status lifecycle | PARTIAL | Status hooks and trap status consequences provide evidence, not full lifecycle parity. |
| terrain/weather/hazards/zones/reactions | MIXED/PARTIAL/BLOCKING | `TerrainHazardEvent` improves trap/landing event exposure only. Weather, zones, reactions and broad hazard behavior remain incomplete. |
| move-specific behavior | PARTIAL | Representative move behavior cannot stand for complete move coverage. |
| abilities | PARTIAL | Representative ability support only. |
| items | PARTIAL | Representative item support only. |
| Trainer Features/perks | PARTIAL | Representative Feature support only. |
| AI legal-action infrastructure | VERIFIED | Previously audited legal-action generation/validation infrastructure. |
| AI tactical policy | BLOCKING | No evidence closes full autonomous tactical policy for ecology pursuit/escape behavior. |
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING | Java now exposes a stronger semantic hazard event seam, but materialization, suspension, battle playback and post-battle rematerialization are not verified end-to-end. |

## Pass 244 encounter dependency

The executable reduced trace intentionally avoids forced movement, reaction timing, complex statuses and tactical weather. It requires a direct structured engagement with explicit combatants, ordinary targeting, action economy and core calculations. Where the real battle would depend on incomplete damage/lifecycle/move/ability support, the fixture records the dependency rather than claiming implementation completeness.

The full intended ecological pursuit version remains gated on:

- complete movement for pursuit, interception and disengagement;
- full turn/round lifecycle for timed escape/escort objectives;
- terrain/weather/hazards/zones/reactions for route hazards or reactive control;
- move-specific behavior, abilities, items and Trainer Features if selected actors use them;
- AI tactical policy for a wild actor that chooses between warning, escape, repositioning and engagement;
- Minecraft/Cobblemon/Craftics adapter/playback for faithful suspension and rematerialization.

## New integration evidence created in the narrative repository

Pass 244 adds an executable cross-fixture trace that binds existing contracts together around the same persistent Sendero Fletchling:

`population -> projection lease -> observation -> ecology event -> overworld warning -> manifest freeze -> AutoPTU handoff -> semantic KO result -> ecology memory/avoidance update -> event reevaluation -> rematerialization with a new Minecraft UUID -> repeat sighting -> server restart`

The trace deliberately keeps population abundance constant because no demographic event occurs. `TACTICAL_KO_CONFIRMED` changes encounter history in the fixture but does not imply ecological death or emigration.

## Open mechanical questions

1. Which exact AutoPTU semantic result vocabulary will be frozen for ecological writeback beyond KO/capture/withdrawal?
2. Which HP, injuries, persistent status or condition values can safely return to Ouros today without duplicating incomplete PTU lifecycle rules?
3. When does a fleeing overworld actor cross the threshold into a tactical pursuit requiring complete movement and AI policy?
4. How should a battle-active projection lease be represented in the Minecraft adapter so renderer loss cannot create a duplicate actor?
5. Which event types can the adapter replay directly from `BattleEvent` without additional world-state interpretation?
6. What persistence store owns cross-system encounter history, disturbance memory and post-battle projection intent across server restart?

## Next implementation gap

The highest-value next slice is no longer another independent fixture. It is a runtime-oriented state reducer / replay harness that consumes the Pass 244 trace and emits a deterministic final Ouros state. After that, the same reducer should be ported or mirrored into the writable Minecraft/Ouros runtime repository so the JSON contract protects actual server behavior rather than only narrative fixtures.
