# Ouros Narrative Research — Volcanic Monitoring, Eruption & Ashfall Continuity — Pass 113

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is automatically Ouros canon.
Date: 2026-08-28

## Scope

This pass investigates a gap left between existing Geology, Weather, Infrastructure Outage, Crisis/Rescue, Travel, Public Notices, Pollution, Water, Agriculture, Health/Care and settlement-recovery systems: the persistent information and recovery lifecycle around volcanic unrest, eruption observations, ashfall observations, volcanic-site access and post-event reassessment.

The goal is not to add a generic volcano combat ruleset. The goal is to let a volcanic region remember what was observed, what was believed at the time, what notices were issued, which sectors experienced which consequences, what was later revised and how ordinary life changed before and after a volcanic episode.

The existing Geology layer already permits `VOLCANIC_FIELD` and `GEOTHERMAL_SITE` as site types and records geological disturbance. This pass therefore does not create a second geology authority. Weather continues to own meteorological observation/forecast products. Crisis systems own evacuation/rescue state. Roads, Aviation, Water, Agriculture, Power, Care and other owner systems keep their own service state.

## Internal PTU / Caelo cross-check

The project source scan remains the controlling summary of the supplied PTU/Caelo corpus.

Relevant established principles:

- PTU supports central plots, character arcs and sandbox activity in one campaign.
- Caelo supports persistent location identity and can attach concrete mechanical effects to authored locations when a governing source explicitly defines them.
- Location flavor alone does not create a universal tactical mechanic.
- Species, Type, Move, Ability, Item or Trainer Feature effects must come from governing PTU/Caelo material and current implementation evidence.

No project-supplied source inspected for this pass establishes a universal contract for natural volcanic eruptions, ashfall damage, lava-flow simulation, toxic gas exposure, lahars, eruption prediction, seismic precursors, volcanic bombs, heat zones, collapsing crater terrain or automatic Fire/Ground-type immunity.

Accordingly, those remain UNKNOWN unless a future source-specific rule and engine contract verify them.

Internal provenance:
- `research/2026-08-18-source-scan.md`
- `design/geology-excavation-resource-frontier-layer.md`
- `design/weather-forecast-preparedness-operational-extension.md`
- `design/engine-readiness-snapshot-pass-112.md`

## Public Pokémon source: Mt. Chimney

Source:
https://bulbapedia.bulbagarden.net/wiki/Mt._Chimney

Reusable structures:

1. One volcanic site can connect several ordinary systems at once: a town, cable-car access, mountain routes, tunnels, tourism/travel and ash-affected surroundings.
2. Ash can be part of a region's normal visible identity rather than appearing only during a boss event.
3. Access to the summit and access through the mountain are separate routes, so a volcanic site can remain partly usable while another segment is restricted.
4. The anime continuity includes a case where local residents initially blame an Absol for a hot-spring disruption, while investigation reveals a different physical chain involving habitat change and volcanic risk.

Ouros transformation:

- Treat volcanic regions as lived-in places with multiple dependencies, not single-use dungeons.
- Preserve `observation`, `public attribution`, `scientific interpretation` and `actual authored cause` separately.
- A Pokémon repeatedly present before or during unusual activity can become folklore, testimony or an investigation lead without granting the species automatic prediction powers.
- A hot-spring, tourism or route consequence remains owned by its downstream system even when the trigger is volcanic.

Not imported:

- Team Magma/Team Aqua plots;
- Meteorite machinery;
- named characters;
- exact geography or route layout;
- automatic Absol prediction;
- Glalie-caused volcanic rules;
- anime-specific eruption physics;
- any mechanical ash, heat, lava or eruption effect.

## Public Pokémon source: Stark Mountain

Source:
https://bulbapedia.bulbagarden.net/wiki/Stark_Mountain

Reusable structures:

- A volcano can have hardened-lava caverns, fissures and persistent ash cover while still functioning as an explorable location.
- The volcanic identity can be expressed through geology and traversal before any crisis is active.
- A location can remain narratively important across repeat visits because the physical setting itself has persistent character.

Ouros transformation:

Use inactive or background-active volcanic landscapes for exploration, science, pilgrimage, habitats, work and route history. Do not require every volcanic location to be erupting when players arrive.

Not imported:

- Heatran plot or encounter;
- Battle Zone geography;
- item placements;
- dungeon layout;
- mechanical lava behavior.

