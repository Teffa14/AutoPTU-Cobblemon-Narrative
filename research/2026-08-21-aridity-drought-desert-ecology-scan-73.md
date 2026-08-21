# Aridity, drought & desert ecology research — pass 73

Status: RESEARCH ONLY. Not Ouros canon. External sources are used for high-level structural inspiration and factual reference. No external plot, dialogue, distinctive character, location or rules text is imported into Ouros.

## Why this pass exists

The repository already contains dedicated systems for meteorology, freshwater, soil, flora, wildfire, cryosphere, hydrology, tourism, travel, conservation and wild Pokémon ecology. It did not contain a dedicated contract for arid-land state: prolonged water deficit, ephemeral pools and streams, desert refuges, exposed-soil/dust source areas, drought response, dryland route pressure and the difference between an overworld dry spell and a PTU Sandstorm.

This pass therefore focuses on drylands as persistent systems rather than treating `desert` as a visual biome or a permanent battle-weather flag.

## Source scan

### Pokémon species-level desert adaptations

Official Pokédex material gives several useful examples of species-specific adaptation rather than a universal desert template.

Sandile lives beneath hot desert sand and moves through sand while remaining hidden. This supports subterranean or sand-buried presence as a species-grounded behavioral possibility, not a generic capability for Ground-types.

Source: https://www.pokemon.com/us/pokedex/sandile

Trapinch lives in arid deserts and constructs funnel-shaped nests in sand. This supports persistent micro-sites created by a particular species, but does not authorize the narrative layer to create Arena Trap, trapping damage or forced movement without the actual PTU mechanic.

Source: https://www.pokemon.com/us/pokedex/trapinch

Hippopotas travels through desert sand and can live in colonies. This supports observed group presence in sandy habitat, but collective identity and tactics still belong to the Wild Collective layer and require evidence.

Source: https://www.pokemon.com/br/pokedex/hippopotas

Cacnea lives in arid environments, stores water and has a recurring flowering cycle. This is valuable because dryland ecology can include phenology and rare short biological windows instead of being static brown terrain.

Source: https://www.pokemon.com/us/pokedex/cacnea

### Desert locations as layered exploration spaces

Unova's Desert Resort combines persistent sandstorm presentation, deep sand, broad open terrain, ruins, ancient structures and a changing relationship with Relic Castle. Later versions alter access because parts of the structure become buried. This is useful as a high-level example of a desert location changing accessibility and preserving older layers beneath moving material.

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Desert_Resort
- https://bulbapedia.bulbagarden.net/wiki/Relic_Castle

This material is used only structurally. Ouros should not recreate Desert Resort, Relic Castle, its statues, quicksand puzzle, fossils, encounters or storyline.

### Community desert-design patterns

A public Pokémon RMXP map discussion describes an oasis settlement positioned as a haven for travelers and merchants within a broader arid landscape. Another desert-map discussion emphasizes repeated traversal, progressively opening areas, hidden caves and stronger visual/ecological differentiation around water sources.

Sources:
- https://www.reddit.com/r/PokemonRMXP/comments/nyx06w/
- https://www.reddit.com/r/PokemonRMXP/comments/ufdawm/

Reusable structure only:
- water sources can organize settlement and travel;
- an arid region can contain distinct subzones rather than one homogeneous sand field;
- returning later can reveal routes or sites whose accessibility changed;
- water-adjacent vegetation should have a causal reason to differ from surrounding dryland.

No creator-specific town, character, secret, cave layout or plot is imported.

### Ephemeral water as a temporary ecosystem

The U.S. National Park Service documents desert potholes and ephemeral pools that fill after rain, support short-lived but important ecosystems, and then shrink or dry. Organisms may escape, resist desiccation or tolerate it in different life stages.

Sources:
- https://www.nps.gov/articles/ephemeral-pools.htm
- https://www.nps.gov/blca/learn/nature/potholes.htm
- https://www.nps.gov/care/learn/nature/desert-water.htm

Reusable structure:
- `water present` should be versioned state, not a permanent map property;
- biological activity can be tied to short windows after rain;
- the same basin can be dry, partially wet or full at different times;
- disturbance to a small pool can matter disproportionately because it is a scarce refuge;
- a dry pool is not necessarily dead or irrelevant state.

### Intermittent and ephemeral streams

USGS research notes that intermittent and ephemeral streams in drylands support both aquatic and terrestrial life, and that the timing and extent of flow can vary substantially across nearby reaches. Monitoring wetting/drying cycles is therefore important for identifying critical habitat and understanding route or ecosystem changes.

Sources:
- https://www.usgs.gov/publications/high-resolution-spatiotemporal-patterns-flow-landscape-scale-montane-non-perennial
- https://www.usgs.gov/publications/ecological-and-hydrological-significance-ephemeral-and-intermittent-streams-arid-and

Reusable structure:
- a channel can remain a persistent geographic entity when dry;
- water continuity can differ reach by reach;
- one storm can activate some channels and not others;
- dryland navigation should use current route/water knowledge rather than biome labels alone.

### Springs, seeps and drought refuges

NPS notes that springs, seeps and waterpockets can become especially important when drought reduces other water sources. These small water features support plants, wildlife and connectivity. A spring can also change toward a seep as output declines.

