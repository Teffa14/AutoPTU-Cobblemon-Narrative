# Candidate Seeds — Fisheries Stock Assessment, Effort & Release Monitoring — Pass 157

Status: PROPOSED / NON-CANON. Extension of Pass 70 Fisheries authority.
Date: 2026-08-24

These concepts focus on evidence quality, monitoring, assessment revision and scoped management. They do not replace the broader fisheries, angling and aquaculture concepts already authored in Pass 70.

## 30 candidates

1. The Harbor Learns to Count Effort — stable landings hide rapidly increasing time and distance spent fishing.

2. Two Boats, Same Catch — identical totals come from radically different effort, location and method.

3. The Survey Saw Plenty, the Harbor Saw Little — standardized observations remain stable while landings fall.

4. The Harbor Saw Plenty, the Survey Saw Little — concentrated catches create confidence that broader surveys do not support.

5. The Quiet Catch Year — landings fall because effort collapses during repairs and route disruption rather than because the stock is known to have declined.

6. The Old Closure, New Run — a traditional closed week no longer aligns cleanly with Migration observations.

7. The Spawning Run Nobody Fishes — an aquatic aggregation is valuable as science, tourism and public memory rather than harvest.

8. The One-Day Opening — a narrowly scoped community event returns after several years and becomes a test of monitoring rather than a catch-maximization contest.

9. The Bycatch That Wasn't a Pest — repeated non-target interaction traces to corridor overlap instead of nuisance behavior.

10. The Release That Was Never a Landing — a historical ledger accidentally treats a released persistent Pokémon as a retained catch.

11. The Former Partner at the Estuary — a released former partner appears in later fishery observations without implying renewed ownership or willingness to return.

12. The Landing Ledger Disagrees With the Survey — both sources are legitimate but measure different parts of the system.

13. The Small-Individual Year — reported size composition shifts, but the interpretation remains open pending biological follow-up.

14. The Juvenile Year — many juveniles and fewer adults create competing recovery and concern narratives without immediate resolution.

15. The Storm Year Without a Stock Collapse — effort and access fail while independent survey evidence remains comparatively stable.

16. The Closure That No Longer Matches the Run — the institution must decide whether to move a familiar management calendar.

17. The Old Method Heritage Day — a traditional gear method is proposed for a festival and requires modern non-target review before use.

18. The Gear Change Changed the Index — a method improvement creates an apparent abundance jump in fishery-dependent records.

19. The Market Kept Selling After the Boats Stopped — stored or imported inventory prevents market availability from proving local fishing activity.

20. The Label Outlived the Management Unit — a famous market name survives after the scientific unit boundaries are revised.

21. The River Stock Was Counted Twice — inland and estuary assessments unknowingly overlap the same migrating population.

22. One Population, Three Institutions — river, estuary and coastal teams maintain different evidence quality and calendars for a connected stock.

23. The Fishery Without Boats — shore and pier activity dominates, preventing Maritime assumptions from leaking into the fishery model.

24. The Pier Camera Changed the Count — better observation coverage creates an apparent jump in activity without evidence of physical increase.

25. The Landing Site Moved — erosion or redevelopment relocates the handoff point while the historical fishery identity persists.

26. The Protected Bay Still Has Activity — research, rescue, transit and observation continue during a no-harvest period.

27. The Emergency Measure Became Expected — a crisis-era resource-use measure outlives the emergency socially and requires deliberate review.

28. Three Records, Three Meanings — the same number in a receipt, effort log and survey means three different things.

29. The Archive Has Catch but No Effort — an early era can be described accurately while remaining unsuitable for abundance inference.

30. Nothing Happened at Pier Three — an ordinary season later becomes the best baseline for interpreting a future anomaly.

## Long arc — Five Seasons at Glasswater Fishery

Year one relies heavily on landing reports. Year two adds independent surveys after crews report longer effort for the same catch. Year three reveals a timing shift in a recurring movement window. Year four brings storms that reduce effort and test whether institutions learned not to interpret low catches mechanically. Year five is deliberately routine: assessment review and scoped decisions happen without needing player intervention.

The arc can reuse the same harbor staff, survey stations, persistent Pokémon, public fishing event and archival ledgers while changing what each record means over time.

