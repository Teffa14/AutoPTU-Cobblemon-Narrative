# Digital Systems, Cyberspace & Data Research — Pass 48

Status: research and provenance only. Not Ouros canon. Not a PTU rules source.

Date: 2026-08-20

## Scope

This pass investigates digital persistence, software, data versioning, virtual spaces, Pokémon-machine relationships and cyber-themed adventure structures that can enrich Ouros without duplicating the existing Technology/Energy and Media/Communications layers.

Existing project boundaries reviewed before research:

- `design/technology-energy-infrastructure-layer.md` owns physical machines, utility networks, faults, maintenance and control interfaces.
- `design/media-communications-information-layer.md` owns information packets, communication channels, coverage, delivery and contact graphs.
- `design/archives-museums-collections-preservation-layer.md` owns archival collections and institutional preservation.
- `design/photography-visual-evidence-layer.md` owns interpretation and provenance of visual records.
- `design/pokemon-agency-partnership-release-layer.md` owns persistent Pokémon identity and partnership history.

No existing dedicated cyberspace/data-versioning layer was found in the narrative repository.

## Source findings

### Official Pokémon: Porygon and digital space

The official Pokémon Pokédex describes Porygon as an artificial Pokémon created through advanced science and explicitly says it can move through cyberspace.

Source: https://www.pokemon.com/us/pokedex/porygon

Reusable structure:

- cyberspace can be a setting that at least some Pokémon can interact with directly;
- a Pokémon capable of entering digital environments remains a Pokémon actor, not merely a software process;
- digital traversal should be species/capability grounded rather than a universal Trainer action.

This source does not define PTU movement rules, data-access permissions, hacking, teleportation or storage metaphysics.

### Official Pokémon: programming does not fully define behavior

The official Porygon2 Pokédex describes an upgraded artificial Pokémon that can display behavior not contained in its programming.

Source: https://www.pokemon.com/us/pokedex/porygon2

Reusable structure:

- authored software state and actor intent should remain distinct;
- unexpected behavior should not automatically be diagnosed as corruption, sabotage or malfunction;
- institutions may disagree about whether a digital Pokémon is following a task, adapting independently or experiencing a fault.

### Official Pokémon: software modification can create unintended outcomes

The official Porygon-Z Pokédex describes programming modified for a new purpose that did not work as intended.

Source: https://www.pokemon.com/uk/pokedex/porygon-z

Reusable structure:

- software releases can have intended goals, actual results, known issues and rollback/review history;
- a failed modification is not automatically malicious;
- historical software versions can become narratively significant.

No Porygon-Z-specific plot or mechanical effect is copied into Ouros.

### Official Pokémon: digital terminals as public infrastructure

The official Galar material for Poké Jobs describes Rotomi terminals in Pokémon Centers as multi-service interfaces used for Poké Jobs, Boxes and other functions.

Source: https://swordshield.pokemon.com/en-us/gameplay/pokejobs/

Reusable structure:

- public terminals can expose several services while those services remain separately governed;
- a terminal is an interface, not necessarily the authoritative data store;
- outage of one service need not imply failure of every service at the same terminal.

The Poké Job reward and growth mechanics are not imported.

### Official PTU campaign design: The Apparatus

The Pokémon Tabletop campaign seed “Mysterious Ruins” includes The Apparatus, a vast technological environment combining city, supercomputer, factory and segmented habitats. Administrator Porygons manage functions while the scenario deliberately leaves questions about intelligence, automation, simulation and persistence open.

Source: https://pokemontabletop.com/campaign-seeds-mysterious-ruins/

Reusable structures:

- infrastructure can itself become an explorable world;
- distinct sectors can have different rules, histories and service states;
- automated systems and intelligent actors must not be conflated;
- virtual-world revelations create stronger stories when persistence, identity and exit conditions are explicitly decided rather than hand-waved;
- system degradation can cause migration and institutional consequences without requiring a villain.

This source is used as campaign-design inspiration only. Its Pods, AIs, history and plot directions are not Ouros canon.

### PTU campaign retrospective: technical Pokémon as persistent characters

