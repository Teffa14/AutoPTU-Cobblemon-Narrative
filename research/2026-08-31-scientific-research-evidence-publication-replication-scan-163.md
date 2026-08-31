# Ouros Narrative Research — Scientific Research, Evidence, Publication & Replication — Pass 163

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-31

## Why this pass exists

The repository inventory and adjacent systems were inspected before writing.

Existing ownership is already strong:

- Observation, Settlement & Time owns observation events, knowledge records, field reports and research opportunities.
- Archives, Museums & Collections owns preserved notebooks, specimens, datasets, catalog records and research collections.
- Material Culture owns physical item identity and provenance.
- Case / Authority / Custody owns evidence custody when a sample is part of an investigation.
- Travel / Expedition owns expedition movement and field logistics.
- Media owns publication as communication and attributed claims.
- Public Memory owns later social remembrance.
- Care, ecology, archaeology, agriculture, weather and other domain layers own their subject-specific facts.

What is still missing is the continuity between a research question and the scientific record built around it: project definition, protocol or method version, observation/sample/dataset links, analysis episodes, interpretation, internal review, publication, replication, correction, retraction and downstream reliance.

This pass does not create a universal science minigame, research XP track, laboratory crafting subsystem, ethics code, peer-review law, sample-collection right or Researcher/Scientist Feature rewrite.

## Official Pokémon source — ecological survey as repeated field observation

Source: https://newpokemonsnap.pokemon.com/en-us/create-photodex/
Source: https://newpokemonsnap.pokemon.com/en-au/explore/
Source: https://www.pokemon.com/us/pokemon-video-games/new-pokemon-snap

New Pokémon Snap explicitly frames the player's activity as an ecological survey. Professor Mirror and assistants operate from a research laboratory, expeditions repeatedly revisit habitats, observations are evaluated, and a Photodex accumulates selected records. The official material also distinguishes ordinary behavior from unusual behavior and gives the player tools that can influence what is observed.

Reusable structures:

- research can revisit the same site many times rather than treating one visit as final truth;
- observation conditions matter;
- a recorded observation can be selected into a long-lived research collection;
- evaluation is a later act distinct from capture of the original observation;
- a research team can contain assistants and field contributors rather than one omniscient professor;
- interventions used to elicit behavior should be recorded because they change observational context.

Ouros use:

Observation events remain the raw field facts. Scientific Research links selected observations into projects, methods and claims. A later interpretation can change without rewriting the original event.

Exclusion: photo scoring, stars, research levels, Illumina mechanics, characters, routes and plot are not imported.

## Official Pokémon source — research institutions can change leadership and research questions

Source: https://legends.pokemon.com/en-ca/story-world/characters/mable
Source: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Research_Lab

Public Pokémon material shows labs with different research specialties, assistants and leadership histories. Current official Legends: Z-A material describes Mable as acting director of a lab investigating a sudden increase in Pokémon in Lumiose City.

Reusable structures:

- a research institution can persist while leadership changes;
- a research question can emerge from a change in world state;
- institutional research may combine repeated registration/observation with a larger causal question;
- an acting director's tenure and the institution's scientific record are separate continuities.

Ouros use:

Research institutions should own project portfolios and records independent of one NPC. Civic Office or institution-tenure systems own leadership where relevant; Research owns only the scientific work.

Exclusion: no Lumiose plot, Mega Evolution reward loop or character-specific story is copied.

## PTU mechanics boundary — Researcher and Scientist are real mechanical surfaces

Source: https://pturpg.wikidot.com/classes
Source: https://pturpg.wikidot.com/104%3Ascientist
Source: https://anyflip.com/deia/psdg/basic/101-150

Public PTU references expose Researcher as a Trainer class and Scientist as a mechanically defined crafting-oriented class with specific prerequisites, costs and effects. Researcher fields also provide explicit Features rather than a generic permission to invent bonuses whenever a character performs research.

Reusable lesson:

Narrative scientific activity cannot silently grant Researcher Features, Scientist recipes, Skill Edges, Tutor effects, item creation, Pokémon creation or combat benefits.

Ouros use:

A research project can create knowledge, relationships, institutional state, assignments and story consequences. Mechanical progression or crafting remains a separate exact PTU/Caelo transaction.

## PTU community evidence — research is often used as a campaign spine

Source: https://www.reddit.com/r/pbp/comments/wncvub
Source: https://startplaying.games/adventure/cl8got8ov000y09l73ppe3mfd
Source: https://app.roll20.net/lfg/listing/425556/the-frozen-god

Public PTU campaign pitches repeatedly use professors, field data, sponsored expeditions and discoveries as adventure generators. One play-by-post pitch has an underfunded independent professor equipping Trainers to gather data and complete small research missions. Another campaign premise centers on mapping a safe route toward a major scientific discovery beneath a mountain.

Reusable structures:

- research assignments can generate modular jobs without every project becoming a world-ending mystery;
- funding, staffing and logistics can constrain what a lab can investigate;
- an expedition may produce maps, observations and uncertainty before producing a conclusion;
- discovering an anomaly and explaining it are separate arcs;
- a scientific discovery can create factional, civic, ecological or media consequences later.

Ouros use:

Research opportunities should arise from actual knowledge gaps or contradictory evidence, then create durable records even when the final hypothesis remains unresolved.

These campaign descriptions are community design evidence only. Their names, discoveries and plots are not imported.

## Research integrity source — data needs provenance and processing history

Source: https://www.nature.com/articles/s41597-024-04312-x

Published data-integrity guidance emphasizes completeness, metadata, versions, processing history, understandability and interpretability.

Reusable structure:

A result should retain links to the observations, samples, dataset version and analysis transform that produced it. A clean final chart must not erase the raw provenance chain.

Ouros use:

Store method versions, dataset versions and analysis episodes separately. If a later researcher reprocesses the same evidence differently, both analytical histories remain inspectable.

Exclusion: no real-world compliance standard becomes Ouros law.

## Scientific record source — correction and retraction are state changes, not time travel

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC9483880/
Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10475207/
Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12912830/

Research-integrity literature treats corrections, retractions and expressions of concern as changes to the public scientific record. Corrective information may propagate imperfectly and older conclusions can continue influencing later work.

Reusable structures:

- a published claim can later be corrected without deleting the historical fact that people read and relied on the earlier version;
- a retraction does not erase the source observations from history;
- a correction can affect only part of a study;
- downstream projects may need reassessment when one dependency changes;
- reasons for correction and the scope of affected conclusions should remain explicit rather than collapsing into `paper_bad=true`.

Ouros use:

Publications, corrections and retractions become linked records. Public Memory and Media can continue to hold outdated beliefs until new information actually reaches those actors.

Exclusion: no biomedical ethics regime, misconduct law or journal procedure is imported.

## Archives cross-check

Internal file reviewed: `design/archives-museums-collections-preservation-layer.md`.

Archives already owns physical preservation, cataloging, accession, specimen/record custody and research collections. It explicitly anticipates datasets, prior methods, replication attempts and revised hypotheses.

Therefore Scientific Research must reference preserved objects rather than duplicate them.

`SPECIMEN_PRESERVED != CLAIM_CONFIRMED`

`DATASET_ARCHIVED != ANALYSIS_VALIDATED`

`FIELD_NOTE_CATALOGUED != OBSERVATION_TRUE`

## Observation cross-check

Internal file reviewed: `design/observation-settlement-time-layer.md`.

Observation already owns raw observation events, knowledge records, field reports and research opportunities. Pass 163 extends that seam rather than replacing it.

`OBSERVATION_RECORDED != HYPOTHESIS_CONFIRMED`

`FIELD_REPORT_ACCEPTED != UNIVERSAL_SCIENTIFIC_CONSENSUS`

`RESEARCH_OPPORTUNITY != ANSWER_PREAUTHORED`

## PTU/Caelo cross-check

Internal project source priority reviewed through `research/2026-08-18-source-scan.md` and the current repository mechanical-source rules.

Relevant sources remain:

- PTU Core Rulebook;
- Pokédex material;
- Caelo Player's Guide;
- Caelo rulebook / errata;
- character-creation material;
- Caelo Region Location & Encounter List.

UNKNOWN until exact source and implementation review:

- universal scientific-research Skill Checks;
- generic hypothesis or experiment DCs;
- automatic research XP or Trainer XP;
- generic peer-review bonuses;
- Researcher/Scientist class benefits triggered by narrative project completion;
- universal specimen-collection mechanics;
- generic tranquilization, tagging or telemetry procedures;
- laboratory crafting outside exact Features/recipes;
- automatic species conclusions from Pokédex registration;
- Pokémon Type implying laboratory capability;
- Telepathy, Aura or Psychic effects proving truth;
- Moves or Abilities acting as generic sensors;
- automatic ownership of captured/recovered research subjects;
- any Caelo-specific publication, lab, grant or academic rule.

## Design conclusions

Scientific Research should preserve an argument and evidence lineage, not a single truth meter.

The minimum chain is:

`research question -> project -> method/protocol version -> observation/sample/dataset refs -> analysis episode -> interpretation/claim -> review state -> publication -> replication/correction history`

World truth remains elsewhere. Research records describe what investigators observed, processed and concluded at particular times.

A failed hypothesis can still be valuable history. A null result can close a question without creating a battle. A later replication can support one part of an old study while rejecting another. A correction should propagate through citations and public knowledge only when the relevant systems receive it.

## Copyright / transformation note

This pass extracts only high-level structures, workflows and design lessons. It does not copy protected dialogue, prose, distinctive characters, encounter scripts or plots from Pokémon, PTU campaigns or community material.