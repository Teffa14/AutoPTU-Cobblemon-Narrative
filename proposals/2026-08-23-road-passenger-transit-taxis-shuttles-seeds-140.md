# Ouros Road Passenger Transit, Taxis & Shuttles — Seeds 140

Status: NON-CANON PROPOSALS.
Date: 2026-08-23

These concepts use the Pass 140 road-passenger-transit layer. They are candidates only.

## 30 worldbuilding and quest seeds

1. The Bus That Still Comes

A low-demand route continues serving one old hill district because several residents depend on it. The mystery is why ridership records look almost empty while drivers insist the route matters. The answer can be ordinary: several riders board at uninstrumented stops.

2. Three Taxis, One Street Closure

Three drivers choose different detours around the same closure. All are legal. Their arrival times differ enough that witnesses later remember an incident in different orders.

3. The Stop Moved Across the Road

A temporary relocation made during construction becomes semi-permanent. Old maps, current signs and passenger habits now point to three different boarding locations.

4. The Shuttle That Bunches

Two frequent shuttles repeatedly arrive together. The cause is not laziness: one busy stop creates uneven dwell time that propagates through the route.

5. Last Ride Before the Festival

A road closes for a procession at a known time. Players can ride the final normal service, wait for a replacement route or walk through a different district.

6. The Gogoat Service Rests Today

A Pokémon-assisted shuttle pauses because one recurring partner is unavailable. The institution runs a smaller replacement instead. No emergency and no villain are required.

7. The Accessible Stop Is Closed

The route still operates, but the temporary boarding point removes a previously viable access path for one traveler. Accessibility state becomes a routing problem rather than a personal medical exposition.

8. The Driver Who Knows the Old City

A veteran taxi driver remembers prior street layouts, former landmarks and old names. Their recollections can help Archives or Cartography, but memory remains evidence rather than automatic truth.

9. The Empty Bus Was Full Earlier

A player sees an almost empty vehicle and assumes low demand. Service records show it had to pass waiting passengers earlier because bunching shifted the load to the previous trip.

10. The Route Everyone Calls Public

A shuttle has used a courtyard shortcut for years. Land Tenure later reveals the passage came from a revocable agreement, not a permanent public right.

11. The Morning Driver Never Saw It

Two drivers on the same route report different wildlife because Diel Activity and work shifts expose them to different time windows.

12. The Taxi Rank After Rain

Stormwater temporarily floods the usual rank. Service continues from another street, creating confusion because vehicles are operating while the official pickup point is unusable.

13. The Replacement Route Becomes Popular

A temporary detour unexpectedly serves a neighborhood better. After the original road reopens, residents ask for part of the temporary pattern to remain.

14. The Missed Research Window

A delayed bus causes a team to miss a tide, migration or bloom observation window. The scientific consequence persists even though nothing dramatic happened during the ride.

15. The Vehicle With Two Histories

A transit vehicle retired from city service becomes a mobile library, clinic shuttle or community artifact. Its `vehicle_id` persists while institutional role changes.

16. The Wrong Bus in the Photograph

A historical photo is dated from route livery. Later research shows that paint scheme continued on one reserve vehicle longer than expected.

17. The Market Crowd Is a Transfer Crowd

An apparent tourism surge is mostly passengers waiting for a disrupted cross-town connection. Demography should not count them as new residents or even destination visitors.

18. The Driver Is Not the Owner

A taxi operator, vehicle owner and dispatch cooperative are three separate actors. A dispute becomes understandable only after those roles are separated.

19. The Fare System Is Down, the Buses Are Not

Payment terminals fail. The operator invokes a fallback rule and keeps service moving. Payments later reconciles rides rather than freezing transit because accounting is delayed.

20. The Route With No Timetable

A high-frequency circulator is managed by spacing rather than exact departure times. Visitors keep asking why the posted schedule lists only an operating window.

21. The Bus That Waited

A dispatcher holds a rural bus for a late ferry connection. Most passengers arrive later, but several avoid being stranded overnight. A later review debates whether the hold was worthwhile.

22. The School Route in Summer

An institutional route disappears during school break, leaving residents who had informally relied on it without realizing its primary purpose.

23. The Stop Used by One Pokémon

A wild Pokémon repeatedly shelters near a stop. Urban Wildlife tracks the behavior; Transit only records that maintenance crews keep observing it there.

24. The Driver Who Retired, the Route That Did Not

Passengers associated a long-running service with one person. Their retirement changes public memory while the institution continues with a new operator.

25. The Rural Request Window

A demand-responsive shuttle groups several trip requests into one run. The system must preserve request windows and actual assignment without simulating a routing optimizer.

