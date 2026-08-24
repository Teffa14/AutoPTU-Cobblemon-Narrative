# Paleontology, taphonomy & fossil-locality research scan — Pass 147

Status: research/provenance only. Nothing in this file is canon unless separately reviewed.

## Why this gap exists

The current Ouros repo already has archaeology, geology-adjacent environmental layers, taxonomy, museums/collections, research ethics and persistent object provenance. Archaeology owns human/cultural deep-history context. Museums own accession, cataloguing, conservation, loans and exhibitions. Taxonomy owns identification/classification. None of those layers currently owns fossils as geological-biological evidence: fossil locality identity, stratigraphic position, trace versus body fossil, taphonomic alteration, excavation jackets/blocks, preparation history, assemblages, or reconstruction of ancient environments.

This pass therefore treats paleontology as a separate evidence system that hands objects to Museums and interpretations to Science/Taxonomy without replacing either.

## Source scan

### Pokémon Fossil Museum — official Pokémon, 2025–2026

Sources:
- https://www.pokemon.com/us/pokemon-news/pokemon-fossil-museum-to-debut-in-north-america-at-chicagos-field-museum — May 14, 2025.
- https://www.pokemon.com/us/news/the-pokemon-fossil-museum-is-now-open — May 22, 2026.
- https://www.pokemon.com/us/pokemon-news/dig-into-the-pokemon-fossil-museum-exhibition-at-chicagos-field-museum — May 28, 2026.

Reusable structure:
- fossil evidence can support education and comparison without becoming a resurrection machine;
- casts, models and real specimens are different object classes;
- scientific interpretation can be publicly exhibited while keeping the underlying evidence and preparation history separate;
- extinct-life reconstruction can be presented as evidence-backed interpretation rather than literal omniscient truth.

Ouros transformation:
- museums may show casts/reconstructions whose labels change as research changes;
- a visually complete skeleton may combine actual fossil material, casts and reconstructed missing portions, all with separate provenance;
- public familiarity with a reconstructed Fossil Pokémon does not imply access to the original specimen or certainty about appearance/behavior.

### “Restore and Renew!” — official Pokémon animation

Source:
- https://www.pokemon.com/us/animation/seasons/23/episode-38-restore-and-renew

Reusable structure:
- museum, excavation site, fossil preparation/restoration technology and a revived Pokémon can coexist as related but separate states;
- an excavation can expose scientifically relevant objects before anyone knows what they are;
- reviving a fossil creates a living Pokémon whose identity/agency is no longer merely collection-object state.

Ouros transformation:
- excavation locality truth remains independent from later Fossil restoration;
- if a future canon-authorized restoration produces a living Pokémon, ownership/custody/agency must hand off to Pokémon Agency rather than remain inside museum inventory;
- a machine accident can be an engineering/crisis incident without changing the specimen’s original locality or stratigraphic record.

### Fossil institutions in the games

Secondary references used only for structural orientation:
- Pewter Museum of Science: https://bulbapedia.bulbagarden.net/wiki/Pewter_Museum_of_Science
- Oreburgh Mining Museum: https://bulbapedia.bulbagarden.net/wiki/Oreburgh_Mining_Museum
- Nacrene Museum: https://bulbapedia.bulbagarden.net/wiki/Nacrene_Museum

Reusable structures:
- excavation, mining, museum interpretation and Fossil restoration may be institutionally linked;
- not every fossil-bearing place is a museum and not every museum controls the extraction site;
- fossils can enter public culture through display, education, research and restoration separately.

### PTU public material: Paleontologist as an explicit rules concept

Project evidence:
- `Teffa14/AutoPTU/reports/trainer_runtime_coverage.md` includes `Paleontologist` but currently reports it as `missing_runtime_mapping`.

Public PTU-derived reference encountered during research:
- https://1e.ptr.wiki/Rules/Playtests/Class-Reworks/Researcher

Important boundary:
- public PTU/PTR material demonstrates that active fossil searching and a Paleontologist concept exist in the tabletop ecosystem;
- this narrative task does not import quarry DCs, fossil-finding frequency, skill thresholds, special revived-Pokémon qualities or any playtest/homebrew mechanics into Ouros;
- current AutoPTU runtime evidence specifically says Paleontologist is not mapped, so Trainer Features/perks remains a dependency if any encounter requires that mechanical benefit.

### Public PTU campaign log

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/mtp9cf

Reusable high-level structure:
- fossil discovery can sit inside a cave expedition alongside reconnaissance, murals, rival forces and battles;
- the fossil can remain relevant beyond the session in which it was found.

Transformation rule:
- do not copy the homebrew Fossil mutation, characters, factions or plot;
- reuse only the layered expedition grammar: exploration → contextual find → preservation/extraction problem → later research consequence.

### NPS: fossils, context and taphonomy

Sources:
- https://www.nps.gov/subjects/fossils/about-fossils.htm
- https://www.nps.gov/subjects/fossils/taphonomy.htm
- https://www.nps.gov/subjects/fossils/significance.htm
- https://www.nps.gov/subjects/fossils/what-is-a-fossil.htm
- https://www.nps.gov/subjects/fossils/paleontology-and-archeology.htm

