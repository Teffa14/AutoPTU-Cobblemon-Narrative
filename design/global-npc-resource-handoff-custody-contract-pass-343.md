# Global NPC resource handoff and custody contract — Pass 343

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-07

Purpose

Close the physical-transfer seam left open by Pass 342 without duplicating travel, reservations, technical readiness, specialized evidence custody or AutoPTU item logic.

Target chain:

accepted resource request -> explicit handoff authorization -> actor travel/coordination elsewhere -> verified handoff facts -> append-only custody transfer -> later work/resource gate

Core boundaries

`REQUEST_ACCEPTED != HANDOFF_AUTHORIZED`

`HANDOFF_AUTHORIZED != RESOURCE_TRANSFERRED`

`ACCOUNTABLE_ACTOR != PHYSICAL_RECIPIENT`

`PROXY_AUTHORIZED != REQUESTER_POSSESSES_RESOURCE`

`RESOURCE_AT_LOCATION != CUSTODY_TRANSFERRED`

`CUSTODY_TRANSFERRED != OWNERSHIP_TRANSFERRED`

`CUSTODY_TRANSFERRED != RESOURCE_READY`

`CUSTODY_TRANSFERRED != PTU_ITEM_EFFECT_LEGAL`

Executable primitive

`tools/global_npc_resource_handoffs.py` adds a region-neutral handoff ledger.

`ResourceHandoffAuthorization` records one accepted request, provider, accountable requester, exact physical receiver, fulfilled resource unit, pickup/delivery mode, place, validity window and optional authority provenance.

`ResourceCustodyTransfer` records the actual completed exchange: transfer ID, authorization, request, resource, from/to actors, accountable actor, location, semantic time and optional condition provenance.

The authorization and the completed transfer are separate append-only facts.

Accepted-request bridge

`authorization_from_accepted_request()` can derive an authorization only from a Pass 342 request whose effective state is `ACCEPTED` at the authorization start time.

If Pass 342 recorded an explicit alternate offered unit, that unit becomes the fulfillment resource for the handoff. The original request remains unchanged in the request ledger.

Proxy boundary

The accountable actor remains the original requester.

The receiving actor may be a different explicitly named proxy.

A successful proxy pickup makes the proxy the current physical holder. It does not teleport the resource into the requester's inventory. If the proxy later gives it to the requester, that requires another explicit custody event or a future higher-level coordinator.

Location and holder checks

A handoff executes only when the provider is still the current holder and the resource's world location equals the authored handoff location.

These checks prevent old consent from moving an object after its physical state has changed.

Single-use authorization

V1 authorizations are single-use. Once a custody transfer consumes an authorization, later attempts fail closed.

This is appropriate for indivisible-unit handoffs. Partial quantity/capacity fulfillment remains deferred.

Pickup and delivery

V1 records the coordination mode but does not execute travel.

For `PICKUP`, the receiving actor must reach the handoff location through the existing travel system.

For `DELIVERY`, the provider/courier side must reach the handoff location through a future coordinator using the same travel authority.

Neither mode teleports an actor or resource.

Condition provenance

A transfer can reference a condition observation made at handoff.

That reference does not replace Pass 340 technical readiness or any specialized inspection/maintenance owner.

WorldResource mutation boundary

Successful execution returns a new immutable `WorldResource` value whose `holder_actor_id` is the receiving actor and whose location remains the handoff location.

The input resource object is unchanged.

Ownership is not represented or changed by this module.

Narrative use

This supports ordinary consequences:

- the requester received acceptance but never arranged pickup;
- a named assistant is authorized to collect an instrument;
- the provider arrives but no authorized recipient is present;
- the object was moved after acceptance, so the old handoff cannot execute;
- a proxy receives the object and later becomes delayed before reaching the requester;
- a condition note at handoff later becomes relevant without retroactively proving readiness.

Reduced version

The reduced narrative version requires no battle system. It uses request state, semantic time, holder/location state, explicit authorization, travel/communication coordination and custody history.

