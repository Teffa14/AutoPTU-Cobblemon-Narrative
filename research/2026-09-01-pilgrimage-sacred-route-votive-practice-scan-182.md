# Research scan 182 — pilgrimage, sacred routes and votive practice

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-01
Writable destination: Teffa14/AutoPTU-Cobblemon-Narrative

This scan explores recurring journeys to meaningful places, shrines, route traditions, offerings, ritual access and contested interpretations. It does not establish a religion, Legendary cosmology, supernatural truth, sacred geography or ritual rule for Ouros.

## Repository fit check

Existing Narrative layers already cover public festivals, archives, public memory, language/interpretation, memorials, route recovery, ecology, shared-resource access and institutional authority. No existing file located in the inspected repository tree or code search defines a dedicated pilgrimage/sacred-route/votive-practice architecture.

Therefore this pass focuses on a narrow seam:

- why people repeatedly travel to a meaningful place;
- what they do there;
- which parts are publicly observable practice;
- which explanations are historical claims or beliefs;
- how access restrictions interact with tradition;
- how practices evolve without proving their metaphysical interpretation.

## Public sources inspected

### Pokémon Gold/Silver/Crystal and HeartGold/SoulSilver — Bell Tower

Source: Pokémon Central Wiki, Bell Tower
https://wiki.pokemoncentral.it/Torre_Campana

Useful high-level structure:

- a place can be socially important because of an inherited relationship with a Legendary Pokémon;
- access can be restricted to selected people rather than functioning as an ordinary public dungeon;
- a tower can carry historical memory even while the entity associated with it is absent;
- a destination can remain meaningful because of continuity of expectation, custodianship and story.

Ouros extraction:

A meaningful destination can sustain recurring travel and gatekeeping without guaranteeing an encounter, blessing or supernatural event.

Rejected copying:

No Bell Tower, Ho-Oh cult, chosen-person test or Ecruteak history is imported.

### Pokémon Crystal / HeartGold and SoulSilver — Ilex Forest shrine

Source: Bulbapedia, Ilex Forest shrine
https://bulbapedia.bulbagarden.net/wiki/Ilex_Forest_shrine

Useful high-level structure:

- a physically small marker can carry large social meaning;
- different people may attribute different functions to the same place, such as good luck, protection or association with a particular Pokémon;
- the physical shrine can exist before a later game mechanic gives it a special event function;
- player/community interpretation can precede formalized mechanical use.

Ouros extraction:

`PHYSICAL_MARKER_PRESENT != METAPHYSICAL_FUNCTION_VERIFIED`

A marker may be important because people treat it as important. Server truth must preserve the difference between practice, belief and proven world effect.

### Pokémon Diamond/Pearl/Platinum — Celestic Town and ruins

Sources:
https://bulbapedia.bulbagarden.net/wiki/Celestic
https://bulbapedia.bulbagarden.net/wiki/Celestic_Ruins

Useful high-level structure:

- a settlement can organize part of its identity around preserving old traditions and material evidence;
- ruins, frescoes and local elders create several interpretive layers around the same history;
- later researchers or characters can offer theories without those theories becoming automatic objective truth;
- historical meaning can be embedded in a lived settlement rather than isolated in an adventure dungeon.

Ouros extraction:

Meaningful routes and destinations work best when custodians, residents, archivists, maintenance workers and visitors all interact with them for different reasons.

### Pokémon Sword/Shield — Crown Tundra and Crown Shrine

Sources:
https://bulbapedia.bulbagarden.net/wiki/Crown_Shrine
https://bulbapedia.bulbagarden.net/wiki/Calyrex_%28game%29

Useful high-level structure:

- public memory can weaken while physical monuments and stories remain;
- offerings or recurring customs can preserve a relationship even after participants no longer understand the original context;
- a community may maintain incomplete, distorted or partially forgotten versions of earlier events;
- built infrastructure can outlast active belief.

Ouros extraction:

A recurring practice should have revision history. Later generations may preserve an action while explaining it differently.

Rejected copying:

No harvest king, faith-powered Legendary, Reins of Unity or Calyrex equivalent is imported.

### Pokémon Ranger: Guardian Signs — temple missions

Sources:
https://www.pokepedia.fr/Temple_foudroy%C3%A9
https://www.pokepedia.fr/Temple_obscur
https://bulbapedia.bulbagarden.net/wiki/Mysterious_Temple

Useful high-level structure:

- one location can support repeated visits with different objectives;
- unlocking deeper access can be staged through prior tasks;
- the same physical complex can host route choice, switches, collection/capture objectives and a culminating confrontation;
- repeated temple visits can feel structurally different without changing the destination itself.

