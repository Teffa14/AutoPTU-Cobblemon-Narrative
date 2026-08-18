# Crisis, Rescue & Recovery Research — Pass 12

Status: external research and design extraction only. Nothing in this file is Ouros canon.

## Research question

How can Ouros turn storms, fires, collapses, eruptions, blackouts, floods, missing-person incidents and other crises into persistent Pokémon adventures without reducing them to scripted cutscenes, arbitrary damage, or a sequence of mandatory battles?

This pass intentionally concentrates on a gap not covered by prior layers: crisis lifecycle, situational uncertainty, evacuation, rescue allocation, temporary shelters, cascading infrastructure failures, recovery and preparedness.

## Source 1 — Pokémon Mystery Dungeon: Rescue Team DX

Official source:
https://mysterydungeon.pokemon.com/en-us/world/

Secondary official product page:
https://www.pokemon.com/uk/pokemon-video-games/pokemon-mystery-dungeon-rescue-team-dx

Observed structure:
- Natural disasters create many local problems rather than one single quest.
- A standing rescue organization receives requests from affected inhabitants.
- The social hub remains important between deployments.
- Players choose from rescue requests rather than following only a single disaster script.
- A large mystery about the disasters can coexist with small self-contained rescue jobs.

Reusable lesson for Ouros:
A regional crisis should emit a portfolio of consequences. One storm may create missing travelers, blocked roads, displaced wild Pokémon, damaged workshops, transport cancellations, shelter demand, research opportunities and later reconstruction work. Players can interact with different consequences according to profession and interest.

Do not copy:
- Pokémon Mystery Dungeon characters, towns, plot reveals, dialogue or specific dungeon narratives.
- Rescue Team ranks or systems as direct mechanical imports unless separately designed and reviewed.

## Source 2 — Pokémon Ranger official mission structure

Official overview:
https://www.pokemon.co.jp/game/ds/ranger/

Official mission examples:
https://www.pokemon.co.jp/game/ds/ranger/mission01.html
https://www.pokemon.co.jp/game/ds/ranger/mission02.html

Official world/system explanation:
https://www.nintendo.co.jp/ds/argj/world/index.html

Observed structure:
- Rangers address both natural hazards and ordinary resident problems.
- Early missions are intentionally smaller and appropriate to experience.
- Pokémon abilities are used to solve field problems and clear obstacles.
- Mission examples include extinguishing a forest fire, escorting a professor through hazardous terrain, finding a missing person, responding to rockfall, and investigating earthquake/volcanic activity.
- The surrounding incident can escalate while the mission objective remains concrete.

Reusable lesson for Ouros:
Crisis content should be decomposed into operational tasks with observable goals. A regional emergency can be large while an individual job remains understandable: locate, escort, clear, stabilize, deliver, survey, contain, restore, evacuate or communicate.

The field-use principle is particularly relevant to PTU, but exact legal use must come from the individual Pokémon's governing PTU/Caelo capabilities and AutoPTU/Cobblemon implementation. Ouros must never assign a rescue power because a species merely looks suitable.

## Source 3 — Pokémon Ranger target-clear design

Official source:
https://www.pokemon.co.jp/game/ds/ranger/pokeassist.html

Observed structure:
- Obstacles are represented as explicit field problems.
- Different Pokémon provide different types of help.
- Progress depends on matching available capabilities to the problem.

Reusable lesson for Ouros:
Represent crisis obstacles as world-state objects instead of prose-only blockers.

Possible narrative obstacle classes:
- BLOCKED_ROUTE
- ACTIVE_FIRE
- FLOODED_PASSAGE
- POWER_LOSS
- COLLAPSED_STRUCTURE
- TOXIC_AREA
- STRANDED_ACTOR
- LOST_SIGNAL
- UNSTABLE_TERRAIN
- PANICKED_WILD_GROUP

These labels are descriptive only. They do not grant PTU effects or define legal actions.

## Source 4 — Public Pokémon RP built around a regional storm

Public roleplay source:
https://pokeheroes.com/forum_thread?id=88202&post=2822651

Observed structure:
- Tremors and persistent severe weather make travel unsafe.
- Residents are advised to remain in place except for essentials.
- Normal institutions are disrupted: starter collection, League activity and Gym access stop.
- High-status figures are also affected by evacuation and closure.