The Tales of Visiwa retrospective describes a long-running PTU character whose Porygon-Z remained part of her scientific/technical identity and participated against technologically capable opponents.

Source: https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Reusable structure:

- technical Pokémon can be recurring characters across many adventures rather than one-off puzzle keys;
- scientific or technical careers can intersect battles, research and world events;
- a Porygon can have persistent character history independent of the systems it accesses.

No campaign characters, custom effects or story beats are transplanted.

### Fangame precedent: digital spaces as explorable places

Super Pokémon Eevee Edition publicly describes an explorable glitch world in which code and data become the environment.

Source: https://eeveeexpo.com/spee/

Reusable structure:

- digital spaces can use different visual/navigation grammar from the physical world;
- data structures can become landmarks, barriers or environmental storytelling;
- returning from a digital space should preserve clear continuity with the physical world.

The source's characters, plot, glitch-world content and battle system are not copied.

### Virtual-world architecture research

Kim J. L. Nevelsteen’s research distinguishes virtual-world properties and discusses pseudo-persistence versus stronger persistence models.

Source: https://doi.org/10.1002/cav.1752

Reusable design lesson:

Ouros should never use the label “persistent virtual world” without defining what actually persists when participants disconnect. A cyberspace instance may be:

- ephemeral;
- resettable;
- snapshot-restored;
- actor-persistent;
- state-persistent;
- linked to a continuously changing physical service.

Those properties should be authored explicitly.

## Cross-source conclusions

### Data is not truth

A database stores records and claims. It does not become canonical world truth merely because it is official.

Digital records therefore need the same provenance discipline already used by Ouros for publications, photographs, cases and archives.

### Restore is not time travel

Restoring software or data from a backup can change current system state. It cannot erase Chronicle events, player memories, previously published information or consequences that occurred after the snapshot.

### Logs are observations produced by systems

A log entry can support a claim. A missing log entry can mean that nothing occurred, logging was disabled, coverage failed, retention expired, the wrong system was queried or the record was altered. Narrative generation must not choose among those explanations without evidence.

### Account identity and real identity are separate

A digital account, handle, device session or credential is evidence about access. It does not automatically prove which person used it.

This extends the existing Ouros rule that presented identity and real identity remain separate.

### Pokémon are not files

Even when official Pokémon games use digital-style storage interfaces, Ouros must not infer that a Pokémon is a copyable file, can be restored from backup, can be duplicated, or ceases to be the same persistent individual.

Pokémon identity remains owned by the Pokémon Agency layer.

### Porygon access is not universal authorization

Official material supports Porygon interacting with cyberspace. It does not imply that every Porygon can:

- read every file;
- bypass credentials;
- control every machine;
- rewrite databases;
- transport Trainers through networks;
- defeat digital security automatically.

Exact PTU/Caelo capabilities still require source extraction and implementation validation.

### Rotom interaction is not universal network access

Rotom’s association with devices should remain separate from data authorization. Entering or inhabiting an appliance does not automatically expose every connected system or private record.

## PTU/Caelo boundary

The official Pokémon Tabletop resources remain the rules authority family for this project, with PTU 1.05 and its associated Pokédex/supplement material serving as the baseline external rules set.

Source: https://pokemontabletop.com/downloads-and-resources/

This runtime did not provide sufficiently reliable direct extraction of the supplied PTU/Caelo text for every digital interaction. Therefore Pass 48 does not define:

- Technology Education DCs;
- computer intrusion rules;
- Porygon cyberspace movement mechanics;
- Rotom device-control mechanics;
- cybernetic Features;
- Upgrade/Dubious Disc effects beyond governing source rules;
- digital Pokémon storage metaphysics;
- remote device possession;
- data-transfer speeds;
- software-derived battle bonuses.

These remain unresolved until checked against the project’s PTU/Caelo corpus and actual engine support.

## Copyright and transformation policy

This pass records URLs, factual source descriptions and abstract structural lessons. It does not copy source dialogue, prose, unique characters, distinctive locations, puzzles or plots into Ouros.

External material remains research provenance. Original Ouros concepts belong in `proposals/` and remain non-canon until reviewed.
