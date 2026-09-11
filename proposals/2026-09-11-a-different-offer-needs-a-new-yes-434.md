# A Different Offer Needs a New Yes — Pass 434

Status: PROPOSED / NON-CANON
Canon effect: NONE

## Premise

A person asks another NPC for help. The responder cannot meet the original request exactly and sends different terms. The requester receives those terms. The changed offer still requires a new decision.

The story value comes from preserving agency on both sides. A requester who asked for immediate field repair may receive an offer for a later inspection, a narrower diagnosis, another location or a remote alternative. Receipt creates knowledge. Acceptance creates a durable choice. The actual work remains downstream.

## World sequence

1. Requester selects `REQUEST_ASSISTANCE` toward one explicit responder.
2. The request travels through ordinary communication.
3. The responder receives it and replans from their own state.
4. The responder selects `COUNTERPROPOSE_ASSISTANCE_REQUEST`.
5. Structured terms become durable under one `proposal_id`.
6. Those terms travel back through ordinary information delivery.
7. Only terminal delivery gives the requester the terms claim.
8. The requester replans.
9. The requester may select `ACCEPT_ASSISTANCE_COUNTERPROPOSAL` or `REJECT_ASSISTANCE_COUNTERPROPOSAL`, naming that exact proposal in `source_ref`.
10. Acceptance still does not perform or schedule the proposed work.

## Possible Marea regression surface

Mara Veyra and Teo Lark remain useful regression actors because existing project material already uses Mara for coordination and Teo for ordinary equipment/field-instrument maintenance. This proposal does not establish a new incident, obligation, standing agreement, schedule, communication channel or relationship between them.

Example only: Mara asks for immediate assistance. Teo offers a later diagnostic window at an existing site and limits the scope to inspection. Mara can accept those changed terms, reject them or let them expire.

The example exists to test the global ownership chain. It is not Marea canon.

## Reduced implementation

The complete premise can run without AutoPTU:

- semantic time;
- two private knowledge ledgers;
- explicit communication events;
- durable world-action intents;
- structured proposal terms;
- delivery-triggered requester replanning;
- explicit accept/reject decision.

The next scene may be an appointment, an inspection report, a reschedule or a missed opportunity. No battle is required.

## Mechanically rich extension

After a later commitment owner exists, an accepted proposal could lead to a hazardous repair, escort, retrieval, rescue, containment or disputed access scene. The negotiated `scope_ref` can constrain what the NPC agreed to do without granting tactical verbs automatically.

Example full version: the accepted scope covers inspection of unstable equipment in a hazardous site. Environmental pressure changes during the visit, and the party may choose whether to withdraw, stabilize the site or request tactical assistance.

Example reduced version: the same inspection occurs as world-state checks and evidence collection. A hazard can close the site or end the appointment without simulating knockback, reactions, status chains or complex terrain.

Both versions preserve the same narrative premise: the specialist agreed to a bounded scope, not to every possible consequence at the site.

## Explicit capability dependencies for the full version

Targeting/footprints/range/LoS is required if positions and targetable equipment matter; current status is VERIFIED only in audited scopes.

Base movement legality is required for ordinary grid traversal; VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement becomes required only if the hazard displaces actors or allows interception; current status PARTIAL.

Core calculations are required for audited standard calculations; VERIFIED only in audited scopes.

Action economy/initiative is required if the site becomes a structured encounter; current status PARTIAL.

Full turn/round lifecycle is required for phase- or round-sensitive consequences; current status PARTIAL.

Full stateful damage pipeline is required if environmental or combat damage must persist through all normal stages; current status PARTIAL.

Status lifecycle is required for persistent or timed status effects; current status PARTIAL.

Terrain/weather/hazards/zones/reactions is required if the environment changes tactical legality or fires reactions; current status MIXED / PARTIAL / BLOCKING by exact behavior.

Move-specific behavior, abilities, items and Trainer Features/perks remain individually gated whenever the scene depends on a specific one.

AI legal-action infrastructure requires explicit admission for specialized verbs such as inspect, brace, protect, retrieve, carry or extract.

AI tactical policy remains BLOCKING for specialized objective behavior unless verified by dedicated policy evidence.

Minecraft/Cobblemon/Craftics adapter/playback remains PARTIAL / BLOCKING for authoritative specialized objective state, non-KO completion and recovery of an in-flight structured operation.

## Consequences and hooks

A narrow accepted scope can create later friction without retroactive rewriting. The specialist may complete exactly what was agreed while the requester wishes they had asked for more. Another actor may solve the broader problem first. New evidence may make the accepted scope obsolete. An expired offer can remain part of relationship history without becoming executable.

These outcomes should emerge from durable events and later policy owners, not from fixed personality scripts.

## Open design questions

An accepted counterproposal still needs a separate owner that converts the proposal's exact time/scope/location terms into an appropriate scheduled commitment.

The structured counterproposal ledger still needs coherent checkpoint integration before restart can be trusted to preserve the whole negotiation chain atomically.

Future normalization may be needed for `scope_ref` and `alternative_ref` before systems treat them as machine-authoritative action contracts.

Route reservation and resource allocation remain separate owners and must occur after agreement rather than being inferred from it.
