# Ouros Narrative Research — Missions, Dungeons & RP Structures — Pass 02

Status: Research only. Provenance and design evidence; not Ouros canon.

This pass deliberately avoids repeating the first scan's main sources and concentrates on mission economies, dungeon traversal, occupation progression, collaborative RP, puzzle design and mission-portfolio variation.

## 1. Pokémon Mystery Dungeon — hub -> request -> expedition -> return loop

Primary sources:
- https://www.pokemon.com/uk/pokemon-video-games/pokemon-mystery-dungeon-rescue-team-dx
- https://mysterydungeon.pokemon.com/en-us/world/
- https://mysterydungeon.pokemon.com/en-au/

Observed structure:
- A central social hub contains useful services and a request board.
- Requests originate from inhabitants with concrete problems.
- Jobs send the team into geographically distinct dungeons.
- Dungeon layouts and item placement vary between visits.
- Team composition matters because recruited Pokémon provide different capabilities.
- Completing work increases rescue-team rank and expands progression.
- The recurring job loop coexists with a larger mystery about world-scale disruptions.

Reusable lesson for Ouros:
A settlement can generate recurring work without feeling detached from the story if each request is grounded in a resident, location, ecological state or faction. The job itself can resolve locally while incrementing profession reputation, revealing clues, changing location state or contributing to a regional arc.

Ouros translation:
- settlements expose diegetic job boards, NPC requests and faction contracts;
- a job records requester, motivation, destination, urgency and world-state cause;
- dungeon/expedition content can vary by ecological state rather than by random layout alone;
- successful jobs may change profession/faction standing and unlock higher-trust requests;
- the hub should visibly react to completed work through NPC availability, services, rumors and physical state.

## 2. Pokémon Ranger — profession identity and capability-gated missions

Primary sources:
- https://www.pokemon.co.jp/game/ds/ranger/mission01.html
- https://www.pokemon.com/us/pokemon-video-games/pokemon-ranger/
- https://www.pokemon.com/us/pokemon-video-games/pokemon-ranger-guardian-signs/

Observed structure:
- The protagonist belongs to an in-world profession with a clear social purpose.
- Early missions are assigned at an appropriate competence level.
- Completing missions raises professional rank and unlocks more important assignments.
- Pokémon are recruited temporarily to solve environmental and traversal problems, not only to fight.
- Some missions require special movement contexts such as underwater travel or access enabled by particular Pokémon powers.

Reusable lesson for Ouros:
Progression can be occupational rather than purely badge-based. A player's profession can be an adventure generator, and Pokémon capabilities can be used as world-navigation verbs.

Ouros translation:
Potential profession tracks include ranger, researcher, courier, ruins surveyor, rescue worker, investigator, contest circuit staff, ecological warden, licensed battler and faction operative. Exact names and canon status remain unapproved.

A profession record could track:
- standing/rank;
- completed contract categories;
- trusted locations;
- known contacts;
- licenses or permissions;
- unresolved failures;
- access to sensitive missions.

Do not map Ranger's exact ranks or mission plots into Ouros. Reuse only the structural principle.

## 3. Pokécharms — collaborative Pokémon RP and distributed story ownership

Sources:
- https://forums.pokecharms.com/
- https://forums.pokecharms.com/threads/pokemon-ranger-almia-goes-old-school-rp-thread.19789/
- https://forums.pokecharms.com/threads/pkmn-mystery-dungeon-the-explorers-guild-sign-ups.18017/
- https://forums.pokecharms.com/threads/pokemon-the-rebellion-discussion.22585/

Observed structures:
- Pokécharms maintains a large dedicated Pokémon RP ecosystem with separate in-character and discussion spaces.
- Some public RPs explicitly allow participants to contribute setting details, encounters, characters, plot hooks and twists rather than relying on one GM for every beat.
- Exploration-guild premises naturally support independent subplots and player-created objectives.
- Safe-haven or organization premises generate mysteries from missing people, theft, internal factions and changing trust.

Reusable lesson for Ouros:
Players can become sources of future content. The system should preserve player-created rumors, discoveries, promises, NPC relationships and unresolved subplots as candidate hooks rather than treating them as disposable chat.

