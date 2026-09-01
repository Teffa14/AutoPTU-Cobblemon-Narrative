# Class & Faction Questline Network Architecture

Status: DESIGN PROPOSAL. This file defines narrative architecture and authority boundaries. It does not make any individual class questline, faction, NPC, location, reward, or world event canon by itself.

Date: 2026-09-01

## Purpose

Ouros now treats PTU class questlines and faction questlines as a primary narrative production target.

The project already contains broad world-state layers for institutions, professions, transport, research, ecology, care, archives, economy, factions, archaeology, media, education, contests, battle institutions and many other persistent systems. Future research should preferentially convert those layers into playable narrative threads instead of indefinitely adding disconnected horizontal systems.

The target structure is:

`WORLD_ARC -> FACTION_ARC -> CLASS_ARC -> CHARACTER_THREAD -> QUEST_EPISODE`

A single world event may support several class and faction perspectives without duplicating the underlying event.

## 1. Complete class coverage

The current PTU oracle catalog contains 69 Trainer Classes. Those 69 classes form the permanent class-questline backlog.

No class may be silently omitted because it is mechanically narrow, difficult to adapt, supernatural, combat-heavy, profession-heavy, playtest-derived, or currently unsupported by AutoPTU-Java.

Each class requires an eventual narrative profile with at least:

- class fantasy;
- social/world role;
- natural institutions and factions;
- mentor, rival and peer archetypes;
- recurring conflict types;
- exploration/research/profession/social/battle lanes where appropriate;
- short quest episodes;
- medium class arcs;
- at least one long-form class storyline candidate;
- intersections with other classes;
- intersections with faction arcs and world arcs;
- mechanical capability dependencies;
- reduced encounter variants where rich mechanics are not yet implemented.

Coverage progress must be measured against the complete catalog, not anecdotal examples.

## 2. Narrative identity is not mechanical ownership

A class questline may explore what the class means in the world, but narrative participation cannot grant mechanics that PTU/Caelo does not grant.

Hard boundaries:

- `CLASS_QUEST_COMPLETED != CLASS_FEATURE_GRANTED`
- `CLASS_REPUTATION != SKILL_RANK`
- `MENTOR_RELATIONSHIP != FEATURE_UNLOCK`
- `FACTION_RANK != TRAINER_CLASS`
- `QUEST_REWARD != PTU_MECHANICAL_REWARD` unless an authoritative progression transaction explicitly grants it
- `NPC_TITLE != MECHANICAL_CLASS`
- `CLASS_FANTASY != COMBAT_CAPABILITY`

Narrative rewards may include relationships, access, information, institutional standing, physical objects owned by the narrative layer when legal, future hooks, public memory, changed world state and eligibility for further story episodes.

Mechanical progression remains owned by authoritative PTU/Caelo progression state.

## 3. Multiclass and respec architecture

A character may hold up to four classes and may later reorganize or respec class investment. Narrative continuity must survive those changes.

The system therefore separates:

```yaml
character_class_narrative_state:
  character_id: null
  current_mechanical_class_refs: []
  historical_class_refs: []
  class_arc_states: {}
  class_relationship_refs: []
  class_institution_refs: []
  class_knowledge_refs: []
  completed_episode_ids: []
  unresolved_episode_ids: []
  former_build_event_refs: []
  current_eligibility_snapshot_ref: null
```

Hard boundaries:

- `HAS_CLASS_NOW != HAS_CLASS_HISTORY`
- `CLASS_REMOVED_FROM_BUILD != CLASS_HISTORY_ERASED`
- `CLASS_ARC_COMPLETED != CLASS_STILL_ACTIVE`
- `CLASS_HISTORY != CURRENT_MECHANICAL_PERMISSION`
- `RESPEC != WORLD_RETCON`
- `CURRENT_CLASS != ONLY_NARRATIVE_IDENTITY`

