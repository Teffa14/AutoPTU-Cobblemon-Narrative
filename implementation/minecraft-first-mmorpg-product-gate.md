# Minecraft-first MMORPG product gate

Status: IMPLEMENTATION PRIORITY
Date: 2026-09-02

## Objective

The success criterion is not the amount of narrative architecture documented. The success criterion is whether a player can enter Minecraft and play a persistent PTU-derived Pokémon MMORPG.

New horizontal narrative infrastructure should normally be created only when it unlocks a visible gameplay slice, a concrete implementation dependency or a required persistence invariant.

Primary review question for implementation work:

> What can the player do or see in Minecraft after this change that they could not do or see before?

Documentation-only work remains valid when it immediately unblocks implementation, protects mechanical authority/canon, or records source/provenance decisions that code must consume.

## First complete vertical slice

A first slice is not complete until a player can, in a fixed Ouros area:

1. create/load a persistent Trainer;
2. possess a legal starter Pokémon;
3. enter a physically built settlement;
4. see persistent NPCs with identity and schedule;
5. accept a quest through Minecraft interaction;
6. leave along a physical route;
7. encounter a visible wild Pokémon selected from authoritative population/context data;
8. escalate to an authoritative PTU battle;
9. perform ordinary legal movement/actions/Moves through the Java engine;
10. receive authoritative damage/status/result state;
11. capture a legal official Pokémon through the authoritative capture path;
12. reconcile the result back into the Minecraft world;
13. receive legal progression/reward state;
14. return to a service point for healing/rest/shop interaction as supported;
15. complete the quest and persist its consequence;
16. disconnect and reconnect with Trainer, Pokémon, quest and world consequences preserved.

A visually impressive route without authoritative battle/capture/persistence is not the completed slice. A complete engine unit test without Minecraft-visible execution is also not the completed slice.

## Product pillars

The target MMORPG eventually needs these connected pillars:

- Trainer creation, Skills, Edges, Features, classes and respec/history.
- Persistent Pokémon identity, Loyalty/care, Moves, Abilities, injuries and progression.
- Physical exploration using PTU-relevant movement/capabilities where applicable.
- Visible ecology and encounter selection by location/time/weather/context.
- AutoPTU-Java tactical combat authority.
- Capture and roster ownership/custody persistence.
- NPC homes, jobs, schedules, teams, relationships and progression profiles.
- Unified quest runtime with main/class/faction/region/secondary/Pokémon/dungeon/equipment/item/relationship/rival/server-event/character/exploration/competitive/settlement content.
- Shops, items, crafting, gathering, fishing, farming, research and other professions where rules support them.
- Gyms/dojos/contests/tournaments and other competitive circuits.
- Parties, dungeons, bosses, raids/world events and multiplayer synchronization.
- Housing/property/homestead systems where explicitly designed for Ouros.
- Live world time, weather, schedules, ecology, events and server persistence.

## Source-to-game rule

Research from PTU, Caelo, Kairos and other sources must terminate in one of four outcomes:

1. reject for Ouros;
2. retain as reference only;
3. approve as a rules/content candidate with an explicit implementation contract;
4. implement and verify in Minecraft/runtime.

Indefinite accumulation of unrelated horizontal research is not the default next step once a gameplay dependency is understood.

## Source pack architecture

Do not encode `if (caelo)` or `if (kairos)` throughout gameplay systems.

Use explicit rules/data profiles so future sources can be compared or selectively adopted without forking the engine architecture.

At minimum, profiles should be able to select or override:

- character/progression rules;
- class/Feature content;
- capture rules;
- rest/injury rules;
- experience rules;
- encounter generation parameters;
- item/service availability;
- economy/downtime policies;
- competitive/progression gates;
- allowed official species/forms/gimmicks.

Species/form safety gates from `design/ouros-source-authority-and-species-policy.md` apply before profile content becomes runtime data.

## Near-term implementation order

1. Minecraft world/runtime end-to-end handoff.
2. Fixed first settlement/route as physical content.
3. Persistent NPC identity + schedules + teams.
4. Trainer/PTU sheet interaction inside Minecraft.
5. Visible wild encounter director.
6. Minecraft -> AutoPTU-Java -> Minecraft battle reconciliation.
7. Capture end-to-end.
8. Quest runtime visible in the same slice.
9. XP/Trainer/Pokémon/class progression.
10. Healing/rest/shop/item loops.
11. First dungeon + boss with explicit capability dependencies.
12. Multiplayer party synchronization.
13. Class/faction questline gameplay.
14. Recurring world events.
15. Expansion to additional settlements/regions.
16. Deeper long-tail world simulation only as concrete gameplay requires it.

Pass 206 already moved in this direction by defining a Minecraft-visible Marea wild encounter runtime contract. Future work should build on that vertical path rather than return to disconnected world-state essays.
