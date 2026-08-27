# Research Scan 87 — Forestry, Managed Woodland, Harvest & Restoration

Status: RESEARCH ONLY. Not Ouros canon.

Date: 2026-08-28

## Internal repository review

Before topic selection, the full recursive tree of `Teffa14/AutoPTU-Cobblemon-Narrative` at head `7e15eb9a03a87aebed94cd19926d000c11d7a8e8` was inspected. GitHub returned `truncated=false`.

Relevant adjacent layers opened or checked before writing:

- `design/conservation-protected-areas-stewardship-layer.md`;
- `design/material-culture-economy-crafting-layer.md`;
- `design/food-agriculture-hospitality-layer.md`;
- `design/workplaces-professions-staffing-layer.md`;
- `design/worksite-safety-near-miss-incident-learning-extension.md`;
- `design/pokemon-work-role-participation-extension.md`;
- `design/wild-collective-agency-layer.md`;
- `design/interspecies-ecological-relations-layer.md`;
- `design/weather-forecast-preparedness-operational-extension.md`;
- `design/crisis-rescue-recovery-layer.md`;
- `design/travel-transport-expedition-layer.md`;
- `design/waste-sanitation-recycling-pollution-layer.md`;
- `design/geology-excavation-resource-frontier-layer.md`;
- `design/cobblemon-runtime-authority-boundary.md`;
- `design/engine-readiness-snapshot-pass-86.md`.

The repository already has a dedicated geology/excavation/resource-frontier layer and Pass 33 research/proposals. Mining, quarrying and fossil extraction were therefore rejected as the Pass 87 topic to avoid duplication.

No forestry/managed-woodland layer, research pass or proposal set exists in the current tree. The gap is the persistent operational lifecycle of a woodland that can simultaneously be habitat, route, workplace, material source, craft landscape, restoration site and public place.

## Source set

### Pokémon Gold/Silver/Crystal and HeartGold/SoulSilver — Ilex Forest

Public reference:
- Bulbapedia, Ilex Forest: https://bulbapedia.bulbagarden.net/wiki/Ilex_Forest

High-level structure:

Ilex Forest is more than an encounter map. It sits between settlements/routes, contains a local charcoal-making tradition, supports human work and travel, and remains a Pokémon habitat. The Farfetch'd retrieval sequence also connects a worker, an individual Pokémon, a forest path and a craft livelihood without requiring the forest to become a generic resource node.

Reusable lessons:

- one woodland can support habitat, transit, craft identity and managed material use at the same time;
- a craft product can carry source-place identity without granting a mechanical bonus;
- work in the forest can depend on specific people, routes and individual Pokémon rather than an abstract “forest industry” meter;
- a familiar forest can be revisited for different purposes instead of being consumed after one quest.

Do not copy Ilex Forest, Kurt/Azalea institutions, the Farfetch'd puzzle, shrine mythology or named characters into Ouros.

### Official Pokémon animation — “A Sappy Ending”

Public official reference:
- Pokémon.com episode page, “A Sappy Ending”: https://www.pokemon.com/us/animation/seasons/8/episode-33-a-sappy-ending

The episode's useful high-level structure is causal rather than plot-specific. A group of wild Pokémon appears to be causing destructive pressure in one area, but investigation reveals that human extraction elsewhere disrupted the ecological balance and displaced the problem.

Reusable lessons:

- visible wildlife conflict can be downstream of resource use somewhere else;
- apparent “pest” behavior should not establish blame before provenance and activity history are checked;
- sap, timber, bark, deadwood or other forest products can be ecologically connected to more than the harvest patch itself;
- the consequence of extraction can emerge later and away from the original worksite.

Ouros should transform this into evidence chains such as `intervention -> habitat/resource change -> altered movement/behavior -> downstream coexistence incident`, never into a copy of Team Rocket, Pinsir or the episode plot.

### Pokémon Ranger: Shadows of Almia — Vien Forest fire and follow-up quests

Public references:
- Bulbapedia, Pokémon Ranger: Shadows of Almia walkthrough, Part 3: https://bulbapedia.bulbagarden.net/wiki/Appendix:Pok%C3%A9mon_Ranger:_Shadows_of_Almia_walkthrough/Part_3
- Bulbapedia, Vien Forest: https://bulbapedia.bulbagarden.net/wiki/Vien_Forest

Vien Forest is useful because the story does not end when the active fire is over. Later local requests involve missing/changed Pokémon presence and clearing fallen trees that block travel.

Reusable lessons:

- fire suppression, ecological recovery, route clearance and ordinary access are separate stages;
- post-disturbance timber can become a route problem, material opportunity, habitat feature or safety concern depending on context;
- a species not returning after a disturbance is an observation requiring follow-up, not proof of death, migration or permanent population loss;
- community recovery can create small linked tasks long after the crisis itself is closed.

Do not import Ranger Field Moves, browser/capture rules, exact requests, characters or supernatural restoration shortcuts.

### Pokémon Rejuvenation — Forest Restoration

Public community reference:
- Pokémon Rejuvenation Wiki, Forest Restoration: https://rejuvenation.wiki.gg/wiki/Forest_Restoration

This fan-game uses a staged restoration project that requires resources, workers and multiple steps before visible change appears.

Reusable structure:

- restoration can be a long project with prerequisites rather than an instant state flip;
- funding, staffing, materials and ecological work can be separate dependencies;
- later visits can show physical changes generated by earlier choices;
- completion can create a different functioning landscape rather than recreating an untouched past.

