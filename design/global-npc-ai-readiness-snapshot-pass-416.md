# Global NPC AI Readiness Snapshot — Pass 416

Status: IMPLEMENTED SLICE / READINESS EVIDENCE

## Repository state inspected

The recursive narrative repository tree at base commit `5bb7d6a0845084cdfdf77758db63d056e6791c30` was inventoried before writing. `CURRENT_FOCUS.md`, canon governance, current Marea/Sendero anchors, global NPC implementation surfaces, AutoPTU session/recovery contracts through Pass 415, recent research/proposals and `sources/kairos/KAIROS_SOURCE_INDEX.md` were checked before selecting this slice.

## Technical progress

Pass 416 adds:

- `tools/autoptu_admitted_result_executor.py`
- `tests/test_global_npc_autoptu_admitted_result_executor.py`
- `design/autoptu-admitted-result-executor-contract-pass-416.md`

The executor accepts only a `RECORD_ADMITTED_RESULT` transition intent. It records the exact result reference on the exact durable session. Same-reference replay is idempotent. A conflicting result fails closed.

The executor deliberately stops at `RESULT_RECORDED`. It does not retire the session, clear `active_autoptu_binding`, move a world agent out of `AUTOPTU_BOUND`, synthesize battle semantics or mutate Minecraft state.

`UNKNOWN` and `EXPLICITLY_ABANDONED` still require their own downstream policy/transition contracts.

## Narrative research completed

New public anchors selected after duplicate-title checks:

- Outer Wilds developer/design interviews: curiosity-driven exploration, knowledge-gated progression and a world that changes independently of player attention.
- Pokémon Shadowside Chapter 4 public release post: a 2026 Pokémon fangame using strong environmental contrast within one island and a traditional-RPG structure outside the Gym Challenge.

Research note:
- `research/2026-09-10-knowledge-route-changing-world-scan-416.md`

Proposal:
- `proposals/2026-09-10-the-route-is-learned-not-unlocked-pass-416.md`

The proposal is PROPOSED / NON-CANON. It does not add a route or hazard to Sendero del Vidrio or Estación Mirador.

## PTU / Caelo / Kairos boundary

The Kairos source index remains a routing aid only. No Skill DC, movement mode, Move effect, Ability effect, Item effect, Trainer Feature, hazard behavior or reaction rule is granted by this pass.

## Engine capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited ordinary scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited calculation paths.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING depending on exact mechanism.

Move-specific behavior: individually gated.

Abilities: PARTIAL and individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for ordinary audited scopes. Specialized traversal, inspect, rescue, protect, interact and extraction actions need explicit admission.

AI tactical policy: BLOCKING for specialized objective policies such as protect-observer, evidence-first withdrawal, route-aware rescue and objective-aware disengagement.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative tactical hazards, specialized interactables, non-KO completion and in-flight tactical recovery.

## Live read-only engine evidence

AutoPTU-Java was inspected at `1c8a4a36711c690f1a485124daf0f6ea191f270e`, merge PR #439, `Freeze Curious Medicine switch-entry oracle`, committed 2026-09-11 UTC. The change freezes Python-oracle evidence for Curious Medicine during switch entry, including nearby combat-stage reset observations. This strengthens one concrete Ability + switch-entry seam. It does not prove the Abilities family, switching family, complete movement, action economy, lifecycle, status lifecycle, hazards or Trainer Features as complete.

AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit explicitly states that the viewport coordinate synchronization change is presentation-only and changes no battle rules or outcomes.

Both engine repositories were treated as read-only.

## Next seam

The next safe technical boundary is world-agent release after a result has been durably recorded. That contract must prove that the selected agent's `active_autoptu_binding` corresponds to the same durable session and exact admitted result before clearing tactical ownership. Session retirement should occur only under an explicit ordering rule that remains safe under replay and restart.

A separate path remains necessary for `UNKNOWN` and explicitly authorized abandonment. Neither state may borrow normal battle-completion semantics.
