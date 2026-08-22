# Pass 91 Proposals — Lake Limnology, Stratification & Inland-Water Ecology

Status: NON-CANON CANDIDATES. Human review required before promotion.

These seeds use the systems proposed in `design/lake-limnology-stratification-layer.md`. They do not establish PTU mechanics.

## 30 worldbuilding / quest candidates

### 01. The Lake That Looks Fine

The shoreline appears normal and tourism continues, but a deep profiling station records a large seasonal oxygen decline. Players must compare surface, mid-depth and deep observations before deciding whether anything operational should change.

### 02. Three Stations, Three Stories

Three research teams sample different parts of the same lake and publish apparently conflicting summaries. All three may be locally accurate. The real problem is scope and communication.

### 03. Turnover Came Early

A mixing event occurs weeks earlier than the historical baseline. The cause may involve weather, inflow, reservoir operation or an incorrect old baseline.

### 04. The Bloom in One Bay

A visible bloom appears only inside a sheltered bay. Residents blame the entire watershed. Evidence instead points toward a local combination of residence time and inflow history, but the investigation remains open until repeated sampling.

### 05. The Clear-Water Problem

Water clarity improves sharply after a management change, yet one ecological survey detects an unexpected decline in a littoral community. Clearer water is not automatically better for every part of the ecosystem.

### 06. The Missing Deep Survey

A survey vessel completed its route, but one depth profile never uploaded. The issue may be equipment failure, bad timestamping, incorrect station coordinates or a real anomaly that exceeded the sensor range.

### 07. The Old Bathymetric Map

A decades-old depth map is still being used for a seasonal survey. Sediment accumulation and a changed reservoir level mean the map is historically valid but operationally wrong.

### 08. The Night Oxygen Shift

Researchers record different oxygen conditions at night than during daylight. The result creates a new monitoring schedule rather than an immediate crisis.

### 09. The Closed Beach, Open Lake

One shoreline is temporarily closed after a localized water-quality observation. Public rumor turns the notice into “the whole lake is poisoned.” Media and institutions must correct the scope without minimizing the real concern.

### 10. The Surface Gathering

Several aquatic Pokémon repeatedly gather near the surface during a narrow seasonal window. The event is documented first as behavior. Oxygen, temperature, food and social explanations remain separate hypotheses.

### 11. The Deep-Water Absence

A species previously observed at depth is no longer found there, while the same species remains common near shore. The change becomes a limnology/ecology investigation instead of a population-collapse declaration.

### 12. The Spring Below the Lake

A suspected groundwater-fed zone shows a stable temperature signature through changing weather. Researchers need to verify the connection before declaring a spring source.

### 13. The Reservoir Drawdown Year

A planned drawdown exposes old shoreline, changes littoral access and forces surveys to use a different bathymetric revision. Submerged structures become visible without automatically becoming loot sites.

### 14. The Bloom That Wasn't Toxic

A visually dramatic bloom causes panic, but samples do not support the feared toxin. The event still matters because it reveals a different ecological imbalance.

### 15. The Quiet Inflow

A tributary that normally creates a visible mixing plume enters the lake with almost no contrast. The investigation reveals a change in temperature or flow rather than a blockage.

### 16. The Ferry Captain's Depth Log

A ferry captain has informal notes about water color, floating material and fish activity spanning twenty years. The records are not scientific measurements, but they provide high-value observation history when properly tagged as such.

### 17. The School Buoy Project

A local school maintains a simple monitoring buoy. One year's data looks strange because the instrument drifted. Students help discover the error and improve the long-term record.

### 18. The Old Partner at the Littoral Shelf

A released former partner is photographed repeatedly near the same shallow shelf over multiple seasons. The system records sightings and identity confidence without inferring motive, ownership or desire to rejoin the Trainer.

### 19. The Inflow After the Fire

Months after a wildfire, the first major rain delivers sediment and ash into one part of the lake. The lake response is monitored over time rather than converted into instant contamination damage.

### 20. The Festival on Turnover Week

A large lakeside festival overlaps with an expected seasonal mixing window. The issue is coordination among tourism, monitoring, fisheries and public communication, not necessarily cancellation.

### 21. The Bottom-Water Mystery

A deep sensor records near-zero oxygen for several weeks, but a neighboring station does not. Players must determine whether basin shape, sensor position or real spatial heterogeneity explains the difference.

### 22. The Littoral Restoration Year Three

A restored shallow shelf looks visually successful. Follow-up surveys show that plant structure improved while Pokémon use remains different from the original baseline.

### 23. The Lake With Two Seasons

A deep basin remains stratified while a shallow connected basin mixes frequently. Residents refer to them as one lake; researchers need two internal models.

### 24. The Archived Bloom Photographs

Old photographs show repeated surface discoloration decades before formal monitoring began. The images establish historical occurrence but do not reveal organism identity or toxicity.