## Public Pokémon source: Faldera Island / Faldera Volcano

Source:
https://bulbapedia.bulbagarden.net/wiki/Faldera_Island

Reusable structures:

- A volcanic island can sustain a distinct heat-adapted ecological community.
- Cooled magma and active magma can coexist as different landscape states.
- Volcanic geography can shape ordinary habitat identity rather than serving only as a hazard.

Ouros transformation:

A volcanic field may preserve habitat observations and local adaptation history. Species presence must remain ecological evidence, never a universal mechanical immunity or occupational assignment.

Not imported:

- Moltres ownership of the location;
- Ranger mission structure;
- exact island geography;
- capture mechanics;
- heat-tolerance mechanics not supported by PTU/Caelo.

## Public Pokémon dungeon lesson: Mt. Blaze and Giant Volcano

Sources:
https://bulbapedia.bulbagarden.net/wiki/Mt._Blaze
https://bulbapedia.bulbagarden.net/wiki/Giant_Volcano

Reusable structure:

Pokémon Mystery Dungeon repeatedly uses volcanic spaces as multi-stage traversal environments, with route progression, repeated environmental identity and a culminating encounter. The useful design lesson is structural: volcanic exploration can be layered by zones and return-state rather than compressed into one arena.

Ouros transformation:

A volcanic expedition may have staged access such as base settlement, outer field, monitoring route, old flow field, restricted observation sector and summit-adjacent area. Each stage can have separate knowledge, authorization and return-state.

Not imported:

- floor counts;
- random dungeon generation tables;
- traps;
- boss identities;
- lava traversal rules;
- weather floor rules;
- recruitment or item mechanics.

## Public operational source: USGS Volcano Hazards Program

Sources:
https://www.usgs.gov/volcano
https://www.usgs.gov/programs/VHP/what-we-do-volcano-hazards-program
https://www.usgs.gov/programs/VHP/volcano-notifications-deliver-situational-information

Reusable structures:

- Monitoring observations feed interpretation and situational awareness.
- Increased unrest and decreased activity can both generate new notices.
- Monitoring data, direct observations and other evidence can disagree or change over time.
- Notification products can address different audiences and purposes.
- Long-term hazard assessment and short-term activity notifications are separate information products.

Ouros transformation:

Represent observations, interpretations, notices, revisions and actor receipt as separate persistent objects. Do not let one `volcano_alert_level` become hidden universal truth. A region can use qualitative authored states without importing USGS terminology.

Explicit exclusions:

- U.S. institutions;
- real-world alert labels/codes as Ouros canon;
- legal authority;
- instrumentation requirements;
- numerical thresholds;
- evacuation rules;
- real-world response procedures.

## Public operational source: volcanic ash information

Source:
https://www.usgs.gov/programs/VHP/usgs-provides-volcanic-ash-cloud-forecasts-and-ashfall-information

Reusable structures:

- Airborne ash and ground ashfall are related but distinct observations/products.
- Ash consequences can propagate into transport, utilities, water, agriculture and health systems.
- Observations after an event can update situational products.
- Reports of no ashfall can also be meaningful evidence for defining the affected footprint.

Ouros transformation:

Store ashfall observations with location, time, source and confidence/scope. Downstream owners decide consequences. The volcanic layer must not automatically close aviation, contaminate water, damage crops, cause illness or disable power.

Do not import:

- Ash3D;
- real dispersion calculations;
- concentration thresholds;
- health guidance;
- engineering impact thresholds;
- regulatory notices.

## Public operational source: uncertainty and audience separation

Sources:
https://www.usgs.gov/programs/VHP/alert-level-system
https://www.usgs.gov/programs/VHP/alert-level-icons

Reusable structures:

- Unrest can increase while eruption timing remains uncertain.
- Ground consequences and airborne consequences can differ, so one scalar indicator is insufficient for every downstream service.
- Monitoring can be insufficient to characterize a site confidently.

Ouros transformation:

Use explicit dimensions such as `activity_assessment`, `observation_coverage`, `ground_consequence_claims`, `airborne_material_claims` and `confidence`. Do not collapse these to one synthetic severity number.

## PTU community source discovered during this pass

Source:
https://www.deviantart.com/brixmon/art/Pokemon-Tabletop-United-Crystal-Cave-Battle-Arena-677772021

