# Global NPC resource allocation notice checkpoint contract — Pass 369

Status: IMPLEMENTED GLOBAL CONTRACT
Date: 2026-09-08

Pass 369 introduces `OUROS_NPC_RESOURCE_CHECKPOINT_V9`.

V9 persists the Pass 350 allocation-notice ledger after Pass 349 application has already been persisted by V8. It preserves both notice obligations and any existing notice-to-communication links. The standalone resource checkpoint does not own or reconstruct the communication queue, so envelope sender/receiver provenance and delivery status remain cross-owner checks for the coherent world checkpoint.

Restore requirements:

- every obligation must reference a persisted Pass 349 application;
- the source application must be `DISPLACE_CONFLICTING_RESERVATIONS`;
- resource identity must agree across application, obligation and displaced reservation;
- the displaced reservation must be part of the exact application displacement set;
- the affected actor must equal the holder on that source reservation;
- obligation creation cannot precede application;
- one application/reservation pair cannot acquire multiple obligations;
- link IDs, linked obligation IDs and communication event IDs cannot be reused inside the persisted notice ledger;
- every link must point to a persisted obligation and cannot precede it;
- obligation/link timestamps cannot exceed restored semantic time when the time validator is used;
- V8-and-earlier migration produces an empty notice ledger instead of inferring obligations from current reservation state, communication history, memory or dialogue.

Ownership remains explicit. Pass 349 owns operational application. Pass 350 owns notice obligations and notice links. Pass 351 validates sender/recipient binding against the transport envelope. Pass 352 preserves terminal envelope provenance. `InformationEventQueue` owns transport and delivery. Memory/belief owns private knowledge.

`APPLIED != NOTICE_REQUIRED != MESSAGE_LINKED != MESSAGE_DELIVERED != KNOWN`

A standalone V9 snapshot can prove that an obligation and a declared link were durably recorded. It cannot prove that the linked communication exists in the same world or that its envelope matches the affected holder. That proof belongs to the next coherent world integration because only that boundary contains both owners.

This contract changes persistence architecture only. It adds no PTU, Caelo, AutoPTU, Minecraft or Cobblemon mechanic.
