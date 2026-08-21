# Coastal Geomorphology, Shorelines & Dunes Research — Pass 80

Status: RESEARCH ONLY. Not Ouros canon. External sources are evidence/inspiration, not rules authority.

Date: 2026-08-21

## Why this pass exists

The repository already models maritime travel, harbors, submerged places, estuaries, salinity, tidal wetlands, freshwater systems, soil erosion, storms, tourism, public works and conservation. It did not yet have a persistent object model for the shape of the open coast itself: beaches, dunes, barrier segments, cliffs, overwash, breaches, shoreline retreat/advance, post-storm profile recovery and sediment-management history.

This pass therefore treats coastal morphology as a new connection layer rather than duplicating Maritime, Estuaries, Meteorology, Soil, Geology or Crisis.

The core design lesson is that coastlines are versioned world state. A storm may move a shoreline tens of meters while the location remains the same named place. A dune can disappear and later rebuild. A barrier can migrate landward. A cliff path can become unsafe even though the road, settlement and sea lane still exist. Minecraft should render the current revision, while the Chronicle preserves how earlier versions differed.

## Repository audit

Relevant internal boundaries inspected before research:

- `design/maritime-coasts-depths-layer.md` owns maritime regions, sea lanes, harbors, vessels, submerged locations and marine condition/access context. It intentionally does not define shoreline morphology.
- `design/estuaries-tidal-wetlands-salinity-layer.md` owns estuary reaches, salinity, tidal-wetland hydroperiod, marsh migration and estuary-mouth state.
- Soil owns land-surface condition/erosion; Geology owns substrate; Meteorology owns storms and weather; Crisis owns emergency response; Architecture/Public Works own structures and projects; Conservation owns stewardship decisions.
- `design/engine-readiness-snapshot-pass-79.md` keeps environment-heavy tactical concepts behind explicit capability gates.

No existing research/design/proposal title in the inspected trees covered beaches, dunes, open-coast shoreline revisions, overwash or barrier-island migration as its own system.

## Public-source findings

### Species-specific sand behavior must stay species-specific

The official Sandygast and Palossand Pokédex material provides useful beach identity without justifying generic coastal powers. Sandygast is explicitly a sand-heap Pokémon with behavior tied to manipulating nearby sand; Palossand is a larger sand-bodied form. These entries can inspire encounters where the physical beach matters to those species, but they do not establish a rule that either species controls shoreline sediment budgets, creates tactical dunes, owns beach sand or causes erosion simply by being present.

Sources:
- https://www.pokemon.com/us/pokedex/sandygast
- https://www.pokemon.com/us/pokedex/palossand

Reusable structure:
- a species can interact strongly with one coastal substrate;
- observation of that interaction can become research or a route-access problem;
- the ecological/geophysical consequence must still be measured rather than assumed.

### PTU campaign design supports island/coastal exploration without requiring combat as the only resolution

Pokémon Tabletop's public campaign retrospectives and GM guidance repeatedly use wilderness travel, island geography and environmental complications as campaign structure. `Tales of Visiwa` uses an island region and dangerous wilderness as a meaningful layer of play. PTU's first-session guidance also supports encounters driven by territory, behavior and environmental opportunity rather than fighting until every opponent is knocked out.

Sources:
- https://pokemontabletop.com/tales-of-visiwa-a-retrospective/
- https://pokemontabletop.com/gm-advice-your-first-ptu-session/
- https://pokemontabletop.com/downloads-and-resources/

Reuse limit:
- PTU public articles support campaign/encounter structure;
- exact beach, sand, wave, erosion, cliff or storm mechanics still require the project PTU/Caelo corpus and implementation evidence.

### A useful fangame anti-pattern: map re-entry must not resurrect old environmental state

Public discussion around `Pokémon Glacial Chronicles` records a state-persistence issue where whirlpools removed by story progression could reappear after re-entering the area. The specific game state is not copied. The reusable lesson is architectural: a persistent Ouros coast cannot reconstruct itself from a static map template whenever a chunk or map reloads.

If a storm removed a dune gap, a boardwalk was rebuilt inland or a breach changed an access route, re-entering the area must project the current authoritative revision rather than the original map asset.

Source:
- https://eeveeexpo.com/glacial-chronicles/

A smaller Eevee Expo beach-visual resource also demonstrates the opposite boundary: shallow-water bubbles and beach presentation can improve atmosphere without defining movement, tide or PTU effects.

Source:
- https://eeveeexpo.com/resources/1354/

### Shorelines can move quickly during storms and slowly over years

USGS coastal-hazard work documents that barrier islands and beaches change through sediment transport, erosion, overwash, breaches and storms. Severe events can remove substantial shoreline and dune volume within hours or days; longer-term shoreline change reflects repeated events and sediment-budget processes.

Useful Ouros translation:
- storm event and shoreline revision are separate records;
- a single storm can create multiple spatial outcomes along one coast;
- long-term retreat/advance should preserve measurement history instead of overwriting an old map;
- a barrier island or beach can remain the same named place while its geometry changes.

