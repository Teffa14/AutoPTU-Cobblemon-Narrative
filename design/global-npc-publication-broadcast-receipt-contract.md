# Global NPC Public Publication / Broadcast Receipt Contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: region-neutral public-information reception by persistent/recurring Ouros NPCs.

## Purpose

Pass 161 already separates broadcast program, episode, transmission, coverage, audience receipt and belief. Passes 282-287 provide private ledgers, transport, audience selection and selective replanning. This contract closes the executable seam between a public transmission/publication and the individual NPCs who actually receive it.

A public publication is never equivalent to universal knowledge.

`PUBLICATION_EXISTS != TRANSMISSION_OCCURRED != NPC_RECEIVED != NPC_BELIEVED`

## Ownership

Existing Media/Broadcast continuity remains owner of programs, episodes, transmissions, editorial framing and correction lineage. Communications Network remains owner of service topology and coverage. The global NPC layer owns only per-agent eligibility/receipt and subsequent private belief state.

This implementation therefore consumes explicit service/scope facts; it does not invent towers, radio technology, subscriptions, coverage or audience metrics.

## Reception model

A candidate receiver can receive a publication only when all required gates pass:

- receiving is enabled for that actor;
- the actor has access to the named service;
- an authored scope restriction matches when the publication has scoped distribution;
- topic filtering matches when the actor exposes explicit topic interests;
- the publication has not passed its retention window;
- the actor has a persistent knowledge ledger;
- the referenced delivery channel exists.

Passing the gates makes an NPC eligible for a receipt event. It does not immediately mutate belief.

The publication is expanded into ordinary `InformationEventQueue` envelopes. Existing channel latency, failure, local acknowledgement, idempotency and backlog semantics therefore remain authoritative.

## Bounded expansion

Mass communication cannot be implemented as one giant per-tick loop or by setting private `max_recipients` to an enormous value.

`expand_publication_bounded()` accepts an explicit receiver budget and a stable cursor. Eligible actors are ordered by stable agent ID. A batch schedules at most the allowed number of receipts and returns remaining count plus the next cursor.

This is a first deterministic scaling seam. Production audience indexes may later replace linear candidate enumeration without changing receipt semantics.

`PUBLIC_AUDIENCE_EXPANSION != PRIVATE_CONTACT_SELECTION`

Pass 285 answers whom a sender personally chooses to contact. Pass 288 answers which individually modeled actors are eligible to receive an already-authored public publication through a service.

## Coverage and access

Being physically inside a region does not guarantee receipt. Being a faction member does not guarantee receipt. Being a fan of a topic does not create access to a service.

Likewise, a transmission may succeed while one NPC remains unaware because they were outside coverage, lacked access, were not receiving that service, or received the publication only later.

## Provenance

Public receipts use the existing claim transmission path. Every receiver claim retains the publisher's source claim as parent and preserves the original provenance root.

Hearing the same report through several rebroadcasts derived from one source does not manufacture independent corroboration.

A correction or retraction must be a new publication/evidence object linked through Media correction lineage. It must not delete or rewrite the historical earlier receipt.

## Retention

`retention_until_minute` limits whether new receipts may be materialized from a publication. It does not erase claims already received and is not a forgetting mechanic.

Future persistent media surfaces may permit later retrieval of archived material through a separate access action. That behavior is not inferred here.

## Minecraft/Cobblemon boundary

A remote public channel may deliver without a loaded entity if its channel contract permits it. A local display, announcement board, conversation or visible screen can require adapter acknowledgement through the existing communication queue.

Minecraft presentation never creates receiver knowledge merely because audio/text was rendered nearby.

## AutoPTU boundary

Ordinary publication and reception require no PTU tactical capability.

If a received warning later causes a structured encounter, the encounter declares only the capabilities it actually uses. This layer never resolves targeting, movement, initiative, damage, statuses, reactions, Moves, Abilities, Items or Trainer Features.

## Canon status

This contract canonizes no radio network, newspaper, broadcaster, phone system, region, faction or NPC. Fixture services, scopes and actors are synthetic.

The implementation is proposed reusable Ouros MMO infrastructure. PTU/Caelo/Kairos provide no adopted rule for publication fanout, latency or retention; these remain explicit Ouros simulation policy.
