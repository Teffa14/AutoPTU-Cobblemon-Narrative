# Engine Readiness Snapshot — Pass 57

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-20

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination remains:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`014933ea022198d5558a4f899ba4b41d0c59a47f`

Latest commit inspected:

`Bind Analytic to authoritative initiative progress`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/014933ea022198d5558a4f899ba4b41d0c59a47f

The slice adds server-owned initiative order/cursor state to `BattleRuntimeState`, exposes lifecycle mutation boundaries for initiative progress and makes Analytic read authoritative initiative/action state rather than adapter-provided claims. Tests cover initiative lifecycle ownership and Analytic behavior.

This is meaningful evidence for:

- action economy/initiative;
- full turn/round lifecycle infrastructure;
- abilities;
- stateful damage-hook integration.

It does not prove the complete Ability registry, complete lifecycle or full damage pipeline.

Current Java README:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

The README still identifies Python AutoPTU as the oracle while the port is incomplete and still lists these broad areas as unfinished:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature registries;
- full semantic BattleSpec → BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest commits are Career-focused, including deterministic roster recovery. No new Python tactical slice inspected in this run changes the permanent capability classification used below.

Canonical URL:
https://github.com/Teffa14/AutoPTU/commit/e4bb0ca38b7018710af476ce365d515a387de4e7

Python remains the behavior oracle for battle slices that Java ports and freezes through parity fixtures.

## Permanent capability map

The classification remains conservative. A representative Ability, Feature or status never promotes an entire family by itself.

| Permanent capability family | Pass 57 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Java README and parity work cover range, areas, footprints, target anchors and LoS. |
| base movement legality | VERIFIED | Shift/Jump legality, basic movement modes, terrain movement costs, blockers and fit rules have dedicated coverage. This does not mean the full terrain subsystem is complete. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | README still lists forced movement and reactions as unfinished; no broad parity contract demonstrates the family. |
| core calculations | VERIFIED | Damage Base/type tables, stages, accuracy primitives, crit probability and several modifiers are implemented as calculation primitives. |
| action economy / initiative | VERIFIED | Typed turn flow, action budget, deterministic initiative ordering and now authoritative initiative progress are directly evidenced. |
| full turn / round lifecycle | PARTIAL | Java has substantial phase/round state and lifecycle hooks, but full combat state and all phase-sensitive mechanics are not complete. |
| full stateful damage pipeline | PARTIAL | Live post-damage hooks, signed adjustments, RNG-hook ordering and Analytic exist, while README still lists full damage resolution as unfinished. |
| status lifecycle | PARTIAL | Several status slices and registries exist, but the full status controller is still explicitly incomplete. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Calculation primitives and movement costs do not prove the runtime terrain/weather/hazard/zone/reaction family. README still lists terrain, hazards and reactions as unfinished. |
| move-specific behavior | PARTIAL | Move contracts/keywords and selected behavior are ported, not the full PTU Move library. |
| abilities | PARTIAL | Multiple Abilities now run through authoritative hooks, including Analytic, but representative hooks do not prove the complete registry. |
| items | PARTIAL | Held-item and selected item slices exist from prior passes; full item registry remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered hook infrastructure and selected Features are present, while the complete registries remain unfinished. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal action-space generation and filtering are explicitly implemented. |
| AI tactical policy | BLOCKING | README still lists AI scoring/policy as future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Repository explicitly states it is not a Minecraft mod yet and adapter work comes after a parity-safe vertical slice. |

## Pass 57-specific implementation boundary

Credentials, permission grants and eligibility are primarily persistent overworld authority state. They should not be implemented inside AutoPTU-Java's battle rules core.

A future server-side Ouros/Minecraft authority layer needs a verified contract for:

identity + credential/permission record + location/activity scope + current world state → allow / deny / supervised / alternate route.

That contract is currently a Pass 57-specific BLOCKER outside the permanent battle categories.

Suggested label:

`OVERWORLD_CREDENTIAL_PERMISSION_GATE = BLOCKING`

This blocker does not lower any battle category. It simply states that the battle engine should not be asked to decide whether a player may enter an archive, protected trail, laboratory, worksite or tournament back room.

## Why the new Java Analytic slice does not change classification

