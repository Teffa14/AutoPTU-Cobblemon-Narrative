# Ouros Narrative Research — Roads, Bridges & Detour Operational Continuity — Pass 95

Status: RESEARCH ONLY. Provenance and design evidence. This file establishes no Ouros canon, transport technology, road jurisdiction or new PTU mechanic.

Date: 2026-08-28

## Repository audit before research

The recursive `main` tree was inspected before selecting this subject and returned `truncated=false` at baseline `2d73b89d7cb16d7b98159dae540f67951a8e985b`.

The inventory showed that Ouros already has broad travel/connectivity, public works, facility maintenance, cartography, public notices, conservation, wildlife monitoring, weather, courier/logistics, worksite safety, railway, aviation and maritime continuity. No dedicated roads/bridges/detours operational layer existed.

Direct overlap review established these boundaries:

- `travel-transport-expedition-layer.md` owns connections, journeys, mode viability, route truth versus route knowledge and broad disruption state.
- `civic-governance-public-works-layer.md` owns proposals, authority, project approval, competing public priorities and implementation projects.
- `facility-maintenance-repair-inspection-extension.md` owns condition observations, faults, assessment, work orders, repairs, verification and facility reopening evidence.
- `cartography-survey-wayfinding-layer.md` owns map/chart versions and surveyed route knowledge.
- `public-notices-signage-world-information-extension.md` owns publication and physical communication of restrictions.
- Conservation/Wildlife systems own ecological interpretation and managed wildlife state.
- `cobblemon-runtime-authority-boundary.md` keeps Minecraft/Cobblemon downstream of Ouros world truth and AutoPTU tactical authority.

The missing connective tissue is the traveler-facing operational state of a road corridor or crossing after those systems produce evidence or decisions: exactly which segment is usable, by whom, in which direction/window, through which detour, and what must be verified before that restriction changes.

## Source 1 — Skyarrow Bridge: inspection can close an intact connection

Source:
https://bulbapedia.bulbagarden.net/wiki/Sky_Arrow_Bridge

Pokémon Black 2 and White 2 temporarily close Skyarrow Bridge for inspections. The location also distinguishes a vehicle roadway from an elevated pedestrian walkway.

Reusable structure:

A crossing can have multiple access surfaces and can be unavailable because of an inspection state rather than destruction. Physical presence, structural condition, inspection progress and traveler access should therefore remain separate facts.

Ouros transformation:

A bridge may expose authored access channels such as pedestrian path, ordinary road surface, service path or other setting-supported use. A restriction can apply to one channel without deleting the entire Travel connection.

Not imported:

- Unova geography;
- exact bridge design;
- Hall of Fame gating;
- named NPCs or rewards;
- any real-world engineering rule.

## Source 2 — Tubeline Bridge: testing belongs between repair and ordinary use

Source:
https://bulbapedia.bulbagarden.net/wiki/Tubeline_Bridge

Black 2 and White 2 close Tubeline Bridge while capacity testing is underway.

Reusable structure:

`work appears complete` and `ordinary access has resumed` can be separated by a verification/test phase.

Ouros transformation:

After repair or modification, a crossing may enter an authored `TESTING_OR_VERIFYING` operational state. Facility Maintenance owns the test/verification evidence. The road layer records the currently authorized traveler-facing result. Travel only treats the connection as available to the access classes actually cleared.

No numerical load limit, engineering calculation or standardized capacity test is imported.

## Source 3 — Driftveil Drawbridge: one crossing can coordinate two transport networks

Sources:
https://bulbapedia.bulbagarden.net/wiki/Driftveil_Drawbridge
https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Black_2_and_White_2/Part_7

The drawbridge raises and lowers around shipping schedules. Flying Pokémon also use the same physical area.

Reusable structure:

One infrastructure asset can alternate between mutually incompatible uses. A road crossing can be operational in general while temporarily unavailable to road travelers because another transport flow has an authorized window.

Ouros transformation:

If canon ever establishes a movable bridge, ferry gate, ford-control structure or comparable crossing, operational windows can reference both Travel and Maritime state. The road layer stores the current crossing configuration and access window. Maritime remains authoritative for vessel/service consequences. Technology/Maintenance owns mechanisms and faults where applicable.

A wild Pokémon flying near or resting on a bridge is an ecological/overworld observation. It does not become a road worker, hazard or combatant by proximity.

Not imported:

- Driftveil;
- its operator;
- exact shipping schedule;
- species encounter tables;
- feather/item mechanics;
- drawbridge technology as Ouros canon.

## Source 4 — Kanto Route 17 / Cycling Road: access class can change over history

Source:
https://bulbapedia.bulbagarden.net/wiki/Kanto_Route_17

Across different game versions, the route has different traversal expectations, including bicycle-specific access in earlier versions and ordinary walking in later reinterpretations. Animation material also uses borrowed bicycles to satisfy access requirements for an urgent delivery.

Reusable structure:

A route can have an explicit access profile that changes with policy, infrastructure or historical era. Access should be checked against the actual traveler/mode/service available at the time rather than baked permanently into geography.

Ouros transformation:

A road segment may carry authored access classes and temporary exceptions. A courier, emergency worker, resident, pedestrian, cycle, cart, vehicle, mounted traveler or Pokémon-assisted traveler only exists as a class if Ouros canon establishes it. Borrowed or public mobility may satisfy an access requirement without transferring ownership.

Not imported:

- Cycling Road layout;
- bicycle-only rules;
- named characters;
- medicine-delivery plot;
- gangs;
- any game-specific movement speed effect.

## Source 5 — “The Green Guardian”: a road closure can be an ecological symptom

