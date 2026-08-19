# Civic Governance, Public Works & Collective Decision Research — Pass 20

Status: research/provenance only. Nothing in this file is Ouros canon.

## Why this pass exists

The repository already has durable systems for factions, settlement capabilities, crisis response, cases and authority, media, public memory, travel, trade, institutions and World Pulse activity. What was still missing was a clean model for prospective collective decisions: who may propose a public change, who is affected, how competing priorities are represented, how infrastructure choices become world state, and how a community can disagree without every dispute becoming a crime case or faction war.

This pass therefore concentrates on civic governance, public works, local administration, public hearings, settlement priorities and the long-term consequences of collective choices.

## Sources and reusable observations

### Pokémon Tabletop — Campaign Seeds: The Road to Tomorrow

Source: https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

The article explicitly frames campaigns around players building structures, establishing norms and making discoveries that affect future society. Its settlement-rebuilding seed also raises the need for government and institutions once a mobile community becomes a permanent city.

Reusable lesson: player impact can be institutional rather than only heroic. Founding a League, restoring a settlement, choosing infrastructure priorities or establishing a standard can become a long-term legacy hook.

Do not import the article's specific scenarios wholesale. The useful abstraction is creator-oriented campaign structure.

### Pokémon Legends: Arceus — Jubilife Village and the Galaxy Team

Official source: https://legends.arceus.pokemon.com/en-ca/story/

Supplemental references:
- https://bulbapedia.bulbagarden.net/wiki/Jubilife_Village
- https://www.serebii.net/legendsarceus/requests.shtml

Jubilife operates as a base with multiple corps and services. Requests from residents and institutional staff can improve or expand services, while the settlement visibly grows across the story.

Reusable lessons:
- a settlement can have several specialized bodies rather than one omnipotent authority;
- ordinary requests can feed durable service changes;
- institutions can depend on residents, facilities and field work;
- public administration can generate adventure without requiring corruption or combat.

The specific Galaxy Team structure is not proposed as Ouros canon.

### Pokémon Reborn — city restoration choices

Reference: https://reborn.sailor.li/walkthroughs/19_city_quests

The restoration intermission lets the player prioritize different city projects. Different choices unlock different follow-up content and change access to parts of the city.

Reusable lesson: a public-works decision becomes more meaningful when projects are mutually constrained by resources or timing and when each choice changes future opportunities rather than merely awarding a numeric bonus.

Do not reproduce Reborn project names, rewards, story events or setting details.

### Pokémon Conquest — territorial services and delegated development

References:
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Conquest
- https://bulbapedia.bulbagarden.net/wiki/Kingdom_location

Conquest treats each kingdom as a place with facilities and development state. Controlled areas can be delegated toward training, recruitment or development, and facilities provide concrete services.

Reusable lessons:
- local capability can come from a portfolio of facilities;
- development can be a deliberate allocation choice;
- territorial control, service access and physical infrastructure are distinct dimensions;
- a region can evolve on a slower world clock without simulating every citizen continuously.

Its conquest mechanics, monthly action economy and warlord system are not proposed for Ouros.

### Public Pokémon roleplay — civic proposals and local government

Example: https://bulbagarden.net/threads/pokemon-mystery-dungeon-performers-of-harmony.279048/post-7000145

This public RP includes residents approaching a mayor with a proposal for a community venue, discussion of land use and plans to bring the proposal before a council.

Reusable lesson: civic content works best when a proposal has a real place, affected people, a concrete purpose and a process. A social scene can matter because it changes what may be built later.

Do not copy the characters, town, theater concept or dialogue.

### Public Pokémon RP — city council as mission stakeholder

Example: https://forums.pokecharms.com/threads/mirages-in-galar.30229/

A public roleplay scene uses a city-council representative as one stakeholder in briefing a group about a regional problem while another important institution is unavailable.

Reusable lesson: civic bodies can commission, coordinate or prioritize work without personally executing it. This creates room for player professions, clubs, contractors, researchers, Rangers or other institutions to act on behalf of a settlement.

Do not copy the RP's characters, crew or specific threat.

### Pokémon fan discussion — government ambiguity as a worldbuilding warning

