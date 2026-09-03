# Engine readiness snapshot — Pass 226

Status: CURRENT READ-ONLY CROSS-CHECK
Date: 2026-09-03

Narrative scope:
- `research/2026-09-03-marea-interspecies-predation-territory-scan-226.md`
- `proposals/2026-09-03-marea-sendero-species-interaction-matrix-226.md`
- builds on `design/global-species-interaction-graph.md` from Pass 225.

## Read-only engine heads checked

### AutoPTU-Java

Current `main` checked during this pass:
- `61321c3ab798993be25e10f287e7a375e5db3b63`
- `Mount authoritative tile-trap state in battle runtime (#332)`

The commit mounts deterministic tile-trap state inside `BattleRuntimeState`, exposes read-only snapshots, and keeps mutation/consumption on runtime-owned boundaries.

Interpretation for this pass:
- useful confirmation of the authority rule that battle state belongs to AutoPTU rather than the world adapter;
- evidence applies to the bounded tile-trap runtime contract only;
- it does not verify predator pursuit, grapple escape, multi-party reinforcement, generic territorial AI, or complete terrain/hazard/reaction semantics;
- no permanent capability family is promoted because of this commit.

### Python AutoPTU oracle

Current `main` checked during this pass:
- `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

No new Python mechanical evidence relevant to ecological species interactions was found by the head check.

## What Pass 226 can implement independently of tactical completeness

The following are Ouros world-state responsibilities and do not require hidden AutoPTU battles:

- species ecology profiles;
- ecosystem cells;
- directed interaction edges;
- resource nodes;
- predation pressure estimates;
- non-consumptive threat pressure;
- territorial pressure;
- resource competition pressure;
- population / exposure / activity separation;
- spawn projection inputs;
- observation/evidence packets for NPC systems.

These systems must not write tactical HP/status/position/action outcomes.

## Permanent capability audit

### VERIFIED within audited contracts

1. targeting / footprints / range / line of sight;
2. base movement legality;
4. core calculations;
5. action economy / initiative;
14. AI legal-action infrastructure.

### PARTIAL

3. complete movement, including push/pull/knockback/interception/forced movement;
6. full turn/round lifecycle;
7. full stateful damage pipeline;
8. status lifecycle;
10. move-specific behavior;
11. abilities;
12. items;
13. Trainer Features/perks.

### MIXED / PARTIAL / BLOCKING OUTSIDE VERIFIED SLICES

9. terrain / weather / hazards / zones / reactions.

Notes:
- persistent weather and some bounded hazard/trap contracts have verified slices from prior passes;
- #332 strengthens ownership of the bounded tile-trap state;
- this does not complete the whole category.

### BLOCKING as a complete family

15. AI tactical policy.

### PARTIAL / BLOCKING end-to-end

16. Minecraft / Cobblemon / Craftics adapter and semantic playback/world writeback.

Native Cobblemon time-aware natural spawning remains separately verified as a platform capability from Pass 216. Dynamic ecological projection from the Ouros ledger into live spawn weights/eligibility remains an integration task rather than a completed end-to-end contract.

## Ecology encounter dependency examples

### Off-screen predator pressure

Example: approved Swellow population lowers exposed Wurmple activity in one ecosystem cell.

Required tactical categories:
- none.

Required world integration:
- Ouros ecology ledger;
- population/exposure/activity update;
- spawn/observation projection.

### Visible avoidance

Example: Wurmple detects Swellow pressure and moves into cover without combat.

Full intended version may require:
- reliable overworld perception/behavior policy;
- movement presentation/navigation;
- semantic adapter playback.

Reduced version:
- update exposure/activity state;
- move/despawn/reproject only through supported world behavior without creating tactical claims;
- emit an observation record.

### Direct territorial escalation

Example: Fletchling and approved local Squawkabilly contest a specific resource and escalation enters structured combat.

Dependencies:
- basic targeting/movement/calculation/action primitives are available within audited contracts;
- full turn/damage/status/move/ability breadth remains partial;
- complete tactical AI remains blocking;
- rich world playback/writeback remains partial/blocking.

Reduced version:
- only enter a simple ordinary legal AutoPTU battle after Ouros explicitly decides structured combat has begun;
- no bespoke chase, flock reinforcement, forced displacement, reactive terrain or unsupported environmental mechanics;
- ecological consequence is written after the authoritative result, without inventing hidden combat facts.

### Predator pursuit / escape

Rich chase semantics remain BLOCKING unless the exact movement, terrain, reaction, AI and adapter contracts needed by the encounter have been verified.

Do not implement `predator catches prey` by comparing Minecraft velocity, visual contact or type matchup and writing a result directly.

## Pass 226 readiness conclusion

The ecological interaction graph and first Marea matrix are safe to advance now as world-state design/data.

The major current blocker is not defining who interacts with whom. It is reliable end-to-end projection of those ecological states into visible overworld behavior and, for rich direct encounters, complete tactical policy/playback.

No mechanics family is promoted by this pass.
