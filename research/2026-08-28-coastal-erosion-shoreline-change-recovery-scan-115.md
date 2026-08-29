# Ouros Narrative Research — Coastal Erosion, Shoreline Change & Recovery — Pass 115

Status: RESEARCH / PROVENANCE ONLY. NON-CANON. This file records external inspiration, internal cross-checks and exclusions. It does not establish Ouros coastal geography, erosion rates, engineering practice, sea-level history, hazard frequency or PTU mechanics.

Date: 2026-08-28

## Research target

Pass 115 investigates a gap between existing Ouros systems: persistent shoreline observations, erosion/deposition evidence, beach/dune change, overwash or breach observations, revised maps, access consequences, recovery handoffs and long-term coastal memory.

The complete repository tree was inspected before authoring. Existing authority already covers:

- Maritime, Coasts & Underwater Depths — maritime regions, coastal locations, sea lanes, tidal access, marine habitat and marine conditions;
- Coastal Navigation Aids — lighthouses, buoys, beacons, observations and navigation notices;
- Weather — atmospheric observations, forecasts and revisions;
- Stormwater — drainage networks, local flooding and flood-control operations;
- Slope Instability — rock/earth/debris movement on authored slope sectors;
- Geology — geological sites, formation/material interpretation and authored disturbance;
- Roads & Bridges — route restriction, detours and reopening;
- Travel — journey topology and actor-specific travel viability;
- Conservation / Wildlife Monitoring — habitats, stewardship and ecological interpretation;
- Ports / Harbors — operational port infrastructure;
- Crisis / Rescue — evacuation, rescue and emergency coordination;
- Public Notices / Cartography — published warnings, maps and editions.

No dedicated continuity layer exists for a coastline whose physical edge changes over time. The new topic therefore has to preserve coastal-change evidence without stealing route, weather, flood, habitat, geology or infrastructure decisions from their owner systems.

## Internal PTU / Caelo cross-check

The controlling internal source remains `research/2026-08-18-source-scan.md`.

Established guardrails remain active:

- PTU/Caelo may give a specific authored location a mechanical identity when a governing source explicitly defines the effect.
- One representative environmental mechanic never proves a universal coastal subsystem.
- world-state evidence and tactical battle rules remain separate.
- exact movement changes, LoS effects, damage, statuses, terrain, weather, reactions, Moves, Abilities, Items and Trainer Features require governing PTU/Caelo evidence and current engine contracts.

Pass 115 found no internal authority for universal shoreline-retreat calculations, wave erosion, dune collapse, overwash forced movement, sand burial, saltwater status, cliff-undercut collapse, storm-surge damage, species-derived erosion sensing or automatic Water/Ground/Rock-type coastal immunity.

## Public Pokémon source — Shoal Cave

Source: https://bulbapedia.bulbagarden.net/wiki/Shoal_Cave

Shoal Cave in Hoenn changes substantially between high and low tide. Different portions become reachable or unreachable depending on water state.

Reusable high-level lessons:

1. Coastal access can be stateful without changing the identity of the place.
2. The same location can support distinct exploration graphs at different observed conditions.
3. Access knowledge can matter as much as raw geography.
4. A condition can change overworld traversal without automatically becoming a tactical modifier.

Ouros transformation:

- keep stable location and connection IDs while access windows change;
- record the condition and observation that justified opening or closing a connection;
- preserve actor knowledge of the current or expected window;
- let Travel/Maritime decide journey viability;
- do not infer water combat, current, drowning or forced movement from the world-state access change.

The six-hour schedule, exact rooms, item placement, encounter tables, HM requirements and game-specific tide implementation are excluded.

## Public Pokémon source — Pokémon Ranger: Shadows of Almia, Marine Cave / Nabiki Beach

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Marine_Cave_(Ranger)
- https://bulbapedia.bulbagarden.net/wiki/Vientown

