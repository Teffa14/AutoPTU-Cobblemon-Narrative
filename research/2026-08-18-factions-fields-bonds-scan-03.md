# Ouros Narrative Research — Factions, Fields, Bonds & Investigation — Pass 03

Status: Research only. Provenance and design evidence; not Ouros canon.

This pass deliberately extends the existing research instead of repeating mission-board, dungeon-memory, ecology, reputation, or general callback conclusions already documented in passes 01–02. The focus is autonomous factions, changing battle environments, relationship state, long-horizon Pokémon care, non-linear investigation, partial information, multiplayer participation lanes, and encounter objectives beyond simple defeat-all combat.

## 1. PTU public campaign evidence — civic power, modernization, and faction overlap

Source:
https://forums.giantitp.com/showsinglepost.php?p=22586704&postcount=1

The public Heights of Londo PTU campaign presents a region where outside corporations bring medicine, infrastructure, technology and League institutions into a more traditional political order. Local rulers react differently, ranging from acceptance to suspicion. Gym Leaders also function as civic leaders with resources and authority, which gives characters reasons to interact with them even when a specific PC does not care about collecting badges.

Reusable lesson for Ouros:
Faction conflict becomes richer when groups provide real benefits while also creating pressure, dependency, cultural friction or competing interests. A useful faction should have services, constituency, assets and goals in addition to ideology.

Ouros translation:
- factions can overlap with public infrastructure, research, commerce, rescue, security, sport or conservation;
- a Gym or major trainer institution can participate in local governance without every Gym becoming the same type of authority;
- players may cooperate with one part of an organization while opposing another project;
- faction conflict should be capable of producing compromise, uneasy coexistence, reform, splinter groups and temporary alliances;
- the world should record which concrete actions a faction performs in each location rather than storing only a global reputation number.

## 2. Pokémon Conquest — territory graph, local services, autonomous regional turns

Source:
https://bulbapedia.bulbagarden.net/wiki/Pokemon_Conquest

Pokémon Conquest models Ransei as connected kingdoms. Adjacent territory matters, control changes access to local facilities, battles use varying victory conditions, and regional events can occur as time advances. Warriors can also be recruited through battle outcomes under specific conditions.

Reusable lesson for Ouros:
A faction can be represented as an actor operating on a location graph. Influence can change access, patrols, services, jobs, resource pressure and NPC presence without requiring the entire map to become a strategy game.

Ouros translation:
Introduce a lightweight `world_pulse` system. On a pulse, eligible factions may advance one supported objective, react to player actions, lose momentum, split attention, reinforce a location or abandon an effort. The player does not need to witness every action directly; consequences become visible through state changes and rumors.

Important adaptation:
Do not copy Conquest's kingdom-capture loop. Ouros should usually track graded influence or active projects rather than binary ownership.

## 3. Pokémon Reborn — location identity as mutable battle state

Source:
https://pokemon-reborn.fandom.com/wiki/Field_Effects

Pokémon Reborn expands battle environments into a large field system. Some fields come from locations; others can be generated, transformed or terminated during battle. The active environment changes move interactions and can itself become part of tactical planning. Field information can also be discovered and recorded by the player.

Reusable lesson for Ouros:
The environment can be a state machine rather than a static modifier. A battlefield may begin in a location-derived state, gain temporary overlays, transition because of actions, or return to an underlying base state.

Ouros translation:
- separate `base_environment` from temporary `battlefield_state`;
- expose environmental affordances before or during combat through readable cues;
- allow only rules-validated moves, abilities, capabilities, objects or scripted world events to change tactical state;
- preserve location identity after temporary effects end;
- support player knowledge of discovered environment interactions so repeated visits reward learning rather than memorization outside the game.

The exact Reborn field rules must not be imported. They are inspiration for state-machine structure only.

## 4. Pokémon Rejuvenation — layered fields and transition-aware boss design

Sources:
https://rejuvenation.wiki.gg/wiki/Field_Effects
https://rejuvenation.wiki.gg/wiki/Blessed_Field
https://rejuvenation.wiki.gg/wiki/Swamp_Field

