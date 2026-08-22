# Pass 94 Research — Kelp Forests, Seagrass Meadows & Submerged Vegetation

Status: RESEARCH / PROVENANCE. Not canon. No PTU mechanic is established by this document.

Date: 2026-08-21

## Why this pass exists

The repository already has dedicated systems for Maritime, Open Ocean, Estuaries, Coral Reefs, Intertidal zones, Fisheries, Freshwater, Coastal Geomorphology and underwater travel-adjacent world state. None of those layers owns persistent submerged vegetation as habitat in its own right.

Kelp forests and seagrass meadows need a separate layer because they can change physical structure, nursery value, water movement, visibility, settlement/use pressure and ecological relationships without being reefs, open ocean, shoreline geomorphology or ordinary terrestrial flora.

The main design question for Ouros is not “what bonus does kelp give?” It is “how does a persistent submerged habitat change over time, what evidence supports that change, what does it cause in the world, and which parts can safely enter AutoPTU?”

## Internal repository review

Before writing, the current branch tree was inspected across README, design, research and proposals. Relevant existing layers include:

- Maritime / Coasts / Depths;
- Open Ocean;
- Coral Reef Ecology & Restoration;
- Estuaries / Tidal Wetlands / Salinity;
- Intertidal / Tidepool / Rocky Shore;
- Fisheries / Angling / Aquaculture;
- Conservation / Protected Areas / Stewardship;
- Interspecies Ecological Relations;
- Biosecurity / Introduced Species / Translocation;
- Water Quality / Waste / Air Quality / Stormwater;
- Seasonality / Meteorology / Coastal Geomorphology;
- Photography / Science / Cartography.

No existing layer owns kelp-canopy identity, seagrass-bed extent, submerged-vegetation recruitment, canopy loss, grazing-state transition, vegetated nursery occupancy or restoration cohorts specific to submerged vegetation.

## Source set

### Official Pokémon species material

1. Pokémon Pokédex — Skrelp
https://www.pokemon.com/us/pokedex/skrelp

Reusable structure:
Skrelp hides among drifting seaweed, feeds on rotten seaweed and can be washed far from home during strong storms. This supports authored species-level relationships among seaweed cover, concealment, food and displacement.

Do not infer:
- generic Stealth bonuses in kelp;
- automatic Poisoned zones from rotten seaweed;
- currents or storm displacement rules;
- that every Skrelp observation indicates a permanent resident population.

2. Pokémon Pokédex — Dragalge
https://www.pokemon.com/us/pokedex/dragalge

Reusable structure:
Dragalge can approach prey under seaweed cover and has a territorial behavioral hook.

Do not infer:
- tactical cover from kelp without a verified terrain/visibility contract;
- territorial AI for every Dragalge;
- environmental poison from simple presence.

3. Pokémon Pokédex — Dhelmise
https://www.pokemon.com/us/pokedex/dhelmise

Reusable structure:
Dhelmise is explicitly connected to seaweed and ship debris. It can therefore support stories where habitat, wreck provenance and a persistent Pokémon entity overlap.

Do not infer:
- every wreck with seaweed creates Dhelmise;
- Dhelmise owns wreck debris;
- anchor-like geometry grants Pull, Grapple or forced movement unless PTU rules and Java support establish it.

4. Pokémon Pokédex — Lileep
https://www.pokemon.com/us/pokedex/lileep

Reusable structure:
Lileep is a fossil organism associated with the seabed and a much older marine environment. It can support paleobiology comparisons between ancient marine structure and modern submerged habitats.

Do not infer:
- modern kelp is equivalent to Lileep habitat;
- fossil restoration establishes exact ancient ecosystem composition;
- Suction Cups creates environmental anchoring rules outside its actual mechanic.

### NOAA / NPS — kelp forests

5. NOAA National Marine Sanctuaries — Kelp Forest
https://sanctuaries.noaa.gov/visit/ecosystems/kelpdesc.html

Reusable structures:
- kelp forests are vertically structured, with canopy, midwater and seafloor layers;
- layered structure supports different organisms and behaviors;
- overgrazing can shift a kelp-dominated system toward an urchin barren;
- monitoring and restoration are separate from declaring recovery.

Ouros lesson:
Submerged vegetation can have internal vertical zones without requiring a 3D battle engine. The world layer can preserve canopy, midwater and holdfast-zone state while a current encounter still freezes one legal tactical projection.

6. NOAA Fisheries — Kelp Forest Habitat on the West Coast
https://www.fisheries.noaa.gov/west-coast/habitat-conservation/kelp-forest-habitat-west-coast

