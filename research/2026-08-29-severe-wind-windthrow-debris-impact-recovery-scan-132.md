# Ouros Narrative Research — Severe Wind, Windthrow, Debris & Impact Recovery Scan — Pass 132

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-29

## Research question

What reusable narrative and operational structures can enrich Ouros when strong wind changes a place without turning generic wind, Minecraft weather, Pokémon species flavor or PTU battle Weather into automatic mechanics?

The useful gap is the continuity between:

1. an observed or forecast wind condition;
2. reported local impacts;
3. verified impact scope;
4. attribution of individual damage or obstruction;
5. cross-owner handoff;
6. repair, clearance, inspection or service restoration by existing owner systems;
7. residual-condition verification;
8. durable changes to routes, vegetation, buildings, routines and public memory.

This scan does not establish that any Ouros region experiences a particular storm type, warning system, wind threshold or institutional response structure.

## Internal repository review

The complete recursive `AutoPTU-Cobblemon-Narrative` tree was inspected before choosing this topic. The tree was not truncated. Pass 131 head was:

`a3ac4749ac7b561ee77ddca05b1e4f16f71ef50f`

Relevant existing owners were checked before writing.

### Weather Forecast & Preparedness

`design/weather-forecast-preparedness-operational-extension.md` already owns observation nodes, forecast products, forecast revisions, notices as authored information objects and preparedness references.

It explicitly allows broad forecast bands such as strong wind possible at exposed elevations.

It does not make a forecast into future truth and does not implement PTU tactical Weather.

Therefore the new candidate layer must consume Weather observations and forecasts rather than duplicate them.

### Crisis, Rescue & Recovery

`design/crisis-rescue-recovery-layer.md` already owns generic crisis lifecycle, affected areas, shelters, staging, missing actors, evacuation, blocked-route references and multi-system recovery orchestration.

It already supports storms as a crisis type.

Therefore a wind-specific extension should not create another generic emergency manager. Its value must be impact provenance and wind-specific continuity across owner systems.

### Building Safety

`design/building-safety-occupancy-reentry-assessment-continuity-extension.md` owns scoped building assessment, restrictions, use/reentry decisions and revision history.

A broken sign, roof element, window or fallen tree against a building can be a wind-impact observation. The conclusion that a structure is safe or unsafe remains with Building Safety.

### Electric Grid

`design/electric-grid-generation-distribution-continuity-extension.md` owns grid assets, outages, isolation, restoration and service verification.

A wind incident can reference a downed line or pole report. It cannot itself de-energize, repair or restore the grid.

### Roads, Rail, Aviation, Ports and Travel

Their respective systems own route/service availability, inspection and reopening.

A branch across a road can be recorded as an obstruction observation. This layer cannot silently close or reopen the road.

### Forestry and Public Space

Forestry owns managed woodland state and vegetation management. Public Space owns park/common operations.

A downed tree, broken limb or windthrow cluster can be an observed impact. Diagnosis of tree health, removal decisions, forestry restoration and park reopening remain with their owners.

### Facility Maintenance and Construction

Facility Maintenance owns faults, repair orders and verification on existing facilities. Construction owns scoped project execution and handover.

Temporary bracing, repair or reconstruction after wind therefore stays outside the proposed wind-impact layer.

### Air Quality, Wildfire, Coastal, Stormwater and other hazard layers

Wind can coincide with smoke, fire behavior, coastal change, rain or flooding. Existing owner systems retain those truths.

The new layer must permit multiple concurrent hazards without inferring that wind caused every observed consequence.

## Pokémon source: Riding the Winds of Change

Source:
https://www.pokemon.com/us/animation/seasons/11/episode-12-riding-the-winds-of-change

The official Pokémon episode synopsis describes a Gliscor swept into a city by a storm. Local wind patterns then keep it trapped. Its navigation behavior in the built environment draws Gligar into the same problem, and the group begins taking food while stranded.

Reusable structure:

- the initial weather event and the persistent local condition are different facts;
- built form can change the consequences of an environmental condition;
- Pokémon displacement can create a later settlement problem without making the displaced Pokémon malicious;
- a response can aim to restore a viable movement path rather than defeat the Pokémon;
- the ecological/social consequence can outlast the original storm.

Ouros transformation:

A wind episode may create `displacement_observation` or an Ecology/Coexistence handoff. A Pokémon found somewhere unusual after a storm is not automatically classified as aggressive, invasive, lost, owned or available for capture.

Do not copy the Gliscor/Gligar plot, characters or exact solution.

## Pokémon source: Drifloon on the Wind

Source:
https://www.pokemon.com/us/animation/seasons/10/episode-28-drifloon-on-the-wind

The official synopsis combines a damaged wind-power facility, a resulting service loss, worsening gusts and a search after a person and Pikachu are blown off course.

Reusable structure:

- an infrastructure fault and a weather hazard can coexist without being the same incident;
- service loss may alter who travels and why;
- wind can change the destination of a journey rather than simply make a route binary-open-or-closed;
- a search begins from the last known movement and observed environmental direction, not omniscient coordinates.