References:
- https://bulbagarden.net/threads/government-in-the-pokemon-world.267211/
- https://bulbagarden.net/threads/pokemon-world-government.9780/page-17

Community discussion repeatedly notes that Pokémon media shows infrastructure, public services, Gyms and police while rarely defining a complete constitutional system.

Reusable lesson: Ouros should not silently infer a modern real-world government model from the existence of roads, Centers or Gyms. Local governance must be authored explicitly where it matters, and unknown areas can remain institutionally ambiguous.

These forum posts are speculation, not canon or rules sources.

### Open-world procedural design — objectives from real mechanics

Reference: https://arxiv.org/abs/1705.00341

The paper models Minecraft mechanics to derive dependencies and feasible objectives rather than placing arbitrary goals over an open world.

Reusable lesson: civic projects in Ouros should check actual world dependencies before generating work. A bridge project needs a real crossing, a route dependency and representable construction state. A clinic expansion needs an existing facility, staffing and service pressure. This aligns with the repository's existing objective-feasibility rule.

### Minecraft settlement generation — context matters

Reference: https://arxiv.org/abs/2108.02955

The GDMC settlement-generation literature emphasizes generating settlements in response to the map rather than placing context-free structures.

Reusable lesson: public works should respond to geography, existing buildings, routes, resources, hazards and history. Ouros should prefer transforming an established settlement over spawning disposable civic locations.

## Cross-check against existing Ouros architecture

This pass should extend rather than duplicate the current systems.

`world-agency-layer.md` already covers faction fronts, influence, actor knowledge and autonomous action. Civic bodies should use those mechanisms when they act, but governance needs a separate decision record so faction influence is not confused with formal authority or public consent.

`observation-settlement-time-layer.md` already defines settlement capabilities, resident roles, upgrades, regional clocks and objective feasibility. The missing piece is how a proposed upgrade is selected, contested, revised, funded and authorized.

`case-authority-custody-layer.md` already models mandate, jurisdiction, incident response and institutional review. Civic governance is primarily prospective: choosing what should happen next. A case is primarily operational: responding to something that happened or is happening.

`media-communications-information-layer.md` already separates facts, publications, delivery and public belief. Civic decisions can consume public information without assuming everyone received or believed the same report.

`public-memory-event-legacy-layer.md` can preserve old decisions, controversies, project dedications and later reinterpretations after the decision is complete.

## PTU/Caelo boundary

The supplied PTU/Caelo project material remains the authority for mechanics. This pass proposes narrative administration only.

The PTU Core guidance already supports organization-based campaigns and mission structures, but that does not define Ouros government, law, taxes, voting, property rights or administrative procedure.

Caelo demonstrates a living-world structure with Jobs, Social scenes, Gyms, Dojos, Contests, Raids and encounters. Those activity containers can receive civic hooks, but their actual PTU mechanics remain unchanged.

A civic proposal must not grant Skill bonuses, Trainer Features, capture authority, movement permissions, battle modifiers, item effects or rewards unless the governing rules and implementation support them.

## Design conclusions for Ouros

The strongest reusable principles are:

1. Represent civic bodies as world actors with explicit scope, membership and decision procedures.
2. Separate formal mandate, faction influence, public support and actual implementation capacity.
3. Make public works respond to real settlement and route dependencies.
4. Let several projects compete for limited timing, labor, materials, attention or access without inventing a universal tax/budget simulation.
5. Preserve testimony, proposals, objections, revisions and final decisions as separate records.
6. Allow legitimate disagreement. A conservation group, transporter, merchant and nearby residents can all have coherent interests.
7. Let players supply evidence, labor, expertise, negotiation or field work without automatically making them rulers.
8. Make rejected projects useful world state. A rejected bridge may return after a crisis, a migration shift or new evidence.
9. Prefer visible consequences in Minecraft: changed roads, scaffolding, new services, closed access, restored areas, new NPC routines and altered route usage.
10. Do not assume democracy, monarchy, mayoral government, League rule or any other political system until Ouros canon explicitly defines it.

## Copyright and provenance rule

Only high-level structural lessons are retained here. No protected dialogue, scene prose, distinctive character, faction, plot or quest chain is copied into Ouros proposals.
