# Introduced-species management legacy research — Pass 325

Status: RESEARCH / PROVENANCE, NOT CANON
Date: 2026-09-07

## Purpose

Find reusable structures for Ouros in ecological conflicts where a species, intervention or management policy was introduced to solve an earlier problem and remains part of the landscape after conditions change. The target is a persistent social-ecological arc, not another single-sensor environmental mystery.

## Repository duplication check

The recursive repository inventory and code-search index were inspected before authoring. Searches for invasive, introduced, biological control, biocontrol, eradication, translocation and population-control workstreams returned no dedicated existing Ouros pass. Recent work already covers hydraulic works, acoustic masking, artificial light, olfactory traces, geomagnetic navigation, reclaimed extraction landscapes, fire mosaics, floodplains, phenology, snowpack and intertidal access. Pass 325 therefore opens a distinct management-history and stakeholder-conflict domain.

Canon governance remains unchanged: research is evidence; proposals are candidates; design defines architecture; only `canon/` establishes approved Ouros world facts.

## Public source findings

### National Park Service — invasive-species treatment is site- and objective-specific

Source:
- https://home.nps.gov/yose/learn/nature/invasive-treatment.htm

Reusable structure:
- management priorities depend on ecological impact and local context;
- manual, mechanical, chemical and biological approaches have different trade-offs;
- an intervention that works in one feature may be inappropriate in another;
- protection zones, wetlands, archeological sites and traditional-use areas can constrain otherwise legitimate treatment;
- repeated treatment can itself create disturbance that changes future conditions;
- some widespread problems may no longer be practically controllable at whole-landscape scale, shifting work toward local protection goals.

Ouros transformation:
A management plan should contain feature-scoped objectives, permissions, evidence thresholds and review dates. Characters can disagree about the correct intervention without one side being corrupt or irrational. A successful local treatment does not prove that the same action is valid region-wide.

Do not import real herbicides, release protocols, safety guidance or real-world treatment thresholds as gameplay instructions.

### National Park Service — biological control requires caution and long-term evaluation

Same NPS source above.

Reusable structure:
Biological control is presented as a potentially long-lived management intervention whose agents require careful selection and testing because non-target effects matter.

Ouros transformation:
A past institution may have introduced a Pokémon, organism or ecological partnership under a formal management charter. Decades later, descendants, changed habitat, new land use and incomplete institutional memory can make the original justification insufficient for current policy. The story should ask what the intervention became, not merely whether it originally worked.

No real biological-control procedure is translated into an Ouros implementation recipe.

### USGS — disturbances can change the effectiveness and trajectory of ongoing control

Source:
- https://www.usgs.gov/publications/simulation-post-hurricane-impact-invasive-species-biological-control-management

Reusable structure:
Ecological management occurs inside a changing system. Major disturbances can alter both target populations and the performance or distribution of control agents. Long-running control therefore benefits from monitoring and model revision instead of assuming yesterday's relationship is permanent.

Ouros transformation:
A storm, fire, new road, land-use change or habitat recovery can invalidate the spatial assumptions of an old control program without invalidating every historical observation. Management records need temporal provenance.

### Pokémon franchise precedent — Yungoos as an introduced control species

Sources:
- archived contemporary Pokémon Sun/Moon information reproduced at https://www.nintendo-insider.com/yungoos-and-pikipek-revealed-in-pokemon-sun-and-moon/
- current official species page: https://www.pokemon.com/es/pokedex/yungoos
- corroborating Alola Pokédex documentation: https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Alola_Pok%C3%A9dex_number_in_Pok%C3%A9mon_Sun_and_Moon

Source boundary:
The 2016 Pokémon promotional description states that Yungoos was not native to Alola and was brought there to address an explosive population of another Pokémon. Current official Pokédex material describes Yungoos as following repeated food-search routes and gives its ordinary franchise flavor and Abilities.

Reusable structure:
Pokémon canon itself supports the premise that people deliberately move a Pokémon population for a management objective and that the introduced population can later become an ordinary part of regional life.

Ouros transformation:
Use this only as permission for the broad ecological-management premise. Do not copy Alola, Rattata/Yungoos history, Hawaiian inspiration, exact species relationship or outcome. An Ouros proposal should invent its own region, species, institutional history, motives and consequences.

Mechanical boundary:
Official Pokédex behavior is not a PTU/Caelo contract. Do not infer tracking bonuses, predator AI, Stakeout behavior, feeding requirements, encounter schedules, control effectiveness or population simulation rules from flavor text.

