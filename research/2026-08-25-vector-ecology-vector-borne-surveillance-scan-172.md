# Vector Ecology & Vector-Borne Surveillance Scan — Pass 172

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. No mechanical rule in this note overrides PTU/Caelo or AutoPTU.
Date: 2026-08-25

## Why this pass exists

Repository-wide comparison was inspected before writing. Ouros already has authoritative or proposed layers for outbreak/health surveillance, biosecurity, community science, toxicology, diel activity, seasonal ecology, water, urban wildlife, research ethics, metrology, timekeeping and telemetry. No dedicated vector-ecology or vector-surveillance layer/protocol was present.

The clean gap is narrower than “disease simulation.” It is the evidence chain between vector ecology and an outbreak hypothesis:

`surveillance design -> trap/search effort -> vector observation -> pooled or individual sample -> pathogen test -> host-contact evidence -> transmission hypothesis -> health/outbreak handoff -> intervention review -> follow-up`

Pass 56 remains authoritative for outbreak/health truth. Pass 61 remains authoritative for biosecurity and introduced-population questions. Pass 166 remains authoritative for public/community submissions. Pass 172 should own only vector-surveillance provenance and vector-specific ecological evidence.

## Existing Ouros boundaries inspected

### Outbreak & health surveillance — Pass 56

`design/outbreak-health-surveillance-layer.md` already separates individual events, observations, diagnoses, case definitions, exposure opportunities, hypotheses, control measures and PTU statuses. It explicitly states that an `EXPOSURE_EVENT` is not a transmission event.

Pass 172 therefore must not create a second outbreak system. Its outputs should be evidence references that Pass 56 may consume.

### Biosecurity — Pass 61

`design/biosecurity-introduced-species-translocation-layer.md` owns origin, arrival pathway, establishment, spread and impact for introduced populations. A newly detected vector population may create a Biosecurity handoff, but vector status alone does not prove introduction, disease transmission or ecological harm.

### Community science — Pass 166

`design/community-science-participatory-monitoring-protocol.md` owns public observation effort, source dependence, validation and sensitive-location presentation. Public bite reports, photos or trap checks can feed a vector program only through that provenance chain.

## Public-health surveillance lessons worth adapting

### 1. Trap type changes what can be observed

CDC’s mosquito-surveillance toolkit describes multiple trap designs aimed at different species and life stages, including egg, larval, adult, host-seeking and gravid females. A collection method is therefore part of the observation, not invisible plumbing.

Ouros design lesson:

- trap/survey method must be stored with each deployment;
- comparing two seasons requires checking whether method, attractant, placement, timing and target stage remained comparable;
- a trap catching few individuals does not directly mean the local population is small.

Source:
- CDC, “Mosquito Surveillance Traps,” 14 May 2024: https://www.cdc.gov/mosquitoes/php/toolkit/mosquito-surveillance-traps.html

### 2. A positive pool is not an individually resolved infection record

CDC’s mosquito-surveillance software treats positive mosquito pools as a basic surveillance product and explains that infection-rate estimates from pooled samples depend on pool sizes, sample sizes and model assumptions. The traditional minimum infection rate assumes only one infected mosquito in each positive pool and can underestimate infection rate.

Ouros design lesson:

`positive pooled sample != every specimen positive`

and also:

`positive pooled sample != host exposure != host infection != illness`

A pool should preserve which collection/deployment supplied it, its composition if known, the laboratory method, result revision and uncertainty.

Sources:
- CDC, “Mosquito Surveillance Software,” 28 May 2024: https://www.cdc.gov/mosquitoes/php/toolkit/mosquito-surveillance-software.html
- CDC, “Guidelines for West Nile Virus Surveillance and Control”: https://www.cdc.gov/west-nile-virus/php/surveillance-and-control-guidelines/index.html

### 3. No record is not absence

CDC’s 2026 tick-surveillance datasets explicitly warn that a county with no records should not be interpreted as tick absence because the cause may be missing sampling, collections or reporting. Their surveillance also separates vector establishment from pathogen detections in those vectors.

Ouros design lesson:

A vector-surveillance programme needs explicit effort and coverage. Valid states include:

- `NOT_DETECTED_WITH_DOCUMENTED_EFFORT`
- `NO_SURVEY_COVERAGE`
- `SAMPLING_INCOMPLETE`
- `DETECTED`
- `ESTABLISHMENT_UNRESOLVED`

The second and third states must never be collapsed into absence.

Sources:
- CDC, “Tick Surveillance Data Sets,” 14 May 2026: https://www.cdc.gov/ticks/data-research/facts-stats/tick-surveillance-data-sets.html
- CDC, “Tickborne Pathogen Surveillance,” 29 April 2026: https://www.cdc.gov/ticks/data-research/facts-stats/tickborne-pathogen-surveillance-1.html

### 4. Vector abundance and pathogen activity are different signals

CDC notes that high mosquito abundance can occur without virus and that lower abundance can coexist with higher infection rates. It recommends representative spatial/temporal trapping and richer indices instead of treating raw trap counts or positive-pool counts as self-explanatory.

Ouros design lesson:

Store separate revisions for:

- vector detections / catch index;
- pathogen detections;
- host-contact observations;
- health cases;
- final outbreak hypotheses.

Do not let any one of these overwrite the others.

Source:
- CDC, “West Nile Virus Surveillance and Control Guidelines”: https://www.cdc.gov/mosquitoes/media/pdfs/2024/09/WestNileVirus-SurveillanceControlGuidelines_508.pdf

