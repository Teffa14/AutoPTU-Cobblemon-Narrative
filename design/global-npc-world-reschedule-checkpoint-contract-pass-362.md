# Global NPC world reschedule checkpoint contract — Pass 362

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-08

Pass 362 introduces `OUROS_NPC_WORLD_CHECKPOINT_V10` as the coherent world recovery boundary for Pass 346 reschedule lineage.

The checkpoint embeds the most advanced resource history supplied by the caller. When a `ResourceHandoffRescheduleLedger` is present, V10 stores `OUROS_NPC_RESOURCE_CHECKPOINT_V5`, including reservations, requests, handoff authorizations/transfers, failed attempts, appointment notices, reschedule proposals, decisions and authorization replacements.

Ownership boundary

Resource history owns the fact that a proposal, decision or replacement exists. `InformationEventQueue` owns whether the source appointment communication was queued, delivered, failed or awaiting acknowledgement.

V10 does not duplicate transport state into the resource ledger. Restore cross-checks both owners after they have been reconstructed from the same world snapshot.

Decision prerequisite

For every restored reschedule decision:

- its proposal must reference an existing `RESCHEDULE_REQUEST` appointment notice;
- Pass 361 validation must already confirm proposal, actors, decision and successor lineage;
- Pass 360 validation must confirm that the appointment notice and communication envelope agree on sender, receiver, source claim, event identity and creation time;
- the restored communication event must have `DeliveryStatus.DELIVERED`.

A queued, failed or unacknowledged source request cannot support a restored responder decision. A successor authorization is never accepted as substitute evidence for delivery.

Backward compatibility

V9 restores its appointment history and returns an empty reschedule ledger. V8 restores failed attempts with empty appointment/reschedule history. V7 restores handoff history only. V6 restores reservations and requests only. Older world-only checkpoints restore every resource ledger empty.

V10 may also carry a V4 or V3 resource bundle when the caller intentionally omitted newer owners. The absence remains explicit; restore does not infer missing history from later custody, memory, dialogue or authorization state.

Build-time constraint

A non-empty or empty reschedule owner can be supplied only together with appointment history because every proposal lineage depends on a source appointment notice. `build_world_resource_checkpoint` rejects `reschedule_ledger` without `appointment_ledger`.

Replay boundary

Restore reconstructs historical facts. It does not resend the reschedule request, re-record the decision, create the successor again, move an NPC, move a resource or wake the planner as a side effect of recovery.

Failure policy

Digest mismatch, invalid nested schemas, future-dated resource events, invalid successor lineage, missing communication provenance or a decision whose source request was not delivered all fail closed. Recovery does not repair one subsystem by rewriting another.

Canon boundary

This contract changes persistence architecture only. It adds no Ouros geography, faction, NPC, PTU rule, Caelo fact, Move, Ability, Item or Trainer Feature.
