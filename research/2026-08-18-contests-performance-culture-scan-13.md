# Contests, Performance Culture & Creative Circuits — Research Pass 13

Status: research and provenance only. Not Ouros canon.

## Scope

This pass focuses on a dimension not yet modeled as its own system in Ouros: Pokémon Contests, staged performance, creative careers, touring circuits, audiences, venues, rehearsal, show production, performer rivalries and public reception.

The repository already has public events, festivals, clubs, social bonds, travel, material culture and persistent institutions. This pass avoids duplicating those systems. It studies what happens when performance itself becomes a durable gameplay path rather than a decorative side activity.

## PTU / Caelo grounding

The supplied PTU 1.05 material already contains a full Contest subsystem. It defines five Contest Stats — Cool, Tough, Beauty, Smart and Cute — and separates a Contest into Introduction and Performance stages. Appeal Points determine the winner, Fumble Points reduce final Appeal, Moves have Contest Types and Contest Effects, and the rules include variants such as Festivals. These mechanics are authoritative for future PTU implementation and should not be replaced by rules taken from the video games.

Public reference mirror used only for locating the same PTU 1.05 material:
https://anyflip.com/deia/psdg/basic/251-300

The supplied Caelo Player's Guide treats Contest as a distinct activity category alongside Social, Wild Encounter, PvP, Job, Raid, Gym and Dojo. Caelo also connects Contest Hall Circuit success to Trainer progression. Therefore Ouros can support a serious non-battle career path without inventing a second progression framework.

## Source observations

### Pokémon Brilliant Diamond / Shining Pearl — Super Contest Shows

Official source:
https://diamondpearl.pokemon.com/en-au/features/

The official game presents Super Contest Shows as cooperative public performances involving four performers and their Pokémon. Evaluation is split into visual presentation, dance and move use. Success can depend on the combined energy of the entire show rather than treating every participant as purely adversarial.

Reusable structures:
- performance can contain multiple evaluated dimensions;
- a public show can mix individual excellence with collective success;
- visual preparation, timing and a chosen Pokémon move can all matter for the same event;
- ranks and categories create a recognizable circuit without requiring combat progression.

Do not import BDSP scoring into PTU. The reusable value is the structure of a layered public performance.

### Anime Contest circuit and Grand Festival

Official episode reference:
https://www.pokemon.com/uk/animation/seasons/13/episode-19-coming-full-festival-circle

Secondary structural reference:
https://bulbapedia.bulbagarden.net/wiki/Grand_Festival

The anime treats coordinating as a sustained career. Local Contests feed into a regional Grand Festival, recurring rivals meet again after earlier competitions, and a final event has greater social meaning because qualification required prior accomplishments.

Reusable structures:
- local events can form a season-long or year-long circuit;
- repeat encounters create professional rivalries distinct from hostility;
- qualification history makes a finale meaningful before the event begins;
- major festivals can mix performance and competitive confrontation while preserving a performer identity distinct from ordinary battlers;
- host locations can change, making travel and preparation part of the career.

### Pokéstar Studios — performance as scenario play

Reference:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9star_Studios

Additional design analysis:
https://www.smogon.com/smog/issue23/pokestudios

Pokéstar Studios turns familiar Pokémon actions into staged film scenarios. A participant follows a role, receives scenario constraints, makes dialogue choices and can achieve different endings. The result is then viewed as a produced film, and repeated success builds public recognition.

Reusable structures:
- familiar mechanics can support a different objective when framed by a production;
- performance scenarios can have success conditions other than defeating an opponent;
- scripts and roles create constrained creativity rather than unrestricted freeform play;
- rehearsal or rental setups can teach an activity before the player risks their own resources;
- released work can become an object in public memory;
- fame can result from a body of work rather than a single victory.

Do not reproduce Pokéstar film scripts, characters or unique scenarios.

### Pokémon Essentials community — modular Super Contest implementation

Source:
https://www.eeveeexpo.com/resources/1423/

A public Pokémon Essentials implementation breaks the Super Contest experience into reception, staging, dress-up, dance, acting/move evaluation, opponent configuration, winner announcement and rewards. The implementation problem itself is instructive: staged content benefits from explicit phases and authorable performer data.

Reusable structures:
- a show should be represented as stateful phases rather than one monolithic minigame;
- venues need participants, judges/hosts, audience state and backstage state;
- performers can have authored identities and specialties;
- results can create persistent awards and visible history.

### Public Pokémon Contest roleplay

Pokémon Roleplay Contest guideline:
https://www.tapatalk.com/groups/pokemon_roleplay/guideline-contests-t6.html

