# Global NPC resource request and provider-consent contract — Pass 342

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-07

## Purpose

Close the next world-agent seam after Pass 341.

Pass 341 can derive `REQUEST_RESOURCE` when a blocked actor knows another actor holds a needed resource. Pass 342 gives that request a persistent identity and provider-controlled response lifecycle without silently moving, reserving, checking out or authorizing the resource.

Target chain:

`blocked work -> Pass 341 recovery option -> request authored -> existing communication delivery -> provider response -> accepted/rejected/expired/withdrawn request state -> later reservation/transfer owner`

## Core invariants

`REQUEST_OPTION != REQUEST_SUBMITTED`

`REQUEST_SUBMITTED != REQUEST_DELIVERED`

`REQUEST_DELIVERED != REQUEST_ACCEPTED`

`REQUEST_ACCEPTED != RESOURCE_RESERVED`

`REQUEST_ACCEPTED != RESOURCE_TRANSFERRED`

`REQUEST_ACCEPTED != RESOURCE_CHECKED_OUT`

`REQUEST_REJECTED != REQUEST_WAS_INVALID`

`REQUEST_EXPIRED != REQUEST_DELETED`

`ACCEPTANCE_WITHDRAWN != ACCEPTANCE_NEVER_HAPPENED`

`ALTERNATE_OFFERED != ORIGINAL_REQUEST_REWRITTEN`

`TEMPORARY_USE != OWNERSHIP_TRANSFER`

`WORLD_RESOURCE_CONSENT != PTU_ITEM_EFFECT_LEGAL`

## Executable primitive

`tools/global_npc_resource_requests.py` introduces a region-neutral request ledger.

```yaml
ResourceRequest:
  request_id: request:stable-id
  requester_actor_id: npc:stable-id
  provider_actor_id: npc:stable-id
  resource_id: resource:stable-id
  created_tick: semantic-time
  quantity: positive-int
  expires_at_tick: semantic-time | null
  purpose_ref: world-state-ref | null
```

The request is immutable historical intent. It is not rewritten if the provider later offers a different resource.

Response history uses:

```yaml
ResourceRequestEvent:
  event_id: request-event:stable-id
  request_id: request:stable-id
  actor_id: npc:stable-id
  kind: ACCEPTED | REJECTED | CANCELLED | WITHDRAWN
  at_tick: semantic-time
  offered_resource_id: resource:stable-id | null
  reason_ref: world-state-ref | null
```

`ResourceRequestLedger` stores original requests and append-only transition events separately.

## State projection

`request_view()` derives the effective state at a semantic tick.

Possible projected states:

- `PENDING`
- `ACCEPTED`
- `REJECTED`
- `CANCELLED`
- `WITHDRAWN`
- `EXPIRED`

Expiry is derived from the original request window when no earlier terminal response applies. Expiry does not create a fake historical event or delete the request.

An acceptance recorded before the request deadline remains historically accepted after the original deadline. Later fulfillment validity belongs to a future transfer/reservation owner; Pass 342 does not invent a second hidden expiry clock.

## Provider agency

Only the explicit provider actor may accept or reject a request in V1.

A physical holder therefore has provider authority only when the request names that actor as provider. Future institutional pools can replace this narrow assumption with delegated authority without changing the request-state boundary.

Provider acceptance may contain `offered_resource_id` when the provider can supply a different unit than the original request named.

The original `resource_id` remains unchanged.

## Requester agency

Only the explicit requester may cancel a pending request.

Cancellation stops future provider acceptance in this ledger. It does not retract a message that has already been heard, delete memories, alter publication history or teleport any resource.

## Provider withdrawal

A provider may withdraw only an already accepted request.

This models cases where new obligations, readiness faults, ownership constraints or other world facts make the prior offer unavailable before fulfillment.

Withdrawal is a later event. The acceptance remains in request history.

## Pass 341 integration

`request_from_recovery_option()` can materialize only a Pass 341 option whose intent kind is `REQUEST_RESOURCE` and whose request target actor is explicit.

It copies:

- provider actor from the recovery option;
- requested resource identity;
- requested quantity from the resource requirement;
- blocked-work/request intent provenance into `purpose_ref` unless the caller supplies a narrower reference.

This bridge does not send the request.

## Communication boundary

Pass 342 deliberately does not claim that `submit_resource_request()` means the provider heard anything.

The existing communication stack must carry the request when communication is required:

`audience/explicit recipient -> channel scheduling -> delivery -> receiver knowledge -> provider decision -> response delivery`

A request can therefore be historically authored while still undelivered.

