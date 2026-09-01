# Marea Interior Fixed Map and Resident Network v2

Status: CANON-APPROVED FOUNDATION
Date: 2026-09-01

This file freezes the first physical map coordinates and expands the resident network for Marea Interior. Coordinates are implementation anchors in `minecraft:overworld` and can only move through an explicit migration because quests, NPC schedules, discovery, structures and server events may reference them.

## 1. Fixed district coordinates

Coordinate convention: `(x, y, z)` is the canonical anchor for the named site. Structure footprints may extend around the anchor.

### Puerto Bruma

- settlement anchor: `(2048, 72, 2048)`
- Bruma Market Hall: `(2052, 72, 2042)`
- Marea Field Office: `(2034, 72, 2040)`
- Tideglass Archive branch: `(2035, 72, 2061)`
- Bruma Battle Yard: `(2070, 72, 2060)`
- ferry landing: `(2066, 69, 2021)`
- clinic/care station: `(2055, 72, 2066)`
- repair row: `(2043, 72, 2029)`

Puerto Bruma is the district's coastal service hub. The market, field office, archive, battle yard, clinic, ferry and repair row are close enough that recurring NPCs plausibly cross paths during an ordinary day.

### Sendero del Vidrio

- south trailhead: `(2048, 73, 2080)`
- lower shelf: `(2056, 77, 2120)`
- seasonal crossing: `(2072, 79, 2154)`
- upper junction: `(2054, 84, 2188)`

The route physically connects Puerto Bruma to Loma Clara and branches toward Estación Mirador.

### Loma Clara

- settlement anchor: `(2048, 86, 2224)`
- cooperative storehouse: `(2038, 86, 2217)`
- communal kitchen: `(2058, 86, 2218)`
- field school: `(2038, 86, 2234)`
- producer lane: `(2059, 86, 2235)`

### Estación Mirador

- station anchor: `(2144, 96, 2160)`
- weather mast: `(2152, 96, 2152)`
- field transect trailhead: `(2133, 95, 2168)`
- specimen/equipment shed: `(2149, 96, 2170)`

## 2. Settlement adjacency

Canonical route graph:

```text
Puerto Bruma
  |
  | Sendero del Vidrio
  |
  +---- Estación Mirador
  |
Loma Clara
```

Puerto Bruma and Loma Clara are not abstract menu destinations. Sendero del Vidrio is the ordinary land connection. Estación Mirador sits on a branch from the upper route. Ferry traffic connects Puerto Bruma outward to later coastal content but no external destination is canonized by this file.

## 3. Primary implemented residents

These five residents are the first required physical NPCs in the mod.

### Mara Veyra

- `npc_id: ouros.npc.mara_veyra`
- home: Puerto Bruma, boarding room near Field Office
- primary workplace: Marea Field Office
- current class concepts: Commander / Survivalist
- companion: Kite the Corviknight
- ordinary responsibility: coordinates field reports, route checks, wildlife incidents and practical assistance
- relationship edges: works with Nerea on evidence quality; depends on Lia for dock reports; asks Mina about ferry observations; often uses Taro's archive when current reports need historical comparison
- Thin Delivery role: owns the route-check lane, but does not own the final explanation

### Ivo Serrat

- `npc_id: ouros.npc.ivo_serrat`
- home: Puerto Bruma market street
- workplace: Bruma Market Hall communal kitchen
- class concepts: Chef / Hobbyist
- companion: Pepa the Greedent
- ordinary responsibility: purchasing, communal meals, supplier coordination, recipe substitution
- relationship edges: sibling/cousin relationship is NOT yet canonized with Alba Serrat despite surname; no kinship is inferred until explicitly established
- Thin Delivery role: notices ingredient substitutions and lot irregularity first through daily purchasing

### Dr. Nerea Sol

- `npc_id: ouros.npc.nerea_sol`
- home: quarters at Estación Mirador
- workplace: Estación Mirador
- class concepts: Researcher / Chronicler
- companion: Lumen the Heliolisk
- ordinary responsibility: longitudinal ecological and weather observations
- relationship edges: shares copies with Tideglass; receives route observations from Mara; disagrees with vendors when uncertainty is presented as a conclusion
- Thin Delivery role: evidence/hypothesis lane

### Taro Min

