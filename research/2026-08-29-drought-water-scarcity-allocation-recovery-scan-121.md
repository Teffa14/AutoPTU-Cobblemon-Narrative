# Ouros Narrative Research — Drought, Water Scarcity, Allocation & Recovery — Pass 121

Status: RESEARCH / PROVENANCE ONLY. This document is not Ouros canon.
Date: 2026-08-29

## Repository gap checked before research

The repository already contains authoritative candidate layers for Weather, Water Management, Drinking Water, Agriculture/Food, Conservation, Fisheries, Wildfire, Crisis/Rescue, Civic Governance, Public Notices, Infrastructure Outage and community health. It does not yet contain a dedicated continuity layer for a slow water-scarcity episode that links those owners over weeks, months or years while preserving uncertainty, changing interpretations, allocation decisions, temporary arrangements and recovery history.

The existing `water-management-dams-reservoirs-canals-continuity-extension.md` owns managed assets, operating regimes, executed operations and observed system state. A drought/scarcity layer must therefore not become a hydraulic simulator or take ownership of reservoir gates, canals, drinking-water treatment, crop outcomes or ecological decisions.

## Internal PTU / Caelo cross-check

The project source scan records that PTU campaign guidance supports central plots, character-centric arcs and sandbox activity, and that larger plots should alternate with periods of relative calm. Drought is suitable for that structure because it can begin as background observation, gradually alter jobs and settlement routines, produce local quests, and later become a regional arc without requiring every session to be a crisis.

Caelo evidence supports location-specific mechanical identity when a governing source defines an exact effect. Toxic Ravine is the known example in the internal scan. This does not create a generic drought, dehydration, heat, aridity, water-rationing, dust, dry-ground or harsh-sun ruleset. Any tactical effect still requires an exact PTU/Caelo source plus verified engine support.

Relevant internal evidence:
- `research/2026-08-18-source-scan.md`
- `design/water-management-dams-reservoirs-canals-continuity-extension.md`
- `design/weather-forecast-preparedness-operational-extension.md`
- `design/food-agriculture-hospitality-layer.md`
- `design/conservation-protected-areas-stewardship-layer.md`
- `design/drinking-water-treatment-distribution-continuity-extension.md`
- `design/engine-readiness-snapshot-pass-120.md`

## Public Pokémon source findings

### A Shadow of a Drought / Azalea Town

Source: https://bulbapedia.bulbagarden.net/wiki/EP142

Reusable structure: a prolonged dry period changes ordinary town life before it becomes an adventure objective. The river is dry and at least one institution changes normal operations. Slowpoke Well and local beliefs connect scarcity to community identity.

Ouros transformation: scarcity should alter schedules, services, visitor behavior and local interpretation before it becomes an emergency. A settlement can remain inhabited and socially active while several routines are constrained.

Do not import characters, the Slowpoke religious practice, exact cause, episode resolution or any species-wide rain capability.

### Take the Lombre Home

Source: https://bulbapedia.bulbagarden.net/wiki/AG063

Reusable structure: a village experiences a dry stream, residents possess a cultural explanation, another actor argues for investigation, and later evidence reveals a different physical explanation. The useful pattern is not the culprit. It is the coexistence of belief, observation, competing hypotheses and infrastructure investigation.

Ouros transformation: a drought/scarcity episode can contain multiple causal claims with different evidence quality. Community belief can remain socially important even when it does not become the governing physical explanation.

Do not import the shrine, Solrock accusation, Team Rocket mechanism, Lombre ritual or plot.

### The Light Fantastic / Remoraid Mountain

Sources:
- https://bulbapedia.bulbagarden.net/wiki/The_Light_Fantastic
- https://bulbapedia.bulbagarden.net/wiki/Remoraid_Mountain

Reusable structure: environmental change can have generational depth. Historical land-use choices altered forests, rivers and lakes, a settlement disappeared, and later ecological signs suggested partial return. The landscape preserves both loss and recurrence.

Ouros transformation: a scarcity arc can leave abandoned infrastructure, changed settlement geography, old water rights, oral history, recurring ecological observations and later restoration evidence. Recovery need not restore the exact former landscape.

Do not import the tribe, Remoraid mechanism, twelve-year cycle, ice pillar or exact ecological history.

### A Crowning Achievement

Source: https://bulbapedia.bulbagarden.net/wiki/Episode_260

Reusable structure: a dried lake exposes physical and cultural material that was previously inaccessible. Scarcity therefore changes what can be observed, not only what can be consumed.

Ouros transformation: low-water periods can reveal old infrastructure, markers, foundations, routes, objects, shoreline evidence or archaeological questions. The exposure itself does not prove ownership, date, cause or legality.

Do not import the Slowking legend, King's Rock sequence, characters or episode solution.

### Wake Up Snorlax!

Source: https://bulbapedia.bulbagarden.net/wiki/Wake_up_Snorlax

