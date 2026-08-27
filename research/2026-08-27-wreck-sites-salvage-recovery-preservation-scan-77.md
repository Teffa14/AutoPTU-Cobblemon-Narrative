# Wreck Sites, Salvage, Recovery & Preservation Research — Pass 77

Status: research/provenance only. Nothing in this file is automatically Ouros canon.

Date: 2026-08-27

## Research question

How can Ouros use wrecks, abandoned transport, flooded facilities and other partially lost structures as persistent places that can support exploration, recovery, ecology, historical investigation and later reuse without turning every object into loot or every ruin into a disposable dungeon?

This pass deliberately does not establish property law, salvage rights, archaeology law, diving rules, underwater combat rules, pressure/decompression rules, drowning rules, environmental damage, item values or Pokémon movement capabilities. Those remain subject to Ouros canon review, PTU/Caelo rules and authoritative engine evidence.

## Internal repository review before research

The complete repository tree was inspected before authoring. The closest existing layers are:

- `design/material-culture-economy-crafting-layer.md`, which already owns persistent item identity, provenance and `SALVAGED` as a possible acquisition method;
- `design/travel-transport-expedition-layer.md`, which owns routes, transport services and expedition logistics;
- `design/archives-museums-collections-preservation-layer.md`, which owns accession, conservation and institutional collections;
- `design/conservation-protected-areas-stewardship-layer.md`, which owns ecological protection and stewardship;
- `design/case-authority-custody-layer.md`, which owns evidence, formal custody and institutional authority;
- `design/found-property-custody-restitution-extension.md`, introduced in Pass 66, which owns ordinary found-property claims and return workflows;
- `design/facility-maintenance-repair-inspection-extension.md`, which owns repair/inspection of active or recoverable facilities;
- `design/crisis-rescue-recovery-layer.md`, which owns active emergencies and recovery after crisis;
- `design/cartography-survey-wayfinding-layer.md`, which owns survey observations and mapped access;
- `design/cobblemon-runtime-authority-boundary.md`, which keeps Minecraft/Cobblemon downstream from Ouros/AutoPTU authority;
- `design/encounter-implementation-contracts.md`, which requires full/reduced encounter forms and permanent capability categories.

No dedicated wreck-site lifecycle exists in the inspected tree. The gap is not generic archaeology, generic found property or generic travel. It is the persistent site-level relationship between structural remains, recoverable objects, historical context, ecological occupation, access, survey state and later intervention.

## Source scan

### 1. Pokémon Ruby/Sapphire/Emerald — Abandoned Ship

Source:
https://bulbapedia.bulbagarden.net/wiki/Abandoned_Ship

Relevant high-level structure:

- a former passenger/cargo vessel persists as an explorable wreck;
- some areas are inaccessible until a later traversal capability is available;
- flooded sections, locked rooms and scattered contents create layered access rather than one linear corridor;
- a specific recovered device matters because of its history/function, not because every surviving object is equally important;
- the same location can support exploration, trainers, hidden objects and environmental occupation.

Reusable Ouros lesson:

A wreck should have a site state, access topology and provenance. Reaching the wreck does not imply reaching every compartment. Recovering one significant object does not turn the whole site into unowned loot.

Do not copy:

- the S.S. Cactus identity;
- Scanner quest structure;
- exact room/key sequence;
- hidden-item placements;
- named NPCs or rewards.

### 2. Pokémon Omega Ruby/Alpha Sapphire — Sea Mauville

Source:
https://bulbapedia.bulbagarden.net/wiki/Sea_Mauville

Relevant high-level structure:

- a closed industrial marine facility remains physically present after operations cease;
- records and remnants preserve workplace history;
- an environmental survey later identifies the abandoned structure as a unique habitat;
- planned demolition is canceled and the site becomes a preserve;
- the location therefore changes meaning across time: workplace -> abandoned infrastructure -> ecological habitat -> protected site visited by others.

Reusable Ouros lesson:

Abandonment is a transition, not deletion. A failed or retired facility can acquire ecological, historical and public-memory value. Later recovery decisions should consider multiple owners of state: maintenance, ecology, archives, public access and possibly former operators.

Important boundary:

The source contains deliberately extreme workplace slogans and specific corporate history. Ouros should not copy those details or infer identical labor culture.

### 3. Pokémon Adventures — Abandoned Ship use and ecological occupation

Source:
https://bulbapedia.bulbagarden.net/wiki/Abandoned_Ship

Relevant high-level structure:

- abandoned cargo can indirectly change the site ecology over time;
- wild Pokémon can occupy and interact with the wreck as habitat;
- later conflict can revisit the same place under different stakes;
- a wreck can be a recurring landmark rather than a one-use dungeon.

Reusable Ouros lesson:

Store the wreck's ecological occupation separately from its historical identity. A known wreck can support later callbacks after weather, species occupation, human access or structural condition changes.

Do not copy named characters, antagonists, exact species combinations or plot beats.

### 4. Pokémon Rejuvenation — Shipwreck Recovery

Sources:
https://rejuvenation.wiki.gg/wiki/Shipwreck_Recovery
https://rejuvenation.wiki.gg/wiki/S.S._Oceana_Wreckage

Classification: fan game inspiration only; not a rules source.

Relevant high-level structure:

- a wreck persists long after the original incident;
- access requires later capabilities and a dedicated staging point;
- the recovery objective is distributed across several points on the structure;
- the player performs a bounded technical support task and returns to an organizer rather than simply taking possession of the wreck;
- underwater rooms retain their own ecology and optional discoveries.

Reusable Ouros lesson:

Separate `site access`, `survey`, `intervention plan`, `intervention points`, `recovery execution` and `post-recovery state`. A player can contribute to a recovery project without owning the vessel or deciding what happens to every recovered object.

Do not copy the S.S. Oceana, Wreckage Rig, flotation-device sequence, rewards, characters or proprietary mechanics.

### 5. Pokémon Rejuvenation — sidequest taxonomy and revisitation

Source:
https://rejuvenation.wiki.gg/wiki/Sidequests

Relevant high-level structure:

The same game treats restoration/recovery as one sidequest family among rescue, delivery, investigation and battle. This supports a useful Ouros principle: a wreck-site story can be primarily survey, recovery or preservation and need not culminate in a boss battle.

### 6. UNESCO underwater cultural heritage principles

Sources:
https://www.unesco.org/en/underwater-heritage/principles-2001
https://www.unesco.org/en/underwater-heritage/annex

Classification: real-world operational reference only. Do not import law or institutional authority into Ouros.

Relevant high-level structure:

- inventory/documentation comes before intervention;
- preservation in place can be preferable to removal;
- recovered objects require conservation and management rather than instant reuse;
- non-intrusive observation can be valuable;
- project design, qualifications, documentation and site-management plans matter.

Reusable Ouros lesson:

A discovery does not automatically authorize excavation. A recovered object may become harder to preserve after removal. Wreck-site gameplay can therefore include survey, stabilize-in-place, document, restrict access, recover selectively or leave untouched.

Do not import:

- UNESCO jurisdiction;
- international-law rules;
- ownership rules;
- sanctions;
- age thresholds;
- permit procedures.

Those are real-world law/policy, not Ouros canon.

### 7. NOAA conservation surveys and maritime archaeology

Sources:
https://oceanexplorer.noaa.gov/technology/conservation-surveys/
https://oceanexplorer.noaa.gov/explainers/archaeology/

Classification: real-world technical inspiration only.

Relevant high-level structure:

- site condition and environmental context are documented repeatedly;
- deterioration can be monitored over time;
- archaeologists and conservation specialists may need different observations;
- intervention decisions can follow longitudinal evidence rather than one visit;
- cargo and structural context together tell a story that isolated objects cannot.

Reusable Ouros lesson:

A wreck-site record should support repeated condition surveys. Removing an object should append a recovery event while preserving its original context reference.

### 8. PTU community material — campaign flexibility and environmental logic

Public searches across Pokémon Tabletop communities did not produce a high-confidence, well-documented shipwreck PTU actual-play source during this pass. This absence is recorded rather than filled with a guessed citation.

Useful adjacent PTU community discussion repeatedly emphasizes that GMs use environment, traversal and Trainer capabilities differently across campaigns. For Pass 77 that means exact underwater access, diving endurance, aquatic Pokémon behavior and environmental battle effects must remain source-reviewed rather than invented from genre expectations.