Reusable lesson for Ouros:
A crisis should temporarily rewrite normal world loops. A dangerous weather state can close a Gym, suspend transport, change shop supply, alter NPC schedules, delay expeditions and create shelter behavior. This is more convincing than leaving every system available while only spawning a disaster-themed quest marker.

Do not copy the RP's region, names, plot or weather premise wholesale.

## Source 5 — Public Pokémon RP: Mt. Moon escape

Public source:
https://forums.pokecharms.com/threads/the-mt-moon-escape-ooc.22773/

Observed structure:
- An earthquake blocks the known entrance.
- Communication is unavailable.
- Existing wild Pokémon and a familiar traversal space become dangerous because route state changes.
- The immediate problem is escape rather than defeating a villain.

Reusable lesson for Ouros:
Existing locations can become emergency dungeons without creating new maps. Change access, communications, hazards, shelter and objectives while preserving the same geography and ecology.

## Source 6 — Pokémon Castaway

Public descriptive source:
https://pokemon-fan-game.fandom.com/wiki/Pok%C3%A9mon_Castaway

Observed structure:
- A transport accident changes the player's goals from travel to survival and search.
- Exploration serves both resource discovery and finding other survivors.
- A geographically bounded area becomes meaningful because escape, safety and missing actors are unresolved.

Reusable lesson for Ouros:
A journey interruption can generate a temporary local campaign. Travel incidents should be capable of producing search areas, temporary camps, missing-person state, route uncertainty and extraction objectives.

The source is used only for high-level structure. No plot, island, characters or scene sequence should be transplanted.

## Source 7 — Disaster Response Game

Project page:
https://www.disastergame.net/

Academic description:
https://onlinelibrary.wiley.com/doi/10.1111/dsji.12261

Observed structure:
- Disaster response is treated as time-sensitive logistics.
- Multiple stakeholders have different responsibilities.
- Personnel and supplies must be allocated to changing needs.
- Scenarios include earthquakes, floods, storms and wildfires.
- Multiplayer role separation increases coordination requirements.

Reusable lesson for Ouros:
Large emergencies should produce competing demands rather than a single optimal waypoint. Players may need to decide whether limited help goes toward medical transport, route clearing, shelter supply, wildlife response, communications or infrastructure stabilization.

Important adaptation:
Ouros should avoid turning human suffering into a score-maximization simulator. Use these structures for fictional resource pressure and coordination, not for realistic casualty optimization.

## Source 8 — Emergency Management Cascading Effects games

Hurricane version:
https://www.captrs.org/games/emce-hurricane

City Blackout version:
https://www.captrs.org/games/emce-city-blackout

Observed structure:
- Preparedness occurs before impact.
- Forecasts remain uncertain.
- Decisions affect mitigation and later response capacity.
- One failure can produce secondary consequences.
- Neighboring jurisdictions can support one another.
- The scenario unfolds through rounds with changing information.

Reusable lesson for Ouros:
Create a crisis lifecycle rather than spawning a disaster at full intensity.

Suggested phases:
1. SIGNAL
2. PREPARE
3. IMPACT
4. RESPONSE
5. STABILIZE
6. RECOVERY
7. AFTERMATH

A player who acts during SIGNAL/PREPARE should change later world state. Preparing shelters, moving vulnerable NPCs, reinforcing a route or relocating a wild collective should reduce or redirect consequences without guaranteeing success.

## Source 9 — CO-SAFE evacuation simulation research

Open-access abstract:
https://www.sciencedirect.com/science/article/pii/S2212420925006727

Observed structure:
- Local responders collaboratively design evacuation strategies.
- Shelter use, limited resources and high-priority vulnerable populations matter.
- Human-in-the-loop planning can improve later outcomes.
- Situational awareness and communication are core parts of response.

Reusable lesson for Ouros:
Different actors should have different mobility and assistance requirements. Do not model every NPC as a generic unit that can instantly follow the player. Some fictional actors may require escort, transport, medicine, reassurance, special terrain access, help with Pokémon, or a safe destination.

## Source 10 — Dynamic evacuation / information research

Agent-based evacuation study:
https://arxiv.org/abs/1910.00767

Cry-wolf / warning-compliance study:
https://arxiv.org/abs/1904.01963

Observed structure:
- Evacuation choices depend on several information sources: signage, crowd movement, familiarity and guidance.
- Contradictory information changes behavior.
- Repeated false warnings can reduce compliance.