Rejuvenation also treats battle fields as location-sensitive, transformable systems and documents transitions between field states. Its field catalog demonstrates how a boss encounter can derive identity from the arena itself rather than from inflated statistics alone.

Reusable lesson for Ouros:
Boss identity can be split across three layers: actor, objective, and arena. Changing the arena can alter tactical priorities without changing the boss's personality or core PTU legality.

Ouros translation:
A boss definition should declare:
- encounter objective;
- arena state and readable hazards;
- legal environment transitions;
- objects or systems that can be interacted with;
- escape or partial-success states;
- what persists after the encounter.

Exact combat modifiers remain a PTU/AutoPTU mechanics task.

## 5. Pokémon Reborn relationship points — relationship state as downstream content selector

Source:
https://pokemon-reborn.fandom.com/wiki/Relationship_Points

Reborn stores hidden relationship values that change through player decisions and can alter later partner availability, scenes, battles or events. Importantly, the value is not presented as a universal objective measurement of affection.

Reusable lesson for Ouros:
Relationship state is most useful when it changes future opportunities and behavior. It should not become a visible morality bar or claim to perfectly describe an NPC's internal feelings.

Ouros translation:
Continue the existing multidimensional relationship model, but add `relationship_effects` that map state to concrete future possibilities such as:
- willingness to share sensitive information;
- accepting or refusing a joint expedition;
- appearing as support in a crisis;
- introducing the player to another contact;
- offering a private job;
- defending or criticizing the player publicly;
- changing negotiation posture;
- becoming a rival, ally, neutral contact or unreliable partner.

## 6. Pokémon Colosseum / XD — long-horizon care as gameplay progression

Sources:
https://bulbapedia.bulbagarden.net/wiki/Shadow_Pok%C3%A9mon
https://bulbapedia.bulbagarden.net/wiki/Purification

Colosseum and XD tie the restoration of Shadow Pokémon to repeated interaction across time: travel, battle participation, calling to the Pokémon, care actions and dedicated facilities all contribute to a longer process. Individual Shadow Pokémon also persist as the same entity when re-encountered.

Reusable lesson for Ouros:
A Pokémon-centered story does not need to resolve in one quest. A named Pokémon can have a persistent personal state that changes through several kinds of interaction and later unlocks narrative consequences.

Ouros translation:
Create a generic `pokemon_bond_arc` structure for rescued, traumatized, distrustful, displaced, injured, unusually intelligent or otherwise story-significant Pokémon. The structure may track narrative facts such as trust milestones, fears, preferred people/places, unresolved needs, witnessed events and adaptation progress.

Guardrail:
Do not import Shadow Pokémon, purification, Heart Gauges, snagging, or their exact fiction unless Ouros later makes a deliberate canon decision. The reusable principle is multi-session care progression with persistent entity identity.

## 7. Heartache campaign — multiple participation lanes in one persistent campaign

Sources:
https://forums.dragonflycave.com/threads/welcome-rules-information.18933/
https://forums.thousandroads.net/

Heartache describes a longform Pokémon Mystery Dungeon group campaign where players can participate in central plot, cooperative tactical battles, player-to-player RP and other creative activities according to interest.

Reusable lesson for Ouros multiplayer:
Not every player needs identical engagement with every system. A shared world can support several participation lanes while preserving common consequences.

Ouros translation:
Possible player-facing lanes include:
- exploration and discovery;
- competitive battling;
- cooperative raids;
- professions and contracts;
- social/relationship play;
- research and Pokédex work;
- contests or performance;
- faction/political involvement;
- dungeon expeditions;
- central authored arcs.

World-state consequences should allow these lanes to intersect without forcing all players into one progression path.

## 8. Non-linear mystery design — redundancy and node navigation