Pokécharms Grand Festival discussion:
https://forums.pokecharms.com/threads/the-grand-festival-discussion.16136/

Serebii Coordinator Adventures RP:
https://forums.serebii.net/threads/pok%C3%A9mon-coordinators-adventures-rated-g.572804/

Lake Valor Road to the Grand Festival:
https://lakevalor.net/threads/pokemon-the-road-to-the-grand-festival-kanto-signup-and-discussion.24523/

These community works repeatedly use Contests as an alternative journey structure. Common patterns include moving from town to town, recurring competitors, training between events, themed appeals, visual rounds, performance-focused battles and a prestigious final competition.

Reusable structures:
- a career can generate travel naturally;
- downtime between events is fertile space for training, friendships, rumors and side stories;
- a contest schedule provides shared rendezvous points for characters who otherwise travel separately;
- judging criteria create meaningful creative constraints;
- rivals can coexist as friends, collaborators, mentors or competitors;
- a performer journey can intersect villain plots or regional events without reducing the career to a combat route.

Community-specific rules, characters and plots are not imported.

## Design lessons for Ouros

### Performance needs its own persistent objects

A contest or show should not exist only as a temporary quest flag. Useful persistent entities include:
- venue;
- event edition;
- circuit;
- performer profile;
- act/routine;
- production;
- audience segment;
- judge/host role;
- award or ribbon instance;
- rehearsal record;
- public reception record.

### Creative careers should not collapse into generic reputation

A performer can be famous without being trusted, politically powerful or respected by researchers. The world should distinguish:
- audience recognition;
- peer respect;
- venue/institution standing;
- artistic identity;
- reliability as a collaborator;
- controversy or polarizing reception.

These are narrative states, not PTU bonuses.

### Audience is state, not a thousand simulated NPCs

Minecraft does not need to spawn every spectator. A venue can maintain aggregate audience state such as expected attendance, local enthusiasm, visiting supporters, faction interest or press presence. A limited number of representative NPCs can embody that state physically.

### The same event can support several player roles

A public show can generate content for:
- performer;
- coordinator;
- stage crew;
- artisan/costume maker;
- photographer or chronicler;
- researcher documenting Pokémon behavior;
- security/rescue staff;
- merchant;
- organizer;
- fan or social participant.

This makes performance culture useful even for characters who never enter a Contest.

### Failure should create career state rather than erase content

A lost Contest can create:
- a new rival;
- an invitation to train;
- a changed routine;
- criticism;
- a fan who appreciated the performance anyway;
- a rematch opportunity;
- a damaged or improved professional relationship;
- a new artistic direction.

The generator should not treat failure as a dead end.

### Public reception is not objective truth

Judges can issue formal results. Audiences, critics, clubs and NPCs can still disagree about what they liked. The system must distinguish official placement from subjective reaction.

## Cross-system connections

Performance culture should connect with existing Ouros layers rather than duplicate them.

Public memory:
- winners, memorable acts and controversial judging can become historical records.

Travel:
- a circuit creates calendar-based travel demand and seasonal routes.

Settlements:
- successful venues can increase visitors and service activity.

Material culture:
- costumes, props, stage equipment, crafted accessories and souvenirs can have provenance.

Social bonds:
- mentors, partners, rivals and troupe members accumulate shared history.

Clubs:
- schools, rehearsal groups and fan clubs can exist as persistent institutions.

World agency:
- factions may sponsor, boycott, protect or exploit public events.

Crisis layer:
- events can be postponed, relocated or converted into relief activity when real world state demands it.

Wild ecology:
- loud events, crowds, lighting and temporary infrastructure may affect nearby wildlife only when a causal model supports it.

## Mechanical boundary

Do not import official-video-game Contest scoring into AutoPTU.

Do not invent:
- Appeal dice;
- Contest Stat changes;
- Fumble effects;
- Contest Effects;
- Poffin effects;
- judge modifiers;
- Ribbon requirements;
- Contest rewards;
- Training features;
- Coordinator class benefits;
- Move legality;
- performance battle rules.

All such mechanics must come from the supplied PTU/Caelo rules and the eventual AutoPTU Contest implementation.

## Research opportunities for later passes

- inspect whether AutoPTU currently contains any Contest subsystem at all;
- map every PTU Contest Effect to required engine data;
- extract Caelo-specific Contest Hall procedures and rewards;
- research Pokémon Musicals, Pokéathlon, showcases and other non-battle disciplines as separate cultural traditions rather than merging all of them into Contest;
- study touring artist, theater-company and sports-league scheduling for multiplayer event orchestration;
- define how recorded performances become public-memory artifacts without storing copyrighted external media.
