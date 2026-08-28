# Ouros Narrative Research — Seismic Monitoring & Recovery Scan 110

Status: RESEARCH ONLY. Provenance and design evidence, not Ouros canon.

Date: 2026-08-28

## Scope

This pass investigates a previously uncovered operational gap: persistent seismic observation, earthquake-event records, warning handoffs, post-event assessment, after-event uncertainty, access verification and long-term recovery memory.

The repository already contains Geology, Crisis/Rescue, Facility Maintenance, Roads/Bridges, Infrastructure Outage, Weather Preparedness, Communications, Public Notices and Settlement recovery material. This pass does not replace those owners. It defines the missing continuity between a ground-motion observation and the downstream owner systems that act on it.

Repository-wide recursive inventory was inspected before writing and returned untruncated. A repository code search for `seismic earthquake tremor aftershock` returned no dedicated existing layer. The Geology layer mentions seismic activity only as one possible source of a site disturbance.

## Internal PTU / Caelo cross-check

Internal governing references remain:

- CoreRulebook.pdf;
- Caelo Player's Guide 1.5.pdf;
- Caelo Region Location & Encounter List.pdf;
- character creation merged.pdf;
- Erratas and extra merged.pdf;
- Pokedex / pokedex merged.pdf.

The existing source scan establishes that Caelo locations can carry concrete environmental mechanics when a governing source explicitly defines them. That does not create a universal earthquake, collapse, falling-debris, unstable-ground, aftershock or structural-damage subsystem.

This pass therefore does not invent:

- earthquake magnitude or intensity arithmetic;
- prediction rolls;
- automatic knockdown or forced movement from shaking;
- collapse probabilities;
- falling-debris damage;
- structural HP;
- fissure generation;
- landslide rules;
- aftershock timing;
- Move-, Ability-, Item- or Trainer-Feature-powered seismic sensing;
- species-wide earthquake prediction;
- Ground-type immunity to earthquake hazards;
- Minecraft block destruction as PTU damage truth.

A PTU Move named Earthquake is not evidence for a general environmental-earthquake simulation contract.

## Public source 1 — Pokémon Mystery Dungeon: Rescue Team

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Red_Rescue_Team
- https://bulbapedia.bulbagarden.net/wiki/Blue_Rescue_Team
- https://bulbapedia.bulbagarden.net/wiki/Sky_Tower_Summit

Reusable structures:

Pokémon Mystery Dungeon: Red/Blue Rescue Team places repeated natural disasters into the background of ordinary rescue jobs. The important design lesson is not the eventual supernatural explanation. It is that a disaster-prone region generates recurring local requests, changes how communities interpret unusual events, gives rescue institutions persistent social importance and lets small incidents coexist with a larger mystery.

Ouros transformation:

- a seismic episode can produce many independent downstream stories instead of one mandatory disaster dungeon;
- reports from residents, rescue teams, scientists and infrastructure operators can coexist with different scopes;
- repeated events can alter routines, route choices, public trust and institutional memory;
- resolving a rescue request does not resolve the cause of the regional event;
- a later explanation must be proven by Ouros evidence rather than inferred from narrative coincidence.

Excluded:

No meteor plot, Rayquaza resolution, named rescue teams, dungeon sequence or distinctive story is imported.

## Public source 2 — Pokémon Ranger: Heatran Rescue!

Source:
- https://bulbapedia.bulbagarden.net/wiki/DP169

Reusable structure:

A small earthquake changes an active mission immediately: a target flees, traversal changes and a rescue becomes necessary. The useful pattern is event -> changed actor behavior -> new access problem -> rescue consequence.

Ouros transformation:

A tremor may be an observed event that changes current actor positions, access state or priorities, but the narrative layer must not infer that a nearby Pokémon caused it. Any tactical shaking, falling rock or rescue movement needs explicit engine support.

Excluded:

No named characters, Heatran mission, Ranger Sign behavior, capture mechanics or episode sequence is copied.

## Public source 3 — Pokémon tabletop community campaigns

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/1hgbuha/
- https://www.reddit.com/r/PokemonTabletop/comments/16tt7ux/
- https://www.reddit.com/r/PokemonTabletop/comments/onnt2p/

Reusable structures:

Public PTU campaign material shows two useful patterns. One campaign premise treats earthquakes and other disasters as long-duration regional history that changes settlement and exploration decades later. Another GM anecdote uses an earthquake-exposed cave and unstable roof as a consequence-rich location.

Ouros transformation:

