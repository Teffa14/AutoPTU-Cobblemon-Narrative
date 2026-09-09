# Global NPC world resource allocation application checkpoint contract — Pass 368

Status: IMPLEMENTED GLOBAL CONTRACT
Date: 2026-09-08

Pass 368 introduces `OUROS_NPC_WORLD_CHECKPOINT_V13`.

V13 persists Pass 349 allocation application inside the same integrity boundary as semantic time, NPC state, communications, resource history, Pass 347 conflict admission and Pass 348 allocation resolution.

The checkpoint does not create Pass 350 notice obligations, send messages, alter private knowledge or replay application side effects during restore.

Restore requirements:

- V13 resource state must use `OUROS_NPC_RESOURCE_CHECKPOINT_V8`.
- every application must reference a persisted allocation resolution;
- application resource, kind and affected reservations must remain consistent with that resolution;
- application time cannot precede its decision or exceed restored semantic time;
- one resolution cannot acquire multiple persisted applications;
- the reconstructed V12 owners must match the V13 resource owners exactly;
- V12 migration produces an empty application ledger rather than inferring application from current reservation state or downstream evidence.

Ownership remains explicit. Pass 348 owns the decision. Pass 349 owns its operational application. Pass 350 owns notification obligation. `InformationEventQueue` owns transport and delivery. Memory/belief owns actor knowledge.

`DECIDED != APPLIED != NOTICE_REQUIRED != MESSAGE_DELIVERED != KNOWN`

This contract changes persistence architecture only. It adds no PTU, Caelo, AutoPTU, Minecraft or Cobblemon mechanic.
