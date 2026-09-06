# Global NPC custody assessment lineage contract

Status: DESIGN CONTRACT / NOT CANON
Date: 2026-09-06
Pass: 308

Purpose: preserve how an investigator's supported custody conclusion changes over time without rewriting earlier epistemic state.

`CustodyAssessment.supersedes_assessment_id` is an optional directed link from a newer assessment to the earlier assessment it revises. The link is historical lineage, not a truth flag.

A valid predecessor must exist, belong to the same investigator, concern the same physical evidence identity and occur no later than the successor. Self-links, missing predecessors, cross-investigator lineage, cross-evidence lineage and cycles fail closed. The registry retains both assessments. `assessment_lineage()` returns the ordered historical chain ending at a selected assessment.

Live creation requires the predecessor to be present before the successor is added. Snapshot restoration parses the whole assessment set before validating lineage so deterministic serialization order does not become a gameplay rule. The V2 custody snapshot persists the predecessor pointer; V1 restores without inventing links.

A successor may reach the same status as its predecessor. Lineage can therefore represent confirmation after new evidence as well as a changed conclusion. Ouros must not infer that every new assessment supersedes the latest one; authored investigation logic must supply the predecessor relation explicitly.

A superseding assessment does not mutate the predecessor's status, cited records, support claims or semantic time. It also does not retract publications, update other NPC ledgers, restore trust, assign guilt, establish evidence admissibility or prove the artifact's substantive interpretation. Those effects belong to their existing subsystems and require explicit causal events.

The intended near-term use is delayed documentation. An investigator may first support `DOCUMENTATION_GAP`, later receive a missing handoff record, and create `CONTINUITY_SUPPORTED` pointing back to the earlier assessment. Another NPC who only received the old conclusion can continue to act on it until the later result is actually communicated.

No PTU/Caelo mechanic is defined here. Skills, Edges, Trainer Features, Pokémon senses, item capabilities, examination procedures and mechanical encounter effects remain subject to the repository's mechanical-source priority and current AutoPTU evidence.