### 25. The Intake Depth Debate

A settlement's water intake draws from a depth that becomes problematic during part of the year. Engineering, public health and ecology groups disagree about the best long-term response.

### 26. The Fishing Reports That Changed First

Anglers report a shift in where catches occur before instruments show a clear trend. Their observations become evidence, not proof, and trigger targeted profiling.

### 27. The Lake That Never Fully Mixes

Long-term records suggest a deep basin has not fully mixed for several years. The discovery creates a multi-season research arc rather than an immediate disaster.

### 28. The Wrong Cause in the Newspaper

A newspaper correctly reports a bloom but attributes it to the newest upstream project before the source investigation finishes. A later correction changes public memory but does not erase the original article.

### 29. The Winter Profile

Under ice or winter surface conditions, a monitoring team finds a depth profile different from what local staff expected. The correct response may be “update the baseline,” not “find the culprit.”

### 30. The Lake Atlas

Several institutions combine bathymetry, water-column profiles, littoral surveys, fisheries observations, oral history and public photographs into a versioned lake atlas. Each edition records what was known at the time.

## Three longer arcs

### Arc A — Five Turnovers at Mirror Lake

Year 1 establishes baseline temperature and oxygen profiles.

Year 2 produces an unusually early mixing event.

Year 3 includes an upstream restoration project and a changed inflow signature.

Year 4 produces a localized bloom that becomes a public controversy.

Year 5 reveals that one long-standing assumption about the deepest basin was based on an outdated bathymetric map.

The arc has no required villain. Its payoff is accumulated knowledge, better institutions and a lake that feels older than the current quest.

### Arc B — The Two-Basin Problem

A single named lake consists of a shallow urban basin and a deeper natural basin connected by a narrow channel.

Different mixing regimes, tourism pressure, fisheries use and public narratives evolve over several seasons. Players gradually learn that policies appropriate for one basin can be wrong for the other.

The arc can involve science, tourism, governance, fishing, conservation and infrastructure without forcing all of them into one faction conflict.

### Arc C — What Came Downstream

An upstream event begins outside the lake layer: wildfire, stormwater problem, agricultural change or infrastructure failure.

The lake receives a measurable input later.

Months after that, deep-water oxygen, transparency or ecological observations change.

The narrative challenge is reconstructing causality across time and systems while leaving room for unrelated concurrent changes.

## Encounter contracts

### Deep Station Recovery

Full version:
The party travels to a deep profiling station, secures failed equipment and handles any wild encounter while keeping research gear intact. A future full implementation could include moving platforms, depth context, withdrawal objectives and legal environmental effects.

Reduced version:
Boat position, equipment recovery and wildlife displacement resolve in overworld state. AutoPTU receives a fixed platform or shoreline arena if a battle occurs.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED for static geometry;
- base movement legality: VERIFIED;
- complete movement including forced movement/interception: BLOCKING for moving platforms/currents;
- core calculations: VERIFIED for existing legal mechanics;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

### Littoral Bloom Survey

Full version:
Researchers sample several shoreline points while the party keeps the area safe. Any toxicity or environmental effect must come from validated mechanics, not the bloom label.

Reduced version:
Sampling, civilians and bloom state remain outside battle. Any encounter is a standard static shoreline battle with no bloom-derived PTU effect.

Primary blockers:
- terrain/weather/hazards/zones/reactions;
- complete movement if water edge changes;
- AI tactical policy for PROTECT_RESEARCHER / WITHDRAW;
- adapter/playback.

### Turnover Night Survey

Full version:
A timed multi-station survey runs during a narrow mixing window. A future version may support sequential tactical scenes whose environment snapshot differs by station and time.

Reduced version:
Timing and travel are overworld state. Each optional battle is resolved independently using a frozen arena.

Primary blockers:
- full lifecycle remains PARTIAL;
- environment family remains BLOCKING;
- AI tactical policy remains BLOCKING;
- adapter/playback remains BLOCKING.

## Canon-review questions

Before promoting any candidate:

- Which lakes exist in Ouros at campaign start?
- Which are natural versus reservoirs?
- Which have deep stratified basins?
- Which institutions monitor them?
- Which local Pokémon associations are authored canon?
- Which historical lake events are already known publicly?
- What access, fishing and boating norms exist?
- Which lakes carry mythic/cultural significance?
- What information is considered public versus sensitive?

## Mechanical review questions

- Exact PTU/Caelo Swim and underwater rules.
- Any rules for drowning, suffocation, deep water or visibility.
- Whether freshwater environment labels affect any Moves beyond verified move-specific cases.
- Whether Caelo changes water encounter or terrain handling.
- Which Java field-state contracts eventually support water-specific effects.
- Whether tactical lake encounters should stay as frozen 2D snapshots rather than attempt 3D depth simulation.
