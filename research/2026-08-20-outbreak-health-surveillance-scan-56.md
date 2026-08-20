# Outbreak, Health Surveillance & Epidemiology Research — Pass 56

Status: RESEARCH ONLY. Not Ouros canon. External sources are inspiration/evidence sources, not PTU rules authority.

Date: 2026-08-20

## Why this pass exists

The repository already models individual care, facility capacity, crises, environmental contamination, wildlife ecology, research programmes, information flow and public memory. It did not yet have a dedicated layer for detecting unusual clusters across those systems, defining a surveillance case, tracing plausible exposure networks, revising hypotheses, coordinating clinics/researchers/conservation actors, or deciding when a health event has ended.

The design gap matters because otherwise a narrative generator can make several unsafe inferences:

- several sick Pokémon nearby => one contagious disease;
- Poisoned => infectious illness;
- an unusual Pokémon behavior => diagnosis;
- one positive test => all similar cases have the same cause;
- one exposed actor => infected;
- quarantine => guilt, danger or confirmed infection;
- absence of reports => absence of disease;
- a visible environmental contaminant => proven causal agent;
- a Pokémon Center visit => mechanical cure;
- Pokérus => generic template for every illness.

Pass 56 treats those as separate claims.

## Public Pokémon sources inspected

### Pokémon Horizons — The Pokémon Center Lady

Source: https://www.pokemon.com/us/animation/horizons/3/the-pokemon-center-lady

Useful structure:

- multiple wild Pokémon fall ill along the same hiking trail;
- a care provider observes a local pattern before the cause is known;
- an apparently aggressive Pokémon may itself be affected by the same underlying disturbance;
- clinical response and environmental investigation can occur in the same story.

Reusable Ouros lesson:

A clinic or ranger station can become an early-warning sensor because it sees repeated cases from the same geography. The shared location is evidence for investigation, not proof of a single diagnosis.

No episode dialogue, character arc or distinctive plot is imported.

### Pokémon — Hypno's Naptime

Source: https://www.pokemon.com/us/animation/seasons/1/episode-26-hypnos-naptime

Useful structure:

- a town experiences two apparently different problems at the same time;
- a Pokémon Center notices poor recovery while another institution investigates missing people;
- a recurring environmental/psychic phenomenon becomes a candidate common cause.

Reusable Ouros lesson:

Health surveillance should be able to join weak signals held by different institutions without converting correlation into truth.

### Pokérus reference

Source: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9Rus

High-level factual lesson only:

Pokérus is represented as a transmissible virus-like phenomenon with its own persistence/spread behavior in multiple game generations. It is not simply a normal battle Status Condition and its implementation varies by generation.

Reusable Ouros lesson:

Do not model every disease as Poisoned, Burned, Confused or another combat status. A persistent health phenomenon may require world-state separate from battle status.

Important restriction:

This source is not authority for PTU/Caelo mechanics. No EV bonus, spread probability, strain timer or storage behavior is imported into Ouros unless the governing PTU/Caelo material explicitly supports it.

## Fangame/community sources inspected

### Pokémon Containment Breach — Eevee Expo

Source: https://www.eeveeexpo.com/threads/8701/

The project uses an outbreak/containment premise and connects laboratory failure, regional disruption, scarce resources and changed Pokémon behavior.

Reusable high-level structure:

- containment failure can create cascading effects across travel, care, supply and public information;
- response gameplay can include investigation, resource allocation, evacuation and institutional failure rather than only battles.

Copyright boundary:

Do not copy its virus, mutations, zombie premise, factions, characters, plot progression or original forms. Ouros should use only the general structural lesson that a health event can become a multi-system regional arc.

## Real-world structural research used only as design methodology

### WHO One Health

Sources:

- https://www.who.int/news-room/fact-sheets/detail/one-health
- https://www.who.int/health-topics/one-health

Current WHO material describes health of humans, animals and ecosystems as interlinked and emphasizes coordinated surveillance, communication and response across those domains.

Reusable Ouros lesson:

A Pokémon-region health problem should be able to connect clinics, wild-population monitoring, water/soil observations, transport, food systems and environmental change without declaring in advance which domain contains the cause.

### WHO outbreak investigation stages

Source: https://www.who.int/emergencies/outbreak-toolkit/standardized-data-collection-tools/investigating-outbreak-of-unknown-disease

Useful structure:

- determine whether observations exceed a normal baseline;
- verify diagnosis instead of assuming it;
- introduce proportionate control measures while investigation continues;
- revise the response when evidence changes.

Reusable Ouros lesson:

The first gameplay objective can be establishing whether there is actually an unusual cluster. The story does not need to begin with a known pathogen.

### CDC surveillance case definitions

Source: https://www.cdc.gov/urdo/php/surveillance/outbreak-case-definitions.html

Useful structure:

A surveillance case definition creates consistent inclusion criteria for investigation. It is not identical to an individual clinical diagnosis.

Reusable Ouros lesson:

Ouros can maintain an `outbreak_case_definition` that groups comparable observations while preserving each individual patient's actual diagnosis as a separate object.

### WOAH wildlife health surveillance

Sources:

- https://www.woah.org/en/what-we-do/animal-health-and-welfare/wildlife-health/
- https://www.woah.org/en/woah-launches-wildlife-health-strategy-2026-2030-to-strengthen-prevention-surveillance-systems-and-rapid-response-capacities/

