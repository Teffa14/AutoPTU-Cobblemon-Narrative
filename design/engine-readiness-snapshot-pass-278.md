# Engine readiness snapshot — Pass 278

Status: evidence snapshot for narrative dependency gating. AutoPTU-Java and AutoPTU inspected read-only; this pass changes only the narrative repository.

Read-only heads inspected

AutoPTU-Java: `6d306a92300428d527df064c80239e320bb4e1ca`, merge PR #355 “Preserve rich move-special target composition order”.

AutoPTU Python: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, viewport synchronization explicitly described as presentation-only.

Capability classification

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

Live Java evidence

PR #355 adds `RuntimeMoveSpecialTargetComposition` and a regression that preserves ordering across pre-resolution, move-special PRE_DAMAGE, pre-damage reactions, ordinary post-damage hooks, the committed/post-move-special outcome and post-hit forced-movement event transport. The helper preserves the target result snapshot and applied damage while composing later event stages.

This is concrete evidence for one runtime composition seam. It does not establish complete movement merely because the regression transports a forced-movement event. It also does not establish complete reaction coverage, full lifecycle coverage, full damage-pipeline coverage, all move-specific behavior or a public typed Ouros semantic-result boundary.

Live Python evidence

No newer mechanical evidence exists at the inspected head. The current main commit explicitly states that its viewport-resize change is presentation-only and does not change battle rules or outcomes.

Pass 278 reduced profile

The contested-stewardship evidence loop requires no AutoPTU capability. It uses persistent evidence/provenance records, semantic windows, Pass 277 accountability state, the Pass 278 evidence-contest contract and Minecraft/Cobblemon presentation.

Pass 278 mechanically rich gates

Tactical detection or selection uses targeting/footprints/range/LoS.

Ordinary traversal uses base movement legality.

Push, pull, knockback, interception and forced displacement require complete movement, still PARTIAL. The presence of a forced-movement event in the new Java composition-order regression is not evidence that the entire family is complete.

Adopted PTU arithmetic uses core calculations.

Structured sequencing uses action economy/initiative; phase-spanning behavior needs full turn/round lifecycle, still PARTIAL.

Persistent damage needs the full stateful damage pipeline, still PARTIAL. Persistent conditions need status lifecycle, still PARTIAL.

Mechanical terrain, weather, hazards, zones or reactions need terrain/weather/hazards/zones/reactions, still MIXED/PARTIAL/BLOCKING.

Exact Moves, Abilities, Items and Trainer Features/perks remain gated by their PARTIAL families.

AI legal-action infrastructure can enumerate legal actions. Autonomous confrontation, enforcement, escort, withdrawal or evidence-protection behavior requires AI tactical policy, still BLOCKING.

Live rendering and authoritative playback remain dependent on Minecraft/Cobblemon/Craftics adapter/playback support, still PARTIAL/BLOCKING end-to-end.

Evidence-dispute boundary

A challenged report, reviewer disagreement, grievance or accountability finding cannot create PTU movement, reactions, damage, status, protected-zone semantics, authority, a battle result or ecological truth.

No capability promotion

Pass 278 promotes no capability family. PR #355 strengthens the move-special target composition seam but remains too narrow for a category-wide promotion.

Caelo/Kairos boundary

No Caelo rule was available locally or adopted. Kairos remains comparative under `design/ouros-source-authority-and-species-policy.md`. No source-specific governance, evidence or tactical rule becomes Ouros mechanics through this pass.