Marine Cave is inaccessible while the tide is high and becomes reachable when the tide lowers during a mission. The entrance exists throughout; access changes with observed coastal state.

Reusable lesson:

A coastal threshold can remain a persistent landmark even when it is temporarily unavailable. A quest can begin because a familiar edge becomes reachable rather than because a new dungeon materializes from nowhere.

Ouros transformation:

- separate `FEATURE_EXISTS`, `ENTRY_EXPOSED`, `ENTRY_VERIFIED_FOR_ACCESS` and `ACTOR_TRAVEL_VIABLE`;
- preserve old observations and failed attempts;
- allow a later mission to reuse the same access point under a different condition;
- keep tide timing and battle mechanics under existing authorities.

The Ranger plot, machine, characters, partner system and field mechanics are excluded.

## Public Pokémon source — Seaside Cave

Source: https://bulbapedia.bulbagarden.net/wiki/Seaside_Cave

The location description presents a passage shaped by wind, waves and Pokémon, with several entrances connecting wider travel spaces.

Reusable lesson:

A route can have a geomorphic history without the game needing to simulate every step of that history. A coastal passage may be the cumulative result of environmental and biological activity, while the current playable state remains a stable authored connection.

Ouros transformation:

- allow coastal features to carry origin claims and observation history;
- distinguish observed form from asserted cause;
- permit Pokémon to appear in local explanations without treating species presence as proof of geomorphic agency;
- let a future change revise or remove one entrance without deleting the whole site.

Exact Pokémon, Strength puzzle, progression gates and plot are excluded.

## Public Pokémon source — Kanto Route 19 across generations

Source: https://bulbapedia.bulbagarden.net/wiki/Kanto_Route_19

Public documentation shows Route 19 changing substantially across generations: the ocean portion becomes smaller, construction appears on the landward section, and later versions present a thinner beach and altered rocks/fences.

This is not proof of canonical erosion. It is useful as a continuity-design precedent: a familiar coastal route can change shape between eras while retaining its identity and travel role.

Reusable lessons:

1. Long-term physical change does not require a new location ID.
2. historical maps can be valid for their own period and wrong for the current coastline;
3. construction and natural coastal change should remain separate claims unless evidence connects them;
4. the player's memory of an older layout can itself become narrative content.

Ouros transformation:

- preserve versioned shoreline observations and map editions;
- keep stable route/location IDs where identity persists;
- record new connections, lost beach sections or changed public-space use as dated events;
- avoid retroactively rewriting old screenshots, records or witness accounts.

No claim is imported that erosion caused Route 19's game-map revisions.

## Public Pokémon source — beach and sandbar geography

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Beach
- https://bulbapedia.bulbagarden.net/wiki/Alola_Route_13

Pokémon locations use beaches as more than decorative edges. Public descriptions include sandbars, surf spots, rest stops, caves, rough-wave coasts and ordinary social/economic activity.

Reusable lesson:

A shoreline can simultaneously be transport edge, habitat, workplace, leisure space, landmark and access route. Physical change therefore creates distributed consequences rather than a single `beach_closed` flag.

Ouros transformation:

A shoreline segment can hand consequences to Tourism, Workplaces, Conservation, Roads/Travel, Maritime, Housing, Public Space or local commerce while retaining one stable coastal-change event history.

## Public PTU community source — regional geography tied to habitat

Source: https://www.reddit.com/r/PokemonTabletop/comments/134qsk5/

A public PTU discussion recommends considering habitat and capabilities when building starter pools and gives coastal versus mountain settlements as an example of world geography influencing available Pokémon.

This is not rules authority. The reusable worldbuilding lesson is that physical region identity should feed ecology and ordinary life, not only combat encounter tables.

Ouros transformation:

When a shoreline changes, habitat observations and human routines may also change, but Conservation/Wildlife systems own those interpretations. The coastal layer records overlap and handoffs rather than automatically changing species populations.

## Public PTU living-world source — persistent player impact

