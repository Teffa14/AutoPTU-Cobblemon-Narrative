# Global NPC AI readiness snapshot — Pass 396

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-10

Narrative baseline before this pass: `115b3f59cf33c2bc6ef1204b8d3cf197b8558c4a`.

## Concrete implementation

Pass 396 adds `tools/global_npc_resource_holder_transitions.py` and `tests/test_global_npc_resource_holder_transitions.py`.

The new layer records explicit checkout, return and authorized handoff holder changes in one contiguous semantic sequence. It does not fabricate gaps and does not claim universal recovery authority yet.

Research/content:
- `research/2026-09-10-holder-transition-field-certification-scan-396.md`;
- `proposals/2026-09-10-the-meter-that-crossed-three-hands-pass-396.md`;
- `design/global-npc-resource-holder-transition-contract-pass-396.md`.

No `canon/` file was changed.

## Read-only AutoPTU evidence

AutoPTU-Java main at inspection: `f4c5c9172e82f7ba01210cb130d982bb1971a992`, merge #422, “Add authoritative combatant-entry ability hook”.

This strengthens evidence for the exact combatant-entry / Impostor Ability path. It does not establish full Ability coverage, full switching semantics, or the complete turn/round lifecycle.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Latest change remains presentation-only.

Neither engine repository was modified.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED only in previously audited scopes.

Base movement legality: VERIFIED only in previously audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in previously audited scopes.

Action economy/initiative: VERIFIED for audited primitives; category-wide lifecycle remains incomplete.

Full turn/round lifecycle: PARTIAL. Merge #422 adds one authoritative entry hook and does not close the category.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated. Impostor entry-path evidence cannot be generalized.

Items: individually gated. A mundane `WorldResource` does not prove PTU Item support.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED for ordinary audited scopes.

AI tactical policy: BLOCKING for rescue-first, escort-first, protect-resource, measurement-first, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for stable objective/resource interaction, holder/pickup/handoff acknowledgement, environmental objective state and authoritative non-KO completion.

## New encounter proposal dependency

`The Meter That Crossed Three Hands` has an implementation-safe reduced version that uses persistent-world state only.

Its mechanically rich version depends explicitly on complete movement for dragging/interception/forced movement; full lifecycle for timed environmental phases; stateful damage/status support for persistent consequences; terrain/weather/hazards/zones/reactions for changing field conditions; exact move/Ability/Item/Trainer Feature support when invoked; tactical policy for non-KO priorities; and adapter/playback support for authoritative objectives.

## Open implementation questions

The holder journal needs deterministic checkpoint/restore before it can participate in Pass 395 post-restore gating.

All production holder mutation callers must eventually route through journal-aware operations before the ledger can be called complete for a covered interval.

After recovery integration, Pass 394 reconciliation can be strengthened: current holder disagreement against a complete recovered transition sequence can become a real conflict rather than remaining indeterminate.

Stable AutoPTU battle/session identity and authoritative in-flight battle recovery remain unresolved.
