# Research Scan — Temporary Visitors, Lodging, Hosting, and Repeat Travel — Pass 193

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-01
Canon effect: NONE. This file does not establish new Ouros facts.

## Research question

How can Ouros make temporary visitors, overnight stays, repeat travelers, visiting specialists, and guest Pokémon feel persistent without turning arrival into residency, creating a generic hotel system, or granting outsiders automatic access to local institutions?

This pass was selected after inspecting the repository tree, all current files in `canon/`, recent continuity layers, and code-search results for `guest`, `visitor`, `lodging`, `hospitality`, `temporary resident`, and related terms. No existing dedicated visitor/hosting continuity layer was found.

## Existing Ouros anchors that constrain this research

Current canon already establishes:

- Puerto Bruma has boarding rooms around Market Street.
- Mara Veyra lives in a boarding room near the Field Office.
- Sela Orrin lives in the north boarding row.
- Lia Morn records ferry arrivals/departures.
- Mina Cors operates short coastal ferry runs.
- Ivo Serrat is explicitly positioned as a later bridge into food, hospitality, and festival arcs.
- Ferry traffic connects Puerto Bruma outward, but no external destination is canonized yet.
- Marea Field Office coordinates practical assistance and is not a police force.
- Tideglass, Mirador, the cooperative, and the Battle Yard each retain their own authority over their work.

Therefore this pass may propose temporary-presence architecture, but it may not silently add a hotel, border service, immigration regime, named external settlement, accommodation tariff, or regional lodging law.

## Source 1 — Kalos hotels and rotating travelers

Source: Bulbapedia, `Kalos hotels`
https://bulbapedia.bulbagarden.net/wiki/Kalos_hotels

Relevant high-level structure:

- several hotels host travelers who rotate among towns on a regular cycle;
- the same traveler can be encountered at different locations on different days;
- repeated encounters reveal more of that person's personality over time;
- temporary presence does not require the traveler to become a permanent resident;
- lodging locations become social connectors between settlements rather than isolated rest menus.

Reusable Ouros lesson:

A visitor can have persistent identity, prior-contact history, an itinerary claim, and recurring appearances while remaining transient. Repeated contact should survive departure. Location changes should follow recorded travel rather than teleporting the same NPC because the player changed chunks.

Do not import:

- Kalos's exact six-day rotation;
- hotel room layouts;
- gifts or ribbons;
- the named travelers;
- hotel ownership or prices.

## Source 2 — Couriway / Ambrette traveler continuity

Sources:
https://bulbapedia.bulbagarden.net/wiki/Couriway_Town
https://bulbapedia.bulbagarden.net/wiki/Ambrette_Town

Relevant structure:

The rotating guests are absent from one hotel because they can be present at another. Conversation continuity follows the person across locations.

Reusable Ouros lesson:

`NOT_HERE != GONE_FROM_WORLD`.

A visitor who left Puerto Bruma may still exist in transit or at another known destination once that destination is canonized. Their absence should not reset relationship, knowledge, unresolved errands, or previous observed state.

## Source 3 — Hotel Richissime

Source: Bulbapedia, `Hotel Richissime`
https://bulbapedia.bulbagarden.net/wiki/Hotel_Richissime

Relevant high-level structure:

The same lodging venue can support sleeping and ordinary work such as room service, bed preparation, and lost-property handling.

Reusable Ouros lesson:

Hosting can create mundane labor, handoffs, mistakes, found objects, food preparation, schedule pressure, and service continuity. A visitor system therefore does not need to be a passive 'sleep and heal' menu.

Do not import:

- luxury-hotel framing;
- wages;
- exact tasks;
- room-service mechanics;
- lost-and-found rewards.

## Source 4 — Alola roadside motel and changing occupancy

Source: Bulbapedia, `Alola Route 8` / Roadside Motel
https://bulbapedia.bulbagarden.net/wiki/Alola_Route_8

Relevant high-level structure:

One room can have different occupants at different campaign phases. An occupant may move out, leave correspondence behind, and later give way to other temporary users.

Reusable Ouros lesson:

Physical space can retain history across occupancy changes. A room assignment needs a time interval and should not overwrite previous occupancy records. Objects or correspondence left behind require separate custody/provenance resolution rather than becoming property of the next occupant.

## Source 5 — Tide Song Hotel

Source: Bulbapedia, `Tide Song Hotel`
https://bulbapedia.bulbagarden.net/wiki/Tide_Song_Hotel

