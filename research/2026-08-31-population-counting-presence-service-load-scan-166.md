# Population Counting, Presence & Settlement Demography Scan — Pass 166

Status: RESEARCH ONLY. NON-CANON.
Date: 2026-08-31

## Purpose

This pass examines how Ouros can remember population-scale facts without turning every visible NPC into an authoritative census record or duplicating existing human identity, household, residence, migration, settlement, employment or electoral systems.

The narrow gap is aggregate continuity: how many people a source says ordinarily live somewhere, how many were physically present during a bounded count, how temporary visitors or absences affect that number, how service demand can differ from resident population, and how revisions preserve provenance.

No source below establishes Ouros canon. Real-world statistical sources provide data-modeling lessons only. Pokémon sources provide franchise-facing narrative patterns only. External tabletop material is inspiration rather than PTU/Caelo rules authority.

## Repository inspection findings

The full repository tree was inspected before writing.

Relevant existing owners were then checked directly.

`design/observation-settlement-time-layer.md` already owns settlement capability, resident roles, regional clocks and causal settlement change. It says capability should come from concrete residents, facilities, supply links and world state. It does not define population-count methodology.

`design/residential-household-relocation-continuity-extension.md` already owns residence identity, resident links, household grouping, occupancy, displacement and relocation. It explicitly separates physical presence from residence and recommends coarse population-level presentation for neighborhoods.

`design/human-identity-name-record-continuity-extension.md` already owns human actor identity linkage, name records and scoped institutional identifiers. It explicitly refuses to create a universal civil registry, citizenship model or universal identifier.

Therefore Pass 166 must remain aggregate. It may consume residence and migration state where appropriate, but it must not become an identity registry or rewrite individual residence records.

## Source 1 — Pokémon settlement demographic snapshots

Bulbapedia documents population totals for many game settlements and often records different totals between game versions.

Examples reviewed:

- Celadon City has different listed populations across Red/Blue/Yellow, Gold/Silver/Crystal, FireRed/LeafGreen and HeartGold/SoulSilver.
- Lavender Town changes across versions, with the Tower-to-radio-station change cited alongside a population decline.
- Mistralton City changes between Black/White and Black 2/White 2; the page even notes one defeated School Kid returning to town and changing the displayed population by one.
- Wyndon is described with a single Sword/Shield population snapshot.
- Cocona Village has one count for the village and another when people on nearby Lapras Beach are included.
- Seafolk Village provides another small-settlement snapshot despite its unusual built environment.

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Celadon_City
- https://bulbapedia.bulbagarden.net/wiki/Lavender_Town
- https://bulbapedia.bulbagarden.net/wiki/Mistralton_City
- https://bulbapedia.bulbagarden.net/wiki/Wyndon
- https://bulbapedia.bulbagarden.net/wiki/Cocona_Village
- https://bulbapedia.bulbagarden.net/wiki/Seafolk_Village

Reusable lesson: a population number is meaningful only with a time/version and a scope. A figure can change because the represented world changed, because the counted area changed, or because the source's counting convention changed.

Ouros should never copy these numeric populations. Game-visible NPC totals are presentation artifacts, not a realistic demographic formula for Ouros.

## Source 2 — Presence and usual residence are different measures

The Australian Bureau of Statistics distinguishes population physically present from population based on usual residence. A person may be counted where they are on the reference night while ordinarily living elsewhere. Residents temporarily away and visitors temporarily present can therefore affect different population measures in different ways.

Sources:

- https://www.abs.gov.au/articles/population-physically-present-australia
- https://www.abs.gov.au/statistics/detailed-methodology-information/information-papers/comparing-place-enumeration-place-usual-residence

Reusable lesson: Ouros needs separate dimensions for `usual_resident_population` and `present_population_snapshot` whenever both matter. A festival town, port, resort, academy district, pilgrimage site or tournament host can have a temporary population far above its normal residential base.

## Source 3 — UN population and housing census principles

