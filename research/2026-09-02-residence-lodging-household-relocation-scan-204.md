# Residence, Lodging, Household and Relocation Research Scan — Pass 204

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02
Canon effect: NONE. This file does not establish Ouros housing law, tenancy, ownership, rent, household definitions or lodging rights.

## Research question

Ouros already has canonical homes, boarding rooms, work sites and settlement anchors. What reusable narrative structures let those facts become persistent residential continuity without inventing legal/economic rules or turning a Minecraft bed into authority over where a character lives?

This pass targets:
- assigned quarters and temporary lodging;
- persistent residence versus physical presence;
- room/bed allocation;
- household membership and guests;
- relocation and move-out history;
- stored personal effects and handover state;
- institutional accommodation;
- temporary displacement after route/service/crisis events;
- home-base evolution;
- privacy and access boundaries;
- world-state continuity when the player is elsewhere.

It intentionally does not define:
- rent or prices;
- leases;
- eviction law;
- ownership doctrine;
- inheritance;
- zoning;
- housing benefits;
- legal household status;
- healing from sleep;
- Pokémon storage/carrying capacity;
- Minecraft respawn mechanics.

## Existing Ouros context checked before research

Current canon already establishes:
- Mara has a boarding room near the Marea Field Office;
- Ivo lives on Puerto Bruma market street;
- Nerea has quarters at Estación Mirador;
- Taro has an archive residence room;
- Sela lives in the north boarding row;
- Puerto Bruma contains boarding rooms around market street;
- canonical Minecraft coordinates describe settlement/site anchors, but presentation state cannot rewrite canon;
- NPC identity persists independently of whether a Minecraft actor is loaded.

Recent design layers already cover rest/sleep, service queues, identity/credentials, duty handoffs, mutual aid, material custody and settlement continuity. No indexed dedicated residence/tenancy/lodging continuity layer was found. The new design therefore must reference those systems rather than duplicate them.

## Source 1 — Pokémon Legends: Arceus: assigned quarters in Jubilife Village

Source:
- Bulbapedia, "Player's house" / Hisui section: https://bulbapedia.bulbagarden.net/wiki/Player%27s_house
- Bulbapedia, "Jubilife Village": https://bulbapedia.bulbagarden.net/wiki/Jubilife_Village
- Bulbapedia, Legends: Arceus task list, Mission 1: https://bulbapedia.bulbagarden.net/wiki/Task_(Legends:_Arceus)

Observed structure:
- the protagonist receives specific quarters after entering an institutional/community relationship;
- the quarters are a persistent place with storage, clothing and rest affordances;
- assignment to the quarters is narratively distinct from simply standing in that building;
- the space remains a recognizable home base through subsequent expeditions;
- resting there can advance time in that game, but that gameplay rule belongs to Legends: Arceus and cannot be imported as PTU/Ouros rest mechanics.

Reusable lesson for Ouros:

`RESIDENCE_ASSIGNMENT != CURRENT_PHYSICAL_PRESENCE`

A character can have a recognized residence while working, travelling or unloaded from Minecraft. A room can remain assigned while empty. Institutional affiliation may explain why accommodation exists without proving ownership of the building.

Do not import:
- Galaxy Team institutions;
- Hisui settlement history;
- automatic time advancement;
- storage limits;
- free accommodation assumptions;
- game-specific healing/rest behavior.

## Source 2 — Pokémon Scarlet/Violet: home and academy dorm coexist

Sources:
- Bulbapedia, "Player's house": https://bulbapedia.bulbagarden.net/wiki/Player%27s_house
- Bulbapedia, Scarlet/Violet walkthrough, academy/dorm sequence: https://bulbapedia.bulbagarden.net/wiki/Appendix:Scarlet_and_Violet_walkthrough/Section_3

Observed structure:
- the player has a family home and also a dorm room at the academy;
- the two spaces serve different contexts without requiring one to erase the other;
- the dorm has persistent domestic functions and is attached to an institutional role.

Reusable lesson:

`PRIMARY_HOME != ONLY_VALID_ACCOMMODATION`

Ouros should allow a person to have a durable home reference plus temporary or institutional lodging. A Mirador work quarter, ferry bunk or field-school guest room need not overwrite a person's ordinary residence.

Do not import:
- Paldea academy governance;
- student housing rules;
- family assumptions;
- school benefits;
- free lodging.

## Source 3 — Pokémon Mystery Dungeon Rescue Team: base as persistent social infrastructure

Sources:
- Bulbapedia, "Team Base": https://bulbapedia.bulbagarden.net/wiki/Rescue_team_base
- Serebii, Rescue Team DX Base Camp: https://www.serebii.net/dungeonrescueteamdx/basecamp.shtml

Observed structure:
- the team base is a persistent home/operations anchor;
- mail and requests can arrive there while the protagonists undertake work elsewhere;
- the base can later be renovated, so physical presentation can change while identity/history persist;
- the home base accumulates visible history instead of functioning only as a teleport/menu location.

