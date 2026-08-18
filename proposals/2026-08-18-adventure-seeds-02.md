# Ouros Adventure Seeds — Pass 02

Status: NON-CANON proposals. Original structures derived from cross-source research. Names are placeholders until canon review.

## Seed H — The Work That Finds You

### Core idea

Ouros settlements maintain visible and invisible request networks. Some jobs are posted publicly. Others only appear because a player has earned trust, witnessed something, made a promise or possesses a useful Pokémon capability.

### System behavior

A request has:
- requester;
- motive;
- causal world state;
- required trust/access;
- expiration or persistence policy;
- destination;
- likely activity profile;
- consequence outputs.

### Why it helps the world

Two players standing in the same town may see different opportunities because their history differs. The town therefore behaves like a social system rather than a static quest kiosk.

### Example pattern

A bridge repair request is public.
A missing-courier investigation appears only to players trusted by the local transport office.
A researcher privately requests help after noticing that a player's Pokémon has a traversal capability relevant to a sealed ravine.

No exact PTU capability is assigned until rules validation.

## Seed I — The Expedition License

### Core idea

Some dangerous ruins, reserves, mines, industrial zones and ecological crisis areas require occupational trust or permits.

The player can earn access through professions, organizations, local reputation or emergency circumstances.

### Design purpose

Access gates become worldbuilding rather than arbitrary level walls.

A gate can be opened by:
- recognized profession rank;
- sponsorship from an NPC/faction;
- completing preparatory work;
- proving a required capability;
- emergency override;
- discovering an unofficial route with different risks.

### Important constraint

The system should rarely reduce this to “your number is too low.” It should explain why the world restricts access.

## Seed J — The Second Route Through

### Core idea

Major dungeons should support at least two meaningful traversal approaches whenever geography allows it.

Potential approaches:
- direct hazardous path;
- longer safe route;
- capability-enabled route;
- machinery restoration;
- social access through an occupying faction;
- hidden route discovered through investigation.

### Consequences

Routes may change:
- encounter ecology;
- who notices the player;
- which clues are found;
- resource cost;
- time pressure;
- later dungeon state.

The goal is not to make every route equivalent. The choice should reveal player priorities.

## Seed K — Rescue Chain

### Core idea

A rescue job can escalate organically without becoming a scripted “three-stage quest.”

State chain example:
1. A traveler fails to return.
2. Search evidence indicates environmental trouble rather than a villain.
3. The expedition locates multiple affected Pokémon and people.
4. Players must choose what to stabilize first.
5. The original rescue resolves, but the cause becomes a new world-state problem.

### Possible follow-ups

- ecological investigation;
- infrastructure repair;
- faction blame dispute;
- rare migration event;
- dungeon opening caused by terrain shift.

This lets simple jobs discover larger arcs without pretending every missing-person mission was secretly a conspiracy.

## Seed L — Rival by Profession

### Core idea

Not every rival wants to beat the player in a League battle.

Potential rivalries:
- two researchers competing to publish a discovery;
- two rescue teams racing to a crisis;
- couriers competing for a prestigious contract;
- ruins surveyors disputing methodology;
- ecological wardens with conflicting intervention philosophies;
- contest performers chasing the same sponsor;
- bounty/investigation teams pursuing the same target.

### Memory

The rival remembers results beyond victory/defeat:
- who found the clue first;
- who protected civilians;
- who took credit;
- who shared information;
- who broke protocol;
- who saved the rival;
- whose interpretation proved correct.

A later Pokémon battle can become one expression of the rivalry rather than its entire identity.

## Seed M — The Breathing Dungeon

### Core idea

A dungeon has three time scales.

Immediate state changes during one expedition:
- doors;
- switches;
- hazards;
- defeated guards;
- temporary water levels.

Persistent state after the expedition:
- opened shortcut;
- repaired structure;
- removed resource;
- rescued inhabitant;
- faction displacement.

Slow background state between visits:
- wild Pokémon migration;
- faction occupation;
- flooding/drying;
- reconstruction;
- scavengers arriving;
- new research team entering.

### Return rule

A return visit should ask “what happened here since last time?” before spawning content.

## Seed N — The Rumor Gradient

### Core idea

Rumors should degrade and mutate according to distance and witness reliability rather than acting as omniscient quest markers.

A Chronicle event can generate multiple rumor forms:
- eyewitness fact;
- second-hand report;
- faction propaganda;
- frightened exaggeration;
- commercial spin;
- academic hypothesis.

### Player use

Investigation compares claims against evidence. Rumors can point toward real content without being guaranteed truth.

### Data principle

Store rumor claim separately from canonical fact.

```yaml
rumor:
  rumor_id: null
  origin_event_id: null
  speaker_id: null
  claims: []
  confidence: 0
  distortion_tags: []
  propagation_locations: []
```

## Seed O — Faction Fronts

### Core idea

A faction should be visible through what it does to places before players are asked to read a lore dump.

Faction fronts are active pressures such as:
- recruitment;
- resource acquisition;
- protection rackets;
- conservation work;
- research expeditions;
- smuggling;
- public aid;
- propaganda;
- sabotage;
- territorial defense.

### World-state use

A faction front attaches to a location and advances while supported by world state. Players can assist, oppose, redirect, expose or ignore it.

### Important design constraint

Ignoring a front should not always mean “the bad guys win.” Some fronts collapse from internal problems, competing factions or ecological conditions. The world should have agency outside the player.

## Seed P — Expedition Loadout as Story Choice

### Core idea

Preparation before a dungeon or field mission should matter narratively.

The party may receive imperfect information and choose what to prioritize:
- traversal support;
- medical supplies;
- capture resources;
- research equipment;
- weather protection;
- extra inventory capacity;
- social credentials;
- emergency extraction.

### Consequence

Preparation changes which problems are easy, costly or impossible during the expedition, but should not create arbitrary instant failure.

Exact item effects remain a mechanics-design task.

## Seed Q — Failure Leaves a Scar

### Core idea

When a meaningful mission fails, the system records the new world state and does not simply reset the quest.

Possible scars:
- target relocates;
- local trust drops;
- rival gains credit;
- route becomes more dangerous;
- faction front advances;
- settlement loses a service temporarily;
- Pokémon population disperses;
- clue becomes harder to obtain.

A recovery arc can later emerge from that state.

### Guardrail

Do not use permanent punishment for every failure. Some failures should be small, funny or recoverable. Scar intensity should reflect stakes established before the choice.

## Seed R — The Commons

### Core idea

Every major settlement has at least one highly reusable social space that changes with world state: market, guild hall, research station, harbor, plaza, shelter, café, training yard or similar.

### Function

The Commons can surface:
- rumors;
- recurring NPCs;
- profession work;
- faction presence;
- player-created callbacks;
- seasonal events;
- changed services;
- consequences from nearby adventures.

This gives procedural and authored stories a stable physical anchor in Minecraft.

## Mechanical/canon questions from this pass

- Which professions belong in Ouros canon, and which are only generic design categories?
- Which Pokémon capabilities can be safely exposed as overworld traversal hooks through AutoPTU/Cobblemon?
- How should mission access interact with Trainer Level, badges and Caelo-style restrictions?
- Which failure states may alter encounter populations automatically?
- How should rumors be shared across multiplayer players who witnessed different facts?
- Which dungeons are handcrafted Minecraft spaces versus stateful templates applied to reusable structures?
