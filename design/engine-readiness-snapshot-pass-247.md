# Engine readiness snapshot — Pass 247

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03

## Read-only engine heads checked

AutoPTU-Java `main`: `cc247607ffa28969990465945e814ccd4545fa51` — `Freeze Naturewalk forced-movement trap block (#339)`. The commit verifies one forced-movement landing/trap/Naturewalk semantic-event slice. It does not prove the complete movement or terrain/hazard families.

AutoPTU Python `main`: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — presentation-only coordinate synchronization. No new rules-parity evidence for this pass.

## Capability families

- targeting/footprints/range/LoS: VERIFIED within audited contracts.
- base movement legality: VERIFIED within audited contracts.
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
- core calculations: VERIFIED within audited contracts.
- action economy/initiative: VERIFIED within audited contracts.
- full turn/round lifecycle: PARTIAL.
- full stateful damage pipeline: PARTIAL.
- status lifecycle: PARTIAL.
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices.
- move-specific behavior: PARTIAL.
- abilities: PARTIAL.
- items: PARTIAL.
- Trainer Features/perks: PARTIAL.
- AI legal-action infrastructure: VERIFIED within audited contracts.
- AI tactical policy: BLOCKING as a complete family.
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

## Pass 247 reduced-version readiness

The resource-scarcity trace itself needs no AutoPTU adjudication. Its world-state reducer, event hysteresis, observation boundary and NPC-knowledge lag are Ouros concerns and are now covered by executable regression tests.

Production remains blocked on adapter/persistence seams that capture authorized visible observations, persist resource/event state and project behavior changes without treating Minecraft entity counts as ecological truth.

## Rich-version dependency

A structured contest over access to a recovering patch would require targeting/range/LoS, base movement, action economy, AI legal-action infrastructure and adapter/playback at minimum. Interception/displacement requires complete movement. Timed access phases require full lifecycle. Tactical zones/weather/hazards require that family. Any attacks add the damage/status pipelines plus exact Move/Ability/Item/Trainer Feature validation.

No capability family is promoted by Pass 247.
