# Biosecurity, Introduced Species & Translocation Research Scan — Pass 61

Status: RESEARCH ONLY. Not Ouros canon. Not a rules source.

Date: 2026-08-20

## Research question

How can Ouros represent newly arrived Pokémon populations, deliberate introductions, accidental escapes, translocations, hitchhikers, establishment, ecological impact and management response without collapsing all unfamiliar species into a single "invasive" label?

This pass extends the existing conservation/stewardship layer. That layer already states that newly observed species are not automatically invasive. Pass 61 adds the missing persistent evidence and movement chain between arrival and any later management decision.

## Existing Ouros material checked before research

Relevant internal systems already cover:

- conservation designations, habitat stewardship and management review;
- wild populations and persistent collectives;
- interspecies ecological relationships;
- travel, shipping, ports and interregional mobility;
- breeding, nurseries and Pokémon custody;
- illicit networks and diverted shipments;
- science, samples and evidence;
- health surveillance and quarantine-like health questions;
- media, rumors and public memory;
- cases, allegations and chain of custody;
- demography and migration for humans;
- Pokémon agency, release and persistent identity.

The gap is ecological provenance for a population: how a species arrived, whether it established, what evidence links it to a pathway, what impacts are observed and what intervention—if any—is justified.

## Source 1 — Official Corphish Pokédex

Source:
https://www.pokemon.com/us/pokedex/corphish

Relevant high-level facts:

- Corphish is described as coming from overseas.
- It is described as hardy and able to proliferate rapidly.
- It can persist in polluted water where it faces less competition for food.

Reusable design lessons:

1. A Pokémon can have explicit non-local provenance.
2. Successful establishment can depend on environmental conditions.
3. Pollution or infrastructure change can create opportunity for a newly arrived population.
4. Population growth is different from demonstrated ecological harm.
5. The arrival pathway and later expansion should be separate records.

Ouros transformation:

Do not copy a Corphish invasion event into Ouros. Use the structure: arrival record -> establishment evidence -> spread observations -> environmental drivers -> impact study -> management review.

## Source 2 — Official Copperajah Pokédex

Source:
https://www.pokemon.com/us/pokedex/copperajah

Relevant high-level fact:

Copperajah is described as having been brought to Paldea long ago by people from a distant land.

Reusable design lesson:

Introduced does not equal harmful.

A population can be human-introduced, long-established and socially/ecologically integrated without requiring an eradication storyline.

Ouros transformation:

Maintain a distinct `INTRODUCED_ESTABLISHED` provenance state and require separate evidence for negative ecological impact.

## Source 3 — Official Rattata Pokédex

Source:
https://www.pokemon.com/us/pokedex/rattata

Relevant high-level facts:

Rattata is described as abundant and strongly food-seeking.

Reusable design lesson:

Abundance alone is not proof of non-native status, causation or management need.

Ouros should never infer introduction merely because a species becomes numerous near settlements, farms or waste streams.

## Source 4 — Official Yungoos Pokédex

Source:
https://www.pokemon.com/us/pokedex/yungoos

Relevant high-level facts:

Yungoos has persistent food-search behavior and repeated daily routes.

Reusable design lesson:

Observed route use and foraging pressure can become measurable world state without assuming why the population is present.

This is useful for monitoring introduced or range-expanding species, but behavior does not prove provenance.

## Source 5 — Pokémon Tabletop community: Social Ecology of Kanto

Sources:
https://startplaying.games/adventure/clnt20u4d000208ma3ty01n49
https://startplaying.games/adventure/cm9ydhbid00412xulbu7lzufh

Relevant high-level structure:

The public campaign description explicitly treats the relationship between society and nature as a core theme while retaining normal PTU travel, battles, badges and character arcs.

Reusable design lesson:

Ecological questions work best when linked to institutions, economic activity, factions and character choices rather than isolated "nature quests".

Ouros transformation:

A biosecurity arc should connect ports, nurseries, traders, scientists, conservation staff, farmers, residents and transport systems as appropriate. It should not create a generic Ranger extermination quest.

## Source 6 — Pokécharms public underwater RP discussion

Source:
https://forums.pokecharms.com/threads/underwater-a-pokemon-scuba-diving-rp.13479/

Relevant high-level design interest:

The public RP proposal explicitly identifies invasive species, keystone species, endangered species and ecosystem research as useful material for a Pokémon ocean setting.

Reusable design lesson:

Players can engage with ecological relationships through observation, diving, research, restoration and community response without requiring every ecology story to be combat-driven.

No characters or prose from the RP are copied.

## Source 7 — Network-scale ecological invasion research

Source:
https://arxiv.org/abs/1803.03475

Relevant high-level finding:

Modeling ecological introductions across a food web can produce indirect and counter-intuitive effects beyond the immediately competing species.

Reusable design lesson:

Ouros should not calculate impact from a single pairwise relationship only.

A new population can affect:

- prey availability;
- competitor behavior;
- scavengers;
- predators;
- resource use;
- habitat pressure;
- human services;
- tourism;
- conservation priorities.

