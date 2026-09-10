# Global NPC AI Readiness Snapshot — Pass 401

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE

## Concrete change

Pass 401 closes the known rescheduled-handoff holder-history bypass.

Updated runtime:
- `tools/global_npc_resource_handoff_rescheduling.py`

Updated regression:
- `tests/test_global_npc_resource_handoff_rescheduling.py`

Existing successful holder-aware runtime remains:
- `tools/global_npc_resource_handoff_rescheduling_holder.py`
- `tests/test_global_npc_resource_handoff_rescheduling_holder.py`

New research:
- `research/2026-09-10-legacy-handoff-closure-and-delayed-ruins-interpretation-scan-401.md`

New narrative candidate:
- `proposals/2026-09-10-the-rubbing-that-made-sense-later-pass-401.md`

## Holder-history status

The legacy reschedule executor can no longer produce an accepted transfer.

A current authorization now returns `HOLDER_TRANSITION_LEDGER_REQUIRED` without mutating resource or custody state. A superseded authorization still returns `HANDOFF_AUTHORIZATION_SUPERSEDED`.

Accepted rescheduled transfers must use the Pass 400 holder-aware executor, which creates custody history and a matching HANDOFF holder transition.

Repository-wide direct-call search at this pass found the lower-level `execute_authorized_handoff()` in its defining module, tests, the holder-aware wrapper and the now-closed legacy reschedule location. No second reschedule-specific production bypass was found.

This strengthens completeness for the rescheduled-handoff path. Future holder mutation paths still require audit before universal completeness can be inferred.

## Research contribution

Two previously unused named research anchors were added:

- P.U.C.L. PTU: field evidence gathered during one activity can become relevant later when shared in another context.
- PMD: Maelstrom: exploration rewards can expand future expedition options and create follow-up exploration nodes.

The resulting Ouros candidate uses established Marea anchors but remains non-canon. A minor observation from an optional field trip can become meaningful only after later archive context, then motivate a second expedition.

## Engine evidence

AutoPTU-Java read-only head inspected: `16352837e09c9fe07e0d38f8942d1dec96c095bb`, merge #425, `Materialize authoritative switch field presence`.

That head strengthens only the audited switching/field-presence seam: outgoing field presence is removed and replacement presence is materialized at the resolved destination for the covered switch flow. It does not establish complete movement, general forced movement, full switching, full lifecycle, Abilities, Trainer Features, AI objective policy or adapter playback.

AutoPTU Python read-only head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The latest commit remains presentation-only and states that battle rules/outcomes are unchanged.

## Permanent capability classification for the Pass 401 rich encounter

Targeting / footprints / range / LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy / initiative: audited primitives VERIFIED; complete family PARTIAL.

Full turn / round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING by exact mechanic.

Move-specific behavior: individually gated.

Abilities: individually gated.

Items: individually gated.

Trainer Features / perks: individually gated.

AI legal-action infrastructure: VERIFIED only in audited ordinary scopes.

AI tactical policy: BLOCKING for investigate-first, protect-researcher, preserve-evidence, rescue-first, avoid-damaging-site, objective-aware withdrawal and disengage-after-objective.

Minecraft / Cobblemon / Craftics adapter and playback: PARTIAL / BLOCKING for persistent site revision, evidence interaction, environmental objective state and authoritative non-KO completion.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid. Pass 401 adds no Skill, Edge, Feature, Item, climbing rule, survey modifier, hazard, weather rule, puzzle check or tactical interrupt.

## Remaining implementation questions

The next holder-history step is to make coverage derivation explicit rather than manually asserted for paths now proven journal-complete, while retaining a fail-closed default for unknown/future mutation paths.

The larger unresolved integration problem remains stable AutoPTU battle/session identity and crash recovery. The persistent world must not infer that an in-flight battle ended, and Minecraft must not become tactical outcome authority.

Narrative questions for the new candidate remain open: exact site, first observation, later archive record, physical change, participating NPCs, any Pokémon encounter and any PTU/Caelo mechanics.
