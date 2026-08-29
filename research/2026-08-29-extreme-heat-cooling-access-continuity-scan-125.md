# Ouros Narrative Research — Extreme Heat & Cooling Access Continuity — Pass 125

Status: RESEARCH ONLY. Provenance and design evidence. Not established Ouros canon.
Date: 2026-08-29

## Why this gap was selected

The complete recursive repository tree was inspected before writing and returned `truncated=false`.

Existing systems already cover:
- observed weather, forecasts, notices and owner-system preparedness decisions;
- drought, water scarcity and allocation;
- air-quality monitoring;
- electric-grid service and restoration;
- facility maintenance;
- Care, clinic capacity and health observations;
- public spaces, temporary events, workplaces, travel and Crisis/Rescue.

No existing file specializes the continuity problem created when prolonged or unusual heat changes when places are usable, when outdoor activity is reasonable, where cooling or shade is available, and how those operational decisions recover at different times.

This pass therefore studies a narrow bridge layer. It does not define a new climate system, medical model, electrical model or PTU tactical Weather implementation.

## Public Pokémon sources

### Candid Camerupt!

Source: https://bulbapedia.bulbagarden.net/wiki/AG046

Observed reusable structure:
- travelers cross a hot desert;
- lack of water and heat alter their ability to continue;
- a remote household becomes a recovery/support location;
- the desert remains ordinary geography rather than a boss arena.

Ouros transformation:
A route can remain physically present while practical access changes because of observed conditions and available support. A farmhouse, shade structure, station, spring, public hall or other canonized site can become temporarily important without becoming a permanent quest hub.

Guardrail:
The anime event does not establish PTU dehydration, heat-exhaustion damage, timed HP loss, universal water requirements or a healing rule for Ouros.

### Raid Battle in The Ruins!

Source: https://bulbapedia.bulbagarden.net/wiki/JN014

Observed reusable structure:
- Desert Resort is too hot to cross on foot at that moment;
- the party changes traversal method rather than treating the route as universally closed;
- a Ranger already understands the local travel problem;
- the destination remains reachable through another capability and route plan.

Ouros transformation:
Keep `physical_route_exists`, `route_use_assessment`, `traveler_capability`, `support_available` and `journey_decision` separate. A location can be traversable for one prepared expedition and inappropriate for another without changing the base map.

Guardrail:
Flying Pokémon, species identity or a Ranger title does not automatically grant heat immunity, safe transport, carrying capability or an alternate-route mechanic. Those require exact governing evidence.

### Some Like it Hot

Source: https://bulbapedia.bulbagarden.net/wiki/EP240

Observed reusable structure:
- heat changes behavior and comfort during travel;
- cooler micro-locations matter;
- volcanic/hot-spring geography and ordinary travel coexist.

Ouros transformation:
Allow local shade, elevation, building form, water access or other authored context to matter as observations and service/access facts without converting every hot area into a tactical hazard.

### Withering Desert / Mystery Dungeon camp geography

Source: https://bulbapedia.bulbagarden.net/wiki/Furnace_Desert

Observed reusable structure:
- a persistently hot environment can also be normal habitat for some Pokémon;
- environmental identity and ecological occupancy coexist.

Ouros transformation:
Extreme heat for a settlement or activity does not imply that every local Pokémon is distressed. Habitat observations remain separate from human assumptions and from mechanical resistance.

## Public operational sources

### CDC — heat and health

Sources:
- https://www.cdc.gov/disasters/extremeheat/
- https://www.cdc.gov/climate-health/php/resources/protect-yourself-from-the-dangers-of-extreme-heat.html
- https://www.cdc.gov/nssp/php/partnerships/cdc-heat-health-tracker-uses-nssp-data.html

Reusable architecture only:
- heat can affect health and ordinary activity;
- conditions can be tracked alongside health signals;
- community response can include access to cooler places, changed activity timing and welfare checks;
- power interruption can interact with heat-sensitive services and equipment;
- aggregate health information can support response without exposing individual records.

Ouros transformation:
Represent heat observations, response decisions, cooling-site availability, welfare-check campaigns and aggregate Care handoffs as separate state objects.

Do not import:
- medical advice as game mechanics;
- real-world risk groups as automatic NPC tags;
- medication rules;
- temperature thresholds;
- clinical diagnostic criteria;
- American service numbers or institutions.

### NOAA/NWS HeatRisk

Source: https://www.wpc.ncep.noaa.gov/heatrisk/whatsinheatrisk.html

