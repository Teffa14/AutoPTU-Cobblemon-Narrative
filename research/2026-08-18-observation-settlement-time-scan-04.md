# Ouros Narrative Research — Observation, Settlement & Time — Pass 04

Status: Research only. Provenance and design evidence; not Ouros canon.

This pass extends the existing work on missions, dungeons, factions, environment state, investigations and persistent actors. It focuses on a different layer: observational play, ecological knowledge, settlement growth, bounded time pressure, defensive preparation, expedition access, and quests that emerge from world mechanics rather than from detached objective lists.

## 1. New Pokémon Snap — observation as primary gameplay

Primary sources:
- https://newpokemonsnap.pokemon.com/en-au/
- https://newpokemonsnap.pokemon.com/en-us/create-photodex/
- https://www.pokemon.com/uk/pokemon-video-games/new-pokemon-snap

Observed structure:
- The player is conducting an ecological survey rather than collecting Pokémon through battle.
- Wild Pokémon are valuable because of their natural behavior, group activity, territoriality and environmental adaptation.
- Repeated expeditions matter because uncommon behaviors and interactions are not all visible at once.
- Research output becomes a persistent knowledge collection through the Photodex.
- The player can deliberately influence attention or behavior with tools, but observation remains distinct from capture or defeat.

Reusable lesson for Ouros:
Wild encounters can have informational value before they have combat value. A player should sometimes benefit from watching, documenting, following or understanding Pokémon rather than immediately initiating battle.

Ouros translation:
Create an `observation_event` layer that may record:
- species/form observed;
- behavior observed;
- group composition;
- location and environmental state;
- time/weather context;
- interaction with another species;
- nesting/feeding/migration evidence;
- player interference level;
- confidence and provenance.

A discovery can later influence research jobs, ecological predictions, encounter preparation, settlement policy, rumors or Pokédex-like knowledge without modifying legal PTU species data.

## 2. Pokémon Legends: Arceus — research tasks as regional access progression

Primary sources:
- https://legends.arceus.pokemon.com/en-us/story/
- https://www.nintendo.com/au/games/nintendo-switch/pokemon-legends-arceus/

Supplemental index:
- https://www.serebii.net/legendsarceus/requests.shtml

Observed structure:
- Jubilife Village acts as a base of operations for survey work.
- Assignments and requests are prepared in the settlement, executed in the field, and reported back afterward.
- Research involves more than catching; observing behavior and completing different research tasks contributes to progress.
- Research rank expands access to additional areas.
- Optional resident requests frequently connect Pokémon knowledge to everyday settlement needs.

Reusable lesson for Ouros:
Knowledge progression can be diegetic. Access to dangerous habitats, specialized jobs or institutional trust can depend on demonstrated field competence rather than a generic character-level gate.

Ouros translation:
A future research/profession layer can distinguish:
- species knowledge;
- habitat knowledge;
- behavior knowledge;
- environmental knowledge;
- verified field reports;
- institutional trust.

No direct Legends: Arceus rank system should be copied.

## 3. Legends: Arceus requests — small quests can permanently improve a hub

Source:
- https://gamewith.net/pokemon-legends-arceus/article/show/31363

Observed examples include requests that expand shop inventory, clothing options, photography services and agricultural capacity. These are optional tasks but visibly improve the usefulness of the settlement.

Reusable lesson for Ouros:
Small jobs become meaningful when they change a service, person, supply chain, facility or visible location state.

Ouros translation:
A settlement improvement should store its causal chain:

```yaml
settlement_upgrade:
  upgrade_id: null
  location_id: null
  sponsor_ids: []
  prerequisite_states: []
  requested_inputs: []
  completion_event_ids: []
  service_changes: []
  visual_changes: []
  npc_changes: []
  new_hooks: []
```

The reward is then partly systemic rather than only an item payout.

## 4. Public PTU retrospective — Tales of Visiwa

Source:
- https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Observed structure:
- The campaign used a dangerous wilderness where access itself had an in-world Explorer certification context.
- Individual PCs entered the central conflict through different personal encounters and motives.
- Their team identity formed after those separate hooks converged.
- Character professions, research interests, personal relationships and recurring Pokémon continued to matter throughout the central conflict.
- Memorable encounters often combined tactical terrain with social or narrative resolution rather than ending only through knockout.

Reusable lessons for Ouros:
- A party or multiplayer group does not need one identical inciting quest; separate personal hooks can converge on a shared problem.
- Exploration credentials can make dangerous-region access feel institutional and contextual.
- A boss or antagonist encounter can resolve through persuasion, changing allegiance or new information when the fiction supports it.
- Character-specific expertise should remain useful during long central arcs.

## 5. Public PTU retrospective — Over There!

Source:
- https://pokemontabletop.com/over-there-a-world-war-one-pokemon-campaign-a-retrospective/

Observed structure:
- Players had an abandoned village as a defensive base.
- Each game day gave a bounded number of opportunities for exploration/preparation before a nightly attack.
- Hostile actors altered the map over time: destroyed infrastructure, encroaching terrain and potential flooding created persistent pressure.
- Repairing infrastructure mattered because it changed future route access.
- The campaign taught its own operational rules through repeated play rather than exposition alone.
- The GM retrospective explicitly warns that concealing the true campaign premise from players risked alienating them.