Source: https://www.reddit.com/r/PokemonTabletop/comments/1jxrz43/

A public PTU living-server description emphasizes characters existing in a world that changes continuously and being able to affect that world.

Reusable lesson:

Long-lived environmental changes work best when they persist between sessions and become context for later stories. A repaired boardwalk, moved beach access, newly protected dune or retired path should survive as world state rather than reset at the end of the quest.

No server-specific lore, rules or content is imported.

## External operational reference — coastal change includes erosion and deposition

Source: https://www.usgs.gov/science/science-explorer/coasts/coastal-change

USGS public material distinguishes erosion, where sediment leaves an area, from deposition, where sediment accumulates elsewhere. It also describes coastline movement being studied through repeated historical and current observations.

Reusable modeling lessons only:

- coastal change can add land in one observed sector while removing it in another;
- `SHORELINE_CHANGED` should not default to `EROSION`;
- observations need dates, methods and geographic scope;
- historical imagery can be valid evidence without being current truth;
- habitat and infrastructure consequences may emerge from the same physical change but remain separately owned.

No measurement method, rate, model, US terminology or engineering threshold becomes Ouros canon.

## External operational reference — event categories should remain distinct

Source: https://www.usgs.gov/centers/spcmsc/science/storm-induced-coastal-change

USGS distinguishes several storm-driven outcomes, including beach erosion, dune erosion, overwash, inundation, breaching, marsh erosion and cliff erosion.

Reusable lesson:

A dramatic coastal episode should not collapse into one scalar hazard state. Different observed effects have different footprints and downstream consequences.

Ouros transformation:

Possible descriptive observation/event tags may include:

- BEACH_EDGE_CHANGE_OBSERVED
- DUNE_OR_BACKSHORE_CHANGE_OBSERVED
- SEDIMENT_DEPOSITION_OBSERVED
- OVERWASH_DEPOSIT_OBSERVED
- NEW_OR_CHANGED_CHANNEL_OBSERVED
- COASTAL_CLIFF_CHANGE_OBSERVED
- SHORELINE_POSITION_REVISION
- ACCESS_POINT_CHANGE_OBSERVED

These remain evidence labels. They grant no PTU damage, movement or terrain effect.

## External operational reference — recovery can take years and does not restore the old shape exactly

Sources:
- https://www.usgs.gov/centers/spcmsc/science/storm-induced-coastal-change
- https://www.usgs.gov/centers/spcmsc/science/hurricane-sandy-coastal-system-change-fire-island-new-york

Public USGS material describes dunes rebuilding over long periods and repeated surveys continuing years after a major event. Post-event shorelines can also shift in different directions at different times.

Reusable lessons:

1. `STORM_ENDED` and `COAST_RECOVERED` are separate states.
2. Recovery is not necessarily a return to the previous geometry.
3. an immediately post-event map can differ from a map months later without either being fraudulent;
4. a temporary detour, boardwalk, observation post or habitat can outlive the event that created it.

Ouros should model recovery sequences and revised observations rather than restoring a saved pre-event coastline wholesale.

## External operational reference — forecasts and observations are separate evidence products

Sources:
- https://www.usgs.gov/programs/cmhrp/science/national-assessment-coastal-change-hazards-project
- https://www.usgs.gov/centers/spcmsc/science/hurricane-sandy-response-storm-impacts-and-vulnerability-coastal-beaches

Public coastal-change programs compare forecasts with later surveys and imagery.

Reusable lesson:

A forecast is a dated claim about possible future change. A later survey is evidence of what was observed. Revised assessments should preserve the earlier forecast and its scope rather than overwrite it.

Ouros transformation:

- `COASTAL_CHANGE_FORECAST` remains distinct from `COASTAL_CHANGE_OBSERVATION`;
- forecast accuracy can become a science/institution story without a hidden truth meter;
- a sector outside the observed footprint remains unknown until evidence arrives;
- public notices can lag behind field observations without implying bad faith.