This public PTU arena demonstrates community willingness to stage battles in visually dramatic cave spaces containing water and lava. It is useful only as a design warning and presentation reference: tabletop maps often imply environmental danger visually even when the governing rules for that danger are not shown in the map description.

Ouros consequence:

A lava tile, magma texture, smoke particle, crater edge or glowing fissure may be visually present while remaining inert scenery unless the exact PTU/Caelo rule and engine capability contract for its tactical effect are verified.

No map geometry, art, tiles, encounter, champion premise or tactical rule is copied.

## High-level reusable narrative patterns

### Pattern A — The warning that changes ordinary life

A monitoring site records unusual observations. Different institutions react differently before any eruption occurs. A cable route may reduce service, a research team may delay fieldwork, residents may ignore or discuss the notice, a market may move an event, and a hot-spring operator may keep normal hours.

The story comes from divergent decisions under uncertainty, not from guaranteeing an eruption.

### Pattern B — The footprint is learned afterward

After ashfall or another event, reports arrive from multiple locations at different times. A settlement north of the mountain reports residue. A closer valley reports none. A ferry crew saw a plume but no ground deposit. Later observations refine the footprint.

This supports investigation and provenance without fabricating dispersion physics.

### Pattern C — The blamed Pokémon

A Pokémon changes behavior near the volcanic area. Residents form a causal story. Researchers have incomplete data. The actual world-state cause remains separate until evidence supports it.

Possible outcomes include:
- the behavior was unrelated;
- the Pokémon reacted to a real change through an authored individual capability;
- habitat displacement caused both observations;
- the apparent pattern was coincidence;
- the cause remains unresolved.

Never convert repeated correlation into a species-wide supernatural warning system.

### Pattern D — Recovery does not occur at one time

The active episode ends. Monitoring remains heightened. One route reopens. Another needs inspection. Ash cleanup continues. Water, aviation, agriculture, clinics, tourism and habitat management recover on their own timelines.

The volcanic layer records the event and evidence; owner systems record service restoration.

### Pattern E — Old deposits become social geography

Years later, an old flow boundary or ash deposit may shape a road, neighborhood edge, shrine, farm practice, research station, local story or habitat. The volcanic event remains part of world history even when no active hazard exists.

## Character and faction archetypes transformed for Ouros

Possible NON-CANON roles:

- monitoring-station technician who values continuity of observations over dramatic claims;
- local guide who knows old access routes but does not claim scientific authority;
- hot-spring operator whose business depends on a geological system they do not control;
- agricultural cooperative representative tracking ash cleanup and crop access;
- transport dispatcher deciding service under incomplete information;
- community historian comparing current observations with an older episode;
- habitat steward tracking Pokémon displacement around a changed field;
- skeptical resident who remembers a prior false alarm;
- researcher whose model changed after new evidence;
- public-information officer separating observed facts from unresolved causes.

These roles grant no Skills, Features, authority or bonuses automatically.

## Encounter-design implications

Volcanic concepts are mechanically dangerous to over-author because their intuitive presentation invites unsupported rules.

Any full tactical version that uses active lava, ash obscuration, gas, extreme heat, moving flows, falling ejecta, unstable crater edges, lahars, changing terrain, delayed eruption phases or environmental reactions depends directly on `terrain/weather/hazards/zones/reactions` and often also full damage/status/movement/turn lifecycle.

Reduced versions should move the active geophysical process outside BattleSpec. Let the world-state event finish, isolate the hazardous sector and run combat in a static reviewed area. This preserves the narrative premise without making Minecraft or Narrative invent PTU rules.

## Research status

Provenance: PUBLIC RESEARCH + INTERNAL SOURCE CROSS-CHECK.
Canon status: NONE ADDED.
Proposed setting facts: NONE promoted.
Uncertain mechanical areas: explicitly preserved as UNKNOWN.

## Follow-up questions for future canon review

- Which Ouros regions contain active, dormant or extinct volcanic systems?
- Which communities intentionally live, work, farm, travel or conduct research near them?
- What monitoring technologies exist in each region?
- Which institutions may issue scientific notices, public warnings or access restrictions?
- Are ash collection, geothermal activity, hot springs or volcanic soils economically/culturally important anywhere?
- Which historical eruptions or unrest episodes are established canon?
- Which Pokémon individuals have documented relationships with volcanic sites?
- Does any region possess an authored tradition of reading Pokémon behavior as environmental evidence, and how does that tradition distinguish folklore from verified capability?
