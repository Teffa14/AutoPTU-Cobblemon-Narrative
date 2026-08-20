# Wildfire, Fire Ecology & Landscape Recovery — Research Scan

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. No PTU mechanic is established by this document.

Pass: 64
Date: 2026-08-20

## Why this pass exists

The repository already contains dedicated systems for crisis response, meteorology, conservation, freshwater hydrology, biosecurity, architecture, settlements, wildlife collectives, care, transport, pollution and public memory.

Those layers can represent a fire as an emergency and later restoration work, but they do not yet provide a persistent fire-ecology contract that distinguishes:

- ignition evidence from cause;
- active fire perimeter from smoke footprint;
- fire weather from tactical Weather;
- burn severity from simple burned/unburned state;
- fire refugia from untouched generic habitat;
- immediate displacement from long-term population change;
- suppression from ecological recovery;
- post-fire regrowth from restoration work;
- planned fire from wildfire;
- post-fire erosion and water-quality risk from the original fire event.

This pass adds research for that missing layer without replacing `crisis-rescue-recovery-layer.md` or `conservation-protected-areas-stewardship-layer.md`.

## Source findings

### 1. Pokémon Horizons treats wildfire as damage with a recovery phase

The official Pokémon Horizons recap states that Arboliva's forest was recently burned by a wildfire caused by lightning. The following episode has Liko and the others gather berries, break up soil, plant seeds and bring water to the damaged forest.

Sources:
https://www.pokemon.com/us/news/pokemon-horizons-the-series-part-1-recap-quiz-easy-version
https://www.pokemon.com/us/animation/horizons/1/the-future-i-choose

Reusable structure:

- ignition cause can be known without making the entire incident a villain plot;
- injured Pokémon and defensive wild behavior can persist after the flames are gone;
- recovery can involve soil, plants, water, care and wild Pokémon rather than one combat objective;
- a burned location can remain narratively important after the emergency phase ends.

Guardrail:

The episode contains extraordinary Pokémon actions. Ouros must not infer that Rain Dance restores habitat, that a Grass Pokémon can accelerate regional recovery, or that a specific Ability can repair wildfire damage unless PTU/Caelo and the engine explicitly support that exact effect.

### 2. Pokémon Ranger material separates fire response from later access

The official episode “The Green Guardian” presents a forest fire threatening wild Pokémon. Celebi contains the fire, becomes exhausted, and later vegetation blocks a public road. A Pokémon Ranger coordinates access and recruits nearby Pokémon to clear a route.

Source:
https://www.pokemon.com/us/animation/seasons/9/episode-10-the-green-guardian

Reusable structure:

- a fire can create secondary infrastructure problems after the flames are controlled;
- responders can need temporary access restrictions and route management;
- Pokémon assistance can be task-specific and temporary;
- ecological response and transport recovery can overlap without being the same system.

Do not copy the Celebi plot, specific Ranger actions or route sequence.

### 3. PTU encourages environmental opportunities but does not establish a wildfire simulator

The public PTU first-session GM guide gives an example where an oil canister can be ignited to create a wall of fire during a battle. The purpose is to encourage players to use the environment rather than only character-sheet actions.

Source:
https://pokemontabletop.com/gm-advice-your-first-ptu-session/

Reusable structure:

- environmental facts can matter tactically when the governing rules and encounter contract support them;
- battle terrain can contain authored opportunities;
- narrative context should not hard-code the combat result.

Mechanical caution:

This example does not prove a general wildfire propagation model, fire spread rate, smoke rules, ignition probability, structure-burning system or persistent battlefield fire zones in AutoPTU-Java.

### 4. A public Pokémon Ranger quest uses wildfire as a multi-system emergency

The public Sufficient Velocity quest `Unprecedented Times` includes a wildfire near a town during a dry period. The fire displaces wild Pokémon into the settlement, creating both response and ecological problems. The mission framing includes helping local fire services while avoiding further ecological damage.

Source:
https://forums.sufficientvelocity.com/threads/unprecedented-times-a-pokemon-ranger-quest.121855/page-4

Reusable structure:

- wildfire can create wildlife displacement rather than only direct fire damage;
- responders may have simultaneous goals that can conflict;
- protecting people, protecting wildlife and suppressing fire can require different actions;
- dry-season context can matter without turning climate state into a battle modifier.

Copyright boundary:

Use only the abstract pattern. Do not copy its region, disaster cause, mission text, organizations or characters.

### 5. Fire severity should be spatial, not one binary flag

The U.S. National Park Service describes fire as producing a patchwork of burn severities and unburned areas. Fire can create a sequence of changing habitats through ecological succession.

Sources:
https://www.nps.gov/brca/learn/nature/fire-ecology.htm
https://www.nps.gov/articles/wildland-fire-ecology-brief.htm
https://www.nps.gov/yose/learn/nature/wildlife-fire.htm

Reusable structure for Ouros:

- represent a fire scar as multiple spatial patches;
- preserve unburned refugia;
- allow lightly burned, severely burned and unburned areas to recover differently;
- change habitat opportunities over time rather than snapping back to the old encounter table;
- let dead trees, open canopy, regrowth and later mature vegetation support different ecological observations.

Important simplification:

Ouros should not simulate every tree. A coarse patch/state model is enough for regional narrative and spawn projection.

### 6. Post-fire recovery can require years of observation

Australian bushfire-recovery programs track burned and unburned areas, refugia, flora/fauna surveys, erosion control, habitat structures, weed pressure and long-term baseline datasets.

Sources:
https://www.dcceew.gov.au/environment/biodiversity/bushfire-recovery
https://www.dcceew.gov.au/environment/biodiversity/bushfire-recovery/activities-and-outcomes
https://www.dcceew.gov.au/environment/biodiversity/bushfire-recovery/bushfire-impacts

Reusable structure:

- immediate rescue and long-term ecological recovery are different phases;
- unburned refuges can become disproportionately important after a severe event;
- recovery may need erosion control, habitat structures, weed management and repeated surveys;
- a project can produce new baseline datasets rather than an instant “restored” flag;
- recovery success can vary by species and patch.

Do not import Australian species, law, agency structures, funding amounts or management policies into Ouros.

### 7. Fire can be ecologically normal, beneficial, harmful or catastrophic depending on regime and context

NPS fire-ecology material emphasizes that many ecosystems are adapted to recurring fire and that fire can create habitat diversity. It also distinguishes severity and succession rather than treating all fire as ecological destruction.

Sources:
https://www.nps.gov/yose/learn/nature/fireecology.htm
https://www.nps.gov/articles/denali-fire-ecology.htm

Reusable structure:

- a low-severity burn should not automatically create a crisis arc;
- some locations may have authored fire regimes;
- too-frequent, too-severe or badly timed fires may have different consequences from expected fire;
- absence of fire can also alter habitat in systems that depend on recurring disturbance;
- “fire present” is not enough information to infer ecological effect.

### 8. Cultural burning is place-specific knowledge and must not be fictionalized casually

Australian government material describes cultural burning as knowledge-led, place-specific practice that can create mosaic burns and support ecological and cultural objectives. It explicitly stresses the role and authority of Traditional Custodians and knowledge holders.

Sources:
https://soe.dcceew.gov.au/extreme-events/environment/bushfires-and-wildfires
https://www.dcceew.gov.au/about/news/restoring-koala-habitat-cultural-burning

Design lesson for Ouros:

- management fire can be intentional and ecologically informed;
- authority, local knowledge, timing and place matter;
- a planned burn should have objectives, responsible actors, monitoring and review.

Cultural-safety boundary:

Do not transplant real First Nations cultural-burning practices, names, ceremonies, knowledge claims or institutions into fictional Ouros cultures. If Ouros later contains authored traditions involving fire stewardship, they must be original, reviewed worldbuilding rather than a reskin of living Indigenous practice.

### 9. Fire can create delayed watershed hazards after the emergency ends

USGS research shows that wildfire can change soil infiltration, runoff and erosion. Later rainfall can move ash, sediment and debris into waterways, produce debris flows and degrade downstream water quality.

Sources:
https://www.usgs.gov/publications/post-wildfire-debris-flows
https://www.usgs.gov/mission-areas/water-resources/science/water-quality-after-wildfire
https://www.usgs.gov/mission-areas/water-resources/science/hydrologic-and-erosion-responses-burned-watersheds

Reusable structure:

- the first major rain after a fire can create a new crisis without being a second unrelated random event;
- fire severity, slope and watershed connectivity can generate downstream consequences;
- reservoir, treatment-plant and aquatic-habitat problems can emerge later;
- a burned catchment should connect directly to the freshwater layer.