If a character removes Chef from the current build after completing Chef-related quests, the world still remembers the relationships, meals, institutions, conflicts and events that actually occurred. However, any Chef Feature, recipe effect, mechanical food benefit or other PTU capability must be checked against the current authoritative build before use.

## 4. Quest eligibility

Quest eligibility is evaluated dynamically.

```yaml
class_quest_eligibility:
  questline_id: null
  character_id: null
  current_class_requirements: []
  historical_class_requirements: []
  skill_requirements: []
  relationship_requirements: []
  institution_requirements: []
  faction_requirements: []
  world_state_requirements: []
  knowledge_requirements: []
  exclusions: []
  result: null
  evaluated_at_event_id: null
```

A quest may require:

- currently possessing a class;
- having previously possessed a class;
- no class requirement at all, but prior involvement with its institutions;
- a specific Skill or Feature when PTU/Caelo explicitly requires it;
- prior world or faction state;
- a completed earlier episode;
- a player choice that created the hook.

This allows respec-safe continuity without allowing inactive classes to retain unsupported mechanics.

## 5. Class arcs are perspectives on shared world state

A class arc should not create a parallel private copy of the world.

Example pattern:

A regional food shortage is one canonical world event.

- Chef sees ingredient substitution, cultural memory, kitchens, suppliers and public feeding.
- Survivalist sees wild sourcing, route reliability and field provisioning.
- Researcher sees crop disease or ecological evidence.
- Commander sees coordination and allocation.
- Chronicler sees historical records of earlier shortages.
- Capture Specialist may see pressure on wild populations and capture ethics.
- relevant factions pursue their own interests.

All of these perspectives must reference the same authoritative event, locations, actors, inventories and consequences where they overlap.

`SHARED_EVENT != DUPLICATED_EVENT_PER_CLASS`.

## 6. Class intersection graph

```yaml
class_arc_profile:
  class_id: null
  class_fantasy: null
  world_roles: []
  natural_institution_refs: []
  natural_faction_archetypes: []
  mentor_archetypes: []
  rival_archetypes: []
  peer_archetypes: []
  core_conflicts: []
  recurring_activity_lanes: []
  relevant_existing_layers: []
  world_arc_tags: []
  faction_arc_tags: []
  cross_class_edges: []
  battle_capability_dependencies: []
  reduced_execution_patterns: []
  source_refs: []
  status: proposed
```

Cross-class edges may be cooperative, competitive, complementary, ideological, institutional or situational.

The graph should deliberately create intersections. It should not force every class to interact with every other class.

## 7. Faction questlines

Every major reviewed faction should eventually have a persistent arc independent of whether the player joins it.

```yaml
faction_arc_profile:
  faction_id: null
  mandate_refs: []
  internal_groups: []
  public_goals: []
  private_goals: []
  current_pressures: []
  recruitment_or_access_rules: []
  member_roles: []
  rival_faction_refs: []
  allied_faction_refs: []
  class_affinity_refs: []
  class_tension_refs: []
  arc_thread_ids: []
  succession_or_split_hooks: []
  exit_or_defection_hooks: []
  source_refs: []
  status: proposed
```

Faction content must support several relationships where fiction permits:

- member;
- contractor;
- student;
- ally;
- rival;
- investigator;
- outsider;
- former member;
- mediator;
- adversary.

A faction questline must not assume permanent player membership.

## 8. World arcs as convergence substrate

World arcs provide large persistent pressures that multiple class and faction arcs can attach to.

Existing Campaign Arc Convergence architecture remains authoritative for thread convergence, pressure, recontextualization, payoff and aftermath.

Class/faction questlines add perspective and participation lanes; they do not override causal convergence rules.

`CLASS_ARC_IMPORTANCE != CONVERGENCE_FORCED`.

## 9. Quest episode grammar

