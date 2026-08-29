# Ouros Narrative Research — Wastewater Collection, Treatment & Release Continuity — Pass 116

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is established Ouros canon.
Date: 2026-08-28

## Scope and repository gap

The full narrative repository tree was inspected before authoring. Existing authority already covers broad waste/sanitation/pollution, drinking-water treatment and distribution, stormwater drainage, water management, infrastructure outages, facility maintenance, conservation, care and public works.

The broad Waste/Sanitation layer already contains a small `wastewater_flow_state` and generic treatment-site model. It intentionally does not preserve the operational chain in enough detail for persistent incidents, restoration, partial service, verification, release handoffs or long-lived sewer history. Drinking-Water Continuity explicitly leaves wastewater to Waste/Sanitation. Stormwater Continuity explicitly leaves sanitary wastewater and treatment to Waste/Sanitation.

Pass 116 therefore researches a specialized continuity extension underneath that existing authority. The proposed extension should preserve collection sectors, authored conveyance links, lift/pump stations, treatment stages, verification, release/receiving handoffs, bypass or overflow observations, temporary arrangements and staged recovery. It must not become a hydraulic, chemistry, public-health or regulatory simulator.

## Pokémon source — Waterworks, Pokémon Ranger

Source: https://bulbapedia.bulbagarden.net/wiki/Waterworks

The Waterworks are described as the sewage system beneath Fall City. The location is explorable as infrastructure, supports a mission, contains Pokémon activity and exists as a meaningful place beneath an ordinary settlement.

Reusable high-level lessons:

- a sewer network can be a persistent place rather than a one-use dungeon;
- infrastructure can support maintenance, investigation, ecology and conflict at the same time;
- Pokémon presence inside infrastructure is an observation, not proof that the Pokémon caused a service problem;
- access to one part of a network need not establish the state of the whole network;
- a service-space adventure can occur without converting every pipe, pool or machine into a battle mechanic.

Ouros transformation:

Use authored wastewater-network locations as durable world objects with operational and historical state. A recurring Pokémon individual or collective may use a gallery, access corridor or dry ledge, but species identity never proves blockage, contamination, treatment capability or immunity.

Rejected copying:

Do not reproduce the mission plot, named antagonists, Grimer-release scheme, map layout, dialogue, capture sequence or distinctive encounter progression.

## Pokémon source — Lumiose Sewers

Source: https://bulbapedia.bulbagarden.net/wiki/The_Sewers

The Lumiose Sewers are described as an extensive sewer system under Lumiose City while only particular sections are accessible to the player.

Reusable high-level lessons:

- network extent and player-accessible extent are separate facts;
- inaccessible infrastructure may still exist in world state;
- separate districts can connect to one larger network without every link being traversable gameplay space;
- later content can reveal another access point without retconning the network into existence.

Ouros transformation:

Preserve stable network IDs, sector IDs and access-point IDs independently. World simulation may know that an authored connection exists while exploration exposes only reviewed sections. Minecraft geometry must never auto-discover hidden sewer topology.

Rejected copying:

Do not copy district layouts, encounters, quests, NPCs or exact sewer maps.

## Pokémon source — Sea of Wailord, Pokémon Ranger: Shadows of Almia

Source: https://bulbapedia.bulbagarden.net/wiki/Sea_of_Wailord

The area is described as a marine location affected by pollutants and discarded supplies associated with an old offshore industrial site.

Reusable high-level lessons:

- a downstream receiving environment can preserve the history of an upstream or adjacent facility after that facility changes use or closes;
- pollution evidence, discarded material, navigation consequences and ecological state can persist on different timelines;
- legacy infrastructure can remain narratively relevant after its original operation ends.

Ouros transformation:

Wastewater release handoffs should point to the receiving-system owner rather than directly rewriting ecology. A treatment or release incident can create evidence and investigation hooks while Conservation, Fisheries, Water Management or another governing system determines ecological consequences.

Rejected copying:

Do not copy the oil-field plot, named corporation, location geography, specific pollution cause or mission structure.

## Pokémon Tabletop community material

Public PTU searches in this pass did not yield a sufficiently specific, well-documented wastewater campaign log worth treating as design evidence. Several public PTU discussions instead reinforced a broader existing lesson: PTU campaigns are commonly homebrewed and public examples can mix setting invention with custom rules.

Pass 116 therefore does not treat community sewer maps, custom Poison effects or homebrew environmental rules as PTU authority. The internal PTU/Caelo source set remains controlling for mechanics.

