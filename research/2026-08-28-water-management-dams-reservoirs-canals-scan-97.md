# Water Management, Dams, Reservoirs & Canals — Research Scan 97

Status: RESEARCH / PROVENANCE. Not canon. No source below establishes Ouros facts or PTU mechanics by itself.
Date: 2026-08-28

## Why this scan

The repository already contains general agriculture, conservation, public works, facility maintenance, infrastructure outage, fisheries, weather, geology, roads and maritime layers. The full design-tree inventory at the start of this pass showed no dedicated layer for persistent managed-water operations: reservoirs, dams, intake structures, canals, gates, release schedules, diversions and downstream operational effects.

This scan therefore targets a narrow gap: how managed water can become persistent world state without turning Narrative or Minecraft into a hydraulic simulator.

## Existing Ouros boundaries inspected before writing

Relevant existing layers include:

- `design/food-agriculture-hospitality-layer.md`: agricultural sites already have `water_dependency_ids`; irrigation may affect ecology, but exact water infrastructure is not owned there.
- `design/infrastructure-outage-restoration-extension.md`: owns service-zone availability, dependency edges, outages, fallback and restoration sequencing.
- `design/facility-maintenance-repair-inspection-extension.md`: owns technical condition, work orders, repair and inspection.
- `design/civic-governance-public-works-layer.md`: owns public decisions, projects and collective authority.
- `design/conservation-protected-areas-stewardship-layer.md` and `design/interspecies-ecological-relations-layer.md`: own ecological interpretation and protected-area consequences.
- `design/weather-forecast-preparedness-operational-extension.md`: owns forecasts and weather-preparedness state.
- `design/geology-excavation-resource-frontier-layer.md`: owns geological interpretation, excavation and geotechnical evidence.
- `design/travel-transport-expedition-layer.md` and `design/roads-bridges-detours-operational-continuity-extension.md`: own travel/access consequences after a route changes.

The new candidate layer must connect these systems, not duplicate them.

## Public Pokémon sources

### 1. Gaiva Dam / “Dig Those Diglett!”

Sources:
- Bulbapedia, Gaiva Dam: https://bulbapedia.bulbagarden.net/wiki/Giva_Dam
- TVMaze episode summary: https://www.tvmaze.com/episodes/55981/pokemon-1x31-dig-those-diglett

Reusable structure:
A large infrastructure project appears straightforward from the project operator’s point of view, while local Pokémon behavior is initially interpreted as obstruction. Investigation reveals that construction would alter habitat at watershed scale, and the project is cancelled after the ecological consequence becomes legible.

Ouros transformation:
- treat construction intent, ecological observation, causal interpretation, authorization and project cancellation as separate records;
- Pokémon interference is evidence of behavior, not proof of motive;
- a public-works decision may be revised after new evidence without making the original participants secretly malicious;
- stopping a project does not erase the partially altered worksite or the social consequences already created.

Do not import:
- named characters;
- the exact Diglett/Dugtrio scenario;
- trainer rewards;
- the episode’s battle beats;
- any rule that wild Pokémon can automatically veto infrastructure.

### 2. “A Mudkip Mission”

Source:
- Apple TV episode summary: https://tv.apple.com/au/episode/a-mudkip-mission/umc.cmc.4g0fscn5tmwqw2xiigdd4m9ie?showId=umc.cmc.721uypshyjjv0u0zbet4rqu71

Reusable structure:
A dam creates a managed lake that has become habitat and a care site. Damage to the structure changes the water body immediately and creates consequences for the resident Pokémon and caretaker.

Ouros transformation:
- an artificial or managed water body may become real habitat over time;
- infrastructure history matters to ecology even when the asset was originally built for another purpose;
- damage state, water-distribution state, resident safety and repair completion must stay separate;
- restoration may require deciding which historical operating condition to restore rather than blindly returning to the oldest known state.

Do not import:
- the specific Mudkip nursery;
- the antagonist action;
- the exact dam geometry;
- any automatic tactical flood or drowning effect.

### 3. Dam-top route / underwater recovery pattern

Source:
- Bulbapedia, “Sandshrew’s Locker!”: https://bulbapedia.bulbagarden.net/wiki/Sandshrew%27s_Locker%21

Reusable structure:
A dam is simultaneously an infrastructure asset, a route surface and the boundary of a reservoir containing recoverable history below the waterline.