Source:
https://bulbapedia.bulbagarden.net/wiki/AG155

A Cycling Road is closed and travelers are redirected. Investigation later connects the blockage to a wider ecological event involving protective vines and an injured Pokémon.

Reusable structure:

The visible blockage can be downstream evidence rather than the central problem. A road authority may correctly close a corridor while the public explanation remains incomplete or wrong.

Ouros transformation:

A closure can reference an observed obstruction while its cause remains unresolved. Conservation, Science, Wildlife Monitoring or a Case may later reinterpret cause. Road Operations should not erase the closure merely because a combat encounter is won, and it should not infer ecological causality from the presence of a species.

Useful sequence:

`observation -> operational restriction -> detour -> investigation -> cause evidence -> intervention -> verification -> access revision`

Not imported:

- Celebi;
- fire/vine plot specifics;
- Ranger characters;
- capture mechanics;
- episode resolution.

## Source 6 — Big Booker Bridge: damage, alternate access and repair are separate world states

Source:
https://bulbapedia.bulbagarden.net/wiki/Renbow_Island#Big_Booker_Bridge

Pokémon Ranger: Guardian Signs depicts a bridge badly damaged, a temporary alternative means of reaching the other side, and later repair of the bridge.

Reusable structure:

A destroyed or unusable connection does not force the entire region to become inaccessible. Temporary traversal can exist independently, and repairing the permanent link can later change the graph again.

Ouros transformation:

Road Operations can preserve:

- original crossing unavailable;
- temporary crossing or bypass available to a limited access profile;
- repair project active;
- verification pending;
- permanent connection restored;
- temporary bypass retired, retained or repurposed.

The alternative route must come from real world state. The generator cannot invent a traversal Pokémon or capability simply because a bridge is broken.

Not imported:

- Renbow/Mitonga geography;
- antagonists;
- Raikou traversal;
- named craftspeople;
- quest rewards.

## PTU 1.05 mechanics cross-check

Source:
https://peda.net/p/josajoki/fista/ohjeet/ptu/pokemon-tabletop-united-1.05-core%3Afile/download/c109e0ecc0ac41065575a4a324183b80189a2c70/Pokemon%20Tabletop%20United%201.05%20Core.pdf

PTU 1.05 defines `Overland` as the Movement Capability used to shift on dry land. PTU also defines tactical Shift movement, footprints, jumps and related combat positioning procedures.

Pass 95 does not derive an overworld road simulator from those rules.

No governing evidence reviewed here authorizes Narrative to invent:

- road speed multipliers;
- vehicle statistics;
- bridge load limits;
- traffic initiative;
- crash or collision damage;
- braking distance;
- slope handling;
- fall damage from bridge edges;
- wet-road accuracy/evasion penalties;
- structural HP;
- lane-control combat rules;
- universal riding/mount permissions;
- repair DCs;
- engineering Skill checks.

If a tactical road encounter uses ordinary dry, static legal cells, verified base movement can eventually represent those cells through the reviewed BattleSpec adapter. If the road itself applies a hazard, moving barrier, collapse, forced displacement, weather effect or reaction, the exact engine capability family must support it first.

## Caelo cross-check

The project’s governing source inventory identifies Caelo Player’s Guide, Caelo Location & Encounter List, errata and character-creation materials as setting/mechanical inputs. Existing internal research records that Caelo locations can carry explicit environmental mechanical identity.

Pass 95 found no already-extracted Caelo rule that establishes a universal road network, bridge engineering procedure, vehicle framework, road-access law or detour mechanic for Ouros.

Therefore those questions remain unresolved. Narrative will not fill the gap with assumptions.

If a future Caelo extraction identifies a location-specific bridge, road condition, terrain effect or transport rule, the specific authored rule can attach to this continuity model without changing authority boundaries.

## Community / campaign research outcome

Public PTU campaign and forum searches were also run for road- and bridge-specific structures. The useful material located was either broad travel/exploration guidance already captured in Pass 10 or too thin to justify importing a new procedure.

That negative result is retained deliberately. A weak community anecdote should not be elevated merely to make the source list longer.

Pass 10 already established from PTU campaign retrospectives that travel works best when routes reveal a pre-existing changing world. Pass 95 specializes that existing lesson into persistent road/crossing state instead of reprocessing those retrospectives as new evidence.

## Design lessons extracted

Road/crossing continuity benefits from the following reusable structures:

1. A corridor has stable identity even when its access changes.
2. A bridge can contain multiple independently restricted surfaces or approaches.
3. Inspection, repair, verification and reopening are separate events.
4. A usable structure can still be operationally restricted.
5. A damaged structure can have a temporary bypass without being repaired.
6. A detour is a real temporary connection with its own consequences, not a teleport around a blocker.
7. Route truth, public notices, maps and actor knowledge can disagree temporarily.
8. A crossing can coordinate multiple transport flows where canon supports them.
9. Access can differ by traveler/mode class only when those classes are authored.
10. Ecological observations can justify investigation or mitigation without proving causality.
11. A closure can be correct even when its first public explanation is incomplete.
12. Reopening should require the correct evidence/authority chain, not a generic quest-complete flag.
13. Old alignments, temporary roads and retired crossings can persist as habitat, service tracks, public paths or historical traces.
14. Winning a battle near infrastructure cannot repair, inspect, reopen or authorize it automatically.

## Copyright and provenance guardrail

No protected dialogue, distinctive external character, exact plot, map, encounter table, custom rule or numeric infrastructure specification is copied into Ouros. External material supplies only high-level structural evidence. All new Ouros examples and proposed records remain original and non-canon until reviewed.
