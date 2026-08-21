# Ouros Volcanism & Geothermal Seeds — Pass 66

Status: NON-CANON proposals. Original Ouros material derived from high-level research patterns.

## 1. The Spring That Cooled First

A mountain town notices that one public bath cools days before any monitoring station reports unusual activity. The first task is to determine whether the cause is plumbing, groundwater diversion, instrument error or a real geothermal change.

## 2. Three Quiet Vents

Three mapped vents have shown no visible activity for decades, but only two are covered by the monitoring network. A proposed trail crosses the unsurveyed sector.

## 3. The Old Cable Car

A summit cable car is culturally important and still useful, but repeated closures make its future uncertain. The story can become infrastructure renewal, tourism adaptation or a debate about retiring it.

## 4. Ash Without an Eruption

A town reports fresh ash on roofs while the observatory reports no new eruption. Investigation finds older deposits being resuspended under unusual wind conditions.

## 5. The Warm Tunnel Census

Researchers compare Pokémon use of naturally warm tunnels over several years. A shift in occupancy may reflect geothermal change, visitor pressure, construction or normal population movement.

## 6. Observatory Blind Spot

A key station fails during otherwise mild unrest. The crisis is not that eruption is certain; it is that confidence drops exactly when decisions become harder.

## 7. The Wrong Volcano

Residents blame the nearest cone for sulfur smells. Measurements suggest the source is a smaller geothermal field farther down the valley.

## 8. Springkeeper's Ledger

A bathhouse has hand-written temperature and flow records spanning generations. The records are imprecise but reveal patterns absent from the modern instrument archive.

## 9. The New Fumarole

A new steaming opening appears beside a popular trail. The content centers on access, mapping, monitoring and visitor behavior rather than an immediate eruption.

## 10. The Cooling District

A settlement uses geothermal heat for several public buildings. A slow decline in output forces staged decisions about backup systems, not a single repair quest.

## 11. Ash on the Orchard

A light deposit reaches agricultural land after a distant eruptive episode. Farmers, scientists and health staff disagree about what should happen next because the long-term effect is still uncertain.

## 12. The Second Summit Map

Two official summit maps disagree because the vent layout changed after a historic event. Both maps were accurate when published.

## 13. Under the Spa

Renovation of a famous hot-spring facility exposes older channels and sealed structures. Archaeology, geology and infrastructure now share the same physical site.

## 14. The Fire-Type Scapegoat, Again

A cluster of Fire-type Pokémon is blamed for unusually hot ground. Their presence may instead be a response to the same geothermal change affecting the town.

## 15. The School Observatory

A small educational station produces an anomalous reading. It may be calibration error, a local effect or the first observation of a wider change.

## 16. The Evacuated Island Returns

A volcanic island closed after an old crisis has been quiet for years. Reopening requires updated mapping, habitat surveys, infrastructure checks and institutional confidence.

## 17. Steam Below the Bridge

A road bridge crosses a geothermal drainage. New steam vents appear after heavy rain, connecting Hydrology and Volcanism without assuming a magma event.

## 18. The Tourist Alert

A popular travel guide continues to call a summit trail “safe year-round” after a new access assessment. Communications and Tourism must propagate the correction.

## 19. The Observatory Rivalry

Two research teams use different models and issue different interpretations from the same measurements. Neither is dishonest.

## 20. The Buried Station

Ash from an old event covered a monitoring station that was never recovered. Decades later, construction exposes its sealed archive.

## 21. The Red Night That Wasn't

A striking red sky causes rumors of eruption. Meteorology explains the optical effect, but the rumor itself still affects tourism and emergency calls.

## 22. Spring Closure Season

A geothermal pool used by wild Pokémon and tourists needs a temporary closure after a chemistry shift. The closure is precautionary, not proof that anyone is ill.

## 23. The Lahar Route

An old deposit corridor has not activated in living memory. A new road proposal crosses it, forcing governance to weigh low-frequency risk against present access needs.

## 24. The Cooled Lava Garden

A decades-old lava flow has become a distinctive habitat and research site. A proposal to quarry part of it creates a conflict among geology, ecology and local development.

## 25. A Vent Under the Warehouse

A warehouse district discovers rising ground temperatures. The answer may be a utility fault, an old geothermal channel or real subsurface change.

## 26. The Lost Warning Bell

An old community used a physical warning system before modern communications. The object survives, but nobody agrees exactly what conditions once triggered it.

## 27. The Hot River Kilometer

One reach of a river becomes warmer than its neighbors. Freshwater observations and geothermal monitoring must be compared before anyone claims a cause.

## 28. The No-Eruption Year

A season of elevated unrest ends with no eruption. The arc focuses on what institutions learn from preparedness that turned out not to be needed.

## 29. Observatory Pokémon

A recurring wild Pokémon appears near monitoring equipment during certain activity windows. Researchers document the association without assuming predictive ability.

## 30. The Long Quiet

A volcano has shown no major event for generations. The story follows how a region keeps knowledge, infrastructure and preparedness alive without turning every year into a scare.

# Longer arcs

## The Mountain That Breathes

Over several world-years, a volcanic system cycles through background activity, mild unrest, a hydrothermal event, declining activity and a later eruptive episode. The important continuity comes from monitoring records, spring behavior, route policy, residents, staff turnover and recovery. Earlier player decisions about sensors, alternate roads and public communication directly change later options.

## The Geothermal Town

A small settlement gradually builds its identity around hot water, research, clinics, hospitality and low-scale geothermal infrastructure. A long decline in spring output exposes how many institutions depend on one natural system. The final outcome may be adaptation rather than restoration to the old state.

## Ash Years

A moderate eruptive episode ends early in the arc. The remaining story follows ash cleanup, water monitoring, agriculture, visitor pressure, resuspended dust, archived observations, ecological succession and rebuilding. Several later problems originate from the same event without being the same quest.

# Encounter contracts

## Observatory Evacuation

Full version:

Staff and instruments occupy the map while access deteriorates. Players protect a withdrawal route, recover selected records and decide when to stop trying to save equipment.

Dependencies:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

Evacuate staff and choose records in world state first. Freeze a safe static summit platform. Ash, steam, gas and falling material remain visual or absent from battle mechanics. Open a standard encounter only if a real confrontation remains.

## Geothermal Intake Failure

Full version:

A service chamber contains changing steam vents, controllable valves and Pokémon moving between safe sectors.

Key blockers:

- terrain/weather/hazards/zones/reactions;
- complete movement if displacement or moving safe areas exist;
- AI tactical policy for avoid-zone/withdraw behavior;
- adapter/playback for machinery and environmental state.

Reduced version:

Resolve machinery, spring flow and access state outside combat. If combat occurs, use one fixed dry platform. Restoring service is a world-state action after the encounter.

## Ashfall Pass Reopening

Full version:

The party advances across a deposit field while wind, visibility, route stability and wild withdrawal behavior change over time.

Key blockers:

- terrain/weather/hazards/zones/reactions;
- complete movement for displacement/interception;
- full lifecycle for changing conditions;
- tactical AI for route/withdraw goals;
- adapter/playback.

Reduced version:

Survey the route first. Pick one validated stable segment as fixed geometry. Run a conventional battle only if needed. The ash itself has no tactical effect until an exact rule is validated.