Reusable lessons:

`HOME_IDENTITY != CURRENT_BUILD_VERSION`

`ABSENT_RESIDENT != FROZEN_HOME_STATE`

A residence can receive deliveries, maintenance, notices or changes while its resident is away when other world actors plausibly perform those actions. Renovation should create versioned physical state rather than destroy residence history.

Do not import:
- Rescue Team characters;
- chestnut renovation plot;
- mailbox capacity;
- saving rules;
- species-shaped buildings.

## Source 4 — Pokémon tabletop community: player bases and settlement investment

Source:
- r/PokemonTabletop discussion, "I run a west marches TTRPG, and need help with city building mechanics" (2024-01-31): https://www.reddit.com/r/PokemonTabletop/comments/1afsyga/

Observed signal:
- Pokémon tabletop groups are interested in persistent bases, businesses, facilities and settlements as campaign state;
- community solutions vary heavily and often become homebrew resource systems;
- one cited approach abstracts Pokémon into permanently donated building resources.

Useful conclusion:
Persistent homes/bases are desirable campaign anchors, but Ouros should not turn Pokémon into fungible construction-resource tokens. Physical assistance by a Pokémon requires individual identity, consent/relationship context where relevant, and authoritative capability validation when mechanics matter.

## Source 5 — General tabletop home-base practice

Source:
- r/TTRPG, "What is your go to home base in your games?" (2025-06-04): https://www.reddit.com/r/TTRPG/comments/1l2wrxr/

Observed signal:
- tables commonly use inns before characters gain more permanent headquarters;
- persistent houses can accumulate improvements, caretakers and allies;
- the most valuable effect is continuity: a place becomes evidence of prior relationships and decisions.

Reusable lesson:
A home/base should produce story because actors, objects, messages and past decisions intersect there. It should not require a universal base-upgrade currency or mandatory property-management minigame.

## PTU / engine boundary check

Repository searches across AutoPTU-Java and AutoPTU for `lodging` and `hotel` returned no indexed implementation evidence in this run.

No indexed Caelo source content was returned by a literal `Caelo` repository search in Narrative, AutoPTU-Java or AutoPTU.

Therefore pass 204 cannot assert any PTU/Caelo mechanics for:
- housing cost;
- rent;
- lodging quality;
- sleeping capacity;
- household size;
- eviction;
- property ownership;
- residence registration;
- legal guest access;
- relocation time/cost;
- storage capacity;
- shelter bonuses.

PTU rest/healing remains a separate governed mechanical concern. A residential record cannot grant HP recovery, remove Injuries, restore AP, cure statuses or reset Move frequencies.

## High-level structures extracted

### Residence as a persistent relationship between actor and place

Useful record components:
- persistent residence ID;
- resident actor ID;
- location/site ID;
- accommodation type as descriptive content;
- assignment/start timestamp;
- current state;
- end timestamp when applicable;
- source/authority for assignment where known;
- access references;
- room/space reference;
- stored-property references without inventing ownership;
- current occupancy observation separate from residence status.

### Multiple simultaneous accommodation roles

A person may have:
- ordinary residence;
- institutional quarters;
- temporary lodging;
- field staging accommodation;
- emergency/displacement accommodation.

These records can overlap when context supports them. Do not collapse them into one `home_location` field.

### Household claims require evidence

Co-residence alone does not prove:
- family relation;
- romance;
- shared finances;
- guardianship;
- ownership;
- permanent household membership.

Ouros already protects surname/relationship inference. Residential state should follow the same discipline.

### Moving is a process, not a teleporting fact

A relocation can preserve:
- notice/decision provenance;
- packing/preparation state;
- transport/custody of selected possessions;
- room handover;
- old-address validity window for messages;
- arrival/settling state;
- later corrections if the move is delayed or cancelled.

No universal duration or cost is proposed.

### Lodging state can create ordinary stories

Strong low-stakes hooks:
- a room remains assigned after a schedule changes;
- a visitor's booking ends before their work does;
- a personal package reaches an old lodging location;
- two legitimate records disagree about which room is available;
- repairs make one room temporarily unusable;
- someone temporarily stays near a work site without changing their permanent home;
- a resident moves but a public directory remains stale;
- a displaced resident returns after a repair/reentry decision.

## Originality boundary

This pass copies no protected plot, dialogue, distinctive character or setting. External material supplies only structural lessons: assigned quarters, concurrent home/dorm contexts, persistent bases, renovation history and campaign use of home bases.

## Research conclusion

Ouros benefits from treating residence as durable world state with provenance, dates and purpose. That gives the existing boarding rooms and canonical homes practical meaning while preserving strict boundaries around law, money, family and PTU recovery mechanics.

Recommended implementation direction: a small `residence_lodging_continuity` layer that can represent ordinary home, temporary room and relocation history independently from Minecraft bed ownership or entity position.