# Soil Health, Erosion & Land Restoration — Research Scan 67

Status: external research and provenance. Not canon. Not a rules source.

Date: 2026-08-20

## Why this pass exists

Ouros already has dedicated layers for Geology, Agriculture, Freshwater, Wildfire, Cryosphere, Volcanism, Conservation, Architecture and Travel. Several of those documents reference soil, erosion, runoff, exposed substrate or disturbed land, but none owns persistent surface-soil condition.

A repository-wide search for soil/erosion/compaction/fertility terminology did not find a dedicated soil systems layer. The Agriculture layer already points to `soil_or_habitat_state_ids`, which is an explicit integration seam rather than a complete implementation.

This pass fills that seam.

Its purpose is to support stories where land changes slowly or cumulatively: foot traffic compacts an orchard, rain cuts a gully through a burned slope, construction stockpiles topsoil, a restored wetland recovers after trampling, or a Pokémon's digging changes local structure. It does not turn soil science into automatic PTU combat rules.

## Source 1 — Dugtrio official Pokédex

Source: https://www.pokemon.com/us/pokedex/dugtrio

The official Pokédex describes Dugtrio loosening nearby soil through the movement of its heads, making burrowing easier.

Reusable structure:

- Pokémon can physically alter soil structure through ordinary behavior;
- the same behavior may affect route stability, agricultural land or habitat differently depending on context;
- repeated Pokémon activity can be a world-state cause rather than a one-off visual effect.

Mechanical caution:

This lore does not mean every Dugtrio automatically creates PTU Rough Terrain, grants Groundshaper, damages structures, increases crop yields or changes Minecraft blocks permanently.

## Source 2 — Swinub official Pokédex

Source: https://www.pokemon.com/us/pokedex/swinub

Swinub searches for food by digging into soil and can uncover hot springs. It can also dig through frozen ground.

Reusable structure:

- digging can expose hidden geological or geothermal information;
- a small Pokémon behavior can create a discovery hook without the Pokémon being an antagonist;
- frozen surface appearance does not mean the underlying ground is inaccessible to every species.

This connects Soil with Cryosphere, Geology and Volcanism.

## Source 3 — Excadrill and Drilbur official Pokédex material

Discovery references:

- https://www.pokemon.com/us/pokedex/excadrill
- https://www.pokemon.com/us/pokedex/drilbur

High-level observations:

- some Pokémon move efficiently through soil and create extensive underground spaces;
- repeated burrowing can intersect with human infrastructure;
- subsurface activity can be useful, disruptive or neutral depending on location.

Ouros should preserve that uncertainty. A cracked service tunnel near a burrowing population is evidence of overlap, not automatic proof that the Pokémon caused the damage.

## Source 4 — Zarude official Pokédex

Source: https://www.pokemon.com/us/pokedex/zarude

Zarude's shed vines are described as becoming soil nutrients that help forest plants grow.

Reusable structure:

- Pokémon-derived organic material can become part of nutrient cycling;
- soil condition can have biological causes and history;
- a forest can recover through many small inputs instead of one magical restoration event.

Do not import a generic fertilizer bonus, yield modifier or accelerated restoration timer from this lore.

## Source 5 — Eldegoss official material

Sources:

- https://www.pokemon.com/us/pokedex/eldegoss
- https://swordshield.pokemon.com/en-ca/pokemon-galar-region/eldegoss/

Official descriptions connect Eldegoss seed dispersal with nutrient-rich seeds and soil enrichment in Galar.

Reusable structure:

- wind-dispersed biological material can connect one habitat to another;
- Pokémon ecology can contribute to soil change without ownership or direct Trainer command;
- a regional agricultural tradition may observe and value a species' role without turning every individual into farm equipment.

## Source 6 — Landorus official Pokédex

Source: https://www.pokemon.com/us/pokedex/landorus

Landorus is exceptionally associated with enriching soil and abundant harvests, and has a cultural title tied to fields.

