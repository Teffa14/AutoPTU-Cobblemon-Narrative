# Global NPC AI readiness snapshot — Pass 303

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-06

Narrative repo head before Pass 303: `cc23de2478ae04395130673de1756565fd0f935b`.

Read-only engine evidence checked during this pass:

AutoPTU-Java remains `c06eee09a22c9c3459f23a320a1fbdbe99059119` via PR #378, `Freeze temporary-HP absorption against Python oracle`. That work freezes the already narrow ordinary-damage temporary-HP absorption seam against a Python oracle. It does not add downstream HP mutation, Injuries, faint prevention, battle history, broad damage ordering or adapter evaluation.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its live head remains presentation-only and does not change battle rules or outcomes.

Capability classification remains conservative:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL; PR #378 validates only the temporary-HP absorption seam;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: BLOCKING for general autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end.

Pass 303 itself is world-simulation only. Evidence-based attribution of an infrastructure failure has no tactical dependency.

The full proposed relay-site inquiry inherits only the families actually authored into its mechanically active version. Ordinary traversal can use verified base movement. Wind/debris forced displacement or rescue interception requires complete movement. Timed collapses/surges require full lifecycle. Mechanical environmental damage requires the stateful damage pipeline. Persistent conditions require status lifecycle. Active storm, debris and electrical zones require terrain/weather/hazards/zones/reactions. Any Move, Ability, Item or Trainer Feature requires its owner family. Autonomous rescue/combat selection requires AI tactical policy. Visible authoritative execution requires Minecraft/Cobblemon/Craftics adapter/playback.

The reduced version removes forced movement, timed hazard phases, persistent conditions and dynamic hazard zones while retaining the same investigation premise and evidence graph.

No capability category is promoted by Pass 303 or by the unchanged Java evidence.