Likewise, a provider response event should eventually be coordinated with actual response communication. The executable V1 stores semantic provider decisions but does not yet own their message transport.

## Reservation boundary

An accepted request does not create a Pass 339 `ResourceReservation`.

A future coordinator may attempt:

`accepted request -> authority check -> reservation attempt`

That attempt can still fail because another reservation exists, because the resource became unavailable or because the offered unit differs from the original.

## Transfer boundary

Pass 342 does not implement handoff, courier movement, physical delivery, pickup, proxy pickup, custody transfer or checkout.

A later transfer owner must record who possessed the resource before and after the handoff and where/when it occurred.

## Readiness boundary

Provider consent cannot override Pass 340 technical readiness.

A provider can sincerely accept a request and later withdraw after a maintenance or inspection record changes the resource's operational readiness.

## Knowledge and belief boundary

NPC dialogue may correctly report:

- “I asked for it” from authored/sent request evidence;
- “they accepted” only when the actor received or otherwise possesses evidence of acceptance;
- “I have it” only from actual holder/custody state.

These claims are not interchangeable.

Pass 335/336/337 dialogue, grounding and audience systems remain responsible for what each NPC actually knows and how shared meaning is established.

## Reduced narrative version

The reduced version can run with no AutoPTU involvement.

A blocked NPC can create a request, receive an acceptance/rejection later, reorganize work, cancel if the window closes, or discover that an accepted offer was withdrawn.

This is sufficient for ordinary logistics, misunderstanding, schedule pressure and institutional relationships.

## Rich narrative version

A richer scenario can continue from accepted request into pickup, transport, field deployment and eventually structured conflict.

Any such encounter must declare the exact capability families it uses.

## AutoPTU capability classification

Pass 342 request-state execution itself requires no battle capability.

If the resource request leads into structured play:

- targeting / footprints / range / LoS: required when exact tactical visibility or target selection matters;
- base movement legality: required for ordinary tactical movement to pickup/delivery/work positions;
- complete movement: required for carrying, dragging, interception, rescue, push/pull, knockback or forced displacement;
- core calculations: required for exact PTU arithmetic invoked by structured actions;
- action economy / initiative: required for tactical handoff, equip, activate, guard, drop or abandon actions;
- full turn / round lifecycle: required for delayed delivery, phase windows, timed activation or round-bound objectives;
- full stateful damage pipeline: required for mechanically represented damage to actors or equipment;
- status lifecycle: required for persistent conditions caused or removed by exact content;
- terrain / weather / hazards / zones / reactions: required for changing work-site or route state during combat;
- move-specific behavior: every exact Move individually gated;
- abilities: every exact Ability individually gated;
- items: every exact PTU Item effect individually gated;
- Trainer Features/perks: every exact Feature individually gated;
- AI legal-action infrastructure: required when tactical pickup/use/transfer actions must be generated legally;
- AI tactical policy: required when agents must decide whether to protect, deliver, abandon, share or retreat with resources;
- Minecraft/Cobblemon/Craftics adapter/playback: presentation and acknowledgement only.

Provider acceptance never proves an Item effect or tactical action is implemented.

## Acceptance cases

1. A new stable request enters the ledger as `PENDING`.
2. Duplicate request IDs fail closed.
3. A non-provider cannot accept or reject.
4. Provider acceptance preserves the original request and does not transfer anything.
5. Provider rejection closes further acceptance attempts.
6. A requester can cancel only while pending.
7. An unanswered request becomes `EXPIRED` at its semantic deadline without deleting history.
8. An expired request cannot be accepted late.
9. A provider may withdraw only after acceptance.
10. An alternate offered resource does not overwrite the originally requested resource.
11. Pass 341 recovery options can be materialized into requests only when their semantic kind is `REQUEST_RESOURCE`.
12. Accepted-request enumeration is deterministic by stable request ID.
13. No local region or place appears in the executable module.
14. No request transition creates `REQUEST_AUTOPTU`.

## Deferred work

- communication coordinator for request delivery and response delivery;
- institutional provider pools and delegated authority;
- accepted-request to reservation transition;
- explicit transfer/handoff/courier events;
- pickup versus delivery responsibility;
- proxy pickup authority;
- quantity/capacity fulfillment;
- partial fulfillment;
- waitlists and fairness;
- request priority/escalation policy;
- checkpoint persistence;
- expiry wake-ups and replanning;
- player-facing request/accept UI;
- Minecraft acknowledgement;
- exact PTU/Caelo validation when a requested resource has mechanical Item behavior.
