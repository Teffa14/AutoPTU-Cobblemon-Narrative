# Recurring Rival Agency and Progression Research Scan — Pass 186

Status: RESEARCH / PROVENANCE ONLY. NOT CANON.
Date: 2026-09-01

## Purpose

This pass examines recurring rivals as persistent people rather than repeating battle dispensers. The reusable problem is how a rival can train, travel, pursue private goals, change roles, help the player, oppose the player, become temporarily unavailable, and continue developing when no rematch is scheduled.

The scan deliberately avoids importing protected dialogue, distinctive characters, exact plots, teams, rewards, or battle rules. External sources supply structural inspiration only.

## Repository overlap check

The current Narrative repository already contains:

- a canon `RIVAL` questline family;
- canon dynamic progression for recurring NPC Pokémon;
- battle-institution challenge contracts, formal battle records, rematches, scouting boundaries and competitive standings;
- relationship and character questline families;
- institutional succession and professional development layers;
- public-memory and information-flow layers;
- persistent schedules, travel, field work and world-state continuity.

The missing seam is a dedicated persistent rival-state model connecting those systems. `battle-institutions-challenge-circuits-layer.md` records formal results and rematches, but it intentionally does not own a rival's life goals, offscreen work, changing competitive role, willingness to battle, or personal arc. `npc-pokemon-dynamic-progression-v1.md` scales battle-ready Pokémon but does not decide why the Trainer appears or what the Trainer is trying to achieve.

## Public sources reviewed

### Pokémon series: recurring rematches

Source: Bulbapedia, Rematch.
https://bulbapedia.bulbagarden.net/wiki/Rematch

Reusable structure:

- recurring rivals are not continuously battleable in one universal way;
- rematches can be tied to time, location, progression stage or postgame state;
- the same recurring character can remain relevant after the main confrontation because availability itself becomes world state.

Ouros lesson:

`RIVAL_EXISTS != RIVAL_AVAILABLE_FOR_BATTLE`.

Availability should come from schedule, current commitments, challenge contracts and world state rather than an always-on dialogue button.

### Nemona: experienced rival choosing a development lane alongside the player

Source: Bulbapedia, Nemona.
https://bulbapedia.bulbagarden.net/wiki/Nemona

Relevant high-level pattern:

- the character begins already highly accomplished;
- she raises a new team while accompanying the player's progression instead of pretending her prior competence disappeared;
- rivalry coexists with guidance and enthusiasm for other Trainers.

Ouros lesson:

A rival's competitive encounter profile can be deliberately scoped without rewriting their whole biography or competence. A strong Trainer can use a development roster, exhibition roster, teaching roster or formal-challenge roster when an approved contract supports it.

This does not authorize hidden level suppression or invented normalization. Ouros already has a canon dynamic-progression policy and AutoPTU remains authoritative for legal encounter construction.

### Cheren: rivalry becoming profession and institution

Sources: Bulbapedia, Cheren and Aspertia Gym.
https://bulbapedia.bulbagarden.net/wiki/Cheren_%28Gym_Leader%29
https://bulbapedia.bulbagarden.net/wiki/Aspertia_Gym

Reusable structure:

- a recurring competitor can later occupy a formal institutional role;
- their earlier competitive identity remains part of their history while their daily responsibilities change;
- their new role includes teaching, investigation and guidance in addition to battling.

Ouros lesson:

Rivalry should survive role transition without swallowing it. A former or current rival can become an instructor, official, researcher or faction worker and still preserve shared competitive history.

`RIVAL_HISTORY != CURRENT_JOB`.

### Silver: behavioral change visible through Pokémon and schedule

Source: Bulbapedia, Silver.
https://bulbapedia.bulbagarden.net/wiki/Rival_Silver

Reusable structure:

- character development is expressed through changed treatment of Pokémon and changed routine rather than a single confession scene;
- later training and rematch availability occur on specific days;
- competitive continuity remains after a meaningful behavioral shift.

Ouros lesson:

Rival development should be evidenced through observable actions, schedules, care decisions, public records and changed choices. The system should not infer private repentance, friendship or forgiveness from one battle result.

`BEHAVIOR_CHANGED != PRIVATE_MOTIVE_PROVEN`.

### Hugh: rivalry serving an independent objective

Sources: Bulbapedia, Hugh and Hugh's sister.
https://bulbapedia.bulbagarden.net/wiki/Hugh
https://bulbapedia.bulbagarden.net/wiki/Hugh%27s_sister

Reusable structure:

- the rival has a goal independent of defeating the player;
- battles can occur while the two characters also cooperate against a separate problem;
- completion of the rival's central objective changes what they do afterward instead of ending their existence.

Ouros lesson:

A rival needs an agenda graph that continues even when the player ignores them. Competitive encounters should intersect that graph, not replace it.