Useful structure:

Wild populations are harder to monitor than managed populations, and early signals can come from researchers, conservation groups and field observers rather than only clinics.

Reusable Ouros lesson:

Wild-Pokémon health surveillance should represent observation gaps. No report from a remote route cannot be treated as a clean bill of health.

## Existing project material cross-checked

The internal repository already has:

- `design/care-recovery-welfare-layer.md` for individual care and facility capacity;
- `design/crisis-rescue-recovery-layer.md` for crisis lifecycle and recovery;
- `design/science-research-discovery-layer.md` for hypotheses, datasets and replication;
- `design/conservation-protected-areas-stewardship-layer.md` for wildlife stewardship;
- `design/interspecies-ecological-relations-layer.md` for population relationships;
- `design/waste-sanitation-recycling-pollution-layer.md` for pollution and waste pathways;
- `design/media-communications-information-layer.md` for publication/delivery;
- `design/meteorology-forecasting-weather-layer.md` for environmental observations and forecasts.

Pass 56 should reference those objects rather than duplicate them.

The persistent File Library research catalogue also contains quarantine/injury-recovery story engines, but it treats them as narrative seeds and explicitly requires server-side validation rather than establishing new rules. This pass keeps the same authority boundary.

## PTU/Caelo mechanical boundary

A complete searchable PTU/Caelo source corpus was not reliably retrievable in this run. No disease, quarantine, Medicine Education, Pokérus, infection, immunity or recovery rule is therefore declared as PTU/Caelo canon here.

Available project evidence does show that Python AutoPTU contains explicit battle statuses and hazards such as Poison/Toxic Spikes. Those are tactical mechanics. They do not establish a general disease model.

Repository search across current AutoPTU-Java and AutoPTU found no direct implementation under `Pokerus`, `Pokérus`, `illness`, `disease`, `infection`, `quarantine` or `contagion` terms. Absence of a search hit is not proof that no related mechanic exists under another name, but it is enough to prohibit narrative code from assuming such a subsystem.

## Reusable narrative structures

### 1. Baseline before outbreak

A cluster becomes meaningful only relative to an expected baseline.

Sources for baseline can include:

- clinic visit history;
- ranger observations;
- wildlife-monitoring routes;
- research datasets;
- seasonal phenology;
- sanitation/water records;
- player Chronicle observations.

A region with no baseline may know only that several similar events occurred, not that they are statistically unusual.

### 2. Surveillance case definition

A temporary investigation definition can group observations by:

- species/population;
- place;
- time window;
- observed signs;
- shared exposure candidate;
- minimum evidence quality.

This definition may change as evidence improves. Version history should persist.

### 3. Clinical case vs surveillance case

An individual care case can receive a diagnosis that later excludes it from the outbreak investigation.

The surveillance system therefore references care cases; it does not replace them.

### 4. Exposure graph

Possible exposure edges may include:

- shared water source;
- common transport;
- same nursery/clinic/shelter;
- shared habitat;
- feeding site;
- market or event;
- direct contact when actually observed;
- environmental location;
- item/material batch.

An exposure edge means opportunity, not transmission.

### 5. Multiple-cause cluster

Several similar cases may have different causes.

This should be a supported outcome, not a failed mystery.

### 6. Sentinel observations

A clinic, researcher, caretaker, wild collective, transport operator or player may detect a change earlier than a central institution.

The information must still travel through existing communication systems.

### 7. Proportionate control

Possible world-state responses may include:

- targeted route notice;
- temporary visitor limit;
- pause on transfers;
- separate waiting area;
- equipment cleaning workflow;
- field sampling;
- adjusted staffing;
- temporary closure;
- voluntary avoidance recommendation;
- targeted wildlife observation.

No measure is automatically legal or canonical. Authority must come from authored institutions.

### 8. False alarm and useful negative result

The system should reward a well-run investigation that concludes there is no outbreak, or that the apparent cluster came from unrelated causes.

### 9. Recovery and after-action review

Ending an outbreak does not erase:

- affected care records;
- public fear;
- business/service disruption;
- missed school/work;
- wildlife displacement;
- changed clinic capacity;
- research datasets;
- policy revisions;
- misinformation that remains in circulation.

Those consequences should become inputs for later content.

## Strong no-inference rules

- `Poisoned` is not infectious disease.
- `Badly Poisoned` is not epidemic severity.
- `Fainted` is not illness.
- Injury is not infection.
- visible symptoms are not diagnosis.
- exposure is not infection.
- infection is not guilt.
- quarantine/isolation is not punishment.
- one case is not automatically an outbreak.
- several cases are not automatically one outbreak.
- a clinic diagnosis is not automatically public information.
- wild Pokémon leaving an area is not proof of disease.
- an aggressive Pokémon is not proof of sickness.
- a positive environmental sample does not prove every nearby patient has the same cause.
- no report from an unloaded/remote area is not evidence of zero cases.

## Copyright transformation rule

External stories contribute only structural lessons such as multi-system response, environmental investigation, uncertainty, containment and institutional coordination. No distinctive outbreak premise, pathogen, mutation, character, dialogue, sequence of revelations or source-specific resolution should be transferred into Ouros.

## Best next use

Build an implementation-facing world-state layer where care records, field observations and environmental evidence can be linked into a versioned outbreak investigation without allowing the narrative generator to invent mechanical diseases or tactical statuses.