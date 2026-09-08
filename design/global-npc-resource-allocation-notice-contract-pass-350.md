# Global NPC resource allocation notice contract — Pass 350

Status: IMPLEMENTED GLOBAL CONTRACT
Date: 2026-09-08

## Purpose

Preserve the downstream obligation to inform each reservation holder displaced by Pass 349, while leaving message creation, transport, receipt, belief and replanning with their existing owners.

## Existing owners retained

Pass 339 owns source reservations. Pass 348 owns the authorized allocation decision. Pass 349 owns operational displacement. The information network owns message delivery state. Memory/belief owns actor knowledge. Replanning owns later plan changes.

Pass 350 owns only an append-only obligation ledger and links from those obligations to real communication events.

## Executable records

`ResourceAllocationNoticeObligation` contains a stable ID, source allocation application, resource, displaced reservation, affected actor, creation tick and optional basis references.

`ResourceAllocationNoticeLink` connects one obligation to one existing communication event and records who authored the linked communication. The link does not itself claim delivery.

## Hard boundaries

`ALLOCATION_APPLIED != HOLDER_INFORMED`

`NOTICE_REQUIRED != MESSAGE_AUTHORED`

`MESSAGE_AUTHORED != MESSAGE_DELIVERED`

`MESSAGE_DELIVERED != BELIEF_REVISED`

`ONE_HOLDER_NOTIFIED != ALL_HOLDERS_NOTIFIED`

`INSTITUTIONAL_DISPLACEMENT != HOLDER_MISCONDUCT`

`WORLD_RESOURCE != PTU_ITEM`

## Derivation

Only `DISPLACE_CONFLICTING_RESERVATIONS` applications create V1 notice obligations. One obligation is created for each exact displaced reservation so provenance is not lost when multiple actors competed for the same unit.

Derivation fails closed when a displaced reservation is absent from the source ledger, points to another resource, duplicates an existing application/reservation obligation, or the obligation timestamp precedes the allocation application.

## Communication integration

Pass 350 never constructs a private delivery system. `link_notice_communication()` accepts only an event already present in `InformationEventQueue`.

Derived state is `REQUIRED`, `QUEUED`, `WAITING_LOCAL_ACK`, `DELIVERED`, or `DELIVERY_FAILED`. Only the existing runtime's `DELIVERED` state closes the delivery obligation. This contract does not infer that delivery necessarily caused understanding, agreement or replanning.

## Reduced narrative version

A team plans around a valid booking. An authorized later allocation displaces it. The affected holder has not yet received the notice and travels using old information. The player can reconstruct the old reservation, allocation decision, application, notice obligation and communication timeline without combat.

## Mechanically rich version

If the story continues into a field transport encounter after a resource is collected, capability dependencies remain explicit:

- targeting/footprints/range/LoS: VERIFIED within audited ordinary contracts;
- base movement legality: VERIFIED within audited ordinary contracts;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED within audited deterministic arithmetic;
- action economy/initiative: VERIFIED for audited primitives; tactical pickup/drop/handoff remains individually gated;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL; Arena Trap has narrower target/effect-plan evidence but not full family coverage;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within ordinary audited action-generation scope;
- AI tactical policy: BLOCKING for escort, protect-carrier, preserve-resource, delivery-first and disengage-after-objective goals;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

No representative mechanic promotes an entire capability family.