Reusable lesson for Ouros:
Warnings should have provenance and credibility state. Different NPCs can know different things about a hazard and respond differently. A town that has experienced repeated false alerts may react differently from one with a trusted local warning network.

This should remain an abstract social model. Ouros should not claim real-world emergency-management accuracy.

## Source 11 — Hazard Extract

Developer design page:
https://www.gravewakelabs.com/games

Observed structure:
- Hazards spread and reshape the map.
- Safe extraction points can become unsafe.
- Limited evacuation capacity creates prioritization.
- The disaster itself changes over time instead of remaining a static backdrop.

Reusable lesson for Ouros:
Some crisis zones should use a spatial hazard frontier or set of changing unsafe tiles/areas. The player should react to new world state rather than memorizing one fixed solution.

## Cross-source patterns

### Crisis is a state generator

A useful emergency generates many linked states:
- route closures
- missing actors
- shelter demand
- supply interruption
- damaged services
- displaced Pokémon
- changed encounter behavior
- communication outages
- temporary authority changes
- new rumors
- economic consequences
- repair projects
- memorial/public-memory changes

### Preparedness must matter

If players receive warning, their choices before impact should alter later consequences.

Preparedness examples:
- inspect weak infrastructure
- move supplies
- establish alternate routes
- prepare a temporary clinic
- relocate a nesting site
- warn travelers
- stage transport
- place field teams
- verify communications

Preparedness should change probabilities or available options only when the underlying simulation supports it. Narrative text alone must not secretly grant mechanical immunity.

### Crisis information is incomplete

Useful uncertainty types:
- severity uncertain
- location uncertain
- route state unknown
- missing-person status unknown
- infrastructure status unknown
- second hazard possible
- rumor contradicts official report

The generator should expose enough information for a decision while preserving uncertainty where world state supports it.

### Rescue is broader than combat

Useful verbs:
- SEARCH
- LOCATE
- SIGNAL
- ESCORT
- EVACUATE
- SHELTER
- STABILIZE
- CLEAR
- DELIVER
- RECONNECT
- EXTRACT
- CONTAIN
- SURVEY
- RESTORE
- REOPEN
- REUNITE

Battle may occur because frightened Pokémon, hostile actors or hazardous circumstances interfere. It should not automatically be the center of every emergency.

### Recovery is playable

Most game disasters stop when the boss or hazard ends. Ouros can gain persistence by keeping the recovery phase:
- reopen a route
- restore a service
- rebuild a workshop
- relocate residents
- survey habitat damage
- trace contamination
- update maps
- revise emergency plans
- commemorate losses or successful rescue
- investigate the original cause

## PTU/Caelo grounding

The supplied PTU/Caelo material already supports the concept that location and terrain can matter to play. Caelo uses distinct Job, Encounter, Raid and Social activity categories, and its regional material contains places such as Toxic Ravine where an environmental condition directly matters during play.

PTU capabilities such as Naturewalk, Groundshaper, movement capabilities and other species-specific tools can potentially interact with rescue situations, but this research pass deliberately does not assign those interactions.

Exact mechanics that must remain authoritative elsewhere:
- Skill Check DCs
- falling damage
- drowning/suffocation
- carrying limits
- movement rates
- Jump/Swim/Sky legality
- Mountable rules
- terrain costs
- weather effects
- damage/status from hazards
- healing and medical effects
- capture legality
- initiative
- combat objectives

Any crisis encounter implemented in AutoPTU must use the governing PTU/Caelo rules and actual engine state.

## Design directions for Ouros

1. Create a persistent CRISIS object with lifecycle phases.
2. Separate hazard truth from forecasts, reports and rumors.
3. Let one crisis produce many optional operational jobs.
4. Track temporary safe zones and shelters.
5. Allow infrastructure failures to cascade through routes, services and settlements.
6. Make preparedness write state before impact.
7. Let recovery persist long after immediate danger ends.
8. Record who responded and what they actually did in the Chronicle/public-memory layers.
9. Allow ecological and wild-collective systems to respond independently.
10. Keep tactical hazard mechanics behind explicit PTU/Caelo + AutoPTU validation.

## Copyright/provenance boundary

The external Pokémon games, public RPs, fangame descriptions and serious-game research are used only for general structures and design lessons. Ouros proposals must use original locations, characters, institutions, incidents, dialogue and causal chains.

No copyrighted prose, scene sequence, distinctive characters or full plots should be copied into future Ouros canon.