Sources:
https://thealexandrian.net/wordpress/1118/roleplaying-games/three-clue-rule
https://thealexandrian.net/wordpress/7949/roleplaying-games/node-based-scenario-design-part-1-the-plotted-approach
https://thealexandrian.net/wordpress/8176/roleplaying-games/advanced-node-based-design-part-2-node-navigation

The Alexandrian's mystery-design guidance argues against single-clue chokepoints and recommends redundant clues for required conclusions. Its node-based approach treats clues as navigation between places, people or situations instead of forcing one predetermined scene order.

Reusable lesson for Ouros:
Investigation content should be represented as an evidence graph. Important revelations need multiple independently discoverable supports, and players should be able to approach nodes in different orders.

Ouros translation:
Represent:
- canonical facts;
- claims made by characters/factions;
- evidence items or observations;
- source reliability;
- which conclusions evidence supports or weakens;
- node-navigation leads;
- which characters know each fact;
- which clues a player has actually discovered.

The generator must never reveal a conclusion to a player merely because the global world model knows it.

## 9. FIREBALL — transcript alone is weaker than transcript plus structured state

Source:
https://arxiv.org/abs/2305.01528

FIREBALL contains nearly 25,000 Discord tabletop sessions paired with underlying game-state information and reports stronger natural-language generation when models receive structured state in addition to dialogue history.

Reusable lesson for Ouros:
The project's earlier Chronicle/world-graph direction is technically well motivated. Raw RP logs should remain provenance, while generation consumes a compact structured state describing participants, location, goals, conditions, known facts and mechanical state.

Ouros translation:
When Discord narratives are later ingested, extract event state separately from prose. Preserve links back to raw messages, but do not require the narrative generator to reread full transcripts for routine decisions.

## 10. PokeAgent / PokeLLMon — battle memory needs partial-observability guardrails

Sources:
https://arxiv.org/abs/2603.15563
https://arxiv.org/abs/2402.01118

Current Pokémon battle-agent research emphasizes long-context reasoning, feedback from prior battles, external knowledge retrieval and partial observability. These are useful AI architecture references even though they do not define PTU legality.

Reusable lesson for Ouros:
A recurring rival can learn from what it plausibly observed, but should not gain perfect access to the player's hidden team state, future moves or private Chronicle information.

Ouros translation:
Separate:
- `world_truth`;
- `npc_known_facts`;
- `npc_inferences`;
- `battle_observations`;
- `rumors_received`;
- `player_private_state`.

AI opponent planning may use only information available to that actor plus globally public rules knowledge.

## New design conclusions from this pass

1. Factions need autonomous action and local projects, not only reputation values.
2. Territory should normally be graded influence, with services and presence changing before hard control changes.
3. Encounters can have victory conditions other than reducing every opponent to zero HP.
4. Battle arenas can be state machines, but transitions must be legal under PTU/AutoPTU.
5. Relationship state should unlock behavior and content rather than claim to measure morality.
6. Story-significant Pokémon need persistent entity memory and can support multi-session care arcs.
7. Multiplayer can support several participation lanes inside one shared world.
8. Mysteries need evidence redundancy and player-specific knowledge state.
9. Transcript ingestion should produce structured state with provenance.
10. Rival AI must respect partial observability and actor knowledge boundaries.

## PTU / Caelo boundary

The supplied project material remains authoritative for mechanics. The PTU Core Rulebook supports central, character-focused and sandbox campaign play and emphasizes meaningful player choices. Caelo separates Social, Encounter, PvP, Job, Raid, Contest, Gym and Dojo activities and uses locations whose environmental conditions can affect combat. The supplied Pokédex/errata material defines actual capabilities, Moves, Abilities and terrain interactions.

Therefore this pass proposes orchestration and state architecture only. No external fangame field multiplier, relationship threshold, Conquest victory rule, Shadow Pokémon mechanic, or AI battle rule is automatically valid in Ouros.

## Copyright and provenance guardrail

No external dialogue, prose, named original characters, distinctive scenes or complete plots are imported. Sources are retained to explain the structural lesson. Ouros proposals derived from those lessons must use original actors, locations, conflicts and wording.
