# Global NPC disclosure expectation contract — Pass 301

Status: EXECUTABLE PROPOSED WORLD-AGENT CONTRACT
Date: 2026-09-06

This pass closes a narrow gap left by Pass 300: `SILENT` can now be evaluated against an explicit, provenance-backed expectation to disclose. Ouros still does not infer omissions from absence of speech or from omniscient access to another NPC's private knowledge.

`DisclosureExpectation` binds one speaker, one recipient, one evidence basis and one temporal window. Its basis is explicit request, role duty, faction obligation, promise or emergency warning. Strength is deterministic gameplay policy in the 0..100 range. It is not a psychological probability or a PTU mechanic.

`bind_disclosure_expectation()` converts an active expectation into inputs already consumed by Pass 300. Every active expectation can raise `silence_cost`; role/faction/promise/emergency bases can also raise `obligation_conflict`. The communication-policy resolver remains authoritative for choosing TRUTHFUL, SILENT or DECEPTIVE.

`assess_observable_silence()` evaluates only a concrete communication opportunity and its recorded policy decision. A strong active expectation plus an observed `SILENT` decision can produce `EXPECTATION_BREACHED`. Truthful disclosure and active deception are different communicative acts and are not mislabeled as silence breaches. Expired or weak expectations do not create a breach.

The trust consequence is directional from recipient toward speaker. It uses the existing `RelationshipState` mutation path and a provenance key derived from the finding. `DisclosureBreachRegistry` makes application idempotent across repeated processing and supports a versioned snapshot.

Important boundaries:

Ouros does not scan the world for things an NPC 'should have said'. A role, promise, faction obligation, emergency protocol or explicit request must first produce a concrete expectation through authored/system state.

Knowing information does not automatically create a duty to disclose it.

Silence can be strategically selected without being a breach when no qualifying expectation exists.

A silence breach does not prove malicious intent. It records failure to meet a disclosure expectation. Motive, deception, negligence, incapacity, channel failure and later repair remain separate questions.

The registry snapshot is component durability only. Pass 301 does not yet integrate the registry into `OUROS_NPC_WORLD_CHECKPOINT_V2`.

No PTU, Caelo or Kairos rule is adopted by this contract. PTU remains authoritative for tactical mechanics; this layer is Ouros world-agent policy.

Narrative use: duty-to-warn disputes, rescue dispatch, missing-person escalation, faction reporting chains, tournament safety notices, habitat closures, infrastructure hazards, promises between recurring NPCs and investigations into who was expected to tell whom.

Mechanics dependency: the reduced communication/investigation loop has no AutoPTU dependency. If a resulting scene uses tactical range/LoS, movement, forced movement, damage, statuses, hazards, Moves, Abilities, Items, Trainer Features, tactical AI or Minecraft playback, that exact family must be admitted independently from current engine evidence.