### 5. Surveillance systems can be provisional and multi-source

CDC’s ArboNET combines human, veterinary, mosquito, bird and sentinel-animal information, while warning that provisional data can change before finalization and that passive surveillance can undercount disease.

Ouros design lesson:

A regional vector-borne dashboard should retain dataset vintage and source class rather than showing one omniscient live number.

Source:
- CDC, “ArboNET,” 24 March 2026: https://www.cdc.gov/vector-borne-diseases/php/arbonet/index.html

### 6. Intervention should be evidence-led and cross-sectoral

WHO’s integrated vector management framework treats vector control as a decision process informed by local vector biology, epidemiology, monitoring and multiple sectors. It specifically emphasizes surveillance, evaluation and combinations of interventions rather than a single universal response.

Ouros design lesson:

Vector surveillance should propose handoffs, not automatically execute control. Any environmental modification, pesticide-like intervention, access closure, relocation, water-management change or public-health measure belongs to the relevant authority layer and must remain reviewable.

Sources:
- WHO, “Integrated vector management (IVM),” 4 February 2022: https://www.who.int/europe/news-room/fact-sheets/item/integrated-vector-management-%28ivm%29
- WHO, “Global vector control response 2017–2030”: https://www.who.int/publications/i/item/9789241512978
- WHO, “Vector surveillance and control at points of entry and onboard conveyances,” 8 September 2025: https://www.who.int/publications/i/item/B09510

## Pokémon material and guardrails

### Golbat — feeding contact without invented transmission

The official Pokédex describes Golbat biting sleeping prey and drinking blood. This supports authored predator/feeding-contact observations.

It does not support any universal claim that Golbat transmits infection. Blood-feeding is a behavioral fact for the relevant source entry; vector competence is a separate scientific question that Ouros must establish, if ever, through canon and evidence.

Source:
- Pokémon, Golbat Pokédex: https://www.pokemon.com/us/pokedex/golbat

### Venonat — insect ecology without “Bug-type = vector”

The official Pokédex describes Venonat as nocturnally catching small Bug Pokémon attracted to light, while poison can ooze from its body. This is useful for night-light ecology and food-web observations.

It does not make Venonat a disease vector, nor does Poison typing convert environmental contact into PTU Poisoned.

Source:
- Pokémon, Venonat Pokédex: https://www.pokemon.com/us/pokedex/venonat

### Zubat — sensory/roost behavior is not disease surveillance

The official Pokédex describes cave roosting and ultrasonic navigation. This can interact with Diel Activity, Cave Ecology and Passive Acoustic Monitoring, but those facts do not create pathogen detection or vector status.

Source:
- Pokémon, Zubat Pokédex: https://www.pokemon.com/us/pokedex/zubat

## PTU/community and fangame structures

### A PTU campaign premise: “remove ailments” as an institutional temptation

A public PTU campaign listing describes a scientifically focused region where an organization seeks to remove ailments from humans and Pokémon and where experiments have produced abnormal outcomes.

Reusable structure for Ouros:

`legitimate health goal -> institutional confidence -> incomplete evidence / unintended effects -> need for independent review`

Do not copy the organization, experiments or plot. More importantly, do not make every vector programme secretly villainous. This is useful as an anti-pattern and as a reminder that “cure everything” institutions need governance and evidence boundaries.

Source:
- Reddit / r/lfg, PTU campaign listing, 8 December 2024: https://www.reddit.com/r/lfg/comments/1h9hi3n

### Pokémon Plague Heart — anti-pattern against type-based persecution

The completed 2025 fangame Pokémon Plague Heart uses a political conflict in which Poison-type Pokémon are criminalized by one side and elevated by another. The useful high-level lesson is not its civil-war plot; it is the danger of converting type identity into presumed public-health risk.

Ouros guardrail:

`Poison-type != contamination source != infection source != vector competence != guilt`

Source:
- Eevee Expo, “Pokemon Plague Heart,” 30 August 2025: https://eeveeexpo.com/threads/9060/

## PTU/Caelo cross-check

The accessible project AutoPTU corpus exposes `MedicineEducation`, `PokemonEducation`, `Survival`, `Perception` and other PTU skills as actual rules data. That confirms these are real mechanical concepts, but it does not provide a vector-surveillance subsystem or authorize invented DCs for trapping, pathogen testing or epidemiological inference.

Project source inspected:
- `Teffa14/AutoPTU/PTUDatabase-main/PTUDatabase/Classes/Skills.cs`

The project search in this run did not recover a reliable primary Caelo passage defining mosquitoes, ticks, vector competence, pooled testing, infection surveillance or vector-control mechanics. No Caelo rule is inferred from general memory.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No output is attributed to it.

## Proposed Ouros design principles from the scan

1. “Vector” is a relationship in a transmission model, not a species tag to apply casually.
2. The surveillance method is part of the evidence.
3. Trap count, population abundance, pathogen positivity and disease risk are separate products.
4. Positive pooled tests preserve group uncertainty.
5. Host contact remains separate from infection.
6. Exposure remains separate from illness.
7. No detections require effort/coverage context.
8. Intervention authority remains outside the surveillance protocol.
9. Public reports can contribute through Community Science but do not bypass validation.
10. Minecraft entities, particle effects, bites, despawns or trap props never write surveillance truth.

## Canon posture

No vector species, pathogen, endemic disease, institution, intervention, transmission cycle or outbreak is established by Pass 172.

All narrative candidates derived from this research must remain `NON-CANON / PROPOSED` until explicitly accepted.