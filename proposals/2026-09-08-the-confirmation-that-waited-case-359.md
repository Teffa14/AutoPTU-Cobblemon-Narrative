# The Confirmation That Waited — Pass 359

Status: PROPOSED / NON-CANON
Canon authority: NONE
Date: 2026-09-08

## Premise

A field team has an accepted request and a valid authorization to collect a shared instrument from a service point. Before the pickup window opens, the provider authors a confirmation and sends it through an ordinary communication channel.

The session ends while the message is still in transit.

When the world resumes, the appointment notice still exists as a historical act. Whether the receiver knows about it depends on the separately restored communication runtime.

No new Ouros institution, named NPC or regional fact is asserted by this proposal.

## Investigation surface

The player can potentially reconstruct:

- the accepted resource request;
- the handoff authorization and its future-valid window;
- who authored the confirmation;
- who it targeted;
- the source claim and communication event identity;
- whether delivery actually occurred;
- what the receiver currently remembers;
- whether an arrival or failed attempt later occurred;
- whether custody eventually changed hands.

The same records support several outcomes without rewriting history.

If delivery completed before departure, the receiver can plan around the confirmed window.

If the message remained queued, the receiver can rationally continue using older knowledge.

If a later cancellation was authored but not delivered, the provider can know the appointment changed while the receiver still travels toward it.

If a successful transfer occurs later, the earlier confirmation remains part of the causal record rather than disappearing because the task finished.

## Reduced implementation version

This version needs no AutoPTU battle.

It uses semantic time, resource request history, handoff authorization, Pass 345 appointment notices, the information queue, knowledge/memory, travel, failed-attempt history and checkpoint restoration.

The player can wait, contact a participant, inspect available records, reroute, return later or continue another obligation.

## Rich encounter version

After the appointment is eventually confirmed and the pickup succeeds, the receiving actor may need to carry the instrument to a field observation site while a time window remains open.

A wild encounter can interrupt the route. The narrative objective is to preserve the instrument and complete or safely abandon the delivery obligation. Defeating every opponent is not required by the premise.

Possible tactical expressions include ordinary route positioning, protecting the carrier, reaching an exit, interception, forced separation, environmental delay or a round deadline. Each expression keeps its own implementation gate.

## Engine capability dependencies

Targeting / footprints / range / LoS: required for ordinary tactical targeting in the rich version; current audited ordinary scope is VERIFIED.

Base movement legality: required for ordinary route movement; current audited scope is VERIFIED.

Complete movement including push/pull/knockback/interception/forced movement: required only if the encounter uses interception, forced separation or displacement; PARTIAL.

Core calculations: required for ordinary resolved attacks/checks routed through AutoPTU; VERIFIED within audited deterministic scope.

Action economy / initiative: required for structured turns; audited primitives are VERIFIED, while explicit cargo/pickup/drop actions remain ungated by a complete contract.

Full turn / round lifecycle: required for round deadlines, start/end-round effects or delayed timing; PARTIAL.

Full stateful damage pipeline: required for ordinary damaging combat; PARTIAL as a category-wide claim.

Status lifecycle: required for persistent conditions affecting the carrier or route; PARTIAL.

Terrain / weather / hazards / zones / reactions: required only when those mechanisms actually alter tactical state; MIXED / PARTIAL / BLOCKING by exact family.

Move-specific behavior: each selected Move remains individually gated; PARTIAL overall.

Abilities: each selected Ability remains individually gated; PARTIAL overall.

Items: battle-active Items remain individually gated; PARTIAL overall.

Trainer Features / perks: any interrupt, modifier or tactical Feature remains individually gated; PARTIAL overall.

AI legal-action infrastructure: ordinary audited legal actions are VERIFIED; cargo/objective-specific actions remain undefined.

AI tactical policy: BLOCKING for protect-carrier, delivery-first, interception, rerouting and disengage-after-objective behavior.

Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING for cargo ownership, objective semantics and end-to-end authoritative playback.

## Degradation rule

If any rich tactical dependency is absent, the appointment story does not change. Resolve the travel interruption at world level or use a simpler audited encounter. Minecraft must not implement missing PTU rules to preserve the scene.

## Canon questions left open

Which institutions, if any, use formal appointment confirmations in Ouros remains unset.

No cancellation penalty, trust consequence, staffing rule or service priority is implied.

No named NPC is assigned this case until a future canon-authoring pass deliberately binds it.
