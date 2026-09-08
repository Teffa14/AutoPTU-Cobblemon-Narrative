# Global NPC resource handoff appointment coordination contract — Pass 345

Status: DESIGN / EXECUTABLE FOUNDATION / NON-CANON
Date: 2026-09-07

Purpose

Close the pre-rendezvous communication seam left by Pass 344. Bind confirmation, cancellation and reschedule-request semantics to the existing communication runtime without giving the appointment layer authority over message transport, custody or PTU mechanics.

Target chain

accepted request -> handoff authorization -> appointment notice authored -> existing communication event -> actual receipt or non-receipt -> actor-specific knowledge -> rendezvous / cancellation / replanning

Core boundaries

`NOTICE_AUTHORED != NOTICE_DELIVERED`

`NOTICE_DELIVERED != NOTICE_BELIEVED`

`CANCELLATION_AUTHORED != ALL_PARTICIPANTS_AWARE`

`CONFIRMATION_SENT != MUTUAL_CONFIRMATION`

`RESCHEDULE_REQUESTED != RESCHEDULE_APPROVED`

`APPOINTMENT_CANCELLED != RESOURCE_TRANSFERRED`

`APPOINTMENT_CONFIRMED != RESOURCE_READY`

`MINECRAFT_DISPLAYED_MESSAGE != COMMUNICATION_RECEIVED`

Executable primitive

`tools/global_npc_resource_handoff_appointments.py` adds an append-only semantic notice ledger. It references Pass 343 handoff authorizations and communication event IDs owned by `InformationEventQueue`.

Supported V1 semantic notices are CONFIRM, CANCEL and RESCHEDULE_REQUEST.

Validation

A notice must reference a real, uncompleted handoff authorization. Sender and receiver must both be participants in that authorization. Self-addressed notices fail closed. Duplicate notice IDs and duplicate linked communication-event IDs are rejected. Notices authored after the handoff authorization expires are rejected.

Communication authority

The new layer does not create a second transport. `notice_delivery_status()` consumes the status already held by `InformationEventQueue`.

QUEUED, WAITING_LOCAL_ACK and failed events do not become receiver knowledge. DELIVERED does.

`known_notices_for_actor()` includes an actor's own authored notices and notices actually delivered to that actor. It does not infer faction-wide knowledge, room-wide knowledge or sender-intent awareness.

Coordination state

`coordination_state()` derives a coarse current coordination view:

- NO_UPDATE
- PARTIAL_CONFIRMATION
- MUTUALLY_CONFIRMED
- RESCHEDULE_REQUESTED
- CANCELLATION_AUTHORED
- CANCELLATION_DELIVERED

Mutual confirmation requires delivered confirmation in both directions between provider and physical receiving actor. The accountable requester can remain a separate actor and does not automatically inherit those receipts.

Cancellation awareness

`actors_unaware_of_authored_cancellation()` identifies authorization participants who neither authored nor actually received a cancellation. This supports stale-information travel without rewriting history or attributing negligence automatically.

This query describes knowledge exposure only. It does not determine moral responsibility, trust loss, employment consequences or whether institutional policy treats the cancellation as effective immediately.

Relationship to Pass 344

Pass 344 still owns failed physical rendezvous attempts. A participant can therefore arrive after a cancellation was authored but not delivered to them and record a valid no-show/absence observation. The appointment layer explains why their plan was stale; it does not erase the attempt.

Reduced version

No AutoPTU dependency. Semantic time, handoff authorization, existing communication queue, appointment notices, private knowledge and event-driven replanning are sufficient.

Rich version capability dependencies

Targeting / footprints / range / LoS: required only if a tactical scene needs exact target/perception geometry around a courier or handoff site.

Base movement legality: required for ordinary tactical movement.

Complete movement: required for interception, carrying constraints, push/pull, knockback, rescue or forced movement.

Core calculations: required for deterministic PTU arithmetic.

Action economy / initiative: required for tactical pickup, drop, handoff, guard or communication actions if those are eventually authored mechanically.

Full turn / round lifecycle: required for round-bound deadlines, delayed messages inside combat or staged objective changes.

Full stateful damage pipeline: required if actors or equipment take authoritative damage.

Status lifecycle: required for persistent conditions affecting participants.

Terrain / weather / hazards / zones / reactions: required when environmental conditions dynamically block a route or meeting site.

Move-specific behavior: each exact Move individually gated.

Abilities: each exact Ability individually gated.

Items: each exact PTU Item effect individually gated.

Trainer Features/perks: each exact Feature individually gated.

AI legal-action infrastructure: required for any new tactical communication, pickup, protection or handoff action.

AI tactical policy: required to choose delivery, protection, retreat, pursuit or other objective-aware tactics.

Minecraft/Cobblemon/Craftics adapter/playback: presentation only. A chat bubble, subtitle, animation or proximity cannot authoritatively create delivery or knowledge.

Live engine evidence

AutoPTU-Java head inspected for this pass: `30ff159abafbef6d14ef4a776789e9077dd26bc4`, merge of PR #398, `Preserve numeric Burrow speed in movement profiles`.

The slice adds numeric `burrowSpeed` to `MovementProfile` and regression coverage distinguishing Burrow 3 from Burrow 4 while preserving legacy boolean compatibility. This strengthens a movement-profile representation contract. It does not by itself verify every Burrow legality interaction, carrying, forced movement or complete movement.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains explicitly presentation-only.

Capability assessment

- targeting / footprints / range / LoS: VERIFIED for previously audited ordinary contracts;
- base movement legality: VERIFIED for previously audited ordinary contracts, with PR #398 adding stronger numeric Burrow profile representation;
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

1. Unknown or completed authorizations reject new appointment notices.
2. Only authorization participants can author or receive notices.
3. Duplicate semantic notice identity and communication-event identity fail closed.
4. A queued cancellation remains unknown to the receiver.
5. A delivered cancellation becomes known only to its actual receiver.
6. A sender knows the notice they authored.
7. Mutual confirmation requires delivered confirmation in both directions.
8. A reschedule request remains distinct from cancellation and approval.
9. Cancellation does not mutate resource custody.
10. Minecraft presentation cannot establish receipt.
11. No appointment notice creates `REQUEST_AUTOPTU` or a PTU Item effect.

Deferred work

- integrate delivery completion with a dedicated appointment-aware replan coordinator without duplicating Pass 287;
- define policy for when authored cancellation invalidates the operational rendezvous versus only the sender's attendance commitment;
- explicit reschedule acceptance and replacement authorization;
- travel-aware departure/arrival evidence;
- no-show expiry coordinator;
- repeated-failure trust policy only where canon supports it;
- checkpoint persistence for resource request/handoff/attempt/appointment ledgers;
- player-facing appointment UI and Minecraft acknowledgement;
- PTU/Caelo validation for any future mechanically active communication or Item effect.
