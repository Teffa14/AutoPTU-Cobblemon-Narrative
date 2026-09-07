# Pass 319 research — reclaimed extraction landscapes and layered industrial ecology

Status: RESEARCH / PROVENANCE ONLY / NOT CANON

Date: 2026-09-06

## Why this scan

Repository inventory and code search found no existing research/proposal centered on quarry reclamation, abandoned mine hazards, highwalls, subsidence, spoil, or the ecological reuse of a former extraction landscape. Passes 315–318 already cover acoustic, artificial-light, olfactory, and geomagnetic observation. Pass 319 therefore opens a more physical exploration axis: a place whose industrial history remains readable in terrain, drainage, access routes, vegetation, and present-day land use.

The Ouros design question is: how can a location contain several legitimate historical layers at once — extraction, abandonment, reclamation, new habitat, renewed access — without reducing every anomaly to sabotage or every old hazard to a combat encounter?

## External source scan

### Abandoned mine land reclamation as persistent world-state transformation

Source: U.S. Office of Surface Mining Reclamation and Enforcement, Reclaiming Abandoned Mine Lands.
https://www.osmre.gov/programs/reclaiming-abandoned-mine-lands

Source: OSMRE Abandoned Mine Land Inventory System.
https://www.osmre.gov/programs/e-amlis

Reusable structure:
- Legacy extraction can leave hazards and environmental degradation long after operations stop.
- Reclamation is not a single binary event. Inventories are updated as problems are identified and reclaimed.
- A formerly hazardous site can later acquire a new purpose.

Ouros transformation:
- Treat the extraction site as durable world state with individually tracked features rather than a dungeon that disappears after completion.
- Separate `LEGACY_FEATURE_IDENTIFIED`, `RECLAIMED`, `MONITORING`, and `NEW_PROBLEM_IDENTIFIED` from player assumptions about whether the whole site is safe.
- Revisits can reveal that one bench was restored while another drainage path, slope, or sealed access has changed independently.

### Reclamation can create new habitat while removing old hazards

Source: OSMRE, Friendship Park Highwall Reclamation Project award.
https://www.osmre.gov/news/2023/OSMRE-presents-National-AML-Reclamation-Award-to-Ohio

Reusable structure:
- Dangerous highwalls and water-filled pits can be remediated while the same project creates wetlands, stream channels, trails, open space, and reforested habitat.
- Safety intervention and ecological benefit can coexist rather than being opposing goals.

Ouros transformation:
- A stakeholder who wants remediation need not be anti-Pokémon or anti-nature.
- A habitat advocate can legitimately value ecological niches that appeared after abandonment while still accepting that some legacy features are dangerous.
- Conflict can come from which feature should change, how quickly, and what evidence supports the intervention.

### Mine drainage produces ambiguous environmental evidence

Source: U.S. Geological Survey, Mine Drainage.
https://www.usgs.gov/mission-areas/water-resources/science/mine-drainage

Source: USGS, Effects of Abandoned Coal Mine Drainage in the New River Gorge.
https://www.usgs.gov/centers/virginia-and-west-virginia-water-science-center/science/effects-abandoned-coal-mine

Reusable structure:
- Water emerging from active or abandoned mines can range from relatively clean to contaminated depending on geology and legacy materials.
- Mine drainage can create visible water-quality changes and ecological impacts.
- Some cold-water seepage from old workings can also create wetland or stream habitat, so an old mine-water feature can have concurrent harmful and habitat-forming effects.

Ouros transformation:
- Do not use discoloration, a seep, or a wetland as automatic proof of poisoning.
- Keep water observation, laboratory interpretation, ecological use, and management decision separate.
- A remediation option can solve one problem while altering a habitat that developed after abandonment.

No real-world contaminant concentration or safety threshold is imported into PTU.

### Extraction landscapes can be repurposed for community use

Source: OSMRE Abandoned Mine Land Economic Revitalization Program.
https://www.osmre.gov/programs/reclaiming-abandoned-mine-lands/amler

Reusable structure:
- Reclamation can connect environmental repair with trails, utilities, education, public access, and economic reuse.

Ouros transformation:
- The same former quarry can matter to route custodians, nearby settlements, researchers, workers, Pokémon habitat stewards, and recreation users for different valid reasons.
- Reopening access is a faction decision with consequences, not merely the reward for defeating a boss.

### Official Pokémon species evidence: mine travel is species-specific

Source: official Pokémon Sword and Shield site, Rolycoly.
https://swordshield.pokemon.com/en-us/pokemon-galar-region/rolycoly/

Reusable franchise evidence:
- Rolycoly is explicitly associated with coal mines and caves.
- The official description says it can illuminate dark areas and traverse rough terrain smoothly.
- Its historical relationship with human households demonstrates a possible species-human material relationship in franchise fiction.

Ouros transformation:
- Rolycoly is a candidate for a former extraction landscape if regional ecology later supports it.
- Its rough-terrain and illumination flavor can motivate observations or local history.
- These descriptions do not establish PTU Overland values, terrain immunity, darkness rules, climb rules, mining labor, ecological residency, or automatic hazard traversal.

