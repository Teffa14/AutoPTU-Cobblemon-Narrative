# Global NPC Assistance Renegotiation Dispatch Contract — Pass 442

Status: IMPLEMENTED GLOBAL CONTRACT
Canon effect: NONE

Purpose

Pass 440 made `REQUEST_RENEGOTIATION` a durable responder choice after an adverse negotiated-assistance start. Pass 441 preserved that choice atomically. The missing causal edge was communication: the requester could not learn that the responder wanted to reopen the accepted terms through an explicit world event.

Pass 442 adds `schedule_assistance_renegotiation_request(...)` in `tools/global_npc_assistance_renegotiation_dispatch.py`.

Contract

The dispatcher consumes an existing negotiated assistance commitment and an existing `REQUEST_RENEGOTIATION` disposition. It authors one responder claim and sends it to the original requester through the existing `InformationEventQueue`.

The payload preserves:

- commitment id;
- proposal id;
- start assessment id;
- disposition id;
- responder rationale reference;
- previously accepted start and end minutes;
- accepted location, scope and alternative references.

The request says only that the responder wants to reopen the agreement. It does not define replacement terms.

Knowledge boundary

The responder knows the request they authored immediately. The requester learns it only if the ordinary information envelope reaches `DELIVERED` and materializes a REPORT claim.

Failed channels, pending latency and local acknowledgement do not create requester knowledge.

Authority boundary

This owner does not:

- mutate or cancel the accepted commitment;
- create a replacement counterproposal;
- accept new terms for either actor;
- reserve time, route, access or resources;
- move an NPC;
- change relationship or blame state;
- mark the obligation fulfilled or missed;
- invoke AutoPTU.

A later proposal cycle must author any replacement terms explicitly. The original agreement remains historical fact.

Validation

Dispatch fails closed unless:

- the disposition exists;
- its kind is exactly `REQUEST_RENEGOTIATION`;
- its commitment exists;
- proposal and actor bindings match that commitment;
- the disposition belongs to the responder;
- the disposition occurred within the accepted assistance window;
- the authored message does not predate the disposition;
- both actors have knowledge ledgers;
- the communication channel exists.

Exact replay of an already scheduled event is idempotent. Reusing an event id with different envelope provenance fails closed.

PTU / Caelo / Kairos boundary

No PTU mechanic is adopted by this contract. The source inventory continues to expose Kairos/PTU routing material for comparison while no adopted Caelo override relevant to this communication seam is present. World-level communication and negotiated obligations remain Ouros simulation authority. Structured battle resolution still requires an explicit AutoPTU handoff.

Battle capability posture

This pass promotes no permanent engine capability family. Any later encounter produced by successful renegotiation remains individually gated for targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.
