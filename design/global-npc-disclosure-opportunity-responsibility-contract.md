# Global NPC disclosure opportunity and responsibility contract — Pass 302

Status: IMPLEMENTED GLOBAL CONTRACT
Date: 2026-09-06

## Purpose

Pass 301 established explicit disclosure expectations and observable silence. Pass 302 prevents infrastructure failure, missing reachability, pending delivery or an unacknowledged local projection from being misclassified as willful withholding.

The governing rule is evidence-first responsibility. A strong disclosure duty is not enough by itself. Ouros must also have evidence that the speaker had a usable communication opportunity before silence can become an `EXPECTATION_BREACHED` finding.

## Executable seam

`tools/global_npc_disclosure_opportunity.py` consumes the existing `CommunicationOpportunity`, `DisclosureExpectation`, dispatch result and `InformationEventQueue` state. It does not create another communication network.

`CommunicationAccessStatus` records one of these evidence states:

- `AVAILABLE`: a usable opportunity is explicitly evidenced, including authored direct contact;
- `NO_KNOWN_CHANNEL`: audience resolution/dispatch found no known channel for that receiver;
- `ATTEMPT_QUEUED`: a real envelope exists but its delivery time or processing has not completed;
- `WAITING_LOCAL_ACK`: delivery reached the local-projection boundary but has not been accepted;
- `DELIVERY_FAILED`: an attempted delivery failed through the existing queue semantics;
- `DELIVERED`: the queue records actual delivery.

`CHANNEL_UNAVAILABLE` is reserved for explicit pre-attempt infrastructure evidence when a future producer can distinguish that state without fabricating a dispatch.

## Responsibility classification

`assess_disclosure_responsibility()` produces an evidence-backed classification.

A missing channel yields `NO_USABLE_PATH`. A queued or local-ack-waiting attempt yields `ATTEMPT_IN_PROGRESS`. A failed attempted delivery yields `ATTEMPT_FAILED`. None creates a speaker trust penalty.

A non-silent policy decision remains `DISCLOSED_OR_DECEIVED`; truth and deception continue through their existing systems.

Only `CommunicationPosture.SILENT` plus `AVAILABLE` access can delegate to Pass 301 `assess_observable_silence()`. If the active expectation is strong enough, the result becomes `WILLFUL_WITHHOLDING` and carries the existing `DisclosureAssessment`. Therefore Pass 301 trust handling remains authoritative; Pass 302 does not duplicate relationship mutation.

A silent decision paired with a delivered message for the same opportunity fails closed as causally inconsistent.

## Non-omniscience and provenance

The runtime never searches all channels or private state to infer that a speaker “could have tried harder.” Access must come from explicit dispatch state or authored evidence such as a face-to-face scene.

A communication failure does not prove innocence about every possible route. It proves only the scoped fact represented by its evidence record. Future investigations may add independent access evidence without rewriting earlier findings.

Infrastructure state, speaker intent, dispatch attempt, message delivery, receiver knowledge and social responsibility remain separate facts.

## Persistence boundary

This pass does not add another registry or persistence payload. Queue delivery state already persists through the information queue/world checkpoint, and Pass 301 owns breach idempotency. `CommunicationAccessEvidence` and the responsibility finding are deterministic projections over explicit source state.

If future authored evidence must survive independently after source logs are compacted, add a durable evidence registry under the world checkpoint rather than silently storing it in relationship state.

## Mechanical boundary

The reduced missing-warning investigation is world-simulation only and requires no AutoPTU battle mechanic.

A full relay-repair or rescue encounter must declare only the families it actually uses. Wind, current, collapse zones or environmental hazards depend on `terrain/weather/hazards/zones/reactions`; forced displacement or interception depends on `complete movement`; delayed phases depend on `full turn/round lifecycle`; mechanical damage depends on the `full stateful damage pipeline`; conditions depend on `status lifecycle`; any Move, Ability, Item or Trainer Feature uses its owner family; autonomous tactical rescue depends on `AI tactical policy`; visible authoritative Minecraft resolution depends on `Minecraft/Cobblemon/Craftics adapter/playback support`.

No representative mechanic promotes an entire capability family.