Reusable structures:
- kelp distribution depends on light, nutrients, temperature, currents and rocky substrate;
- kelp reduces current speed inside the forest;
- kelp functions as a foundational habitat whose effects extend beyond its exact footprint;
- detached kelp can form floating habitat in open water.

Ouros lesson:
A kelp bed should not be a binary tile tag. It can have canopy extent, density, substrate attachment, exposure history and detached-mat events.

7. NPS — Kelp Forest Community Monitoring
https://www.nps.gov/im/medn/kelp-forest-communities.htm

Reusable structures:
- repeated monitoring of the same sites is needed to detect change;
- canopy loss can result from interacting natural and human pressures;
- nursery function and community composition can change before or after obvious visual collapse.

Ouros lesson:
A photograph of “lots of kelp” does not prove ecosystem recovery. Monitoring needs date, site, method and indicator context.

8. NOAA — Restoring Balance: What Sea Urchins Reveal About Ecosystem Health
https://sanctuaries.noaa.gov/news/2026/restoring-balance.html

Published 2026-06-25.

Reusable structure:
The same ecological actor can play a normal role at one abundance and contribute to regime shift at another. Restoration targets relationships, not moral categories.

Ouros lesson:
Do not write “grazer = bad.” A grazer population can be normal, overabundant, recovering, displaced or responding to predator loss. Management proposals need evidence and scope.

### NOAA / NPS — seagrass and submerged aquatic vegetation

9. NOAA Fisheries — Restoring the Indian River Lagoon’s Seagrass Meadows and Wetlands
https://www.fisheries.noaa.gov/feature-story/restoring-indian-river-lagoons-seagrass-meadows-and-wetlands

Published 2026-03-05.

Reusable structures:
- seagrass can anchor a food web and shelter juvenile organisms;
- sediment stabilization and water clarity are linked to vegetation state;
- restoration can require system-wide work, not one planting event;
- severe algal-bloom periods can produce large habitat losses.

Ouros lesson:
Seagrass restoration should have baseline, intervention, survival/recruitment follow-up and water-quality dependencies. Completion of planting does not equal recovery.

10. NOAA Fisheries — Why Is Submerged Aquatic Vegetation Designated As Essential Fish Habitat?
https://www.fisheries.noaa.gov/southeast/habitat-conservation/why-submerged-aquatic-vegetation-designated-essential-fish-habitat

Published 2026.

Reusable structures:
Submerged aquatic vegetation can support feeding, reproduction, shelter and nursery use and can host attached organisms. Its ecological role is broader than “underwater grass.”

Ouros lesson:
A vegetation unit can have multiple ecological functions simultaneously. The system should record observed function rather than hard-code a universal nursery bonus.

11. NOAA Fisheries — Seagrass on the West Coast
https://www.fisheries.noaa.gov/west-coast/habitat-conservation/seagrass-west-coast

Reusable structures:
Seagrass beds can stabilize sediment, support juvenile fish and occur in bays, harbors and open coast settings. Development, poor water quality and vessel activity can affect them.

Ouros lesson:
Harbors and settlements can coexist with seagrass, creating legitimate infrastructure-versus-habitat decisions rather than automatic villainy.

12. NOAA Fisheries — Indian River Lagoon benthic cover monitoring
https://www.fisheries.noaa.gov/inport/item/78513

Published 2026-02-17.

Reusable structure:
Repeated mapping of submerged vegetation can act as an indicator of environmental change and management outcomes.

Ouros lesson:
Vegetation extent should be versioned spatial data, not only prose. Old maps remain historically valid for their survey date.

### PTU community / campaign practice

13. r/PokemonTabletop — How do you handle water type Pokémon?
https://www.reddit.com/r/PokemonTabletop/comments/e5dfuz

14. r/PokemonTabletop — How do I handle water type Pokémon?
https://www.reddit.com/r/PokemonTabletop/comments/r9am9x

Reusable lesson:
Community discussion repeatedly exposes the same campaign-design pressure: aquatic Pokémon become either unusable or arbitrarily hand-waved if the environment does not respect their actual movement capabilities.

Ouros use:
Build underwater and nearshore adventures around explicit route and movement capability gates. Do not grant floating, water bubbles, suffocation rules or house-rule Levitate from community suggestions.

15. r/PokemonTabletop — Pokémon without a Swim Capability
https://www.reddit.com/r/PokemonTabletop/comments/eazaut

