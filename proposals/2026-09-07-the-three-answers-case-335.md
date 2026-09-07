# The Three Answers — Pass 335

Status: PROPOSED / NON-CANON
Date: 2026-09-07
Depends on: `design/global-npc-belief-aware-dialogue-projection-contract-pass-335.md`

## Premise

A routine institutional delivery fails to arrive at its expected destination. The package is ordinary enough that the incident begins as a practical search rather than a criminal accusation.

Three recurring NPCs appear to give incompatible accounts of the last leg of the delivery:

- one says the carrier left by the north route;
- one says the carrier was redirected to the lower road;
- one says the delivery never left the transfer point.

All three statements can be sincere.

The investigation becomes a test of what each person actually knows rather than a contest to identify which witness is lying.

No settlement, institution, route, carrier, package, species or named NPC is canonized by this proposal. It is intentionally region-neutral so it can later bind to an established place without forking the global NPC system.

## Hidden authored state for the case

The case author chooses a concrete truth before play. One example structure:

- Witness A directly saw the carrier depart toward the north approach but lost sight before the route fork.
- Witness B received a message saying a lower-road redirect had been requested, but never saw the carrier receive it.
- Witness C saw the package remain at the transfer point earlier in the day and has not received the later departure log.
- the institution's public status board still displays an older operational assumption;
- a later record can establish which message was delivered and when without automatically proving the carrier's physical path.

Other truth structures are valid if every claim keeps explicit provenance and semantic time.

## Why the first conversation is misleading

A generic dialogue system tends to flatten all three NPCs into confident summaries.

The belief-aware version exposes materially different answers depending on the player's question.

### Ask: `What happened?`

Witness A may state a working belief based on direct observation.

Witness B may state a working belief based on a received redirect message.

Witness C may state a stale but sincere belief based on an earlier observation and missing later information.

### Ask: `What did you personally see?`

Witness A can narrow the claim to departure toward an approach, not completion of a route.

Witness B may have no firsthand route observation at all.

Witness C can identify the earlier package position and time.

### Ask: `Who told you?`

Witness B can identify or fail to identify the source according to actual attribution state.

Witness A does not need a source for the directly observed portion.

Witness C may reveal that nobody told them the package departed.

### Ask: `How sure are you?`

The response should expose the relevant uncertainty class rather than invent a percentage.

This makes dialogue itself a navigable evidence surface without creating a lie-detection minigame.

## Adventure loop

The player first receives the operational problem: find the delayed delivery or determine whether the destination should keep waiting.

The player interviews available actors and notices that broad summary questions produce apparent contradiction.

More precise questions separate observation, report, source and inference.

The player can then seek one or more external evidence nodes:

- a dispatch or departure record;
- a route checkpoint observation;
- a message-delivery receipt;
- a public status-board revision history;
- a physical observation at the route fork;
- the carrier or package itself if later found.

Each node answers a narrow question. No single generic `clue collected` flag completes the case.

The player can return to witnesses with new evidence. Their beliefs may update only if the new information is actually communicated and accepted through the existing memory/belief systems.

## NPC arcs and relationship consequences

The case can create small durable character changes without requiring betrayal.

Possible outcomes include:

- an NPC learns to distinguish what they observed from what they inferred;
- another becomes more careful about naming sources;
- an institution changes how it publishes delivery status;
- two coworkers discover that they were operating from different publication versions;
- a witness who was initially treated as unreliable is later shown to have given the narrowest accurate statement;
- a confident witness retains social credibility while acknowledging that their earlier inference exceeded the evidence.

These are candidate consequences. They require later binding to actual NPC relationship and institutional state before becoming world facts.

## No forced culprit

The delivery can be delayed by an ordinary cause: a missed message, route obstruction, carrier decision, scheduling conflict, incorrect status publication or another authored world event.

If later evidence introduces theft, deception or hostile interference, that becomes a separate case fact with its own provenance.

`CONFLICTING_TESTIMONY != LIAR_PRESENT`

`MISSING_DELIVERY != CRIME`

## Reduced encounter version — usable with current verified basics

The entire core adventure can run without structured battle.

Use:

- existing world-agent schedules and commitments;
- explicit communication delivery;
- durable claim ledgers;
- retrieval/access state;
- subjective source attribution;
- belief assessment;
- publication revision/receipt history;
- the new read-only dialogue projection contract;
- static route observations and semantic world events;
- ordinary travel/world investigation.

If an ordinary battle is desired for pacing, it can occur at a static route location for an independently authored reason. The battle result may establish only narrow tactical facts such as safe passage through that encounter.

Battle victory does not reveal the correct witness, route history or package provenance.

## Rich encounter version — optional later implementation

A richer final scene can place the carrier near a changing route hazard while two groups arrive with different assumptions about where the carrier should go.

Possible objectives:

- reach the carrier before a route window closes;
- protect the carrier rather than defeat all opponents;
- communicate a verified correction during the encounter;
- escort a noncombatant through legal terrain;
- withdraw if the route becomes unsafe;
- prevent an avoidable confrontation caused by stale information.

This version is explicitly capability-gated.

### targeting / footprints / range / LoS

Ordinary static targeting is VERIFIED within existing audited contracts.

Any smoke, darkness, concealment, unusual elevation or dynamic visibility requires additional verified support.

### base movement legality

VERIFIED for ordinary audited movement.

Any special climbing, swimming, jumping, mounts or route-specific movement needs separate evidence.

### complete movement including push / pull / knockback / interception / forced movement

PARTIAL.

Escort interception, rescue displacement, moving hazards, knockback at unsafe edges and forced movement remain gated.

### core calculations

VERIFIED for ordinary audited deterministic calculations. No delivery, persuasion or route-check formula is invented.

### action economy / initiative

VERIFIED for ordinary audited primitives.

Special `deliver message`, `secure package`, `signal`, `escort` or `convince` tactical actions need explicit contracts before they consume battle actions.

### full turn / round lifecycle

PARTIAL.

A timed route closure, delayed message arrival during battle or phased environmental change depends on this family.

### full stateful damage pipeline

PARTIAL.

Any route hazard that causes real HP/Injury consequences needs authoritative support.

### status lifecycle

PARTIAL.

No custom confused, panicked, delayed, burdened or similar status is created for the narrative premise.

### terrain / weather / hazards / zones / reactions

MIXED / PARTIAL / BLOCKING by subfamily.

Dynamic route hazards, warning zones, changing access or reaction windows remain gated.

### move-specific behavior

PARTIAL. Every Move used for signaling, rescue, mobility, protection or terrain interaction needs individual verification.

### abilities

PARTIAL. Flavor cannot grant route sensing, message delivery, tracking or protection behavior.

### items

PARTIAL. Radios, signal devices, ropes, transport containers or route gear gain no tactical effects from this proposal.

### Trainer Features / perks

PARTIAL. No Feature provides invented interrogation, investigation, logistics or communication bonuses.

### AI legal-action infrastructure

VERIFIED for ordinary audited legal-action infrastructure.

### AI tactical policy

BLOCKING for a fully autonomous rich version where NPCs must prioritize escort, communication, withdrawal and non-defeat objectives.

### Minecraft / Cobblemon / Craftics adapter and playback

PARTIAL / BLOCKING end-to-end.

The adapter may render witnesses, routes, signs, messages, carrier and package state supplied by Ouros. It cannot infer what an NPC knows from proximity, choose which testimony is true, mark a message as received because a visual animation played, or convert a Minecraft item pickup into authoritative package recovery.

## Implementation value

This case is a regression fixture for the new dialogue contract because all three witnesses can remain honest while their broad answers conflict.

A correct implementation must make the investigation solvable by provenance and semantic time rather than tone, arbitrary dialogue flags or omniscient quest scripting.

## Unresolved canon fields

Before promotion, a content owner must choose:

- region and settlement;
- institution or independent actors involved;
- package and its significance;
- carrier identity;
- route topology;
- exact authored truth;
- witness identities and starting evidence;
- communication channels;
- whether a public status system exists;
- aftermath;
- whether any structured encounter is necessary.

Until those fields are reviewed, this file remains a reusable non-canon adventure candidate.