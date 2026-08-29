# Ouros Narrative Research — Slope Instability, Landslide & Rockfall Continuity — Pass 114

Status: RESEARCH / PROVENANCE ONLY. NON-CANON. This file records external inspiration, internal cross-checks and exclusions. It does not establish Ouros geography, hazard frequency, engineering practice or PTU mechanics.

Date: 2026-08-28

## Research target

Pass 114 investigates a gap between existing Ouros systems: persistent slope observations, landslide/rockfall events, evolving footprint evidence, access consequences, assessment, stabilization handoffs and long-term recovery.

The full repository tree was inspected before authoring. No dedicated landslide, rockfall, debris-flow or slope-instability continuity layer exists. Related authority already exists in:

- Geology, Excavation & Resource Frontier — geological sites, context, disturbance and interpretation;
- Roads, Bridges & Detours — route restrictions, detours and reopening;
- Weather — atmospheric observations and forecasts;
- Seismic Monitoring — earthquake observations, detection and recovery handoffs;
- Volcanic Monitoring — volcanic episodes and downstream handoffs;
- Winter Mountain Operations — snow/ice/avalanche observations and winter access;
- Stormwater — drainage/flood observations and recovery;
- Wildfire — fire incidents and post-incident continuity;
- Crisis/Rescue — evacuation, rescue, stabilization and recovery coordination;
- Facility Maintenance/Public Works — technical assessment, repair/work and verification.

The new topic therefore must preserve slope-specific evidence without stealing those systems' decisions.

## Internal PTU / Caelo cross-check

The controlling internal source scan remains `research/2026-08-18-source-scan.md`.

Relevant conclusions already established there:

- PTU supports location-specific mechanical identity when a governing rule actually defines the effect.
- Caelo demonstrates authored environmental conditions, but one location-specific rule does not create a universal environmental subsystem.
- narrative/world state and tactical rules must remain distinct.
- exact Skills, Moves, Abilities, Items, Trainer Features, statuses, damage, movement changes and terrain effects require governing PTU/Caelo evidence plus current AutoPTU implementation evidence.

Pass 114 found no internal authority for universal landslide prediction, falling-rock damage, debris-flow forced movement, slope-angle checks, automatic collapse, burial, dust status, mud penalties or species-derived slope sensing.

## Public Pokémon source — Unova Route 10 and old Victory Road

Source: https://bulbapedia.bulbagarden.net/wiki/Unova_Route_10

Public documentation records that a landslide occurred on the old Victory Road between Black/White and Black 2/White 2. As a precaution, the Route 10 entrance from Opelucid City was sealed, and a new path/new Victory Road took over the functional connection.

Reusable high-level lessons:

1. A slope event can permanently change regional topology without destroying the surrounding world.
2. Closure, abandonment and replacement can be more narratively useful than instant restoration.
3. A former main route can become a legacy alignment whose old importance still matters to maps, memory, institutions and later exploration.
4. A new route can inherit traffic and institutional functions while the old place remains historically meaningful.

Ouros transformation:

- preserve the failed/closed alignment as a persistent world object;
- let Travel and Road Operations own the replacement connection;
- retain old notices, maps, local names and prior journey records as provenance;
- allow later investigations, habitat change, heritage use or stabilization projects without automatically reopening the route.

Nothing about Unova's exact geography, League gates, characters or plot is imported.

## Public Pokémon source — Giant Chasm access change

Source: https://bulbapedia.bulbagarden.net/wiki/Giant_Chasm

Between Black/White and Black 2/White 2, the path from Lacunosa Town toward Giant Chasm is documented as blocked by a landslide, with a physical obstruction affecting the connection.

Reusable lesson:

A large regional event and a small local obstruction can coexist in the same continuity model. Narrative state should identify the exact affected connection rather than converting an entire named area into `INACCESSIBLE`.

Ouros transformation:

- preserve segment-level blockage scope;
- separate the observed blockage from the inferred cause;
- allow access from another side when world topology supports it;
- record later clearing as a new event rather than rewriting the earlier blocked state.

The Strength interaction, exact boulder and game progression gate are not imported as Ouros mechanics.

## Public Pokémon source — Pokémon Ranger, Krokka Tunnel

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Krokka_Tunnel
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Ranger/Part_2

