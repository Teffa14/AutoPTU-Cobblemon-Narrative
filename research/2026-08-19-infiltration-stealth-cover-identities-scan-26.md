# Infiltration, Stealth & Cover Identity Research — Pass 26

Status: research and provenance only. Nothing in this document is Ouros canon.

## Why this pass

The existing repository already has cases, evidence, antagonists, faction fronts, communications, travel, investigations, public memory and encounter contracts. It does not yet have a dedicated model for covert access: sneaking through physical space, presenting a false or partial identity, maintaining a cover story, learning security routines, being recognized by witnesses, losing access without automatically starting combat, or extracting after a compromised operation.

This pass studies those structures without importing plots, characters, dialogue or stealth mechanics wholesale.

## Source findings

### Pokémon: Looker and covert investigation

Official Pokémon animation repeatedly uses Looker as an investigator who hides his role, adopts disguises and follows evidence before an open confrontation. In “Team Plasma’s Pokémon Power Plot!” he initially appears under a disguise before revealing himself and continuing an investigation of Team Plasma. In “Unlocking the Red Chain of Events!” the story also shows an investigation losing accumulated information when hostile technology destroys collected data.

Sources:
- https://www.pokemon.com/us/animation/seasons/16/episode-15-team-plasmas-pokemon-power-plot
- https://www.pokemon.com/us/animation/seasons/12/episode-45-unlocking-the-red-chain-of-events
- https://www.pokemon.com/us/animation/seasons/12/episode-25-frozen-on-the-tracks

Reusable structure:
- covert identity can precede open action;
- investigation and infiltration are connected but not identical;
- discovering a target is not the same as preserving usable evidence;
- an operation may partially succeed even if the infiltrator is discovered;
- compromised evidence or burned access can create later consequences without retconning what actually happened.

The Ouros adaptation should track identity presentation, observer belief, access state and evidence separately.

### Pokémon games: Looker as a recurring undercover investigator

Public reference material documents Looker infiltrating a Team Galactic facility while disguised as a grunt, operating in Kalos under a public-facing detective identity, and repeatedly using disguises during investigations.

Source:
- https://bulbapedia.bulbagarden.net/wiki/Looker

This is useful only as structural confirmation. Ouros should not reproduce Looker, the International Police, Team Galactic or their plots.

Reusable structure:
- one actor may have a true identity, institutional role and current presented identity;
- different observers may know different subsets of those facts;
- a cover identity can remain useful in one place after being compromised elsewhere;
- undercover work can transition into ordinary investigation, social contact or battle.

### Pokémon Parallax: stealth as a first-class mission mode

Pokémon Parallax is a public fangame centered on an undercover mission. Its project page explicitly advertises infiltration, blending in, eavesdropping, avoiding guards and completing covert tasks instead of treating every hostile area as a sequence of battles.

Primary project page:
- https://eeveeexpo.com/parallax/

Secondary discovery page:
- https://www.ducumon.click/2025/08/pokemon-parallax.html

Reusable structure:
- infiltration can be its own adventure grammar;
- the objective can be information, access, observation or extraction rather than defeat;
- detection pressure changes route choice;
- overt combat can remain possible while being undesirable or costly.

No characters, locations, Team Masque material, dialogue, custom Moves or stealth implementation are copied.

### PTU campaign seed: infiltrators inside an expedition

The official Pokémon Tabletop campaign seed “The Road to Tomorrow” includes a research expedition where a hostile organization may secretly infiltrate the research team and manipulate NPC researchers before the players even realize another organization is operating on the island.

Source:
- https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

Reusable structure:
- infiltration can target an institution rather than a building;
- an infiltrator needs plausible access, relationships and information;
- discovering that an organization has been penetrated can become a campaign arc;
- compromised staff should remain individual actors with their own beliefs rather than becoming generic hostile flags;
- counter-infiltration should rely on evidence and knowledge, not omniscient faction AI.

This connects directly to the existing Ouros actor-knowledge, institution and case layers.