No real-world probability scale or hazard classification is imported.

## Boundary with Maritime and tidal access

Maritime already owns tide/current/sea-state context and tidal access windows.

Pass 115 owns persistent changes to the coastal edge when authored evidence says the physical shoreline or backshore changed.

Example:

- high tide temporarily covers a cave entrance -> Maritime tidal access;
- a later event deposits enough sediment that the entrance geometry is persistently different -> Coastal Change continuity record plus Maritime/Travel handoff.

Do not create duplicate owners for ordinary tide cycles.

## Boundary with Slope Instability

Coastal cliff retreat may involve rockfall or slope failure.

Use the governing physical event as owner:

- observed rock/earth/debris movement from a cliff sector -> Slope Instability owns the failure event;
- longer-term shoreline/cliff-edge position change -> Coastal Change may preserve the coastal observation and link to the slope event.

A Minecraft cliff face does not decide ownership.

## Boundary with Weather, Stormwater and Flooding

Weather owns atmospheric event/forecast state.

Stormwater owns drainage-network flooding and local flood-control operations.

Maritime owns sea-state/tide context.

Coastal Change can record overwash deposits, shoreline revisions or changed barrier geometry after an authored event. It does not calculate surge, rainfall, inundation depth or drainage behavior.

## Boundary with Conservation and Public Works

Conservation owns ecological interpretation, habitat protection and stewardship decisions.

Public Works / Facility Maintenance owns engineered asset work and verification.

The coastal layer may link a changed dune to a nesting-site observation, a damaged access path, a boardwalk project or a beach-replenishment proposal, but it never decides ecological benefit or engineering success by itself.

## Reusable narrative structures extracted in Pass 115

### The map that becomes historical while still in use

A public map, tourism brochure or courier route can remain widely used after the shoreline has moved. The document is not fake; it is stale.

### Two directions at once

One sector loses sediment while another gains it. Residents can truthfully report that “the beach disappeared” and “the beach grew” because they describe different segments.

### Recovery without reset

A beach or dune can recover function while taking a different shape. New paths, habitats, routines and property boundaries can persist.

### Temporary infrastructure becomes social infrastructure

A temporary walkway, observation platform, ferry handoff, market edge or meeting place created during restricted access can remain useful later.

### Repeated observation becomes story

Photographs, survey stakes, ranger notes, family albums, Pokémon observation logs and old route maps can collectively show a coastline changing over years.

### Pokémon behavior as evidence, not explanation

A particular Pokémon may stop using a nesting edge, begin resting on a new sandbar or repeatedly visit an exposed object. Preserve the observation. Let Ecology/Conservation interpret it. Do not infer species-wide sensing or causation.

### The coast as a multi-system hinge

One physical change may affect a path, business, habitat, public beach, navigation landmark and historic site. Each system receives a handoff and keeps its own decision authority.

## Explicit exclusions

Pass 115 does not establish:

- shoreline-retreat rates;
- sea-level-rise arithmetic;
- wave-energy calculations;
- sediment budgets;
- beach-profile equations;
- dune-height thresholds;
- erosion probability;
- storm-surge or runup calculations;
- overwash timing;
- breach probability;
- cliff-collapse probability;
- generic sand or surf movement costs;
- undertow/current forced movement;
- drowning;
- burial by sand;
- saltwater damage/status;
- wet/slippery terrain;
- visibility penalties from spray;
- automatic habitat change;
- automatic road/building closure;
- species-derived erosion prediction;
- Move-powered beach restoration;
- Water/Ground/Rock-type environmental immunity;
- Minecraft fluid/sand physics as world authority.

## Canon posture

Everything introduced by Pass 115 remains PROPOSED or UNKNOWN unless an existing canon source already establishes it.

The pass does not name an Ouros coast, settlement, institution, disaster, historic storm, protected dune, engineering program or Pokémon occupation.

Research provenance remains in this file. Candidate system architecture and adventure material remain in separate design/proposal files.