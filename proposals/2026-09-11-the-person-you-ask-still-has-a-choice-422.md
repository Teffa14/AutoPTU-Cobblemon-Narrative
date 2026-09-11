# The Person You Ask Still Has a Choice — Pass 422

Status: PROPOSED / NON-CANON

## Premise

A warning changes one person's plan. That person decides another specialist would help.

The specialist does not change course merely because the first NPC selected `REQUEST_ASSISTANCE`.

The request must become a world action, travel through an explicit communication path and reach the specialist. The specialist then makes an independent decision from their own state.

## Canon-safe anchors

Existing Marea roles provide natural test surfaces without adding new canon.

Mara Veyra can plausibly identify a need for practical assistance. Teo Lark already maintains equipment and field instruments. Oren Vale already handles routine care. Dr. Nerea Sol already performs longitudinal observation. Lia Morn already coordinates dock windows.

This proposal does not establish a new standing hierarchy, incident, mandatory duty, relationship or schedule among them.

## Narrative state sequence

A legible version keeps these facts separate:

1. A field fact exists.
2. One NPC receives the fact.
3. That NPC replans.
4. Their planner selects an ordinary world intent such as `REQUEST_ASSISTANCE`.
5. A durable world-action intent records what that requester decided and why.
6. No second actor changes yet.
7. A separate communication attempt is authored toward one proposed recipient.
8. If the message is delivered, the recipient gains the request with provenance.
9. The recipient replans independently.
10. Acceptance may create a commitment, travel plan or later action. Refusal, delay and counter-proposal remain valid.

This preserves agency on both sides of the request.

## Example scene

A route report convinces Mara that an instrument check should happen before another team departs.

She decides to ask Teo for support.

At this point only Mara's state has changed. The world records that she intends to contact Teo.

If Teo is already repairing equipment needed elsewhere, travelling, resting or committed to another urgent job, the later delivered request may not outrank his current agenda.

He can accept for later, refuse, suggest another person, ask for the instrument to be brought to repair row or change course if the new problem is sufficiently important.

The player can later discover the full chain rather than seeing Teo's schedule change invisibly.

## Why this matters for recurring NPCs

Persistent characters should feel like people with overlapping responsibilities rather than quest terminals.

A field office can request help without owning every worker's future. A researcher can ask for transport without automatically scheduling the pilot. A medic can recommend a delay without globally freezing a departure.

Different responses create useful relationship and institution scenes without requiring deception or artificial conflict.

## Reduced implementation

The reduced version needs only:

- private knowledge;
- semantic time;
- event-triggered replanning;
- durable world-action intent records;
- explicit communication delivery;
- schedules and commitments;
- permissions;
- travel-time state.

No battle is required.

A complete quest beat can consist of one NPC asking for help, the request arriving late, the requested person declining because of another commitment, and the requester finding a different solution.

## Full implementation

A richer version can make the requested capability relevant to a structured encounter.

Examples include asking for a medic before a dangerous extraction, requesting an equipment specialist before entering a damaged facility, or asking an experienced field worker to join an escort through a hazardous route.

The request and acceptance remain world-agent facts. Exact combat legality, Features, Items and encounter actions remain under verified PTU/AutoPTU contracts.

## Capability dependencies

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required if the full encounter uses dragging, interception, forced displacement or similar mechanics.

Core calculations: VERIFIED only in audited paths.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL. Required by timed extraction, staged protection or delayed encounter phases.

Full stateful damage pipeline: PARTIAL when harm must persist from structured resolution.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact behavior.

Move-specific behavior: individually gated.

Abilities: PARTIAL and individually gated.

Items: individually gated.

Trainer Features/perks: individually gated. Narrative expertise cannot silently grant a mechanical Feature.

AI legal-action infrastructure: VERIFIED only for audited ordinary actions. Specialized rescue, escort, protect, retrieve, carry, interact or extract actions require explicit admission.

AI tactical policy: BLOCKING for specialized rescue-first, escort, protect-carrier, objective-aware withdrawal or disengagement policy unless implemented.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objective state, specialized non-KO completion and in-flight battle recovery.

## Reduced fallback

If the accepted specialist would require unsupported tactical mechanics, keep the request/acceptance story intact but resolve the practical problem through a supported ordinary field task, a verified simple encounter or a non-battle inspection.

Minecraft does not implement a substitute PTU rule merely to make the richer version work.

## Open questions

Which intent kinds are allowed to materialize directly into world-action intent records, and which should require an authored action policy first?

Should a request for a capability name a specific person immediately or allow audience resolution to choose among eligible specialists?

When a requested person accepts, does acceptance create a commitment directly or first create a proposed commitment requiring schedule conflict checks?

How should a counter-proposal preserve the original request's provenance while creating a new decision owned by the recipient?

When a request arrives during travel, should the recipient replan immediately or only at defined interruption-safe points for that travel action?

No answer above is canonized by this proposal.