- `npc_id: ouros.npc.taro_min`
- home: Puerto Bruma archive residence room
- workplace: Tideglass Archive
- class concepts: Chronicler / Mentor
- companion: Margin the Noctowl
- ordinary responsibility: archive custody, editions, interviews, local history
- relationship edges: mentors Pia Min professionally; surname does not automatically define family relationship until separately canonized
- Thin Delivery role: historical-comparison lane

### Sela Orrin

- `npc_id: ouros.npc.sela_orrin`
- home: Puerto Bruma north boarding row
- workplace: Bruma Battle Yard
- class concepts: Ace Trainer / Duelist
- companion: Rook the Falinks
- ordinary responsibility: training sessions, audited battles and battle-yard maintenance
- relationship edges: trains Jace Orrin; exact family relationship is intentionally unresolved until canonized
- Thin Delivery role: may provide field assistance or a training thread; battle victory does not explain the supply irregularity

## 4. Secondary resident network

These residents are canon and should be implemented progressively. They exist even before their visual NPC actor is added.

### Lia Morn

- `npc_id: ouros.npc.lia_morn`
- settlement: Puerto Bruma
- role: dock coordinator
- class concepts: Commander / Rider
- companion: Pelipper, nickname **Gale**
- works at: ferry landing and dock office
- does: assigns berths, records arrivals/departures, coordinates unloading windows
- connects to: Mara, Mina Cors, Ivo, cooperative drivers
- questline surfaces: Region, Faction, Settlement, Exploration, Server Event
- Thin Delivery edge: can verify which shipments physically arrived without proving why they were small

### Mina Cors

- `npc_id: ouros.npc.mina_cors`
- settlement: Puerto Bruma
- role: ferry pilot/operator
- class concepts: Rider / Survivalist
- companion: Floatzel, nickname **Wake**
- works at: ferry landing
- does: short coastal ferry runs and practical weather judgment
- connects to: Lia, Mara, Nerea
- questline surfaces: Exploration, Character, Region, Server Event

### Oren Vale

- `npc_id: ouros.npc.oren_vale`
- settlement: Puerto Bruma
- role: clinic practitioner
- class concepts: Medic
- companion: Audino, nickname **Mell**
- works at: clinic/care station
- does: routine Trainer/Pokémon care within verified mechanics and local care administration
- connects to: Mara during incidents; field school for prevention education
- questline surfaces: Class, Character, Settlement, Pokémon

### Teo Lark

- `npc_id: ouros.npc.teo_lark`
- settlement: Puerto Bruma
- role: repairer and tool maintainer
- class concepts: Hobbyist / Researcher
- companion: Magnemite, nickname **Pin**
- works at: repair row
- does: maintains ordinary equipment, lamps, carts and field instruments; exact mechanical crafting transactions require PTU validation
- connects to: Nerea for instrument servicing; cooperative for carts; Sela for battle-yard fixtures
- questline surfaces: Equipment, Item, Character, Settlement

### Alba Ríos

- `npc_id: ouros.npc.alba_rios`
- settlement: Loma Clara
- role: mixed-crop producer and cooperative delegate
- class concepts: Survivalist / Chef
- companion: Appletun, nickname **Miga**
- works at: producer lane and cooperative meetings
- does: manages her own holding and represents one producer voice; she is not the cooperative itself
- connects to: Ivo, Brin Havel, Jo Venn
- questline surfaces: Faction, Class, Character, Settlement, Pokémon
- Thin Delivery edge: direct production evidence for one holding only

### Brin Havel

- `npc_id: ouros.npc.brin_havel`
- settlement: Loma Clara
- role: cooperative storehouse clerk
- class concepts: Commander / Hobbyist
- companion: Munchlax, nickname **Ledger**
- works at: cooperative storehouse
- does: intake records, dispatch preparation and storage coordination
- connects to: Alba, Ivo, Lia
- questline surfaces: Faction, Item, Settlement, Secondary
- Thin Delivery edge: tracks lots entering/leaving cooperative custody

### Jo Venn

- `npc_id: ouros.npc.jo_venn`
- settlement: Loma Clara
- role: field-school instructor
- class concepts: Mentor / Researcher
- companion: Budew, nickname **Sprig**
- works at: field school
- does: practical instruction in observation, cultivation records and safe field practice
- connects to: Nerea, Oren, local producers
- questline surfaces: Class, Character, Relationship, Settlement

