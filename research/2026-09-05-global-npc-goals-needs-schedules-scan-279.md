# Pass 279 research — global NPC goals, needs and schedules

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon effect: NONE by itself

## Question

How should persistent Ouros NPCs choose believable world-level activity across long-term goals, immediate needs, scheduled commitments and unexpected events without hard-coding one region, granting omniscience or duplicating AutoPTU tactical AI?

## Existing Ouros constraints inspected

- `CURRENT_FOCUS.md` now makes global NPC/world-agent AI the primary implementation focus.
- `design/global-npc-world-agent-ai-contract.md` requires one region-neutral planner, non-omniscient knowledge, off-screen named NPC persistence and explicit `REQUEST_AUTOPTU` handoff.
- `design/ouros-source-authority-and-species-policy.md` keeps Minecraft as presentation/realtime interaction while PTU/AutoPTU owns mechanical adjudication.
- `canon/npc-pokemon-dynamic-progression-v1.md` already distinguishes persistent NPC Pokémon identity from generated battle state. This pass does not alter that policy.
- Existing `tools/global_npc_ai.py` already supplies deterministic utility scoring, knowledge/permission gates and AutoPTU binding. It lacked durable agenda state.
- Repository search found no separate general-purpose schedule/goals implementation that should be reused instead.

## Sources and reusable lessons

### Park et al., “Generative Agents: Interactive Simulacra of Human Behavior” (UIST 2023)

Source: https://arxiv.org/abs/2304.03442

Reusable structure: observation, memory, reflection and planning can produce coherent daily behavior and social coordination over time. The useful Ouros lesson is architectural separation: planning should consume remembered/available information rather than raw hidden simulation truth. Natural-language generation is not adopted as world authority.

### Game AI Pro series

Source: https://www.gameaipro.com/

The public chapter index includes behavior selection, utility-based considerations, modular AI, knowledge representation and efficient event-based simulation. The reusable pattern is to rank several valid behaviors from multiple considerations instead of scripting one fixed routine. Ouros keeps scoring deterministic and versioned. The scoring weights are Ouros policy, not PTU mechanics.

### GDC 2012 report on The Sims ambient AI

Source: https://www.gamedeveloper.com/programming/gdc-2012-i-sims-i-team-s-graham-says-ambient-ai-tells-better-stories

Reusable lesson: agents with individual agendas and simple utility selection can make a location feel inhabited without relying on looping ambient animations. Schedules are useful, but they should interact with motives and events rather than force every actor through an immutable script.

### Humanoid Agents (2023)

Source: https://arxiv.org/abs/2310.05418

Reusable structure: basic needs, relationship closeness and dynamic state can alter daily activities. Ouros only adopts the broad concept that changing internal pressures can influence agenda selection. It does not import their LLM implementation or assume their behavior model is a simulation of real people.

### Pokémon Reborn public encounter documentation

Sources:
- https://pokemon-reborn.fandom.com/wiki/Obsidia_Alleyway
- https://pokemon-reborn.fandom.com/wiki/Lower_Peridot_Alley
- https://pokemon-reborn.fandom.com/wiki/Static_Encounters

Reusable pattern: time, weather and progression can change who or what is present and which small stories are available. Ouros should generalize this from scripted spawn/event gates into persistent agents whose availability follows semantic schedules and world knowledge. No Reborn character, encounter, dialogue, reward or plot is copied.

### PTU community NPC-preparation discussions

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/ndootg
- https://www.reddit.com/r/PokemonTabletop/comments/ctjl56

Reusable lesson: recurring rivals and other important NPCs justify richer persistent state, while most incidental characters do not need full PTU character construction. This supports Ouros execution tiers: named world agents can persist; crowds/background actors can remain aggregate until promoted. Community advice is not a PTU rule.

## Design synthesis

The smallest useful global agenda layer needs four independent inputs:

1. durable goals that remain until complete, invalidated or explicitly abandoned;
2. needs that become candidate actions only after a declared pressure threshold;
3. scheduled commitments evaluated against Ouros semantic time;
4. situational intents produced by observations, communications and other legitimate world events.

An active intent can receive a small continuity bonus so tiny score changes do not cause oscillation every evaluation. Strong new evidence, hard commitments or critical needs must still be able to interrupt it.

A missed commitment must create a consequence/follow-up state. The planner must never repair lateness by teleporting the NPC or backdating world state.

## Authority boundaries

Goals, need pressure, schedule policy and utility weights are Ouros MMO/world-simulation policy. They are not PTU Actions, Features, Status Afflictions or trainer rules.

When a chosen world intent requires structured combat/training/chase mechanics, the global planner may request AutoPTU. It may not choose tactical squares, Moves, targets, reactions, damage or status outcomes.

Minecraft/Cobblemon may project local activity and navigation. Chunk loading, entity presence and wall-clock ticks do not become authoritative schedule time by themselves.

## Canon status

All fixture people, regions, commitments, messages and needs in Pass 279 are `FIXTURE_ONLY`.

No source above becomes Ouros canon automatically. No Caelo/Kairos/PTU mechanic is adopted by this research note.
