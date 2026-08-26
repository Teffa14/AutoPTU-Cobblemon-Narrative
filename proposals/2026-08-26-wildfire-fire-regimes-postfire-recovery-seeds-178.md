# Ouros Wildfire, Fire Regimes & Post-Fire Recovery — Seeds 178

Status: NON-CANON PROPOSALS
Date: 2026-08-26
Pass: 178

All concepts below are original Ouros candidates derived from Pass 178 research. They establish no settlement, institution, historic fire, species behavior, prescribed-fire practice or PTU mechanic as canon.

## 30 candidate seeds

1. The Patch That Never Burned — a famous wildfire is remembered as having consumed an entire valley, but old imagery and surviving vegetation reveal an unburned island that later became important habitat.

2. The Second Fire Crossed the First — two fires separated by twelve years overlap only partially. Residents remember a single “burned district,” while ecology records two different histories.

3. The Black Hillside Turned Green First — the darkest-looking slope after a fire regrows vegetation faster than a lightly burned neighboring patch. Visual appearance stops being used as a recovery score.

4. The Fireline Became a Trail — a temporary access line cut during an old incident gradually becomes an informal path, then a mapped route, then a Wayfinding problem when managers try to restore habitat.

5. The Prescribed Burn Met the Wrong Wind — a planned treatment stays within safe operational limits but burns a different mosaic than predicted. Monitoring, not blame, decides what the ecological result means.

6. The Objective Was Fuel, Not Flowers — public debate calls a treatment unsuccessful because a popular flowering plant declines temporarily, while the authorized objective had been fuel continuity. Conservation later reviews both outcomes.

7. The Forest That Needed No Intervention — post-fire monitoring shows a section recovering without planting or clearing. The correct management action is to keep watching.

8. The Recovery Crew Disturbs the Recovery — well-intentioned restoration traffic repeatedly crosses a regenerating patch used by wildlife. The repair project becomes part of the ecological question.

9. The Old Burn Became a Nursery — a low-canopy post-fire patch becomes disproportionately important for juveniles of an authored local population. It is not globally “better habitat.”

10. The Fire-Adapted Species Rumor — local media claims a Fire-type population caused or welcomed a burn. Longitudinal observations support continued site use but not ignition or immunity.

11. The Rain Came Too Fast — the active fire is over, but intense rain produces runoff and sediment concerns from part of the footprint. Freshwater and Soil own the downstream result.

12. The Smoke Went Elsewhere — communities downwind experience the strongest smoke impacts even though their land never burned. Air Quality and Fire Ecology preserve different affected geographies.

13. Three Severities, One Photograph — a widely circulated aerial image flattens a complex burn mosaic into one dramatic color grade. The original and processed products remain preserved separately.

14. The Monitoring Plot Burned Twice — a long-term plot survives one fire and is reburned years later. The value of the plot increases because its full history remains intact.

15. The Road Reopened Before the Habitat — infrastructure recovery finishes quickly while ecological recovery remains uncertain for years. Public Works completion does not close the fire history.

16. The Habitat Recovered Before the Road — wildlife and vegetation return while an old bridge remains closed. Ecological and infrastructure recovery move at different speeds.

17. The Festival Moved One Year — a community relocates a seasonal celebration after smoke and access restrictions. Years later the temporary venue has become the preferred site even though the old area recovered.

18. The Burn Scar Is Older Than the Town — archaeology and fire history reveal repeated burns before the current settlement. Nobody alive “remembers” the oldest regime directly.

19. The Fire Tower Lost Its View — decades of regrowth make an old lookout less useful. The structure becomes heritage while monitoring moves elsewhere.

20. The Water Tank Was Built for the Last Fire — an emergency tank constructed after one event becomes routine civic infrastructure, then creates a maintenance problem long after the original hazard is forgotten.

21. The Lightning Fire Was Not a Disaster — a small remote ignition burns within a historically fire-active ecosystem and creates no crisis beyond monitoring and temporary access control.

22. The Planned Burn Was Cancelled — conditions fail the authorized window. The cancellation becomes evidence of institutional competence rather than a quest failure.

23. The Wildlife Returned Differently — the same population uses a post-fire area in a different season or part of the day. Spatial Ecology and Diel Activity own the behavioral interpretation.

24. The Old Severity Map Changes — a new processing method revises the mapped boundary between moderate and high effect zones without changing the fire event itself.

25. The Burned Orchard Question — a fire crosses abandoned agricultural land and adjacent recovering forest. The same severity label has different ecological consequences in each land-use history.

26. The Charred Sign Survives — a damaged trail sign becomes a public-memory object while Wayfinding replaces its operational function elsewhere.

27. The Fire Crew’s Quiet Year — a whole season produces monitoring, training and maintenance but no major incident. Those records later establish what “normal readiness” looked like.

28. The Reburn Avoided the Old Core — a later event wraps around a previous high-severity patch. Researchers investigate fuel structure and weather without assuming the older burn “protected” it.

29. The Community Wants the Forest Back — residents expect the exact pre-fire landscape to return. Climate and ecological monitoring suggest several plausible future states instead of one restoration endpoint.

30. Nothing Happened at Plot Twelve — repeated measurements show ordinary recovery and no unusual species turnover. Years later it becomes the clean comparison site for a more complex neighboring burn.

## Long arc: Five Fires of Meridian Basin

