# Ecology-driven world events and player consequences — source scan 241

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03
Pass: 241
Canon effect: NONE

## Question

How can Ouros turn persistent ecological state into world events that have observable causes, evolving consequences and player agency without collapsing into random encounter tables or scripted quest flags?

## Existing Ouros constraints inspected

- `CURRENT_FOCUS.md`: ecology remains the active workstream.
- `design/ecology-development-program.md`: Pass 241 is ecology-driven quests/events; world truth must flow through Ouros, Cobblemon projection and explicit AutoPTU handoff.
- `design/ouros-source-authority-and-species-policy.md`: Minecraft presentation cannot author ecological or PTU truth.
- `design/observation-evidence-npc-knowledge-contract.md`: players and NPCs receive evidence and claims, not hidden truth.
- `canon/marea-interior-map-resident-network-v2.md`: Sendero del Vidrio, Estación Mirador, Puerto Bruma and Loma Clara already have fixed anchors and residents suitable for observation, route management and consequences.
- `canon/marea-interior-first-wild-population-v1.md`: Sendero has one canon-approved Fletchling population and one persistent encounter slot; no additional species are authorized by this pass.

## New public sources

### PTU community exploration and encounter practice

1. r/PokemonTabletop, “Question for Exploration” (2024-11-22)
   https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9
   Reusable lesson: maps feel more alive when wild Pokémon have small ongoing situations—resource theft, tree cutting, territorial behavior—rather than waiting as isolated combat nodes. Travel obstacles and POIs work better when their existence is tied to the environment.

2. r/PokemonTabletop, “How do you plan your wild encounters?” (2020-10-27)
   https://www.reddit.com/r/PokemonTabletop/comments/jivcud
   Reusable lesson: evidence such as territorial markings, sound, tracks and habitat context can precede contact. Perception/Survival/Education can support discovery and interpretation instead of every wild encounter beginning as combat.

3. r/PokemonTabletop, “GM Advice: sessions drawn out by each player wanting encounters” (2022-09-17)
   https://www.reddit.com/r/PokemonTabletop/comments/xgemb5
   Reusable lesson: world events should create shared group problems and choices rather than serial individual capture scenes. The ecological event should remain meaningful even if no capture attempt occurs.

These are community design observations, not Ouros rules authority.

### Pokémon structures

4. Pokémon Mystery Dungeon — natural disasters / rescue-team premise
   https://mysterydungeonwiki.com/wiki/Pkmn%3ANatural_Disasters
   Reusable structure: environmental disruption creates new traversal risks, rescues and institutional responses. A crisis can generate several local jobs without requiring one central battle.

5. New Pokémon Snap — ecological survey loop
   https://en.wikipedia.org/wiki/New_Pok%C3%A9mon_Snap
   Reusable structure: revisiting the same habitat under changed time/context reveals different behavior and new routes. Investigation can itself be progression.

6. Nintendo — Pokémon Ranger: Guardian Signs
   https://www.nintendo.com/jp/titles/20010000023022.html
   Reusable structure: protect nature and resolve incidents by coordinating with Pokémon and local conditions. Environmental intervention is a first-class adventure objective rather than scenery.

No distinctive plot, character or dialogue from these works is imported.

### Real ecology

7. USGS, “Migrating mule deer compensate en route for phenological mismatches” (2023-04-10)
   https://www.usgs.gov/publications/migrating-mule-deer-compensate-en-route-phenological-mismatches
   Finding: animals can change speed and stopover use to compensate for resource timing mismatches. Event consequence should therefore alter behavior and route use before assuming demographic loss.

8. USGS, “Drought reshuffles plant phenology and reduces the foraging benefit of green-wave surfing for a migratory ungulate” (2020-06-11)
   https://www.usgs.gov/publications/drought-reshuffles-plant-phenology-and-reduces-foraging-benefit-green-wave-surfing-a
   Finding: a shorter resource window can reduce foraging opportunity even when animals remain synchronized with the moving resource pulse.

9. Nature Ecology & Evolution, “Evolutionary and demographic consequences of phenological mismatches” (2019-04-22)
   https://www.nature.com/articles/s41559-019-0880-8
   Finding: consumer demand and resource abundance can become temporally misaligned; demographic effects depend on context and density rather than one universal penalty.

10. USGS, “Effects of road management on movement and survival of Roosevelt elk” (1997)
    https://www.usgs.gov/publications/effects-road-management-movement-and-survival-roosevelt-elk
    Finding: limiting vehicle access changed movement and was associated with improved survival. Human access management can therefore be a reversible intervention with ecological consequences.

