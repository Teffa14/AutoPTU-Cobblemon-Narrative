# Disturbance, succession and ecological recovery scan

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03
Pass: 237

## Research question

How should Ouros represent a habitat after a meaningful disturbance so the world can recover, reorganize or remain degraded without reducing the process to a respawn timer or silently restoring a pre-event snapshot?

This note does not create canon. It extracts reusable structures and keeps source provenance separate from Ouros decisions.

## Existing Ouros constraints checked before research

The repository-wide ecology directive requires an explicit path for disturbance, succession and recovery. `canon/ecosystem-conflict-managed-development-foundation.md` already allows persistent changes to vegetation, resources, spatial use and environmental evidence while leaving exact recovery rates open. `canon/marea-interior-first-wild-population-v1.md` freezes the first Sendero Fletchling population identity and explicitly warns that visible actors are not abundance. `design/human-disturbance-habituation-gradient-contract.md` already models repeated human exposure and memory, so Pass 237 must model habitat/community trajectory after an ecological disturbance rather than repeat behavioral habituation.

The source-authority policy remains controlling: official Pokémon evidence can establish explicit species/world patterns; PTU/Caelo/Kairos can inform living-world structure; real ecology proposes mechanisms; Minecraft projects state; AutoPTU only adjudicates structured mechanics after handoff.

## New public-source findings

### 1. Recovery has multiple legitimate outcomes

USGS summarizes post-disturbance ecosystem outcomes as persistence, recovery and reorganization. Some reorganized states are temporary successional stages; others become persistent alternative states. This supports an Ouros state machine with branching outcomes rather than `disturbed -> normal`.

Source: U.S. Geological Survey, “Mechanisms of forest resilience,” 2022.
https://www.usgs.gov/publications/mechanisms-forest-resilience

A companion USGS diagram explicitly describes pathways after severe disturbance as recovery, transient reorganization or alternate states.

Source: U.S. Geological Survey, “Diagram of possible pathways following disturbance,” 2022.
https://www.usgs.gov/media/images/diagram-possible-pathways-following-disturbance

Older synthesis literature also warns that gradual pressure can reduce resilience before an apparently abrupt shift into another ecosystem state. For Ouros, pre-event stress and repeated disturbance should therefore matter to recovery probability.

Source: Scheffer et al., “Catastrophic shifts in ecosystems,” Nature 413, 2001.
https://www.nature.com/articles/35098000

Reusable lesson: the simulator should distinguish recovery toward the former state from reorganization into a new persistent state. “Different” is not automatically “broken.”

### 2. Disturbance leaves ecological memory

USGS describes ecological memory as both information legacies, such as traits adapted to disturbance, and material legacies, such as surviving organisms, seeds, nutrients and physical structures. Changing disturbance regimes can erase these legacies and create resilience debt that becomes visible only after a later impact.

Source: U.S. Geological Survey, “Changing disturbance regimes, ecological memory, and forest resilience,” 2016.
https://www.usgs.gov/publications/changing-disturbance-regimes-ecological-memory-and-forest-resilience

Reusable lesson: recovery should read surviving resource/structure/occupancy state from immediately before and after the event. Chunk reload must not reconstruct recovery only from biome defaults.

### 3. Recovery can be nonlinear and stage-dependent

USGS work on biological soil crusts describes a general succession sequence after disturbance while emphasizing that climate, severity and substrate can change or skip stages. Recovery can be highly nonlinear.

Source: U.S. Geological Survey, “Natural recovery of biological soil crusts after disturbance,” 2016.
https://www.usgs.gov/publications/natural-recovery-biological-soil-crusts-after-disturbance

Reusable lesson: Ouros needs stage conditions and transition evidence rather than a universal elapsed-time percentage.

### 4. A disturbance can create temporary resources

US Forest Service research on post-fire snags found that dead standing trees change ecological function through time and can create a transient wildlife resource pulse, including cavity habitat, before later decomposition changes the site again.

Source: U.S. Forest Service, “Snag decomposition following stand-replacing wildfires alters wildlife habitat use and surface woody fuels through time,” 2023.
https://research.fs.usda.gov/treesearch/67003

Reusable lesson: impact may reduce one resource while increasing another. `disturbance_severity` must not simply subtract a uniform habitat-quality score.

### 5. Population recovery can lag behind habitat suitability

USGS demographic work after fire found years of low density and decline during recovery even at sites capable of supporting stable long-term populations. Habitat improvement therefore must not instantly refill a population to a target carrying capacity.

Source: U.S. Geological Survey, “Transient population dynamics impede restoration and may promote ecosystem transformation after disturbance,” 2019.
https://www.usgs.gov/publications/transient-population-dynamics-impede-restoration-and-may-promote-ecosystem

Reusable lesson: Pass 237 should modify habitat/resource conditions and occupancy pressure, while Pass 238 owns demographic arithmetic. Recovery of habitat and recovery of population numbers are separate transitions.

## Pokémon-specific narrative precedents

### Long restoration can be a living-world process