## Cross-project mechanical evidence

### AutoPTU-Java

Inspected `main` head during this pass:

`c3b94bf4d4d5d0c3939bed027d3f9556b7c300e9`

Current live evidence includes:

- VERIFIED targeting/footprints/range/LoS;
- VERIFIED base Shift/Jump movement legality;
- VERIFIED core calculation primitives;
- VERIFIED action economy/initiative;
- VERIFIED AI legal-action infrastructure;
- increasingly real held-item START lifecycle ownership, rule profiles and Magic Room suppression.

The current README still explicitly leaves unfinished:

- core combatant/grid battle state;
- full damage resolution;
- full StatusController;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This means no underwater hazard, current, pressure, unstable deck, flooding, forced displacement or objective-aware escape logic may be assumed executable merely because the overworld can depict it.

### AutoPTU Python

Inspected `main` head during this pass:

`11c4aea350193d2ed0940ec5a8ada09e44b6d291`

The latest change lets the full active Career squad complete seasonal training. This is progression/roster behavior and does not add a new tactical family needed by Pass 77.

### Cobblemon boundary

Pass 77 follows `design/cobblemon-runtime-authority-boundary.md`.

Cobblemon should be reused aggressively for:

- aquatic Pokémon embodiment;
- models, textures, animations, cries and particles;
- entities and overworld tracking;
- swimming/flying visual locomotion;
- water blocks, bubbles, lighting and environmental presentation;
- UI, networking and interaction surfaces;
- persistent props and site markers where appropriate.

Cobblemon must not decide:

- which nearby Pokémon become combatants;
- battle participants or sides;
- tactical HP/status/positions;
- legal moves/targets;
- underwater battle legality;
- current/pressure/hazard effects;
- victory/defeat/capture outcomes;
- whether a recovered object grants a battle effect.

Ouros decides world facts and participants. AutoPTU decides tactical facts. Cobblemon projects and presents the committed state.

## PTU/Caelo source-review gates

Before mechanically rich wreck or underwater content becomes authoritative, review project sources for at least:

- legal Swim/Sky/Overland movement for each participant;
- underwater combat assumptions;
- drowning/suffocation if any;
- water/underwater terrain rules;
- visibility/LoS changes if any;
- weather interactions;
- pressure/depth effects if any;
- forced movement/currents if any;
- falling/collapse/debris effects if any;
- object interaction/action costs;
- Trainer Skill/Feature requirements for diving, surveying or technical work;
- Pokémon capabilities used for transport, lifting, cutting, carrying or sensing;
- item behavior for diving/recovery equipment when mechanically relevant.

Narrative world state may depict depth, corrosion, blocked compartments, unstable structure and water ingress without converting those facts into tactical modifiers until the governing mechanics exist.

## High-level design conclusions

1. A wreck is a persistent site, not a loot container.
2. Site identity survives recovery, partial dismantling, stabilization and ecological occupation.
3. Historical context, structural condition, ecology, access and recoverable objects need separate state.
4. Discovery does not imply ownership, salvage permission or excavation authority.
5. Recovery of an object appends provenance; it does not erase original context.
6. In-place preservation can be a meaningful successful outcome.
7. A former industrial/transport site can become habitat, memorial, archive subject, public attraction, restricted zone or redevelopment candidate over time.
8. Players can contribute to survey/recovery without becoming the site owner or project authority.
9. A wreck can support multiple visits with different purposes as new access, evidence, weather, ecology or institutional priorities emerge.
10. Battle is optional. Survey, mapping, documentation, stabilization, custody and negotiation can carry the scenario.
11. Minecraft/Cobblemon should provide as much physical embodiment as possible while never becoming the tactical or ownership authority.
12. Mechanically rich underwater encounters require the same permanent capability map as any other encounter and cannot be simulated by Minecraft-side shortcuts.

## Originality boundary

Pass 77 uses only high-level structures: layered access, persistent remains, selective recovery, repeated survey, ecological reoccupation, preservation-vs-intervention decisions, provenance and staged recovery. It does not copy protected dialogue, named characters, exact quests, item placements, maps or distinctive plot sequences.