Ouros transformation:
- the same asset can have multiple operational roles without collapsing them into one state;
- reservoir level can affect access to submerged or shoreline evidence;
- a retrieval operation needs its own custody/provenance chain after discovery;
- changing access does not imply that underwater items become loot nodes.

### 4. Ground-type work crew versus water ingress

Source:
- IMDb summary of “Follow the Surfing Saidon!? The Battle at the Lake!”: https://www.imdb.com/title/tt0910433/

Reusable structure:
A construction team can include Pokémon performing real work while an environmental condition creates a practical mismatch with the assigned task.

Ouros transformation:
- Pokémon work participation remains individual and capability-validated;
- assignment, willingness, observed response and actual capability stay separate;
- leakage/water ingress is a technical observation that must be diagnosed before a cause is asserted;
- reassignment or changing the work method can be a legitimate solution without turning every site problem into combat.

Do not import:
- species-based universal labor assumptions;
- the episode’s exact crew composition;
- invented engineering checks.

### 5. Fan-game dam as route + facility

Source:
- Pokémon Glazed community wiki, Seaspray Dam: https://fanmadepokemonglazed.fandom.com/wiki/Seaspray_Dam

Reusable structure:
A dam can function as both a technical facility and a traversable connection between settlements, with access controlled independently from simple physical existence.

Ouros transformation:
- facility operation, public crossing, staff access and technical restricted access can have different states;
- authorization to cross can exist without granting maintenance access;
- a facility may remain present and partially useful during a technical outage.

Do not import:
- the fan game’s pass item;
- trainers, items, Pokémon placements or map layout.

## Supporting infrastructure comparison

Kanto Power Plant provides a useful non-water analogue for persistent infrastructure history: the facility is abandoned in some periods while machinery still works, later refurbished, and its surrounding Pokémon ecology changes with that history. Source: https://bulbapedia.bulbagarden.net/wiki/Kanto_Power_Plant

The reusable lesson is temporal separation between physical structure, service state, ownership/operation, ecological use and later recommissioning. Pass 97 applies the same principle to managed water.

## PTU/Caelo cross-check

The project’s existing source inventory and earlier design work support PTU movement capabilities, Skills, Moves, Abilities, Features, Items and location-specific environmental identities. The inspected material does not establish a universal hydraulic-engineering subsystem.

Pass 97 therefore does not invent:

- reservoir-volume arithmetic;
- flow-rate simulation;
- dam structural HP;
- gate-opening DCs;
- pressure damage;
- current strength tables;
- drowning rules beyond whatever the governing PTU/Caelo sources explicitly provide;
- universal irrigation yield modifiers;
- flood-zone damage;
- bridge/dam collapse mechanics;
- species-based engineering permissions;
- automatic Water/Ground-type labor roles;
- hydropower output formulas.

If later PTU/Caelo review identifies an exact rule, the narrative records should reference that authoritative rule rather than duplicate it.

## Design lessons extracted

Managed water creates strong stories because one intervention can affect several systems at different times. The useful reusable chain is:

`observation -> operational interpretation -> technical diagnosis -> ecological/social review -> authorized intervention -> changed distribution/access -> downstream observations -> verification -> revised operating baseline`

Important separations:

- structure condition versus water-operation state;
- planned release versus executed release;
- gate command versus observed downstream effect;
- reservoir level observation versus cause;
- repair completion versus safe recommissioning;
- water availability versus water quality;
- irrigation availability versus crop outcome;
- ecological response versus assumed motive;
- temporary diversion versus permanent route;
- visual Minecraft water versus authoritative world-state water operation.

## Original Ouros opportunity space

High-value noncombat content:

- reconcile conflicting level/flow observations from different points in a network;
- trace why one agricultural site lost supply while another remained normal;
- compare a posted release schedule with actual observations;
- inspect an old canal that became habitat after decommissioning;
- decide whether a temporary bypass should be removed after the original channel returns;
- document a project whose technical repair succeeded but ecological reopening remains pending;
- reconstruct a historic operating regime from maintenance logs, photographs and downstream testimony;
- investigate whether a reported “gate failure” was actually an upstream shortage, a blocked intake, an outdated notice or a true mechanical fault.

Mechanically rich concepts should use reduced forms until terrain/weather/hazard/reaction, tactical AI and adapter support are verified.

## Provenance policy

All concepts derived from public sources above are transformed structural inspiration. No protected dialogue, distinctive characters, exact plots, bespoke fan-game mechanics or map layouts are copied. Proposed Ouros names and scenarios belong in `proposals/`, while this file remains research/provenance only.