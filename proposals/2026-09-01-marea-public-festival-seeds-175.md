# Marea Public Festival Seeds — Pass 175

Status: PROPOSAL / NON-CANON
Date: 2026-09-01
Depends on:
- `canon/ouros-playable-foundation-v1.md`
- `canon/marea-interior-map-resident-network-v2.md`
- `design/recurring-public-festival-ritual-layer.md`
- existing local-knowledge, communication, public-memory, service-dispatch and questline systems.

None of the names, dates, historical explanations or annual practices below are canon-approved.

## Candidate A — Sendero Open Day

Premise:
A seasonal public day marks the practical reopening or inspection of Sendero del Vidrio after the heavier-weather period. The event is civic and operational before it is ceremonial.

Existing residents naturally involved:
- Mara coordinates current route notices;
- Nerea presents recent observation methods without claiming final truth;
- Teo checks temporary signs and ordinary equipment;
- Jo runs an observation activity for students/visitors;
- Lia and Mina coordinate altered ferry demand if land traffic changes;
- Ivo prepares portable food service;
- Taro displays older route surveys with edition/provenance labels.

Possible programs:
- guided route walk;
- compare-current-map-to-old-survey exercise;
- temporary sign inspection;
- public meal at the trailhead;
- Battle Yard exhibition after the walk, not as proof of route safety.

Long-term memory:
If one edition discovers that the public route map is outdated, the next edition displays both the old and revised map with the correction history preserved.

Mechanical risk:
Low when implemented as visits, observations and service tasks. High if a procession, wild confrontation, unstable terrain or evacuation is represented inside BattleSpec.

## Candidate B — First Basket Table

Premise:
Loma Clara producers and Bruma Market Hall hold a public shared table when a defined seasonal set of products first reaches the bay. The event emphasizes traceability, substitution, recipes and producer identity rather than generic harvest abundance.

Existing residents:
- Ivo handles cooking/purchasing context;
- Alba represents one producer voice, not the whole cooperative;
- Brin handles lot records;
- Lia can verify dock receipt timing;
- Taro can show historical menus/market records;
- Jo can run a provenance exercise.

Thin Delivery Season connection:
The event can expose changes in lot size, substitutes or missing ingredients without declaring a crop failure or a cause.

Potential branch:
A traditional dish uses a substitute this year. Residents disagree whether the result should retain the old public label. This creates a cultural/relationship discussion, not a rules bonus.

Mechanical dependency:
None unless an optional battle exhibition or field encounter is attached.

## Candidate C — Tideglass Revision Night

Premise:
Tideglass hosts an evening where one older public story, map annotation or route record is shown alongside later corrections and competing testimony.

Purpose:
Teach the world’s provenance rules diegetically.

Possible interaction:
The player follows a chain from an older claim to its source, then to a later contradictory observation, then chooses which questions to ask Taro, Nerea or Pia. Completion records understanding of the evidence chain; it does not force the player to declare a single interpretation when evidence remains incomplete.

Recurring behavior:
Each edition can feature a different record. Prior editions remain archived.

Mechanical dependency:
None for the core program.

## Candidate D — Bruma Yard Measure Day

Premise:
Sela and Jace host an annual or seasonal audited exhibition where returning Trainers can compare present performance with an earlier recorded battle or drill.

Narrative function:
The event gives rivalry and training history a public social context. It reinforces Sela’s canon motivation that rematches are evidence of change.

Full version:
Could support format-specific scoring, ring control, timed rounds, crowd-facing announcements and tactical opponent adaptation.

Required capability families for full version:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement if ring control, forced movement or interception matters;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle for timed/scored formats;
- full stateful damage pipeline;
- status lifecycle;
- exact move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy for opponent adaptation;
- adapter/playback.

Current status: FULL BLOCKED/PARTIAL.

Reduced version:
Run an ordinary audited battle with no festival-specific tactical modifier. After resolution, compare server-owned Trainer/battle record fields outside BattleSpec. The public event can acknowledge changed results without claiming tactical AI learned the player’s style.

## Candidate E — Ferry Welcome Window

