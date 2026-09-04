# Engine readiness snapshot — Pass 248

Status: LIVE EVIDENCE SNAPSHOT
Canon effect: NONE

## Read-only engine heads inspected

AutoPTU-Java main: `cc247607ffa28969990465945e814ccd4545fa51` — Freeze Naturewalk forced-movement trap block (#339).

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — presentation-only viewport coordinate synchronization.

No engine repository was modified by this pass.

## Capability classification

Targeting / footprints / range / LoS: VERIFIED within audited contracts.

Base movement legality: VERIFIED within audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Recent Java work proves forced-movement landing consequences and Naturewalk trap blocking for that slice only.

Core calculations: VERIFIED within audited contracts.

Action economy / initiative: VERIFIED within audited contracts.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING outside verified slices. Recent Java evidence strengthens the exact landing-trap semantic seam but does not complete the family.

Move-specific behavior: PARTIAL.

Abilities: PARTIAL.

Items: PARTIAL.

Trainer Features / perks: PARTIAL.

AI legal-action infrastructure: VERIFIED within audited contracts.

AI tactical policy: BLOCKING as a complete family.

Minecraft / Cobblemon / Craftics adapter / playback: PARTIAL / BLOCKING end-to-end.

## Pass 248 dependency result

The reduced ecology-pressure projection slice does not require AutoPTU. It requires Ouros persistent ecology state, Pass 239 lease reconciliation, projection-policy evaluation and the Minecraft/Cobblemon adapter.

A rich pursuit/interception version requires base movement plus complete movement, lifecycle, tactical AI and adapter/playback. Terrain/zones/reactions are required only when the authored chase actually uses them. Damage/status and Move/Ability/Item/Trainer Feature families are required only if those mechanics enter the encounter.

## Current blocking seam

Ouros now has a proposed deterministic contract and fixture for translating resource/disturbance pressure into projection eligibility. The unresolved implementation seam is the actual adapter path that consumes an envelope, reserves an already-counted source and controls or reconciles Cobblemon materialization without letting native spawn state become population truth.
