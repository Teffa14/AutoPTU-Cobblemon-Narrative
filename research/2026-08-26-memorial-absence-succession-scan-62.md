# Narrative Research Scan — Pass 62

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-26

## Scope

This pass studies how Pokémon stories use graves, memorials, absence, mourning, remembered partners and institutional continuity without assuming that every disappearance means death or that every memorial claim is historically complete.

The target gap in Ouros is not another Public Memory system. The existing repository already models historical events, public records, living memory, commemoration, retired-character boundaries and legacy handoffs. The missing layer is operational continuity around absence and confirmed loss: what world state is allowed to change, what remains unknown, how memorial spaces stay active over time, and how institutions continue after a person or Pokémon is no longer present.

## Repository overlap review

Relevant existing ownership boundaries inspected before writing:

- `design/public-memory-event-legacy-layer.md` owns community interpretation, commemoration and legacy history.
- `design/archives-museums-collections-preservation-layer.md` owns records, collections and preservation.
- `design/care-recovery-welfare-layer.md` owns health, treatment and recovery rather than death assumptions.
- `design/case-authority-custody-layer.md` owns formal case/evidence/custody state where applicable.
- `design/material-culture-economy-crafting-layer.md` owns physical object provenance.
- `design/residential-life-household-relocation-layer.md` owns residence and occupancy continuity.
- `design/workplace-staffing-service-continuity-layer.md` and institution systems own staffing/role continuity.
- `design/rumor-testimony-local-knowledge-extension.md` owns informal claims and testimony provenance.

Pass 62 therefore focuses on absence state, confirmed-loss references, memorial-site continuity, remembrance practices and explicit handoffs to the systems above.

## Source 1 — PTU campaign-tone guidance

Source: Pokémon Tabletop United, Playing the Game / GM-tone guidance, community wiki transcription.

URL: https://pokemontabletop.fandom.com/wiki/Playing_The_Game

Useful high-level lesson:

PTU explicitly notes that Pokémon campaigns can support major defeats without permanent death and advises groups to establish setting assumptions with the GM instead of importing video-game expectations automatically. This is important for Ouros because a narrative generator must never create a death merely to produce dramatic stakes.

Reusable design rule:

- death is a world/canon fact, not a default consequence of losing a battle;
- disappearance, retirement, relocation, incapacitation and death remain distinct states;
- narrative continuity can preserve consequences without requiring permanent character loss;
- encounter design should not infer fatal outcomes from HP, fainting, defeat or missing presence unless the governing rules/canon explicitly establish them.

## Source 2 — Hau'oli Cemetery

Source: Bulbapedia summary of Pokémon Sun/Moon and Ultra Sun/Ultra Moon.

URL: https://bulbapedia.bulbagarden.net/wiki/Hau%27oli_Cemetery

Useful structures:

- people and Pokémon share a memorial landscape;
- visitors return for remembrance rather than because the location is a one-time dungeon;
- grief is expressed through observable behavior and personal history;
- an individual Pokémon may retain a relationship to a deceased Trainer's history without the story reducing that Pokémon to transferable property;
- the cemetery remains part of ordinary regional geography while also supporting wild Pokémon encounters.

Transformation for Ouros:

Create memorial sites as persistent civic/ecological places with access, visitors, upkeep, records and nearby wild activity. A surviving Pokémon's routines or object associations must be based on observed/canonized history, not species stereotype or ownership inference.

## Source 3 — Celestial Tower

Source: Bulbapedia summary of Pokémon Black/White and Black 2/White 2.

URL: https://bulbapedia.bulbagarden.net/wiki/Celestial_Tower

Useful structures:

- one site supports remembrance, ordinary traversal, NPC reflection and unrelated care activity;
- a small ritual action such as ringing a bell creates a repeatable interaction without needing a supernatural mechanical effect;
- a major character can revisit the site because of an old partner, connecting present characterization to prior loss;
- the same location can hold personal memory and regional public meaning.

Transformation for Ouros:

Memorial practices should be represented as authored or culturally documented acts. The system may record that an actor participated, visited, rang a bell, left flowers or maintained a marker. It must not invent buffs, spirit communication, supernatural truth or automatic emotional resolution.

## Source 4 — Mt. Pyre

Sources:

- Pokémon.com regional spotlight: https://www.pokemon.com/us/pokemon-news/remember-the-region-hoenn-spotlight
- Bulbapedia: https://bulbapedia.bulbagarden.net/wiki/Mt._Pyre

Useful structures:

- a memorial site can also be culturally guarded infrastructure;
- caretakers preserve traditions and objects over long periods;
- outside actors can exploit the importance of the site, creating conflict without making the graves themselves loot nodes;
- Ghost-type presence and memorial use coexist without proving that every ghost is the spirit of someone buried there.

Transformation for Ouros:

Memorial-site stewardship can generate maintenance, access, custody and security problems. Grave markers, offerings and protected objects require explicit ownership/custody rules before they can be moved, awarded or used. Nearby Ghost-type ecology never establishes identity with a deceased individual without canonical evidence.

## Source 5 — Lost Tower and regional burial grounds

Sources:

- Lost Tower: https://bulbapedia.bulbagarden.net/wiki/Lost_Tower
- Death/burial-ground overview: https://bulbapedia.bulbagarden.net/wiki/Death_in_the_Pok%C3%A9mon_world