The United Nations Principles and Recommendations for Population and Housing Censuses distinguishes people usually resident and present, usually resident but temporarily absent, and not usually resident but temporarily present. It also stresses careful allocation to avoid double counting.

Source:

- https://unstats.un.org/unsd/demographic-social/Standards-and-Methods/files/Principles_and_Recommendations/Population-and-Housing-Censuses/Series_M67rev3-E.pdf

Reusable lesson: a count procedure needs an explicit inclusion rule. Two competent counts can disagree because they answer different questions rather than because one is wrong.

No UN legal or administrative rules are imported into Ouros.

## Source 4 — Population measurement can be revised between full counts

Australian population statistics distinguish census counts from estimated resident population and update estimates using demographic components between censuses.

Source:

- https://population.gov.au/population-topics/topic-population-measurement

Reusable lesson: Ouros can preserve a `COUNTED`, `ESTIMATED`, `PROJECTED` or `REVISED` provenance class rather than presenting every settlement number with equal epistemic authority.

The simulation must not invent demographic arithmetic merely because the real world uses births, deaths and migration components. Exact estimation methods remain authored per institution or setting.

## Source 5 — Population and service demand can diverge

ABS material distinguishes resident, present and service-population concepts. People may travel into an area to use health, food, accommodation, work or other services without becoming residents.

This is especially useful for Ouros because settlement systems already model facilities and capacity.

Reusable lesson: a clinic queue, market crowd, Gym event or ferry terminal can be under pressure without implying permanent population growth.

`SERVICE_LOAD != RESIDENT_POPULATION_CHANGE`.

## PTU/Caelo cross-check

The project README establishes the source priority for mechanical claims: PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List, plus live AutoPTU implementation.

The inspected Narrative material does not establish a PTU/Caelo population-count mechanic, universal census Skill Check, citizenship system, residency entitlement, population-derived Trainer reward, or battle modifier based on settlement population.

Pass 166 therefore treats demographic state as narrative/administrative world state only.

UNKNOWN until exact project authority says otherwise:

- any Caelo-authored census institution;
- any universal civil registration system;
- any Skill Check used to conduct or validate an enumeration;
- any Trainer Feature that changes population records;
- any mechanical bonus tied to town size, crowd size or resident count;
- any rule treating visible Minecraft NPCs as a canonical population total.

## Wild Pokémon boundary

Human/settlement demography must remain separate from wild-population ecology.

Wild Collective and scientific research layers already own abundance, persistent wild groups, observation and ecological evidence.

A settlement census cannot silently count wild Pokémon as residents. A wildlife survey cannot silently define civic population.

Domesticated, partnered, institutional or co-resident Pokémon may be represented by separate authored aggregate dimensions if Ouros canon later needs them, but no default equivalence is created here.

## Core transferable patterns

A useful demographic record should preserve:

- the measured concept;
- geographic scope;
- reference time;
- inclusion/exclusion rule;
- collection or estimation method;
- source institution;
- uncertainty or coverage state;
- revision lineage.

The narrative engine should prefer ranges or coarse bands when precision is unsupported.

A number should not become more precise merely because Minecraft currently renders a finite number of NPC entities.

## Anti-duplication rules

Population counting may reference individual resident links, but it does not own them.

Population counting may reference relocation events, but it does not cause them.

Population counting may inform settlement-capacity planning, but it does not create facilities or resources.

Population counting may inform an electoral denominator only when the Electoral layer supplies an authored electorate rule. Resident population and electorate are never assumed equal.

Population counting may inform public reporting, but Media/Broadcast own publication and transmission.

Population counting may become historical evidence, but Archives/Public Memory own preservation and later interpretation.

## Design conclusion

The high-value addition is not a universal census bureaucracy. It is a provenance-aware aggregate layer that lets Ouros remember that a town had 900 usual residents in one estimate, 1,350 people physically present during a festival, a clinic serving a much wider surrounding catchment, and a later revised historical series without forcing any of those figures to overwrite the others.

That continuity creates useful story pressure while remaining compatible with the existing settlement, housing, identity and migration architecture.