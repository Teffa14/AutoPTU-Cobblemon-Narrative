# Pass 149 Proposals — Settlement Demography, Residency & Population Change

Status: NON-CANON CANDIDATES. Requires authored approval before promotion.

## 30 reusable seeds

1. **The Town Is Full, the Homes Are Not** — A regional tournament doubles the present population for nine days. Water, transit and lodging feel stressed, but the usual-resident count barely changes.
2. **Five Addresses, One Resident** — A field researcher spends months rotating through lodges and stations while maintaining one usual residence. Several institutional databases incorrectly count five separate moves.
3. **The Empty District That Is Not Abandoned** — Most residents work seasonal jobs elsewhere for part of the year. A visitor interprets the quiet streets as permanent decline.
4. **The Evacuation Lasted a Winter** — Flood evacuees live in another settlement for months. Some return, some relocate, and some remain undecided long after the floodwater is gone.
5. **The Census Missed the Ferry Crew** — A settlement survey was conducted while a large share of regular residents were working offshore. The later revision changes the estimate without changing the historical survey record.
6. **The New Dormitory Problem** — A research institute opens large residential quarters. Population rises slowly because the building is ready before staff recruitment is complete.
7. **The Festival That Looks Like Growth** — Shops report record traffic and streets are crowded, but the surge is almost entirely temporary visitors.
8. **The School Closed, the Families Did Not All Leave** — An institutional closure changes travel patterns before it changes residence patterns.
9. **The Return Program Has Three Outcomes** — After a wildfire, one household returns, another rebuilds elsewhere, and a third keeps temporary accommodation while deciding.
10. **Two Counts, Both Correct** — One estimate uses the old municipal boundary and another uses the expanded one. The disagreement is geographic, not fraudulent.
11. **The Worker Camp Became a Neighborhood** — Temporary quarters used during a five-year infrastructure project gradually gain permanent services. The transition happens through many individual residence episodes, not one settlement flag.
12. **The Neighborhood Lost Population but Gained Foot Traffic** — Residents move outward while a new rail station turns the area into a daytime hub.
13. **The Hospital Census** — A clinic’s overnight patient count is accidentally reused as a resident count in a local report. The patients were physically present but mostly lived elsewhere.
14. **The Seasonal Market Quarter** — Merchant families return for the same months every year. Ouros can remember the recurring presence without deciding that each arrival is a permanent migration.
15. **The Route Diversion Town** — A bridge failure strands hundreds of travelers for a week. Service pressure spikes, but residence remains unchanged.
16. **The House With No Current Resident** — A maintained family home remains physically intact while its usual resident lives elsewhere for several years. Homes and Demography disagree only if their states are collapsed.
17. **The Resident Without a Private Home** — A long-term resident uses institutional quarters. Residence does not require property ownership or a private dwelling.
18. **The Famous Population Number** — A century-old guidebook’s exact number becomes part of local identity even though modern methodology suggests it was only a rough estimate.
19. **The Missing Ten Percent** — A survey has unusually low coverage in one district. The correct conclusion is uncertainty, not sudden depopulation.
20. **The New Ferry Changed Where People Sleep** — Better transport lets workers move their usual residence farther from their workplace over several years.
21. **The Research Boom Ends Quietly** — A temporary influx leaves when a major study concludes. Empty rentals increase, but no crisis or antagonist caused it.
22. **The Pokémon Center Expansion** — A service facility adds staff and lodging. Its daily population grows before the surrounding settlement does.
23. **The Old Mining Quarter Reopens** — A former worker district gains residents again after a different industry moves in. The same buildings acquire a new demographic history without erasing the old one.
24. **The Staged Return** — Only one flood-safe district reopens at first. Return occurs street by street over months rather than through one world-state reset.
25. **The Survey That Changed Method** — A new methodology produces a different estimate from last year. Chronicle records both the method change and the number instead of treating the difference as literal movement.
26. **The Last Resident Did Not Leave** — A rumor calls a hamlet abandoned, but one household still uses it as usual residence while several others visit seasonally.
27. **The Temporary Camp Outlived the Emergency** — Relief housing remains occupied after the original incident ends because reconstruction is slower than incident response.
28. **The Return Visit Mistake** — A former resident visits for a festival and is incorrectly marked as having moved back.
29. **The Population Atlas With Transparent Pages** — A museum overlays settlement estimates, boundaries and major institutions from several eras so visitors can see that growth was spatially uneven.
30. **Nothing Happened This Year** — Population, services and movement stay within ordinary variation. Years later this quiet baseline becomes necessary to interpret a real change.

