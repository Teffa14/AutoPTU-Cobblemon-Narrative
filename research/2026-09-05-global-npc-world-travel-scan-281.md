# Pass 281 research — global NPC world travel

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon authority: NONE by itself

## Question

How can Ouros let persistent NPCs move through a large world, keep appointments, travel off-screen and react to route changes without teleporting, without running Minecraft pathfinding globally, and without duplicating PTU movement rules?

## New public sources

### Kring, Champandard & Samarin — DHPA* / SHPA* hierarchical pathfinding (AIIDE 2010)

Source: AAAI AIIDE proceedings, “DHPA* and SHPA*: Efficient Hierarchical Pathfinding in Dynamic and Static Game Worlds.”

Reusable lesson:
- large game spaces benefit from hierarchical path planning rather than treating every navigation query as one flat fine-grained search;
- dynamic environments need a way to revisit path assumptions;
- performance, path optimality and memory are explicit tradeoffs.

Ouros transformation:
- use a coarse semantic world-route graph for world-agent decisions;
- leave fine local geometry to Minecraft/Cobblemon projection;
- replan when a semantic edge becomes unavailable;
- do not copy the paper's algorithms wholesale into narrative code or claim its performance characteristics for Ouros.

### chasm — game-agnostic agentic NPC engine

Source: public GitHub project `chasmlol/chasm`.

Reusable lesson:
- persistent agents can schedule future actions and travel to real destinations;
- movement can combine local visible movement with off-screen progression;
- schedule and movement state need persistence rather than being recreated from the player's current cell.

Ouros transformation:
- reserve semantic travel time before commitments;
- preserve travel state while the NPC is off-screen;
- keep the engine adapter separate from the persistent agent brain.

No code, characters, dialogue, quests or implementation-specific timed-teleport behavior is copied. Ouros specifically avoids using teleport as semantic travel truth.

### RPG Maker NPC scheduler/routine implementations

Sources: public pages for Siro Games NPC Scheduler and BitQuest Studio Dynamic NPC Routines.

Reusable lesson:
- multi-map schedules need persistent location state and explicit map connections;
- off-screen routines can continue without the currently loaded map;
- graph connections are a useful boundary between high-level travel and local pathfinding.

Ouros transformation:
- route nodes/edges are world semantic data;
- local projection is a separate acknowledgement step;
- generic schedules feed the same global NPC agenda instead of region-authored event scripts.

These plugin designs are references, not adopted dependencies.

### Pokémon Tabletop community — exploration between towns

Source: r/PokemonTabletop discussion “Question for Exploration.” (2024-11-22)

Reusable lesson:
- travel distance between hubs can be represented as a sequence of meaningful areas rather than one continuous undifferentiated road;
- routes feel more alive when intermediate locations contain environmental activity and small stories;
- the amount of detail should depend on how important travel is to the campaign.

Ouros transformation:
- semantic travel edges may later expose authored points of interest or world-event hooks;
- an NPC's high-level trip can remain cheap off-screen while the same journey can expand into locally projected scenes when player proximity makes them relevant.

No submitted map, Pokémon vignette or campaign-specific encounter is imported.

### Pokémon Tabletop community — road-trip campaign experience

Source: r/PokemonTabletop discussion “Asking out of curiousity.” (2022-03-17)

Reusable lesson:
- long stretches of road can become empty content if every unit of distance is treated as play;
- travel should be compressed when nothing meaningful changes.

Ouros transformation:
- world agents advance across semantic-duration edges rather than simulating every step;
- local scenes are promoted only when an encounter, relationship, observation, route disruption or player presence makes them useful.

The specific campaign vehicle and setting are not reused.

### Pokémon Tabletop community — route utility and ecology

Source: r/PokemonTabletop discussion “Need help with making routes.” (2023-03-21).

Reusable lesson:
- route design benefits from considering its actual role in the campaign, nearby settlements, biome and points of interest;
- geography is more convincing when route content follows environmental context instead of existing only as battle filler.

Ouros transformation:
- route metadata can later consume ecology/world-state inputs and content importance without turning every trip into a random encounter table;
- route planning itself remains independent of ecology so the global NPC architecture works everywhere.

## Design synthesis

The sources converge on a useful three-level boundary:

```text
world agent chooses destination / semantic route / departure / ETA
-> local adapter projects visible traversal where required
-> AutoPTU receives only encounters that require structured mechanics
```

This prevents three authority failures:

1. loaded Minecraft geometry deciding where an off-screen NPC exists;
2. schedule code teleporting an NPC to make a commitment succeed;
3. world-route duration pretending to adjudicate PTU movement capabilities.

## Narrative opportunities enabled

A recurring rival can leave another city early enough to reach a tournament rather than spawning when the player enters the venue. A mentor can miss a meeting because a route was closed, later report the delay, and preserve that social consequence. A faction courier can know a restricted shortcut while an ordinary member uses the public road. A researcher can begin a journey off-screen and become locally projected only when the player crosses the same corridor. A travel interruption can remain a world event or escalate into AutoPTU without the travel planner deciding tactical outcomes.

## PTU / Caelo / project cross-check

No new PTU, Caelo or Kairos rule is adopted by this scan. The existing project authority boundary remains controlling: world-simulation duration and route selection are Ouros policy; structured movement remains AutoPTU/PTU territory when handoff occurs.

The current global agenda contract already states that missed commitments do not teleport an NPC and that travel planning must resolve locality gaps. Pass 281 implements that previously open seam rather than changing established canon.

## Provenance boundary

All named sources above remain research references. Their protected characters, dialogue, plots, maps and code are not Ouros canon. Fixture actors and route nodes introduced in Pass 281 are synthetic and have no lore authority.
