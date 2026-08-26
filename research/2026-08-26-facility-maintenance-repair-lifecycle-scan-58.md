# Facility Maintenance, Repair & Operational Lifecycle Scan — Pass 58

Status: external research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-26

## Why this pass

The full repository tree was inspected before writing. Ouros already has strong systems for civic proposals/public works, settlement infrastructure, construction/restoration projects, material supply, staffing, workplaces, housing, technology, crises, conservation, transport and storefront continuity.

The remaining gap is the period after a facility exists: routine inspection, wear, small faults, temporary closure, repair sequencing, reopening, deferred work and visible maintenance memory. Current public-works design can create or restore a project, but it does not yet give ordinary facilities a reusable operational lifecycle when the central question is neither a new civic decision nor an emergency.

This pass therefore studies maintenance as persistent world state. It does not create engineering simulation, building codes, contractor law, property law, repair prices, structural calculations or new PTU mechanics.

## Repository overlap review

Relevant existing ownership boundaries:

- `design/civic-governance-public-works-layer.md` owns collective proposals, authored authority and approved public-works implementation.
- `design/observation-settlement-time-layer.md` owns settlement capability, clocks and coarse infrastructure effects.
- `design/material-culture-economy-crafting-layer.md` owns physical material instances, provenance, workshops and supply routes.
- `design/workplaces-professions-staffing-layer.md` owns roles, shifts, coverage, training and staffing continuity.
- `design/technology-energy-infrastructure-layer.md` owns authored technology/infrastructure state.
- `design/crisis-rescue-recovery-layer.md` owns emergencies and recovery after acute incidents.
- `design/homes-housing-neighborhoods-layer.md` and `design/residential-life-household-relocation-layer.md` own residential suitability and occupancy.
- `design/commercial-services-storefront-continuity-extension.md` owns public-facing commercial service availability.

The new layer should orchestrate these systems around facility condition and work history rather than replace any of them.

## Source 1 — Pokémon Legends: Arceus, Construction Corps and camp setup requests

Sources:
- Serebii, Pokémon Legends: Arceus Requests: https://www.serebii.net/legendsarceus/requests.shtml
- Pokémon Database, missions/requests catalogue: https://pokemondb.net/legends-arceus/missions-requests

Useful pattern:

Several requests make Construction Corps activity visible as a recurring institutional function. Camps are set up in multiple regions, and each setup depends on a local blocker being resolved before the facility becomes usable. The narrative value comes from linking an operational place to a concrete site condition rather than treating camps as abstract fast-travel unlocks.

Reusable lessons:

1. A facility can have a readiness gate tied to the actual site.
2. The institution doing the work can recur across geographically separate jobs.
3. Clearing a blocker can produce a durable service change.
4. Not every work problem needs a combat encounter; investigation, ecology, access or missing staff may be the real dependency.
5. Repeated work by one institution creates continuity without requiring every worker to become a permanent named NPC.

Do not reuse the Construction Corps identity, specific camp locations, requested Pokémon or dialogue in Ouros.

## Source 2 — Pokémon Legends: Arceus, Bothersome Bidoof

Sources:
- Serebii request page: https://www.serebii.net/legendsarceus/requests/bothersomebidoof.shtml
- Bulbapedia walkthrough: https://bulbapedia.bulbagarden.net/wiki/Appendix:Legends:_Arceus_walkthrough/Requests_1-30

Useful pattern:

A nuisance problem is reframed as a practical capability match. The Bidoof causing trouble in Jubilife are retained by the Construction Corps because their natural capabilities are useful for work. The important design lesson is not “Bidoof should build things.” The reusable structure is:

`observed problem -> understand actor capability -> redirect conflict into a durable role -> future world-state consequence`

For Ouros, a Pokémon may assist with work only when the individual Pokémon’s authoritative movement, Move, Ability, Trainer relationship or other governing state actually supports the claimed task. Narrative convenience cannot invent labor capabilities.

## Source 3 — Pokémon Ranger: Guardian Signs, damaged bridge and delayed repair

Source:
- Pokémon Wiki summary of Big Booker Bridge: https://pokemon.fandom.com/wiki/Big_Booker_Bridge

Useful pattern:

A major bridge is damaged, the repair specialist cannot restore it immediately, the route remains constrained while work is underway, and normal access returns later. The story therefore treats infrastructure failure as a temporal state rather than an instant binary toggle.

Reusable structure:

`damage/fault -> temporary restriction -> alternate access or workaround -> repair clock/dependency -> completed repair -> normal or changed route state`

This is especially useful for Minecraft because the world can visibly move through multiple states: damaged, barricaded, scaffolded, limited access, repaired.

Do not reuse the bridge, characters, villain action or traversal solution.

## Source 4 — Pokémon Ranger: Shadows of Almia, bridge operation failure

Source:
- Bulbapedia walkthrough, Part 4: https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Ranger:_Shadows_of_Almia/Part_4

Useful pattern:

The Norward Bridge becomes unavailable because its operator loses the key. The infrastructure itself is not necessarily destroyed; service failure comes from an operational dependency. Restoring access requires identifying and resolving that dependency.

Reusable lesson:

Facility/service state should distinguish physical condition from operational readiness. A perfectly intact asset may be unavailable because of staffing, access control, power, supply, inspection, documentation or another dependency.

That distinction prevents every closure from turning into “repair the broken machine.”

## Source 5 — Pokémon Reborn, city restoration projects