Year one establishes a small lightning-caused event with limited emergency impact. Year four adds a prescribed burn with explicit fuel and habitat objectives. Year seven produces a large mixed-severity wildfire that overlaps both earlier footprints. Year ten brings a minor reburn in one corner. Year fifteen has no major fire but the accumulated history now shapes vegetation mosaics, public expectations, route planning, water management and monitoring priorities.

The arc is about cumulative landscape history. It should remain possible for some years to contain no player-facing crisis at all.

## Long arc: The Forest After the Headline

The story begins after an active wildfire is already contained. A burned landscape that the public describes as “destroyed” still contains surviving trees, displaced and resident Pokémon, unburned patches, damaged infrastructure, newly opened habitat and areas needing protection.

Over several years, different institutions disagree less about facts and more about goals: public access, passive recovery, active restoration, fuel management, heritage preservation and wildlife protection. No single answer has to be universally correct.

## Long arc: The Prescribed Fire Ledger

A conservation unit keeps ten years of planned burns, cancellations, partial implementations and follow-up monitoring. Early projects use coarse objectives. Later projects become better targeted because old monitoring data survives. One burn that looked operationally perfect misses an ecological objective. Another that looked visually messy creates the desired heterogeneous structure.

The institutional payoff is improved decision quality, not a perfect fire-control technology.

## Encounter contract: Burn Perimeter Access Interruption

Narrative premise: after an active wildfire has stabilized, researchers must reach a monitoring plot near a closed edge of the footprint. Wildlife movement and an unrelated hostile actor create a confrontation.

FULL version:
- technicians may need to reach or withdraw from observation points;
- wildlife may attempt `WITHDRAW`, `CROSS` or `RETURN_TO_COVER` rather than fight to KO;
- some routes may become temporarily unavailable;
- if active heat, smoke or unstable burned ground changes tactical state, those effects must come from validated environmental rules.

Capability dependencies for FULL:
- targeting/footprints/range/LoS: VERIFIED for ordinary battle targeting; not authority for smoke visibility or ecological observation;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for dynamic withdrawal, interception and route changes;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL if any exact PTU condition is used;
- terrain/weather/hazards/zones/reactions: BLOCKING if fire, smoke, hot ground or unstable zones have tactical effects;
- move-specific behavior: PARTIAL when exact Moves matter;
- abilities: PARTIAL when exact Abilities matter;
- items: PARTIAL if protective equipment has tactical effect;
- Trainer Features/perks: PARTIAL if responder or Fire-related Features matter;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for non-hostile withdrawal/protection objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED version:
Fire Ecology and Crisis declare the active perimeter stable enough for a static battle area. Researchers and background wildlife are moved outside the grid first. No smoke, fire-spread, hot-ground or collapse mechanic exists in battle. AutoPTU resolves only the independent confrontation. The monitoring visit continues afterward.

## Encounter contract: Prescribed Burn Monitoring Day

Narrative premise: a planned burn has already been completed safely. During post-burn monitoring, a separate conflict develops near the edge of the treatment area.

FULL version:
- observers move between fixed monitoring stations;
- wildlife can retreat through known exits;
- the treatment mosaic may create different traversable spaces only if validated terrain rules exist;
- no one receives fire-themed bonuses simply because the setting recently burned.

Capability dependencies match Burn Perimeter Access Interruption, with `terrain/weather/hazards/zones/reactions` required only if treatment-state differences become tactical.

REDUCED version:
Monitoring stations, treatment effects and wildlife movements remain world-state objects. A conventional static battle occurs in an already safe clearing. Results do not determine whether the prescribed burn met its ecological objectives.

## Encounter contract: Post-Fire Watershed Survey

Narrative premise: after a fire and subsequent rain, a team surveys a drainage below part of the burn footprint. The ecological question is erosion/runoff; a battle is incidental.

FULL version:
- researchers may need to cross or withdraw;
- water/debris/mud can become tactical only if validated environment and movement rules support them;
- AI must understand protection and exit objectives.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full lifecycle/damage/status/move/ability/item/Trainer Feature families: PARTIAL when invoked;
- terrain/weather/hazards/zones/reactions: BLOCKING if runoff, mud, debris or unstable banks affect combat;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

REDUCED version:
Soil, Freshwater and Fire Ecology finish the survey geometry outside combat. Researchers leave the hazardous drainage. Any battle occurs on adjacent stable ground. A battle cannot prove erosion severity, water quality or recovery.

## Non-combat scenario: Fire-Regime Review

A community, conservation staff and researchers compare oral history, archives, tree/vegetation records, old maps and modern remote sensing. The question is whether the current fire-regime assessment still describes the landscape adequately.

Possible valid outcomes include:
- retain current assessment;
- revise frequency or seasonality interpretation;
- split one management unit into several;
- mark historical coverage insufficient;
- leave a major causal question unresolved.

No battle engine is required.

## Explicit mechanic prohibitions

Do not infer:
- wildfire -> Sunny Weather;
- smoke -> Accuracy penalty;
- charred ground -> Rough Terrain;
- flame front -> forced movement;
- post-fire ash -> Poisoned;
- Fire-type -> ecological fire immunity;
- Water-type -> firefighting capability;
- Rain Dance -> suppression volume;
- Flash Fire -> wildfire immunity;
- Flame Body -> ignition source;
- prescribed fire -> XP, Loyalty, stat or spawn bonus;
- Minecraft fire spread -> authoritative fire footprint;
- block destruction -> ecological severity;
- Pokémon KO/capture -> fire contained;
- green regrowth -> recovered=true.