### Wally and long-gap payoff

Source: Bulbapedia, Wally.
https://bulbapedia.bulbagarden.net/wiki/Wally

Reusable structure:

- a rival can disappear for substantial stretches;
- later reappearance carries visible growth because the world did not freeze while the player was elsewhere;
- repeated rematches can occupy a stable later location.

Ouros lesson:

Absence can create payoff when offscreen progression is traceable. The rival does not need to appear every chapter to remain persistent.

### PTU campaign-log evidence

Source: r/PokemonTabletop campaign log #8.
https://www.reddit.com/r/PokemonTabletop/comments/n3iqr2/campaign_log_8/

The log describes a session in which the party fights recurring rivals before continuing toward the next city and Gym. It is anecdotal community evidence, not PTU rules authority.

Reusable lesson:

- rival encounters naturally coexist with travel, training, city arrival and other campaign activities;
- a rival battle can become exhausting if it has no concise narrative purpose or mechanical pacing budget;
- rivalry works better as one beat in a larger campaign rhythm than as mandatory repeated full fights.

Ouros implication:

Every proposed rival confrontation should state why this encounter exists now and what changes afterward. If nothing meaningful changes, compress, postpone or represent the contact without a full tactical battle.

### PTU community rival concept

Source: public PTU player request describing a campaign rival with a Fairy-type identity and persistent partner.
https://www.reddit.com/r/ICanDrawThat/comments/ud6zhc/can_someone_draw_my_pokemon_rival/

This is weak evidence and is used only for one broad pattern: tabletop players naturally make rivals memorable through a stable thematic identity and named partner rather than numeric difficulty alone.

Ouros implication:

A rival profile may preserve public style tags, recurring partner identities, known habits and authored values, but those tags cannot grant combat effects.

## Structural synthesis

A durable rival needs at least five independent tracks:

1. persistent person identity;
2. independent agenda and current activity;
3. competitive history with the player and other Trainers;
4. battle-eligible encounter profile governed by AutoPTU;
5. observable character development supported by world evidence.

These tracks must not collapse into a scalar affinity or win-loss counter.

## Important boundaries

`RIVAL != ENEMY`.

`RIVAL != FRIEND`.

`RIVAL != BATTLE_ON_DEMAND`.

`PLAYER_WIN != RIVAL_HUMILIATED`.

`PLAYER_LOSS != RIVAL_SUPERIOR_PERSON`.

`REMATCH_ACCEPTED != RELATIONSHIP_IMPROVED`.

`RIVAL_ABSENT != CONTENT_DISABLED`.

`RIVAL_POKEMON_LEVEL_SCALING != TRAINER_LIFE_PROGRESSION`.

`PUBLIC_BATTLE_RECORD != PRIVATE_EMOTION`.

`SHARED_GOAL != FRIENDSHIP_CONFIRMED`.

`ROLE_CHANGE != RIVAL_HISTORY_ERASED`.

`NPC_OFFSCREEN_PROGRESS != SECRET_AUTO_WIN`.

## PTU / Caelo cross-check boundary

The Narrative README names the project's PTU Core, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List as authoritative sources when available to implementation review.

The current AutoPTU repository contains mechanical and career content, but this pass did not locate an indexed Caelo-specific rule that defines a formal mechanical `Rival` condition, rivalry bonus, rivalry XP multiplier, automatic rematch reward or relationship effect.

Therefore this pass creates none.

The canon dynamic NPC Pokémon progression policy already states that recurring rivals can use a `rival` difficulty profile and that persistent Pokémon identity is separate from encounter-derived battle state. That policy is Ouros canon configuration, not evidence that PTU grants a special rival mechanic.

## Design lessons for Ouros

A recurring rival should be authored around questions such as:

- What are they pursuing when the player is absent?
- What would make them seek a battle today?
- What would make them refuse one?
- What can they accomplish without the player?
- What public evidence shows that they changed?
- Which shared events can turn competition into cooperation without forcing friendship?
- Which responsibilities can pull them away from the competitive circuit?
- Which battle memories can legally affect future scouting?
- Which changes require canon approval rather than automatic inference?

## Candidate implementation direction

The best immediate Marea anchor is Jace Orrin because canon already tags him for `Rival`, `Competitive`, `Relationship` and `Character` surfaces, gives him a fixed workplace, mentor, responsibilities and persistent companion, and explicitly says he seeks stronger competition.

A first slice should not canonize Jace as the player's personal rival. It should add non-canon candidates demonstrating how Jace can become a recurring competitive peer if play establishes that relationship.

## Provenance status

All external material above is inspiration only.

No copied dialogue, named external character, external plot, team composition, reward table, battle rule or setting fact is promoted into Ouros canon by this research file.
