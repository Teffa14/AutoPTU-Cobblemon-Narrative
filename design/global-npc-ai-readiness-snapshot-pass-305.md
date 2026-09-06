# Global NPC AI readiness snapshot — Pass 305

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

Narrative repo head before Pass 305: `7beb2ff3ac80b3255962636b7e84ae64324b64e4`.

## Read-only engine evidence

AutoPTU-Java advanced to `0066150247490ad5d79834a0aac83ba345362989` through PR #380, `Freeze reusable Tick value against Python oracle`.

The commit adds a reusable Tick value contract, exports pinned Python Tick-value fixtures, compares the Java result against the Python oracle and gates that seam in CI. This is positive parity evidence for the specific deterministic value contract represented by Tick. It does not prove that the full core-calculation family, turn lifecycle, damage pipeline, Move behavior, Trainer Features or adapter playback are complete.

The previous Java head `3c6d641c63b33d8ab3ace4d90539dbad2975b8c2` remains relevant for the server-owned ordinary-damage ingress through temporary HP into normal HP. That seam still excludes prevention/reactions, Injuries, faint handling, history rotation, semantic events and source attribution.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its live head remains presentation-only and explicitly changes no battle rules or outcomes.

## Capability classification

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts; PR #380 strengthens a specific reusable Tick-value parity seam but does not expand this classification beyond the already-audited boundary;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

No category is promoted by Pass 305 or by Java PR #380.

## Pass 305 dependency boundary

Concurrent infrastructure attribution is world-simulation reasoning over provenance-backed evidence and requires no AutoPTU tactical capability family.

The full proposed relay encounter activates additional families only when those mechanics are authored:
- ordinary site traversal can use verified base movement;
- wind displacement, forced rescue movement, interception or knockback require complete movement;
- timed surges or collapse phases require full turn/round lifecycle;
- environmental damage requires the full stateful damage pipeline;
- persistent conditions require status lifecycle;
- active weather, debris zones, hazards and reaction rescues require terrain/weather/hazards/zones/reactions;
- any mechanically active Move, Ability, Item or Trainer Feature requires its owner family;
- autonomous tactical response requires AI tactical policy;
- authoritative visible execution requires Minecraft/Cobblemon/Craftics adapter/playback support.

The reduced version removes forced movement, timed phases, persistent conditions, dynamic hazards and reaction rescues while preserving the investigation, concurrent-cause logic and consequences.
