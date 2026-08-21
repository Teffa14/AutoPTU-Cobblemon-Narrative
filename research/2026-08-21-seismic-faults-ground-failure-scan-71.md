# Seismic Faults, Ground Failure & Slope Instability Research — Pass 71

Status: research/provenance only. Not Ouros canon. External sources below are inspiration and factual-reference sources, not PTU/Caelo rules authority.

Date: 2026-08-21

## Why this pass exists

The repository already has dedicated layers for geology/excavation, crisis response, soil/erosion, freshwater, volcanism, architecture, infrastructure and meteorology. None of them owns persistent seismic-event state, fault observations, aftershock sequences, earthquake early warning, earthquake-triggered ground failure or the long-lived instability of a previously failed slope.

A repository search for `earthquake seismic fault landslide tremor` returned no existing dedicated layer. `geology-excavation-resource-frontier-layer.md` explicitly avoids defining geological hazard damage. `crisis-rescue-recovery-layer.md` can consume tremors or collapses as crisis signals and impacts, but it does not model the underlying seismic process.

The useful gap is therefore not “earthquake quest design.” It is the world-state contract that lets one earthquake create different shaking, ground failure, infrastructure, travel, ecological and recovery consequences in different places without turning every cracked block into an invented PTU hazard.

## Sources inspected

### Pokémon official — Team Eevee and the Pokémon Rescue Squad!

Source:
https://www.pokemon.com/us/animation/seasons/16/episode-5-team-eevee-and-the-pokemon-rescue-squad

The episode begins with a rockslide blocking a route. The failed material is still unstable; an attempted crossing causes it to give way again, requiring rescue. The same story later shifts to a dam emergency with disabled power and trapped workers.

Reusable high-level structures:
- a visible slope failure can remain unstable after the initial event;
- route closure, rescue and infrastructure consequences can coexist without being the same problem;
- a completed rescue does not automatically restore the route or underlying slope condition;
- Pokémon capabilities can matter to rescue only when the actual Pokémon and rule state support them.

Do not copy the named rescue team, characters, dialogue or incident sequence.

### Pokémon official — Saving the World from Ruins!

Source:
https://www.pokemon.com/us/animation/seasons/12/episode-7-saving-the-world-from-ruins

Explosives placed by human antagonists cause the island to tremble. This is useful specifically as an anti-assumption: observed shaking does not prove a tectonic earthquake. Human activity, machinery, collapse, blasting or another authored process may generate a tremor-like signal.

Reusable structures:
- seismic observations and causal interpretation must remain separate;
- an investigation can compare multiple candidate causes before declaring a fault event;
- regional instruments, witnesses and later physical inspection may disagree at first.

### Pokémon official — Pokémon Ranger: Deoxys' Crisis, Parts 1–2

Sources:
https://www.pokemon.com/uk/animation/seasons/9/episode-26-pokemon-ranger-deoxys-crisis-part-1
https://www.pokemon.com/us/animation/seasons/9/episode-27-pokemon-ranger-deoxys-crisis-part-2

These episodes use unusual geomagnetic observations, disrupted devices and animal behavior as signals that motivate investigation before the cause is resolved.

Reusable structure:
- environmental instruments and Pokémon behavior can become evidence streams;
- a signal may be real even when the first causal explanation is wrong;
- technical outages can be consequences, sensors, or unrelated complications and should not automatically become proof of the same cause.

This source does not justify supernatural seismic prediction in Ouros.

### Public PTU community campaign — Raist disaster campaign

Source:
https://www.reddit.com/r/PokemonTabletop/comments/16tt7ux

A publicly described PTU campaign uses escalating storms, earthquakes and heatwaves as the historical crisis that reshapes an entire region and later drives exploration from sealed settlements.

Reusable high-level lesson:
- a natural-hazard event can define the state of routes, settlements, institutions and exploration decades later;
- the long tail of a disaster may be more valuable than repeatedly replaying the initial catastrophe;
- unexplained coincidence among multiple hazard types can remain a campaign mystery without requiring every individual local event to share one cause.

Do not import the region, vault premise, characters or plot.

### Public PTU anecdote — earthquake-exposed cave

Source:
https://www.reddit.com/r/PokemonTabletop/comments/onnt2p

A public PTU anecdote describes a cavern exposed by an earthquake and subsequently treated as structurally unstable during exploration.

Reusable structure:
- an earthquake can reveal a new site while simultaneously making it unsafe;
- discovery and access are separate from stability;
- a newly opened cave can become archaeology/geology content first and only later a battle site.

The anecdote's specific combat and damage choices are not treated as rules guidance.

### USGS — Earthquake Early Warning Overview

Source:
https://www.usgs.gov/programs/earthquake-hazards/science/earthquake-early-warning-overview

Key factual design lesson: earthquake early warning detects an earthquake after it has already begun. It is not earthquake prediction. A sensor network estimates location, size and expected shaking quickly enough that some locations may receive seconds of warning before stronger waves arrive. Alerts can trigger protective actions or automatic system responses.

Reusable structures for Ouros:
- `detection` and `prediction` must be separate data states;
- an alert may reach some locations before shaking and others after it;
- alert delivery depends on sensor, processing and communications infrastructure;
- automated actions can change transport, utilities or institutional state before impact;
- the alert itself never guarantees how strong local shaking will be.

### USGS — Ground Failure

Source:
https://earthquake.usgs.gov/data/ground-failure/

