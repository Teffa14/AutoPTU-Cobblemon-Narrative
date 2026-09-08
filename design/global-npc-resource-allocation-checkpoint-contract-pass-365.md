# Global NPC resource allocation checkpoint contract — Pass 365

Status: IMPLEMENTED GLOBAL CONTRACT

Pass 365 adds `OUROS_NPC_RESOURCE_CHECKPOINT_V7` above the Pass 363 V6 admission checkpoint.

The checkpoint persists the Pass 348 allocation resolution together with the exact authority evidence needed to validate it after restart. It preserves decision provenance and does not perform Pass 349 application.

A restored resolution must have a matching historical Pass 347 conflict admission for the same proposal, resource and exact conflicting reservation set at or before the decision tick. Its authority evidence must exist, name the same decision actor, carry action scope `ALLOCATE_RESOURCE_WINDOW`, target the same resource, be `AUTHORIZED`, and be current at the decision tick.

`SELECT_EXISTING_RESERVATION` must select an ID present in the persisted conflict set. Other resolution kinds cannot silently carry a selected reservation.

Duplicate authority-check IDs and resolution IDs fail closed. Authority checks and decisions from after the recovered semantic time fail time validation.

V1–V6 remain readable. Their restore result contains empty allocation-authority evidence and an empty `ResourceAllocationResolutionLedger`. Older saves never infer a decision from current availability, a later displacement, handoff state, memory or dialogue.

Ownership remains separated. Pass 347 owns conflict admission. Pass 348 owns the institutional choice. Pass 349 owns application/displacement. Reservations retain their own lifecycle. Handoff owners retain authorization and custody. Communications and private knowledge retain their own delivery and belief semantics.

PTU/Caelo mechanics are unchanged. This contract persists world provenance only.
