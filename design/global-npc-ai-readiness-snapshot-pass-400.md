# Global NPC AI Readiness Snapshot — Pass 400

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE

## Concrete change

Pass 400 adds a holder-aware execution path for rescheduled resource handoffs.

New runtime:
- `tools/global_npc_resource_handoff_rescheduling_holder.py`

New regression:
- `tests/test_global_npc_resource_handoff_rescheduling_holder.py`

New research:
- `research/2026-09-10-rescheduled-handoff-journal-and-expedition-duty-scan-400.md`

New narrative candidate:
- `proposals/2026-09-10-the-relief-team-arrived-with-the-right-case-pass-400.md`

## Holder-history status

The new executor checks that a handoff authorization remains current after rescheduling and then routes successful physical transfer through the existing holder-aware handoff runtime.

Successful current successor:
- `ResourceCustodyTransfer` recorded;
- `WorldResource.holder_actor_id` updated;
- one `ResourceHolderTransition(HANDOFF)` recorded;
- transition provenance points to the custody transfer ID.

Superseded or otherwise invalid transfer:
- no custody event;
- no holder event;
- current resource state remains unchanged.

The old compatibility executor in `global_npc_resource_handoff_rescheduling.py` still exists. Holder history must therefore remain explicitly coverage-gated until production callers migrate or that mutation path is removed.

## Engine evidence

AutoPTU-Java read-only head inspected: `16352837e09c9fe07e0d38f8942d1dec96c095bb`, merge #425.

This head materializes authoritative switch field presence. The parity test demonstrates the outgoing combatant leaving the field-presence store and the replacement occupying the resolved destination for the audited switch case.

This strengthens only the switching/field-presence seam. It does not complete full movement, turn lifecycle, Abilities, Trainer Features, objective policy or adapter playback.

AutoPTU Python read-only head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; latest change is presentation-only.

## Permanent capability classification for the Pass 400 rich encounter

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

AI tactical policy: BLOCKING for rescue-first, protect-resource, escort-carrier, transfer-object, abandon-cargo-to-save-person, objective-aware withdrawal and disengage-after-objective.

Minecraft / Cobblemon / Craftics adapter and playback: PARTIAL / BLOCKING for persistent resource projection, handoff acknowledgement, emergency objective state and authoritative non-KO completion.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid, not an automatic grant of rules. Pass 400 adds no Skill, Edge, Feature, Item, hazard, weather, carrying or rescue mechanic.

## Remaining implementation questions

The next holder-history seam is migration or removal of the legacy unjournaled rescheduled-handoff executor, followed by another repository-wide holder mutation audit.

After complete coverage can be demonstrated, `complete_holder_history_resource_ids` can become derivable rather than manually asserted for those resource paths.

Stable AutoPTU battle/session identity and crash recovery remain separate blocking integration work. Persistent-world recovery must not infer that an in-flight battle finished, and Minecraft must not become tactical outcome authority.