```yaml
quest_episode:
  episode_id: null
  parent_class_arc_ids: []
  parent_faction_arc_ids: []
  parent_world_arc_ids: []
  source_world_fact_refs: []
  hook_refs: []
  eligible_character_ids: []
  activity_lanes: []
  objective_refs: []
  decision_points: []
  persistent_outputs: []
  relationship_outputs: []
  knowledge_outputs: []
  faction_outputs: []
  world_state_outputs: []
  mechanical_progression_request: null
  battle_contract_refs: []
  reduced_variant_refs: []
  completion_state: null
```

A quest episode should advance at least one persistent thread. Repeated jobs may exist, but they should not impersonate authored class progression unless they change relationships, knowledge, status, capability access, world state or future options.

## 10. Mechanical progression requests

When a quest is intended to coincide with a legitimate PTU progression event, narrative code may only request the authoritative progression subsystem to evaluate it.

It may not directly grant:

- Trainer Classes;
- Features;
- Edges;
- Skill Ranks;
- Moves;
- Abilities;
- Tutor Points;
- Combat Stages;
- permanent stat changes;
- item effects;
- Pokémon capabilities.

The progression owner either accepts or rejects the transaction according to PTU/Caelo and current engine state.

## 11. Research policy from Pass 172 onward

Future research should preferentially answer one or more of these questions:

1. Which PTU class fantasies or faction fantasies does this source enrich?
2. Which existing Ouros world-state layers can become playable quest content through it?
3. Which world arcs could connect several class lines around the same event?
4. Which NPC mentor/rival/peer archetypes emerge from it?
5. Which faction structures or internal conflicts emerge from it?
6. Which class intersections become possible?
7. Which battle capability categories would a full implementation require?
8. What reduced version can preserve the narrative premise with currently verified capabilities?

Horizontal world-system research remains valid when a real gap blocks several questlines, but it is no longer the default research target.

## 12. Research source breadth

Continue broad research across:

- Pokémon games, manga and spin-offs;
- Pokémon Ranger missions and institutions;
- Mystery Dungeon guild/exploration structures;
- academy, League, contest, research and profession story structures;
- PTU actual plays, campaign logs, GM notes and roleplay communities;
- fan games and ROM hacks;
- fan-made stories where high-level patterns are reusable;
- MMO class-order and faction-campaign structures;
- RPG companion, guild, profession and reputation quest design;
- dungeon, boss, puzzle and environmental storytelling design.

External stories remain inspiration only. Do not copy distinctive plots, dialogue or characters.

## 13. Engine dependency contract

Every battle-bearing class/faction quest episode must classify dependencies against the permanent capability families:

1. targeting/footprints/range/LoS
2. base movement legality
3. complete movement including push/pull/knockback/interception/forced movement
4. core calculations
5. action economy/initiative
6. full turn/round lifecycle
7. full stateful damage pipeline
8. status lifecycle
9. terrain/weather/hazards/zones/reactions
10. move-specific behavior
11. abilities
12. items
13. Trainer Features/perks
14. AI legal-action infrastructure
15. AI tactical policy
16. Minecraft/Cobblemon/Craftics adapter/playback support

Representative implementation of one mechanic never promotes an entire family.

## 14. Minecraft/Cobblemon boundary

Class identity, faction membership, quest progress, world facts, relationship state, mechanical class ownership and tactical results are not decided by Minecraft or Cobblemon presentation.

Minecraft/Cobblemon/Craftics may display:

- NPCs;
- institutions;
- class halls, workshops, kitchens, archives and guild spaces;
- quest markers;
- environmental changes;
- battle playback;
- earned narrative artifacts.

It cannot create PTU outcomes, grant classes, grant Features, decide battle state or rewrite quest history.

## 15. Immediate backlog

The immediate production order is:

1. build and maintain a complete 69-class narrative matrix;
2. map every class to existing Ouros research layers;
3. identify under-supported classes and research those gaps;
4. build class clusters and cross-class intersections;
5. build faction profiles that naturally host or oppose those class lines;
6. connect them through shared world arcs;
7. author full and reduced quest episodes;
8. track coverage until every class has a viable long-form storyline candidate.

This backlog remains live as new PTU/Caelo evidence, world canon and engine implementation changes arrive.