# Global NPC evidence custody checkpoint integration contract

Status: DESIGN CONTRACT / NOT CANON
Date: 2026-09-06
Pass: 307

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
- an old assessment remains historical evidence of what the investigator could support at that time. Later documentation should create a later assessment rather than retroactively rewriting the earlier result.

Fail-closed restore behavior applies before live world state is returned. Unknown or malformed custody snapshots, future assessments, missing cited claims, impossible predecessor chronology and evidence-identity crossover are rejected.

Current scope deliberately stops short of several adjacent systems. The checkpoint does not persist the physical object itself, its Minecraft block/entity representation or a storage inventory. Those belong to the world/inventory persistence layer. It also does not decide whether a sample's scientific interpretation is correct, which PTU Skill can authenticate an item, whether a Pokémon sense is sufficient to discover a trace, or whether a custody defect makes evidence unusable. Those require separate PTU/Caelo validation and authored world rules.

The current registry has no explicit `supersedes_assessment_id` field. Reopened investigations can store multiple assessments, but the relationship between an earlier gap and a later repaired assessment must remain explicit in authored provenance or receive a future lineage extension. Do not overwrite old assessments as a shortcut.

This subsystem requires no AutoPTU tactical capability. If recovery of evidence becomes a structured encounter, only the mechanics actually authored in that encounter activate the permanent engine dependency families.