Ouros transformation:

A wind-impact episode can link a Grid incident, Search/Crisis record and Travel deviation while keeping causal edges explicit. Wind direction reports can be evidence. They do not reveal a missing actor's exact position.

Do not import anime physics, Drifloon carrying capacity or species-derived safe transport.

## Pokémon source: Valley Windworks

Source:
https://bulbapedia.bulbagarden.net/wiki/Valley_Windworks

The location is a wind farm placed in a windy valley and connected to a power facility and surrounding ecology.

Reusable structure:

- habitual wind can be part of local identity and infrastructure rather than a perpetual hazard;
- a place may be designed around normal wind while still experiencing exceptional episodes;
- wind-related infrastructure can create professions, maintenance routines, local knowledge and recurring Pokémon activity.

Ouros transformation:

Keep `NORMAL_LOCAL_WIND_CONTEXT` separate from `DAMAGING_WIND_EPISODE`. Do not treat a windy location, wind turbine, Flying-type population or Electric-type population as evidence of an active hazard.

## PTU community source: weather timing and round lifecycle

Source:
https://www.reddit.com/r/PokemonTabletop/comments/o36tsd/delaying_initiative_to_avoid_environmental_ticks/

A public PTU rules discussion about Sandstorm shows why weather effects are highly sensitive to turn/round timing, initiative and exact rules text. The discussion focuses on whether a tick occurs relative to a delayed turn and the end of a round.

Reusable design lesson:

Environmental battle behavior cannot be approximated from narrative language. Timing matters.

Ouros consequence:

A narrative windstorm must remain world state unless a governing PTU/Caelo rule and AutoPTU contract explicitly implement its tactical effects. Do not create generic wind push, accuracy penalties, end-of-turn damage or reaction windows from prose.

This Reddit discussion is not governing rules evidence. It reinforces the need to consult the actual PTU/Caelo source before implementation.

## PTU community source: homebrew weather caution

Source:
https://www.reddit.com/r/PokemonTabletop/comments/u63fir/ptu_105_weather_effect_for_all_types/

This thread presents homebrew weather effects and community feedback. One useful design observation warns that repeated skill checks for every combatant can slow already large battles.

Reusable lesson:

A rich environmental premise should not automatically become repeated tactical tax rolls.

Ouros consequence:

Do not add generic Wind Survival/Acrobatics checks every round. Prefer narrative preconditions, explicit BattleSpec geometry and verified engine contracts.

The proposed homebrew effects in the thread are not PTU authority and must not be imported.

## Operational source: NWS local storm-damage assessment

Source:
https://www.weather.gov/arx/stormdamage

The National Weather Service material describes storm-damage survey as an evidence reconstruction problem. It notes that cleanup can remove evidence, that precise locations matter, and that apparent clues can be ambiguous. Tree-fall direction, for example, can be influenced by tree structure, soil, terrain and prior weakness. It explicitly warns that damage alone does not prove a tornado and that straight-line wind can produce projectiles and widespread damage.

Reusable architecture:

- impact report;
- timestamp and exact scope;
- observation/evidence bundle;
- competing source hypotheses;
- survey revision as more evidence arrives;
- distinction between observed damage and event classification;
- record of evidence lost or altered during cleanup.

Ouros transformation:

`DAMAGE_OBSERVED != WIND_CAUSE_CONFIRMED`.

`TREE_FELL != TREE_WAS_HEALTHY_BEFORE_EVENT`.

`DEBRIS_FOUND != DEBRIS_ORIGIN_CONFIRMED`.

`DAMAGE_PATTERN_INTERPRETED != WORLD_TRUTH_CREATED`.

Do not import Enhanced Fujita ratings, US agency roles, technical thresholds or legal definitions.

## Operational source: NWS high-wind preparedness and aftermath

Sources:
https://www.weather.gov/safety/preparedness
https://www.weather.gov/safety/thunderstorm-after
https://www.weather.gov/safety/wind-coastal-frontal

These sources show that wind impacts can include fallen trees, downed power lines, debris, transportation disruption and building damage, and that post-event assessment should wait until immediate hazardous conditions have ended sufficiently for access.

Reusable architecture:

- hazardous condition window;
- access-to-assess prerequisite;
- multiple impact channels;
- residual hazards after the strongest wind ends;
- owner-specific restoration that occurs on different clocks.

Ouros transformation:

`PEAK_WIND_PASSED != SITE_SAFE_TO_ASSESS`.

`SITE_ASSESSED != ROUTE_REOPENED`.

`DEBRIS_REMOVED != POWER_RESTORED`.

`POWER_RESTORED != BUILDING_REENTRY_AUTHORIZED`.

`ROAD_CLEARED != TREE-RISK REVIEW COMPLETE`.

No real-world threshold, warning name or emergency instruction becomes Ouros canon.

## Operational source: FEMA P-2055 post-disaster evaluation

Source:
https://www.fema.gov/sites/default/files/2020-07/fema_p-2055_post-disaster_buildingsafety_evaluation_2019.pdf