## Long arc — One Population, Three Institutions

A population uses an inland river, estuary and coastal area. Each institution begins with locally valid but incomplete evidence. Migration, photography, tagging/identity observations and possibly Conservation Genetics gradually reveal more overlap than expected.

Success means compatible monitoring and clearer handoffs, not institutional merger or one group being exposed as incompetent.

## Long arc — The Harbor Learns to Count Effort

The harbor has decades of catch stories but little standardized effort information. Players may help compare old route logs, gear revisions, work hours and independent surveys. The strongest outcome is an institution that becomes more explicit about uncertainty, not a magical exact population count.

## Encounter — Spawning Run Closure at Reedmouth

Narrative premise: a recurring aquatic movement passes through a public reach during a temporary management measure. A crowd and a separate disturbance converge while the movement is in progress.

FULL dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- AI legal-action infrastructure — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING for dynamic `CROSS`/`WITHDRAW`/route protection;
- terrain/weather/hazards/zones/reactions — BLOCKING if current, depth, moving water or a protected tactical lane changes rules;
- AI tactical policy — BLOCKING for `CROSS`, `WITHDRAW`, `PROTECT_ROUTE`, `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- move-specific behavior, abilities, items, status lifecycle and Trainer Features/perks — PARTIAL only if the authored encounter invokes exact examples.

REDUCED version:

Fisheries closes the activity, Public Space redirects the crowd and Migration advances the aquatic group outside the battle grid. If an independent confrontation remains, AutoPTU receives a static riverbank/bridge arena with only actual combatants. The battle result does not determine whether the migration episode completed.

## Encounter — Bycatch Release at South Pier

Narrative premise: a non-target Pokémon becomes involved in authorized fishing activity while a separate disturbance complicates release operations.

FULL dependencies:

- verified basic combat families as above;
- complete movement — BLOCKING for a withdrawal/release lane;
- AI tactical policy — BLOCKING for non-hostile `WITHDRAW_TO_WATER` or `PROTECT_ROUTE` objectives;
- adapter/playback — BLOCKING;
- items — PARTIAL if fishing gear has tactical effects;
- terrain/weather/hazards/zones/reactions — BLOCKING if water or gear becomes a tactical zone.

REDUCED version:

The non-target Pokémon is released through world state before battle. No restraint, injury, drowning or survival rule is invented. A static pier confrontation resolves the independent threat, then Pass 70 Fisheries records disposition and later evidence.

## Encounter — Survey Device Recovery After Storm

Narrative premise: monitoring equipment and its provenance are stranded after a storm. The goal is recovering evidence, not harvesting wildlife.

FULL dependencies:

- complete movement — BLOCKING for moving technicians/device objectives;
- terrain/weather/hazards/zones/reactions — BLOCKING if water/debris/storm effects matter tactically;
- AI tactical policy — BLOCKING for `RETRIEVE_DEVICE`, `PROTECT_TECHNICIAN`, `WITHDRAW`, `REACH_EXIT`;
- adapter/playback — BLOCKING;
- items — PARTIAL if the survey device becomes a true tactical item.

REDUCED version:

Freshwater/Meteorology resolve the storm state and technicians secure the instrument outside battle. If a conflict remains, use a static adjacent arena. Scientific provenance survives independently of the battle result.

## Non-combat scenario — Landing Discrepancy at Harbor Market

Fisheries, Markets, Supply Chains, Archives and Metrology compare landing records, effort, stored inventory, imports, survey evidence and unit definitions.

Valid outcomes include reporting lag, changed effort, stored product, incompatible scopes or unresolved discrepancy. A battle cannot establish abundance, fraud or provenance.

## Permanent guardrails

Pass 70 remains the Fisheries authority.

Do not infer stock abundance from catch counts, CPUE without an authored assessment method, Minecraft fishing, loaded Cobblemon, KO/capture/despawn, market stock or a single survey.

Do not infer survival or injury from `released` alone.

Do not convert fishing access into capture permission or ownership.

Do not create nets/lines/hooks as Stuck or forced movement, deep water as drowning, current as knockback, or protected areas as tactical zones without exact validated mechanics.

All content in this file remains NON-CANON until separately approved.