USGS groups earthquake-triggered landslides and liquefaction under earthquake ground-failure products and produces spatial estimates after significant events.

Reusable structure:
- the seismic event should be one object;
- ground-failure assessment should be another object derived from event + local conditions;
- a map can estimate susceptibility without asserting that every mapped patch failed;
- post-event surveys can replace model estimates with observed state.

### USGS — What Are the Effects of Earthquakes?

Source:
https://www.usgs.gov/programs/earthquake-hazards/what-are-effects-earthquakes

This source distinguishes surface faulting, shaking and liquefaction-related ground failure. It also explains that liquefaction depends strongly on local geological and hydrological conditions.

Reusable structure:
- magnitude is a property of the earthquake; local shaking is spatially variable;
- local soil/water conditions can change consequences dramatically;
- `liquefaction_susceptible` is not the same state as `liquefaction_observed`;
- structural damage is downstream of both hazard exposure and the structure's own vulnerability.

### USGS — Shaking, Damage and Failure

Source:
https://www.usgs.gov/programs/earthquake-hazards/science/shaking-damage-and-failure

This research explicitly separates ground motion, near-surface soil behavior, liquefaction/ground failure and building response.

Reusable structure:
- do not calculate building damage directly from earthquake magnitude;
- Architecture/Infrastructure should own structure condition while the seismic layer supplies exposure/evidence;
- the same event can create very different outcomes in neighboring districts.

### USGS — Landslides Can Cause More Landslides

Source:
https://www.usgs.gov/programs/landslide-hazards/science/landslides-can-cause-more-landslides

A previously failed slope may remain more vulnerable because vegetation, roots, drainage and soil structure changed. Rainfall can later reactivate a failure.

Reusable structure:
- landslide aftermath can remain persistent world state for months or years;
- a later rainfall-triggered reactivation may trace back to an older failure without being an aftershock;
- Soil, Flora, Meteorology and Freshwater can all alter later slope stability;
- repairing a road below the slope does not automatically stabilize the slope itself.

### USGS — What Are Landslides and How Can They Affect Me?

Source:
https://www.usgs.gov/programs/landslide-hazards/what-a-landslide

Landslides can move slowly or rapidly and can be triggered by rainfall, earthquake shaking or volcanic activity.

Reusable structure:
- a landslide is an event family, not an earthquake synonym;
- trigger attribution should remain evidence-based;
- slow slope deformation can create monitoring, maintenance and route-planning content before a catastrophic failure occurs.

## Cross-layer design lessons

The research supports this authority chain:

`physical seismic event`
→ `sensor/witness observations`
→ `event solution / interpretation`
→ `local shaking footprint`
→ `ground-failure assessments and observations`
→ `Crisis / Travel / Infrastructure / Architecture / Ecology consequences`
→ `recovery and long-term monitoring`

No later layer should rewrite the historical seismic event to explain its own local state.

A second useful chain is:

`old landslide`
→ `changed slope/drainage/vegetation`
→ `rain / snowmelt / shaking / construction disturbance`
→ `new slope observation`
→ `reactivation assessment`
→ `route or infrastructure decision`

This gives Ouros delayed consequences without arbitrary world events.

## Strong anti-inference rules

- A tremor does not prove a tectonic earthquake.
- A Ground-type Pokémon nearby does not prove causation.
- The Move Earthquake used in battle does not automatically create a regional seismic event.
- A seismic event does not mean every settlement experiences the same shaking.
- Strong shaking does not automatically mean a building collapsed.
- A crack in Minecraft terrain does not automatically become PTU Rough Terrain, Slow Terrain, a Hazard or forced movement.
- A liquefaction susceptibility estimate does not prove liquefaction occurred.
- A landslide after an earthquake may have multiple contributing causes.
- A previously failed slope is not automatically stable after debris is cleared.
- An early-warning message is not a prediction made before the earthquake began.
- Pokémon behavior before a quake can be an observation; it is not a reliable prediction system unless future canon and mechanics explicitly establish one.

## PTU / Caelo mechanical boundary

The current project file evidence exposes a specific Python `Mold the Earth` implementation requiring both the Trainer Feature and Groundshaper capability before it reshapes legal tiles and places Spikes. That narrow implementation is useful as a guardrail: earth manipulation only becomes mechanical when an exact rule authorizes it.

The primary Caelo corpus was not reliably retrieved in this run for exact seismic, collapse, falling-rock, liquefaction, landslide or environmental-damage rules. No such mechanics are asserted here.

Nothing in this research establishes:
- earthquake environmental damage;
- falling-debris damage;
- automatic Tripped or Slowed conditions from shaking;
- knockback from seismic motion;
- structural HP;
- cave-collapse rolls;
- landslide movement rules;
- seismic prediction Skills;
- immunity for Ground/Rock/Steel types;
- a Groundshaper ability to stop regional earthquakes;
- a Move Earthquake effect outside its authoritative battle definition.

## Recommended Ouros design direction

Create a dedicated Seismic / Ground Failure layer between Geology and Crisis. It should own event identity, sensor observations, fault/deformation records, shaking footprints, aftershock sequences, surface rupture and ground-failure observations/assessments. Crisis should own immediate response. Architecture and Infrastructure should own damage/inspection state. Soil/Hydrology should own local substrate/water context. Science should own interpretation. Media should own communication. AutoPTU should receive only an explicitly validated, frozen tactical projection when a battle begins.