Do not copy exact money values, named characters, species requirements, karma, rewards or map changes. Ouros should route money to Finance, materials to Procurement/Material Culture, labor to Workplaces/Pokémon Work and ecological decisions to Conservation.

### Public PTU actual-play/campaign log — forest microecology

Public community reference:
- Reddit /r/PokemonTabletop campaign-log material surfaced during Pass 87 research: https://www.reddit.com/r/PokemonTabletop/

A public session log describes a forest as a sequence of distinct micro-sites occupied by different wild Pokémon groups and behaviors instead of a homogeneous encounter table.

Reusable lesson:

- a forest becomes memorable when clearings, old growth, stream edges, deadwood, paths, understory and work zones produce different social/ecological situations;
- group behavior can vary by local context without granting unsupported combat bonuses;
- recurring wild actors can become persistent only when observation supports identity, territory or routine.

The log is inspiration only. Do not copy its characters, jokes, exact species groupings, encounter sequence or prose.

## PTU/Caelo mechanics boundary

The project's mechanical source priority remains PTU/Caelo source material, the AutoPTU Python oracle where it encodes the selected rules interpretation, Java parity evidence, and finally the Minecraft/Cobblemon adapter.

Pass 87 does not establish a new forestry subsystem in PTU.

Unresolved mechanics that must be checked against the supplied PTU/Caelo material before execution include:

- whether a specific Move, Capability, Skill, Feature or tool can legally cut, carry, clear, burn, move or process woodland material;
- exact time, quantity, yield, weight or economic value of harvested material;
- any rules for falling trees, unstable branches, smoke, fire, difficult ground, entangling vegetation or weather;
- any mechanical effect from forest cover, undergrowth, deadwood or canopy;
- any Pokémon work contribution that depends on an individual Move/Ability/Capability/Feature;
- any capture, encounter or battle modifier attributed to a managed woodland.

A Minecraft log block breaking is not sufficient evidence that an authorized harvest happened. A Pokémon playing a work animation is not sufficient evidence that a PTU work action succeeded.

## Design conclusions

### A woodland needs persistent management history

A forest should not be represented only as biome + spawn table.

Useful persistent facts include:

- woodland identity and sub-zones;
- observed vegetation/structure changes;
- public trails and work routes;
- active or historical material-use areas;
- restoration patches;
- post-fire/post-storm zones;
- habitat/corridor overlap;
- stewardship/management decisions;
- intervention history;
- product provenance handoffs;
- access changes;
- evidence about regeneration or decline;
- disputed interpretations.

### Observation, cause and policy remain separate

Examples:

- six fresh stumps are observations;
- “the contractor cut six trees” is a claim requiring provenance;
- “the opening caused the wildlife-route change” is an ecological interpretation requiring evidence;
- “close this zone” is a management decision owned by an authorized institution/community state;
- “the opening grants tactical difficult terrain” is a mechanical assertion requiring AutoPTU support.

### Forest products must preserve provenance without simulating every tree

Narratively significant batches can point to a zone and intervention event.

The world does not need one database object per tree.

Create individual persistence for:

- landmark trees;
- culturally/historically significant specimens;
- trees central to a case or restoration project;
- exact fallen logs whose position materially changes access;
- other authored exceptions.

Everything else can remain stand/patch-level state.

### Post-disturbance wood has multiple possible meanings

A fallen tree can be:

- an access blocker;
- deadwood habitat;
- a safety concern;
- recoverable material;
- part of an erosion-control intervention;
- evidence of a storm or earlier cut;
- deliberately retained by a stewardship plan.

The generator must not automatically turn every fallen log into loot or every retained log into “waste.”

### Restoration should create a new history, not erase the old one

A restored patch can retain:

- old cut boundaries;
- changed trails;
- surviving mature trees;
- replanted areas;
- new monitoring points;
- altered wildlife routes;
- public-memory records of the earlier disturbance;
- changed work practices.

“Restored” is therefore an authored management state supported by observations, not a reset to pristine terrain.

### Working forests support long arcs

A useful long-form rhythm is:

1. establish ordinary mixed use;
2. observe a small discrepancy or pressure;
3. trace the cause across work, ecology and access histories;
4. change one intervention or route;
5. return after time has passed;
6. observe intended and unintended effects;
7. revise management;
8. preserve the resulting landscape as the new baseline.

## Minecraft/Cobblemon reuse boundary

Potential reuse targets:

- vanilla/Minecraft logs, leaves, saplings, vines, mushrooms, paths, fences, gates and signs;
- Cobblemon Pokémon entities, models, forms, poses, movement animation and cries;
- particles, ambient sound and weather presentation;
- worksite props and item models where available;
- entity tracking, networking and persistence hooks;
- biome/spawn observations as world inputs after review;
- visual block-state changes for reviewed intervention results.

Required authority direction:

`Ouros woodland/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden authority shortcuts:

- nearby Cobblemon Pokémon -> automatic combatants;
- Cobblemon BattleState/controller -> Ouros battle truth;
- block break -> automatic authorized harvest/yield;
- wildfire visual -> automatic PTU damage/status/hazard;
- species stereotype -> automatic work capability.

## Research status

All source-derived material in this file is research-only. It does not establish a Ouros forest, logging institution, charcoal tradition, legal regime, harvest right, restoration standard, specific species use or canonical technology.

Those remain proposals until reviewed against Ouros canon and PTU/Caelo implementation constraints.