Lake Lucid is described as having become uninhabitable because of pollution, followed by a multigenerational cleanup effort and the later return of Water-type Pokémon. The useful pattern is not the specific location or characters; it is that restoration can involve monitoring, institutional continuity, delayed recolonization and visible return over long periods.

Source: Bulbapedia, “Lake Lucid.”
https://bulbapedia.bulbagarden.net/wiki/Lake_Lucid

### Resource degradation can displace groups and create secondary conflict

A Pokémon Journeys story at Cerise Park depicts dirty water displacing one group into another group's space, with conflict resolving only after the environmental cause is addressed. This is a useful high-level causal pattern for Ouros: habitat disturbance -> displacement -> interaction pressure -> restoration/relocation response.

Source: Bulbapedia, “JN107 - Big Brother to the Rescue!”
https://bulbapedia.bulbagarden.net/wiki/JN107

### Some Pokémon have explicit restoration capabilities, but they are exceptional

Shaymin has explicit Pokédex/fictional evidence for purifying polluted environments. That supports species-specific ecological interventions when such a species is canonically present and its behavior/rule is approved. It does not justify a generic “Grass Pokémon heals biome” rule and does not authorize Shaymin for Marea.

Source: Bulbapedia, “Shaymin (Pokémon).”
https://bulbapedia.bulbagarden.net/wiki/Shaymin_(Pok%C3%A9mon)

## PTU/community design evidence

A PTU exploration discussion describes travel maps where wild Pokémon are active parts of the environment with small local situations rather than stationary encounter tokens. This supports exposing succession through changed behaviors and local stories instead of a hidden recovery meter alone.

Source: r/PokemonTabletop, “Question for Exploration,” 2024.
https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9/

A separate PTU GM discussion highlights injured wild Pokémon and assistance as noncombat travel encounters. This supports recovery-phase quests where the player can stabilize habitat or individuals without combat being mandatory.

Source: r/PokemonTabletop, “Favorite nonviolent encounters?”, 2024.
https://www.reddit.com/r/PokemonTabletop/comments/1fta66r/

A campaign recruitment post describes a region decades after a catastrophe where some areas remain unsuitable. It is homebrew and provides no Ouros canon, but it is useful evidence that long-lived post-disturbance world states can support an exploration loop instead of being resolved in the same session as the triggering event.

Source: r/PokemonTabletop, “Looking for players for an ongoing PTU game,” 2024.
https://www.reddit.com/r/PokemonTabletop/comments/1hgbuha/

## PTU / Caelo / Kairos cross-check

The current Narrative repository tree contains a local Kairos source index but no raw Caelo source directory. Existing canon records preserve the supplied Caelo comparison: ordinary Fletchling can be route/urban-capable and show territorial/diurnal behavior, but Caelo rules do not automatically become Ouros rules. The first Sendero Fletchling mechanical blueprint remains bounded to supplied PTU 1.05 material.

Pass 237 therefore does not create tactical modifiers, PTU Status Afflictions, damage, healing, Levels, Moves, Abilities or Features from ecological recovery. Habitat succession remains Ouros world-state until a concrete structured encounter is explicitly handed off.

## Derived Ouros design principles

1. Disturbance is an event with typed effects, not a generic habitat-damage scalar.
2. The post-event site retains material and biological legacies.
3. Recovery state branches among persistence, recovery, transient reorganization and persistent reorganization.
4. Successional stages may expose temporary resources unavailable before the event.
5. Habitat recovery and population/demographic recovery are separate systems.
6. Repeated impacts before recovery can compound state and erase ecological memory.
7. Player restoration can influence pressures and legacies but must not guarantee an original-state outcome.
8. Minecraft can show debris, vegetation, access and visible actors; it cannot decide that recovery occurred merely because blocks changed or entities spawned.
9. Species-specific restoration powers require explicit species provenance and mechanical/content approval.
10. Observation should expose indicators and uncertainty rather than reveal hidden recovery state perfectly.

## Candidate state dimensions

The following are proposed implementation fields, not canon values:

```text
site_id
disturbance_regime_id
current_stage
pre_event_reference_id
last_disturbance_tick
impact_severity_by_dimension
surviving_structure_legacy
surviving_resource_legacy
surviving_population_legacy
soil_or_substrate_integrity
cover_availability
forage_access
water_or_air_quality
route_accessibility
temporary_resource_pulse
recolonization_pressure
recovery_momentum
reorganization_pressure
repeat_disturbance_pressure
observation_confidence
```

## Encounter patterns unlocked

A recovery site can support investigation of why an expected population has not returned, protection of an early-successional refuge, rerouting human traffic around vulnerable regrowth, removal of a persistent disturbance source, documentation of an unexpected beneficiary, or a decision between restoring the previous condition and accepting a stable new configuration.

Combat is optional in all of these premises. If a concrete defense or displacement encounter begins, AutoPTU receives only explicit combatants and verified mechanics.

## Next design decision

Pass 237 should formalize the branching disturbance/recovery contract and provide a deterministic Sendero fixture proving four invariants: an impact can change habitat without changing population count by itself; succession can create a temporary resource pulse; elapsed time alone does not guarantee recovery; and a repeat disturbance can push a recovering site toward reorganization.