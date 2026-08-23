# Research Scan — Emergency Services, Dispatch & Incident Coordination — Pass 121

Status: research/provenance only. Not Ouros canon. External stories are inspiration sources, not rules sources.

## Why this pass

The repository already models crises, rescue, infrastructure, communications, workplaces, health, transport and recovery. What was still missing was the operational layer between a report and a coordinated response: call intake, triage, dispatch, staging, unit status, transfer of responsibility, mutual aid, demobilization and after-action learning.

This pass therefore treats emergency response as an institutional coordination problem rather than as a synonym for the hazard itself.

## Sources and reusable structures

### Pokémon — The Pokémon Water War
Source: https://www.pokemon.com/us/animation/seasons/2/episode-50-the-pokemon-water-war

The episode presents a trained local Wartortle fire brigade that arrives after an initial attempt to control a fire fails. A second fire becomes more dangerous when that specialized team is unavailable.

Reusable structure:
- trained response teams can be persistent institutions;
- capability depends on actual availability, not merely on institutional existence;
- removing one specialized unit can create a coverage gap without changing the hazard itself;
- Pokémon can participate institutionally without being treated as equipment.

Do not import episode plot, characters, exact team composition or any invented firefighting mechanics.

### Pokémon — The Fire-ing Squad!
Source: https://www.pokemon.com/us/animation/seasons/3/episode-31-the-fire-ing-squad

A firefighting competition emphasizes trained team coordination and leadership as distinct from raw Pokémon power.

Reusable structure:
- drills and competitions can expose coordination weaknesses before a real incident;
- readiness has a training/history dimension;
- team leadership is an institutional role, not automatically a Trainer Feature or combat bonus.

### Pokémon — A Squad Worth of Passion!
Source: https://www.pokemon.com/uk/animation/seasons/25/episode-47-a-squad-worth-of-passion

The Squirtle firefighting team appears as a traveling professional/public-facing unit and later responds to a real fire.

Reusable structure:
- a responder organization can have training, public demonstrations and operational duties;
- a unit can travel between settlements;
- public reputation and actual operational readiness remain separate.

### Pokémon Ranger: Heatran Rescue!
Source: https://www.pokemon.com/us/animation/seasons/13/episode-11-pokemon-ranger-heatran-rescue

The scenario combines search, hazardous terrain, rescue, Pokémon assistance and transport to a destination after stabilization.

Reusable structure:
- incident response can transition through search -> stabilization -> extraction -> transfer;
- the actor handling the immediate rescue need not own the receiving institution;
- the rescue destination and custody handoff matter after the dramatic scene ends.

No Ranger Capture rules are inferred from this episode.

### Pokémon Mystery Dungeon: Rescue Team DX
Source: https://mysterydungeon.pokemon.com/en-au/

The Rescue Team premise demonstrates a world where rescue requests can be a durable institutional loop rather than isolated scripted events.

Reusable structure:
- requests can enter a queue;
- different jobs can require different capabilities;
- completion history can shape institutional memory;
- routine jobs should compress while exceptional incidents expand.

The game’s ranks, rewards and dungeon rules are not imported.

### FEMA/NIMS — incident coordination and interoperability
Sources:
- https://training.fema.gov/emiweb/is/icsresource/assets/ics_training_reference_guide.pdf
- https://www.fema.gov/sites/default/files/documents/fema_eoc-quick-reference-guide.pdf

The useful abstraction is that multiple organizations can coordinate toward common incident objectives while retaining their own authority. Standardized terminology, interoperable communications and explicit interfaces improve handoffs.

Ouros adaptation:
- use explicit incident roles and unit status;
- support mutual aid without merging institutions into one faction;
- preserve which organization owns which decision;
- allow common objectives while authority remains scoped;
- store handoffs and after-action corrections.

Do not import US legal authority, NIMS terminology as canon, emergency-number systems, command titles, certification requirements or jurisdiction rules.

## Design lessons for Ouros

1. A crisis and a response operation are different persistent objects.
2. A report can be valid even if its interpretation is wrong.
3. Dispatch is a resource-allocation decision, not proof of severity.
4. A unit can be assigned, en route, staged, operating, unavailable, released or out of service.
5. Mutual aid must preserve institutional identity and authority boundaries.
6. A responder Pokémon must retain agency, individual identity, custody/partnership state and the right to stop participating where the world model supports that state.
7. A battle result cannot by itself mark an evacuation complete, a fire controlled, a patient transferred or a route safe.
8. The response timeline should persist after the incident for reviews, training and later public memory.
9. Multiple incidents can compete for the same scarce unit.
10. A quiet period can still create content through drills, inspections, dispatch failures and readiness exercises, but these should arise from institutional state rather than random filler.

## PTU/Caelo boundaries

No new PTU mechanics are validated by this research. In particular, do not infer:
- firefighting damage or extinguishing values from Water-type Moves;
- rescue checks;
- civilian HP;
- carry/extraction rules;
- medical triage bonuses;
- responder initiative bonuses;
- command radius;
- panic status;
- vehicle speed;
- smoke/fire/environmental hazards;
- automatic cooperation from institutional Pokémon.

These require exact PTU/Caelo text and AutoPTU implementation evidence.

## Provenance status

All material in this file is research-only. Proposed Ouros structures belong in design/proposals. Nothing here is canon.