### Ema Rey

- `npc_id: ouros.npc.ema_rey`
- settlement: Estación Mirador
- role: observation technician
- class concepts: Researcher / Backpacker
- companion: Minccino, nickname **Dust**
- works at: station and transect trail
- does: equipment checks, transect observations and field-note preparation under Nerea's project protocols
- connects to: Nerea, Teo, Mara
- questline surfaces: Class, Exploration, Character, Equipment

### Pia Min

- `npc_id: ouros.npc.pia_min`
- settlement: Puerto Bruma
- role: archive assistant and document courier
- class concepts: Chronicler / Backpacker
- companion: Fletchling, nickname **Redline**
- works at: Tideglass Archive, market/dock courier routes
- does: circulation work, copies, deliveries and source retrieval
- connects to: Taro, Nerea, Lia
- questline surfaces: Class, Relationship, Exploration, Item
- relation to Taro: professional mentorship is canon; family relation is not inferred from surname

### Jace Orrin

- `npc_id: ouros.npc.jace_orrin`
- settlement: Puerto Bruma
- role: junior Battle Yard Trainer and maintenance hand
- class concepts: Athlete / Ace Trainer
- companion: Machop, nickname **Knuckle**
- works at: Bruma Battle Yard
- does: assists sessions, cleans/repairs ordinary yard fixtures and seeks stronger competition
- connects to: Sela, Teo
- questline surfaces: Rival, Competitive, Relationship, Character
- relation to Sela: mentor/student is canon; family relation is not yet canonized

## 5. Daily activity weave

The district should feel connected because ordinary tasks create recurring crossings:

- Ivo purchases from Loma Clara lots that Brin records.
- Lia receives arrival information that can corroborate or contradict dispatch records.
- Mina carries people and small consignments when scheduled.
- Mara reads route and incident reports rather than receiving omniscient truth.
- Nerea's station observations are copied to Tideglass through Pia.
- Taro can compare current claims against older deposits.
- Teo maintains field instruments used by Nerea and fixtures used by Sela.
- Oren handles actual care cases rather than being a generic heal button in narrative canon.
- Jo uses selected public observations for field-school instruction.
- Sela and Jace create a competitive social hub that remains connected to the district without becoming the solution to every problem.

## 6. Initial questline coverage from this network

- `REGION`: Thin Delivery Season
- `SETTLEMENT`: Puerto Bruma service continuity; Loma Clara cooperative season
- `FACTION`: Marea Field Office evidence practice; Loma Cooperative internal coordination; Tideglass source stewardship; Bruma Battle Yard local circuit
- `CLASS`: Chef, Researcher, Chronicler, Survivalist, Commander, Mentor, Backpacker, Rider, Medic, Hobbyist, Ace Trainer, Duelist, Athlete first intersections
- `RELATIONSHIP`: Mara, Ivo, Nerea, Taro, Sela and secondary residents can all develop persistent player history
- `CHARACTER`: Nerea's longitudinal project, Jace's competitive development, Ema's field competence, Pia's archive/courier development
- `POKEMON`: each named companion is a persistent individual; wild-population arcs must be grounded in ecology evidence
- `EXPLORATION`: Sendero del Vidrio and Mirador transects
- `COMPETITIVE`: Bruma Battle Yard
- `EQUIPMENT`: Teo/Nerea instrument maintenance
- `ITEM`: delivery lots, records and source documents when individually tracked
- `SERVER_EVENT`: ferry disruptions, market days, seasonal observations and future festivals when scheduled

## 7. Implementation order

P0 visible slice:
1. fixed coordinate registry;
2. simple authored structures for four locations;
3. physical primary five NPCs with canonical IDs;
4. dialogue options exposing Thin Delivery Season;
5. location discovery at real anchors;
6. quest journal entries and objectives tied to visiting/correlating sites.

P1:
- physical secondary residents;
- schedules and homes/workplace movement;
- companion Pokémon projection with safe non-wild identity binding;
- additional questline episodes;
- environmental dressing and custom NPC visuals.

P2:
- server calendar events;
- richer settlement state changes;
- dungeon and expanded regional connections.

Minecraft entities are presentation actors. Their unload, death, AI pathing or duplication cannot author canonical NPC death, relationship changes, quest completion or battle outcomes.