Ouros translation:
Add a `player_seed` provenance type to the Chronicle. A player seed can later be promoted into a quest candidate if it is compatible with canon and does not seize control of another player's character.

Candidate fields:
```yaml
seed_id: null
source_type: player_seed
creator_character_id: null
source_event_id: null
scope: local
entities: []
claims: []
open_questions: []
consent_scope: world_reuse
status: candidate
```

## 4. Fangame dungeon and puzzle design — readable challenge with recovery tools

Sources:
- https://eeveeexpo.com/ghosts-of-knowledge/
- https://www.eeveeexpo.com/released-games/

Observed patterns:
- Pokémon fangames use floor/tile logic, object-moving variations, hidden passages and puzzle-centered dungeons to create identity beyond combat.
- Public player feedback on Ghosts of Knowledge specifically praises distinct puzzle forms and the presence of restart switches and hints.
- Current Eevee Expo releases include compact interconnected locations, hidden passages, archaeology-driven dungeons, side quests, reputation systems and exploration-based secrets.

Reusable lesson for Ouros:
Puzzle difficulty should be recoverable. A dungeon needs explicit affordances for retrying, resetting or gathering hints so a failed puzzle does not permanently halt an adventure.

Ouros translation:
Every authored puzzle should declare:
- information visible before interaction;
- reversible vs irreversible actions;
- reset condition;
- hint sources;
- alternate capability-based solutions where appropriate;
- failure consequence;
- whether combat can alter the puzzle state.

## 5. Mission portfolio variation — action-block analysis

Research source:
- https://arxiv.org/abs/2603.18398

The 2026 MAQV research models open-world missions as action sequences and evaluates dimensions including combat, exploration, narrative, emotion, problem-solving and uniqueness across a large mission corpus.

Reusable lesson for Ouros:
A procedural quest system should measure portfolio-level repetition, not merely whether an individual quest appears coherent.

Proposed Ouros mission-vector fields:
```yaml
mission_vector:
  combat: 0
  exploration: 0
  social: 0
  investigation: 0
  puzzle: 0
  capture: 0
  traversal: 0
  emotional_stakes: 0
  world_consequence: 0
  novelty: 0
```

Before offering a new job, the generator can compare its vector to the player's recent activity history and prefer complementary experiences.

This is a project-specific adaptation; the field names above are not copied from MAQV.

## 6. PTU campaign evidence — persistent NPC dossiers

Source:
- https://forums.giantitp.com/showsinglepost.php?p=22586704&postcount=1

The public Heights of Londo PTU OOC material demonstrates a practical campaign memory pattern: settlements retain named NPC dossiers and concise records of how they intersected with player characters.

Reusable lesson for Ouros:
An NPC should maintain a short operational memory rather than a giant generated biography. Store relevant interactions, obligations, current objective, location and relationship edges.

## 7. PTU design boundary from internal project material

The supplied PTU Core Rulebook supports central-plot, character-centric and sandbox modes and recommends weaving ordinary Pokémon activities into larger plots. It also recommends meaningful interactivity and self-contained satisfaction that contributes to a larger whole.

Caelo's supplied Player Guide treats Social, Wild Encounter, PvP, Job, Raid, Contest, Gym and Dojo as distinct living-world activity containers. Its regional location material demonstrates environmental effects that matter mechanically.

Therefore the research above should influence content orchestration, traversal and world state, while exact battles still require PTU/Caelo validation.

## New design conclusions from this pass

1. Jobs need a requester and world-state cause, not just an objective marker.
2. Profession rank can be a parallel progression spine beside Gyms.
3. Pokémon capabilities should unlock alternate routes and solutions outside combat.
4. Dungeon puzzles need recovery affordances and alternate solutions.
5. Recent player activity should influence which quest shape is offered next.
6. Player-created narrative seeds can be stored and reused with provenance.
7. NPC memory should be concise, factual and relationship-oriented.
8. A stable social hub can make recurring procedural work feel grounded.

## Copyright and provenance guardrail

No dialogue, prose, distinctive characters, named plots or scene text from the external works above is being imported. Only high-level structural observations and factual feature descriptions are retained with source attribution.