Ouros extraction:

A meaningful destination can support multiple episodes across seasons or relationship states. Progress should be tied to world state and permissions rather than arbitrary dungeon reset.

### PTU community — religion and legendary framing

Sources:
https://www.reddit.com/r/PokemonTabletop/comments/1sb2npg/help_me_with_my_worldbuilding/
https://www.reddit.com/r/PokemonTabletop/comments/10fgir6/ideas_for_elemental_shrine_trials/
https://www.reddit.com/r/PokemonTabletop/comments/15ryqex/making_a_campaign_need_help_and_ideas/

Observed community patterns:

- PTU GMs often make regional religious practice part of ordinary social rules and institutions;
- shrine trials are frequently used as alternatives to purely combat-based progression;
- groups often associate different communities with different powerful Pokémon or local myths;
- community advice repeatedly recommends building a temple around the kind of play it is meant to support rather than adding combat by default.

Use with caution:

These are community implementations and discussions, not PTU rules authority. They demonstrate playable narrative patterns only.

## PTU project cross-check

Read-only AutoPTU contains `audit_sources/Blessed and the Damned.txt`.

Relevant project evidence:

- the supplement contains explicit Legendary-domain, avatar, aura and campaign-framework material;
- it discusses worlds where powerful Pokémon can function as godlike entities;
- this confirms that PTU has optional material for campaigns where Legendary metaphysics are mechanically important.

However:

`BLESSED_AND_DAMNED_OPTION_EXISTS != OUROS_USES_THAT_COSMOLOGY`

Read-only AutoPTU also contains `audit_sources/Game of Throhs.txt`, including an alternative framework where Icons emerge from long-lived stories and belief.

Therefore the project contains more than one possible supernatural model. Narrative cannot silently choose between them.

No indexed Caelo source was located in the inspected repositories that establishes Ouros/Caelo religion, pilgrimage, shrine authority, Legendary worship, offerings, vows, sacred geography or divine intervention.

## Reusable design lessons

1. The journey itself can matter as much as the destination.
2. A route can have ordinary users and ritual users at the same time.
3. A practice can survive after its original explanation is forgotten.
4. Different residents may perform the same action for different reasons.
5. Custodianship does not imply theological authority.
6. Restricted access can be practical, ecological, historical or ritual; those reasons must remain distinct.
7. Offerings create physical aftermath: storage, decay, litter, theft concerns, return policy and cleanup.
8. A ritual object remains an ordinary tracked object unless PTU/Caelo mechanics explicitly grant an effect.
9. Repeated visits should reveal changing social context rather than replay the same scripted scene.
10. A Legendary encounter, if one ever becomes canon, must be exceptional evidence rather than the default explanation for why a tradition exists.

## Strong Ouros invariants suggested by the research

- `PRACTICE_OBSERVED != BELIEF_TRUE`
- `LOCAL_TRADITION != REGIONAL_RELIGION`
- `SHRINE_PRESENT != LEGENDARY_PRESENT`
- `OFFERING_PRESENT != BLESSED_ITEM`
- `RITUAL_ROUTE != ACCESS_OVERRIDE`
- `CUSTODIAN != PRIEST`
- `HISTORICAL_ORIGIN_CLAIM != VERIFIED_ORIGIN`
- `REPEATED_CORRELATION != DIVINE_CAUSATION`
- `NPC_REVERENCE != MECHANICAL_CLASS_FEATURE`
- `PLAYER_PARTICIPATION != CONVERSION_OR_BELIEF_STATE`

## Candidate gameplay loops

### Witnessed route

The player walks a known route with residents, records who stops where and what each person says the stop means. The useful output is attributed testimony and observed behavior, not one authoritative explanation.

### Practice under closure

A traditional route becomes temporarily unsafe or restricted. Residents debate postponement, rerouting or symbolic substitution. The interesting state is how practice adapts while physical safety authority remains separate.

### Material stewardship

A meaningful marker accumulates ribbons, stones, food, written notes or other objects. The episode concerns custody, weathering, cleanup and provenance. It should not require deciding whether any offering has supernatural effect.

### Tradition revision

Tideglass evidence contradicts one popular explanation of a recurring practice. The community can revise its public text while deciding whether the practice itself still matters.

## Anti-copy and anti-overreach boundary

This pass does not create:

- a Church of Arceus;
- a direct analogue of Bell Tower or Crown Shrine;
- an Ouros Legendary pantheon;
- a mechanically blessed pilgrimage item;
- a universal religious practice;
- a mandatory belief choice for the player;
- a supernatural proof event;
- a Caelo-derived religion without Caelo provenance.

The result is a reusable social-history architecture only.