# Research Scan — Pokémon Cognition, Problem Solving, and Tool Use — Pass 133

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-08-23

## Scope and duplication check

This pass follows the full repository inventory through Pass 132.

The closest existing layer is `design/pokemon-social-learning-behavioral-traditions-layer.md` from Pass 125. That layer explicitly focuses on transmission between Pokémon and does not attempt a general theory of cognition. This pass therefore stays on the individual side of the boundary: how one persistent Pokémon encounters a problem, manipulates objects, tries strategies, changes approach, succeeds or fails, and potentially invents a behavior before any evidence exists that another Pokémon learned it.

This pass also avoids duplicating:

- Material Culture, which owns persistent physical objects and provenance;
- Pokémon Agency, which owns the persistent Pokémon individual and partnership/custody state;
- Social Learning, which owns evidence that behavior spreads between individuals;
- Research Ethics, which owns authorization and subject-protection constraints for studies;
- Science, which owns hypotheses, protocols, datasets, uncertainty, and publication;
- AI tactical policy, which remains an engine implementation concern rather than world lore.

No material in this scan is promoted to canon.

## PTU project-source check

The project copy of the PTU 1.05 changelog contains a particularly important constraint: the old `Intelligence Capability` was removed in PTU 1.05.

Project source:
https://github.com/Teffa14/AutoPTU/blob/main/files/rulebook/PTU%201.05/PTU%20changelog%201.05.txt

Design consequence:

Ouros must not recreate a universal numeric Intelligence stat as an unofficial replacement. A Pokémon solving a latch, manufacturing an object, remembering a route, issuing commands, or changing strategy is evidence about that observed behavior in context. It is not permission to assign a global IQ-like score, infer every other cognitive ability, or grant battle bonuses.

The project corpus also contains many imported AI files whose filenames use the word `Intelligence`. Those are battle-AI implementation terminology, not a PTU Pokémon Capability and not a narrative cognition model.

No reliable Caelo rule text specific to cognition/tool use was recovered in an invocable form during this run. Super PTU Online Helper was not exposed as a callable capability. No Caelo or Helper output is invented here.

## Source 1 — Tinkatink: repeated manufacture and revision of an external object

Official Pokémon Pokédex:
https://www.pokemon.com/uk/pokedex/tinkatink

The official entry describes Tinkatink pounding iron scraps together to make a hammer and remaking it repeatedly until satisfied with the result.

Reusable structure:

- object manufacture can be iterative rather than a one-time species animation;
- the same persistent Pokémon can have a history of successive tool versions;
- discarded components, repair attempts, theft, replacement, and preferred materials can create Material Culture provenance;
- an observed successful product does not reveal the entire cognitive process that produced it.

Ouros transformation:

A Pokémon may maintain an `object-use repertoire` or a sequence of attempts around one problem without receiving a generic crafting score. When a tool is physically persistent, Material Culture owns the tool identity and provenance while this cognition layer owns the observed problem-solving behavior around it.

Mechanical guardrail:

The official Pokédex behavior does not prove a PTU crafting action, Technology Education rank, weapon proficiency, item slot, Move, damage value, or universal ability to fabricate arbitrary tools.

## Source 2 — Tinkatuff/Tinkaton: object use embedded in ecology

Official Pokémon Pokédex:
https://www.pokemon.com/uk/pokedex/tinkatuff
https://www.pokemon.com/us/pokedex/tinkaton

Tinkatuff is associated with scrap-metal homes, comparison of hammer strength, and gathering metal to create a larger hammer. Tinkaton uses a very large hammer and can launch rocks with it.

Reusable structure:

Tool use can have ecological dependencies. Material availability, competition, scavenging, storage sites, damage to a tool, and changes in the surrounding built environment can alter how the same behavior is expressed.

Ouros transformation:

Do not store `tool_user=true` as a complete explanation. Store the object, task, material context, observed actions, outcome, and confidence separately. If another Pokémon later copies the behavior, hand that evidence to the Social Learning layer rather than retroactively declaring the original behavior culturally transmitted.

Mechanical guardrail:

Tinkaton flavor cannot create arbitrary projectile attacks, improvised knockback, object damage, crafting yield, inventory capacity, or Corviknight-targeting AI outside verified PTU mechanics.

## Source 3 — Oranguru: apparent complex coordination without a universal intelligence score

Official Pokémon Pokédex:
https://www.pokemon.com/us/pokedex/oranguru

The current Pokédex describes Oranguru issuing repeated commands to other forest Pokémon strongly enough that people once mistook it for a human.

Reusable structure:

- observers can disagree about what a sophisticated behavior means;
- coordination, communication, planning, leadership, imitation, and direct command are different hypotheses;
- a behavior that looks humanlike does not justify assuming human institutions, language, morality, or knowledge.

Ouros transformation:

An observer may record `issued repeated directional signals before group movement` while interpretations remain separate: leadership, learned routine, species-typical display, mutual coordination, or another cause.

Mechanical guardrail:

This does not grant Command Skill ranks, Trainer Orders, telepathy, shared initiative, Pack Mon, tactical omniscience, or authority over unrelated Pokémon.

## Source 4 — Public PTU campaign logs: puzzles can be world structure without becoming a universal subsystem

