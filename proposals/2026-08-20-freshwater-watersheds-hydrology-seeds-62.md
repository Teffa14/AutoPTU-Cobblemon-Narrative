# Freshwater, Watersheds & Hydrology Seeds — Pass 62

Status: NON-CANON proposals. Original Ouros candidates derived from research patterns, not adaptations of any single source.

## 30 worldbuilding and quest seeds

1. The Reach That Never Reconnected — A side wetland normally reconnects after the first major seasonal release, but this year it remains isolated. Possible causes include debris, gate operation, altered channel geometry, sensor error or a changed upstream regime.

2. The Submerged Road — During an unusually low reservoir phase, an old road and foundations reappear. Residents disagree about what the structures once were, while Pokémon already use the exposed corridor.

3. Three Gauges, Three Stories — Three monitoring stations report contradictory water levels. The problem may be calibration, local backwater effects or genuinely different reach behavior.

4. The Spring Below the Orchard — A spring feeding a small orchard weakens while the visible river remains normal. Players can investigate groundwater, recent excavation, pumping or seasonality without assuming sabotage.

5. First Water Through the Old Channel — A restoration project sends water through a side channel for the first time in decades. Researchers, residents and wild Pokémon activity react over several days.

6. The Ferry Without a River — A ferry service remains on public timetables even though low flows make its route temporarily unusable. The service operator, transport office and local businesses all hold different pieces of the explanation.

7. Downstream Before Upstream — Fishers and researchers downstream observe a sudden ecological change before anyone upstream reports a problem. The cause may lie in groundwater, tributary flow, a delayed release or an unnoticed infrastructure issue.

8. The Wetland That Needs to Dry — A public campaign demands permanent inundation of a wetland because dry ground looks unhealthy. Long-term field records suggest periodic drying is part of the normal regime.

9. A Flood With Two Meanings — The same high-flow event threatens a low-lying road while reconnecting a breeding habitat nearby. Crisis response and conservation priorities must coexist.

10. The Old Dam Keeper's Ledger — Handwritten operating notes from a retired dam worker conflict with digital records. Neither source is automatically authoritative.

11. Water for the Festival — A settlement wants to raise water levels for a seasonal festival route. The proposed release may affect downstream habitat timing and another settlement's crossing.

12. The Vanishing Gravel Bar — A familiar low-flow crossing disappears one year even though total river level appears similar. Channel shape may have shifted.

13. Mudkip Nursery Detour — A protected nursery site becomes vulnerable after a diversion changes current through its inlet. The solution may involve infrastructure, timing or temporary relocation rather than capture.

14. The Reservoir Village Archive — Families whose former homes lie under a reservoir contribute photographs, maps and oral histories. Some locations can be verified when water recedes; others remain uncertain.

15. Irrigation Turnout 7 — A single irrigation gate is blamed for poor downstream flow, but the total shortage may come from several smaller changes across the catchment.

16. The Unexpected Return Flow — Water released for one wetland unexpectedly benefits a second downstream habitat, creating a new research opportunity and a debate about future planning.

17. Floodplain Market Week — A market traditionally operates on a floodplain during the dry season. A revised seasonal forecast creates uncertainty about whether the site will remain usable.

18. The River That Runs Underground — A mapped stream disappears into limestone and re-emerges kilometers away. Researchers suspect a connection but need tracing evidence before joining the two systems in canon.

19. Blue Water, Bad Data — A lake looks unusually clear after cleanup. Chemical and ecological observations remain mixed, forcing institutions to resist declaring success early.

20. The Broken Fish Ladder — A migration route around a control structure is present on official plans but no longer works as built. The problem is maintenance and geometry, not a villain.

21. The Flooded Mine Spring — Water begins emerging from an abandoned mine and feeding a tributary. Geology, pollution, habitat and old industrial records all become relevant.

22. A New Pond in the Quarry — A closed quarry fills gradually and becomes a freshwater habitat. Ownership, safety, public access and conservation lag behind the ecology.

23. The Last Summer Pool — During an extreme low-flow period, several isolated pools remain. Different Pokémon groups, researchers and nearby farms depend on the same shrinking water network.

24. The Town Above the Aquifer — A growing settlement discovers that its wells and nearby spring are linked more closely than expected. Population growth, housing and water planning become one long-term arc.

25. Upstream Rumor, Downstream Panic — A rumor claims a dam is failing. No failure is confirmed, but downstream communities react before the official correction reaches them.