Useful structures:

Pokémon settings repeatedly use dedicated resting places, memorial pillars, towers, mountains and shared cemeteries. The forms vary by region. This suggests memorial practice should not be globally standardized by the generator.

Transformation for Ouros:

- each region/settlement must define its own approved memorial forms;
- one area may use a cemetery, another a monument, archive, bell, garden, named route or private household practice;
- the absence of a grave does not imply disrespect or uncertainty;
- the presence of a marker does not prove the completeness of the story recorded on it.

## Source 6 — Pokémon Legends: Z-A cemetery rumor

Sources:

- Serebii: https://www.serebii.net/legendsz-a/sidemissions/asortascarycemeterystory.shtml
- Game8: https://game8.co/games/Pokemon-Legends-Z-A/archives/570867

Useful structure:

A cemetery rumor creates a compact investigation whose initial supernatural framing becomes narrower after direct observation. The useful pattern is not the exact quest solution. It is the separation between local story, conditions for investigation, direct encounter and revised interpretation.

Transformation for Ouros:

A memorial location can generate mysteries through conflicting observations, changed markers, access patterns, maintenance records or wild Pokémon activity. Resolution should narrow claims rather than automatically dismiss or confirm every related tradition.

## Source 7 — Pokémon Reborn, Simon/Tara continuity

Sources:

- Tara's Identity Sidequest: https://pokemon-reborn.fandom.com/wiki/Tara%27s_Identity_Sidequest
- Beryl Ward/Cemetery: https://pokemon-reborn.fandom.com/wiki/Beryl_Ward

Useful high-level structures:

- a memorial can exist even when physical remains are unavailable;
- incomplete identity information can become a later investigation;
- a character's role/faction affiliation can change after confronting loss;
- revisiting the same grave location can advance a personal arc over long spans of the game;
- the marker itself can change when new verified information becomes available.

Transformation for Ouros:

A memorial record may have `identity_confidence`, missing fields and later corrections. Updating a marker should create a provenance-preserving revision, not overwrite the earlier record. A character's decision to leave an organization must remain an explicit authored/canon event rather than an automatic grief outcome.

## Cross-source reusable patterns

### Persistent place, not one-shot dungeon

Memorial spaces work best when they remain available before and after dramatic scenes. Return visits can show upkeep, new markers, changed access, seasonal practices, revised records or different visitors.

### Observable practice instead of inferred emotion

Record what actors do: visit, maintain, speak publicly, decline a ceremony, leave an object, request a correction, avoid a place, take over a duty. Do not infer grief intensity, guilt, forgiveness, closure or spiritual belief without explicit evidence.

### Confirmed loss and unresolved absence must not collapse

A missing actor can be:

- temporarily unreachable;
- traveling;
- retired;
- relocated;
- missing under investigation;
- presumed dead by some actors;
- publicly reported dead;
- canonically confirmed dead.

Only the last state authorizes the narrative layer to treat death as fact.

### Memorial truth is layered

A marker may preserve:

- verified identity;
- public interpretation;
- a family/institutional claim;
- an incomplete name;
- a later correction;
- an intentional omission;
- disputed attribution.

The marker itself is evidence of commemoration, not automatic proof of every proposition written on it.

### Succession is a handoff, not inheritance inference

When an absent or deceased actor held a role, service, residence, Pokémon partnership, collection, item or obligation, Pass 62 should create a handoff question. It must not decide ownership, inheritance, guardianship, transfer or institutional succession without an existing rule/canon source.

### Wild Pokémon around memorial sites are ecology first

Ghost-type or other Pokémon near graves can create atmosphere and encounters. Their presence does not establish reincarnation, haunting, spirit identity or ritual effect. Those claims stay mythic, anomalous or unresolved unless canon explicitly promotes them.

## Originality transformation rules

This pass does not import:

- specific Pokémon characters;
- named graves, towers or memorial ceremonies;
- exact quest chains;
- dialogue;
- specific villain plots;
- Reborn character arcs;
- region-specific religious claims;
- resurrection mechanics;
- supernatural ghost identity assumptions.

It reuses only structural lessons: persistent memorial place, incomplete record, return visit, observable remembrance, identity correction, site stewardship, absence-state separation and role handoff.

## Mechanical guardrails

No memorial or loss state may automatically create:

- PTU status conditions;
- Injuries or death from battle defeat;
- morale bonuses/penalties;
- Loyalty changes;
- social Skill modifiers;
- Trainer Feature effects;
- Ghost-type encounters because someone died nearby;
- supernatural communication;
- resurrection;
- item inheritance;
- Pokémon ownership transfer;
- faction leadership transfer;
- property rights;
- legal presumption of death.

Where a combat occurs near a memorial site, tactical resolution must still use the permanent engine capability map and must not let Minecraft invent missing PTU rules.

## Pass-62 design direction

Recommended implementation focus:

1. explicit absence-state object;
2. canonical-death reference gate;
3. memorial-site and marker revision history;
4. remembrance participation events;
5. memorial stewardship/upkeep hooks;
6. unresolved-property/role/Pokémon handoff packets;
7. return-visit callbacks;
8. capability-aware encounters that protect fragile sites without making graves tactical loot.
