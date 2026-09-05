# Global NPC publication revision contract

Status: PROPOSED executable infrastructure. Region-neutral. Not canon-setting content.

Public information can change after release. Ouros must preserve the historical fact that an NPC received an earlier version while also representing a later update, correction, or withdrawal.

Core invariant: a later revision is a new world event. It does not erase an earlier publication, its receipts, or consequences that already occurred.

`PublicationRevisionRegistry` owns a deterministic lineage. Each record is classified as `ORIGINAL`, `UPDATE`, `CORRECTION`, or `RETRACTION`. A non-original revision references an existing predecessor through `supersedes_publication_id`.

The registry rejects missing predecessors, self-reference, earlier timestamps, publisher/service/topic identity changes, and forks. These restrictions preserve a stable root and one deterministic current revision. If editorial branching is needed later, merge semantics must be designed explicitly.

`received_state()` is individual to one NPC. It records which revisions that NPC actually received, the latest received version, and whether that receiver has the current version. This permits one actor to retain an old bulletin while another has a correction and a third remains unaware.

The registry does not delete or rewrite `KnowledgeLedger` claims. Transport remains owned by the publication/information queue layers. Belief assessment remains owned by the memory layer. Revision metadata describes publication history and receipt history; it does not silently force a personal belief change.

A `RETRACTION` records withdrawal of a publication. It does not automatically assert the opposite factual value. Any replacement fact requires its own source claim and normal provenance path.

Snapshot schema `OUROS_NPC_PUBLICATION_REVISION_V1` preserves revision history across restart.

This is Ouros simulation policy. It does not adopt a PTU, Caelo, Kairos, Pokémon, manga, or fan-work rule. `SOURCE_HAS_RULE != OUROS_USES_RULE` remains in force.

The component has no tactical-resolution authority. If changed public information later causes a structured encounter, that encounter must declare its own exact engine capability dependencies.
