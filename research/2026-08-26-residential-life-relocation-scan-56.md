# Narrative Research Scan — Pass 56: Residential Life, Relocation & Neighborhood Continuity

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-26

## Why this pass

The repository already has strong layers for settlement capabilities, civic works, hospitality, travel, care, social bonds, economy, media, public memory and recurring events. Those systems can say that housing exists or that a settlement changes, but there is still no dedicated model for a residence as a persistent place with occupants, routines, Pokémon compatibility, maintenance history, relocation pressure and neighborhood continuity.

This pass therefore focuses on homes and residential life as durable world state rather than as decorative interiors.

## Sources reviewed

### 1. PTU: Kairos Isles — Real-Estate
Source: https://kairosptu.wiki.gg/wiki/Real-Estate

Reusable structure:
- a persistent home or team property can accumulate function over time;
- upgrades can represent services, workshops, nurseries, training spaces or other long-lived capabilities;
- ownership, team use and property function are distinct states;
- property development can become a continuing downtime loop instead of a one-scene reward.

Transformation rule for Ouros:
Do not copy Kairos upgrade prices, slot counts, house levels, bonuses or custom rules. The useful pattern is persistence: a residence can remember who uses it, what services exist there, which changes were completed and what dependencies remain.

### 2. PTU: Kairos Isles — Herkimer Town
Source: https://kairosptu.wiki.gg/wiki/Herkimer_Town

Reusable structure:
- settlement history is recorded through dated player-facing events;
- new facilities and residents become part of the town's durable identity;
- repeated cleanup, construction and installation activity can make the same place feel changed over time;
- residential and service growth can be visible without inventing a new town for each arc.

Transformation rule for Ouros:
Use event history as provenance for changed residential state. Avoid reproducing Kairos names, building lists or mechanical housing levels.

### 3. Pokémon Legends: Arceus — Request 85, At Home under the Eaves
Sources:
- https://www.serebii.net/legendsarceus/requests/athomeundertheeaves.shtml
- https://pokemondb.net/legends-arceus/missions-requests

Reusable structure:
- a housing problem can be about compatibility rather than ownership;
- several plausible locations can fail for different environmental or social reasons;
- the final outcome can change because the resident's attitude changes after observing the Pokémon;
- a small domestic request can reveal wind exposure, isolation, nearby battle activity and neighborhood relationships.

Transformation rule for Ouros:
Do not copy the Chimecho story. Preserve the high-level grammar: identify a residential mismatch, survey alternatives, learn why each option works or fails, and allow the requester to revise their position from new evidence.

### 4. Pokémon Legends: Z-A — Finding a Place for Heliolisk
Source: https://www.nintendolife.com/guides/pokemon-legends-z-a-finding-a-place-for-heliolisk-side-mission-whats-the-right-apartment

Reusable structure:
- housing selection can account for the needs of a human-Pokémon household;
- affordability and suitability can conflict;
- an urban apartment search can become a quest about fit, routine and quality of life rather than combat;
- a Pokémon's environmental preferences can matter to a household decision.

Transformation rule for Ouros:
Do not infer generic species housing bonuses. A Pokémon-specific need must come from observed behavior, established species information or an authoritative capability where relevant. Narrative preference must remain separate from PTU mechanical effect.

### 5. Pokémon Unbound — Mission 030, Home for a Hobo
Source: https://unboundwiki.com/missions/mission-030/

Reusable structure:
- housing access can depend on another unresolved problem elsewhere;
- the eventual residence is a persistent world change with a moved NPC;
- relocation can create a callback location and changed social geography;
- a housing arc can combine social investigation, travel and combat while keeping the actual move itself non-combat.

Transformation rule for Ouros:
Do not copy the mission's characters, criminal setup, reward or plot sequence. The useful structure is dependency chaining: an available residence may exist, but access depends on resolving the owner's current blocker.