Reusable architecture only:
- a heat-impact product can vary by location and season;
- daytime and nighttime conditions can both matter to an assessment;
- a forecast-derived risk product is an interpretation, not a raw thermometer reading;
- decision support can be spatially scoped and time-bounded.

Ouros transformation:
If canon later supports a heat-impact product, preserve its method, scope, issue time, validity window and source observations. Do not use a universal hidden `heat_level`.

Do not import:
- HeatRisk colors or thresholds;
- numerical formulas;
- U.S. climatology;
- official warning authorities.

## Cross-source design lessons

### 1. Hot weather is not one state

Keep distinct:
- observed temperature/conditions;
- forecast conditions;
- heat-impact assessment;
- route or facility decision;
- cooling/shade availability;
- individual health observation;
- clinical assessment;
- electrical service state;
- water-service state;
- eventual recovery.

### 2. Route existence and route suitability differ

A road, trail or plaza can physically exist while a specific activity is delayed, shifted to another time, moved indoors or rerouted.

Travel remains authoritative for journeys and route use. This pass only preserves the heat-related evidence and decision lineage that Travel consumes.

### 3. Cooling access is a service, not a magic aura

A building being open does not prove its cooling function is available.

Power being restored does not prove the building is ready.

A shade structure can be useful without being a medical facility.

A temporary cooling location can persist socially after the episode ends.

### 4. Nighttime matters to continuity

A daytime condition may improve while overnight recovery remains poor, or vice versa. The model should preserve time windows instead of one daily boolean.

No physiological rule is inferred from this distinction.

### 5. Different institutions can react differently

A school, market, worksite, ferry, public event and clinic can consume the same weather evidence and make different decisions under their own authority.

The bridge layer records those decisions and their evidence. It does not make them automatically consistent.

### 6. Pokémon observations are evidence, not thermometers

A Pokémon seeking shade, changing activity time, gathering near water or remaining active can be recorded as behavior.

Those observations do not automatically establish:
- heat stress;
- heat immunity;
- future weather;
- water quality;
- Type-based resistance;
- a species-wide rule.

## PTU/Caelo cross-check

The internal source scan confirms that PTU/Caelo can attach exact mechanical environmental effects to specific governed locations or rules. Toxic Ravine is the established example in the project evidence.

That precedent does not establish a universal extreme-heat subsystem.

Remain UNKNOWN without an exact governing source and implementation evidence:
- generic heat damage per round;
- dehydration tracks;
- exhaustion/fatigue from temperature;
- automatic Burn, Poison, Sleep, Confusion or other status from heat;
- hot-ground movement penalties;
- sunlight-based accuracy or LoS changes;
- nighttime recovery bonuses;
- Type-derived heat immunity;
- Fire-type universal climate immunity;
- Water-type universal cooling capability;
- species-derived heat forecasting;
- generic cooling effects from Moves;
- Sunny Day, Drought or other battle Weather as long-duration civic climate authority;
- Trainer Features that create general heat-management authority.

Any exact rule discovered later must be linked by source and tested contract rather than inferred from theme.

## Engine implications

The world-state layer itself can advance now.

Mechanically rich encounters involving live heat zones, changing shade, delayed exposure, hot surfaces, environmental damage/status or weather-driven reactions depend on `terrain/weather/hazards/zones/reactions`, currently BLOCKING.

Escort, Intercept or forced displacement during evacuation depends on `complete movement including push/pull/knockback/interception/forced movement`, currently PARTIAL.

Timed closure or staged withdrawal can depend on `full turn/round lifecycle`, currently PARTIAL.

Objective-aware PROTECT/WITHDRAW/CLEAR_ROUTE behavior depends on `AI tactical policy`, currently BLOCKING.

Semantic presentation of cooling-site activation, evacuation or environmental state depends on `Minecraft/Cobblemon/Craftics adapter/playback support`, currently BLOCKING.

## Research exclusions

No protected prose, dialogue, distinctive character arc or complete plot is copied.

Public Pokémon material is used only for high-level structural patterns.

Operational sources are used only to design evidence/state boundaries. Real-world thresholds, clinical rules, legal mandates and procedures are not imported.

## Candidate Ouros questions left for canon

- Which regions experience recurring unusual or prolonged heat?
- Which institutions, if any, issue heat-specific assessments or notices?
- Which public buildings can serve as temporary cooler spaces?
- What technologies exist in each region for cooling, ventilation and monitoring?
- How do work, school, markets, events and travel change during hot periods?
- Which historical heat episodes are remembered locally?
- Which Pokémon individuals have documented trained roles during such episodes?
- What terminology do local communities use?

No answer is established by this research file.