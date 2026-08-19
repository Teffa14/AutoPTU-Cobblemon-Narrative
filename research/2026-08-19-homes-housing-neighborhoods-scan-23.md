# Homes, Housing, Neighborhoods & Personal Bases — Research Scan 23

Status: research/provenance only. Nothing in this file is automatically Ouros canon.

Date: 2026-08-19

## Why this pass

The repository already has persistent settlements, clubs, workshops, nurseries, clinics, transport, public works, social bonds, crisis recovery and player history. It does not yet have a dedicated model for the place where a character actually lives, returns, hosts others, stores personal history, shares space, moves away from, loses, repairs or deliberately chooses as home.

That gap matters in Minecraft because buildings can persist physically even when no quest is active. It also matters narratively because a home can become an anchor for downtime and callbacks without becoming a mechanical buff station.

Repository search before writing found no dedicated housing/residence/home layer.

## Sources reviewed

### 1. Pokémon Omega Ruby / Alpha Sapphire — Secret Bases

Official Pokémon page:
https://www.pokemon.com/us/pokemon-video-games/pokemon-omega-ruby-and-pokemon-alpha-sapphire/

Reusable structure:
- the player chooses a location rather than receiving one fixed universal room;
- the space can express identity through customization;
- other players can visit/share the space;
- the base is meaningful even when it is not the central plot.

Do not import ORAS decoration rules or mechanical bonuses.

### 2. Brilliant Diamond / Shining Pearl — Grand Underground Secret Bases

Official Pokémon guide:
https://diamondpearl.pokemon.com/en-au/trainersguide/grandunderground/

Reusable structure:
- a base is a persistent place the player creates inside an exploration network;
- it can be relocated while preserving its contents;
- decorating a space can interact with the wider world.

Important boundary:
BDSP statues alter wild-Pokémon appearance rates. Ouros must not copy that rule. A home decoration cannot change Cobblemon encounter rates unless a separate approved system explicitly defines such an effect.

### 3. Pokémon Pokopia — homes, habitats and visitors

Official Pokémon pages:
https://www.pokemon.com/us/pokemon-video-games/pokemon-pokopia
https://www.pokemon.com/uk/features/your-guide-to-playing-with-friends-in-pokemon-pokopia

Reusable structure:
- building a home is connected to long-term place-making;
- Pokémon can have habitat preferences rather than being interchangeable occupants;
- other players can visit a created town/home space;
- building, gardening and environmental improvement can make a place feel inhabited;
- housing is strongest when it connects to the surrounding settlement rather than existing as an isolated menu.

Do not import Pokopia Move-based construction, habitat bonuses, visitor spawning logic or multiplayer permissions.

### 4. Pokémon Mystery Dungeon: Rescue Team DX — recurring team base

Official Pokémon page:
https://mysterydungeon.pokemon.com/en-us/world/

Reusable structure:
- requests can arrive at a recurring base;
- repeated return to the same location can frame an expedition loop;
- a base can be both operational headquarters and familiar home-like anchor.

The lesson for Ouros is not that all PCs need one headquarters. It is that returning somewhere recognizable creates rhythm between excursions.

### 5. Kairos Isles PTU living world — Real Estate

Public PTU living-world wiki:
https://kairosptu.wiki.gg/wiki/Real-Estate

The wiki explicitly treats real estate as downtime content for a long-running PTU living world. Properties can be personal or team bases and can develop over time.

A related town page shows a property evolving through player activity, new services and public projects:
https://kairosptu.wiki.gg/wiki/Herkimer_Town

Reusable high-level structures:
- property persists beyond individual quests;
- development takes time;
- homes and team bases can accumulate facilities;
- a property can become a recognizable public location;
- a settlement can record the history of who established services there.

Do NOT copy Kairos housing levels, prices, slot counts, passive income, upgrades, hired-help costs, capability bonuses, League ownership rules, building lists or mechanical effects. Those are campaign-specific homebrew, not PTU authority.

### 6. PTU campaign seed — The Last Caravan

Official PTU campaign-seed article:
https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

