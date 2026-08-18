# Ouros Narrative Research — Cases, Authority & Custody — Pass 06

Status: Research only. Provenance and design evidence; not Ouros canon.

This pass follows the existing work on mission grammar, world agency, ecology, settlements, public memory and recurring events. The missing layer examined here is how a persistent Pokémon world can represent incidents, cases, response organizations, evidence custody, pursuit, institutional handoffs and non-lethal resolutions without assuming one universal police system or importing real-world law into Ouros.

## 1. Detective Pikachu Returns — humans and Pokémon can both contribute evidence

Primary source:
- https://detectivepikachu.pokemon.com/en-au/

Observed structure:
- Cases are solved by gathering statements and clues rather than only by defeating opponents.
- Information can come from both humans and Pokémon.
- Particular Pokémon can assist through their own capabilities; the official example uses a Growlithe following scent trails.
- Pokémon assistance reveals information available through that Pokémon's ability rather than granting unrestricted knowledge of the case.

Reusable lesson for Ouros:
Investigation should have explicit evidence acquisition routes. A Pokémon may enable a route only when its actual PTU/Caelo capabilities, senses or legal actions support that interaction.

Ouros translation:
- store human statements, Pokémon-observation evidence and physical evidence separately;
- every clue records how it became observable;
- capability-assisted discovery returns observable facts, not the hidden canonical answer;
- a player without the relevant capability must be able to pursue alternate leads when the information is plot-critical;
- the global narrative model must never silently substitute world truth for what the investigator can know.

This extends the existing evidence graph and actor-knowledge boundary rather than replacing them.

## 2. Pokémon Ashen Frost — recurring cases can coexist with an open city

Source:
- https://www.eeveeexpo.com/ashen-frost/

The public fangame description presents a story-focused detective game with a large sequence of cases, clue searching, evidence presentation, a dedicated case interface, extensive optional quests and an expanding city. Battles remain present, but case progression has its own interaction structure.

Reusable lesson for Ouros:
A case can be a persistent state object parallel to ordinary quests. It may remain active while players explore, battle, socialize, complete side work or pursue other leads in the same settlement.

Ouros translation:
A case should track:
- triggering incident;
- responsible or affected jurisdictions/institutions;
- victims, missing entities or damaged assets;
- claims and evidence;
- current hypotheses;
- people/Pokémon of interest;
- locations to investigate;
- assigned and voluntary participants;
- unresolved questions;
- current response state;
- possible handoff or closure states.

The case UI concept is reusable at a structural level. No case text, characters, plots or custom mechanics from Ashen Frost are imported.

## 3. Pokémon Ranger — response organizations can be geographically distributed

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Ranger_Base
- https://bulbapedia.bulbagarden.net/wiki/Ranger_Union_HQ
- https://bulbapedia.bulbagarden.net/wiki/Ranger_Missions

Public Ranger material shows local Ranger Bases where teams discuss missions before deployment, alongside a larger Union headquarters supporting regional operations. Mission portfolios span escort, investigation, disaster response, missing-person searches, rescue, ruins, protection, sabotage response and major coordinated operations.

Reusable lesson for Ouros:
An organization should not need omnipresent jurisdiction. It can have local offices, regional coordination, specialist teams and limited operational scope.

Ouros translation:
An institution may declare:
- geographic operating scope;
- incident categories it normally handles;
- local bases and personnel;
- specialists available;
- escalation and handoff relationships;
- emergency-response capability;
- public services;
- active cases or operations.

Different institutions may overlap. A local settlement, Gym, conservation service, research institute and regional response organization can all care about the same event for different reasons.

## 4. Ranger mission variety — response does not imply arrest

Source:
- https://bulbapedia.bulbagarden.net/wiki/Ranger_Missions

The Ranger mission catalogue mixes rescue, environmental emergencies, investigation, protection, pursuit, infrastructure threats and organized opposition.

Reusable lesson for Ouros:
Institutional assignments should use a broad response vocabulary. An official request does not automatically become a combat or apprehension mission.

Candidate response intentions:
- observe;
- warn;
- escort;
- rescue;
- evacuate;
- search;
- investigate;
- secure a location;
- protect an entity;
- recover an asset;
- contain a hazard;
- negotiate;
- pursue;
- interrupt an operation;
- transfer responsibility.

Each intention must later map to actually implemented Minecraft/AutoPTU verbs.

## 5. Mystery Dungeon — ordinary jobs and outlaw jobs are separate request channels

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Job_%28Mystery_Dungeon%29
- https://bulbapedia.bulbagarden.net/wiki/Outlaw_Notice_Board

Explorers-era Mystery Dungeon distinguishes a normal Job Bulletin Board from an Outlaw Notice Board. Publicly documented mission types include rescue, escort, item work and outlaw apprehension. The Guild also checks entrants against known outlaw status.

