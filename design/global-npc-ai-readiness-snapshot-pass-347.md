# Global NPC AI readiness snapshot — Pass 347

Status: LIVE EVIDENCE SNAPSHOT / NOT CANON

This file records the evidence used during Pass 347. It does not promote unverified engine families.

## Narrative repository evidence

Pass 347 adds a resource-window admission seam for rescheduled handoffs. The implementation is a pure read model over the existing Pass 339 reservation ledger plus Pass 343/346 handoff state.

New executable owner:
- `tools/global_npc_resource_handoff_reschedule_admission.py`

New regression coverage:
- `tests/test_global_npc_resource_handoff_reschedule_admission.py`
- `implementation/global-npc-resource-handoff-reschedule-admission-regression-v1.json`

Global NPC AI Regressions run #211 completed successfully on commit `bdaa81e2a83056697b0c29015a1df4f0a20b0e5a`, covering the new admission tests through the pytest-based global NPC suite.

A separate repository QA defect was exposed because the ecology validator and ecology workflow were sweeping unrelated global-NPC fixtures/tests. Pass 347 adds explicit ecology-owned discovery in `tools/ecology_fixture_scope.py`, a scoped validation entrypoint, a regression guard in `tests/test_ecology_fixture_validator.py`, and narrows ecology test discovery to `test_ecology_*.py`. No ecology fixture semantics were changed.

## Read-only AutoPTU-Java evidence

Observed head during this pass:

`30ff159abafbef6d14ef4a776789e9077dd26bc4`

This remains the merge of PR #398, `Preserve numeric Burrow speed in movement profiles`.

The slice preserves numeric Burrow speed in movement profiles and tests distinct numeric values. This is meaningful evidence for movement-profile representation. It does not establish carrying, interception, push/pull, knockback, rescue, forced movement, all Burrow interactions, or complete movement as a family.

No newer AutoPTU-Java head was observed during this pass.

## Read-only AutoPTU Python evidence

Observed head during this pass:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

The head remains the presentation-only coordinate synchronization change already audited in earlier passes. Its own scope states that battle rules and outcomes are unchanged.

No Python mechanic is promoted from that commit.

## Permanent capability categories

### Targeting / footprints / range / LoS
VERIFIED within the ordinary contracts already audited by the engine project.

Pass 347 does not depend on tactical targeting in its reduced form.

### Base movement legality
VERIFIED within the ordinary contracts already audited.

The reduced resource-conflict scene can use world travel without invoking tactical movement. Numeric Burrow preservation strengthens representation but is not used to broaden this category.

### Complete movement including push/pull/knockback/interception/forced movement
PARTIAL.

A rich courier or escort encounter that physically intercepts a carrier depends on this family. Pass 347 provides no new evidence for it.

### Core calculations
VERIFIED within the ordinary deterministic contracts already audited.

### Action economy / initiative
VERIFIED for the audited primitives.

Exact tactical pickup, drop, handoff, equip or protect-resource actions remain individually gated.

### Full turn / round lifecycle
PARTIAL.

Any encounter using round-counted delivery deadlines or timed tactical phases depends on this family.

### Full stateful damage pipeline
PARTIAL.

Required if a carrier or transported instrument can take authoritative tactical damage.

### Status lifecycle
PARTIAL.

Required for persistent conditions affecting carrier, pursuer, equipment or objective state.

### Terrain / weather / hazards / zones / reactions
MIXED / PARTIAL / BLOCKING by exact family.

A rich route encounter must declare each used family separately. World scheduling does not infer tactical terrain legality.

### Move-specific behavior
PARTIAL.

Each Move used by a rich encounter remains individually gated.

### Abilities
PARTIAL.

Representative Ability slices from prior engine work do not establish the whole family.

### Items
PARTIAL.

A conflict-free `WorldResource` does not prove that an equivalent PTU Item effect is implemented. World logistics and tactical Item behavior remain separate authorities.

### Trainer Features / perks
PARTIAL.

Any Feature used to interrupt, alter movement, authorize an action or change a tactical consequence requires exact current evidence.

### AI legal-action infrastructure
VERIFIED for the ordinary audited action-generation scope.

Pass 347 does not add tactical actions.

### AI tactical policy
BLOCKING for rich non-defeat objectives such as escorting a carrier, protecting a delivery, disengaging after successful delivery, choosing whether to abandon equipment for rescue, or prioritizing route progress over total defeat.

### Minecraft / Cobblemon / Craftics adapter and playback
PARTIAL / BLOCKING end-to-end.

Minecraft may present locations, actors, equipment and travel. It must not decide reservation authority, conflict priority, recipient knowledge, PTU legality or battle aftermath.

## Pass 347 encounter dependency summary

Reduced `The Window Someone Else Needed`:
- no AutoPTU dependency;
- requires semantic time, resource IDs, reservation state, delivered communication, handoff/reschedule state, travel, belief and replanning;
- current resource conflict assessment is executable in the narrative repository.

Rich continuation after physical pickup:
- ordinary targeting/base movement/core arithmetic/action primitives can use verified audited coverage where exact contracts match;
- interception/carrying/forced displacement remains dependent on complete movement;
- tactical deadlines depend on full lifecycle;
- authoritative injury/damage depends on the stateful damage pipeline;
- persistent tactical conditions depend on status lifecycle;
- weather/hazards/zones/reactions, Moves, Abilities, Items and Trainer Features remain exactly gated;
- delivery-first or escort behavior remains blocked on richer AI tactical policy;
- presentation remains adapter-gated.

## Unresolved questions

- Which institutional role owns arbitration when two legitimate obligations compete for one indivisible resource?
- Should resource-window admission be mandatory before `record_reschedule_decision(ACCEPT)`, or should an actor be allowed to accept socially while producing a known allocation conflict for later resolution?
- How should institutional priority policy be represented without embedding local policy in the global planner?
- When a proposed window is open-ended, what bounded planning horizon is authoritative for conflict screening?
- When another compatible unit exists, which owner may offer substitution and how is its readiness checked before the offer becomes actionable?
- Resource request, reservation, handoff, attempt, appointment and reschedule ledgers still need integration with the atomic world checkpoint rather than parallel persistence.
- Arrival/departure evidence should eventually come from the travel runtime rather than authored convenience facts.
- PTU/Caelo mechanics remain authoritative whenever a world resource maps to a mechanically active Item.
