# Global NPC AI readiness snapshot — Pass 307

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

Narrative repo head before Pass 307: `b796c1a8fb212837cb7e8efc72dfbc6f451243fb`.

## Read-only engine evidence

AutoPTU-Java remains at `3ca3540a94bafdb57ff69d2feaa56ec0b3d65d3b`, PR #381, `Add reusable post-damage faint transition contract`.

That commit provides a server-owned post-damage classification for whether an actor was fainted before damage, is fainted after damage, and crossed alive-to-fainted. Ordinary damage ingress exposes this classification and the Python parity gate checks pinned oracle cases.

This is narrow but valid evidence for the stateful damage pipeline. The same live change still excludes Substitute, prevention/reactions, Injuries, faint prevention, history rotation, semantic events and source attribution. The full stateful damage pipeline therefore remains PARTIAL.

AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its current head is presentation-only and explicitly changes no battle rules or outcomes.

## Capability classification

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
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

No category is promoted by Pass 307.

## Pass 307 dependency boundary

Atomic persistence of evidence-custody state is world-simulation infrastructure and requires no AutoPTU tactical capability. It consumes the existing private KnowledgeLedger and the Pass 306 EvidenceCustodyRegistry.

The proposed full annex/reopened-evidence encounter activates only the capability families actually authored. Ordinary traversal can remain on verified base movement. Wind displacement, rescue interception and other forced relocation require complete movement. Timed collapse or weather phases require full turn/round lifecycle. Authoritative environmental damage requires the full stateful damage pipeline. Persistent PTU conditions require status lifecycle. Mechanically active debris, weather, zones and reaction rescues require terrain/weather/hazards/zones/reactions. Move, Ability, Item and Trainer Feature effects require their owning families. General autonomous combat choice requires AI tactical policy. End-to-end authoritative presentation requires Minecraft/Cobblemon/Craftics adapter/playback support.

The reduced version removes forced movement, delayed phases, dynamic hazards, statuses and general tactical autonomy while preserving the investigation, custody history, restart durability and downstream social consequences.
