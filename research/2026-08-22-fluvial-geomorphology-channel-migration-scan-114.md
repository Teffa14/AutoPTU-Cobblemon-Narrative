# Fluvial Geomorphology, Channel Migration & River-Landform Scan — Pass 114

Status: RESEARCH / PROVENANCE ONLY. Not canon. Not a PTU rules source. No mechanical effect is established here.

Pass: 114

## Why this scan

The narrative repository already has a broad Freshwater layer for flow regime, catchment connectivity, flood pulses, reservoirs, wetlands and water-control assets. It also has Soil/Erosion, Road Ecology, Architecture, Land Tenure, Conservation and Cartography layers.

The remaining gap is physical river-form history: where the active channel itself was at different dates, how banks migrate, how point bars and islands form, how meanders cut off, how abandoned channels become oxbows/backwaters/wetlands, and how those changes invalidate roads, boundaries, maps and access assumptions without changing the identity of the river.

This pass therefore focuses on geomorphic change, not discharge simulation.

## Source set and reusable structures

### 1. USGS — Oxbow Lakes

Source:
https://eros.usgs.gov/earthshots/oxbow-lakes

Reusable structure:

A meandering river can shorten its course by cutting across a bend. The abandoned bend can persist as an oxbow lake, later accumulate sediment and organic material, and eventually change again into wetland or dry land.

Ouros adaptation:

- keep the river identity while channel geometry changes;
- keep the abandoned bend as a persistent landform with its own history;
- allow an old route, property description, habitat record or map to remain historically correct after the main channel moved;
- treat oxbow evolution as a long-running state transition rather than a one-time set-piece.

Do not copy real locations or measurements.

### 2. USGS — Geomorphic and vegetation processes of the Willamette River floodplain

Source:
https://www.usgs.gov/publications/geomorphic-and-vegetation-processes-willamette-river-floodplain-oregon-current

Reusable structure:

River form, sediment transport, flood regime and vegetation interact over time. Reduced channel migration or avulsion can change the diversity of gravel bars, islands, side channels and functional floodplain surfaces.

Ouros adaptation:

A river should not be represented only as water level. A stable-looking reach may be losing bars, side channels or floodplain turnover. Conversely, a mobile reach can create new habitat and new route problems without being “damaged.”

### 3. USGS — McKenzie / Middle Fork Willamette geomorphic mapping

Source:
https://pubs.usgs.gov/of/2016/1186/ofr20161186.pdf

Reusable structure:

A large flood can initiate a sequence of erosion and overflow-channel changes, while later smaller floods continue migration, bar growth and vegetation transition. A channel may eventually abandon an older bend and occupy a previously secondary path.

Ouros adaptation:

Use multi-year cascades:

large flood → overflow channel scoured → smaller events enlarge it → vegetation changes → route becomes viable → main channel eventually shifts.

The important lesson is delayed consequence. The event that created the eventual new channel may happen years before the avulsion becomes obvious.

### 4. USGS — Santa Cruz River channel change

Source:
https://www.usgs.gov/publications/channel-change-santa-cruz-river-pima-county-arizona-1936-86-0

Reusable structure:

Different reaches can change by different mechanisms: lateral migration, avulsion/cutoff, channel widening or incision. The same flood magnitude does not produce the same result everywhere because topography, geology, previous channel state and artificial constraints differ.

Ouros adaptation:

Never use a single `river_changed=true` flag. Change must be scoped to reaches and mechanisms.

### 5. USGS — Powder River long-term meander migration

Source:
https://www.usgs.gov/publications/a-184-year-record-river-meander-migration-tree-rings-aerial-imagery-and-cross-sections

Reusable structure:

Long historical records can reconstruct channel migration using multiple evidence types such as repeat surveys, aerial imagery and vegetation age.

Ouros adaptation:

Cartography, Photography, Archives, Flora and Science can independently contribute evidence about where the river used to be. A later synthesis may resolve apparently contradictory historical maps without declaring any source fraudulent.

### 6. USGS — Sediment exchange between channel and floodplain

Source:
https://www.usgs.gov/publications/exchanges-sediment-between-flood-plain-and-channel-amazon-river-brazil

Reusable structure:

Bank erosion, bar deposition, overbank deposition and floodplain channels exchange large amounts of sediment. Material eroded in one place can become a bar, island or floodplain deposit elsewhere.

Ouros adaptation:

Sediment provenance can connect upstream erosion to downstream landform change without requiring exact volumetric simulation. Use coarse batches or event-linked sediment pulses where narratively important.

### 7. USGS — Fluvial islands

Source:
https://www.usgs.gov/publications/processes-fluvial-island-formation-examples-plum-creek-colorado-and-snake-river-idaho

Reusable structure:

River islands can form through avulsion, deposition, channel migration and erosion around previously continuous land. They can later move, merge or disappear.

Ouros adaptation:

A river island can be a persistent location even when its shape or connection to the bank changes. It can become habitat, farmland, a survey station, a ferry stop, a contested boundary or a ruin site.

### 8. NOAA-hosted channel migration-zone guidance

Source surfaced through NOAA repository search:
https://repository.library.noaa.gov/view/noaa/2599/noaa_2599_DS1.pdf

Reusable structure:

A river can occupy a wider migration corridor over time than the active channel visible today. Fixing the channel in place can shift erosion, sedimentation and flood consequences elsewhere.

Ouros adaptation:

Separate `active_channel` from `channel_migration_zone`. Structures can be safe today yet exposed to a known long-term migration corridor.

Do not import real planning regulations.

## Pokémon sources

### 9. Pokémon — “Absol-ute Disaster”