## Long arc A — Five Censuses of Meridian Ward

Year 1 establishes a coarse resident estimate and documents weak survey coverage in one block. Year 2 brings a university annex and temporary workers. Year 3 a transit upgrade changes where workers live without changing where they work. Year 4 an emergency displaces one section of the ward. Year 5 uses a better method and revised boundary.

The arc works because every published estimate can remain historically valid for its method and geography. No mastermind is required. The reward is a settlement whose population history explains why transport, schools, markets, public space and housing feel different after several years.

## Long arc B — The Town That Moved Without Moving

A remote settlement keeps the same buildings and name while its usual-resident population gradually shifts between generations. Seasonal workers increase, older institutions close, a ferry improves access, a research station becomes permanent and several former residents return only part of the year.

The physical town changes slowly. Its demographic function changes quickly. This allows Chronicle to make a familiar map feel historically different without rebuilding everything.

## Long arc C — Return Years

A major flood causes a genuine displacement episode. Emergency shelter is handled by Crisis/Lodging. Demography tracks who remains temporarily elsewhere, who returns, who relocates and which outcomes remain unknown. Architecture and Public Works decide what can reopen. Five years later the former evacuation camp may itself have become ordinary housing.

The arc must not force every displaced actor back “home.” Permanent relocation, return, split residence if canon permits it, and unresolved plans are all legitimate outcomes.

## Encounter contract 1 — Return Day at Riverside

Narrative premise: a staged return is underway after a flood. A small wild-Pokémon conflict blocks one already-cleared access route while residents are still outside the tactical area.

FULL version dependencies:
- `complete movement including push/pull/knockback/interception/forced movement` if returnees/responders must cross or withdraw dynamically;
- `AI tactical policy` for `CLEAR_ROUTE`, `WITHDRAW`, `PROTECT_RESPONDER` or `REACH_EXIT` objectives;
- `Minecraft/Cobblemon/Craftics adapter/playback` for civilians, route state and semantic objectives;
- `terrain/weather/hazards/zones/reactions` only if flood debris, unstable water or another environmental condition becomes tactically active.

REDUCED version: world state pauses civilian return, responders clear the perimeter and the battle starts on a dry static arena. After AutoPTU resolves combat, Public Works/Crisis decide whether the route can reopen and Demography records only the subsequent return state. Winning never marks residents as returned automatically.

## Encounter contract 2 — Seasonal Arrival at North Depot

Narrative premise: a scheduled seasonal workforce and visitors arrive during a local wildlife disturbance. The demographic issue is temporary presence, not migration.

FULL version dependencies:
- `complete movement` for passengers/wildlife moving through the depot;
- `AI tactical policy` for `EVACUATE`, `WITHDRAW`, `CLEAR_PLATFORM`, `REACH_EXIT`;
- `Minecraft/Cobblemon/Craftics adapter/playback` for crowds and transport state.

REDUCED version: Rail/Road Transit unloads or redirects passengers outside the battle grid. AutoPTU receives a static encounter with the actual combatants. The temporary-population episode remains unchanged by battle results.

## Encounter contract 3 — Census Route Through a Changing Settlement

Primarily non-combat. Surveyors compare building use, voluntary survey responses and administrative records while several blocks have changed function since the previous estimate.

If an unrelated battle occurs, resolve it as a conventional static AutoPTU encounter after surveyors/civilians are removed. A battle cannot determine residence, population count, survey validity or actor intent.

## Mechanical non-inferences

Do not add population-based morale, crowd bonuses, resident-only stats, migration bonuses, displacement Status, wild spawn rates, household Features or demographic Skill checks. Any combat mechanic must come from verified PTU/Caelo rules and the engine capability that implements it.