Sources:
- https://pubs.usgs.gov/of/2007/1152/
- https://www.usgs.gov/programs/cmhrp/science/national-assessment-hurricane-induced-coastal-erosion-hazards
- https://www.usgs.gov/programs/cmhrp/science/national-assessment-shoreline-change

### Dunes are both physical buffers and habitat, and recovery has its own timescale

NOAA coastal guidance describes dunes as sand reservoirs that can buffer waves, erosion and flooding while also providing habitat. Storms can sharply reduce dunes, after which beach recovery and wind-blown sand may begin quickly while full dune rebuilding can take much longer.

This supports a multi-stage recovery model:

storm impact -> beach/profile response -> early sand accumulation -> vegetation establishment -> dune rebuilding -> later management review

The exact stages and timing in Ouros should remain authored/world-state abstractions, not real-world simulation equations.

Sources:
- https://coast.noaa.gov/data/digitalcoast/pdf/adaptation-strategies.pdf
- https://dnrec.delaware.gov/watershed-stewardship/beaches/dunes/
- https://coast.noaa.gov/states/stories/barrier-island-monitoring.html

### Beach nourishment and shore protection have trade-offs

NOAA adaptation material treats beach nourishment as adding compatible sediment to widen/rebuild a beach. It can support coastal protection and recreation but requires repeat maintenance and may have ecological impacts. Structural defenses can protect a particular asset while changing how waves and sediment interact nearby.

Ouros should therefore avoid a universal `coastal_protection = good` variable. Projects should retain:
- project objective;
- source/placement provenance for material;
- monitoring state;
- neighboring-segment effects;
- habitat/access consequences;
- maintenance history;
- unresolved disputes where evidence is incomplete.

The layer must not import modern legal coastal-management frameworks unless explicitly authored for an Ouros region.

## Reusable narrative structures

### Versioned coastline

A familiar route can change while staying recognizable. Old photographs, survey stakes, maps and memories become usable evidence. This creates return-value without needing a new dungeon every time.

### Storm consequence without instant crisis reset

The emergency can end while the shoreline remains changed for months or years. Recovery content can involve route redesign, habitat shifts, exposed ruins, tourism pressure, rebuilding and scientific monitoring.

### Conflicting maps can both be correct

A shoreline survey from five years ago and a current survey may differ without either being fraudulent. This naturally connects Cartography, Public Memory and Science.

### Newly exposed does not mean newly created

A storm can reveal old foundations, fossils, wreckage or archaeological material. Exposure changes discoverability, not provenance or ownership.

### Sediment moves across administrative boundaries

A project in one settlement may influence a neighboring beach. This supports civic conflicts without requiring one side to be malicious.

### Ecological use changes with physical shape

A new dune, washover fan, exposed flat or retreating cliff can alter where Pokémon shelter, nest, forage or travel. The ecological response must come from observed/authored state, never from a generic rare-spawn multiplier.

## Proposed systems boundary for Pass 80

Coastal geomorphology should own:
- open-coast segment identity;
- shoreline-position revisions;
- beach-profile revisions;
- dune-system and dune-condition revisions;
- barrier/overwash/breach history;
- cliff-edge/retreat history;
- coarse sediment-budget revisions;
- nourishment/restoration project provenance;
- coastal-access revisions caused by physical change.

It should consume or reference:
- storms/waves from Meteorology/Maritime;
- substrate from Geology;
- erosion/soil condition from Soil where relevant;
- emergency actions from Crisis;
- habitat/stewardship from Conservation;
- buildings/roads/defenses from Architecture and Public Works;
- visitors from Tourism;
- maps from Cartography.

It should not own sea-lane service, tidal-wetland salinity, building construction rules, legal property boundaries or battle mechanics.

## PTU/Caelo mechanical boundary

The project Python oracle contains narrow semantic terrain labels such as `ocean`, `wetlands`, `desert`, `sand` and `dune` in specific rule paths, plus exact Feature/Move logic that consumes those labels. That does not establish a generic beach, dune, wave, overwash, erosion, cliff or coastal-hazard subsystem.

A beach in narrative state must not automatically create:
- Rough/Slow Terrain;
- Sandstorm;
- Accuracy penalties;
- movement bonuses/penalties;
- knockback from waves;
- falling/cliff damage;
- drowning;
- Sandygast/Palossand mechanical effects;
- Water Compaction triggers;
- any rare-spawn modifier.

The primary Caelo material was not reliably retrievable during this run. No Caelo-specific beach, tide, dune, erosion or coastal-hazard rule is asserted here.

## Copyright and attribution boundary

No dialogue, prose, characters, plots, maps, puzzles or distinctive story sequences are imported from public Pokémon campaigns, fangames or official media. The research retains source links and extracts only broad design structures, factual species/environment references and implementation lessons.

## Research gaps for later passes

Future validation should inspect exact PTU/Caelo text for terrain categories, Groundshaper, Naturewalk, movement near cliffs/water, falling, forced movement, environmental damage and any sand/water interactions before a coastal encounter is promoted to mechanical canon.

Minecraft/Cobblemon integration also needs a separate authority contract for projecting a versioned coastline into chunks without treating loaded blocks as the canonical sediment model.