### PTU campaign retrospective: stealth can trivialize content

The official “Over There!” retrospective describes a player character built around Rogue/Mastermind and stealth who could scout dangerous territory so effectively that many encounters became much easier or were bypassed.

Source:
- https://pokemontabletop.com/over-there-a-world-war-one-pokemon-campaign-a-retrospective/

Design lesson:
- infiltration competence must be allowed to work;
- designers should not negate a specialist just to force the planned battle;
- the content portfolio must still offer meaningful decisions after successful reconnaissance;
- success can change the encounter rather than delete all consequences.

Ouros should therefore convert successful scouting into better information, alternate entry points, reduced uncertainty, avoided hazards or changed encounter setup. It should not respond by secretly spawning guards that already know where the specialist is.

### PTU GM advice: Pokémon can matter to an infiltration style

Official PTU GM advice discusses a Trainer who shifts into Rogue/Ninja and an infiltration-oriented style. The article notes that Pokémon qualities such as Telepathy, Stealth, Phasing and similar capabilities can influence how useful a partner is during covert play.

Source:
- https://pokemontabletop.com/gm-advice-keeping-starter-mons-special/

Important boundary:
- this is evidence that PTU supports infiltration-oriented characters;
- it does not authorize Ouros to grant a Pokémon Telepathy, Stealth, Phasing, Invisibility or any other capability because it would be narratively convenient;
- the individual Pokémon’s authoritative PTU/Caelo state must be checked first.

### PTU source/oracle evidence

The project’s Python AutoPTU repository contains authoritative PTU source/audit material and runtime data that recognizes Stealth and Guile as skills in multiple contexts. Its source material also contains special capabilities such as Dead Silent and other concealment-related capabilities. The current Java project still treats Python AutoPTU as the source oracle while the port is incomplete.

Relevant project references inspected during this pass:
- `Teffa14/AutoPTU` search results for Stealth, Guile, Invisibility and Dead Silent;
- `Teffa14/AutoPTU-Java` README and current lifecycle commits.

Guardrail:
Exact skill uses, opposed checks, capability effects, Features, Edges and class effects must be taken from the governing PTU/Caelo source set before implementation. This research does not define new Stealth or Guile DCs.

### Public Pokémon roleplay: multiple cover identities

A public Pokécharms recruitment thread for an undercover Team Rocket scenario asks participants to maintain separate trainer, agent and Team identities and explicitly calls out skills such as disguises and technical expertise.

Source:
- https://forums.pokecharms.com/threads/pokemon-rocket-invasion.30046/

Reusable structure:
- one actor can maintain several context-specific presented identities;
- a cover may include appearance, affiliations, contacts and a story about why the person belongs there;
- the group may need to coordinate consistent covers rather than rolling stealth independently;
- exposure can be partial: one alias may be compromised while another remains usable.

No characters, scenario details or forum prose are reused.

### Pokémon Adventures: infiltration can serve a non-police profession

Public summaries of the Scarlet & Violet arc describe a treasure hunter entering an academy under a transfer-student cover while pursuing a private objective.

Source:
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Adventures

Reusable structure:
- covert identity is useful beyond police/spy stories;
- archaeology, research, journalism, faction work, rescue and rivalries can all create legitimate reasons for concealed purpose;
- an infiltrator’s actual goal may be unrelated to the institution’s central conflict.

This supports a broader Ouros design where covert play is not synonymous with crime or law enforcement.

## Stealth-game design research

### Guard placement and patrols are level-design problems

Research from the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment studies procedural placement of guards and cameras and emphasizes the balance among coverage, difficulty and believable movement.

Source:
- https://ojs.aaai.org/index.php/AIIDE/article/view/12711

Ouros implication:
Security actors need authored or generated patrol responsibilities tied to actual locations. Randomly wandering guards are poor substitutes for a security model.

### Patrol behavior changes player experience