This is useful primarily as a boundary case.

Ouros must not generalize an exceptional Legendary association into a universal soil-restoration mechanic. It also must keep cultural belief, observed soil change, Legendary presence and mechanical effect separate.

A local story saying that fertile ground is a blessing from a Legendary can be culturally important even if the causal mechanism remains unresolved.

## Source 7 — PTU campaign seed: Mysterious Ruins

Source: https://pokemontabletop.com/campaign-seeds-mysterious-ruins/

The Oran Valley seed starts with ordinary farmers, innkeepers and breeders in a farming town before subsurface discoveries disrupt daily life.

Reusable structure:

- productive land can have geological, archaeological and cultural layers beneath it;
- a farm or field can become an exploration site without ceasing to matter economically;
- excavation and continued land use can produce legitimate competing priorities;
- surface disturbance can reveal a deeper story instead of serving only as scenery.

Do not copy Oran Valley, its ruins, supernatural elements or named plot events.

## Source 8 — public PTU campaign anecdote

Discovery reference: public Pokémon Tabletop discussion where a field anomaly/dug patch becomes a paleontology clue.

Reusable structure only:

- players can notice a small disturbance before they understand its cause;
- wild Pokémon behavior can expose evidence without intentionally delivering a quest;
- expertise matters when converting a mundane observation into a useful hypothesis.

Community anecdotes are inspiration sources, never mechanical authority.

## Source 9 — NRCS: Understanding Soil Risks and Hazards

Source: https://www.nrcs.usda.gov/sites/default/files/2022-10/soil-risks-and-hazards.pdf

NRCS describes compaction as reduction of pore space. It can restrict infiltration, increase runoff and erosion, affect plant roots, and occur in cropland, parks, trails, construction zones, lawns and forests.

Reusable world-state structure:

`traffic / machinery / disturbance -> compaction observation -> reduced infiltration claim -> runoff observation -> downstream consequence`

Each arrow needs evidence. The game should not jump directly from visible footsteps to crop failure or flooding.

## Source 10 — NRCS soil-quality indicators

Discovery references:

- NRCS Soil Health assessment materials
- NRCS Soil Quality Information Sheets

Relevant high-level indicators include:

- organic matter;
- bulk density/compaction;
- infiltration;
- aggregate/structure condition;
- soil depth;
- water-holding behavior;
- biological indicators;
- erosion evidence.

Design lesson:

`soil_quality = 72` is too lossy for Ouros.

A site can have good infiltration but poor nutrient state, good fertility but severe compaction, or stable surface cover with a deeper restrictive layer.

## Source 11 — NRCS organic matter and infiltration

NRCS material links organic matter and stable aggregates with improved infiltration and reduced runoff/erosion risk.

Reusable structure:

- restoration can change several indicators over time;
- a visual green-up is not enough to declare the soil restored;
- management history matters when interpreting later observations.

Exact agronomic formulas are outside Ouros narrative authority.

## Source 12 — FAO soil degradation and conservation

Discovery references:

- https://www.fao.org/soils-portal/soil-management/soil-conservation/en/
- FAO land degradation/restoration materials
- FAO soil erosion materials

FAO treats erosion as one form of land degradation among several, alongside physical, chemical and biological degradation. Soil conservation can address erosion, compaction, salinity, fertility and soil-water problems.

Reusable structure:

- erosion should not become the universal explanation for every damaged field;
- restoration should respond to the actual limiting condition;
- a site may need different interventions in different zones;
- restoration success should be assessed over time, not declared immediately after work is completed.

## Source 13 — urban and recreational compaction

NRCS urban-soil guidance identifies concentrated foot traffic, construction/demolition and heavy machinery as common compaction pressures.

A recent protected-area soil study also shows how visitor/off-road pressure can compact and crust soil, and how soil mapping can support targeted closures or rehabilitation rather than blanket exclusion.

Reusable Ouros structure:

