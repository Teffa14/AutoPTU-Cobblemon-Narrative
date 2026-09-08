# Global NPC AI readiness snapshot — Pass 345

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

Narrative repository writable target

`Teffa14/AutoPTU-Cobblemon-Narrative`

Pass 345 adds communication-aware pre-handoff confirmation/cancellation semantics and no AutoPTU rules.

## Read-only engine evidence

AutoPTU-Java head inspected: `30ff159abafbef6d14ef4a776789e9077dd26bc4`, merge of PR #398, `Preserve numeric Burrow speed in movement profiles`.

PR #398 changes `MovementProfile` so Burrow retains a numeric speed rather than collapsing to a boolean. Regression coverage distinguishes Burrow 3 from Burrow 4, preserves the value through position changes and gives legacy boolean data only a minimal compatibility value. This is useful evidence for movement-profile representation and exact threshold checks.

The commit has 77 reported check runs. Retrieved checks including parity and movement-related suites were completed successfully. This remains narrow evidence and does not prove all movement interactions.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its latest commit states that the change is presentation-only and does not change battle rules or outcomes. Python remains read-only for this task.

## Permanent capability categories

Targeting / footprints / range / LoS: VERIFIED for previously audited ordinary contracts. PR #398 does not change this assessment.

Base movement legality: VERIFIED for previously audited ordinary contracts. Numeric Burrow speed representation is stronger live evidence for movement-profile inputs but is not a promotion of richer movement interactions.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Numeric Burrow speed does not prove carrying, interception, forced movement, push/pull or all Burrow interactions.

Core calculations: VERIFIED for previously audited deterministic arithmetic.

Action economy / initiative: VERIFIED for current audited primitives.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL and individually gated. Earlier Air Lock and Arena Trap slices remain representative evidence only.

Items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED for its currently audited ordinary legal-action scope.

AI tactical policy: BLOCKING for objective-aware delivery, protection, retreat, warning and route-progress policy.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING end-to-end. Presentation cannot establish communication receipt, appointment knowledge, custody or PTU truth.

## Pass 345 encounter dependency

Reduced `The Cancellation Beyond Coverage` case has no structured battle dependency. It uses semantic time, handoff authorization, existing communication delivery truth, appointment notices, travel, failed-attempt provenance, memory/belief and replanning.

A richer route encounter needs the exact capability families it invokes. Ordinary movement can rely on the verified base-movement scope. Interception/carrying/forced movement remains dependent on PARTIAL complete movement. Round-bound deadlines depend on PARTIAL lifecycle. Equipment or actor damage depends on PARTIAL stateful damage. Persistent combat conditions depend on PARTIAL status lifecycle. Dynamic environment mechanics remain gated by terrain/weather/hazard/zone/reaction coverage. Every Move, Ability, Item and Trainer Feature remains individually gated. Objective-aware delivery behavior remains blocked on tactical policy. Minecraft remains presentation only.

## PTU / Caelo boundary

The narrative source policy continues to treat PTU Core, Pokédex material and supplied Caelo material as the authority boundary for exact game mechanics.

Pass 345 introduces no PTU communication Action, Skill DC, Feature, Move, Ability, Item effect or hearing rule. No new PTU/Caelo mechanical claim therefore requires adoption in this slice.

## Open questions after Pass 345

The next integration questions are operational rather than combat-rule questions: when a cancellation becomes operationally binding, how reschedule acceptance creates a replacement authorization, how appointment delivery should wake affected actors without duplicating the existing Pass 287 coordinator, how travel departure/arrival evidence should interact with stale appointment knowledge, how no-show expiry should be materialized, and how the new resource ledgers enter coherent world checkpoints.
