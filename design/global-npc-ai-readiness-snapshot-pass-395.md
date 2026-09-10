# Global NPC AI Readiness Snapshot — Pass 395

Status: DESIGN / READINESS. Not canon.
Date: 2026-09-10

## Slice completed

Pass 395 adds an explicit post-restore activation stage after coherent recovery generation selection and independent owner restore.

Executable seam:
- `tools/global_npc_persistent_world_post_restore.py`
- `tests/test_global_npc_persistent_world_post_restore.py`

The stage requires a reconciled V2 persistent-world recovery manifest, a restored WorldResource catalog from the same semantic minute, and restored reservation/handoff histories. It runs Pass 394 reconciliation and fails closed on explicit conflicts while preserving indeterminate findings for diagnostics and narrative use.

## Recovery boundary

`MANIFEST_SELECTION -> OWNER_RESTORE -> CROSS_OWNER_VALIDATION -> WORLD_ACTIVATION`

Pass 395 owns only the third stage.

It does not alter current resources, reservations, handoffs, private knowledge, evidence, AutoPTU state or Minecraft state.

## Engine evidence

Read-only AutoPTU-Java head inspected: `19dd2d9b99d81f8479c73e6ef4709a30f0794474`, merge #421.

The current evidence strengthens the specific Impostor negative-guard and lifecycle-hook paths covered by that merge. It does not justify promotion of the full Abilities family or the full turn/round lifecycle.

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Latest change remains presentation-only.

## Permanent capability categories

Targeting/footprints/range/LoS: VERIFIED within audited scopes.

Base movement legality: VERIFIED within audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited scopes.

Action economy/initiative: VERIFIED only for audited primitives.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED.

Items: INDIVIDUALLY GATED.

Trainer Features/perks: INDIVIDUALLY GATED.

AI legal-action infrastructure: VERIFIED for ordinary audited scopes.

AI tactical policy: BLOCKING for rescue-first, escort-first, protect-resource, retrieve-object, transfer-object, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative objective acknowledgement, persistent resource projection, escort/rescue state and non-KO completion playback.

## New narrative candidate

`proposals/2026-09-10-kit-that-returned-before-team-pass-395.md` is PROPOSED / NON-CANON.

Its reduced version is world-state investigation and logistics only. Its rich version declares every tactical dependency rather than requiring the adapter to reproduce missing PTU behavior.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked only as a router toward supplied source material. No new Skills, Edges, Trainer Features, Items, environmental modifiers, rescue mechanics or interrupts were authorized by Pass 395.

## Next seams

A complete authoritative holder-transition journal remains necessary before current holder mismatches can be strengthened beyond indeterminate where checkout, return or other legal mutations may explain the state.

In-flight AutoPTU recovery remains separate and higher risk. Stable battle/session identity, authoritative tactical state/result and restart reconciliation must exist before persistent-world recovery may resume around a battle without guessing that the battle completed.

Production Minecraft acknowledgement also remains incomplete for resource pickup/handoff and non-KO objective completion.
