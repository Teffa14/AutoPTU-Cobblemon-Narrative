# Public Space, Parks & Commons Continuity Scan — Pass 67

Status: research/provenance only. Nothing in this file is Ouros canon.
Date inspected: 2026-08-26

## Research question

Ouros already models civic decisions, public works, housing, tourism, events, accessibility, maintenance, conservation, wild ecology, hobbies, sport, travel and settlement routines. The remaining gap is the ordinary shared place between those systems: parks, plazas, courtyards, promenades, greenways, waterfront walks and other commons that many unrelated actors use repeatedly for different reasons.

This scan asks which reusable structures make such places feel persistent without inventing universal property law, municipal rules or a generic "public-space reputation" meter.

## Repository overlap check

The full repository tree was inspected before writing. Closest existing layers are:

- `civic-governance-public-works-layer.md`: authority, proposals, consultation, major collective decisions and public works;
- `facility-maintenance-repair-inspection-extension.md`: physical faults, repair, verification and reopening;
- `temporary-public-event-operations-extension.md`: temporary festival/event overlays;
- `tourism-visitors-destination-pressure-layer.md`: destination pressure and visitor cohorts;
- `accessibility-participation-accommodations-layer.md`: participation barriers and accommodations;
- `conservation-protected-areas-stewardship-layer.md`: protected habitat and stewardship;
- `sports-racing-athletic-culture-layer.md` and `downtime-hobbies-personal-projects-layer.md`: the activities people perform;
- `homes-housing-neighborhoods-layer.md` and `residential-life-household-relocation-layer.md`: residents and neighborhood continuity;
- `wild-collective-agency-layer.md`, `interspecies-ecological-relations-layer.md` and `observation-settlement-time-layer.md`: Pokémon presence, ecology and evidence.

The new concept therefore should own only the persistent shared-use state of the place itself: ordinary use patterns, zones, recurring cohorts, authored access rules, temporary restrictions, overlapping uses, visible traces and the return from exceptional use to normal use.

## Source 1 — Amity Square, Sinnoh

Source:
https://bulbapedia.bulbagarden.net/wiki/Amity_Square

Useful observations:

Amity Square is a dedicated urban park for Trainers walking with Pokémon. Its access policy is explicit rather than inferred. Across game versions, the eligible Pokémon pool changes, the physical layout expands, and the park is reconfigured into east and west sections with separate gates. The location therefore has both a stable identity and a revision history.

Reusable structures:

1. A shared leisure place can have an authored access policy that differs from surrounding streets.
2. Entry points can matter operationally; closing or separating one gate changes use without deleting the place.
3. A familiar public space can be redesigned between eras while preserving its identity and memory.
4. Human-Pokémon co-presence can be part of ordinary civic life without implying ownership of every Pokémon present or creating a battle rule.

Transformation for Ouros:

Do not copy Amity Square, its eligibility list, item-finding loop or bond mechanics. Instead, model location-specific access rules, gate state, zone state and revision history. Any Pokémon-access rule in Ouros must be authored for that site and must not be generated from appearance, type or species stereotype.

## Source 2 — Obsidia Park, Pokémon Reborn

Source:
https://pokemon-reborn.fandom.com/wiki/Obsidia_Park

Useful observations:

Obsidia Park is normally a modest urban green space used as relief from dense city development. During a crisis, plant growth blocks the park and spreads into the surrounding ward. The same ordinary location becomes a major disruption node because its ecological state changes.

Reusable structures:

1. The narrative value of a park comes partly from having a known normal state before disruption.
2. A change inside a shared space can propagate into adjacent streets, services or routines.
3. Restoration has more meaning when players can later compare the recovered place with its disrupted state.

Transformation for Ouros:

Do not import Reborn characters, plot causes, battle-field rules, item placements or crisis sequence. Use only the structure `ordinary public space -> abnormal state -> adjacent consequences -> recovery -> later callback`.

The Reborn Forest Field is not PTU/Caelo authority and cannot justify a tactical terrain effect in Ouros.

## Source 3 — PTU campaign log #24

Source:
https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

Useful observations:

In this public Pokémon Tabletop United session recap, players travel through woods near a training area. A player knocks down a tree, provoking a protective Pokémon because eggs are nearby. The conflict de-escalates after the player plants more trees and leaves the eggs alone.

Reusable structures:

1. Player damage to a shared/natural-use space can create consequences beyond combat.
2. A Pokémon response may be about protecting a concrete local interest rather than seeking a KO.
3. Repair or restoration can be a meaningful resolution after the immediate confrontation.
4. The altered environment should remain in world state instead of resetting after the encounter.

Transformation for Ouros:

Do not import the campaign's characters, Pokémon personalities, Channeler scene, exact species, dialogue or resolution. The reusable pattern is `player-caused environmental trace -> observed stakeholder response -> repair option -> persistent local callback`.

## Source 4 — PTU campaign log #22

Source:
https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t

Useful observations:

This PTU recap describes a community festival associated with a central tree, offerings and local Pokémon. Investigation reveals that a condition affecting the tree is also connected to the town's drought.

Reusable structures:

1. A shared landmark can support ordinary social use, tradition and ecological function simultaneously.
2. Different user groups can interpret the same place through different lenses.
3. A problem that appears ceremonial or social can have a physical/ecological dependency underneath it.

Duplication caution:

This campaign log has already been useful to earlier Ouros event research. Pass 67 does not reuse its festival structure. The only retained lesson here is that a shared place can carry multiple simultaneous functions and therefore should not be represented by one scalar status.

## Source 5 — gate and access-state patterns in Pokémon games

