# Global NPC AI readiness snapshot — Pass 304

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

Narrative repo head before Pass 304: `746a47a1494d5a44e3742993d69a698a09facde4`.

Read-only engine evidence checked during this pass:

AutoPTU-Java advanced to `3c6d641c63b33d8ab3ace4d90539dbad2975b8c2` via PR #379, `Add server-owned ordinary damage ingress`. The new server-owned boundary clamps incoming ordinary damage, applies temporary-HP absorption, then mutates canonical normal HP with the remainder. The commit also gates that state transition against a pinned Python oracle. Its own contract explicitly leaves substitute/prevention/reactions, injuries, faint handling, history rotation, semantic events and source attribution to other pipeline stages.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its live head remains presentation-only and does not change battle rules or outcomes.

Capability classification remains conservative:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL; PR #379 adds an authoritative ordinary-damage ingress seam through temporary HP into normal HP, but explicitly excludes prevention/reactions, Injuries, faint handling, history, semantic events and attribution;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

Pass 304 itself is world-simulation persistence only and requires no tactical capability family.

The full proposed reopened-relay encounter inherits only the families it actually activates. Ordinary traversal can use verified base movement. Wind displacement and interception rescue require complete movement. Timed surges require full lifecycle. Environmental damage requires the full stateful damage pipeline, not merely PR #379's ordinary ingress seam. Persistent conditions require status lifecycle. Active storm/debris zones and reactions require terrain/weather/hazards/zones/reactions. Any mechanically active Move, Ability, Item or Trainer Feature requires its owner family. Autonomous rescue/combat selection requires AI tactical policy. Visible authoritative execution requires Minecraft/Cobblemon/Craftics adapter/playback.

The reduced version removes forced movement, timed hazard phases, persistent conditions, dynamic hazard zones and reaction rescues while retaining the same investigation and persistence premise.

No capability category is promoted by Pass 304. PR #379 strengthens evidence inside the stateful damage pipeline but does not complete that category.