No species is assigned by this research note.

### PTU community encounter design: cave geometry can be tactically meaningful

Source: Brixmon, public `Pokemon Tabletop United- Crystal Cave Battle Arena` map description.
https://www.deviantart.com/brixmon/art/Pokemon-Tabletop-United-Crystal-Cave-Battle-Arena-677772021

Reusable structure:
- PTU community encounter design uses cave layouts where water, lava, entrances, elevation/viewing assumptions, and visible environmental features shape the arena.

Ouros transformation:
- An extraction site can use benches, haul roads, drainage cuts, retaining walls, pits, and service galleries as readable tactical geometry.
- The terrain should first function as a place. A battle may happen there, but the location should not exist only as a battle grid.

The map, tiles, champion encounter, and distinctive visual composition are not copied.

### Fan-game exploration: persistent mapping and reshaping a discovered dungeon

Source: Pokémon Shale, public itch.io project page.
https://kaimedina.itch.io/pokemon-shale

Reusable structure:
- Exploration reveals rooms/events that are added to a persistent map.
- Understanding a dungeon can eventually let the player reshape it as community space expands.

Ouros transformation:
- Surveying the old extraction site should produce durable knowledge of routes, hazards, and usable spaces.
- Later remediation can physically change the same mapped place instead of replacing it with a new quest instance.
- The player can return to compare old and new environmental states.

No rules, cards, Pokémon roster, map procedure, or distinctive dungeon content is imported.

### Current Cobblemon community structure reference

Source: `Cobblemon: Explore Legendary Dungeons`, public CurseForge page, updated 2026-07-20.
https://www.curseforge.com/minecraft/mc-mods/cobblemon-explore-legendary-dungeons

Reusable structure:
- Current Cobblemon community projects already treat large world-generated structures as exploration progression spaces with escalating internal challenge.

Ouros transformation:
- A large industrial ruin can be represented as a world structure with navigable subspaces rather than a menu-only adventure.
- Ouros should diverge by making the structure persistent, socially embedded, and causally altered by reclamation instead of using it only as a combat ladder to a legendary encounter.

No structure, encounter, legendary placement, asset, or code is imported.

## Reusable Ouros design lessons

### 1. A reclaimed place has several timelines at once

Useful evidence can belong to different phases:
- active extraction;
- shutdown/abandonment;
- emergency stabilization;
- formal reclamation;
- spontaneous ecological succession;
- new community use;
- recent disturbance.

A rusted rail proves old use, not current operation. Fresh sediment over an old drainage channel proves a newer event. Young vegetation on compacted spoil can reveal sequence without identifying a responsible actor.

### 2. `Reclaimed` must not mean globally safe

Track hazards and repairs by feature. A restored trail does not certify a sealed adit. A stable lower bench does not certify an upper highwall. A repaired drainage channel does not prove water chemistry elsewhere.

### 3. Restoration can create a second-order conflict

Once Pokémon use a wetland, ledge, warm seep, spoil grassland, or quiet gallery that arose after abandonment, changing the site again can have ecological consequences. This does not automatically make the original industrial damage beneficial or make restoration wrong.

### 4. Environmental evidence should be cross-channel

Useful evidence can include:
- survey monuments;
- historical maps;
- slope geometry;
- rockfall age classes;
- vegetation succession;
- drainage stains/sediment fans;
- tool or vehicle traces;
- sealed/failed access works;
- Pokémon tracks, nests, feeding signs, or observations only when species behavior is sourced;
- testimony from workers, residents, researchers, and route custodians.

No one channel is omniscient.

### 5. Faction conflict should survive a non-villain resolution

Potential interests:
- reclamation steward: reduce documented hazards;
- habitat researcher/steward: preserve or understand secondary habitat;
- logistics operator: restore a useful haul-road corridor;
- nearby community: wants safe access and economic use;
- former worker/legacy institution: has historical knowledge but incomplete current data;
- route authority: needs defensible open/close decisions.

Each can be partly right about a different feature.

## PTU / Caelo cross-check status

Repository inspection still exposes `sources/kairos`; no adopted `sources/caelo` directory or project-authoritative quarry/reclamation overlay was located in the current narrative tree.

PTU/Caelo mechanics therefore remain conservative:
- ordinary audited movement/geometry may support the reduced route exploration;
- rough terrain, climbing, jumping, unstable ledges, falling, rockfall, swimming through mine water, environmental damage, reactions, rescue/interception, delayed collapse, and species-specific traversal must use the relevant verified engine/PTU contracts before becoming mechanical;
- official Rolycoly material is franchise ecology/theme evidence only;
- any Move, Ability, Item, Trainer Feature, Capability, Skill check, immunity, or environmental modifier must be individually sourced and verified.

No DC, damage value, fall rule, collapse timer, terrain cost, water-quality effect, status, or species spawn is authored here.

## Canon boundary

This research changes no canon. Region, geology, extraction material, former operator, present owner, responsible institution, reclamation history, Pokémon population, hazard state, drainage chemistry, and final mystery resolution remain unset.