Official source:
https://www.pokemon.com/us/animation/seasons/8/episode-15-absol-ute-disaster

Reusable structure:

Repeated bridge failures and abnormal river behavior are initially blamed on a visible Pokémon associated with disaster. Investigation reveals that the Pokémon is warning about the underlying water problem rather than causing it.

Ouros adaptation:

This is a strong anti-scapegoat template for fluvial stories:

observed channel/bridge problem → visible Pokémon blamed → field evidence contradicts blame → upstream/geomorphic cause investigated → Pokémon behavior reinterpreted.

Do not reuse Absol as the default warning species, the same village structure or the episode’s exact resolution.

### 10. Pokémon — “Type Casting!”

Official source:
https://www.pokemon.com/us/animation/seasons/4/episode-5-type-casting

Reusable structure:

A storm-damaged bridge changes travel assumptions. A map can correctly encode a crossing that no longer exists, and local transport alternatives become relevant until reconstruction finishes.

Ouros adaptation:

A river-form or flood event can invalidate route state without making the map historically wrong. Temporary ferries, detours and later rebuilding can become long-lived transport history.

### 11. Pokémon — “A Mudkip Mission!”

Secondary episode source used only for structural reference:
https://dogasu.bulbagarden.net/comparisons/houen/ep025.html

Reusable structure:

A managed pond/nursery depends on a dam and downstream water movement. Removing the structure changes current immediately and affects Pokémon occupying the system.

Ouros adaptation:

Infrastructure, channel form and habitat should remain separate authorities. Changing a dam or bank can change local hydrology, but the ecological result still requires observation rather than automatic population mutation.

## PTU / community sources

### 12. PTU official blog — “The Road to Tomorrow”

Source:
https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

Reusable structure:

PTU campaigns can be built around rebuilding, settlement, infrastructure, exploration and consequences that persist for generations instead of only League progression. The source explicitly emphasizes travel/exploration and player actions that shape future society.

Ouros adaptation:

River migration is especially useful for this style because decisions about bridges, levees, ferry routes, settlements, floodplain use and restoration can remain visible years later.

### 13. Public PTU campaign log — river as spatial clue

Source:
https://www.reddit.com/r/PokemonTabletop/comments/oeddi8

Reusable structure:

The campaign uses a river as spatial orientation and a hidden-route clue leading to a hostile base. The useful pattern is not the base or faction; it is that natural geography can structure discovery and navigation.

Ouros adaptation:

A former channel, backwater or side channel can expose or conceal access to a location depending on current geometry and season. Do not reuse the log’s faction, characters or encounter details.

## Design lessons extracted

### River identity should outlive river geometry

The same river should retain one persistent identity while its centerline, banks, bars, islands and secondary channels receive revisions.

### Flow and form are different

Freshwater owns hydrological state: flow, level, connectivity, flood pulses and control assets.

Fluvial Geomorphology should own persistent landform state: channel position, bank migration, cutoffs, bars, islands, abandoned channels and floodplain surfaces.

A high flow can trigger geomorphic change, but the flow event and resulting physical revision remain separate records.

### Maps can disagree without one being wrong

Two maps from different decades can both be correct. Historical routefinding should use the map edition and river revision that existed at the time.

### Boundaries tied to rivers need historical context

Land Tenure must not assume that a boundary described as “along the river” automatically moves when the active channel migrates. Whether it moves is a canon/legal question, not a geomorphic inference.

### New land is not automatically unowned or public

A newly deposited bar or island does not automatically belong to the first actor who reaches it.

### Erosion is not a tactical attack

Minecraft bank collapse, exposed sediment, a point bar or a fresh cutoff do not create PTU damage, Rough Terrain, forced movement, falling, Tripped or Accuracy penalties unless an authoritative rule and battle projection define them.

### A river can produce slow mysteries

Good long arcs can begin with mundane evidence:

- an old fence line ending in water;
- a map showing a road through an oxbow;
- a bridge pier standing on dry land;
- trees of different age on opposite bars;
- an island that appears in photographs only after a flood;
- a side channel that becomes the main channel years later.

## Proposed handoffs to existing Ouros layers

Freshwater → supplies hydrological events and connectivity state.

Soil/Erosion → receives bank/soil-condition consequences where appropriate.

Flora → records vegetation establishment on bars, abandoned channels and floodplain surfaces.

Conservation → evaluates habitat implications.

Road Ecology / Travel → revalidates crossings and route viability.

Architecture / Infrastructure → inspects exposed or abandoned structures.

Cartography → versions maps and route traces.

Land Tenure → handles claims/boundaries without geomorphic shortcuts.

Archaeology / Public Memory → records former settlements, roads, structures or community memory revealed by channel change.

Minecraft → projects the current physical revision only after server validation.

AutoPTU → receives a frozen battle snapshot, never a live river simulator by implication.

## PTU/Caelo validation boundary

No PTU/Caelo rule is derived from the hydrology/geomorphology sources above.

Potentially relevant PTU/Caelo families that still require primary-project validation before mechanical use include:

- Swim;
- Naturewalk;
- Groundshaper;
- Water/ground terrain interactions;
- falling;
- forced movement;
- currents;
- environmental hazards;
- bridge/structure damage;
- movement through shallow/deep water.

The full Caelo primary corpus and Super PTU Online Helper were not available as reliable invocable sources during this run, so no new mechanical rule is asserted.

## Provenance / copyright guardrail

All reuse in this pass is structural and high-level. Do not copy episode dialogue, campaign prose, distinctive NPCs, factions, place names, plots or real-world management rules into canon. Preserve source attribution in research; transform only the reusable design pattern into original Ouros material.