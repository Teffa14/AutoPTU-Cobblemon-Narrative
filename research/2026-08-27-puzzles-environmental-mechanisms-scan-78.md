# Puzzles, Environmental Mechanisms & Persistent State Research — Pass 78

Status: research/provenance only. Nothing in this file is automatically Ouros canon.

Date: 2026-08-27

## Research question

How can Ouros make puzzles, switches, machinery, environmental mechanisms and multi-room logic feel like parts of a persistent place rather than disposable minigames, while keeping clues readable, supporting recovery from mistakes, allowing multiple approaches and never asking Minecraft/Cobblemon to invent PTU battle rules?

This pass deliberately does not establish new PTU Skills, DCs, Pokémon capabilities, field-move rules, damage from puzzle mistakes, Trainer Feature effects, tactical terrain rules, forced movement, reaction timing or objective mechanics. Those remain governed by PTU/Caelo and live AutoPTU evidence.

## Internal repository review before research

The complete repository tree was inspected before authoring. The closest existing systems are:

- `design/mission-dungeon-grammar.md`, which already defines a minimal puzzle contract, reset semantics, hints, alternate solutions and anti-softlock rules;
- `design/cartography-survey-wayfinding-layer.md`, which owns mapped access and navigation observations;
- `design/language-translation-symbolic-systems-layer.md`, which owns interpretation of writing, symbols and translations;
- `design/myth-archaeology-sacred-sites-layer.md`, which owns archaeological observations and historical claims;
- `design/technology-energy-infrastructure-layer.md`, which owns active technical assets and networks;
- `design/facility-maintenance-repair-inspection-extension.md`, which owns repair and condition assessment;
- `design/digital-systems-cyberspace-data-layer.md`, which owns persistent digital-system state;
- `design/anomalous-spaces-dimensional-exploration-layer.md`, which owns unusual spatial phenomena without assuming cosmological truth;
- `design/wreck-sites-salvage-recovery-preservation-extension.md`, which owns persistent abandoned-site state;
- `design/cobblemon-runtime-authority-boundary.md`, which keeps Cobblemon battle-state code outside the authoritative combat stack;
- `design/encounter-implementation-contracts.md`, which requires permanent capability categories and full/reduced forms for mechanically rich encounters.

No dedicated layer currently owns a puzzle's persistent mechanism graph, transition history, clue provenance, visible feedback, reset/bypass behavior and revisit state. Pass 78 fills that narrow gap rather than creating another generic dungeon system.

## Source scan

### 1. Goldenrod Tunnel switch-and-shutter puzzle — Pokémon Gold/Silver/Crystal

Sources:
https://bulbapedia.bulbagarden.net/wiki/Goldenrod_Underground
https://pokemow.com/Gen2/ShutterPuzzle/

Relevant high-level structure:

- three switches can change many shutters at once;
- the final arrangement depends partly on the sequence of earlier inputs, not only the current switch positions;
- different sequences can open the exit or expose optional spaces;
- a separate emergency switch restores a known state;
- the original implementation is difficult to infer because the causal mapping is not legible from room presentation alone.

Reusable Ouros lessons:

- a mechanism may have history-dependent state, so the state record needs more than a final boolean;
- optional outcomes can emerge from different valid sequences rather than one universal answer;
- a diegetic reset is valuable when experimentation can create confusing states;
- complexity must be observable. The player should be able to learn what an input changed without reverse-engineering hidden scripts.

The later HeartGold/SoulSilver redesign is a useful contrast: visual grouping makes the connection between controls and shutters clearer. Ouros should prefer readable causal feedback over obscurity that can only be solved by random trial.

Do not copy the exact three-switch sequence, shutter layout, item placements or Team Rocket scenario.

### 2. Seafoam Islands — environmental state changed by physical intervention

Source:
https://bulbapedia.bulbagarden.net/wiki/Seafoam_Islands

Relevant high-level structure:

- boulders are moved through a multi-floor cave;
- their final positions alter water-current traversal;
- once solved, the boulders remain in place and the changed route persists;
- the puzzle therefore changes the environment rather than merely awarding a key.

Reusable Ouros lesson:

A puzzle output can be a persistent world-state mutation such as rerouted water, opened access, stabilized machinery or a new shortcut. Chronicle state should remember the cause and resulting topology.

Mechanical boundary:

Ouros cannot infer Strength-like legality, current-driven displacement, drowning, damage or underwater combat rules from this example. Any Pokémon-assisted solution needs exact PTU/Caelo capability validation for the individual actor.

