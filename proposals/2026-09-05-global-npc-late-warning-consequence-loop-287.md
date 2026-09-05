# Proposal — Late Warning / Divergent Consequence Loop

Status: PROPOSED NARRATIVE PATTERN
Date: 2026-09-05
Canon approval: NOT CANON-APPROVED
Region binding: none. This is a reusable global pattern.

## Premise

A meaningful world fact changes after an NPC has already committed to a plan. Someone else learns the new fact and sends a warning. Whether the warning arrives before, during or after the recipient's next decision changes what happens.

The premise works for:
- road or transit closure;
- dangerous wild activity;
- a competition changing venue or start time;
- an ally becoming unavailable;
- a faction order being revoked;
- a resource shipment failing;
- a suspect being sighted elsewhere;
- an environmental hazard becoming known;
- a rival changing plans;
- a rescue target moving.

The interesting state is not merely the fact itself. It is the distribution of knowledge over time.

## Reusable sequence

1. An NPC already has an agenda and possibly a journey in progress.
2. Another actor observes or otherwise legitimately learns a changed world fact.
3. Audience selection decides whether the first NPC is actually contacted.
4. A real communication envelope is scheduled through an available channel.
5. Until delivery, the recipient continues acting from older knowledge.
6. Successful delivery updates only that recipient's private state.
7. The delivery schedules one semantic wake-up.
8. Existing goals, commitments, relationships, travel and needs are reconsidered together.
9. The NPC may continue, reroute, report, seek help, cancel, investigate or request structured resolution.
10. Later characters can reconstruct who knew what, when they learned it and what decision followed.

## Quest and mystery value

This pattern supports consequences that do not require a villain or scripted betrayal.

A failed rendezvous can come from a warning arriving late rather than someone deliberately refusing to help. Two witnesses can make different choices because only one received updated information. A faction can appear disorganized because a private channel was delayed, while the source/provenance ledger later demonstrates what actually occurred.

The player can investigate causality through:
- sender and recipient;
- message creation and delivery time;
- channel status;
- source provenance;
- subsequent route or agenda changes;
- independent observations that confirm or contradict the warning.

This keeps mystery generation grounded in persistent state instead of retroactively inventing explanations.

## Rival / ally variant

A recurring rival learns that a planned challenge site has become unsafe.

If the warning reaches them early, they relocate the challenge and notify the player.
If it arrives after departure, they may divert midway.
If it never arrives, they can reach the original location and face the same world condition without privileged knowledge.
If they are already in structured combat when the information arrives, world-agent planning records the new knowledge but does not interrupt AutoPTU with an invented tactical action.

The same pattern works for a friend, mentor, courier, investigator, worker or faction representative. No role gets a special brain.

## Reduced implementation

The reduced version requires only verified/current Ouros world-agent seams:
- persistent agenda;
- semantic travel state;
- private memory/claim delivery;
- event-driven wake-up;
- replanning;
- world-state consequence recording.

Example outcome:
- warning arrives;
- NPC chooses `REPLAN_ROUTE`;
- semantic ETA changes;
- a meeting is delayed or missed;
- the world records the consequence.

No battle is forced.

## Full structured implementation

A richer version can turn the same late warning into a mechanical encounter. Examples include arriving at a blocked route during a wild confrontation, attempting a rescue under environmental pressure, or pursuing another actor after receiving new information.

Exact capability dependencies depend on authored mechanics:

- target selection, ranged attacks or LoS-sensitive encounter geometry -> targeting / footprints / range / LoS;
- ordinary capability-gated traversal -> base movement legality;
- interception, push, pull, knockback or other forced movement -> complete movement;
- accuracy/stat/type/deterministic arithmetic -> core calculations;
- legal action timing and initiative -> action economy / initiative;
- phase changes, delayed events or round-scoped behavior -> full turn / round lifecycle;
- HP/damage consequences that must persist correctly through hooks -> full stateful damage pipeline;
- poison/burn/other persistent status timing -> status lifecycle;
- mechanical weather, hazards, zones or reactions -> terrain / weather / hazards / zones / reactions;
- unusual individual Move clauses -> move-specific behavior;
- Ability-triggered effects -> abilities;
- held/consumable/equipment effects -> items;
- Trainer interrupts or special Features -> Trainer Features / perks;
- constructing legal tactical choices -> AI legal-action infrastructure;
- autonomously choosing among legal tactical actions -> AI tactical policy;
- visible Minecraft execution and semantic result playback -> Minecraft / Cobblemon / Craftics adapter/playback support.

A concept using only some of these families declares only those families. It must not inherit unsupported complexity merely for spectacle.

## Narrative safeguards

- A delayed warning does not prove negligence by the sender.
- A recipient continuing an old plan before delivery does not make them irrational.
- Faction membership does not imply everyone knew the warning.
- A failed delivery does not retroactively become received because the plot needs it.
- A received warning does not force one authored reaction; goals, obligations and relationships still matter.
- The adapter cannot invent delivery by displaying an animation.
- A full encounter can fall back to the reduced consequence version without changing the underlying story premise when required mechanics are not verified.

## Long-term arc potential

Repeated information timing can create durable social consequences. A courier may become known as reliable because messages consistently arrive through them. An institution may discover a weak communication route. Rivals can learn which people trust each other. Players may deliberately protect, intercept, improve or investigate information channels.

Those later systems require explicit mechanics for deception, public information, channel interference and reputation change. Pass 287 does not canonize them.