Reusable structure: an apparent drought can be experienced locally even when rainfall exists because a downstream supply path is interrupted. Scarcity symptoms and meteorological drought are therefore different facts.

Ouros transformation: `WATER_SCARCITY_OBSERVED` must remain separate from `METEOROLOGICAL_DROUGHT_SUPPORTED`. A town can face shortage because of blockage, damaged conveyance, demand, allocation, contamination, maintenance or another cause.

Do not import the Snorlax premise, characters or resolution.

### Gotta Catch A Roggenrola!

Sources:
- https://bulbapedia.bulbagarden.net/wiki/BW034
- https://bulbapedia.bulbagarden.net/wiki/Mr._Garrison

Reusable structure: facility plumbing can appear normal while the upstream spring or conveyance is unavailable; restoration can require a different owner institution from the facility itself.

Ouros transformation: local service failure, source-water condition, conveyance, habitat disturbance and repair should remain linked but separately authoritative.

Do not import the antagonists, weapon plot or species abilities.

## Public operational research

### USGS — drought and groundwater

Source: https://www.usgs.gov/water-science-school/science/drought-and-groundwater-levels

Reusable abstraction: dry periods can affect streams, lakes, reservoirs and groundwater differently and on different timescales. Pumping and recharge both matter to groundwater state.

Ouros use: separate observation families and preserve lag. Surface recovery does not automatically prove groundwater recovery. A well recovering does not prove a reservoir recovered. No real-world percentages, pumping limits or hydrologic equations are imported.

### USGS — drought monitoring

Sources:
- https://www.usgs.gov/drought
- https://www.usgs.gov/centers/sawsc/science/south-atlantic-water-science-center-drought-monitoring

Reusable abstraction: drought assessment uses multiple long-running observation networks. Current conditions and long-term context both matter.

Ouros use: preserve observation provenance, monitoring coverage and comparison baselines. A missing gauge interval is `UNKNOWN_FOR_INTERVAL`, not normality.

### Drought.gov — impacts and timescales

Sources:
- https://www.drought.gov/impacts
- https://www.drought.gov/what-is-drought/drought-timescales-short-vs-long-term-drought
- https://www.drought.gov/topics/water-supply

Reusable abstraction: drought has different manifestations and timescales across water supply, agriculture, ecology, public infrastructure and community life. Long-term effects can persist after visible conditions improve.

Ouros use: keep one scarcity episode connected to multiple owner systems through handoffs instead of using one scalar `drought_level` to mutate everything.

No U.S. drought categories, legal restrictions, thresholds, emergency powers or public-health guidance are imported.

## Reusable design lessons

1. Scarcity is an evidence graph, not one meter. Precipitation, streamflow, reservoir condition, groundwater, supply operations, demand, ecological observations and local reports can disagree temporarily.

2. Shortage and drought are different. A blocked route, contamination hold, equipment outage or allocation decision can produce scarcity without meteorological drought.

3. Slow hazards need ordinary life. Markets, schools, clinics, farms, routes, festivals, habitats and household routines should change gradually rather than switching from NORMAL to CRISIS in one tick.

4. Recovery is staggered. Rainfall can return before reservoirs, wells, crops, habitats, finances or public confidence recover.

5. Low-water states create exploration. Exposed structures, older shorelines, submerged roads, forgotten markers and historical infrastructure become discoverable without requiring a combat mechanic.

6. Competing explanations are useful when provenance stays visible. Folklore, institutional claims, resident memory and scientific observation can coexist without the generator declaring one speaker foolish or dishonest.

7. Pokémon observations should stay individual and evidentiary. A herd changing route, one Pokémon returning to a spring or a species appearing near remaining water can be recorded. None automatically creates drought sensing, weather prediction or water-generation capability.

## Explicit exclusions

This pass does not establish any Ouros drought region, reservoir, aquifer, water law, rationing system, irrigation right, emergency authority, water price, drought category, rainfall threshold, dehydration mechanic, crop-yield formula, groundwater model or species capability.

It also does not convert Water-type Moves into civic water supply, Rain Dance into reliable drought termination, Drought into a regional climate simulator, Sunny Day into long-term hydrology, or Minecraft biome/weather state into authoritative scarcity.

## Candidate scope for design layer

A dedicated layer should preserve:
- scarcity episode identity;
- observation bundles and coverage gaps;
- scarcity assessments with revision history;
- cause claims and confidence;
- affected water-source/service references;
- demand-pressure observations where canon supplies them;
- allocation/restriction handoffs owned by civic/service systems;
- temporary supply arrangements;
- ecological/agricultural/community consequence handoffs;
- recovery checkpoints by subsystem;
- historical low-water footprints and newly exposed features;
- individual Pokémon observations;
- unresolved questions and provenance.

That architecture is advanced in the paired Pass 121 design file.