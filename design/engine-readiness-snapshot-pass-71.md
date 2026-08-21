# Engine Readiness Snapshot — Pass 71

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-21

## Repositories inspected

Read-only:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`cd4941d146d18e34d985a8783ea8f670dfd6eef0`

Latest inspected commit:

`Derive Hardened initiative from authoritative runtime state (#104)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/cd4941d146d18e34d985a8783ea8f670dfd6eef0

### New bounded evidence since Pass 70

Java now derives Hardened initiative from server-owned runtime state rather than accepting a caller-supplied Hardened bonus.

The bounded contract includes:
- canonical current round;
- canonical current Injury count;
- canonical temporary effects;
- Trainer Feature ownership for Press On!;
- Trainer Intimidate skill rank;
- Python-oracle fixtures and parity gate.

This further strengthens the already VERIFIED `action economy / initiative` family and gives additional concrete evidence inside the PARTIAL `Trainer Features / perks` family.

It does not prove:
- complete Trainer Feature coverage;
- complete Injury mechanics;
- seismic or environmental injury rules;
- earthquake damage;
- collapse rules;
- falling debris;
- structural HP;
- forced movement;
- dynamic terrain;
- hazards/zones;
- objective-aware retreat/rescue AI;
- Minecraft/Cobblemon projection.

A representative Feature or initiative interaction never promotes its whole family automatically.

## Python AutoPTU live evidence

Current inspected Python head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible work remains Career-focused and does not change this run's tactical capability map.

Available project-file evidence also exposes a specific `Mold the Earth` implementation in Python. It requires the Trainer Feature `Mold the Earth`, the Groundshaper capability and an appropriate Ground move before reshaping specific legal tiles and placing Spikes.

That is narrow evidence for one authored interaction. It does not establish a general earthquake, landslide, cave-collapse or ground-deformation subsystem.

## PTU / Caelo evidence relevant to Pass 71

The exact primary Caelo text for earthquake, collapse, falling objects, ground failure, liquefaction, landslides or seismic rescue was not reliably retrievable in this run.

No new mechanic is therefore asserted for:
- Earthquake environmental consequences;
- falling rock/debris;
- structural collapse;
- Tripped or Slowed from shaking;
- forced movement from ground motion;
- rough/slow ground after rupture;
- liquefaction;
- earthquake prediction;
- Groundshaper at regional scale.

## Permanent capability map

| Permanent capability family | Pass 71 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Geometry, target anchors, footprints, ranges and LoS have bounded parity evidence. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers and fit predicates have bounded implementation evidence. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Broad forced movement, interception and movement reactions remain unfinished. |
| core calculations | VERIFIED | Core PTU tables/stages/accuracy and selected modifiers have implementation evidence. |
| action economy / initiative | VERIFIED | Ordering, initiative assembly/install, runtime projection and additional modifier families have strong parity coverage. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial; complete status/Ability/Feature/reaction/delayed coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Multiple damage and post-damage slices exist; complete stateful pipeline is not proven. |
| status lifecycle | PARTIAL | Several status contracts exist; full controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Canonical semantic environment inputs exist in some paths, but broad terrain behavior, dynamic changes, hazards, zones and reactions are incomplete. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; catalog behavior is incomplete. |
| abilities | PARTIAL | Multiple Ability hooks exist; complete registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog does not. |
| Trainer Features / perks | PARTIAL | Runtime/registry infrastructure and selected Features now include Hardened/Press On!-related initiative behavior, but complete catalog is not proven. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-choice generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware decisions for retreat, rescue, avoid-hazard, reach-safe-zone or protect-objective remain future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a headless rules core; world projection and semantic playback are not complete. |

## Pass 71-specific overworld blockers

`OVERWORLD_SEISMIC_EVENT_GRAPH = BLOCKING`

Persistent event identity, revised origin solutions, observations, causality claims and historical linkage do not yet exist as server authority.

`OVERWORLD_FAULT_SEGMENT_STATE = BLOCKING`

Fault geometry, revisions, observed rupture and interpretation need persistent authored/scientific state.

`OVERWORLD_SEISMIC_SENSOR_NETWORK = BLOCKING`

Stations, calibration, outage, processing and communication dependencies require persistent infrastructure state.

`OVERWORLD_EARLY_WARNING_PIPELINE = BLOCKING`

The server needs a detect-after-origin → estimate → message → delivery → automatic-action contract. It must not be implemented as earthquake prediction.

`OVERWORLD_SHAKING_FOOTPRINT = BLOCKING`

One event must be able to produce different local shaking estimates/observations without deriving damage directly.

`OVERWORLD_AFTERSHOCK_SEQUENCE = BLOCKING`

Member events need individual identity plus sequence grouping and reinspection triggers.

`OVERWORLD_SURFACE_DEFORMATION = BLOCKING`

Surface rupture/uplift/subsidence/offset need persistent geometry and provenance separate from visual Minecraft cracks.

`OVERWORLD_GROUND_FAILURE_ASSESSMENT = BLOCKING`

Landslide/liquefaction susceptibility needs evidence and uncertainty separate from observed failure.

`OVERWORLD_GROUND_FAILURE_EVENT = BLOCKING`

Observed landslide, rockfall, lateral spread, settlement and related state need their own persistent objects.

`OVERWORLD_SLOPE_STABILITY_STATE = BLOCKING`

Previously failed slopes need persistent condition/monitoring across later rainfall, vegetation and drainage changes.

`OVERWORLD_SEISMIC_TO_GEOLOGY = BLOCKING`

Geology remains authority for substrate/fault interpretation; the new seismic layer must consume rather than duplicate it.

`OVERWORLD_SEISMIC_TO_SCIENCE = BLOCKING`

Event solutions, models, confidence and revisions need Science integration.

`OVERWORLD_SEISMIC_TO_CRISIS = BLOCKING`

Crisis should consume event/ground-failure impacts without creating seismic causes itself.

`OVERWORLD_SEISMIC_TO_ARCHITECTURE_INFRASTRUCTURE = BLOCKING`

Shaking/deformation should produce inspection/exposure inputs. Structure condition and utility failure remain their own authoritative state.

`OVERWORLD_SEISMIC_TO_TRAVEL = BLOCKING`

Route closures/restrictions require inspection and operator decisions, not direct inference from magnitude.

`OVERWORLD_SEISMIC_TO_SOIL_FLORA_FRESHWATER = BLOCKING`

Slope stability and liquefaction context require local soil, roots/vegetation, drainage and groundwater state.

`OVERWORLD_SEISMIC_TO_MEDIA_COMMS = BLOCKING`

Warnings, corrections and felt reports require delivery/knowledge state rather than global broadcast.

`OVERWORLD_SEISMIC_TO_COBBLEMON = BLOCKING`

Loaded entities or Pokémon movement must never become the authoritative seismic sensor or direct spawn-control mechanism.

`OVERWORLD_SEISMIC_TO_BATTLE = BLOCKING`

A world earthquake/landslide cannot create PTU terrain, damage, statuses or forced movement until exact rules and projection contracts exist.

## Critical distinction: Earthquake Move versus regional seismic event

A Pokémon battle Move and a world-scale geological event are separate concepts.

Even if a future Java slice implements the Move `Earthquake` perfectly, that would prove only the Move's authoritative battle behavior.

It would not prove that the Move can:
- create a fault rupture;
- trigger a regional seismic event;
- damage buildings outside battle;
- cause landslides;
- liquefy soil;
- generate aftershocks;
- alter groundwater;
- rewrite Minecraft terrain permanently.

Any world consequence would require an explicit, separately reviewed world rule.

## Critical distinction: geometry versus dynamic hazard

Verified base movement can operate on a frozen post-event map.

That supports reduced versions where:
1. world state resolves the earthquake/slide first;
2. the server generates a stable encounter snapshot;
3. AutoPTU receives fixed blockers/tiles;
4. ordinary legal combat proceeds.

It does not support:
- tiles collapsing during turns;
- actors being pushed by shaking;
- moving debris;
- expanding liquefaction zones;
- dynamically changing river blockage;
- autonomous evacuation behavior.

Those remain dependent on BLOCKING capability families.

## Encounter dependency review

### Aftershock at Switchback

Full version:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL
- full stateful damage — PARTIAL if exact environmental damage later exists
- status lifecycle — PARTIAL if exact status rules later apply
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Reduced version:
Resolve the aftershock before battle, commit one revised static route geometry, keep debris/civilians outside the grid and run ordinary combat only if needed.

### Liquefaction Yard Evacuation

Full version additionally needs:
- dynamic unstable zones — BLOCKING under terrain/hazards/zones;
- reach-safe-exit/protect semantics — BLOCKING outside the permanent capability map until objective contracts exist;
- tactical AI — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:
Evacuate and inspect outside battle. Use an inspected stable platform as the fixed arena. No sinking, Tripped, forced movement, damage or terrain penalty is inferred.

### Landslide-Dam Survey

Full version additionally needs:
- dynamic water/debris state — BLOCKING;
- potentially forced movement — BLOCKING;
- changing terrain/zones — BLOCKING;
- goal-aware withdrawal/navigation — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:
Freshwater + Seismic settle the current dam/water state before battle. AutoPTU receives a static safe-bank arena. Survey equipment and changing water stay outside tactical authority.

## Pass 71 recommendation

Narrative and world-state work can proceed immediately using reduced encounters.

Do not wait for dynamic-hazard support to author:
- event histories;
- sensor networks;
- aftershock sequences;
- inspections;
- route closures;
- slope monitoring;
- public warnings;
- archaeology exposed by failures;
- ecological displacement;
- long recovery arcs.

Do wait for exact PTU/Caelo + Java support before making shaking or ground failure mechanically alter a live battle.
