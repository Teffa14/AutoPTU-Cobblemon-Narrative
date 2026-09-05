# Pass 279 proposal — living recurring NPC agenda loop

Status: PROPOSED / NOT CANON
Date: 2026-09-05
Scope: reusable worldwide encounter/relationship structure

## Premise

A recurring rival, mentor, coworker, courier, investigator or friend should continue having a life when the player is elsewhere. They maintain long-term goals, ordinary needs and scheduled commitments. The player can intersect that agenda, disrupt it, help it or miss it.

No specific NPC, faction, settlement or region is canonized by this proposal.

## Reusable loop

An important NPC has one or more durable goals and a short agenda. The player learns only some of it through conversation, observation or messages.

The same NPC can therefore:
- be at work during one visit;
- leave because a hard commitment becomes due;
- delay an optional conversation because rest or another need becomes critical;
- miss an appointment because travel or another world event prevented arrival;
- report/reschedule rather than teleport into place;
- react to a genuine emergency only after learning about it;
- later resume the durable goal that was interrupted.

The world state explains absence instead of treating absence as a despawn accident.

## Example fixture-shaped story

A recurring Trainer is preparing for a certification, competition or professional task. That remains a durable goal across several player visits.

The player arranges a meeting for a later semantic-time window. Before the meeting, the NPC receives unrelated work or social obligations. If the player arrives early, the NPC may still be occupied. If the commitment becomes due, it gains weight. If the NPC cannot arrive, a missed-commitment follow-up can create a message, apology, replacement meeting, relationship consequence or new quest lead.

If both parties meet and choose to train through structured PTU mechanics, the world agent emits `REQUEST_AUTOPTU`.

The resulting battle/training outcome can later feed relationship, memory and progression systems. Pass 279 does not define that return path.

## Reduced implementation

The reduced version requires no battle engine:
- persistent NPC identity;
- durable goal state;
- need pressure;
- semantic schedule state;
- message/knowledge intake;
- travel/work/report/rest world intents;
- local Minecraft projection where available.

A scheduled spar can be represented as conversation and rescheduling until structured handoff is available.

## Full implementation

The full version may allow a scheduled commitment to culminate in a structured training match, pursuit, confrontation or other mechanical encounter.

Capability dependencies must be declared from what that encounter actually uses:

- targeting/footprints/range/LoS — required when the structured encounter performs tactical targeting;
- base movement legality — required for ordinary tactical movement;
- complete movement — required only if push/pull/knockback/interception/forced movement appears;
- core calculations — required for PTU arithmetic;
- action economy/initiative — required for structured turns/actions;
- full turn/round lifecycle — required for a complete battle sequence;
- full stateful damage pipeline — required if damage persists through the structured encounter;
- status lifecycle — required if statuses are applied/expire;
- terrain/weather/hazards/zones/reactions — required only when the encounter uses them mechanically;
- move-specific behavior, abilities, items and Trainer Features/perks — each required only when selected content depends on that family;
- AI legal-action infrastructure — needed for machine-controlled legal tactical choices;
- AI tactical policy — needed for autonomous selection among those legal tactical choices;
- Minecraft/Cobblemon/Craftics adapter/playback — needed for end-to-end visible structured playback.

World-level scheduling itself does not depend on those battle families.

## Narrative consequences

This structure enables recurring characters to feel persistent without omniscience or scripted omnipresence. Missed meetings become authored world consequences instead of bugs. The player's relationship with an NPC can develop through respecting, disrupting or helping with their agenda.

Future passes can attach relationships, faction obligations, travel paths and communication propagation to the same agenda layer without changing its region-neutral semantics.

## Open questions

- How should travel duration reserve time before a commitment without granting teleportation?
- Which commitments can be cancelled, delegated or renegotiated?
- How should relationships alter willingness to interrupt another goal?
- How are recurring schedules represented without creating unbounded event queues?
- What state returns from AutoPTU into memory/relationship progression after a scheduled structured encounter?
