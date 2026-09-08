# Global NPC AI readiness snapshot — Pass 351

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-08

## Narrative repository baseline

Inspected narrative main before writing: `3428a65cae5e22bb6b5e9f03779e168db03a4e90` (Pass 350 snapshot).

Pass 351 closes notice recipient/sender binding and deliberately reuses Pass 287 for actual delivery-triggered knowledge/replanning.

## AutoPTU-Java read-only evidence

Current main inspected: `74691ce736384743807d77a083e99c8513eef6ca`.

Commit message: `Merge pull request #401 from Teffa14/parity/status-effect-mutation-executor — Apply planned status effects through authoritative runtime`.

The inspected diff adds a general `StatusEffectInstruction`, a server-owned `StatusEffectMutationExecutor`, conversion from Arena Trap effect plans to instructions, and oracle parity coverage that compares ordered semantic events plus final Arena Trap `Slowed` status metadata against pinned Python evidence.

This is stronger evidence than Pass 350. Arena Trap can now progress from authoritative target projection through effect planning into authoritative status-state mutation for the audited slice.

It still does not prove:

- expiration/cleanup of `Slowed` after the intended duration;
- every interaction that depends on `Slowed` during movement/action resolution;
- the full status lifecycle family;
- the complete Ability family;
- complete movement;
- Minecraft/Cobblemon playback of every resulting semantic event.

GitHub Actions query for this head reported 77 workflow runs. Visible sampled runs were completed successfully, including parity workflows.

## AutoPTU Python read-only evidence

Current main remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its head explicitly describes a viewport-coordinate synchronization regression as presentation only and states that battle rules and outcomes do not change.

No capability family is promoted from this Python head.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within the ordinary audited contracts. Arena Trap has additional authoritative runtime candidate projection evidence.

Base movement legality: VERIFIED within the ordinary audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Numeric Burrow representation and ordinary movement legality do not establish carrying, interception, forced movement or all movement interactions.

Core calculations: VERIFIED within audited deterministic arithmetic scope.

Action economy/initiative: VERIFIED for audited primitives. Tactical pickup/drop/handoff and other objective-specific actions remain individually gated.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL. PR #401 proves authoritative status mutation for the Arena Trap slice, but not complete duration expiration, cleanup or all status interactions.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family.

Move-specific behavior: PARTIAL and individually gated.

Abilities: PARTIAL. Arena Trap now has target projection, effect planning and authoritative status mutation evidence. One Ability does not establish family completeness.

Items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited action-generation scope.

AI tactical policy: BLOCKING for escort, protect-carrier, preserve-resource, delivery-first, intercept-without-elimination and disengage-after-objective goals.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end. Server-owned semantics are moving in the correct direction, but complete authoritative playback/ack integration is not verified.

## Pass 351 encounter dependency note

The reduced wrong-recipient notice case needs no AutoPTU battle.

A rich catch-up/interception branch requires exact capability gates. Ordinary route movement can use verified base movement. Physical interception, carrying, push/pull, knockback or forced displacement depend on complete movement. Round deadlines depend on full lifecycle. Persistent conditions depend on status lifecycle. Any route weather/hazard/zone/reaction needs its exact family. Any Move, Ability, Item or Trainer Feature remains individually gated. Non-elimination escort/intercept decisions remain blocked on AI tactical policy. Minecraft playback remains separately gated.

## Unresolved engine questions

- Does the next Arena Trap slice prove one-round expiration and cleanup through the normal lifecycle owner?
- Are movement restrictions produced by `Slowed` consumed by all authoritative movement paths?
- Is status event playback/acknowledgement complete through Minecraft/Cobblemon/Craftics?
- What exact contracts will own cargo, escort and interception objectives without duplicating PTU rules in the adapter?