Public campaign log #4:
https://www.reddit.com/r/PokemonTabletop/comments/mkks6b

Public campaign log #13:
https://www.reddit.com/r/PokemonTabletop/comments/nwtoj5

These logs include Gym/haunted-mansion riddles, route gating, room-by-room exploration, environmental clues, battles, captures, and player-directed problem solving.

Reusable structure:

- a puzzle can alter pacing between battles;
- clues, rooms, NPC/Pokémon behavior, and physical access can carry the challenge;
- a location can preserve partial progress and evidence independently of combat;
- not every obstacle needs a new combat rule.

Ouros transformation:

For Pokémon-centered cognition, the lesson is to avoid replacing a world puzzle with a single opaque `Intelligence check`. Observe actual interactions. If a Pokémon tries three different objects, abandons a failed approach, returns later, or discovers a novel route, Chronicle records those events. The player can investigate what happened without the world assigning a hidden universal score.

The distinctive riddles and mansion sequence are not copied.

## Source 5 — Comparative cognition: specific abilities are safer than a general-intelligence label

Review: Neural Processes Underlying Tool Use in Humans, Macaques, and Corvids
https://pmc.ncbi.nlm.nih.gov/articles/PMC7561402/

The review distinguishes specific tool-use abilities and notes the value of studying concrete intellectual abilities rather than treating a single broad intelligence construct as sufficient explanation.

Reusable structure:

Track task-specific evidence:

- object selection;
- object orientation;
- manipulation sequence;
- persistence;
- switching after failure;
- transfer to a changed version of the task;
- manufacture or modification;
- latency and number of attempts;
- environmental affordances.

Do not convert these into an omnibus intelligence stat.

## Source 6 — Individual learning and spontaneous tool-use forms

Review: Exploring the role of individual learning in animal tool-use
https://pmc.ncbi.nlm.nih.gov/articles/PMC7521350/

This review collects cases where tool-use forms emerged in naïve individuals and emphasizes that social exposure is not always necessary for a behavior to appear. It also highlights object manipulation, problem solving, working memory, motivation, attention, and information seeking as separable contributors.

Reusable structure:

When Ouros observes a novel behavior, preserve alternative explanations:

- individual innovation;
- repeated trial and error;
- prior unobserved experience;
- socially mediated opportunity without copying;
- copied behavior;
- species-typical behavior expressed in a new context.

The correct handoff to Pass 125 happens only when evidence of transmission exists.

## Source 7 — Behavioral flexibility and multi-access problems

Review: Can Cognitive Ability Give Invasive Species the Means to Succeed?
https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2020.00187/full

The review discusses behavioral flexibility, innovation, problem solving, and tasks in which previously successful access methods are blocked, forcing a subject to switch strategies.

Reusable structure:

A high-value longitudinal Ouros observation is not simply `solved puzzle`. It can be:

1. method A works;
2. environment changes and A stops working;
3. the same individual persists with A, abandons it, or discovers B;
4. later observations test whether B is retained or generalized;
5. if another Pokémon acquires B after exposure, Social Learning receives a new transmission hypothesis.

## Source 8 — Tool use depends on morphology and ecology, not cognition alone

Royal Society theme introduction: Tool use as adaptation
https://pmc.ncbi.nlm.nih.gov/articles/PMC4027410/

The review emphasizes morphology, development, ecological opportunity, life history, and learning as interacting constraints on tool-use behavior.

Reusable structure:

Failure to use an object does not prove failure to understand the task. The object may be too heavy, poorly shaped, inaccessible, unfamiliar, risky, or physically incompatible with the Pokémon's body plan. Conversely, easy success can result from a well-matched affordance rather than broad reasoning ability.

This is especially important in a Pokémon setting where body plans and Capabilities vary dramatically.

## High-level Ouros design lessons

1. Observe behavior before naming cognition.
2. Preserve attempts and strategy changes, not only success/failure.
3. Keep object provenance separate from the cognitive event.
4. Keep individual innovation separate from social transmission.
5. Keep task performance separate from species-wide lore.
6. Never infer a general Intelligence score; PTU 1.05 explicitly removed that Capability.
7. Preserve uncertainty about prior experience.
8. Treat morphology and environmental affordances as possible explanations.
9. Allow persistent individuals to build longitudinal behavioral histories.
10. Let a study conclude that a supposed clever solution was accidental, species-typical, or impossible to distinguish from prior training.
11. Do not convert Minecraft block interaction into PTU rules automatically.
12. Do not make every interesting behavior a quest. Chronicle can simply record it.

## Mechanics boundary

No source in this scan establishes a generic PTU rule for:

- puzzle-solving checks;
- universal Pokémon Intelligence ranks;
- arbitrary tool manufacture;
- arbitrary object interaction in combat;
- doors/locks solved by species flavor;
- carrying capacity from observed tool use;
- improvised weapon stats;
- object-based forced movement;
- AI planning outside implemented policy;
- social learning bonuses;
- crafting yield;
- automatic command authority.

Any mechanically rich battle version must use the permanent engine capability map and remain behind the exact families it needs.

## Provenance policy

Research links remain here, outside canon. The design layer derived from this scan is proposed architecture. The proposal file is NON-CANON. No protected plot, dialogue, riddle, character, or distinctive scenario is copied wholesale.