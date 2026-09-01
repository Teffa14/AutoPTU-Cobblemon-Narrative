# Persistent Aftermath, Site Recovery and Environmental Continuity — Research Scan 176

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-01
Writable target: Teffa14/AutoPTU-Cobblemon-Narrative
Read-only cross-checks: Teffa14/AutoPTU-Java, Teffa14/AutoPTU

## Purpose

This pass studies how places can retain consequences after an incident instead of resetting when a quest or battle ends. The target is a reusable Ouros pattern for visible damage, restricted access, stabilization, repair, ecological succession, archival trace and changed use over later visits.

This file records sources and transformed design lessons. It does not canonize an incident, ruin, disaster, species behavior, historical cause, repair technology or new Marea location.

## Duplication check

The repository was inspected before research. Existing recent layers already cover:

- service-dispatch/request boards;
- local knowledge, claims, rumor and revision;
- media/communications and public memory;
- recurring public events/festivals;
- investigation/evidence boundaries;
- fixed Marea sites and resident responsibilities.

No dedicated layer was found whose primary ownership is the physical continuity of a site across disruption, stabilization, repair, recovery and later reuse. This pass therefore treats physical site condition as the gap, while reusing existing communications, claims, public memory, calendar, dispatch and questline systems rather than duplicating them.

## New public sources

### Pokémon Omega Ruby / Alpha Sapphire — Sea Mauville

Source:
https://bulbapedia.bulbagarden.net/wiki/Sea_Mauville

Observed high-level structure:

- a former industrial/research facility remains physically legible after closure;
- documents and remnants preserve multiple layers of institutional history;
- environmental survey changes the site's future: demolition is canceled after the derelict structure becomes habitat for Pokémon and plants;
- abandonment therefore produces a new ecological state rather than only a loot dungeon.

Reusable Ouros lessons:

1. A damaged or obsolete site can become useful in a different way.
2. Recovery can mean adaptation or conservation, not return to the previous condition.
3. Physical evidence, records and later ecological observations can tell different parts of the same history.
4. Decommissioning should leave custodial questions: who owns access, who surveys risk, what gets preserved, what gets removed.
5. A site can be safer for wildlife while remaining unsuitable for its former human function.

Do not copy Sea Mauville's company history, named staff, documents, Infinity Energy material, layout or special encounters.

### Pokémon HeartGold/SoulSilver — Ruins of Alph

Sources:
https://bulbapedia.bulbagarden.net/wiki/Ruins_of_Alph
https://guidestrats.com/pokemon-hgss-ruins-of-alph-rooms/

Observed high-level structure:

- exploration is distributed among multiple chambers rather than one linear corridor;
- puzzles alter access and reveal additional information/encounters;
- later traversal capabilities open additional chambers;
- archaeology and active Pokémon ecology coexist in the same location.

Reusable Ouros lessons:

1. A historical site can support repeated visits with different purposes.
2. Physical access, interpretation and ecological observation can progress separately.
3. A puzzle need not be a magical lock; it can represent reconstruction, reading a damaged plan, aligning markers or understanding old operational logic.
4. New access should reveal a new layer of the place, not merely another reward chest.

Do not copy Unown messages, puzzle images, hidden-room solutions, species gating or Johto history.

### Pokémon Reborn — Reborn City restoration

Sources:
https://pokemon-reborn.fandom.com/wiki/Adrienn
https://reborn.sailor.li/walkthroughs/19_neo_reborn
https://www.rebornevo.com/forums/profile/55666-friz/

Observed high-level structure:

- a previously damaged city later returns in a materially changed state;
- reconstruction changes traversal, buildings, services, side content and available interactions;
- the restored map communicates passage of time and collective work without requiring every repair to occur in front of the player.

Reusable Ouros lessons:

1. Returning to a familiar place after time away can be a major narrative payoff.
2. World-state change should affect ordinary routes and services, not only dialogue flags.
3. Collective recovery can continue while the player is elsewhere.
4. Restoration is strongest when the player can compare before/after states through known landmarks.
5. Avoid total cosmetic reset: retain traces, records or changed uses when continuity benefits the setting.

Do not copy Reborn City, its disasters, restoration leader, factions, plot sequence, dialogue or map redesign.

### Pokémon Tabletop United campaign log — ruined Azalea/PokéCenter scene

Source:
https://forums.giantitp.com/archive/index.php/t-527075.html

Observed high-level structure:

- players encounter a dilapidated PokéCenter whose damaged roof obstructs equipment;
- the GM explicitly considers structural collapse as a consequence for poor rubble removal;
- nearby town ruins are a navigable world condition rather than merely exposition;
- ordinary interaction with damaged infrastructure creates risk and player choice before or outside a formal battle.