- disaster history can remain relevant long after the immediate event;
- an event can expose a new route or context without making that route permanently safe;
- hazard state should be explicit and separately verified;
- community homebrew damage, collapse rolls or probabilities are not authoritative PTU rules.

Excluded:

No campaign setting, vault premise, factions, damage rolls, instability probabilities or homebrew mechanics are imported.

## Public source 4 — Fan-game reconstruction structure

Source:
- https://www.reddit.com/r/PokemonRMXP/comments/1kbh6fu/

Reusable structure:

A public Pokémon fangame development post describes a city rebuilt through several visible phases and linked quests after an earthquake. The useful lesson is staged recovery: route access, workforce, materials, morale and civic function can recover on different timelines.

Ouros transformation:

Post-event recovery should be a graph of owner-system states, not a single `city_rebuilt` flag. Roads, housing, utilities, work, public spaces, commerce and memory can recover separately while the event remains part of local history.

Excluded:

No city, quest count, gym gate, map, characters or reconstruction sequence is copied.

## Public source 5 — USGS earthquake early warning

Source:
- https://www.usgs.gov/programs/earthquake-hazards/science/earthquake-early-warning-overview

Reusable operational distinction:

USGS explicitly distinguishes earthquake early warning from prediction. The system detects an earthquake already in progress, estimates characteristics and hands information to delivery partners. Detection and public delivery are therefore separate operational stages.

Ouros transformation:

Model these as distinct facts when a region canonically supports such technology or institutions:

1. observation received;
2. event detection record created;
3. event characterization reviewed or revised;
4. alert product authorized;
5. alert handed to a communication/public-notice owner;
6. delivery attempted;
7. endpoint receipt, if known;
8. protective action by the owning system.

Do not import ShakeAlert, US agencies, sensor counts, thresholds, telecommunications or warning times into Ouros canon.

## Public source 6 — USGS aftershock forecasting

Sources:
- https://www.usgs.gov/publications/aftershock-forecasting
- https://www.usgs.gov/observatories/hvo/news/volcano-watch-aftershock-forecasts-let-you-know-what-expect-after-large

Reusable operational distinction:

Aftershock forecasts are probabilistic and revised as observations accumulate. Recovery decisions can therefore occur while uncertainty persists. A forecast is not a scripted future event and an earlier earthquake can be reclassified relative to a later larger event.

Ouros transformation:

- preserve advisory version history;
- distinguish observed event labels from later scientific interpretation;
- allow recovery work during an active uncertainty window;
- never schedule a guaranteed aftershock merely because an advisory exists;
- do not convert real-world percentages or magnitude thresholds into Ouros rules.

## Design lessons extracted

### Observation is not prediction

Pokémon behavior, a sensor reading, a resident report and a scientific interpretation are different evidence objects. None silently proves a future event.

### Detection is not delivery

An alert can exist while some settlements, devices or actors never receive it. Communications and Public Notices own dissemination.

### Shaking ended is not safe

End of observed shaking does not complete structural inspection, road inspection, utility checks, rescue, evacuation, access reopening or habitat review.

### Recovery is multi-owner

A seismic event may create work for Crisis, Roads, Maintenance, Utilities, Housing, Conservation, Commerce and Communications. This layer only preserves the event and assessment continuity needed to coordinate those owners.

### Contradictory reports can all be valid

One actor may record first felt motion, another first instrument detection, another alert authorization, another shaking end and another route reopening. Provenance and timestamp scope resolve the apparent contradiction.

### Pokémon presence is evidence, not automatic causation

A Pokémon leaving a ridge before a tremor can become a recurring mystery. It must not become a species-wide prediction capability without governing evidence.

## Candidate Ouros data needs

- persistent seismic event ID;
- observation ID and provenance;
- monitoring node state;
- detection/review revisions;
- alert/advisory handoff state;
- observed shaking footprint claims without invented numeric scale;
- post-event assessment windows;
- owner-system access restrictions by reference;
- after-event watch/advisory revisions;
- legacy-event links to later construction, routes, habitats and public memory.

## Battle implementation guardrail

Any encounter with active shaking, falling debris, fissures, collapsing terrain, landslides, unstable structures, delayed aftershocks or environmental displacement depends on the exact mechanical families involved. Minecraft physics must not fill those gaps.

Reduced encounters should move the tactical battle to a reviewed static area after the active environmental event has stopped, while leaving rescue, inspection, reopening and scientific interpretation in world-state systems.

## Canon status

Everything introduced by this research file is PROPOSED or UNKNOWN unless a separate canon file approves it. No seismic agency, technology, institution, regional hazard profile, fault system, magnitude scale or Pokémon seismic role is established by this pass.