Krokka Tunnel uses rockfalls as a route consequence. Early in the story, falling boulders separate actors and interfere with travel between settlements; a later mission returns to the same tunnel and removes the rockfalls.

Reusable high-level lessons:

1. The dramatic incident and the restoration operation can be separate playable episodes.
2. A blockage can affect communities beyond the immediate encounter location.
3. Returning to a changed place creates continuity: the second visit can answer a problem established earlier rather than spawning an unrelated dungeon.
4. Clearing material is a world-state operation with social consequences, not merely an animation after combat.

Ouros transformation:

- create a slope/rockfall event record;
- hand route restriction to Road/Travel authority;
- preserve clearing as a later operation with its own evidence and verification;
- let reopened connections alter routines, commerce, visits and relationships.

The Go-Rock Squad, exact Pokémon, mission beats, Field Moves and plot are excluded.

## Public Pokémon source — Kalos Route 9 / Spikes Passage

Source: https://bulbapedia.bulbagarden.net/wiki/Kalos_Route_9

Route 9 is a rough mountain path whose traversal depends on a deliberately authored travel mode, and large boulders obstruct parts of the route.

Reusable lesson:

Rough terrain, obstruction and route usability should be authored separately. A location can remain visually rugged without every rock becoming a tactical hazard. Different travel modes can have different route viability while the underlying geographic connection remains the same.

Ouros transformation:

- keep physical form, Travel viability and battle terrain as separate layers;
- never infer a required mount, Rock Smash, Strength or equivalent from visible Minecraft geometry;
- allow a route owner to mark a section usable for one authored travel profile and unavailable for another only when canon establishes those profiles.

## Public Pokémon source — Mystery Dungeon, Landslide Cave

Source: https://bulbapedia.bulbagarden.net/wiki/Landslide_Cave

Landslide Cave demonstrates that a landslide-themed place can function as an ordinary repeatable mission destination rather than existing only during a disaster climax.

Reusable lesson:

A slope-failure landscape can remain part of ordinary exploration after the initiating event is over. The narrative value can shift from emergency to route knowledge, ecology, mission access and accumulated local history.

Ouros transformation:

A legacy slide field can become a named exploration site, research location, wildlife habitat, controlled passage or local landmark. Its tactical geometry remains static unless exact mechanics are deliberately authored.

Dungeon floor count, encounters, traps, items and procedural generation are excluded.

## Public Pokémon Tabletop / community boundary

Broad searches for public PTU landslide/rockfall campaign material returned sparse, inconsistent examples and homebrew environmental mechanics. None provided sufficiently strong governing evidence to import a landslide rules package.

Design lesson:

Community scenarios remain useful for narrative premises, but numerical collapse checks, environmental damage, burial rolls or custom terrain effects cannot be treated as PTU 1.05 authority.

## External operational reference — USGS landslide definition and cascading consequences

Source: https://www.usgs.gov/programs/landslide-hazards/what-a-landslide

USGS describes landslides broadly as downslope movement of rock, debris or soil and notes that events can range from slow movement to rapid failure. It also describes consequences including blocked roads, damaged infrastructure and cascading effects such as debris dams and later flooding.

Reusable modeling lessons only:

- `LANDSLIDE` should not imply one speed, material or footprint shape;
- a single event may create several downstream cases owned by different systems;
- the event record and its consequences should remain linked without collapsing them into one global hazard state;
- consequences can persist much longer than the movement itself.

No real-world magnitude, speed, engineering or safety thresholds are imported.

## External operational reference — triggers are claims/evidence, not automatic causation

Sources:
- https://www.usgs.gov/faqs/what-a-landslide-and-what-causes-one
- https://www.usgs.gov/publications/landslide-triggers-and-types

Public USGS material identifies rainfall, snowmelt, water-level changes, erosion, earthquakes, volcanic activity and human disturbance among possible initiating/contributing factors. It also emphasizes that slope failures often have multiple causes.

Ouros design consequence:

`FAILURE_OBSERVED` must remain separate from `CAUSE_ESTABLISHED`.

Weather, Seismic, Volcanic, Stormwater, Wildfire, Geology, Public Works or an authored actor may supply evidence, but temporal proximity does not prove causation.