### 3. Ruins of Alph — independent modules that aggregate into a larger site change

Source:
https://bulbapedia.bulbagarden.net/wiki/Ruin_of_Alph

Relevant high-level structure:

- four separate puzzle chambers can be completed in any order;
- each completed chamber changes what can appear or be learned in a shared central area;
- extra clues can unlock secondary rooms;
- cumulative completion gradually changes the meaning and content of the larger site.

Reusable Ouros lesson:

A large dungeon puzzle does not need one linear chain. Independent modules can contribute to a site-level aggregate state. This supports exploratory order, revisits and partial completion without resetting earlier work.

Do not copy the Unown imagery, exact hidden-room triggers, species requirements or revealed text.

### 4. Snowpoint Temple — observational sequence puzzles

Sources:
https://bulbapedia.bulbagarden.net/wiki/Snowpoint_Temple
https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Legends:_Arceus/Part_9

Relevant high-level structure:

- Legends: Arceus asks the player to inspect statue orientation and symbols in the environment;
- later doors extend the same learned grammar rather than changing to an unrelated trick;
- the answer is recoverable from spatial observation inside the site.

Reusable Ouros lesson:

A puzzle can teach a local visual language, then ask the player to apply it at greater complexity. Clues should be present in the authored space and recorded as observations if the world-state system needs to remember what an actor has actually seen.

Do not copy the Regi symbols, statue sequence or temple geography.

### 5. PTU community puzzle in old ruins

Source:
https://www.reddit.com/r/PokemonTabletop/comments/1e3huvj/

Classification: community inspiration only; never a mechanical rules source.

Relevant high-level structure:

- a GM placed a puzzle in old ruins using visible pillars, Pokémon carvings, Unown letters and environmental imagery;
- the room description itself contained the evidence needed to reason through the puzzle;
- Pokémon-world knowledge was part of the theme rather than an invisible GM-only solution.

Reusable Ouros lesson:

Tabletop puzzles benefit from inspectable evidence and multiple observation surfaces. If knowledge about a Pokémon matters, Ouros should use information the character can plausibly know or discover, not force the player to use external franchise trivia.

### 6. Cobblemon community feedback — solved state without perceptible confirmation

Source:
https://www.reddit.com/r/cobblemon/comments/1lc6xmf/solving_the_snowpoint_temple/

Classification: community implementation feedback.

Relevant high-level observation:

Players reported entering the correct solution but failing to notice that a side wall had opened. They expected a more obvious visual or sound cue and continued manipulating the controls because the successful transition was not perceptible enough.

Reusable Ouros lesson:

Every important mechanism transition needs a feedback contract. Accepted input, rejected input and completed state should each produce discoverable confirmation appropriate to the fiction. If the changed object is outside the player's camera, the site should expose an audible, visual, textual or environmental cue that directs attention without simply displaying the answer.

This is particularly important for Minecraft/Cobblemon, where block changes can occur outside the immediate view.

### 7. Pokémon Reborn — Voclain Estate observational comparison

Source:
https://pokemon-reborn.fandom.com/wiki/Voclain_Estate

Classification: fan-game inspiration only.

Relevant high-level structure:

- the player compares near-symmetric room arrangements;
- progression depends on identifying the meaningful anomaly;
- the puzzle asks for observation of authored scenery rather than a hidden random combination.

Reusable Ouros lesson:

Environmental comparison can make ordinary props mechanically meaningful as clues. However, Ouros should not copy the source's punishment where a wrong choice directly damages the entire Pokémon team. Puzzle failure cannot mutate authoritative HP or statuses unless an exact PTU/Caelo rule and AutoPTU runtime path support that consequence.

### 8. Pokémon Reborn — Yureyu Power Plant remote controls

Source:
https://pokemon-reborn.fandom.com/wiki/Yureyu_Power_Plant

Classification: fan-game inspiration only.

Relevant high-level structure:

- controls distributed across side rooms affect gates on a central route;
- the puzzle establishes a causal connection between remote mechanisms and access topology;
- solving side spaces changes later navigation through the same facility.

Reusable Ouros lesson:

Mechanisms may affect distant zones. The state model therefore needs explicit output references and feedback so a player can verify what changed elsewhere.

### 9. Pokémon Reborn — Blacksteam Factory multi-actor interaction chain

Source:
https://pokemon-reborn.fandom.com/wiki/Blacksteam_Factory

