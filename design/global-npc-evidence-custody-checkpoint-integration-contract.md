# Global NPC evidence custody checkpoint integration contract

Status: DESIGN CONTRACT / NOT CANON
Date: 2026-09-06
Pass: 307, updated by pass 308

Purpose: keep custody reasoning causally coherent with the private evidence that supports it across world restarts.

`OUROS_NPC_WORLD_CHECKPOINT_V4` persists `EvidenceCustodyRegistry` alongside managed agents, private `KnowledgeLedger` state, information delivery state, replanning state, delivery idempotency guards, infrastructure attribution and optional publication runtime state.

The checkpoint remains a logical atomic unit. Crash-safe storage, database transactions and physical artifact storage remain adapter responsibilities.

Core invariants:

- restart cannot preserve a custody assessment while silently losing the investigator's cited support claims;
- restart cannot move a custody record or assessment backward in semantic time;
- a predecessor record cannot cross from one evidence identity into another;
- an assessment may cite only custody records for the same evidence identity;
- support claims must correspond to documentation attached to a custody record the investigator actually knows;
- compromise evidence must remain present in that investigator's private ledger;
- restoring a legacy V1, V2 or V3 world checkpoint produces an empty custody registry because those schemas never persisted this subsystem;
- an old assessment remains historical evidence of what the investigator could support at that time. Later documentation creates a later assessment rather than retroactively rewriting the earlier result.

Pass 308 adds explicit assessment lineage inside the custody registry. A later `CustodyAssessment` may name `supersedes_assessment_id`. The predecessor must already exist during live mutation, must belong to the same investigator and evidence artifact, and cannot be later in semantic time. Snapshot restoration validates all rows together so serialization order cannot invalidate a legitimate lineage, while unknown predecessors, cross-investigator links, cross-evidence links and cycles fail closed. The earlier assessment remains immutable and addressable.

`OUROS_NPC_EVIDENCE_CUSTODY_V2` stores this optional lineage pointer. Legacy custody V1 snapshots restore with no invented predecessor relationship. The enclosing world checkpoint remains V4 because its subsystem slot and atomic boundary are unchanged; the nested custody registry owns its own schema evolution.

Fail-closed restore behavior applies before live world state is returned. Unknown or malformed custody snapshots, future assessments, missing cited claims, impossible predecessor chronology, evidence-identity crossover and invalid assessment lineage are rejected.

Current scope deliberately stops short of several adjacent systems. The checkpoint does not persist the physical object itself, its Minecraft block/entity representation or a storage inventory. Those belong to the world/inventory persistence layer. It also does not decide whether a sample's scientific interpretation is correct, which PTU Skill can authenticate an item, whether a Pokémon sense is sufficient to discover a trace, or whether a custody defect makes evidence unusable. Those require separate PTU/Caelo validation and authored world rules.

Supersession records a changed supported assessment for one investigator. It does not broadcast the new conclusion, erase the predecessor from memory, establish canonical truth, repair social trust automatically, prove culpability or invalidate every downstream belief that relied on the earlier assessment. Those consequences require explicit information delivery, replanning and social-state events.

This subsystem requires no AutoPTU tactical capability. If recovery or re-examination of evidence becomes a structured encounter, only the mechanics actually authored in that encounter activate the permanent engine dependency families.