The guide notes that strong wind can create flying debris, add stress to already damaged structures, create access problems and down power lines. The useful lesson is procedural rather than structural: evaluators may be unable to inspect safely while the environmental condition is still active, and the assessment scope must remain separate from the weather observation itself.

Ouros transformation:

A post-wind assessment can have state `ACCESS_DEFERRED` or `ASSESSMENT_INCOMPLETE` without implying a technical conclusion about the asset.

Do not import placards, evaluator qualifications, building categories, standards or US procedures.

## Operational source: multi-system cascade without single-system ownership

Source:
https://www.weather.gov/jkl/2024-09-27-easternkentucky-helene-damaging-winds

This public event summary describes wind interacting with full foliage, saturated soil and atypical wind direction, producing uprooted trees, blocked roads, power-line damage and isolated structural damage.

Reusable structure:

One environmental episode can produce many owner-system consequences through different causal paths.

Ouros transformation:

A wind-impact graph can link observations to Road, Grid, Building Safety, Forestry, Public Space and Crisis without giving the wind layer authority over those systems' final states.

Do not reproduce the real event as an Ouros disaster.

## Key design lessons

### 1. Wind is an observed condition before it is a tactical mechanic

Weather owns observations and forecast products. Narrative can remember strong wind, gust direction, duration band and exposed-area reports. Tactical effects require explicit governing mechanics.

### 2. Impact and cause need different records

A roof element on a street is observable. Its exact origin may be unknown.

A tree is down. Wind may be one contributor among soil saturation, prior damage, decay or another event.

A power line is down. The Grid owner determines electrical state.

### 3. The strongest wind ending does not reset the world

Residual conditions can include:

- blocked access;
- hanging or unstable objects;
- downed vegetation;
- asset damage awaiting assessment;
- utility faults;
- relocated wild Pokémon;
- changed public routes;
- missing signage;
- temporary closures;
- cleanup evidence loss;
- revised local preparedness practices.

### 4. Spatial scope matters

An episode can be broad while impacts are highly local.

One street can be blocked while an adjacent street remains usable. One façade can need review while another entrance is unaffected. One park sector can have fallen trees while the wider district operates normally.

### 5. Recovery belongs to many owners

The wind-impact layer should coordinate provenance and handoffs. It should not repair roads, restore power, declare buildings safe or decide ecological recovery.

### 6. Pokémon displacement needs agency-safe handling

A storm-displaced Pokémon can be frightened, hungry, stranded, habituated, cooperative, defensive or simply present. No motivation should be inferred from species, Type or post-storm location alone.

### 7. Cleanup can change the evidence landscape

A branch may need immediate removal before a formal survey. A temporary photograph, witness report or work record can preserve what was known before cleanup changed the site.

This creates fair mysteries based on chronology rather than hidden retcons.

## Candidate Ouros state distinctions

- `WIND_OBSERVED != DAMAGING_IMPACT_CONFIRMED`
- `FORECAST_ISSUED != IMPACT_OCCURRED`
- `IMPACT_REPORTED != IMPACT_VERIFIED`
- `DAMAGE_OBSERVED != WIND_CAUSE_CONFIRMED`
- `TREE_DOWN != TREE_HEALTH_CAUSE_KNOWN`
- `OBJECT_DISPLACED != OBJECT_ORIGIN_CONFIRMED`
- `ROAD_OBSTRUCTED != ROAD_CLOSED_BY_OWNER`
- `ROAD_CLEARED != ROAD_REOPENED`
- `LINE_DOWN_REPORTED != ELECTRICAL_STATE_KNOWN`
- `PEAK_WIND_PASSED != SAFE_ACCESS_CONFIRMED`
- `BUILDING_DAMAGE_REPORTED != USE_RESTRICTION_ISSUED`
- `DEBRIS_REMOVED != INCIDENT_CLOSED`
- `WILD_POKEMON_PRESENT_AFTER_STORM != STORM_DISPLACEMENT_CONFIRMED`
- `ASSESSMENT_COMPLETE_FOR_ONE_SCOPE != DISTRICT_FULLY_ASSESSED`

## Research exclusions

This pass does not import:

- US warning names or thresholds;
- tornado or hurricane classifications;
- Enhanced Fujita scales;
- building-code wind design values;
- legal cleanup authority;
- utility safety procedure;
- forestry removal authority;
- generic PTU wind push;
- generic accuracy penalties;
- wind damage ticks;
- Flying-type immunity or vulnerability;
- species-derived forecasting;
- Drifloon carrying capacity;
- battle-weather equivalence between world wind and PTU Weather;
- homebrew Reddit weather mechanics.

## Candidate implementation direction

Create a proposed continuity extension that owns only wind-impact episode provenance, verified impact scopes, impact-source hypotheses, residual-condition records, evidence-preserving cleanup references and cross-owner handoffs.

Full tactical encounters can express active withdrawal, flying debris, wind displacement and protected corridors only when the exact engine families are verified.

Reduced versions should move the active wind hazard and noncombatants outside BattleSpec, then resolve a conventional battle on static inspected geometry while preserving the same narrative premise.