Premise:
A short public program is timed around one scheduled ferry arrival. It is less a “festival” than a recurring civic window when visitors, market staff and residents gather at the landing.

Gameplay:
- check current arrival notice;
- help route visitors to real facilities;
- deliver archive/event handouts;
- reconcile a changed berth or delayed unloading notice;
- escort a visitor only through ordinary world navigation, not tactical escort rules.

Why useful:
It provides a smaller recurring event that can test the lifecycle architecture before a large festival is canonized.

Mechanical dependency:
None for reduced world-state implementation. Tactical escort is not required.

## Candidate F — The Old Marker Walk

Premise:
A guided route visits several old survey markers between Puerto Bruma, Sendero and the Mirador branch. The public story says the markers represent one historical route-improvement effort, but Tideglass holds records from multiple dates.

Mystery structure:
The player can discover that the markers were installed in stages. This does not require the public story to be fraudulent; it may be a later simplification.

Possible consequences:
- Taro revises exhibit wording;
- Mara updates a training handout;
- Jo changes the field-school version;
- older residents retain personal phrasing while acknowledging the archive dates.

Mechanical dependency:
None unless access to a marker requires a battle or mechanically hazardous terrain.

## Candidate G — Crossing Lantern Line

Premise:
Residents place temporary lights or visible markers near an ordinary safe section of the seasonal crossing during an evening event. This candidate deliberately avoids canonizing a mystical function.

Narrative uses:
- temporary infrastructure work with Teo;
- route observations with Mara/Nerea;
- food and gathering with Ivo;
- source story with Taro;
- children/students with Jo;
- public-memory revision if the event’s origin turns out to have several documented explanations.

Full encounter possibility:
A wild group occupies the approach while residents are still clearing the event site.

Full dependencies:
All standard battle families plus complete movement for protected corridors, lifecycle for sustained objectives, terrain/weather/hazards/zones/reactions if crossing conditions matter, AI tactical policy for corridor behavior, and adapter/playback.

Current status: FULL BLOCKED.

Reduced version:
Residents withdraw before battle compilation. An ordinary audited encounter occurs in a clean arena segment. Allowed output: `IMMEDIATE_EVENT_ROUTE_CLEAR`. The battle cannot determine why the wild group was present.

## Candidate H — Marea Shared Table Aftermath

Premise:
The day after a larger event, several residents meet to review leftovers, damaged equipment, missing archive loans, public complaints, route litter and useful observations.

Purpose:
Make cleanup and institutional learning playable instead of letting the event vanish after its climax.

Possible outputs:
- new service requests;
- corrected public information;
- repaired/replaced objects;
- relationship consequences;
- next-edition changes;
- archived incident refs.

Mechanical dependency:
None by default.

## Recommended first implementation candidate

`Ferry Welcome Window` is the safest implementation test because the existing ferry landing, Lia, Mina, Mara, Pia, Ivo and service/communication systems already provide a connected graph. It can demonstrate planning -> open -> closing -> aftermath without requiring new combat capability or a major historical canon decision.

Second choice: `Tideglass Revision Night`, because it exercises local knowledge and public-memory correction with minimal mechanical risk.

## Canon questions before promotion

- Does Marea already have a named seasonal civic event, or should one emerge from current institutions after Thin Delivery Season develops?
- Which event, if any, predates the current Field Office/Archive institutions?
- Which historical records are sufficiently established to support a commemorative practice?
- Is there a regional civil/religious distinction that affects how “ritual” should be framed? No answer is assumed here.
- Which calendar/season model will be canonical in the playable district?
- Are visitors common enough to justify a recurring ferry welcome program?
- Which practices are settlement-specific versus district-wide?

## Mechanical questions before any battle-bearing promotion

- Which exact Moves, Abilities, Items and Trainer Features are selected for the encounter?
- Does the scene require forced movement, interception, knockback, protected corridors or crowd units?
- Does weather or terrain have mechanical meaning or only narrative/presentation meaning?
- Does success require surviving N rounds or another lifecycle-dependent condition?
- Must AI reason about non-KO objectives?
- Can Minecraft/Cobblemon playback represent the semantic objective without becoming rules authority?
