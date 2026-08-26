# Executable Puzzle & Mechanism Runtime Research Scan — Pass 184

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-08-26

## Scope

This pass continues the implementation pivot established by Pass 183. It does not add another puzzle authority. `design/puzzles-dungeons-challenge-state-layer.md` remains authoritative for challenge definitions, mechanism state, clues, solution routes, reset semantics, fail-forward and battle handoffs. `design/ouros-runtime-scene-world-execution-contract.md` remains authoritative for executable scene state, triggers, interaction ordering, idempotent effects, recovery and AutoPTU handoff.

The gap addressed here is narrower: how a persistent puzzle mechanism should behave when represented by Minecraft blocks and interactions, including multiplayer races, server restart, stale client state, presentation failure and optional battle transitions.

The full repository tree was inspected before writing. Existing implementation content contains the Cedar Meadow scene slice, but no second vertical slice that exercises persistent block/mechanism state.

## Official Pokémon precedent: Nessa's Gym challenge

The official Pokémon Sword and Shield E3 demo description presents a water-themed Gym where colored switches turn waterfall flows on or off. The physical route changes according to switch order, and battles occur along the route before the final Gym Leader battle.

Source:
- The Pokémon Company International, `We Battle Nessa and Her Dynamax Pokémon in the Pokémon Sword and Pokémon Shield Demo at E3`, 2019.
- https://www.pokemon.com/us/news/we-battle-nessa-and-her-dynamax-pokemon-in-the-pokemon-sword-and-pokemon-shield-demo-at-e3

Reusable structure:

`visible mechanism -> player interaction -> persistent route-state change -> newly legal path -> possible battle -> continuation`

Ouros adaptation:

The mechanism has server-owned logical state. Minecraft waterfalls, doors, lamps or blocks are projections of that state. A block update cannot independently mark a challenge solved.

## PTU community precedent: campaign world responds to timed events and interaction

A public PTU campaign recruitment post describes a prebuilt region whose story is shaped by player interaction and timed events. The useful lesson is not any specific plot; it is that authored world state and scheduled events can coexist with player-driven consequences.

Source:
- Reddit, r/PokemonTabletop, `PTU Game Looking for a Player!`, 2020.
- https://www.reddit.com/r/PokemonTabletop/comments/fp5xyn/

Ouros adaptation:

A challenge instance can be persistent and shared without becoming a fixed cutscene. Players change legal mechanism state through explicit interactions, while scheduled or world-state changes may alter availability later.

## Fan-game anti-pattern: puzzle complexity can exceed player-visible state

Pokémon Reborn community discussions around Victory Road repeatedly describe needing guides, losing track of goals, long repeated sequences and frustration with state-heavy puzzle chains. Other players enjoy the difficulty, so the lesson is not `hard puzzle bad`; the useful design boundary is that challenge state must remain legible and recoverable.

Sources:
- Reddit, r/PokemonReborn, `How to make it through Victory Road a second time`, 2024.
- https://www.reddit.com/r/PokemonReborn/comments/1bunryz/
- Reddit, r/PokemonReborn, `Not-Really Spoiler Victory Road Puzzle Help`, 2022.
- https://www.reddit.com/r/PokemonReborn/comments/u5hhhc/
- Reddit, r/PokemonReborn, `Victory Road`, 2025.
- https://www.reddit.com/r/PokemonReborn/comments/1hwlmwd/

Ouros adaptation:

Every critical mechanism should expose enough in-world state for a returning player to reconstruct the current situation. Persistent clue history, readable mechanism state, explicit reset semantics and shortcuts after solved sections reduce dependence on external guides.

## Server authority and persistence

Minecraft presentation can desynchronize from authoritative state because of chunk unload, reconnect, server restart, delayed packets, external block edits or concurrent interaction.

Required architecture:

`interaction intent -> server validates observed revision -> mechanism transition commits -> persistent state revision advances -> presentation command emitted -> adapter acknowledges`

If presentation fails after the commit, recovery re-renders the committed mechanism state. It does not rerun the interaction.

## Multiplayer race condition

Two players can activate different controls from the same observed state.

Required rule:

- each request carries the mechanism/scene revision observed by the player;
- only a request legal against the current revision can commit;
- a stale request is rejected or explicitly rebased by authored policy;
- client last-writer-wins is prohibited;
- every accepted transition has a stable operation ID.

This is necessary before challenges become shared server content.

## Redstone and block-state boundary

Redstone can be useful presentation plumbing, but it cannot be the authority for Ouros challenge truth.

Forbidden direction:

`lever block is powered -> therefore challenge state changed`

Required direction:

`server accepts ACTIVATE(control A) -> challenge state revision changes -> adapter sets lever/door/water presentation`

This prevents griefing, rollback, WorldEdit, piston side effects, chunk reconstruction or client desync from silently rewriting Chronicle.

## Restart recovery

A safe persistent mechanism must recover from these crash windows:

1. request received before validation;
2. transition validated before authoritative commit;
3. authoritative commit completed before block presentation;
4. presentation applied before acknowledgement;
5. optional battle request created before battle session acknowledgement;
6. battle result committed before aftermath presentation.

The authoritative state determines recovery. Visual effects are replayable; world-state commits and rewards are not duplicated.

## Puzzle-to-battle boundary

A puzzle may unlock or create a battle opportunity, but the mechanism must freeze into a legal battle configuration before AutoPTU takes authority.

Reduced implementation pattern:

`solve mechanism -> commit stable route/open arena -> freeze mechanism changes -> instantiate static BattleSpec -> AutoPTU resolves -> ingest declared result fields -> unfreeze or advance challenge`

This avoids asking Minecraft to simulate moving floors, currents, crushing walls or forced movement that AutoPTU does not yet support completely.

## PTU/Caelo boundary

No new PTU rule is introduced by this runtime work.

The following remain forbidden unless exact PTU/Caelo evidence and engine support are verified:

- Technology Education automatically solves machinery;
- Focus automatically solves riddles;
- Perception automatically reveals hidden mechanisms;
- Strength, Teleport, Groundshaper or Moves universally bypass challenge state;
- failed interaction creates damage, Status or resource loss;
- puzzle reset restores HP, AP, Frequency or Items;
- mechanism state grants Accuracy, Evasion, Initiative or combat bonuses.

A validated PTU Skill/Capability/Move/Feature may be exposed later as one explicit interaction route with an authoritative rules check.

## Pass 184 implementation target

Implement a reduced version of Pass 173's `Rotating Archive Hall` as a machine-readable vertical slice.

The slice should prove:

- one persistent shared mechanism state;
- three authored controls;
- server-side legal transitions;
- visible clue state separate from mechanism state;
- stale-request rejection;
- idempotent block presentation;
- explicit safe reset;
- restart reconstruction;
- shortcut persistence after completion;
- optional static AutoPTU handoff only after the mechanism is frozen;
- no redstone-derived canon truth.

## Sources newly used this pass

1. The Pokémon Company International — Nessa Gym challenge / colored water switches.
2. Public PTU campaign discussion — persistent world shaped by interaction and timed events.
3. Pokémon Reborn community discussions — high-state puzzle readability, repetition and guide dependence as an anti-pattern signal.
4. Existing Ouros Pass 173 puzzle authority and Pass 183 runtime execution contract.
5. Live read-only AutoPTU-Java status inspected at `b35f09bbcc4246b1846e57c5c4f9bb5771d474e8`.
6. Live read-only AutoPTU status inspected at `7e6ce7c8138273f8d45180d192e84088b9f0986f`.

Nothing in this research file establishes an Ouros ruin, archive, Gym, mechanism, NPC, reward or historical explanation as canon.