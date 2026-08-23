# Ouros Candidates — Emergency Services, Dispatch & Incident Coordination — Pass 121

Status: NON-CANON proposals. Requires review before promotion.

## 30 candidates

1. The Call That Was Correct for the Wrong Reason — a resident reports smoke; the visible plume is harmless steam, but responders discover a separate electrical fault nearby.
2. Two Fires, One Brigade — a trained local unit is already committed when a second incident appears, forcing mutual aid rather than escalation-by-villain.
3. The Unit That Never Left — dispatch records say a rescue unit was assigned, but a maintenance lockout prevented departure; the error is discovered during after-action review.
4. The Silent Repeater — a hilltop relay fails during a storm and a neighboring service becomes the temporary communications bridge.
5. The Wrong Entrance — an old facility map sends responders to a sealed gate while workers know a newer access route.
6. The Wartortle Retirement — a long-serving responder Pokémon stops participating; the service must adapt staffing without treating the Pokémon as replaceable equipment.
7. Mutual Aid at Cedar Pass — two settlements keep separate services but share one mountain rescue agreement during winter closures.
8. The Drill That Found the Real Leak — a planned exercise exposes an actual infrastructure problem before any emergency occurs.
9. The Staging Lot Became a Market — a former emergency staging area gradually acquires normal civic uses, creating future conflicts when it must be reactivated.
10. The Fire Station Archive — decades of response logs reveal how a district’s risk profile changed as roads, buildings and ecology changed.
11. Three Reports, One Incident — calls from different neighborhoods describe incompatible symptoms that are eventually traced to the same infrastructure failure.
12. One Report, Three Incidents — what appears to be a single crisis turns out to involve unrelated events sharing a location and time window.
13. The Bridge Unit Is Across the River — route geometry, not lack of personnel, causes the delayed response.
14. The Closed Station That Still Matters — a decommissioned station remains the best emergency cache location and landmark.
15. The Responder Pokémon Chooses Another Route — an institutional Pokémon repeatedly avoids one tunnel; investigation treats the behavior as evidence, not proof.
16. The Last Working Radio — an older device becomes temporarily important because newer infrastructure depends on a failed network.
17. The Handoff Nobody Logged — a rescued Pokémon reached care safely, but custody documentation was never completed.
18. The Ambulance Without a Road — the receiving clinic has capacity, but flood damage removes the normal route and forces transport planning.
19. The Festival Drill Pays Off — an evacuation rehearsal performed months earlier changes the options during a real crowd incident.
20. The Night Shift Knows the Alarm — overnight workers recognize that a recurring alert is abnormal before central dispatch does.
21. False Alarm, Real Readiness Problem — an alarm proves benign, but responders discover their maps and equipment caches are outdated.
22. The Mutual-Aid Team Speaks Different Procedure — two competent services use different terminology and must build an interoperable protocol over several incidents.
23. The Unit Returned Too Early — demobilization releases a team before a secondary impact becomes visible; the decision was reasonable based on known facts.
24. The Missing Responder — a responder fails to check in after a routine survey, turning the service itself into the subject of a search.
25. The Station Pokémon Is Famous — visitors treat a responder Pokémon as a mascot while staff preserve its work/rest boundaries and agency.
26. The Emergency Cache Was Used Yesterday — a second incident exposes how quickly supposedly redundant supplies can disappear.
27. The Route Is Safe for Trucks, Not Evacuees — access is technically open but unsuitable for the people or Pokémon who need to move through it.
28. The Dispatch Board From Twenty Years Ago — an archived board becomes evidence for historical settlement growth and former station coverage.
29. The Quiet Year — almost no major incidents occur, so the service focuses on drills, maintenance, maps and interagency exercises rather than receiving filler crises.
30. The Same Bell Means Something Else Now — an old public warning signal remains in use after the original hazard disappeared, accumulating a new civic meaning.

## Long arc: Five Seasons at Meridian Rescue District

Year 1: a routine storm reveals poor radio coverage.
Year 2: a new repeater improves one valley but creates maintenance obligations.
Year 3: a simultaneous bridge collapse and wildfire forces the first major mutual-aid activation.
Year 4: an after-action review changes staging and map practices.
Year 5: a quieter season tests whether the institution preserves lessons without needing another catastrophe.

The arc is about institutional memory and changing geography, not escalating villains.

## Long arc: The Unit With Three Generations

A response team begins with one veteran Trainer-Pokémon partnership. Over years the Trainer retires, the Pokémon changes its own participation, new members arrive and the unit’s public reputation outlives its original roster. The service identity persists without making any individual permanently obligated.

## Long arc: The Dispatch Atlas

Several settlements gradually combine route maps, station coverage, seasonal hazards, hospital access and communications dead zones into a regional dispatch atlas. Old editions remain useful historical evidence. A future crisis tests whether the atlas is treated as a living model rather than perfect truth.

## Encounter contract: Station Access Fire

FULL version:
A fire or other validated hazard blocks part of a station while responders and equipment must move through a protected route. Some actors withdraw while a small number of combatants create a separate tactical threat.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for moving responders/protected routes
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING for any actual fire/smoke/hazard behavior
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for WITHDRAW/PROTECT/CLEAR_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:
The world layer evacuates responders, secures equipment and freezes a safe tactical room. The hazard remains narrative/world state. AutoPTU resolves only the conventional combat encounter. Afterwards Crisis and Emergency Services re-evaluate whether the station can operate.

## Encounter contract: Mountain Rescue Handoff

FULL version:
A recovered actor must be transferred from field team to transport team while wild Pokémon or another tactical threat occupies the route.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for escort/handoff movement
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if snow, cliff, wind or other hazards are tactical
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for REACH_OBJECTIVE/WITHDRAW/PROTECT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:
The rescue, medical stabilization and patient movement occur in overworld state. The handoff is paused while a separate static encounter is resolved nearby. Care/Transport completes the transfer after the path is safe. Battle victory never equals patient stabilization.

## Encounter contract: Mutual-Aid Chokepoint

FULL version:
Two independent services approach the same incident through a narrow route while civilians and wild Pokémon must leave in the opposite direction.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if the incident has validated tactical environment effects
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for CLEAR_ROUTE/WITHDRAW/PROTECT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:
Dispatch coordinates arrival order and civilians/wildlife clear the chokepoint in world state. The two services keep separate authority. If a battle remains, AutoPTU receives a conventional static map and only actual combatants.