A 2023 AIIDE user study found that players could distinguish different dynamic patrol behaviors in difficulty and enjoyment.

Source:
- https://ojs.aaai.org/index.php/AIIDE/article/view/27513

Ouros implication:
Patrol behavior should be a readable world property. Different institutions can secure spaces differently without giving guards arbitrary perception bonuses.

### Distractions change the search problem

AIIDE research on stealth games with distractions models guard-path changes caused by player-triggered events, including delayed or remote distractions.

Source:
- https://ojs.aaai.org/index.php/AIIDE/article/view/12872

Ouros implication:
A distraction should generate an observable event that a security actor may investigate according to its own knowledge and responsibility. It should not simply subtract points from a universal detection meter.

### Stealth paths depend on geometry and observers

Another AIIDE project analyzes stealthy paths based on the map, enemy motion, field of view and start/goal positions.

Source:
- https://ojs.aaai.org/index.php/AIIDE/article/view/12591

Ouros implication:
Minecraft geometry matters. If the eventual adapter cannot expose reliable visibility, observer position and navigation data, a tactical stealth simulation should not be faked in narrative code.

### Modern guard AI research emphasizes information and confidence

A 2025 AIIDE paper proposes an explainable guard framework using Information, Confidence and Connectivity maps and shows how distractions and environmental elements can integrate into guard behavior.

Sources:
- https://ojs.aaai.org/index.php/AIIDE/article/view/36819
- https://arxiv.org/abs/2508.18527

Reusable principle:
A guard should react to what it has reason to believe, not to hidden global truth. This aligns with Ouros’s existing actor-knowledge architecture.

## Derived Ouros design lessons

1. Infiltration should operate on observer knowledge, access and suspicion rather than a global hidden/detected Boolean.
2. A presented identity and a real identity must remain separate facts.
3. Security zones should have explicit access logic; uniforms or disguises alone should not unlock every door.
4. A cover can be partially compromised.
5. Detection is an event with a witness and evidence trail, not magical global knowledge.
6. Patrols need responsibility, route and knowledge state.
7. Successful stealth should meaningfully reduce risk or reveal information instead of being negated to preserve a planned battle.
8. Failed stealth should often create reroutes, questioning, lost access, alarms, pursuit or evidence rather than immediate combat.
9. Pokémon-assisted infiltration requires the individual Pokémon’s authoritative capability state.
10. Group infiltration needs coordinated cover and failure handling rather than one bad roll automatically invalidating the whole operation.
11. Social infiltration and physical concealment are different modes and may use different skills, information and risks.
12. Covert actions can leave traces that later feed cases, public memory, faction attention and counterintelligence.
13. Institutions can be infiltrated over time by NPC actors even while the players are elsewhere, but only through plans supported by access, knowledge and resources.
14. Counterintelligence must never grant factions omniscience.
15. Tactical stealth should wait for reliable engine/adapter support rather than duplicating PTU rules inside Minecraft scripts.

## Copyright and attribution boundary

This pass records source names, URLs and high-level structures only. It does not reproduce protected dialogue, scenes, maps, characters or plots from Pokémon games, animation, manga, fangames, fanfiction or roleplay threads. Original Ouros proposals derived from these patterns must use new institutions, locations, identities, conflicts and outcomes.

## Research gaps for later passes

- exact PTU/Caelo text for Stealth and Guile uses and opposed checks;
- exact Caelo modifications, if any, to stealth/social checks;
- exact PTU behavior of Invisibility, Dead Silent, Blender, Phasing and other relevant capabilities;
- Rogue, Ninja, Mastermind and other Trainer Feature interactions relevant to infiltration;
- whether current Python AutoPTU implements out-of-combat concealment as authoritative state or only stores the underlying character data;
- Minecraft/Cobblemon visibility, hearing, entity-awareness and disguise hooks;
- multiplayer privacy rules for cover identities;
- acceptable persistence and performance model for guard patrols in unloaded chunks;
- boundary between legitimate scouting and exploitative information extraction from the server.