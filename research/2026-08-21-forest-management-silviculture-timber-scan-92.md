# Pass 92 Research — Forest Management, Silviculture & Timber Provenance

Status: RESEARCH / PROVENANCE ONLY. Not canon. Not a PTU rules source.

Date: 2026-08-21

## Why this pass exists

The repository already contains persistent layers for forest canopy structure, flora, decomposition/deadwood, wildfire, soil, freshwater, roads, workplaces, material culture and conservation.

What it does not yet own is the management cycle of a working forest itself.

A managed forest can be simultaneously:

- wildlife habitat;
- a source of timber and non-wood resources;
- a workplace;
- a water catchment;
- a fire-management landscape;
- a travel and road network;
- a cultural or historical place;
- a restoration site;
- a conflict point between institutions, residents and Pokémon.

Without a dedicated layer, timber extraction would otherwise be reduced to either generic resource gathering or a one-off environmental conflict. This pass instead studies harvest planning, retention, regeneration, monitoring, provenance, roads and post-harvest consequences as long-lived world state.

## Source set inspected

### Official Pokémon Pokédex — Trevenant

Source:
- https://www.pokemon.com/us/pokedex/trevenant

Relevant official behavior:
Trevenant connects to trees through its roots, monitors its forest and drives away intruders, while treating forest-dwelling Pokémon kindly.

Reusable structure:
A Pokémon can have an authored relationship to a forest as a place and community rather than simply occupy one spawn table.

Design lesson:
If Trevenant or another species is present in a managed forest, its observed behavior can become evidence about local disturbance or territory. Presence alone does not prove that all forestry is harmful or that Trevenant has legal or ecological authority over the site.

Mechanical boundary:
Do not convert this lore into automatic root control, curse zones, forced movement, terrain ownership or anti-logging mechanics.

### Official Pokémon — Forging Forest Friendships!

Source:
- https://www.pokemon.com/us/animation/seasons/17/episode-37-forging-forest-friendships

Reusable structure:
A forest Pokémon can recruit human help because another actor has trapped or threatened Pokémon it cares about. The forest scene supports training, rescue, social interpretation and battle in one location.

Design lesson:
Forest conflict does not need to begin with combat. A Pokémon can signal a problem, players can interpret it, and only the actors actually responsible for the immediate confrontation need to enter battle.

Copyright boundary:
Do not reuse Ash, Clemont, Team Rocket, their dialogue, or the episode plot.

### Public PTU map discussion — working logger area

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/mrvkx8/original_maps_tell_me_what_you_think/

High-level observation:
A PTU GM describes a logger working overtime because of a large lumber order and asks how to make that working area feel spatially credible. Community suggestions include machinery, a smaller work footprint and hidden routes.

Reusable structure:
A logging site can be a real workplace with demand, equipment, routes and time pressure instead of an anonymous clear-cut battle map.

Design lesson:
The same forest can contain production zones, hidden ecological routes, water edges, machinery and untouched sectors. Encounter design should derive from this spatial state.

Copyright boundary:
No maps, characters or campaign-specific locations are copied.

### Public PTU campaign example — persistent consequences after a forest conflict

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/k2k94e

High-level observation:
A campaign report describes player decisions around a forest conflict producing large persistent consequences to nearby settlements and later priorities.

Reusable structure:
Forest decisions can propagate into refugees, settlement recovery, institutional response and future expeditions rather than reset after one battle.

Design lesson:
Major forest events should write back to Chronicle and linked systems. Winning or losing one encounter should not restore the prior map automatically.

Copyright boundary:
No campaign characters, named corporations, unique artifacts or plot sequence are copied.

### FAO — Wood harvesting module

Source:
- https://www.fao.org/sustainable-forest-management-toolbox/modules/wood-harvesting/1/en?tabInx=0

Key findings:
Wood harvesting includes planning, roads, felling, extraction, transport and post-harvest assessment. Harvest operations can affect residual trees, soils, roads, drainage and future forest structure. Reduced-impact approaches use pre-harvest inventories, planned roads/skid trails, directional felling, controlled extraction and assessment after work.