The latest Java work correctly removes a dangerous adapter shortcut: Analytic now reads initiative progress and action history from canonical runtime state.

That strengthens the architecture because future Minecraft clients cannot claim that a target already acted merely to activate a damage bonus.

The evidence remains narrow:

- one Ability using authoritative initiative/action state;
- one family of post-damage behavior;
- specific tests around initiative cursor/order.

It does not verify:

- every initiative-sensitive Ability;
- all interrupts/reactions;
- full lifecycle cleanup;
- complete damage sequencing;
- tactical AI;
- Minecraft playback.

No permanent category is promoted in Pass 57.

## Encounter dependency review

### Survey Annex Checkpoint

Full version intended mechanics:

- controlled corridors;
- protection/escort lanes;
- access verification during an evolving disturbance;
- potentially interactive doors or alarm zones;
- autonomous opponent/wild behavior.

Dependency result:

- VERIFIED foundation: targeting/footprints/range/LoS, base movement legality, core calculations, action economy/initiative, AI legal-action infrastructure;
- PARTIAL dependencies: lifecycle, stateful damage, statuses, move-specific behavior, abilities, items, Trainer Features/perks depending on roster;
- BLOCKING for full version: complete movement/interception/forced movement, terrain/zones/reactions if used, AI tactical policy, Minecraft/Cobblemon/Craftics playback;
- extra overworld blocker: credential/permission gate.

Reduced version:

Resolve permission state before battle. Keep doors, civilians and verification equipment out of tactical authority. Launch a normal static battle only if combat actually occurs.

### Seasonal Corridor Permit

Full version intended mechanics:

- reach/withdraw objective;
- moving wild collective;
- non-defeat resolution;
- corridor state that may constrain movement;
- time-bound permission state.

BLOCKING families:

- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions if corridor state is tactical;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics playback;
- overworld credential/permission gate.

Reduced version:

Keep the migration, access window and withdrawal decision in persistent world state. Freeze an ordinary static battle only for contact that genuinely becomes combat.

### Promotion Challenge Gate

Reduced version can use the existing verified foundation more directly:

1. overworld service verifies eligibility;
2. AutoPTU-Java runs an ordinary legal static battle;
3. battle transcript/result returns authoritatively;
4. institution applies rank/credential consequence afterward.

If the future full challenge adds HOLD_ZONE, REACH_TILE, destructible objectives, forced movement or special arena hazards, those exact families become blocking dependencies and must be listed in the encounter contract.

## PTU/Caelo caution

Pass 57 does not infer mechanical competence from a narrative credential.

Examples:

- a climbing qualification does not grant a movement capability;
- a research pass does not grant an Education Skill rank;
- a security badge does not grant Command, Guile or Perception bonuses;
- a Ranger title does not grant Features unless the actual PTU/Caelo build does;
- a tournament ticket does not modify Initiative or damage.

Project-supplied Caelo material previously reviewed includes location access tied to authored requirements such as items/levels. The full primary Caelo files were not reliably recoverable in this runtime, so no new Caelo-specific rule is declared here.

## New evidence required before promoting the Pass 57 full encounters

For full tactical versions:

- explicit objective-state contracts such as PROTECT / REACH_EXIT / HOLD_ZONE if used;
- complete forced movement/interception semantics where escort lanes matter;
- terrain/zone/reaction contracts for active checkpoints or alarms;
- tactical AI capable of respecting objectives other than damage optimization;
- server-authoritative Minecraft adapter/playback.

For the overworld system:

- server-owned identity and permission registry;
- versioned eligibility rule storage;
- scope-aware access query;
- token/credential presentation that cannot override server state;
- privacy controls;
- expiry/suspension/revocation history;
- interregional recognition integration;
- audit-safe emergency grants.

## Snapshot conclusion

Pass 57 adds no reason to relax the conservative engine readiness map.

The latest Java work materially improves authoritative initiative state and the Analytic Ability slice. The richest permission-themed encounters still depend on movement objectives, broad reactions, tactical AI and Minecraft playback that are not ready.

The narrative layer can advance immediately because qualification, access, admission, recognition and expiry are world-state systems. Reduced encounters can keep those decisions outside the tactical grid until the relevant battle families are verified.