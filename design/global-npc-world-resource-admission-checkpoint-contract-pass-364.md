# Global NPC World Resource Admission Checkpoint Contract — Pass 364

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-08

Pass 364 introduces `OUROS_NPC_WORLD_CHECKPOINT_V11` as a coherent recovery boundary through Pass 347 reschedule-conflict admission history.

## Scope

V11 extends the existing V10 world/resource recovery boundary with `OUROS_NPC_RESOURCE_CHECKPOINT_V6` admission records. The same SHA-256 covers world-agent state, semantic time, knowledge, communications, resource history, reschedule lineage and the historical resource-window assessment.

An admission record remains a historical read-model result. It says what the resource calendar showed when a proposal was assessed. It does not decide who receives the resource, mutate a reservation, create priority, or prove later allocation authority.

## Required lineage

Every persisted admission must remain valid against the owners recovered from the same checkpoint:

- the proposal exists in restored reschedule history;
- the proposal's authorization exists;
- the resource identity agrees with that authorization;
- every conflicting or same-purpose reservation remains available as historical reservation evidence;
- each reservation actually overlapped the proposed bounded window;
- purpose provenance still supports its stored classification;
- the assessment does not occur before the proposal or after the restored semantic minute.

Pass 362 remains responsible for appointment-to-envelope binding and for requiring delivered `RESCHEDULE_REQUEST` provenance before a decision can exist. V11 delegates those checks to the V10 recovery path rather than duplicating communication ownership.

## Migration

A V10 checkpoint restores through the Pass 364 API with an empty `ResourceRescheduleAdmissionLedger` because V10 never persisted that owner. No admission is reconstructed from current availability, NPC memory, dialogue, a later allocation decision or the fact that a successor authorization exists.

## Ownership boundary

Pass 347 owns conflict admission as an observed historical state. Pass 348 owns institutional allocation decisions. Pass 349 owns application of an approved decision. A later mutation must not rewrite the earlier admission record.

## Canon boundary

This checkpoint changes persistence architecture only. It establishes no Ouros settlement, faction, office, professional rule, resource policy or PTU mechanic. Research and proposals remain outside `canon/` until reviewed.