26. The Canal That Became a Habitat — An old irrigation canal no longer serves farms but now supports a stable wild population. A proposal to restore its original use creates a genuine tradeoff.

27. Research Buoys After the Storm — Several freshwater sensors stop reporting after severe weather. Missing data should not be interpreted as abnormal water state until equipment is checked.

28. The Side Channel Nobody Owns — Multiple institutions assume another party maintains a small channel that matters for drainage and habitat connectivity. Years of unclear responsibility produce a backlog.

29. Two Maps of the Floodplain — An old map and a modern map disagree sharply. Both are accurate for the river geometry of their respective periods.

30. The Quiet Headwaters — A headwater valley shows reduced flow with no obvious local cause. The eventual explanation may involve snow/rainfall timing, groundwater recharge, vegetation change, geology or measurement error.

## Three longer arcs

### Arc A — The River Through Five Towns

A single freshwater system passes through five settlements with different dependencies: drinking water, farming, a wetland reserve, a ferry crossing and an industrial workshop district.

Year 1 establishes baselines and ordinary seasonal behavior.

Year 2 introduces a small upstream infrastructure change with benefits locally and ambiguous downstream effects.

Year 3 adds a dry season that exposes weak coordination between institutions.

Year 4 produces a major high-flow event. Previous maintenance and planning matter.

Year 5 forces a regional review. No ending requires one side to “win.” The strongest resolution is a better catchment model, revised agreements and visible physical changes justified by accumulated evidence.

### Arc B — The Lake Above the Old Town

A reservoir created decades earlier submerged part of an older settlement.

A prolonged low-water period exposes structures, road sections and habitat that have not been accessible in years. Tourism, archaeology, family memory, conservation and infrastructure safety collide.

Players can document sites, help establish access rules, identify unsafe areas, recover items only when custody/ownership is clear and observe how wild Pokémon use the newly exposed terrain.

When levels rise again, the content does not disappear. Chronicle stores what was learned, and future low-water windows can reveal different sections.

### Arc C — Springs of the Eastern Range

Several settlements rely on springs emerging along a mountain front.

One spring declines, then another. Initial theories focus on drought, but records show different timing at each site.

The arc can involve cave surveys, groundwater observations, old mine maps, pumping records, field ecology and public communication.

The final conclusion may remain probabilistic. The campaign rewards building a better model and adapting regional plans rather than defeating a culprit.

## Capability-aware encounter concepts

### Sluice Gate Survey

Full version:

Players investigate a control structure while water levels can change across the tactical map. Wild Pokémon may seek exits instead of fighting, and actors may need to reach or secure the gate.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement incl. interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

Investigation and gate manipulation occur in overworld state. Freeze one water-level map before battle. No current, rising water or automatic hazard effect occurs during combat.

### Floodplain Reconnection

Full version:

A controlled release gradually reconnects a side channel. The battle space may gain or lose traversable tiles while Pokémon pursue movement goals.

Blocking families: terrain/weather/hazards/zones/reactions; complete movement; tactical AI; playback. Exact Move/Ability/item/Feature interactions remain PARTIAL unless specifically verified.

Reduced version:

Advance the floodplain in coarse phases outside battle. Each encounter snapshots one stable phase. Pokémon relocation/migration writes back to ecology after combat or observation.

### Dry-Season Ford

Full version:

Actors cross a partially exposed riverbed while current and footing vary. A rescue or withdrawal objective may replace KO.

Blocking families: complete movement/interception; terrain/hazards/zones/reactions; tactical AI; playback.

Reduced version:

Resolve route eligibility first. Use a static ford geometry and standard battle rules if conflict occurs. Water has no invented mechanical effect.

## World-state consequences worth testing

These seeds are useful because they can write back to existing layers without creating new battle rules:

- route availability;
- ferry/service state;
- wetland connectivity;
- habitat observation;
- irrigation availability;
- public-works proposals;
- crisis preparedness;
- water-quality investigations;
- archaeological access;
- tourism pressure;
- research programs;
- settlement growth constraints;
- map revisions;
- public information corrections;
- agreements between upstream/downstream actors.

## Canon boundary

Nothing in this file establishes Ouros rivers, towns, dams, water law, irrigation rights, hydrology institutions, species distributions or PTU mechanics.

Promotion requires regional geography, institutional ownership/mandate, PTU/Caelo validation and implementation review.
