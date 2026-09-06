# Global NPC AI readiness snapshot — Pass 306

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

Narrative repo head before Pass 306: `44acc0395778d4530f0a57ebdbbc8d9ac1e29cf2`.

## Read-only engine evidence

AutoPTU-Java advanced to `3ca3540a94bafdb57ff69d2feaa56ec0b3d65d3b` through PR #381, `Add reusable post-damage faint transition contract`.

The commit adds a shared server-owned post-damage classification for whether an actor was fainted before, is fainted after, and transitioned alive-to-fainted. Ordinary damage ingress exposes that classification and the Python parity gate asserts the result against pinned oracle cases.

This is positive evidence for one specific post-damage transition seam. The commit itself continues to exclude Substitute, prevention/reactions, Injuries, faint prevention, history rotation, semantic events and source attribution. It therefore strengthens but does not complete the full stateful damage pipeline or full lifecycle.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its live head remains presentation-only and explicitly changes no battle rules or outcomes.

## Capability classification

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL; PR #381 strengthens the narrow post-damage faint-transition seam but does not close the omitted pipeline families;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

No category is promoted by Pass 306 or by Java PR #381.

## Pass 306 dependency boundary

Evidence-custody reasoning is world-simulation state over per-agent provenance-backed records and requires no AutoPTU tactical capability.

The proposed full recovery encounter activates only the capability families actually authored: ordinary traversal can use verified base movement; spatial interaction may use verified targeting/range contracts; forced rescue movement or wind displacement requires complete movement; timed surges require lifecycle; damage requires the full stateful damage pipeline; persistent conditions require status lifecycle; active weather/debris/electrical zones/reaction rescues require terrain/weather/hazards/zones/reactions; mechanically active Moves/Abilities/Items/Trainer Features require their owner families; autonomous tactical behavior requires AI tactical policy; authoritative presentation requires the Minecraft/Cobblemon/Craftics adapter/playback layer.

The reduced version removes forced movement, delayed phases, dynamic hazards, statuses and tactical autonomy while preserving the custody investigation and narrative consequences.