26. The First Night Bus

A city adds late service after years of nightlife growth. Light, Public Space, Lodging and Workplaces all change around the new option over time.

27. The Pass-Up Nobody Logged

Several riders report being left behind by a full vehicle, but the official system only records completed trips. The issue is missing operational detail, not necessarily misconduct.

28. The Route That Crosses Three Jurisdictions

The same service passes through areas maintained by different institutions. One road closure creates conflicting notices because each authority updates its own segment first.

29. Nothing Happened on Route 7

A full week of uneventful service creates useful baseline history. The route should be allowed to function without generating content every day.

30. The Transit Atlas

A long-running archive overlays route revisions, stop moves, service suspensions, working-Pokémon assignments, accessibility projects and district growth over decades.

## Long arc A — Five Years on Meridian Loop

Year 1: Meridian Loop operates as a basic circular shuttle.

Year 2: a redevelopment closes two streets and creates a temporary detour.

Year 3: the detour proves useful to a growing district; one temporary stop becomes permanent.

Year 4: demand increases enough that bunching and pass-ups appear despite more scheduled service.

Year 5: the operator restructures the route into two overlapping patterns and preserves the old Loop name only as public branding.

This arc can intersect Public Space, Demography, Accessibility, Road Ecology, Payments, Working Pokémon and Public Memory without requiring a villain.

## Long arc B — The Last Gogoat Shuttle

A corridor historically used a small Pokémon-assisted passenger service.

Over several years:

- one veteran Pokémon retires from regular duty;
- replacement coverage changes the schedule;
- an accessibility retrofit modifies boarding platforms;
- a new rail station reduces some trips but increases feeder demand;
- the service may survive as a shorter neighborhood circulator rather than disappear.

The point is institutional adaptation. Retirement of a Pokémon partner does not imply death, abandonment or ownership transfer.

## Long arc C — The Road Before the Bus

A rural road first supports irregular private rides, then an institutional weekly shuttle, later a fixed service after a research station expands.

Years later, population stabilizes and the route returns to lower frequency. The service history becomes evidence for Demography, Land Tenure, Road Ecology and regional planning.

## Encounter contract 1 — Transit Hub Evacuation

Narrative premise:

A disruption at a busy interchange requires passengers to clear a boarding concourse while a separate confrontation develops nearby.

FULL version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for live passenger evacuation, interception and moving protected actors;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if exact effects are used;
- terrain/weather/hazards/zones/reactions — BLOCKING if the disruption itself becomes tactically hazardous;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `EVACUATE`, `CLEAR_ROUTE`, `PROTECT_PASSENGER`, `REACH_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:

Transit state stops boarding and evacuates all passengers before battle. Vehicles are frozen outside the tactical arena. AutoPTU receives only actual combatants in a static legal space. Service recovery happens afterward.

## Encounter contract 2 — Last Shuttle Through the Detour

Narrative premise:

A shuttle must reach a safe transfer point before a planned closure takes effect. A conflict intersects the route.

FULL version dependencies:

Primary blockers:

- complete movement for moving service assets and interception;
- AI tactical policy for `REACH_DESTINATION`, `PROTECT_ROUTE`, `WITHDRAW`;
- adapter/playback;
- terrain/weather/hazards/zones/reactions only if an exact environmental hazard becomes tactical.

REDUCED version:

World state halts the shuttle at a safe point. Passengers disembark and continue through an alternate plan. Any confrontation is resolved in a static arena. Victory does not drive the vehicle or reopen the road.

## Encounter contract 3 — Taxi Rank Wildlife Spillover

Narrative premise:

Urban wildlife begins using a temporarily quiet taxi rank after a nearby road closure. Service restoration creates a coexistence problem.

FULL version dependencies:

- complete movement for live wildlife withdrawal and passenger flows;
- AI tactical policy for `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_WILDLIFE`;
- adapter/playback;
- environmental family only if a validated road or weather hazard is present.

REDUCED version:

Urban Wildlife resolves most movement before battle. Transit relocates pickup operations temporarily. If a battle still occurs, AutoPTU receives a static subset of combatants. Restoring service does not prove the ecological issue is solved.

## Canon questions

- Which Ouros cities have taxis, fixed-route buses, shuttles or demand-responsive services?
- Which services use ordinary vehicles, Pokémon partners or both?
- Who operates them?
- Which are public-facing institutions versus private businesses?
- How exact should schedules and fares be?
- Can player organizations create routes?
- How does accessible boarding work across different settlement architectures?
- Can a transit vehicle ever remain inside a live battle space?
- Which PTU/Caelo rules govern any Pokémon-assisted passenger carrying?
