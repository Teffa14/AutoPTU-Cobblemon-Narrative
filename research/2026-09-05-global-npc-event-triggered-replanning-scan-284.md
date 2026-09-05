# Pass 284 Research — Event-Triggered Global NPC Replanning

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon effect: none by itself.

## Question

How can Ouros let many persistent NPCs react to meaningful world changes without polling every agent continuously or making one event globally visible?

## New sources

### Menda et al. — Deep Reinforcement Learning for Event-Driven Multi-Agent Decision Processes

Public source: https://arxiv.org/abs/1709.06656

Reusable lesson: asynchronously acting agents fit an event-driven simulator better than an arbitrarily tiny fixed timestep. The paper specifically notes scaling and event-ordering problems with forcing asynchronous processes into smaller and smaller global steps.

Ouros use: semantic events can wake individual world agents when relevant state changes. The learning algorithm and Dec-POMDP formulation are not adopted.

### NPBehave — Event Driven Behavior Trees for Unity

Public source: https://github.com/meniku/NPBehave

Reusable lesson: an AI can remain in its current state and resume evaluation when observed state changes instead of traversing its whole decision graph every frame.

Ouros use: the wake-up queue follows this efficiency principle, but Ouros does not adopt NPBehave's tree API or blackboard implementation.

### Fortino, Garro and Russo — discrete-event validation of agent-based and multi-agent systems

Public abstract: https://iris.unical.it/handle/20.500.11770/160318

Reusable lesson: agent systems can be executed by interleaving explicitly scheduled events, including communication and migration, while retaining deterministic test cases around ordering.

Ouros use: supports treating communication, travel changes and commitments as semantic wake-up sources instead of a universal tick.

### The Guild of the Undaunted — PTU living-world community

Public discussion: https://www.reddit.com/r/PokemonTabletop/comments/1m4xfxk/the_guild_of_the_undaunted_ptu_lw/

Reusable lesson: a PTU living world can be player-driven, faction-rich and persistently changed by participant actions. A global NPC system therefore needs selective consequences that can propagate beyond one authored session.

Ouros use: only the high-level living-world structure is retained. No factions, setting, characters, rules or plots from the community are imported.

## Synthesis for Ouros

The strongest reusable pattern is selective asynchronous activation:

- state changes generate explicit semantic events;
- events name affected agents rather than entire regions;
- several simultaneous causes can be coalesced into one reevaluation while preserving provenance;
- future events remain dormant until their semantic time;
- restart persistence must preserve timing and duplicate protection;
- receiving information can alter eligibility or priority of existing world intents;
- tactical resolution remains outside the event scheduler.

This pattern fits the current Pass 279–283 architecture because it composes existing agenda, social, travel, memory and communication layers instead of replacing them.

## Material intentionally not adopted

- no LLM-generated world truth;
- no reinforcement-learning policy;
- no imported PTU living-world factions or plots;
- no fixed assumption that every event must cause an NPC reaction;
- no claim that an event-driven world-agent wake-up is a PTU Reaction or Interrupt;
- no regional special cases.