### 6. The Reckless Rollers — downtime episode pattern
Sources:
- https://the-podcast-app.com/podcasts/the-reckless-rollers-p6669367
- https://creators.spotify.com/pod/show/reckless-rollers

Reusable structure:
- PTU actual play can sustain sessions where travel, jobs and downtime matter between larger conflicts;
- not every meaningful episode requires a dungeon or formal battle arc;
- recurring characters and personal business can coexist with the next job.

Transformation rule for Ouros:
Use domestic and neighborhood scenes as playable connective tissue when they contain decisions, relationships, maintenance, preparation or consequences. Compress uneventful routine.

## Cross-source synthesis

The strongest reusable pattern is not "give the player a house." It is "make residence state persistent enough that place, occupants and routines can accumulate history."

A useful residential loop can be:

1. a household has a need or mismatch;
2. the current residence is inspected rather than assumed inadequate;
3. alternatives are evaluated against concrete constraints;
4. a blocker may live in another system such as transport, public works, care, economy, ecology or social relations;
5. a move, renovation or accommodation is selected;
6. the chosen residence changes world state;
7. the former residence and neighborhood remain historical state;
8. later events can reference the change without replaying the original quest.

## Design lessons for Ouros

### Residence should be an object, not a reward flag
Useful state includes occupants, access, purpose, condition, environmental context, Pokémon accommodation, maintenance, nearby services and prior changes.

### Household does not imply family
A household may contain one resident, unrelated roommates, a temporary guest, a trainer and Pokémon, a caretaker arrangement, a club residence, a work-live arrangement or another authored structure. The generator must not infer family or romance.

### Pokémon presence does not imply ownership
A wild Pokémon may shelter near a residence. A cared-for Pokémon may be present temporarily. A visitor's Pokémon may stay overnight. Ownership and custody stay authoritative elsewhere.

### Suitability should have reasons
"Good house" is too abstract. A location may succeed or fail because of noise, weather exposure, stairs, distance from care, transport access, workspace needs, nearby habitat, crowding, service reliability or another explicit fact.

### Relocation should preserve continuity
Moving an NPC should update their address, routines, route access, neighbors, service dependencies and likely encounter surfaces. It should not silently delete their previous ties.

### Domestic scenes should be selective
Routine sleeping, eating, cleaning and returning home should usually compress. Playable home scenes need a decision, interruption, relationship beat, maintenance issue, preparation task, information reveal or consequence.

## High-value Ouros hooks derived from the research

- a resident asks for help evaluating three possible accommodations, each failing for a different traceable reason;
- a wild Pokémon repeatedly shelters on a building and the household must decide whether to adapt, relocate it or change the site;
- a relocation becomes possible only after a public-works or transport blocker is resolved;
- a long-term NPC moves districts and their daily route changes who they meet and which services they use;
- a shared residence gains a workshop or care space through a project rather than a menu purchase;
- a neighborhood notices a recurring environmental problem through several homes rather than through a single quest giver;
- a former home becomes narratively relevant later because records, neighbors or lingering maintenance state still exist there.

## Canon/provenance boundary

This research establishes no Ouros landlord system, tenancy law, rent economy, property ownership model, zoning rules, household benefits, mortgage rules, homelessness policy, building code, Pokémon housing standard or residential geography.

Any such material must be authored and reviewed separately.

## Mechanical boundary

Residential content is primarily narrative/world-state content. It must not invent:
- Trainer Feature benefits from owning a home;
- healing bonuses from sleeping in a residence;
- breeding benefits from co-location;
- Pokémon capability bonuses from housing type;
- movement bonuses from neighborhood familiarity;
- custom weather protection;
- combat buffs from workshops, kitchens or training rooms;
- automatic ownership from occupancy;
- Skill-check DCs for tenancy, repair or relocation without PTU/Caelo support.

Mechanically rich incidents must declare exact AutoPTU capability dependencies and provide a reduced implementation where useful.