Rich version and capability dependencies

A field-delivery encounter can add tactical pressure only when the exact capabilities are verified.

Targeting / footprints / range / LoS: required for exact tactical visibility or target selection around the carrier/resource.

Base movement legality: required for ordinary tactical movement toward pickup, delivery and exit positions.

Complete movement: required for carrying constraints, dragging, interception, rescue, push/pull, knockback or forced displacement of carrier/resource.

Core calculations: required for deterministic PTU arithmetic used by structured actions.

Action economy / initiative: required for explicit tactical handoff, equip, drop, guard, activate or abandon actions.

Full turn / round lifecycle: required for delivery deadlines, delayed handoffs, phase changes or round-bound objectives.

Full stateful damage pipeline: required if actors or equipment can take authoritative damage.

Status lifecycle: required for persistent conditions affecting carrier or recipient.

Terrain / weather / hazards / zones / reactions: required if route/site conditions change or interrupt transfer.

Move-specific behavior: every exact Move individually gated.

Abilities: every exact Ability individually gated.

Items: every exact PTU Item effect individually gated.

Trainer Features/perks: every exact Feature individually gated.

AI legal-action infrastructure: required when pickup/drop/handoff/use actions must be generated as legal tactical choices.

AI tactical policy: required when agents must decide whether to protect, deliver, abandon, share, retreat or prioritize the objective over defeating opponents.

Minecraft/Cobblemon/Craftics adapter/playback: presentation and acknowledgement only. An animation cannot create authoritative custody.

Current live evidence

AutoPTU-Java head inspected during this pass: `b85fe17319d16e54402a5a45fb6acccd6b388553`, merge of PR #397, `Freeze Python Arena Trap target eligibility`.

That evidence strengthens one Arena Trap target-eligibility seam. It does not prove stateful Arena Trap application, the full Ability family, complete movement, status lifecycle or any handoff action.

AutoPTU Python head inspected during this pass: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit is explicitly presentation-only.

Capability assessment remains conservative:

- targeting / footprints / range / LoS: VERIFIED for previously audited ordinary contracts;
- base movement legality: VERIFIED for previously audited ordinary contracts;
- core calculations: VERIFIED for previously audited deterministic arithmetic;
- action economy / initiative: VERIFIED for current audited primitives;
- AI legal-action infrastructure: VERIFIED for its current ordinary scope;
- complete movement: PARTIAL;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING;
- move-specific behavior: PARTIAL and individually gated;
- abilities: PARTIAL and individually gated;
- items: PARTIAL and individually gated;
- Trainer Features/perks: PARTIAL and individually gated;
- AI tactical policy: BLOCKING for delivery/protection/retreat objective policy;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

Acceptance cases

1. Pending or rejected requests cannot authorize handoff.
2. Accepted requests can authorize future pickup/delivery without moving the resource.
3. Alternate accepted units preserve original request identity.
4. Duplicate authorization IDs fail closed.
5. Provider must remain current holder.
6. Resource must be at the handoff location.
7. Transfer actor/resource/request facts must match the authorization.
8. Early and expired-window transfers fail closed.
9. Successful transfer changes current physical holder and records append-only history.
10. Proxy pickup preserves requester accountability while assigning physical custody to the proxy.
11. Authorization is single-use.
12. Stable IDs determine deterministic active-authorization and custody-history ordering.
13. No handoff creates `REQUEST_AUTOPTU`.
14. No handoff authorizes a PTU Item effect.

Deferred work

- communication coordinator for request/response/handoff arrangements;
- pickup versus delivery responsibility assignment;
- travel-aware courier orchestration;
- successive proxy/courier transfer coordinator;
- delegated institutional authority;
- reservation/check-out integration;
- partial and quantity fulfillment;
- refusal/no-show at the actual handoff;
- return and overdue custody obligations;
- checkpoint persistence;
- expiry-triggered replanning;
- player inventory binding;
- Minecraft acknowledgement/UI;
- PTU/Caelo validation for any mechanically active Item.
