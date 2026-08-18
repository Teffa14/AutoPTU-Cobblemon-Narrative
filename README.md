# AutoPTU-Cobblemon-Narrative

Narrative and world-state design repository for the Ouros AutoPTU + Cobblemon project.

The long-term goal is a persistent Pokémon world where player decisions, battles, discoveries, relationships, faction activity, ecological knowledge, settlement changes, public memory, recurring events, investigations, institutional responses, material culture, production, trade, mythology, archaeology, sacred-site stewardship, mentorship, clubs, learning communities, travel networks, transport services, expeditions, wild Pokémon collectives and environmental changes can become durable world state. Minecraft/Cobblemon provides the explorable overworld; AutoPTU provides the tactical grid-battle rules engine.

## Repository layers

- `research/`: external-source research and provenance. Nothing here is automatically canon.
- `design/`: narrative architecture, schemas and implementation-facing design.
- `proposals/`: original Ouros worldbuilding, quest, faction, NPC, dungeon, encounter and story-arc candidates. Explicitly non-canon until reviewed.
- future `canon/`: only reviewed material promoted after originality, continuity, PTU/Caelo rules and implementation review.

## Current foundation

### Research
- [Narrative research scan — pass 01](research/2026-08-18-source-scan.md)
- [Mission, dungeon & RP research — pass 02](research/2026-08-18-missions-dungeons-rp-scan-02.md)
- [Factions, fields, bonds & investigation research — pass 03](research/2026-08-18-factions-fields-bonds-scan-03.md)
- [Observation, settlement & time research — pass 04](research/2026-08-18-observation-settlement-time-scan-04.md)
- [Public memory, events & legacy research — pass 05](research/2026-08-18-public-memory-events-legacy-scan-05.md)
- [Cases, authority & custody research — pass 06](research/2026-08-18-cases-authority-custody-scan-06.md)
- [Material culture, crafting & economy research — pass 07](research/2026-08-18-material-culture-crafting-economy-scan-07.md)
- [Myth, archaeology & sacred-sites research — pass 08](research/2026-08-18-myth-archaeology-sacred-sites-scan-08.md)
- [Social bonds, mentorship, clubs & learning research — pass 09](research/2026-08-18-social-bonds-mentorship-clubs-scan-09.md)
- [Travel, transport & expedition logistics research — pass 10](research/2026-08-18-travel-transport-expedition-scan-10.md)
- [Wild collectives, territory & group ecology research — pass 11](research/2026-08-18-wild-collectives-territory-scan-11.md)

### Systems design
- [Ouros narrative architecture](design/ouros-narrative-architecture.md)
- [Mission & dungeon grammar](design/mission-dungeon-grammar.md)
- [World agency layer](design/world-agency-layer.md)
- [Observation, settlement & time layer](design/observation-settlement-time-layer.md)
- [Public memory, event & legacy layer](design/public-memory-event-legacy-layer.md)
- [Case, authority & custody layer](design/case-authority-custody-layer.md)
- [Material culture, crafting & economy layer](design/material-culture-economy-crafting-layer.md)
- [Myth, archaeology & sacred-sites layer](design/myth-archaeology-sacred-sites-layer.md)
- [Social bonds, mentorship & clubs layer](design/social-bonds-mentorship-clubs-layer.md)
- [Travel, transport & expedition layer](design/travel-transport-expedition-layer.md)
- [Wild collective agency layer](design/wild-collective-agency-layer.md)

### Non-canon Ouros candidates
- [First worldbuilding seeds](proposals/2026-08-18-worldbuilding-seeds.md)
- [Adventure seeds — pass 02](proposals/2026-08-18-adventure-seeds-02.md)
- [World agency seeds — pass 03](proposals/2026-08-18-world-agency-seeds-03.md)
- [Observation & settlement seeds — pass 04](proposals/2026-08-18-observation-settlement-seeds-04.md)
- [Public memory & event seeds — pass 05](proposals/2026-08-18-public-memory-event-seeds-05.md)
- [Case & authority seeds — pass 06](proposals/2026-08-18-case-authority-seeds-06.md)
- [Material culture & crafting seeds — pass 07](proposals/2026-08-18-material-culture-seeds-07.md)
- [Myth & archaeology seeds — pass 08](proposals/2026-08-18-myth-archaeology-seeds-08.md)
- [Social bonds, mentorship & clubs seeds — pass 09](proposals/2026-08-18-social-bonds-seeds-09.md)
- [Travel, transport & expedition seeds — pass 10](proposals/2026-08-18-travel-transport-expedition-seeds-10.md)
- [Wild collective seeds — pass 11](proposals/2026-08-18-wild-collective-seeds-11.md)

## Mechanical source priority

Narrative proposals must not invent combat legality, crafting legality, item behavior, supernatural powers, ritual effects, social progression rewards, Pokémon Loyalty mechanics, Legendary encounter permissions, overworld movement rules, mount eligibility, travel speeds, carrying limits, transport capacities, navigation checks, pack bonuses, collective morale, group leadership mechanics or wild-group combat modifiers. When mechanics are required, validate against the project's supplied PTU/Caelo source set, including the PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List, plus the actual AutoPTU implementation state.

External stories are inspiration sources, not rules sources.

## Generation rule

Research may propose structures and original candidates, but generated objectives should be traceable to current world facts, actor motives, ecological state, player history, public memory, case state, institutional mandate, material provenance, workshop/service state, supply routes, cultural traditions, archaeological observations, mythic claims, social history, mentorship state, club projects, route state, transport availability, wild-collective state or executable game mechanics. Material should not enter future `canon/` until reviewed.

Case generation must keep allegations, hypotheses, evidence, public belief and canonical truth separate. The generator must not invent legal powers, ownership rules, detention procedures or criminal status until those systems are explicitly established for Ouros.

Production generation must keep mechanical item definitions separate from narrative item instances. The generator must not invent recipes, prices, crafting prerequisites, yields, repair bonuses or resource-producing Pokémon powers that are not supported by the governing PTU/Caelo data and current implementation.

Deep-history generation must keep archaeological observation, historical interpretation, mythic tradition, ritual practice, anomalous phenomena and canonical truth separate. The generator must not automatically treat an old object as loot, a sacred Pokémon as owned, a ritual as mechanically effective, a rumor as a Legendary appearance, or a community belief as established cosmology.

Social generation must keep observable shared events separate from inferred private emotions. The generator may remember cooperation, conflict, promises, lessons, competitions and institutional membership, but it must not assign romance, friendship, hatred, forgiveness, betrayal, mentorship or other PC-to-PC relationship labels without player-authored evidence or explicit consent. It must not grant Skills, Edges, Features, Tutor Moves, Loyalty effects or other PTU progression through narrative relationship state unless governing rules explicitly support it.

Travel generation must keep physical connection state, transport-service state and actor route knowledge separate. Routine known travel should compress when no meaningful decision intersects the journey. Personal Pokémon-assisted traversal requires authoritative validation of the individual Pokémon's legal movement/capability state; public transport, guides and institutional mobility remain valid alternatives when world state supports them. Route incidents must come from actual route, clock, ecology, faction, case, service or player-intent state rather than mandatory filler encounters.

Wild-collective generation must keep population abundance, persistent group identity, currently visible subgroup and tactical encounter participants separate. Leadership, territory, kinship, cooperation, communication and group memory require species-grounded or observed evidence; they are never inferred merely from multiple Pokémon spawning together. Collective state may shape why an encounter occurs and what persists afterward, but it cannot grant unsupported PTU combat bonuses or replace actual Pack Mon, swarm, escape, capture or encounter rules.