Sources:
- Grand Hall: https://pokemon-reborn.fandom.com/wiki/Grand_Hall
- Railnet Reconstruction Project: https://pokemon-reborn.fandom.com/wiki/Railnet_Reconstruction_Project
- Azurine Nature Center Project: https://pokemon-reborn.fandom.com/wiki/Azurine_Nature_Center_Project

Useful pattern:

Reborn’s restoration projects permanently alter previously damaged or inaccessible spaces. A restored rail system changes access and relocates missed items to Lost and Found; an environmental restoration creates a new Nature Center and changes the island’s later state. These are useful because restoration has consequences beyond a cosmetic rebuild.

Reusable lessons:

1. Completion should update several connected systems, not only a visual flag.
2. Repair can close old access while opening new access.
3. Restoration may create follow-up work and new services.
4. Old-state information should remain in history even when the physical map changes.
5. A completed project can produce downstream ecological, transport, commercial and public-memory effects.

Do not reuse Reborn’s project names, prices, reward structure or exact area transformations.

## Source 6 — Official PTU campaign seed, The Road to Tomorrow

Source:
- Pokémon Tabletop official site, Campaign Seeds: The Road to Tomorrow: https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

Useful pattern:

The seed explicitly proposes characters taking responsibility for parts of a city, seeking supplies to repair and maintain them, and then facing new problems as a functioning settlement grows around those restored assets. It frames maintenance as campaign play rather than a one-time post-apocalypse montage.

Reusable lessons:

1. Repair can create obligations and new story rather than conclude it.
2. A repaired facility becomes part of a larger social system with residents, trade, institutions and competing priorities.
3. Different players or groups can care about different assets without requiring universal ownership.
4. Supply gathering is meaningful only when tied to an actual repair dependency.
5. Recovery should expose new pressures instead of returning the world to a featureless baseline.

This source is useful for campaign structure, not as a mechanical rules source.

## Source 7 — Public PTU campaign setting example with reconstruction as long-term goal

Source:
- Kairos Isles PTU Wiki, Nedri Greening: https://kairosptu.fandom.com/wiki/Nedri

Useful pattern:

A recurring character goal is rebuilding lost research facilities, linking income-generating work, faction involvement and long-term research ambitions. The reusable lesson is that facility recovery can support a character arc over many sessions rather than act as a single construction quest.

Do not reuse the character, facility, factions or personal story.

## Synthesized structures for Ouros

### A. Facility condition is separate from service state

Track at least two independent views:

`physical condition` and `operational availability`

A building may be physically sound but closed due to staffing. A damaged facility may still provide LIMITED service. A repaired structure may remain unavailable until inspection or setup is complete.

### B. Maintenance lifecycle

A reusable lifecycle:

`baseline -> observation/fault -> assessment -> work order -> dependency resolution -> active work -> verification -> reopen/limited operation -> later review`

Not every stage needs player interaction.

### C. Fault provenance

A fault should come from traceable world state:

- ordinary wear;
- prior crisis damage;
- weather exposure;
- ecological interaction;
- supply failure;
- staffing/operations problem;
- previous incomplete repair;
- authorized renovation;
- known technology limitation.

Do not spawn random breakdowns simply to create chores.

### D. Maintenance memory

Persist useful facts such as:

- last known inspection/assessment;
- repaired component or area;
- temporary workaround;
- repeated fault history;
- who performed or coordinated work;
- materials used when provenance matters;
- closure/reopening events;
- unresolved deferred work;
- visible modifications after completion.

This creates callbacks without simulating every screw, beam or machine part.

### E. Worksite as temporary world-state overlay

During maintenance, an existing location can gain:

- barriers;
- scaffold/temporary supports;
- rerouted entrances;
- moved service points;
- posted notices;
- work crews;
- restricted rooms;
- temporary storage;
- alternate transport/service links.

The overlay disappears or changes when the job advances, while its history remains.

### F. Small repair versus civic project

Routine maintenance should not automatically create a political process.

Escalate into `civic-governance-public-works-layer.md` when the work requires a collective future decision, major public resource allocation, land-use choice, competing alternatives or authored public authority.

### G. Acute incident versus maintenance

If immediate life/safety response dominates, use `crisis-rescue-recovery-layer.md` first. After stabilization, unresolved repair work can become a maintenance object.

## Risks to avoid

- Do not invent building codes, inspection powers, permits, contractor licensing or property rights.
- Do not assign numerical structural integrity without an approved model.
- Do not make every fault a fetch quest.
- Do not let one repaired representative component imply an entire facility is safe.
- Do not infer that a Pokémon can perform construction labor from species stereotype alone.
- Do not invent PTU Move/Ability effects as repair tools.
- Do not generate prices, labor rates or repair durations without an authored economy/time model.
- Do not use Minecraft block breakage as authoritative structural damage logic.
- Do not treat reopening as proof that every downstream service has fully recovered.

## Candidate implementation value

Most of this layer is executable as narrative/world-state logic now. Facility states, work orders, dependencies, closures, temporary service relocation, visual overlays and callbacks do not require tactical battle rules.

Battle dependencies appear only when a worksite incident becomes tactical. Dynamic debris, collapses, moving machinery, forced displacement, environmental zones, rescue objectives and objective-aware AI remain dependent on capability families that AutoPTU-Java has not yet verified completely.

## Provenance boundary

All proposed structures are transformed abstractions. No source character, dialogue, exact quest chain, named infrastructure project, reward table or distinctive plot is proposed for Ouros. Future names and locations remain `PROPOSED / NON-CANON` until reviewed.