Reusable lessons for Ouros:
1. Time pressure becomes legible when the world shows what advances between player actions.
2. A home base can convert exploration resources into defense, access and recovery.
3. Hostile fronts can alter terrain and infrastructure even when players are elsewhere.
4. Repair/fortification can be narrative progression.
5. Surprise is valuable, but the system should not invalidate a player's chosen fantasy or build through hidden premise replacement.

Ouros translation:
Introduce explicit `regional_clock` and `maintenance_state` concepts. These should be used sparingly and only where the fiction establishes pressure.

## 6. PTU scenario outline — ecology, industry and conflict as one causal system

Source:
- https://pokemontabletop.com/wiki/index.php/Quest%3AASOIAI_Outline

Publicly indexed outline details connect industrial/mining activity, displaced Fire Pokémon, failed hot springs, tourism/research decline, poaching and a supernatural ecological crisis.

Reusable lesson for Ouros:
Strong regional problems can connect ecology, economy, infrastructure, Pokémon behavior and faction activity through one causal graph.

Ouros translation:
When generating a regional arc, avoid isolated problem flags such as `pollution=true`. Store the chain of causes and affected stakeholders so different players can intervene at different points.

Example abstract graph:

```text
resource extraction
  -> habitat disturbance
  -> species displacement
  -> local service failure
  -> economic decline
  -> opportunistic exploitation
  -> escalating ecological response
```

The exact source scenario, characters and plot are not imported.

## 7. Pokémon Burning Scales — density over geographic scale

Public repository:
- https://github.com/Benitex/Pokemon-Burning-Scales

The project describes a small open world built around dense interactions, characters and numerous side quests rather than constant region-to-region travel.

Reusable lesson for Ouros:
A Minecraft region does not become richer by endlessly expanding its map. Narrative density, reuse of locations and changed context can make a compact area support more stories than a much larger static map.

Ouros translation:
Track a `location_content_density` target and favor revisiting evolved spaces before generating another one-use location.

## 8. Settlement recruitment pattern — residents as capabilities

Public fan-game guide:
- https://pokemonzfangame.com/acrylic-town-residents-guide/

The described side activity has the player recruit residents into a depleted settlement, with residents unlocking services as the town recovers.

Reusable lesson for Ouros:
A settlement can grow through people rather than only construction levels.

Ouros translation:
Potential resident state:

```yaml
resident_candidate:
  npc_id: null
  current_home_id: null
  relocation_motives: []
  requirements: []
  settlement_fit: []
  service_candidate: null
  relationship_dependencies: []
  relocation_status: null
```

Migration must remain character-motivated. NPCs should not function as collectible buildings.

## 9. Procedural quest research — world facts and motivations first

Research source:
- https://arxiv.org/abs/1808.06217

CONAN generates quests from a world represented as facts about characters, locations and items, considering character preferences and motivations.

Reusable lesson for Ouros:
The existing world-state-first mission pipeline is preferable to selecting a quest trope first and painting Pokémon names over it.

Ouros extension:
Every generated objective should be traceable to at least one world fact, actor need or mechanical dependency. The generator should be able to answer `why does this objective exist now?`.

## 10. Deriving quests from open-world mechanics

Research source:
- https://arxiv.org/abs/1705.00341

This work models Minecraft mechanics as logical rules, then analyzes dependencies, loops and bottlenecks to place meaningful goals in the open world.

Reusable lesson for Ouros:
Because Ouros actually lives inside Minecraft/Cobblemon, content generation can eventually inspect what the player can physically do rather than treating the overworld as decorative scenery.

Potential future inputs:
- reachable locations;
- traversal capabilities;
- available crafting/resources;
- facility states;
- current NPC services;
- encounter access;
- blocked routes;
- battle-engine availability;
- world-state dependencies.

A quest should not ask for an action that the current world cannot support.

## 11. Design conclusions from this pass

1. Observation should be a first-class interaction alongside battle, capture and dialogue.
2. Knowledge can unlock opportunities without becoming a replacement XP bar.
3. Small resident requests become valuable when they improve persistent services or locations.
4. Shared arcs can converge from different personal entry points.
5. Time pressure needs visible clocks and causal state changes, not invisible punishment.
6. Base maintenance, repair and fortification can be adventure progression.
7. Regional crises should be causal graphs linking ecology, infrastructure, economy and actors.
8. Dense reuse of evolving locations is preferable to endless disposable geography.
9. NPC migration can change settlement capability when relocation is motivated in-fiction.
10. Procedural objectives should derive from world facts and executable mechanics.

## PTU / Caelo mechanics boundary

The supplied project PTU/Caelo files remain authoritative for mechanical execution. This pass introduces knowledge, scheduling, settlement and orchestration state only.

Observation does not invent new Skill effects. Any check involving Perception, Survival, Pokémon Education, Medicine, Technology, social Skills, capabilities or other PTU concepts must use the project's actual governing rules.

Environmental hazards, battle effects, capture, experience, Moves, Abilities and capabilities continue to require source and AutoPTU validation.

## Copyright and provenance guardrail

No external dialogue, prose, distinctive characters, complete plots, quest text or custom mechanical systems are imported. Only structural lessons and factual feature descriptions are retained with source attribution.