Reusable principles:
- fossils include body fossils and trace fossils;
- preservation is highly biased and incomplete;
- taphonomy covers what happens between death and fossilization, including decay, scavenging, transport, burial, breakage and post-burial alteration;
- exact geologic context matters: locality, layer, rock/sediment, orientation and associated finds;
- excavation is destructive in the technical sense that removing a fossil breaks its original physical context, so documentation before removal is essential;
- paleontological and archaeological grids/tools may look similar while the research questions and authorities remain different.

Ouros consequences:
- absence from the fossil record never proves biological absence;
- a concentration of bones does not automatically prove a herd died together;
- disarticulated remains may have been transported or disturbed;
- a footprint/trackway can be paleontological evidence even without body remains;
- removing a Fossil item from Minecraft blocks without recording its context can permanently reduce what the world can know about it.

### Smithsonian: field-to-museum preparation

Source:
- https://naturalhistory.si.edu/education/teaching-resources/paleontology/fossil-preparation-field-museum

Reusable chain:
field discovery → stabilization/secure transport → preparation → interpretation → collection/display/research.

Ouros consequence:
- “found a fossil” and “museum-ready specimen” are very different states;
- a specimen can spend months or years in matrix/jacket/preparation without becoming a different object;
- preparation may expose additional structures and revise earlier identifications.

### USGS: locality, stratigraphy and collection records

Sources:
- https://pubs.usgs.gov/of/2001/of01-223/wardlaw.html
- https://www.usgs.gov/data/cenozoic-and-mesozoic-denver-vertebrate-fossil-collection-us-geological-survey-core-research

Reusable architecture:
- locality, stratigraphic section, specimen record and museum repository identifier are linked but distinct records;
- older field maps and notebooks can later be digitized and linked to specimens;
- the scientific value of a specimen depends heavily on retaining where and in what stratigraphic context it was collected.

## Design lessons extracted

1. Fossil identity and Fossil Pokémon identity must remain separate.
2. Body fossil, trace fossil, cast, reconstruction, matrix block and living restored Pokémon are different object/entity classes.
3. Site context must survive excavation through records because the physical context may be destroyed by removal.
4. Taphonomic interpretation needs hypotheses with evidence, not instant labels such as “predation site” or “mass death”.
5. A fossil assemblage is not a census of the ancient ecosystem.
6. Preservation bias should create uncertainty and research hooks rather than procedural rarity scores.
7. Stratigraphic revisions can make an old field note more informative without making the note “wrong”.
8. Public exhibits can simplify science; the research record should preserve nuance and uncertainty.
9. Fossil restoration, if canon later permits it, is a separate high-stakes transformation with an explicit handoff to Pokémon Agency.
10. Paleontology should connect to Geology, Taxonomy, Museums, Science, Climate/ancient-environment reconstruction and Research Ethics, but own none of their downstream decisions.

## Candidate narrative grammars

- roadcut/storm/erosion exposes a new locality → survey → stabilize → determine whether excavation is justified → document context → prepare specimen → revise interpretation years later;
- museum drawer specimen lacks reliable locality → archive search → compare old field notebook/map/photo → recover probable context → reclassify confidence rather than pretending certainty;
- trackway crosses an infrastructure project → record first → alter project plan or recover what can be preserved → public debate → later research;
- spectacular skull receives public attention while unglamorous pollen/microfossils/sediment provide the stronger ancient-environment evidence;
- two teams reconstruct the same assemblage differently because one emphasizes body fossils and the other taphonomic transport;
- a restored Fossil Pokémon becomes a living participant whose current behavior cannot be treated as a direct recording of prehistoric behavior.

## Mechanics/rules guardrails

Do not infer:
- Paleontologist Edge/Feature benefits from narrative training;
- Pokémon Education or Survival DCs for fossil finding;
- Fossil availability rates;
- restoration legality, timing, cost or success rate;
- revived Pokémon species/Nature/Ability/Level/Move set;
- ownership of a revived Pokémon;
- Rock/Ground type from fossil context;
- ancient Moves/Abilities from morphology;
- excavation damage, cave-in damage, falling rocks or rough terrain from narrative description;
- fossils as loot simply because Minecraft exposes a block;
- a fossil locality as an infinite respawn source.

Current AutoPTU evidence shows `Paleontologist` in source content but `missing_runtime_mapping`. AutoPTU-Java does not expose a fossil/paleontology subsystem. PTU/Caelo source extraction must therefore precede any mechanical fossil-search or restoration rule.

## Caelo / Super PTU Online Helper status

No reliable Caelo-specific paleontology/restoration rule source was recovered through the project repositories in this run. Super PTU Online Helper was not exposed as an invocable capability. No output has been invented for either source.

## Provenance policy for generated Ouros material

All downstream material from this scan remains PROPOSED/NON-CANON. Source notes preserve attribution. Original Ouros names, institutions, localities and stories must be newly authored rather than copied from Pewter, Oreburgh, Nacrene, the Field Museum exhibit, PTU campaign logs or real-world fossil sites.