Relevant structure:

A lodging location contains temporary residents with different purposes: waiting, research-related interests, personal reunions, and other local errands. One person can be temporarily staying in a public area without the game establishing permanent residence.

Reusable Ouros lesson:

Reason for presence should be explicit and independent from lodging state. `STAYING_HERE` does not explain why someone came, what access they possess, or how long they intend to remain.

## Source 6 — Pokémon Concierge

Source: Netflix official series page
https://www.netflix.com/title/81186864

Relevant high-level structures from the official episode descriptions:

- the resort's core premise is receiving Pokémon guests and helping them during a temporary stay;
- a Trainer's preference for their Pokémon can differ from what the Pokémon appears comfortable doing;
- changed plans can alter staff workload;
- a guest and companion may become separated when departure is expected;
- weather can transform an ordinary stay into a safety problem;
- hospitality work is responsive to individuals rather than one uniform 'guest satisfaction' value.

Reusable Ouros lesson:

A guest Pokémon should remain an individual actor. Hosting needs to track the Trainer/companion relationship, observed needs, and current presence separately. Staff should not infer a Pokémon's wishes from species identity or from the Trainer's request alone.

Do not import:

- Pokémon Resort;
- Haru or other characters;
- episode plots;
- concierge profession mechanics;
- resort services or aesthetics.

## PTU/community scan

Public PTU searches for lodging, guest NPCs, traveler rotations, and temporary residence produced mostly campaign advertisements and homebrew downtime discussion rather than authoritative PTU procedure.

One useful community signal is that PTU campaigns commonly reserve downtime for training, study, social activity, and other non-adventure continuity. This supports making temporary stays playable between major incidents, but no community rule is treated as PTU authority.

No searched source justified a mechanical `Hospitality` Skill, generic guest bonus, lodging recovery rule, temporary-residency benefit, or automatic relationship gain.

## PTU/Caelo boundary

Repository searches across Narrative, AutoPTU-Java, and AutoPTU returned no indexed `Caelo` source material in this pass.

No current evidence inspected establishes:

- Caelo lodging law;
- visitor registration requirements;
- borders or immigration procedure;
- legal residency categories;
- accommodation prices;
- identity documents;
- visitor taxes;
- institutional guest-access doctrine;
- Trainer/Pokémon lodging recovery mechanics.

These remain unresolved.

## Reusable design structures

### Persistent temporary identity

A transient NPC can have a durable ID, relationship history, knowledge state, previous stays, prior disputes, promises, and future return hooks.

### Presence interval

Arrival, expected departure, actual departure, extension, cancellation, and no-show should be separate facts.

### Hosting is capacity, not ownership

A room or bed can be assigned for a period without transferring ownership. A person can be expected without having arrived. A room can be unavailable without revealing why to the player.

### Purpose is separate from access

A visiting researcher may be in town but still need Tideglass or Mirador permission for protected material. A visiting Trainer may be allowed to observe the Battle Yard without being entitled to a battle. A courier can sleep locally without gaining institutional authority.

### Companion needs are individual

A visiting Pokémon may require space, quiet, feeding arrangements, supervision, or route accommodations, but those needs must come from authored/observed facts or mechanics, not species stereotypes.

### Local burden can persist

Delayed departure can consume a room longer, change meal counts, alter ferry manifests, delay another planned stay, or create extra work. This creates low-stakes world continuity without villainy.

### Visitors can carry incomplete outside information

An outsider can provide attributed claims about places not yet canonized. Narrative must store those statements as claims until external geography and history are approved.

## Failure modes to avoid

- treating ferry arrival as proof that a named person checked in;
- treating room assignment as proof of physical occupancy;
- converting every traveler into a quest giver;
- converting repeat visits into residency automatically;
- giving visitors unrestricted archive, station, cooperative, clinic, or Battle Yard access;
- inventing an omniscient guest registry;
- turning Pokémon companions into baggage;
- assuming delayed departure means missing person;
- assuming overstay means wrongdoing;
- using Minecraft bed ownership as canon authority;
- deleting a visitor's history when the entity unloads.

## Research output for Ouros

The strongest opportunity is a `temporary visitor / hosting continuity` layer that connects ferry records, boarding capacity, food/service work, institutional access, correspondence, found property, route safety, and relationship history while leaving residence, ownership, law, prices, and Caelo doctrine unresolved.

This seam can enrich Marea immediately using already-canonized spaces and residents, without adding a new faction or settlement.