Classification: fan-game inspiration only.

Relevant high-level structure:

- the puzzle chains several different actor interactions toward one environmental objective;
- no single interaction solves the whole problem;
- actor placement and sequence matter.

Reusable Ouros lesson:

A puzzle can be a dependency graph of several actions instead of a code entry. For Ouros, any Pokémon-dependent action must be validated against the exact individual's authoritative capabilities, Moves, Abilities or other governing state. Species/theme alone never grants a puzzle power.

Do not copy the species chain, prison scenario or exact interaction sequence.

## Cross-source design findings

### Readable causality matters more than obscurity

The strongest contrast is Goldenrod GSC versus later clearer presentations. Complexity can be deep while each local interaction remains understandable. A difficult puzzle should challenge inference, planning or tradeoffs rather than hide whether an input did anything.

### Puzzle state belongs to the place

Seafoam and Ruins of Alph both treat puzzle results as location changes. Ouros should persist mechanism state in the site rather than reconstructing the same untouched challenge on every visit.

### Partial completion is valid

Independent modules can remain solved while other modules are untouched. This supports exploration across several visits and allows other world systems to react to partial access.

### A bypass should create state, not erase design

A legitimate bypass can become a new Chronicle fact: a damaged lock, a repaired conduit, a temporary bridge, a capability-assisted route or an institutional override. It should have its own provenance and consequences.

### Feedback is an implementation contract

Minecraft is a spatial presentation layer where a correct transition may happen off-screen. The mechanism layer should require explicit feedback events instead of assuming the player notices block changes.

## PTU/Caelo boundary

Pass 78 treats puzzle reasoning and world interaction as narrative/world-state design unless an action invokes a governed mechanic.

Before a puzzle uses a Pokémon's capability, Move, Ability, item, Skill, Edge, Trainer Feature or movement mode as a required solution, the exact rule must be checked against the project's PTU/Caelo source set and the current authoritative state of that actor.

Do not infer:

- Fire type = can heat any mechanism;
- Electric type = can power any device;
- Psychic type = can move arbitrary machinery;
- Water type = can redirect or survive any current;
- large Pokémon = can push any object;
- Ghost type = can bypass walls;
- a Move name = unrestricted overworld utility.

If a source-supported capability exists, it can become one solution path. The system should still preserve the distinction between overworld world-state consequences and tactical battle effects.

## Cobblemon authority boundary

Pass 78 follows `design/cobblemon-runtime-authority-boundary.md`.

Safe or desirable Cobblemon/Minecraft reuse for puzzles can include:

- blocks and structure variants;
- doors, trapdoors, pistons or other visual machinery where appropriate;
- particles, sounds and animation;
- Pokémon overworld entities;
- interaction hooks;
- UI prompts;
- networking and synchronization;
- world coordinates and block geometry as observations;
- persistent props and visual state;
- client-side presentation of mechanism transitions.

Ouros owns the semantic puzzle state and authoritative world transition. Minecraft block state may mirror that record, but a client-side block change cannot silently establish canonical completion.

If the mechanism directly changes tactical combat state, the handoff must go through AutoPTU. Cobblemon battle-state code remains excluded.

## Live engine evidence inspected

### AutoPTU-Java

Current inspected `main` head:

`a2a2b7fc040bacd0242de615b774d63890952225`

Latest change:

`Freeze held-item START slot ordering (#239)`

This strengthens the deterministic held-item START lifecycle/item slice with parity-backed ordering. It does not establish a full Item family and does not change the readiness of movement, terrain, hazards, reactions, AI policy or adapter playback.

The current Java README still lists as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- semantic battle-event emission and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### AutoPTU Python

Current inspected `main` head:

`11c4aea350193d2ed0940ec5a8ada09e44b6d291`

Latest work trains the full active squad each Career season. It is progression/Career behavior and does not establish a new tactical capability family for Pass 78.

## Originality guardrails

Pass 78 may reuse high-level structures such as observable cause/effect, multi-module accumulation, persistent environmental change, remote-control topology, diegetic resets and capability-aware alternate approaches.

Do not copy:

- exact puzzle answers;
- distinctive maps;
- named ruins or factions;
- exact species combinations;
- dialogue;
- proprietary riddles;
- source-specific rewards;
- punishment mechanics;
- legendary gating structures.

Original Ouros candidates derived from these lessons belong in `proposals/`, remain NON-CANON and require continuity review before promotion.