The game does not need a full ecological simulator. It needs a causal graph and evidence-driven state changes.

## Source 8 — Public fan story discovery example

Source:
https://www.royalroad.com/fiction/66812/a-region-not-my-own-a-pokemon-story/chapter/1379721/chapter-30-interlude-02-hana

Use restrictions:

Do not copy prose, characters, scenario details or plot.

Reusable high-level pattern only:

A public-news report can announce sightings of unfamiliar Pokémon before researchers know the complete cause, and the resulting public response can itself change behavior and pressure on the ecosystem.

Ouros transformation:

Media publication should be downstream of observation and upstream of visitor/capture pressure. It must not convert an unverified sighting into world truth.

## Core design conclusions

### A. Distinguish arrival from impact

Use a staged evidence model:

```text
new observation
-> provenance hypothesis
-> arrival pathway evidence
-> establishment evidence
-> spread evidence
-> impact hypothesis
-> impact evidence
-> management review
-> action, monitoring or no action
```

Skipping stages creates bad stories and poor simulation.

### B. Use multiple provenance states

Candidate descriptive states:

- NATIVE_ORIGIN_CONFIRMED
- LONG_ESTABLISHED_ORIGIN_UNRESOLVED
- NATURAL_RANGE_EXPANSION_SUSPECTED
- NATURAL_RANGE_EXPANSION_SUPPORTED
- HUMAN_INTRODUCTION_SUSPECTED
- HUMAN_INTRODUCTION_CONFIRMED
- CAPTIVE_ESCAPE_SUSPECTED
- CAPTIVE_ESCAPE_CONFIRMED
- RELEASE_EVENT_CONFIRMED
- HITCHHIKER_PATHWAY_SUSPECTED
- TRANSLOCATION_AUTHORIZED
- TRANSLOCATION_UNAUTHORIZED
- ORIGIN_UNKNOWN

These are ecological provenance states, not moral labels.

### C. Establishment is separate

Candidate population states:

- SINGLE_OBSERVATION
- REPEATED_OBSERVATION
- TEMPORARY_PRESENCE
- REPRODUCTION_UNCONFIRMED
- REPRODUCTION_CONFIRMED
- SELF_SUSTAINING_POPULATION_SUPPORTED
- LOCAL_EXPANSION_SUPPORTED
- REGIONAL_SPREAD_SUPPORTED

No exact thresholds should be invented until authored for the region or supplied by a simulation layer.

### D. Impact requires evidence

Candidate impact dimensions:

- competition pressure;
- predation pressure;
- habitat modification;
- food-web effects;
- nesting displacement;
- infrastructure interaction;
- crop or stored-food interaction;
- disease/exposure association;
- human–Pokémon conflict;
- beneficial service or mutualism;
- unknown/neutral effect.

A species can have mixed effects.

### E. Management has alternatives

Possible responses include:

- continue monitoring;
- improve identification/provenance evidence;
- close an arrival pathway;
- change shipping or nursery practices;
- remove attractants;
- habitat restoration;
- targeted relocation when justified;
- containment of a small confirmed escape;
- public education;
- temporary access management;
- no intervention;
- formal acceptance of a long-established population.

The system must not default to capture, removal or extermination.

### F. Public pressure can create a second problem

An unfamiliar or rare Pokémon can attract:

- collectors;
- tourists;
- researchers;
- media;
- poachers;
- conservation attention;
- businesses;
- misinformation.

A management problem can therefore come from people reacting to the species rather than from the species itself.

## PTU/Caelo boundary

The project-supplied PTU/Caelo corpus was not reliably retrievable in this automation runtime.

Existing internal Ouros documents already preserve several relevant principles from prior source checks:

- wild encounters remain PTU mechanical encounters;
- capture legality and capture mechanics are separate from narrative policy;
- species capabilities and behavior must be validated rather than invented;
- conservation policy does not rewrite battle legality;
- relocation and release do not imply ownership changes;
- Fainted/Injury states must not be interpreted as death.

Pass 61 adds no new PTU/Caelo mechanics.

Do not invent:

- capture bonuses for introduced species;
- mandatory removal rules;
- population damage from one battle;
- ecological damage from a Move unless the rules/world layer explicitly records it;
- relocation checks;
- quarantine mechanics;
- tracking bonuses;
- habitat-control Abilities;
- encounter scaling based on introduction status.

## Copyright/provenance rule

External sources are used for factual reference and abstract structural inspiration only.

Do not copy:

- distinctive plots;
- dialogue;
- original fan characters;
- long prose passages;
- source-specific factions;
- source-specific locations into Ouros.

Preserve URLs in research notes. Transform all scenario material into original Ouros concepts.

## Pass 61 design opportunity

The strongest reusable structure is a persistent `BIOSECURITY_CASE` that can begin with a single observation and remain unresolved for months of world time.

It should connect:

- science;
- conservation;
- ports/transport;
- nurseries/custody;
- settlements;
- media;
- tourism;
- interspecies ecology;
- cases when wrongdoing is alleged;
- illicit networks only when evidence supports them.

That object should never itself decide combat mechanics.