Reusable lesson:
Community uncertainty around Swim demonstrates why this project must defer to PTU/Caelo source text and the project oracle rather than filling gaps through intuition.

### Fangames / exploration design

16. Eevee Expo — Pokémon Gaia
https://www.eeveeexpo.com/gaia/

Reusable structure:
Dive and underwater maps work well as a distinct exploration layer linked to hidden locations and optional discoveries.

17. Eevee Expo — Pokémon Potassium
https://mail.eeveeexpo.com/threads/9542/

Reusable structure:
Multiple underwater biome layers and propulsion gimmicks show how vertical/submerged exploration can become visually distinct.

Do not import:
custom stat boosts, artifact systems, puzzle rules, custom Moves or its specific biome layouts.

## PTU / project evidence

The currently available project evidence contains an AutoPTU Python `can_swim()` boundary. Swim is treated as a movement capability and can also be present as a capability label. The same code handles Naturewalk labels separately.

Available evidence also shows a concrete Wilderness Guide branch for `ocean` / `wetlands` that can apply specific temporary effects when the Feature exists and resolves legally.

This is narrow evidence only.

Do not infer:
- kelp = Ocean terrain;
- seagrass = Wetlands terrain;
- submerged vegetation = Naturewalk;
- kelp canopy = cover or concealment;
- water plants = movement bonus;
- kelp entanglement = Stuck;
- seaweed = Poisoned;
- underwater vegetation = tactical zone.

The complete Caelo primary corpus was not recovered reliably in this run. No Caelo-specific aquatic, underwater, kelp, seagrass or visibility mechanic is claimed here.

## Reusable Ouros structures

### Persistent habitat identity

The same kelp forest or seagrass meadow should remain one entity through canopy loss, storm damage, grazing shifts, restoration and regrowth.

### Vertical ecological structure without mandatory 3D combat

A kelp forest can contain canopy, midwater and seafloor ecological bands. These affect observations and habitat use even if the current battle engine supports only a frozen 2D projection.

### Vegetation extent is versioned

Maps can show different extents in different years. An old map can be correct for its date.

### Visual abundance is not recovery

A visually dense canopy can still have poor recruitment or altered community structure. A sparse bed can be recovering.

### Nursery function requires evidence

Do not label every bed a nursery. Record juvenile observations, spawning use, repeated occupancy or authored regional ecology.

### Regime shifts are relationship changes

A kelp forest can shift toward a grazer-dominated barren. Do not moralize the grazer species. Preserve predator, grazer, habitat and disturbance evidence separately.

### Floating vegetation can leave the habitat

Detached kelp mats can become temporary open-ocean habitat and connect this layer to Open Ocean and Maritime without copying the entire kelp forest identity.

### Restoration is a longitudinal project

Planting, transplanting, grazer management, access controls or water-quality work require monitoring. A completed intervention does not automatically become successful restoration.

## Candidate handoffs to existing layers

Maritime:
nearshore route changes, vessel interactions, dive access and detached kelp mats.

Open Ocean:
floating kelp habitat after detachment.

Coral Reef:
adjacent rocky reef state and shared grazers/predators, without merging reef and kelp identities.

Fisheries:
juvenile habitat, observed fishing effort and stock-assessment context.

Estuaries:
seagrass beds in salinity-gradient environments.

Coastal Geomorphology:
substrate, sedimentation and shoreline change affecting shallow vegetation.

Stormwater / Waste / Air / Wildfire:
water-quality or sediment inputs that may alter submerged vegetation after evidence is collected.

Conservation:
restoration projects, protected zones, visitor/anchoring policy and stewardship.

Science / Photography / Cartography:
transects, canopy maps, underwater imagery and time-series evidence.

Cobblemon:
coarse presence opportunities after ecology validation; never loaded-entity truth.

AutoPTU:
a frozen encounter snapshot only after exact terrain, visibility, movement, hazard and Ability dependencies are verified.

## Copyright / transformation guardrail

No protected plot, dialogue, character, map or distinctive fangame scenario is copied into Ouros. Pokémon species material is used as factual/lore reference for high-level behavior. Community/fangame material contributes only abstract encounter and exploration structures. NOAA/NPS material contributes ecological system concepts and monitoring/restoration logic.

## Conclusion

Submerged vegetation should become a first-class persistent habitat in Ouros. The strongest design opportunity is not to turn kelp into a combat modifier. It is to let the same underwater forest or meadow accumulate history through storms, grazers, water quality, restoration, fisheries, tourism, wrecks and Pokémon observations, while battle mechanics remain behind explicit PTU/Java capability gates.