Sources:
- https://www.nps.gov/articles/000/nrca_care_2022_water.htm
- https://home.nps.gov/moja/learn/nature/researchneeds.htm

Reusable structure:
- a small persistent water point can become a regional node during drought;
- pressure on a refuge can come from wildlife, travelers, settlements or institutions simultaneously;
- a declining spring does not automatically prove regional drought because groundwater and local infrastructure also need investigation;
- management can protect access without establishing ownership over wild Pokémon using the site.

### Dust as a mobile consequence

NOAA and NPS material shows that dust events can originate from dry/exposed source areas and travel far beyond the source. Strong winds, dry surface conditions, sparse vegetation and particular landforms can increase dust emission. Recent NOAA work also links major blowing-dust periods with drought conditions in observed datasets.

Sources:
- https://www.nesdis.noaa.gov/about/k-12-education/dust-ash-fire-smoke/what-dust-storm
- https://www.nesdis.noaa.gov/news/noaas-satellites-detect-blowing-dust-events-impact-human-health-and-safety
- https://www.nps.gov/articles/white-sands-as-dust-emission-hotspot.htm
- https://www.usgs.gov/special-topics/drought/science/dryland-ecosystems

Reusable structure:
- dust source and dust impact can be geographically separate;
- dust should have provenance/source hypotheses rather than appearing as generic regional weather;
- exposed soil, vegetation state, drought and wind can interact;
- downstream consequences can touch visibility, transport, health surveillance, snowmelt research or observatory data without becoming automatic PTU effects.

## PTU / AutoPTU mechanical cross-check

The available Python AutoPTU oracle contains real Sandstorm behavior. At START phase it checks effective weather and applies one Tick of damage to non-Ground/Rock/Steel combatants unless an explicit immunity or blocking Ability/effect applies. It also contains specific interactions for Desert Weather, Sand Force, Sand Rush, Sand Veil, Sand Stream and Overcoat.

This is narrow evidence for a battle `Sandstorm` state. It does not prove an overworld drought, dust plume, dry channel, desert heat or loose sand should create that state automatically.

Available evidence: uploaded `battle_state.py`, especially START-phase weather handling.

The same Python oracle contains a terrain-sensitive Wilderness Guide implementation. In desert/tundra terrain it can grant specific temporary weather-related protections. Again, this proves a specific Trainer Feature behavior in the oracle; it does not grant every traveler desert immunity.

Available evidence: uploaded `battle_state.py`, WildernessGuideAction.

The live AutoPTU-Java main inspected for this pass is commit `fe572021445fa0aa862db17514ca2b7e2cff3b18` (2026-08-21). The commit projects canonical Trainer initiative entries from runtime state. Java's README still lists full damage, status controller, terrain, hazards, forced movement, reactions, complete hook registries, tactical AI and Minecraft/Cobblemon integration as incomplete.

Python AutoPTU main remains `e4bb0ca38b7018710af476ce365d515a387de4e7` in the inspected repository state.

## Hard boundaries for Ouros

The narrative layer must not infer any of the following merely because a region is arid or visually sandy:

- Sandstorm Weather;
- Sandstorm damage;
- Sunny/Harsh Sun effects;
- heat damage or dehydration damage;
- Accuracy or Evasion penalties from dust;
- Rough/Slow Terrain;
- Tripped from loose sand;
- Arena Trap or Sand Tomb effects;
- Burrow movement;
- Naturewalk (Desert);
- immunity for Ground/Rock/Steel/Fire types to environmental heat or dust;
- water-consumption meters;
- starvation/thirst clocks;
- dust-related status conditions;
- rare-spawn boosts after rain;
- automatic population collapse during drought.

Exact PTU/Caelo rules and AutoPTU-Java support must validate each tactical effect.

## Design lessons for Ouros

1. Drought is a duration-bearing world condition, not simply lack of rain today.
2. Drylands are mosaics: dunes, rocky surfaces, channels, springs, seeps, pools, refuges, settlements, fields and ruins can behave differently.
3. A channel remains geographically meaningful while dry.
4. Water points create temporary concentration without implying ownership, friendship or hostility among the Pokémon using them.
5. Biological responses should be species-grounded or observed rather than inferred from elemental type.
6. Dust needs a source footprint and transport path; the place experiencing dust may not be the place causing it.
7. After-rain biological windows can create observation, research and travel content without guaranteeing special encounters.
8. Scarcity should create choices and state, not repetitive survival chores.
9. Small refuges can have disproportionate ecological importance and therefore create conflicts among multiple legitimate interests.
10. A battle launched inside a dryland location should receive an explicit validated environment snapshot. The overworld biome alone cannot manufacture PTU Weather or Terrain.

## Research gaps

- Extract the exact PTU/Caelo rules for Sandstorm, Desert Weather, Naturewalk (Desert), Survival in harsh environments and any dehydration/heat guidance.
- Determine whether Caelo modifies Sandstorm or environmental survival.
- Inspect how AutoPTU-Java will initialize Weather/Terrain from `BattleEnvironmentState` once those families are fully ported.
- Decide which Ouros regions have authored arid or semi-arid regimes.
- Define how long drought state advances offline.
- Define coarse water-refuge state without simulating every Minecraft water block.
- Design anti-exploit rules before linking rain pulses or ephemeral water to Cobblemon spawn projections.