Reusable structure:
A harvest should be a project with phases and recorded decisions rather than one boolean `logged=true`.

Potential phases for Ouros:

- inventory/survey;
- designation;
- access planning;
- harvest window;
- extraction;
- road/landing closure or reuse;
- post-harvest assessment;
- regeneration monitoring.

### FAO — Forest management monitoring

Source:
- https://www.fao.org/sustainable-forest-management-toolbox/modules/forest-management-monitoring/2/en?tabInx=0

Key finding:
Monitoring should compare actual operations against plans and can inspect residual stand condition, regeneration, roads, landings, skid trails, erosion, soil disturbance, wildlife effects and conservation prescriptions.

Reusable structure:
Ouros should store planned state separately from observed state.

Design lesson:
A harvest can be legally or institutionally complete while regeneration, erosion or habitat monitoring remains active for years.

### FAO — Silviculture in natural forests

Source:
- https://www.fao.org/sustainable-forest-management-toolbox/modules/silviculture-in-natural-forests/en

Key findings:
Silvicultural treatment may retain seed trees, protect advance regeneration, manage light and reduce unnecessary damage to non-target vegetation. Different objectives can require different treatments.

Reusable structure:
Forest management should support heterogeneous prescriptions rather than one universal `cut percentage`.

Examples of coarse Ouros treatment intents:

- regeneration support;
- thinning;
- habitat retention;
- selective harvest;
- sanitation/safety removal;
- road closure and rehabilitation;
- restoration planting;
- no intervention / monitoring only.

These are management intents, not mechanical buffs.

### USDA Forest Service — Reforestation

Source:
- https://www.fs.usda.gov/forestmanagement/vegetation-management/reforestation/index.shtml

Key finding:
Reforestation can rely on natural regeneration or planting after wildfire, wind disturbance, pests/disease or planned timber harvest. Forest recovery can serve multiple goals including habitat, water, soil stabilization, recreation and wood products.

Reusable structure:
Regeneration should be its own monitored trajectory. Planting trees does not instantly restore the previous forest.

### USDA Climate Hubs — retention of living and dead biological legacies

Source:
- https://www.climatehubs.usda.gov/approach/increase-structural-complexity-through-retention-biological-legacies-living-and-dead-wood

Key finding:
Retained large trees, survivors, snags and downed wood can preserve structural complexity and microhabitats after management or disturbance.

Reusable structure:
A harvest prescription can intentionally leave specific persistent trees, snags or logs because they matter for habitat, history or regeneration.

This connects directly to the existing persistent-tree and decomposition layers.

### USDA Forest Service research — riparian buffers and timber harvest

Source:
- https://research.fs.usda.gov/treesearch/37304

Key finding:
In one catchment study, different riparian buffer widths produced different stream-water responses after timber harvest.

Reusable structure:
Forest management can hand off effects to Freshwater based on spatial relationships such as stream buffers, roads and drainage. The harvest layer should never directly invent water-quality outcomes.

### USDA Forest Service / FAO — roads and sediment

Sources:
- https://www.fs.usda.gov/eng/pubs/pdf/w-r/97771816.pdf
- https://www.fao.org/4/i2596e/i2596e00.pdf

High-level finding:
Forest roads and extraction routes can be important sources of soil disturbance and sediment, and careful planning is part of reduced-impact harvesting.

Reusable structure:
The largest downstream consequence of a forest operation may come from access infrastructure rather than the removed trees themselves.

That creates strong cross-layer stories with Road Ecology, Soil and Freshwater.

## High-level reusable design patterns

### 1. Plan versus operation versus outcome

Track separately:

- what managers intended;
- what was marked/designated;
- what workers actually did;
- what materials were removed;
- what remained;
- what later monitoring observed.

A plan can be sound and execution poor.

A plan can be followed perfectly and still produce an unexpected result.

### 2. Timber is a provenance chain

A relevant timber batch can retain:

forest unit → harvest project → tree/stand source class → landing → transport → mill/workshop → finished object.

This can connect directly to Material Culture without simulating every log block.

### 3. Forest roads are persistent decisions

Temporary roads, skid trails and landings can later become:

- closed and restored;
- maintained as public access;
- reused by workers;
- wildlife routes;
- erosion hotspots;
- emergency access;
- forgotten historical features.

Their afterlife is often more narratively useful than the day they were built.

### 4. Regeneration has multiple pathways

Possible coarse states:

- natural regeneration adequate;
- natural regeneration patchy;
- planting underway;
- planting failed/uncertain;
- competing vegetation dominant;
- mixed recovery;
- monitoring insufficient.

Do not infer a single desired climax state for every forest.

### 5. Retention creates future story assets

A retained veteran tree, snag or habitat patch can later become:

- a landmark;
- a roost;
- a research station reference point;
- a memorial;
- a Trevenant-related observation site;
- a seed source;
- deadwood after windthrow;
- the center of a later access dispute.

### 6. Demand belongs outside the forest layer

A sudden lumber order should originate from Finance, Public Works, Housing, Disaster Recovery, Industry or another system.

Forest Management consumes that demand and decides what project is proposed or authorized. It does not create demand simply to generate logging content.

### 7. One harvest can produce different spatial outcomes

A project may contain:

- untouched retention patch;
- thinned stand;
- extraction corridor;
- riparian buffer;
- landing;
- worker camp;
- regeneration plot;
- road closure area.

This is more useful for Minecraft than a binary harvested/unharvested map.

### 8. Pokémon observations remain evidence

Examples:

- Trevenant appears repeatedly near marked trees;
- nesting Pokémon abandon one extraction corridor but remain elsewhere;
- a burrowing species uses a closed skid trail;
- a released former partner is observed near a regeneration plot.

None of these observations establish motivation, ownership or a battle mechanic by themselves.

## PTU / AutoPTU guardrails

No new PTU rule is established here.

Do not infer:

- tree = blocker with universal HP;
- felled log = Rough Terrain;
- stump = cover;
- active logging = hazard zone;
- Trevenant = forest-wide controller;
- Grass-type = forestry worker;
- Fire-type = logging tool;
- Naturewalk (Forest) = immunity to falling timber;
- Groundshaper = road-building permission;
- Cut-like Move = legal logging operation;
- timber harvest = ecological damage by definition;
- forest restoration = automatic encounter-rate improvement.

Any battle use of falling trees, moving logs, machinery, smoke, unstable slopes, active fire, forced displacement or protective corridors requires explicit engine capability support and verified PTU/Caelo mechanics.

## Suggested handoffs to existing Ouros layers

Forest Management → Forest Canopy
- canopy openings;
- retained trees;
- tree identity;
- vertical structure changes.

Forest Management → Flora
- regeneration observations;
- planting cohorts;
- seed-source provenance.

Forest Management → Decomposition
- retained slash/deadwood;
- snags;
- down logs;
- removal versus retention history.

Forest Management → Soil
- compacted extraction routes;
- disturbed landings;
- erosion observations.

Forest Management → Freshwater
- riparian buffers;
- road drainage;
- sediment observations;
- catchment-linked monitoring.

Forest Management → Wildfire
- fuels treatment proposals;
- post-fire salvage proposals;
- fire-access roads.

Forest Management → Material Culture
- timber batches;
- maker provenance;
- repair/reuse history.

Forest Management → Workplaces
- forestry crews;
- mills;
- supervisors;
- training/coverage.

Forest Management → Road Ecology
- forest roads;
- closure/reuse;
- crossing effects.

## Sources deliberately not treated as authority

Community campaign logs, Reddit posts and fan material are inspiration for structure only.

Real forestry guidance is used to make fictional processes causally coherent. It is not imported as Ouros law, certification, property rights or regulatory policy.

No real community, Indigenous forestry practice, labor regime or legal system should be reskinned into Ouros without dedicated authored review.

## Research outcome

The useful missing object is not `logging_site` alone.

Ouros needs a versioned forest-management project that can connect demand, authorization, treatment intent, mapped work areas, retained structures, timber provenance, worker operations, roads, post-harvest assessment and multi-year regeneration.

That object can produce quests and encounters while preserving the stronger rule already established across the repository: world state must explain why the encounter exists, and AutoPTU must remain the authority for any tactical effect.