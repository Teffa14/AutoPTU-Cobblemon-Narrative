# Global NPC infrastructure attribution checkpoint integration — Pass 304

Status: PROPOSED EXECUTABLE INFRASTRUCTURE
Date: 2026-09-06

Pass 303 made infrastructure-failure findings independently snapshot-capable. Pass 304 closes the world-recovery boundary so those findings cannot drift away from the private evidence ledgers that justified them.

`RESTORED_FINDING_REQUIRES_RESTORED_EVIDENCE`

`CHECKPOINT_DIGEST != CAUSAL_VALIDATION`

`OUROS_NPC_WORLD_CHECKPOINT_V3` now embeds one versioned `InfrastructureAttributionRegistry` snapshot beside managed agents, private knowledge ledgers, communication state, replanning state, deception state and the coordinator materialization guard.

Restore validates more than the child schema. Every infrastructure finding must reference a discoverer whose knowledge ledger exists in the same checkpoint. Every `evidence_claim_id` must exist in that discoverer's restored ledger. A finding cannot occur after the checkpoint semantic minute, and a finding cannot predate one of the claims it cites.

This prevents a restart from preserving a conclusion while losing the testimony, record, material trace or observation that made that conclusion possible. It also prevents a separately restored future finding from leaking backward into an earlier world snapshot.

The registry remains a record of one investigator's assessed conclusion. It does not become objective world truth. Different investigators may still hold different findings for the same incident because their ledgers differ. Restoring one finding does not grant its evidence to another agent.

The checkpoint does not recompute old findings during restore. Findings are historical assessment events. New evidence should create a later finding through the normal attribution resolver so the investigation can evolve while the earlier conclusion remains auditable.

Legacy compatibility is explicit. `OUROS_NPC_WORLD_CHECKPOINT_V2` and `V1` remain readable. Because those schemas predate embedded infrastructure attribution, they restore an empty registry. A current V3 checkpoint missing the child snapshot fails closed.

The existing SHA-256 still protects the canonical logical payload against accidental mismatch or corruption. It is not an authenticity signature and does not substitute for a crash-safe storage transaction.

This pass changes no PTU, Caelo or AutoPTU rule. Infrastructure investigation remains world-simulation state. A later encounter inherits only the mechanical families actually authored into that scene.

Acceptance evidence: create an evidence-backed tampering finding, checkpoint and restart, verify the finding and evidence both survive, checkpoint again and verify the conclusion remains stable. A finding with a missing evidence claim or future semantic time must fail closed. A legacy V2 checkpoint must restore without inventing infrastructure conclusions.
