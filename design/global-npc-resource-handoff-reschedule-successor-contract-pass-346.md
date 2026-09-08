# Global NPC resource handoff reschedule successor contract — Pass 346

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-07

Purpose

Close the reschedule-acceptance seam left by Pass 345. Preserve the original handoff authorization while allowing an explicitly accepted proposal to create a successor authorization with a new window and/or location.

Target chain

accepted resource request -> original handoff authorization -> RESCHEDULE_REQUEST notice -> actual delivery -> responder decision -> successor authorization -> old authorization operationally superseded -> eventual physical handoff

Core boundaries

`RESCHEDULE_REQUESTED != RESCHEDULE_ACCEPTED`

`RESCHEDULE_ACCEPTED != RESOURCE_TRANSFERRED`

`OLD_AUTHORIZATION_SUPERSEDED != OLD_HISTORY_DELETED`

`SUCCESSOR_AUTHORIZATION_CREATED != ALL_PARTICIPANTS_AWARE`

`NEW_WINDOW != CUSTODY_CHANGE`

`NEW_LOCATION != RESOURCE_TELEPORTED`

`MINECRAFT_UI_ACCEPT != WORLD_AUTHORITY`

Executable primitive

`tools/global_npc_resource_handoff_rescheduling.py` adds an append-only proposal/decision/replacement ledger around the existing Pass 343 handoff owner and Pass 345 appointment notices.

A structured proposal must reference a real `RESCHEDULE_REQUEST` notice. Proposal actors must match the notice sender/receiver and the original authorization must still be incomplete and not already superseded.

A responder cannot decide a proposal until the source notice is actually `DELIVERED` by the existing communication runtime. This prevents omniscient acceptance of a message that is still queued or awaiting acknowledgement.

Decision authority

Only the named proposal responder can ACCEPT or REJECT. A requester, bystander, faction peer or Minecraft projection cannot decide on that actor's behalf.

Rejection preserves the original authorization unchanged.

Acceptance alone records a decision. `create_successor_authorization()` then materializes a new `ResourceHandoffAuthorization` carrying forward the original request, provider, accountable actor, receiving actor, resource and mode while applying the accepted location/window.

The new authorization receives a distinct ID and points its `authority_ref` at the accepting decision.

Historical continuity

The old authorization remains in `ResourceHandoffLedger.authorizations`. A `ResourceHandoffAuthorizationReplacement` records the supersession edge.

`operational_authorization_state()` distinguishes CURRENT, SUPERSEDED, COMPLETED and UNKNOWN.

`current_authorization_id()` follows successor edges deterministically and rejects replacement cycles.

Execution guard

`execute_current_authorized_handoff()` wraps the existing physical handoff executor. A transfer still referencing a superseded authorization fails closed with `HANDOFF_AUTHORIZATION_SUPERSEDED`. A transfer referencing the current successor continues through the existing Pass 343 custody validation.

This wrapper does not change ownership, readiness or PTU mechanics. It only prevents stale appointment authority from authorizing a physical transfer after an accepted replacement exists.

Knowledge boundary

Creating a successor authorization establishes operational world state. It does not prove the proposer, accountable actor, courier or other participants know that it exists. Communication of the accepted change remains the responsibility of the existing information runtime and future appointment-aware replanning coordination.

Reduced version

No AutoPTU dependency. Semantic time, existing handoff authorization, Pass 345 notice delivery, Pass 346 proposal/decision/replacement state and ordinary world-agent replanning are sufficient.

Rich version capability dependencies

Targeting / footprints / range / LoS: only required when a tactical encounter needs exact geometry around a courier, handoff point or interception.

Base movement legality: required for ordinary tactical travel inside an encounter.

Complete movement: required for carrying constraints, interception, push/pull, knockback, forced movement or rescue.

Core calculations: required for deterministic PTU arithmetic.

Action economy / initiative: required if pickup, handoff, guard, communication or objective interaction becomes a tactical action.

Full turn / round lifecycle: required for round-bound pickup windows, delayed objective updates or timed transfer conditions.

Full stateful damage pipeline: required if participants or carried equipment receive authoritative damage.

Status lifecycle: required for persistent conditions affecting participants.

Terrain / weather / hazards / zones / reactions: required when environmental state changes access to the successor rendezvous or affects tactical delivery.

Move-specific behavior: each exact Move remains individually gated.

Abilities: each exact Ability remains individually gated.

Items: each exact PTU Item effect remains individually gated.

Trainer Features/perks: each exact Feature remains individually gated.

AI legal-action infrastructure: required for new tactical handoff/protection actions.

AI tactical policy: required to choose delivery, protection, retreat, interception avoidance or other objective-aware behavior.

Minecraft/Cobblemon/Craftics adapter/playback: presentation only; it cannot create proposal delivery, acceptance, supersession or custody.

Live engine evidence

AutoPTU-Java head inspected: `30ff159abafbef6d14ef4a776789e9077dd26bc4`, merge of PR #398, preserving numeric Burrow speed in movement profiles. This strengthens one movement-profile representation contract but does not verify carrying, interception, forced movement or the complete movement family.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains explicitly presentation-only and does not change battle rules or outcomes.

Capability assessment

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

1. A proposal must reference a real Pass 345 RESCHEDULE_REQUEST notice.
2. Proposal actors must match that notice.
3. A queued reschedule request cannot be decided by its intended responder.
4. Only the named responder can ACCEPT or REJECT.
5. Rejection leaves the original authorization current.
6. Acceptance can create one successor authorization only.
7. The old authorization remains historical and becomes SUPERSEDED.
8. A stale physical transfer using the old authorization fails closed.
9. The successor executes only under its new window/location through Pass 343 validation.
10. No reschedule decision transfers custody, creates PTU effects or grants Minecraft authority.

Deferred work

- communicate accepted/rejected decisions back through the durable communication runtime;
- appointment-aware replanning when successor authority becomes known to each actor;
- explicit institutional authority for changing provider/resource/mode rather than only time/place;
- conflict checks against resource reservations when the new window is proposed;
- cancellation policy interaction when an old appointment was already cancelled;
- arrival/departure evidence from travel runtime;
- chained reschedules in production UI;
- persistence of request/handoff/attempt/appointment/reschedule ledgers in the atomic world checkpoint;
- player-facing acknowledgement and Minecraft projection;
- PTU/Caelo validation if any future reschedule mechanic acquires tactical effects.
