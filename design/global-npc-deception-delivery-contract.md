# Global NPC deception delivery contract — Pass 296

Status: PROPOSED / EXECUTABLE FOUNDATION

Purpose: carry an authored deceptive statement through the same selective audience, channel latency, backlog and local-delivery boundaries already used by ordinary NPC communication without inserting the false assertion into the speaker's private knowledge ledger.

The speaker must own the evidence basis named by `basis_claim_id`. A deceptive statement may alter the asserted content, the declared source, or both. Dispatch resolves explicit recipients through the existing audience resolver. Shared faction membership alone remains worth zero and never creates broadcast knowledge.

`DeceptionInformationEventQueue` reuses `InformationEventQueue` ordering, channel availability, semantic latency, bounded processing, local-projection ACK and delivered-event idempotence. For deceptive envelopes only, final delivery calls `materialize_deceptive_report` instead of `transmit_claim`. The receiver therefore gets the authored assertion with `provenance_root=deception:<statement_id>`, while the speaker's evidence basis remains unchanged.

Receiver confidence uses the ordinary report transport rule: trust may lower or partially recover report confidence, but a report can never exceed the confidence of the evidence basis used by the speaker. This keeps transport semantics consistent without declaring the false content objectively credible.

Declared source attribution remains subjective state in `SourceAttributionStore`. The historical claim records the actual immediate speaker. A false source declaration therefore cannot overwrite causal provenance.

Deception dispatch has no automatic lie detector. Detection, suspicion, trust consequences and the decision to lie are separate future policies. The delivery layer only records what was authored, who was selected, which channel carried it, when it arrived and what attribution was presented.

The specialized queue has its own versioned snapshot containing the ordinary queue snapshot, deceptive statements, event-to-statement mapping and source-attribution store. Pending deceptive messages therefore survive a runtime restart. Pass 292's global atomic checkpoint still expects the ordinary queue schema; integration of this specialized snapshot into that world checkpoint remains unresolved and must not be implied complete.

Canon boundary: this contract is simulation infrastructure. It adds no PTU, Caelo or Kairos rule, no region lore, no faction, no named NPC and no mandatory story event.