The Last Caravan frames a campaign around people searching for a place to settle and rebuild. The reusable lesson is that choosing where to stop, what to restore and what a community considers home can itself be a campaign-scale objective.

This complements Ouros crisis/recovery and settlement layers without requiring apocalypse as a setting.

### 7. Virtual-place attachment research

DiGRA 2024 — The Dynamic Roles of Home Bases: Finding Home in Game Worlds:
https://dl.digra.org/index.php/dl/article/view/2226

University of East Anglia / Psychology of Popular Media Culture — place attachment in MMO players:
https://research-portal.uea.ac.uk/en/publications/tourism-migration-and-the-exodus-to-virtual-worlds-place-attachme/

Reusable design lessons:
- repeated return can distinguish a familiar interior from the wider unknown world;
- a virtual place can acquire identity, uniqueness, affect and social bonding;
- a home base is useful as a narrative rhythm, not only as storage or fast travel.

### 8. Narrative design of character-driven home bases

GDC Vault — How to Build a Home: Designing Narrative for Sindri's House in God of War Ragnarök:
https://gdcvault.com/play/1029158/How-to-Build-a-Home

Reusable high-level lesson:
A convincing home should not freeze supporting characters into furniture. Residents can have independent routines, arrivals, absences and conversations while the player retains freedom to enter and leave.

No characters, dialogue or plot details are imported.

## PTU / Caelo source boundary

The supplied Caelo Player's Guide uses the term `homestead` in its experience rules, confirming that persistent home-space play existed in that living-world environment. This pass did not locate or rely on a governing Caelo housing subsystem.

Therefore this layer remains narrative/world-state only until the project explicitly chooses housing rules.

Do not invent:
- property prices;
- rent;
- ownership law;
- land grants;
- construction Skill DCs;
- building times;
- passive income;
- healing bonuses;
- training bonuses;
- Pokémon capability bonuses;
- fast-travel rights;
- storage limits;
- daycare/breeding services;
- visitor permissions;
- destructibility rules.

Existing PTU/Caelo mechanics remain authoritative when a home scene invokes Skills, Features, items, healing, training, breeding, crafting or combat.

## Reusable Ouros design conclusions

### A. Home is a relationship to a place

A character may reside somewhere without considering it home. A character may consider a place home without owning it.

Keep these separate:
- residence;
- ownership claim;
- tenancy/permission;
- membership;
- emotional/home status;
- public address;
- operational base.

### B. Household is not the same as social relationship

Sharing an address does not prove friendship, romance, family, trust or financial dependency.

Household membership should record observable co-residence and access only. Private relationship labels remain governed by the social-bonds consent rules.

### C. Moving should preserve history

When someone moves, the previous home should not disappear from the Chronicle. Former residences can retain:
- old neighbors;
- modifications;
- stored objects;
- unresolved promises;
- witnesses;
- public memory;
- later occupants;
- damage or restoration state.

### D. Neighborhoods create low-intensity world state

Homes become more useful when connected to:
- nearby shops;
- transit;
- clinics;
- schools/clubs;
- workshops;
- wild habitats;
- public works;
- local events;
- recurring neighbors.

This makes a settlement feel lived in without generating a quest for every house.

### E. Supporting residents need agency

A resident or neighbor can be absent, busy, travelling, hosting someone, repairing something or working elsewhere. The player should not expect every home NPC to stand in the same coordinate forever.

### F. Home loss and recovery require restraint

Fire, crisis, displacement, redevelopment or faction conflict can affect housing, but destroying a player's home is a high-impact consequence. It should require authored stakes, explicit causal state and careful multiplayer handling rather than random procedural escalation.

### G. Homes should not become mandatory optimization stations

The strongest use is identity, continuity, storage provenance, social scenes, visitor events, downtime compression and visible world history.

Any mechanical advantage needs separate PTU/Caelo/AutoPTU validation.

## Copyright / transformation note

This research extracts only high-level structural lessons. No protected dialogue, distinctive characters, plots, room layouts, decoration catalogues or source-specific mechanics are copied into Ouros proposals.