### Pokémon Tabletop United campaign retrospective — Tales of Visiwa

Source:
- https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Source type: PTU developer/community retrospective of a completed long-running campaign.

Reusable structures:
- a custom region can support multiple institutions and factions with distinct agendas;
- character relationships, public reputation, research, exploration and combat can affect one another across a long campaign;
- a confrontation can be redirected by non-combat information or persuasion instead of ending only through damage;
- recurring consequences become memorable when earlier character choices return in later contexts;
- the retrospective explicitly notes substantial GM prep/crunch, supporting Ouros's preference for reusable state contracts rather than bespoke bookkeeping per quest.

Ouros transformation:
The new management arc should recur through reports, hearings, field work, local jobs, revised access, stakeholder trust and optional battles. No Visiwa characters, factions, supernatural plot, dialogue, custom Pokémon or encounter sequences are copied.

### PTU living-world community — Super Pokémon Online

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/1mkct0y/super_pok%C3%A9mon_online_ptu_living_world_rpg/

Source type: community description, not rules authority.

Reusable structure:
The server explicitly advertises a world where economy, discovered locations and reputation change through player actions. This supports a design goal already central to Ouros: management outcomes should alter jobs, access, reputation and later NPC agendas rather than terminate at quest completion.

No server-specific setting, guild, character or story material is imported.

## Reusable Ouros design lessons

### Intervention history is durable state

Store why an intervention began, who authorized it, what evidence supported it, what geography it covered, what review conditions were promised and what later events changed the context.

`PAST_JUSTIFICATION != CURRENT_JUSTIFICATION`

### Population identity and management classification are separate

A population can be long-established socially while still being classified as introduced by an institution. Conversely, a population labeled harmful in an old file may no longer present the same current impact.

Do not let a label substitute for current evidence.

### Management conflicts should operate by feature and objective

Possible objectives include protecting a nursery, keeping a food store secure, preserving a corridor, preventing infrastructure damage, maintaining a cultural site or protecting another population. The same species may be tolerated in one feature and actively excluded from another.

### Descendants are not historical decisions

Individual Pokémon alive now did not personally make the institutional decision that placed their ancestors in the area. NPC ethics and policy should distinguish current individuals from historical responsibility.

### Institutions can remember badly without anyone lying

A shortened public notice, inherited work order, oral explanation and archived charter can preserve different slices of the same intervention. The global NPC knowledge system should carry those as separate claims with provenance.

### Review should create new decisions, not erase old ones

If a management policy changes, preserve the earlier authorization and its consequences. A revised plan can narrow, suspend, expand or replace it while maintaining historical traceability.

### Failure can become the next story state

An unsuccessful exclusion attempt can shift feeding routes. A successful local treatment can push pressure toward another feature. A compromise can produce monitoring obligations. A delayed decision can change jobs, prices, access or trust. None requires a binary quest reset.

## PTU / Caelo cross-check boundary

The current narrative source registry exposes `sources/kairos` only. No adopted `sources/caelo` directory was visible in the inspected tree. Kairos remains comparative evidence and a routing aid, not automatic Ouros law.

Pass 325 therefore does not author population-control mechanics, capture permissions, encounter-rate modifiers, hunting/tracking bonuses, territorial AI, forced relocation, custom Trainer Feature privileges, species-specific feeding systems, Ability effects, Item effects or Move effects.

If a future full encounter uses ordinary PTU combat, its legal actions remain owned by AutoPTU. Any specialized ecological or control mechanic must be verified against the adopted PTU/Caelo source before implementation.

## Research-to-content candidates

Primary candidate:
`Borrowed Teeth, Permanent Roots`

Core premise:
A management program introduced a Pokémon population generations ago to protect a productive district from another recurring problem. The original target pressure has shifted, but the introduced descendants now occupy routes, work yards and habitat edges that multiple groups rely on differently. An old management charter is still being cited as if its original scope automatically decides the present dispute.

Secondary candidates:
- a nursery where an exclusion program protects eggs but displaces pressure toward a market district;
- a restored wetland where an old control species is now part of a food web that did not exist when the program began;
- a cargo depot whose historical pest-control contract conflicts with a newer wildlife corridor;
- a farming cooperative whose buyer standards, habitat agreement and old management plan create incompatible obligations;
- a public hearing where every faction has valid evidence but refers to a different feature, time window or management objective.

All remain research-level until separately proposed or canon-approved.