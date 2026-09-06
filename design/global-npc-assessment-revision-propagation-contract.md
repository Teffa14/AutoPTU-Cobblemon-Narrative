# Global NPC assessment revision propagation contract

Status: DESIGN CONTRACT / NOT CANON
Date: 2026-09-06
Pass: 309

## Purpose

Connect durable custody-assessment lineage to the existing non-omniscient information network. A superseding assessment remains local to its investigator until it is converted into an explicit conclusion claim and delivered to explicit recipients.

## Invariants

1. Historical assessments remain immutable.
2. Each materialized assessment conclusion has its own provenance root keyed to the assessment identity.
3. Only the investigator recorded on the assessment may author the default conclusion claim for that assessment.
4. A superseding assessment never retroactively edits the claim generated from its predecessor.
5. The correction audience is explicit. Receipt of the old assessment does not automatically subscribe an NPC to later revisions.
6. Delivery uses the ordinary `InformationEventQueue`; latency, unavailable channels, backlog and local ACK rules remain authoritative.
7. No receiver gains the conclusion until delivery actually completes.
8. A failed or deferred correction can leave two rational NPCs with different current conclusions.
9. Receiving a correction does not automatically undo prior social, institutional or planning consequences.
10. This layer does not determine whether a custody assessment is technically correct; it only communicates the recorded conclusion.

## Runtime

`tools/global_npc_assessment_revision_propagation.py`

`record_assessment_conclusion()` materializes the investigator's conclusion as an `INFERENCE` claim whose subject is the evidence identity and whose value is the assessment status.

`register_assessment_notice()` binds that claim to the assessment after validating investigator, provenance root and semantic time.

`schedule_assessment_notice()` schedules explicit per-recipient envelopes through the existing information network. The function deliberately does not infer recipients from previous notice history.

## Boundaries

This contract does not implement belief-aware dialogue, relationship repair, public retraction, institutional adjudication, technical sample validity, physical item persistence or tactical mechanics. Those remain separate seams.
