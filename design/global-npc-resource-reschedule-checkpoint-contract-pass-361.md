# Global NPC resource reschedule checkpoint contract — Pass 361

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-08

Pass 361 introduces `OUROS_NPC_RESOURCE_CHECKPOINT_V5` as the standalone durability boundary for Pass 346 handoff rescheduling.

The snapshot preserves the V4 resource history plus reschedule proposals, responder decisions and authorization-replacement records. A successor authorization remains a normal Pass 343 authorization in the handoff ledger; the replacement record explains why it supersedes an older authorization.

Restore requirements

Every proposal must reference an existing authorization and a Pass 345 `RESCHEDULE_REQUEST` notice for the same authorization. Proposer/responder identities must match the notice. Proposal creation cannot precede the source notice and cannot occur after a completed transfer under the original authorization.

Every decision must reference one proposal, be made by that proposal's responder and occur no earlier than proposal creation. A proposal may have at most one restored decision.

Every replacement must reference an ACCEPT decision for the same proposal. Its superseded authorization must be the proposal's original authorization. Its successor authorization must already exist in the restored handoff ledger and preserve request, provider, accountable actor, receiver, resource and mode while taking location/window from the accepted proposal and authority provenance from the decision.

A completed authorization cannot later be superseded. Replacement IDs, successor IDs and superseded IDs are unique within one V5 history. Replacement chains are checked through the existing cycle-detecting `current_authorization_id` resolver.

Temporal boundary

Proposal creation, decisions and replacement materialization are completed historical acts. `validate_reschedule_checkpoint_time()` rejects any such row later than the restored semantic minute. Proposed future handoff windows remain legal because they describe prospective authorization, not events already claimed to have happened.

Backward compatibility

V1–V4 restores produce an explicit empty `ResourceHandoffRescheduleLedger`. Missing historical reschedule data is never inferred from the currently active authorization, current resource holder, NPC memory, location, dialogue or appointment notices.

Ownership boundary

This standalone checkpoint does not re-prove delivery of the source `RESCHEDULE_REQUEST`, because delivery remains owned by `InformationEventQueue`. Pass 346 required delivered communication at decision time. A later world-level integration should cross-validate the restored source notice against communication provenance and terminal delivery state before treating a persisted decision as causally coherent with the same world checkpoint.

No restore path replays `record_reschedule_decision()` or `create_successor_authorization()`. Restore reconstructs persisted history and validates its consistency.
