# Engine readiness snapshot — Pass 243

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03

## Read-only heads inspected

AutoPTU-Java: `c5ca00d22cc234d0ec8dc0429e60f8ee42381dec`

Latest relevant change: `Freeze terrain-trap semantic event payload (#337)`. The commit freezes the tile-trap semantic event shape against the Python oracle and exposes the contract through parity/CI artifacts. This is evidence for that narrow tile-entry/trap seam only.

AutoPTU Python oracle: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Latest commit remains presentation-only (`Career: keep battle coordinates synced after viewport resize (#237)`). It adds no new PTU rules evidence for this pass.

## Capability classification

- targeting / footprints / range / LoS: VERIFIED within audited contracts
- base movement legality: VERIFIED within audited contracts
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED within audited contracts
- action economy / initiative: VERIFIED within audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features / perks: PARTIAL
- AI legal-action infrastructure: VERIFIED within audited contracts
- AI tactical policy: BLOCKING as a complete family
- Minecraft / Cobblemon / Craftics adapter and playback: PARTIAL / BLOCKING end-to-end

## Pass 243 implication

The narrative regression harness validates ecology-side conservation, authority boundaries, projection leases, evidence flow, event thresholds and handoff gating. It does not promote any PTU capability category because it deliberately does not adjudicate attacks, movement legality, statuses, terrain mechanics or tactical AI.

The newly frozen AutoPTU-Java trap semantic payload is useful for future cross-repo handoff tests. A future integration trace may consume a verified semantic result envelope, but it must continue to mark any unverified terrain/weather/reaction behavior as partial or blocking.