Reusable Ouros lessons:

1. Ruins should communicate operational risk through the environment, not only enemies.
2. Repair/recovery actions require their own authority; combat competence does not automatically imply safe structural work.
3. Failed or careless intervention can worsen a site, but consequences need authored rules rather than improvised hidden punishment.
4. Salvage, access and restoration should be separate decisions.
5. A mechanically dense PTU campaign benefits from keeping environmental resolution auditable instead of assuming a single skill roll or battle win repairs infrastructure.

Do not copy the campaign's ruined Azalea scenario, characters, exact incidents, dialogue, criminal encounter or home rules.

### PTU living-world community example — Super Pokémon Online

Source:
https://www.reddit.com/r/PokemonTabletop/comments/1mkct0y/super_pok%C3%A9mon_online_ptu_living_world_rpg/

Observed high-level structure:

- the advertised living world explicitly says locations can be discovered and the economy can shift based on player actions;
- player reputation persists around characters in an asynchronous shared setting.

Reusable Ouros lesson:

A persistent-world promise is stronger when consequences are stored in world-facing facts. Site condition is one useful world-facing consequence alongside economy, reputation and discovery.

This source is promotional/community material, not a rules authority.

## PTU / project-source cross-check

Repository search confirmed PTU 1.05 source material under `Teffa14/AutoPTU`, including the 1.05 changelog, May 2015 Playtest Packet, trainer sheets and engine data. The Playtest Packet explicitly describes tactical combat as a core part of the system. The project also contains data-driven PTU moves, abilities and items.

This research pass therefore does not invent a universal PTU 'repair roll', structural HP system, construction action, hazard subsystem or ecological recovery mechanic. Non-battle site changes remain authored world-state facts unless an exact PTU mechanic is separately validated.

Searches for the literal term `Caelo` across the currently accessible Narrative, AutoPTU-Java and AutoPTU repositories returned no code-search hits in this run. That is not evidence that Caelo material does not exist elsewhere in the project. It means no Caelo-specific assumption can be promoted from this pass. Any candidate that depends on Caelo-specific history, institutions, technology or metaphysics remains UNCERTAIN pending a located source.

## Transformed design principles for Ouros

### Places need temporal layers

A location can carry at least three distinguishable layers:

- what it was used for;
- what happened to it;
- what it is used for now.

Later events may add more layers without deleting earlier ones.

### Recovery is multidimensional

'Fixed' is too coarse. A site can be:

- physically stable but still closed;
- operational but visibly scarred;
- ecologically recovering while infrastructure remains damaged;
- repurposed instead of restored;
- historically preserved while no longer functional;
- safe for one activity but restricted for another.

These are design dimensions, not canon enum values.

### World repair needs custodians

Every persistent change should have an actor or institution able to authorize or perform it. The player may supply observations, labor, transport, protection or resources, but should not become omnipotent municipal authority by quest completion.

### The world can work without the player

If a repair requires three days of ordinary work, those three days can progress through calendar/world simulation while the player does something else. The player can return to an intermediate or completed state.

### Restoration should preserve evidence when useful

A repaired place does not need to look permanently ruined, but meaningful traces can persist through patched materials, retained markers, archived photographs/records, replaced equipment, changed paths or institutional memory.

### Battle outcome has a narrow handoff

A battle may author only the consequences covered by its authoritative result. Examples include removal of an immediate hostile obstacle or creation of a temporary safe corridor. It does not automatically:

- repair a slope;
- prove why a structure failed;
- restore an ecosystem;
- authorize reopening;
- decide historical truth;
- complete unrelated labor.

## Candidate narrative opportunities

- a route whose detour remains visible after the immediate danger passes;
- a facility that is repaired but one damaged section becomes a permanent monitoring site;
- old equipment retained as a teaching example after replacement;
- a dock whose temporary workaround changes how shipments are handled for several days;
- archival conservation where some damaged records survive, some become partial, and later claims inherit that evidence quality;
- a former work site repurposed for habitat or observation because returning it to the old use would destroy an emergent ecological value;
- a repaired competitive venue where fixture changes alter later training routines without changing battle rules.

## Encounter implementation caution

The richest site-recovery concepts can touch tactical categories indirectly. A collapsing shelf, moving debris, unstable cells, forced evacuation, weather escalation, delayed structural effects or protective wild Pokémon can require categories that are not complete merely because a representative mechanic exists.

This pass uses the permanent engine category taxonomy and records exact dependencies in the companion design/proposals. A reduced version keeps unstable-site resolution outside BattleSpec and moves any authorized battle onto a bounded, mechanically audited space.

## Promotion boundary

All material here remains research/provenance. No site condition, disaster, repair project, historical ruin or ecological succession event becomes Ouros canon through this file.