- festivals, tourist surges, construction and repeated Trainer traffic can leave persistent land-condition consequences;
- visitor management can redirect pressure instead of closing an entire destination;
- trail recovery can itself become a measurable long-term project.

## Cross-layer synthesis

### Agriculture

Agricultural sites should reference a versioned soil/land unit rather than store a vague internal `soil_quality` field.

Soil condition can affect narrative expectations, planting decisions, investigation and restoration planning. Exact Berry yields, growth rates and Chef/food mechanics remain authoritative elsewhere.

### Freshwater

Erosion source and sediment destination are separate state.

A gully on a hillside can later affect a stream, reservoir, wetland or irrigation channel. The downstream sediment may be harmful, neutral or locally useful depending on context.

### Wildfire

Post-fire loss of cover can raise erosion/runoff concerns, especially when later rain arrives. Fire history should reference soil units; the Soil layer should not recalculate fire severity.

### Cryosphere

Freeze/thaw, snowmelt and frozen surfaces can change infiltration or surface condition. Cryosphere owns snow/ice state; Soil owns the land response.

### Volcanism

Ash, tephra and new volcanic substrate can alter land condition over time. Fresh ash is not automatically fertile soil, and a volcanic deposit does not instantly create productive farmland.

### Architecture, Travel and Tourism

Construction, roads, trails, crowds and repeated vehicle/service traffic can compact or seal ground. Built-environment state identifies where disturbance occurs; Soil records the resulting surface condition.

### Conservation

Protected areas can use soil-sensitive zoning, restoration plots and monitoring without turning every visitor into a rule violation.

### Archaeology and Geology

Soil horizon/context can preserve archaeological and geological information. Removing material can destroy provenance even when the recovered object survives intact.

## PTU / Caelo boundary

Available project evidence confirms narrow mechanics related to terrain and ground manipulation.

Python AutoPTU contains a `Mold the Earth` implementation that requires both the specific Trainer Feature and Groundshaper capability, and can create rough ground plus Spikes under its exact rule path.

That is evidence for one authored mechanic. It is not permission for narrative soil state to call Groundshaper automatically.

Project evidence also contains Naturewalk terrain handling. That remains individual/mechanical capability state, not a generic benefit assigned because a Pokémon lives in a soil-associated habitat.

Do not infer or invent:

- automatic Rough Terrain from bare soil;
- automatic Slow Terrain from mud;
- erosion damage;
- gully fall damage;
- sink or slip checks;
- dust Accuracy penalties;
- compaction movement penalties;
- fertility bonuses;
- crop-yield modifiers;
- Ground-type damage bonuses;
- Groundshaper access from species flavor;
- Naturewalk access from habitat flavor;
- Spikes from digging;
- landslide rules;
- excavation DCs;
- soil-restoration Skill checks;
- automatic Poison/Burn/other Status from contaminated soil;
- automatic Legendary soil enrichment;
- Minecraft block state as PTU terrain authority.

The full Caelo primary corpus was not reliably available in this runtime. No Caelo-specific soil, farming, Groundshaper, Survival or terrain rule is asserted here.

## Research-to-design conclusions

1. Soil needs persistent identity independent of Minecraft blocks and geological substrate.
2. Physical, chemical and biological condition should remain separable rather than one score.
3. Observation, assessment, causal hypothesis and management decision are different records.
4. Erosion source and sediment destination require linked but distinct events.
5. Compaction can accumulate from ordinary traffic and infrastructure use.
6. Pokémon can alter soil through normal behavior without becoming tools or automatic culprits.
7. Restoration should create a monitored trajectory, not an instant `fixed=true` state.
8. A visually green or muddy site does not establish authoritative soil condition.
9. Soil can connect Agriculture, Freshwater, Wildfire, Cryosphere, Volcanism, Conservation and Travel through causal world-state edges.
10. AutoPTU receives only explicitly validated battlefield terrain/effects; most soil stories can progress safely in overworld state before those families are complete.