11. U.S. National Park Service, “Bighorn Sheep Reclaimed Abandoned Habitat during the Pandemic...”
    https://home.nps.gov/articles/000/bighorn-sheep-reclaimed-abandoned-habitat-during-the-pandemic-and-had-lots-of-young-now-what.htm
    Finding: repeated human disturbance can produce cumulative avoidance and shift habitat use; reduced disturbance can allow rapid re-use of previously avoided space.

## Reusable event-design lessons

### Event source must be state, not a random quest roll

An ecology event should begin because one or more persistent variables cross a declared condition. Examples include a resource window opening/closing, route connectivity falling, disturbance accumulating, a cohort arriving late, a nesting site becoming exposed or an interaction edge becoming unusually strong.

A scheduler may decide when to evaluate conditions. It must not fabricate the ecological cause.

### Event and observation are separate

The event may be active before anyone knows it. Pass 240 should determine which NPCs or players acquire evidence and how quickly their claims converge on the real cause.

### Events need a causal graph

Recommended shape:

`driver -> ecological pressure -> behavioral response -> visible symptoms -> institutional/player response -> persistent consequence`

This prevents a quest objective from directly mutating world state without a causal seam.

### Event intensity is not one scalar

Useful dimensions include:

- spatial extent;
- duration;
- resource deficit/surplus;
- disturbance pressure;
- population exposure;
- route/connectivity effect;
- uncertainty;
- reversibility.

Two events with the same visible count may therefore require different responses.

### Player intervention changes pressures, not predetermined endings

Closing a trail, restoring a resource, reducing traffic, observing without approaching, relocating equipment or defending a site can alter variables. The engine should then re-evaluate consequences. The system should not jump directly to `GOOD_ENDING` because a quest flag was set.

### Consequences can be beneficial, harmful or mixed

A resource pulse can increase visible activity while also creating conflict at a bottleneck. A temporary closure can reduce disturbance while hurting travel/service continuity. Recovery can yield a different stable arrangement rather than return to the exact baseline.

### Shared events beat capture queues

A route-level problem gives every participant something to do: observe, communicate, manage access, fetch equipment, protect infrastructure, escort, investigate, or fight if escalation requires it.

## Proposed Ouros event families

These are taxonomy candidates, not canon events:

- `RESOURCE_WINDOW_SHIFT`
- `MIGRATION_TIMING_MISMATCH`
- `DISTURBANCE_THRESHOLD`
- `NESTING_CONFLICT`
- `PREDATOR_PRESSURE_SPIKE`
- `ROUTE_BOTTLENECK`
- `LOCAL_RECOLONIZATION`
- `HABITAT_RECOVERY_WINDOW`
- `ECOLOGICAL_INFORMATION_CASCADE`
- `HUMAN_WILDLIFE_CONFLICT`

## Pass 241 Marea test premise

Use only existing canon Fletchling and Sendero geography.

A temporary forage-resource window at the lower shelf becomes compressed relative to expected timing. The Fletchling population increases visible activity around a narrower time/space window. Human route use overlaps with that concentration and disturbance rises.

The event is not an “outbreak” and does not create population members. Possible responses include temporary route management, observation, equipment relocation and reduced approach pressure. Whether the situation improves must be derived from subsequent ecology state.

This premise combines Passes 235, 236, 238, 239 and 240 without inventing a second species or modifying existing canon.

## PTU/Caelo/Kairos cross-check

PTU skills can support field detection and interpretation when the active rules profile calls for them; this research does not introduce fixed DCs or replacement checks.

Kairos is useful evidence that living-world servers can run discrete quests/events against persistent character/world progression, but its specific encounter-generation and homebrew rules remain source-specific.

Caelo/Kairos content may suggest institutions, services or event operations only through explicit Ouros adoption.

## Mechanical boundary

The reduced Pass 241 event is world-state only. It requires no battle engine if players observe, report, redirect traffic or change non-tactical world-service variables.

If an event escalates into structured pursuit, defense or combat, its exact AutoPTU dependencies must be declared rather than inferred from the ecological state.

## Open questions

- Which event conditions should use deterministic thresholds versus seeded stochastic evaluation?
- How much hysteresis is required to prevent events opening/closing every evaluation tick?
- How are simultaneous events merged when they share a driver but affect different sites?
- Which interventions need explicit institutional authority before players can change access or infrastructure?
- How should event summaries expose uncertainty without leaking hidden state?
- What is the first adapter seam for projecting an event’s visible symptoms into Cobblemon/Minecraft?