Do not import real-world debris-flow thresholds or water-quality numbers as Ouros mechanics.

### 10. Smoke footprint and fire perimeter should be separate

Fire ecology and sky-observation research already imply that smoke can affect places far outside the active burn perimeter. This pass formalizes the distinction for world state.

Reusable structure:

- fire perimeter answers where active burning is occurring;
- smoke footprint answers where visibility/air-quality observations are affected;
- a town can experience smoke without being threatened by flames;
- observatory visibility, transport operations, public events and health signals may react to smoke separately.

Mechanical caution:

Smoke does not automatically create Accuracy penalties, suffocation, Poisoned, Blindness or other PTU effects. Those require exact rules and implementation evidence.

## Cross-system lessons for Ouros

### Use a fire-event chain rather than a single crisis flag

Recommended chain:

ignition observation → cause hypotheses → active perimeter → severity mosaic → containment/suppression state → fire scar → ecological response → post-fire watershed response → recovery monitoring → long-term fire-regime update.

Not every fire needs every stage.

### Preserve cause uncertainty

Lightning, infrastructure failure, deliberate ignition, accidental ignition and volcanic/other natural sources must remain claims until evidence supports them.

A Fire-type Pokémon seen nearby is not proof of ignition.

### Preserve unburned refugia

The world should retain small unburned or lightly burned areas inside a larger scar. These can matter for wildlife, later recovery, research and route planning.

### Preserve post-fire succession

A location can pass through multiple ecological states:

- active burn;
- recently burned;
- early regrowth;
- shrub/young growth;
- later recovery;
- changed long-term community.

The exact stages should be authored per biome rather than universal.

### Connect fire to existing systems

Wildfire can legitimately affect:

- crisis response;
- wildlife collectives and displacement;
- care facilities;
- route access and transport;
- meteorology and smoke visibility;
- freshwater catchments;
- sanitation and water treatment;
- conservation/refugia;
- science and monitoring;
- public memory;
- architecture and infrastructure;
- settlement capacity;
- tourism and events.

The fire layer should emit state to those systems rather than recreate them.

## PTU / Caelo mechanical caution

Available project evidence supports selected PTU concepts such as Burned, Fire-type interactions, Firestarter, terrain-linked Features and individual environmental examples. Python AutoPTU also contains specific status, terrain and Feature logic.

None of that establishes a complete wildfire rules subsystem.

Do not invent from this research:

- fire spread per round;
- ignition chance from a Fire Move;
- wildfire damage;
- smoke damage;
- smoke Accuracy/Evasion penalties;
- oxygen/suffocation rules;
- structure-burning HP;
- water-volume extinguishing rules;
- Rain Dance extinguishing wildfire;
- Firestarter suppression/ignition rules beyond its exact source text;
- ember zones;
- moving flame fronts;
- wind-driven knockback;
- heat exhaustion;
- automatic Burned from entering a burned tile;
- automatic immunity for Fire-type Pokémon to environmental wildfire;
- firefighting Skill DCs;
- special capture modifiers for displaced Pokémon.

## Engine implications

Mechanically rich wildfire battles depend heavily on capability families that remain incomplete in Java:

- terrain / weather / hazards / zones / reactions;
- complete movement when a fire front or evacuation forces movement;
- AI tactical policy for retreat, evacuation, protection or fire-avoidance goals;
- full lifecycle for timed spread or duration effects;
- Minecraft/Cobblemon/Craftics playback for safe visual synchronization.

Reduced encounters can still use static arenas with world-state fire handled before and after battle.

## Research gaps

Future work should resolve:

- exact PTU/Caelo text for Firestarter, Burned, smoke/visibility if any, weather interactions and environment-specific Features;
- whether Caelo defines authored wildfire, ash, smoke or fire-zone rules;
- Cobblemon/Minecraft hooks for fire blocks, smoke/particles, biome state and safe server-authoritative presentation;
- whether Java eventually exposes battlefield hazard/zone state suitable for dynamic fire;
- what Ouros biomes have fire-adapted, fire-sensitive or rarely burned authored regimes;
- which institutions are responsible for wildfire response and landscape stewardship in canon.

## Provenance rule

External Pokémon episodes, PTU advice, public roleplay/quest material and real-world fire-ecology sources are research references only. Ouros must use original places, institutions, cultures, species combinations and plots. Real Indigenous fire-management practices must never be copied into fictional cultures as flavor.