This is especially important for Pokémon agency: a Pokémon observed near a failure can be a witness, displaced resident, participant, victim, worker or unrelated passerby. Species/Type never establishes cause by itself.

## External operational reference — inventories, confidence and changing footprint knowledge

Sources:
- https://www.usgs.gov/tools/us-landslide-inventory-and-susceptibility-map
- https://www.usgs.gov/programs/landslide-hazards/data

USGS landslide inventories preserve event locations from multiple sources and explicitly carry differences in confidence/quality. Event knowledge improves as new observations and mapping arrive.

Reusable lessons:

- preserve observation provenance;
- allow approximate footprints and later revisions;
- an old map can be honest and incomplete rather than false;
- `NO_OBSERVATION` is not equivalent to `NO_FAILURE`;
- historical events should remain addressable after their footprint is refined.

Ouros should use stable event IDs plus versioned footprint observations, not silently overwrite the earlier evidence.

## External operational reference — monitoring is incomplete by nature

Source: https://www.usgs.gov/programs/landslide-hazards/monitoring

Monitoring is performed at selected sites and data can be preliminary or incomplete.

Reusable lesson:

An operational sensor does not imply complete regional coverage. A monitoring gap must remain `UNKNOWN_FOR_INTERVAL` or another explicit uncertainty state rather than being interpreted as stable terrain.

Ouros must not create a universal landslide prediction system from monitoring availability.

## Important boundary with existing Winter Mountain Operations

Pass 82 already owns snow/ice/avalanche operational continuity. Pass 114 must not duplicate it.

If moving material is primarily snow/ice and is authored as an avalanche/snow slide, Winter Mountain Operations owns the event record.

If a slope failure is primarily rock, earth or debris, the new slope-instability layer may own the event record.

A mixed event can reference both systems if canon/evidence requires it. The narrative generator must not classify a mixed event solely from visual Minecraft blocks.

## Important boundary with Stormwater and Volcanic systems

A debris flow may interact with drainage/flooding, but Stormwater owns drainage-network state and flood-control operations.

A volcanic lahar belongs under Volcanic Monitoring when the volcanic episode is the governing event. A slope-instability record may reference the observed mass movement only when that separation adds useful provenance.

Avoid two competing owners for the same event.

## Reusable narrative structures extracted in Pass 114

Persistent access loss:
A formerly ordinary connection can disappear for years, forcing a new route and giving the old alignment historical weight.

Incident then restoration:
The dramatic failure and later clearing/stabilization can be separate stories with different actors and consequences.

Partial knowledge:
First reports can locate a blockage, later observations refine the source area and runout, and still later assessment may revise cause claims.

Cascading ownership:
One slope event can create road closure, utility interruption, habitat disturbance, water blockage, workplace shutdown and rescue cases without the slope system deciding every consequence.

Legacy landscape:
A slide scar, debris fan, abandoned road, retaining work, changed stream or relocated service can remain narratively useful long after the emergency ends.

Noncombat mystery:
Conflicting maps, inspection photos, witness reports and route names can be reconciled through provenance rather than a hidden truth meter.

## Explicit exclusions

Pass 114 does not establish:

- numerical slope angle thresholds;
- landslide susceptibility scores as canon;
- failure probability;
- rainfall thresholds;
- earthquake-to-landslide formulas;
- material strength;
- debris velocity or runout calculations;
- rockfall trajectories;
- stabilization engineering procedures;
- retaining-wall specifications;
- road-clearing rates;
- generic falling-rock damage;
- burial or suffocation rules;
- mud/rock Slow Terrain by default;
- debris-flow forced movement;
- dust or respiratory status;
- automatic Ground/Rock-type resistance or immunity;
- species-based slope prediction;
- Pokémon-caused landslides from flavor alone;
- Move/Ability/Item/Trainer Feature interactions without exact PTU/Caelo contracts.

## Pass 114 design direction

Create a slope-instability continuity layer whose job is to preserve:

- stable slope-sector identity;
- observations and monitoring gaps;
- assessments with provenance and revision history;
- observed failure events;
- evolving source/runout/affected-footprint observations;
- blockage/impact handoffs;
- stabilization and verification handoffs;
- access-review handoffs;
- legacy failure history.

Keep dynamic landslide simulation outside AutoPTU until every required capability family and governing rule is actually verified.
