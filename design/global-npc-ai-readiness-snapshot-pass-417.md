# Global NPC AI Readiness Snapshot — Pass 417

Status: IMPLEMENTED SLICE / READINESS EVIDENCE

Repository state inspected

The recursive narrative repository tree at base commit 7ff589207fff36489762092143c9ac08b8d055d1 was inventoried before writing. CURRENT_FOCUS.md, the complete canon inventory, global NPC implementation surfaces, AutoPTU session/recovery contracts through Pass 416, current research/proposals and sources/kairos/KAIROS_SOURCE_INDEX.md were checked before selecting this slice.

Technical progress

Pass 417 adds:

- tools/autoptu_world_agent_release.py
- tests/test_global_npc_autoptu_world_agent_release.py
- design/autoptu-world-agent-release-contract-pass-417.md

The new boundary separates world-agent release from session retirement.

Phase one accepts only an exact RESULT_RECORDED session/result pair and an exact participating world agent. If that agent remains AUTOPTU_BOUND, its active_autoptu_binding must equal the selected durable session. The agent is released through the existing global NPC primitive while the session deliberately remains RESULT_RECORDED.

Phase two permits retirement only after the selected agent has no AutoPTU binding and is no longer AUTOPTU_BOUND. Participant identity and the authoritative result reference are checked again. Same-state replay is idempotent.

The safe crash intermediate is therefore a released agent plus a RESULT_RECORDED session. Retirement is never allowed to race ahead while the NPC still advertises tactical ownership.

Narrative research completed

New public anchors selected after duplicate-title checks:

- Pokémon Starwish Demo: an adult courier revisits a familiar region years later, providing a useful high-level pattern for ordinary work, changed context and revisiting known geography.
- Pokémon Unchosen: local co-op lets another participant control a party Pokémon in exploration and battle, providing a high-level pattern for one objective with multiple independent actors.

Research note:
- research/2026-09-10-shared-assignment-field-team-scan-417.md

Proposal:
- proposals/2026-09-10-the-assignment-does-not-pause-when-you-split-up-pass-417.md

The proposal is PROPOSED / NON-CANON. No new assignment, institution, incident or NPC duty is promoted into canon.

PTU / Caelo / Kairos boundary

The Kairos source index remains a routing aid only. This pass grants no Skill DC, movement mode, Move behavior, Ability behavior, Item effect, Trainer Feature, hazard rule or reaction behavior.

Engine capability posture

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

AI legal-action infrastructure: VERIFIED only for ordinary audited scopes. Specialized protect, retrieve, escort, carry, interact and extraction actions need explicit admission.

AI tactical policy: BLOCKING for specialized objective policies such as objective-first movement, protect-partner, evidence-first withdrawal and objective-aware disengagement.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative tactical objective state, specialized interactables, non-KO completion and in-flight tactical recovery.

Live read-only engine evidence

AutoPTU-Java was inspected at 1c8a4a36711c690f1a485124daf0f6ea191f270e, merge PR #439, Freeze Curious Medicine switch-entry oracle, committed 2026-09-11 UTC. The commit freezes a Python oracle for one switch-entry Ability behavior involving nearby combat-stage reset observations. This strengthens that specific Ability + switch-entry seam only. It does not prove the Abilities family, switching family, complete movement, action economy, turn lifecycle, status lifecycle, hazards or Trainer Features as complete.

AutoPTU Python remains at 729bae2d424963ff9bb3f4159c9a7ac9152128a7. Its latest known change remains presentation-only and does not change battle rules or outcomes.

Both engine repositories were treated as read-only.

Next seam

The next safe boundary is consequence application after session retirement. A future contract must consume the already-admitted semantic result and apply only world consequences that the result schema explicitly authorizes, with idempotent provenance and no reconstruction of hidden tactical state.

UNKNOWN engine authority and explicitly authorized abandonment remain separate paths. Neither may borrow normal battle-completion semantics.
