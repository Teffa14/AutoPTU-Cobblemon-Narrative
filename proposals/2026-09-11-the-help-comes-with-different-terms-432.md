# The Help Comes With Different Terms — Pass 432

Status: PROPOSED / NON-CANON
Date: 2026-09-11

## Premise

A request for help does not need to end with yes, no or later.

The responder can offer a materially different version of the help.

The changed terms can concern:

- when the work happens;
- where it happens;
- how much of the original request the responder will cover;
- another way to contribute.

The response remains useful even when neither side has agreed yet.

## Marea regression surface

Use existing canon only.

Mara Veyra already coordinates field reports, route checks, wildlife incidents and practical assistance through the Marea Field Office.

Teo Lark already maintains ordinary equipment, lamps, carts and field instruments from repair row.

Dr. Nerea Sol already owns longitudinal ecological/weather observation and evidence quality work at Estación Mirador.

Those roles are sufficient to test negotiation without adding a new NPC, institution or geography.

Example non-canon setup:

Mara receives a field report that makes specialist assistance useful. She asks Teo for a specific contribution. Teo cannot satisfy the request as written because his current state, schedule, location or obligations make it unattractive or impossible.

Instead of ACCEPT, DEFER or REJECT, Teo selects `COUNTERPROPOSE_ASSISTANCE_REQUEST` and authors one or more concrete terms.

Possible transformed forms:

- time: Teo offers a later inspection window;
- place: Teo offers to inspect the equipment at repair row instead of travelling to the field site;
- scope: Teo offers diagnosis only rather than a full repair;
- alternative: Teo suggests a remote evidence check by a qualified observer before anyone travels.

None of those examples is canon until separately approved through normal canon governance.

## Required causal chain

1. Mara has a reason to request assistance.
2. Mara selects `REQUEST_ASSISTANCE`.
3. The request travels through explicit communication.
4. Teo receives it.
5. Teo replans from his own state.
6. Teo selects `COUNTERPROPOSE_ASSISTANCE_REQUEST`.
7. `OUROS_ASSISTANCE_COUNTERPROPOSAL_LEDGER_V1` records the concrete terms with the response action as provenance root.
8. The response itself can travel back through the existing assistance-response communication path.
9. The requester must not know the structured terms until a future communication seam explicitly carries them.
10. Any eventual agreement requires another requester-owned decision.

This preserves actor independence.

## Narrative consequences

A counterproposal creates useful branches without fabricating hostility or compliance.

A narrower scope can save time but leave part of the original problem unresolved.

A changed location can make the work safer or cheaper but add transport of an object or evidence.

A later time can preserve both actors' obligations while allowing the world state to change before the meeting.

An alternative contribution can route the story toward another character or evidence lane without forcing the original helper into work they did not choose.

Repeated counterproposals can also expose stable preferences through history. The system should derive that pattern from durable decisions rather than assigning a hidden personality label that overrides current state.

## Quest graph use

The same negotiated incident can contribute to existing canonical questline families without another runtime engine:

- `CHARACTER` when the focus is the responder's own priorities;
- `RELATIONSHIP` when repeated negotiation changes interpersonal history;
- `SETTLEMENT` when the assistance concerns a local service;
- `EQUIPMENT` or `ITEM` when a tool/object owns the problem;
- `EXPLORATION` when the changed terms alter where field work occurs;
- `FACTION` when an institutional duty or permission constrains the offer.

The underlying world event remains one event even when several questline views reference it.

## Reduced playable version

No battle is required.

A field report creates a request. The selected specialist sends back a counterproposal with a later time and narrower scope. The requester learns the response kind through the existing communication path. A later implementation seam transmits the structured terms. The requester can then decide whether to accept them, reject them or make another request.

This version exercises private knowledge, communication latency, schedules, obligations, locations and durable decisions.

## Full encounter version

If accepted terms later lead to hazardous field work, the encounter can add tactical pressure while preserving the same narrative premise.

Examples include protecting an inspection, retrieving equipment, crossing a dangerous route or containing an ecological disturbance.

The full version must declare the exact capability families it uses. Knockback, forced movement, interception, reactions, weather phases, dynamic hazards, delayed effects, complex statuses, ability-triggered terrain and Trainer Feature interrupts are not available merely because a simpler representative mechanic exists.

Current dependency posture:

- targeting / footprints / range / LoS: VERIFIED in audited scopes only;
- base movement legality: VERIFIED in audited scopes only;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED in audited scopes only;
- action economy / initiative: PARTIAL;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING;
- move-specific behavior: individually gated;
- abilities: PARTIAL / individually gated;
- items: individually gated;
- Trainer Features / perks: individually gated;
- AI legal-action infrastructure: specialized objective actions require explicit admission;
- AI tactical policy: BLOCKING for specialized objective policies;
- Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING for specialized objective state and non-KO completion.

## Canon questions left open

- Which concrete incident, if any, should first use this pattern?
- Which structured refs should become canonical identifiers for work scope and alternatives instead of free-form authored strings?
- Can a counterproposal expire silently, or must expiry create an explicit world transition and/or message?
- What exact action kind should the requester use to accept a counterproposal rather than the original request?
- When accepted terms alter location, should route planning occur before or after commitment creation?

No answer is canonized by this proposal.
