# Global NPC resource allocation notice recipient-binding contract — Pass 351

Status: IMPLEMENTED GLOBAL CONTRACT
Date: 2026-09-08

## Purpose

Close the provenance gap between a Pass 350 notice obligation and the communication event linked to it. The linked event must actually be addressed to the displaced reservation holder and must actually come from the sender recorded on the link.

## Existing owners retained

Pass 339 owns reservations. Pass 348 owns allocation resolution. Pass 349 owns operational displacement. Pass 350 owns notice obligations. `InformationEventQueue` owns message transport and delivery. Memory/belief owns private knowledge. Pass 287 owns delivery-triggered replanning.

Pass 351 adds recipient/sender binding validation only. It does not create a new communication or replanning subsystem.

## New executable invariant

`NOTICE_LINK_EVENT_ID` is valid only while the transport envelope is still inspectable and all of the following are true:

- the event already exists in `InformationEventQueue`;
- the envelope sender equals `ResourceAllocationNoticeLink.sender_actor_id`;
- the envelope receiver equals `ResourceAllocationNoticeObligation.affected_actor_id`;
- the link timestamp does not precede either the obligation or the authored message.

An envelope waiting for local Minecraft acknowledgement remains inspectable and can still be bound. A fully delivered event is no longer retroactively bindable in V1 because the base queue does not retain the complete delivered envelope. Pass 351 fails closed rather than infer addressing from delivery status alone.

## Hard boundaries

`EVENT_EXISTS != EVENT_ADDRESSED_TO_HOLDER`

`DELIVERED_TO_SOMEONE != HOLDER_NOTIFIED`

`DECLARED_SENDER != VERIFIED_ENVELOPE_SENDER`

`NOTICE_LINKED != NOTICE_DELIVERED`

`NOTICE_DELIVERED != BELIEF_REVISED`

`BELIEF_REVISED != PLAN_CHANGED`

`WRONG_RECIPIENT_MESSAGE != INVALID_WORLD_EVENT`

A message to the wrong actor may remain a valid communication event and may affect that actor's beliefs. It cannot close another actor's notice obligation.

## Delivery and replanning integration

No new coordinator is introduced. Once a correctly bound event reaches `DELIVERED`, the existing Pass 287 `GlobalNpcWorldEventCoordinator` applies the delivered claim to the managed receiver and schedules the existing selective `KNOWLEDGE_DELIVERED` replan trigger. Tests in Pass 351 verify that only the addressed holder wakes and acquires the delivered claim.

## Reduced narrative version

An allocation office displaces one team's valid booking but accidentally sends the update to another team. The unintended recipient receives a real message and may reasonably react to it. The actual holder keeps acting from their last received schedule. The player can resolve the incident by inspecting reservation identity, notice obligation, message addressing and delivery history.

No AutoPTU battle is required.

## Mechanically rich version

If either team is already in the field when the routing error is discovered, the same premise can continue into travel, interception or protection play. Capability dependencies remain explicit:

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
- abilities: PARTIAL; Arena Trap now has authoritative target projection, effect planning and state mutation evidence, but this does not establish full Ability coverage or status expiration;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED within ordinary audited action-generation scope;
- AI tactical policy: BLOCKING for escort, protect-carrier, preserve-resource, delivery-first and disengage-after-objective goals;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

No representative mechanic promotes an entire capability family.