Reusable lesson for Ouros:
A world can distinguish ordinary requests from response-to-threat cases. The difference should come from incident state and institutional mandate rather than merely changing the icon color of the same quest template.

Ouros translation:
A pursuit or wanted-case source may create objectives such as locating, observing, intercepting, negotiating surrender, protecting another party or transferring custody. Defeat-all should remain only one possible tactical route when mechanically and narratively appropriate.

No Mystery Dungeon rank, outlaw or guild rules are imported directly.

## 6. International Police — cross-regional investigations create handoff stories

Source:
- https://bulbapedia.bulbagarden.net/wiki/International_Police

The official Pokémon setting contains a worldwide investigative organization whose agents work undercover and pursue major groups across several regions. Its appearances demonstrate that local events can become part of a broader investigation and that operatives may arrive from outside the immediate setting.

Reusable lesson for Ouros:
Some cases can cross settlement or regional boundaries, but global scope should not erase local institutions. Cross-region authority is useful primarily because it creates coordination, information asymmetry, handoffs, competing priorities and travel-linked case progression.

Ouros translation:
A case may have:
- origin jurisdiction;
- current location jurisdiction;
- requesting institution;
- assisting institutions;
- transfer history;
- information-sharing restrictions;
- reasons another group has become involved.

Exact legal powers must be authored in Ouros canon rather than inferred from Pokémon canon or real-world law.

## 7. Public roleplay — operational specialization supports multiplayer investigations

Source:
- https://forums.pokecharms.com/threads/pokemon-international-police-discussion.22224/

A public Pokémon RP concept divides an investigative group among detectives, a data specialist, an assistant/logistics function and a tactical task force. The specific fictional organization and characters are not relevant; the structural division of work is.

Reusable lesson for Ouros multiplayer:
A case does not need every participant standing on the same tile doing the same Skill Check.

Potential participation roles:
- field investigator;
- interviewer/liaison;
- analyst;
- Pokémon tracker or capability specialist;
- tactical responder;
- rescue specialist;
- logistics/support;
- local guide;
- expert consultant;
- witness or reporting party.

These are narrative roles, not new Trainer Classes or PTU bonuses.

## 8. Fanfiction metadata — case-of-the-week framing is compatible with Pokémon worlds

Source:
- https://www.fanfiction.net/s/13403179/1/Pokemon-Case-Files

Public metadata for Pokémon mystery/crime fanfiction demonstrates recurring-case framing inside familiar Pokémon regions. This source is retained only as evidence that readers/authors use Pokémon successfully in episodic investigative structures.

Reusable lesson for Ouros:
Cases can offer episodic closure while long-term institutional, relationship and regional arcs continue around them.

No prose, characters, scene details or case plots from fanfiction are used.

## 9. Internal PTU / Caelo grounding

The project PTU/Caelo corpus already gives Ouros the required boundary for mechanical investigation:
- PTU supports meaningful choices and character/Pokémon capabilities as session tools;
- Caelo uses Skill Checks and opposed resolution when failure is meaningful;
- Pokémon capabilities, senses, movement and Moves must come from the actual governed character/Pokémon state;
- Caelo's Social, Job, Encounter, Raid, Gym and other activity categories allow a case to cross multiple types of play;
- existing location and environmental rules can make scene security, pursuit and evidence access physically meaningful.

Therefore this pass does not define new Skill effects, warrant rules, capture legality, detention systems, arrest mechanics or punishment. Those are canon/mechanics decisions that require explicit design.

## 10. Design conclusions from this pass

1. `CASE` should be a persistent orchestration object distinct from `QUEST`.
2. Every case begins from an incident or report with provenance.
3. Jurisdiction and institutional mandate should be explicit world data rather than assumed universal authority.
4. Players need participation roles; not every participant is automatically an investigator or official.
5. Pokémon-assisted investigation must be capability-gated and reveal only observable information.
6. Evidence needs acquisition and custody history so it can be lost, transferred, contested or tampered with without rewriting truth.
7. Hypotheses and accusations must remain separate from canonical facts.
8. Pursuit should be a moving world state, not always a battle marker.
9. Custody and transfer outcomes can resolve cases without knockout or imprisonment being mandatory.
10. Institutional mistakes, conflicting mandates and handoffs can create stories without requiring an evil authority faction.
11. Public accusation belongs to the public-memory layer; case truth remains separate.
12. Cross-regional cases should increase coordination complexity rather than centralize all world authority.

## Copyright and provenance guardrail

No external dialogue, distinctive characters, case plots, institutional lore or custom mechanics are imported. Source material is retained only to support high-level structural observations. Any Ouros institution, law, jurisdiction, procedure, case or NPC created from this research must be original and remain non-canon until reviewed.
