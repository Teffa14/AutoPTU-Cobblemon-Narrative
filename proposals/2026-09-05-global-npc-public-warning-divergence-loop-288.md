# Proposal 288 — Public Warning / Divergent Reception Loop

Status: PROPOSED NARRATIVE PATTERN
Date: 2026-09-05
Canon effect: NONE until approved and bound to authored world content

## Premise

A public service publishes a warning, result, opportunity, closure, recall, event notice or correction. The world fact can be public without becoming instantly known by every person.

Different persistent NPCs receive the publication at different times or not at all because access, coverage, receiving state and queue timing differ. Their later choices therefore diverge for explainable reasons.

## Reusable loop

An authoritative owner system creates or verifies an underlying event. A Media/publication actor publishes a claim derived from available evidence. The transmission/distribution layer exposes a service and scope. Eligible NPC receipts are expanded in bounded batches. Existing communication latency determines when each claim enters an NPC ledger. Selective replanning can then change travel, work, meetings, investigations or other world intents.

The player can encounter consequences before encountering the explanation.

Examples of original Ouros-compatible uses include:

- a route warning reaches one expedition before departure while another has already left;
- a competition schedule correction reaches a rival but not their travelling companion;
- a public request for assistance reaches specialists who actively receive that service while nearby civilians remain unaware;
- a correction arrives after an earlier mistaken report has already changed several agents' plans;
- a field notice becomes available in one service scope before a neighboring area receives it.

These are patterns, not canon events.

## Mystery / investigation value

A useful investigation question becomes more precise than “was the announcement public?” The player can establish:

- whether a publication existed;
- whether a transmission/service was available;
- whether a particular NPC was eligible to receive it;
- when their receipt event actually completed;
- what claim and provenance entered their ledger;
- whether they believed it strongly enough to replan.

This supports misunderstandings and accountability without requiring arbitrary NPC stupidity or omniscience.

## Reduced implementation version

The reduced version uses semantic world state only:

publication -> bounded receipt expansion -> information queue -> private ledger -> event-triggered replanning -> travel/schedule consequence.

No battle is required. The world can resolve missed departures, altered routes, delayed work, investigations and changed meetings entirely through Ouros state.

## Full encounter version

If a late or missed warning puts actors into a structured danger, Ouros authors a BattleSpec and requests AutoPTU. The public-information layer stops at the semantic reason the actors are present.

Possible mechanical dependencies are conditional:

- line-sensitive or ranged encounter geometry: targeting / footprints / range / LoS;
- ordinary capability traversal: base movement legality;
- interception, pushes, pulls, knockback or forced movement: complete movement;
- deterministic battle arithmetic: core calculations;
- initiative/action timing: action economy / initiative;
- delayed or phase-scoped consequences: full turn / round lifecycle;
- persistent damage hooks: full stateful damage pipeline;
- persistent status timing: status lifecycle;
- environmental danger or reactions: terrain / weather / hazards / zones / reactions;
- special clauses: move-specific behavior, Abilities, Items and Trainer Features/perks as individually selected;
- autonomous tactical choice: AI legal-action infrastructure plus AI tactical policy;
- visible authoritative scene playback: Minecraft / Cobblemon / Craftics adapter/playback support.

The narrative premise does not require the mechanically rich version. Until a selected capability family is verified, the encounter may use the reduced world-state consequence or a simpler audited BattleSpec.

## Safeguards

`PUBLIC_WARNING != UNIVERSAL_KNOWLEDGE`

`MISSED_WARNING != NPC_IRRATIONALITY`

`BROADCAST_RECEIPT != BELIEF`

`LATE_RECEIPT != RETCON`

`BATTLE_WON != COMMUNICATION_FAILURE_REPAIRED`

A later correction never deletes the fact that an earlier publication was received and acted upon.