## Operational research — wastewater networks as many distinct assets

Source: https://www.epa.gov/npdes/smart-sewer-technologies
Source: https://www.epa.gov/npdes/smart-sewers

Public wastewater material distinguishes collection and treatment infrastructure such as pipes, sewer mains, manholes, pumps, lift stations, valves, storage and treatment assets. It also describes monitoring at selected locations and operational decisions that can route or store flow in response to system conditions.

Reusable abstract lessons only:

- one network contains multiple independently observable assets;
- monitoring coverage can be partial;
- asset state, network state and treatment state should not collapse into one flag;
- a local intervention can improve one bottleneck without proving full-system recovery;
- routing/storage decisions need provenance and effective windows;
- a monitoring gap is uncertainty, not evidence that nothing happened.

Ouros must not import real-world capacities, sensors, software, automation levels, operating procedures, engineering formulas or regulatory obligations.

## Operational research — influent, treatment, effluent and receiving handoff

Sources:

- https://www.epa.gov/compliance/clean-water-act-cwa-compliance-monitoring
- https://www.epa.gov/eg/effluent-guidelines-implementation-compliance

The external material distinguishes incoming wastewater, treatment operations, monitored discharge and downstream receiving environments. It also shows why treatment completion, monitoring evidence and an authorized/recorded discharge are conceptually separate stages.

Reusable abstract lessons:

- received material and treated output are different subjects;
- treatment operation and output verification should have separate records;
- a release point should be an explicit handoff rather than an invisible world-state mutation;
- bypass/overflow observations need timestamps and scope;
- downstream environmental or health consequences should be decided by the systems that own them.

Ouros does not inherit permit structures, pollutant limits, sampling schedules, legal standards or treatment requirements from these sources.

## Design synthesis

The specialized continuity layer should preserve at least these distinctions:

`COLLECTION_PATH_AVAILABLE != EVERY_SOURCE_CONNECTION_AVAILABLE`

`PUMP_RUNNING != FLOW_PATH_VERIFIED`

`WASTEWATER_RECEIVED != TREATMENT_COMPLETE`

`TREATMENT_STAGE_RUNNING != OUTPUT_VERIFIED`

`OUTPUT_VERIFIED != RELEASE_HANDOFF_AUTHORIZED`

`RELEASE_HANDOFF_AUTHORIZED != RELEASE_OBSERVED_COMPLETE`

`OVERFLOW_OBSERVED != CAUSE_CONFIRMED`

`BYPASS_RECORDED != ENVIRONMENTAL_HARM_ESTABLISHED`

`POWER_RESTORED != WASTEWATER_SERVICE_RESTORED`

`REPAIR_COMPLETE != ASSET_VERIFIED`

`NETWORK_VERIFIED != DOWNSTREAM_SYSTEM_RECOVERED`

These separations support mysteries and recovery stories without fabricating hidden truth.

## Narrative structures worth reusing

A local service failure can generate several adventures over time: first access/security, later inspection, then temporary routing, treatment verification, downstream assessment and eventual decommissioning of the workaround.

A sewer sector can acquire social and ecological history. Workers remember old names; residents remember a temporary access point; Pokémon may repeatedly use an unused gallery; a map revision can make two apparently contradictory records both correct.

A downstream observation can precede causal proof. Odor, discoloration, unusual wildlife movement or a reported overflow can create an investigation, but each remains evidence with scope and provenance until the governing system establishes more.

Recovery can change the city. A temporary pump site may become an emergency asset. An old outfall may become a monitored habitat or heritage object. A decommissioned alignment may survive in plans and local language long after service moves elsewhere.

## PTU/Caelo guardrail

The internal source scan remains controlling. Caelo proves that an authored location can carry a specific mechanical environmental identity when its governing source defines one. It does not authorize a universal sewer/wastewater hazard subsystem.

Pass 116 found no governing internal evidence for universal rules covering wastewater current, drowning, contamination damage, automatic Poison, infection, gas exposure, slippery surfaces, confined-space effects, pump suction, pressure, moving machinery, sewer-depth changes, treatment chemistry or species/type immunity.

Those remain UNKNOWN unless exact PTU/Caelo evidence and current engine contracts support them.

## Originality boundary

This pass extracts only high-level structures: persistent network identity, partial access, multi-stage operation, evidence provenance, downstream handoffs, staged restoration, legacy infrastructure and ecology/infrastructure coexistence.

No protected prose, dialogue, named character arc, map, puzzle, mission sequence or distinctive plot is copied into Ouros.