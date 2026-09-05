# Pass 287 Research — Delivery-to-Replanning Coordination

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon effect: none by itself.

## Research question

How can a persistent NPC world turn delivered information into selective, state-grounded behavior changes without global polling, duplicate reactions, tactical-authority leakage or region-specific scripts?

## Existing Ouros material checked first

The full repository tree was inspected before writing. Relevant executable and design layers reviewed included Passes 279–286, `CURRENT_FOCUS.md`, source-authority policy, communication queues, event-triggered replanning, audience resolution, runtime tests and current engine-readiness evidence.

The current architecture already had both ends of the seam:
- Pass 283/286 can deliver a claim to one explicit receiver;
- Pass 284 can turn a successful delivery into a `KNOWLEDGE_DELIVERED` wake-up and re-evaluate one agent.

Pass 287 therefore composes those existing responsibilities instead of inventing a second memory system or second planner.

## New public sources reviewed

### WorldMind — Decoupled Game World Model for State-Aware NPC Behavior
Source: https://arxiv.org/abs/2608.21439
Date: 2026-08-18

Reusable structure:
- separate state understanding, decision, control and visual generation;
- ground decisions in explicit evolving state rather than coupling reasoning directly to rendering.

Ouros transformation:
- information delivery updates explicit private state;
- world-agent planning consumes that state;
- execution remains a later owner-specific concern;
- Minecraft/Cobblemon presentation does not become the decision authority.

No dataset, model architecture, generated behavior or implementation code is adopted.

### Yang, Ren & Zhang — BDI Agent-Based Task Scheduling Framework
Source: https://arxiv.org/abs/2401.02223

Reusable structure:
- belief updates and uncertain external events can trigger rescheduling in distributed agents;
- asynchronous notification avoids requiring continuous centralized reevaluation.

Ouros transformation:
- successful delivery of a claim can create one semantic wake-up for the receiving NPC;
- failure or non-delivery creates no belief-driven wake-up;
- the affected agent reconsiders its agenda using existing Ouros goals, needs, commitments and situational intents.

The cloud-scheduling algorithms, recommendation mechanism and performance claims are not adopted.

### Pokémon Unbound mission system documentation
Source: https://www.pokemonunboundpokedex.com/wiki/missions/

Reusable high-level structure:
- mission state and progression are tracked persistently through a mission log;
- availability and later consequences can depend on prior progress rather than only immediate proximity to an NPC.

Ouros transformation:
- world consequences should be derived from durable semantic state and delivered events;
- presentation to the player is downstream from persistent state;
- an NPC receiving news can alter a quest/world situation without the player standing next to that NPC.

No mission names, plots, locations, rewards or unlock counts are imported into Ouros.

### Pokémon Tabletop community — campaign log #25
Source: https://www.reddit.com/r/PokemonTabletop/comments/xtwhxv

Reusable design lesson:
- a campaign can lose momentum when a long encounter is repeated or mechanically overextended;
- the GM in the reported campaign chose to resolve a repeated fight off-screen rather than replay it when that no longer served the table.

Ouros transformation:
- narrative consequences triggered by delivered information should have a reduced world-state version when tactical detail is unnecessary or unsupported;
- a warning can change travel, availability or quest state without forcing a battle;
- a full structured encounter is reserved for cases where the mechanics and player-facing experience justify it.

No campaign characters, homebrew material, encounter content or prose is copied.

## PTU / Caelo / Kairos cross-check

No PTU combat rule is needed for semantic delivery-to-replanning coordination.

No Caelo-specific rule was located in the current narrative repository as an adopted authority for this seam. Existing project policy therefore remains controlling: Caelo can provide living-world structures, but no rule activates without explicit Ouros adoption.

No Kairos rule is adopted. `SOURCE_HAS_RULE != OUROS_USES_RULE` remains binding.

A delivered report is not a PTU Action, initiative event, Trainer Feature, reaction or tactical interrupt. If the resulting world intent later requests structured mechanics, AutoPTU becomes the adjudication owner through the existing handoff.

## Design lessons carried forward

1. Delivery and reaction need an explicit seam: a message becoming knowledge must be distinguishable from a message merely being queued.
2. Only the affected agent should wake because of a private delivery.
3. Failed, deferred or local-ACK-pending messages cannot alter private knowledge or agenda eligibility.
4. Duplicate delivery materialization cannot produce repeated behavior changes.
5. State, planning and visual execution remain separate ownership layers.
6. Narrative concepts should retain a world-state-only form when tactical resolution adds no value or depends on incomplete engine families.

## Rejected shortcuts

- polling every NPC after each communication cycle;
- waking all members of the receiver's faction;
- treating a queued message as already known;
- letting a Minecraft animation or proximity event create the belief before accepted delivery;
- rerunning the tactical planner from the narrative scheduler;
- turning a representative AutoPTU lifecycle hook into evidence that the complete capability family exists;
- importing Pokémon Unbound mission content or PTU campaign-specific characters into Ouros canon.
