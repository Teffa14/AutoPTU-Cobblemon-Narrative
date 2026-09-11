# Pre-start Commitment Viability Research — Pass 437

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-11

## Scope

This pass looks for reusable structures for a narrow world-simulation problem left open by Pass 436: an assistance agreement has already been negotiated and persisted, but new evidence before its start can make fulfillment risky or impossible.

The research question is not how to erase, retroactively fail, or silently reschedule the agreement. The question is how to preserve what was agreed while allowing the responder to observe that the present world no longer supports the original plan.

The complete recursive repository tree at the Pass 436 head was inventoried before writing. Current focus, canon surfaces, assistance Passes 422–436, world travel, replanning, schedules, private knowledge, counterproposal terms, negotiated commitments, checkpoints, and prior research source names were checked before selecting sources.

Repository searches confirmed that `Wartales` and r/PokemonTabletop thread `1gfdmzw` had no prior source-level match. Frequently reused anchors including Pentiment, Roadwarden, Pokémon Ranger, Majora's Mask, Six Ages, Heaven's Vault, Pyre, Unsighted, Citizen Sleeper, Battle Brothers, Pokémon Unbound, Shadows of Doubt and the 2024 PTU `Question for Exploration` thread were not reused as primary sources.

## Source 1 — Wartales contracts preserve an accepted job while the world remains a separate state

Public sources:
- Wartales Wiki, `Bounties and Contracts`: https://game.wiki/wartales/bounties-and-contracts
- Wartales Wiki, `Help requested: Drunkards`: https://wartales.fandom.com/wiki/Help_requested%3A_Drunkards

Observed high-level structures:
- a contract is an identifiable accepted job rather than the same thing as its objective state;
- designed contracts can describe local problems while allowing more than one resolution method;
- a local situation can remain present when the player disengages instead of being auto-resolved by opening or accepting the contract;
- contract identity, objective state and resolution method are separable concepts.

Reusable Ouros transformation:
- preserve the negotiated assistance commitment as historical agreement state;
- represent later execution viability as separate evidence-backed state;
- a route closure, revoked access, missing resource or invalidated premise should not rewrite what the actors previously agreed;
- the responder can reconsider whether and how to fulfill the promise without pretending the promise never existed;
- a blocked original method can lead to communication, a new proposal, a different lawful method, or a missed commitment rather than an automatic combat encounter.

Excluded material:
- Wartales factions, currencies, named contracts, map locations, dialogue, reward values and combat scenarios;
- its bounty-board economy and progression rules;
- any assumption that Ouros contracts share Wartales cancellation or reward semantics.

## Source 2 — PTU encounter discussion separates opposition from the actual objective

Public source:
- r/PokemonTabletop, `Needing help balancing an encounter` (2024-10-30): https://www.reddit.com/r/PokemonTabletop/comments/1gfdmzw

Observed high-level structures:
- community advice asks what the opposing group is actually trying to accomplish rather than treating every encounter as a pure defeat-all fight;
- participants discuss an enemy objective continuing while players decide whether to spend time fighting or interfere with the objective;
- the later report says players used the environment and better tactical choices, demonstrating that encounter state can change through interaction rather than only HP depletion.

Reusable Ouros transformation:
- when an accepted field appointment becomes difficult, the narrative owner should preserve the underlying objective separately from any battle that might occur around it;
- if the route becomes dangerous, `reach and inspect the site` remains the premise while combat, detour, waiting, negotiation or withdrawal are possible methods;
- viability should be evaluated before a tactical handoff so a blocked world-level plan does not instantiate an AutoPTU battle merely because the original commitment existed;
- if a tactical scene later occurs, objective-state support and specialized AI verbs must be declared explicitly instead of using defeat-all as a substitute.

Excluded material:
- the thread's specific antagonist group, mine, party composition and encounter numbers;
- its exact tactics or character builds;
- any claim that one community encounter demonstrates PTU engine implementation coverage.

## PTU / Caelo cross-check

The project PTU/Kairos source index remains a routing aid rather than automatic mechanical authority. This pass adds no PTU rule, Trainer Feature, move, item, ability or combat resolution.

The new runtime owner operates entirely before a negotiated commitment begins. It records evidence-backed viability and schedules ordinary world-agent replanning. It cannot move an actor, reserve a route, grant access, allocate resources or invoke AutoPTU.

Any later encounter must independently declare the exact permanent capability families it consumes. One verified representative mechanic in AutoPTU-Java remains insufficient evidence for a whole family.

## Reusable design lesson

An accepted promise and the present ability to perform it are different durable facts.

For Ouros, a robust causal chain can be:

agreement -> later evidence -> responder observes risk/blocker -> responder replans -> explicit communication or another world action -> possible new agreement or missed obligation -> tactical handoff only if structured mechanics are actually required.

The original agreement remains queryable throughout that chain.

## Canon posture

Nothing in this note is canon-approved world lore. No location, faction, NPC role, quest, route closure or environmental condition is established by this research. The companion proposal is deliberately region-neutral and non-canon.
