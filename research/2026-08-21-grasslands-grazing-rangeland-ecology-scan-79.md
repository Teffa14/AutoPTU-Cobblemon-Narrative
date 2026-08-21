# Grasslands, Grazing & Rangeland Ecology Research Scan — Pass 79

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Not a PTU rules source.

Date: 2026-08-21

## Why this pass exists

The repository already has dedicated layers for wild collectives, flora, soil, agriculture, conservation, aridity, wildfire, freshwater, travel and workplaces. Those systems can all touch grasslands, but none currently owns persistent grazing pressure, herbivore-use mosaics, herd routes, pasture/range condition, congregation around water or the difference between wild grazing and managed husbandry.

This pass investigates grassland ecology, browsing/grazing pressure, large-herbivore movement, pasture/rangeland stewardship and herd-linked landscape change as a new connective layer.

## Internal overlap check

Inspected before writing:

- `design/wild-collective-agency-layer.md`
- `design/flora-pollination-seed-dispersal-layer.md`
- `design/soil-health-erosion-land-restoration-layer.md`
- `design/food-agriculture-hospitality-layer.md`
- `design/conservation-protected-areas-stewardship-layer.md`
- `design/aridity-drought-desert-ecology-layer.md`
- `design/wildfire-fire-ecology-landscape-recovery-layer.md`
- `design/freshwater-watersheds-hydrology-layer.md`
- `design/travel-transport-expedition-layer.md`
- `design/workplaces-professions-staffing-layer.md`
- `design/engine-readiness-snapshot-pass-78.md`

Wild Collectives already owns persistent group identity. Flora owns vegetation units and succession. Soil owns compaction/erosion observations. Agriculture owns productive sites. Conservation owns management decisions. Pass 79 therefore focuses on the interaction layer: where herbivore presence, grazing/browsing, trampling, water access, migration, fire history and human management produce persistent spatial patterns.

## Pokémon sources

### Bouffalant — herd structure can be species-specific world state

The official Pokédex describes Bouffalant living in herds of roughly twenty individuals and records a hierarchy associated with mane size.

Reusable structure:

- some species can have authored herd-size expectations or social structure;
- a visible subgroup may belong to a larger persistent herd;
- leadership/hierarchy can be observed or inferred from species-specific evidence rather than generic assumptions;
- a herd can move through multiple grassland units over time.

Do not infer:

- every Bouffalant group has exactly twenty members;
- mane size is a PTU combat bonus;
- herd rank implies universal obedience;
- all herd Pokémon use Bouffalant social rules;
- defeating a prominent individual dissolves the herd.

Source:
- https://www.pokemon.com/us/pokedex/bouffalant

### Wooloo — managed herd behavior and material culture can coexist

The official Sword/Shield Wooloo profile states that Wooloo live as a herd, mimic their Trainer or herd leader, dislike conflict, and produce fleece used as a regional specialty product.

Reusable structure:

- managed herds can be workplaces, material-culture sources and social groups simultaneously;
- movement/routine can be shaped by a handler without making the herd a single combat unit;
- shearing/production can create seasonal work, trade and craft provenance;
- retreat from conflict can be a behavior goal rather than a battle defeat state.

Do not infer:

- all Wooloo are domesticated;
- all herd members share ownership;
- wool yield is a free resource generator;
- Run Away defines overworld herd evacuation rules;
- a Trainer's ownership creates perfect command over every group member.

Sources:
- https://swordshield.pokemon.com/en-us/pokemon-galar-region/wooloo/
- https://www.pokemon.com/us/pokedex/wooloo

### Gogoat and Skiddo — work, herds and mobility are separate contracts

The official Gogoat Pokédex describes mountain herds and contests for leadership. Skiddo is described as historically used for travel in mountain communities.

Reusable structure:

- a herd species may have its own leadership behavior;
- a species can participate in work or transport through authored relationships;
- a local community may build traditions around a species without every individual serving people;
- herd ecology and service-Pokémon systems should remain separate.

Do not infer:

- all Gogoat are Mountable in every PTU/Caelo context;
- headbutting contests create battle stages or rank buffs;
- wild herds are available as public transport;
- Sap Sipper models grazing.

Sources:
- https://www.pokemon.com/uk/pokedex/gogoat
- https://www.pokemon.com/us/pokedex/skiddo

## PTU public material

### Mareep Family Spotlight — ranching can generate problems beyond battle

The Pokémon Tabletop blog's Mareep Family spotlight presents a ranch where wild predation, herd defense, evolution and the rancher's wool-based livelihood interact. It also proposes a second scenario where a large population of Mareep/Flaaffy/Ampharos creates unintended interference with aircraft through behavior rather than malice.

Reusable structures:

- a ranch problem can involve ecology + material economy + Pokémon development at once;
- making a herd stronger can produce unintended consequences;
- livelihood dependence on a Pokémon product can create non-villain conflicts;
- a population can cause infrastructure problems while acting from normal curiosity or communication.

Do not import:

- the spotlight's exact ranch plot;
- its variants;
- its mechanical builds;
- its homebrew Ability text;
- any assumption that evolution should be prevented for economic convenience.

Source:
- https://pokemontabletop.com/pokemon-spotlight-mareep-family/

### PTU grassland mechanics exist only when authored

Available AutoPTU Python evidence contains a semantic `grassland` environment label and specific authored effects that read that label, including Natural Fighter mappings and traps. This proves only those exact rule interactions.

It does not prove:

- generic grazing mechanics;
- hoof/trampling damage;
- pasture bonuses;
- herd movement rules;
- stampede mechanics;
- grass-height cover;
- forage restoration;
- grazing-based healing;
- grassland spawning bonuses.

The existence of a `grassland` tag must not be expanded into a narrative environment simulator by the Minecraft adapter.

## Rangeland and grassland ecology sources

### Grazing can create heterogeneity rather than a single degradation axis

National Park Service research on bison documents that herbivory can change vegetation height, cover, litter, forb/grass composition and productivity. Effects vary by ecosystem and grazing pattern. Dynamic grazing can increase habitat heterogeneity; the same process under different density or context may produce different outcomes.

Design lesson:

Do not use `grazing_pressure = bad`. Track where, when and by whom grazing occurs, plus the vegetation/soil response actually observed.

Sources:
- https://www.nps.gov/articles/bison-impacts-and-monitoring.htm
- https://www.nps.gov/articles/bison-bellows-3-24-16.htm
- https://www.nps.gov/articles/plant-community-monitoring-badl.htm

### Grazers can redistribute nutrients and create microhabitats

NPS describes large herbivores moving nutrients across landscapes through waste deposition, grazing and wallowing. Bison wallows can create depressions that collect water and support different plants.

Design lesson:

A persistent herd can create small landscape features and nutrient hotspots without requiring every movement to be simulated. Ouros should store coarse disturbance/use events and allow Flora/Soil/Freshwater to evaluate downstream state.

Sources:
- https://www.nps.gov/subjects/bison/bison-facts.htm
- https://home.nps.gov/articles/000/prairie-ecology-badl.htm

### Grazing and fire can interact over years

Tallgrass Prairie National Preserve describes a strong interaction between fire, regrowth and grazing. Newly burned grass-dominated patches can attract grazers, which then influence vegetation structure and nutrient cycling.

Design lesson:

Wildfire and grazing should communicate through world state. A burn scar can change forage distribution, which changes herd use, which can alter later vegetation. No direct tactical fire/grazing bonus is implied.

Source:
- https://www.nps.gov/tapr/learn/nature/fire-and-grazing-in-the-prairie.htm

### Concentrated use around water or infrastructure can produce local pressure

USDA research shows that livestock often congregate near waterers, feeding points or shade. These concentration areas can show vegetation loss, compaction, reduced infiltration and higher erosion/runoff risk. Other research shows the magnitude of grazing impacts depends on soil moisture, stocking pressure, season, vegetation and site characteristics.

Design lesson:

Do not apply a herd-wide condition to an entire grassland. Pressure hotspots should be separate spatial objects tied to actual congregation behavior and site vulnerability.

Sources:
- https://www.ars.usda.gov/research/publications/publication/?seqNo115=240625
- https://www.ars.usda.gov/research/publications/publication/?seqNo115=126586
- https://directives.nrcs.usda.gov/sites/default/files2/1712930328/33930.pdf

### Drought changes what sustainable grazing looks like

USDA Climate Hubs notes that drought management often involves maintaining ground cover, plant vigor and appropriate grazing distribution. The same stocking/use pattern can have different consequences under dry versus wet conditions.

Design lesson:

Aridity/Drought must feed the grassland layer. A range-use pattern that was sustainable in a normal year may become damaging under prolonged dryness, and recovery can require more than one season.

Source:
- https://www.climatehubs.usda.gov/hubs/topic/drought-and-rangelands-effects-and-management-responses

## Reusable Ouros structures

1. Herd-route memory: a persistent collective uses multiple grazing units and water points across seasons.
2. Patch mosaic: grazed, lightly used and resting patches develop different vegetation histories.
3. Congregation hotspot: a water point, shade structure or narrow gate receives much heavier pressure than the surrounding range.
4. Fire-following movement: a herd shifts toward recent regrowth after a burn, creating follow-up ecology questions.
5. Drought redistribution: usual herd routes fail because water/forage availability changed.
6. Managed-vs-wild overlap: a ranch herd and a wild collective use the same grassland differently.
7. Material-production season: fleece/milk/other authored resources affect schedules without creating automatic item yields.
8. Leadership correction: researchers misidentify a herd leader because visible prominence is not always command authority.
9. Range-rest project: a heavily used patch changes over multiple seasons after pressure is reduced.
10. Movement corridor conflict: fences, roads, tourism or construction alter a long-used herd route.
11. Grassland-to-shrub transition: long-term vegetation structure shifts and changes which species use the area.
12. Monitoring disagreement: two observers sample different patches and publish apparently conflicting grassland condition assessments.

## Copyright/provenance boundary

Only high-level structures, factual ecological principles and source metadata are retained. No protected dialogue, fan characters, source-specific plots or PTU spotlight prose should be copied into Ouros.

## Questions for future validation

- Which Ouros regions contain major grasslands, savannas, alpine meadows or managed pastures?
- Which Pokémon species have authored herd/grazing behavior in those regions?
- How should wild collectives and managed herds share identity without collapsing ownership and ecology?
- Which PTU/Caelo rules govern Naturewalk (Grassland), Mountable, Pack Mon, Run Away, shepherding, tracking and retreat?
- Does Ouros need numeric stocking/grazing pressure, or coarse use classes plus observations?
- How should Cobblemon receive herd presence projections without treating loaded entity count as population truth?
- How should a grassland snapshot enter AutoPTU without Minecraft inventing cover, Rough Terrain, trampling or stampede rules?

Caelo primary material was not reliably available for a dedicated grazing/rangeland rule during this run. No Caelo-specific grazing mechanic is claimed here.