Source:
https://bulbapedia.bulbagarden.net/wiki/Gate

Useful observation:

Pokémon games repeatedly use gates to express temporary or conditional access between otherwise persistent places. The geography does not cease to exist when one entrance is unavailable.

Reusable structure:

Represent access at the entrance/zone level rather than collapsing the whole location to OPEN/CLOSED whenever possible.

Transformation for Ouros:

Do not copy arbitrary badge locks or story blockers. A restriction must come from current authored world state: maintenance, event setup, conservation, safety review, institutional policy, route disruption or another owning system.

## Design lessons extracted

### Baseline before drama

A shared space becomes narratively valuable when players know what normal looks like: who exercises there, who eats lunch there, which Pokémon are usually seen, which gate commuters use, when maintenance happens and which corners stay quiet.

A generator should establish routine use before spending the place on a crisis.

### Same place, different clocks

Many apparent contradictions can be explained by time windows. A dawn exercise group, midday workers, afternoon families, evening hobbyists and nocturnal wildlife can all truthfully describe the same location differently.

This creates low-cost mysteries and callbacks without fabricating secrets.

### Rules have provenance

A sign, barrier, steward statement or habitual practice can indicate an access rule, but the system should record who established it, when, for what scope and whether it is current.

A faded sign cannot silently become timeless law.

### Shared use is multidimensional

Conflicts should be represented by concrete incompatible uses, not by a universal "park tension" score.

Examples:

- a route through a plaza conflicts with a temporary closure;
- a quiet observation zone conflicts with loud practice;
- maintenance access conflicts with normal recreation;
- habitat protection conflicts with a popular shortcut;
- event teardown overlaps the return of ordinary users.

### Exceptional use must hand back to baseline

After a tournament, festival, emergency shelter, research setup or repair project ends, the public-space layer should receive a closure handoff describing what remains changed.

Temporary barriers should not become permanent scenery by accident. Conversely, worn grass, a repaired bench, a new preferred route or revised hours can remain if world state supports them.

### Pokémon presence does not define ownership

A wild Pokémon repeatedly using a park corner can create an observation and perhaps a stewardship concern. It does not become a resident's Pokémon, a municipal Pokémon or a legal occupant by inference.

### Physical presence does not prove permission

Minecraft can show a player inside a zone. That alone does not establish that access was authorized. The adapter should render and enforce only rules already established by narrative/world authority.

## Candidate story structures

1. Routine collision: two recurring groups begin using the same zone at overlapping times.
2. Partial closure: one gate or path is unavailable while the rest of the location remains usable.
3. Changed shortcut: users create an informal path that starts affecting maintenance or ecology.
4. Return after event: ordinary users come back before teardown, cleanup or habitat recovery is complete.
5. Famous quiet corner: media attention turns an overlooked space into a pressure point.
6. Rule provenance dispute: several people remember different versions of the same access rule.
7. Environmental trace: player or NPC activity leaves visible damage that becomes a later callback.
8. Multi-clock mystery: several testimonies conflict until recurring use windows are reconstructed.

## Mechanically relevant encounter pattern A — Pondside Withdrawal

Narrative premise:

An ordinary shared path passes near a zone where defensive wild Pokémon are currently active. Civilians or routine users need to leave safely while the affected section is closed.

Intended full version may require:

- protected or withdrawing noncombatants;
- changing safe lanes;
- protect/withdraw objective state;
- interception or forced displacement;
- terrain/weather or hazard rules when exact PTU/Caelo mapping exists;
- territorial/retreat tactical AI;
- adapter playback synchronized with the closure and later reopening.

Reduced version:

Evacuate ordinary users in world state before battle. Close the affected zone. Use a reviewed static arena at the edge of the space and only mechanics that are currently supported. After the authoritative battle, hand the result back to public-space/ecology state for access review and reopening.

A battle victory cannot establish permanent park policy, prove why earlier incidents occurred or grant ownership of the space or Pokémon.

## Mechanically relevant encounter pattern B — Plaza Access Break

Narrative premise:

A threat or obstruction makes one entrance to a shared plaza unusable while another route remains available. Clearing the immediate danger matters because the plaza is part of daily circulation.

Intended full version may require:

- several exits and civilian route choices;
- protected fixtures;
- dynamic barriers;
- escort/withdraw/clear-route objectives;
- interception or forced movement;
- tactical AI that understands access rather than only KO value;
- adapter support for exact post-battle entrance state.

Reduced version:

Close the plaza to civilians before combat, select a static arena outside protected fixtures and run an ordinary legal battle. Reopening happens only after the owning world systems verify access and condition. Winning does not repair a damaged gate or settle a civic policy question.

## Originality guardrails

- No Pokémon location, institution, NPC, ritual, park rule or civic model from a source enters Ouros by default.
- No source-specific puzzle, dialogue, plot twist, boss or field mechanic is copied.
- Public-source stories are used only for abstract patterns.
- PTU campaign logs are inspiration evidence, not rules authority.
- Exact mechanics must come from PTU/Caelo and current AutoPTU evidence.

## Canon questions left open

- Which Ouros settlements actually have parks, plazas, promenades, greenways, courtyards or equivalent commons?
- Who owns, stewards, maintains or operates each one, if anyone?
- Which access restrictions are culturally normal and which require formal authority?
- Which shared spaces allow routine Pokémon presence, and under what established rules?
- Which locations have recurring use schedules worth persisting?
- How much ordinary population should Minecraft materialize versus aggregate?
- Which spaces have ecological sensitivity that should be owned by Conservation rather than this layer?

Until reviewed, every Ouros-specific application remains proposed.