# Research Scan — Pass 88: Hot Springs, Bathhouses & Thermal Leisure

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-28

## Scope

This pass investigates hot springs, bathhouses and geothermal leisure as persistent places where geology, hospitality, tourism, ordinary social life, maintenance, access, public belief and wildlife can intersect.

The complete recursive `Teffa14/AutoPTU-Cobblemon-Narrative` tree was inspected before topic selection. GitHub returned `truncated=false` at head `83170825f938bd08aa26b98186daf7ed3592954d`.

Two candidate topics were rejected as duplicates before research was written:

- cave-system continuity, because `design/geology-excavation-resource-frontier-layer.md` already owns `CAVE_SYSTEM`, underground occupancy, subsurface connections, flooding, collapse, survey and cave-rescue state;
- generic resort/tourism operations, because `design/tourism-visitors-destination-pressure-layer.md` already models visitor attractions, accommodation, capacity and destination pressure.

The remaining gap is the source-to-bath continuity of a thermal place itself: source observations, water-delivery dependencies, multiple pools/zones, access rules, operational closure, recurring local use, ecological overlap and the difference between cultural/advertising claims and mechanically authoritative healing.

## Existing Ouros boundaries checked

Relevant internal layers reviewed before authoring:

- `design/geology-excavation-resource-frontier-layer.md` — owns geological source/context and subsurface facts;
- `design/tourism-visitors-destination-pressure-layer.md` — owns destination/visitor pressure;
- `design/food-agriculture-hospitality-layer.md` — owns hospitality venues and service events, while explicitly avoiding invented rest/healing buffs;
- `design/care-recovery-welfare-layer.md` — owns treatment and authoritative health-state handoffs;
- `design/facility-maintenance-repair-inspection-extension.md` — owns faults, repairs, inspection and reopening of facilities;
- `design/public-space-parks-commons-continuity-extension.md` — owns shared/public-space use when applicable;
- `design/seasonality-calendar-phenology-layer.md` — owns time/season recurrence;
- `design/cobblemon-runtime-authority-boundary.md` — binding runtime authority rule;
- `design/engine-readiness-snapshot-pass-87.md` — current permanent capability map.

## Source 1 — Lavaridge Town hot springs

Source: Bulbapedia, “Lavaridge Town”.
https://bulbapedia.bulbagarden.net/wiki/Lavaridge_Town

Useful high-level structures:

- the settlement’s springs are physically tied to Mt. Chimney’s geothermal activity;
- the springs are a destination identity rather than a one-use quest object;
- bathing, lodging/visitor activity and ordinary town life can coexist around the same source;
- the same place appears across games, animation and manga in different narrative functions;
- source condition can matter to the town even when the player is not currently in a battle.

Transformation for Ouros:

A thermal settlement should store a source dependency and a separate service/facility state. “The source is hot” and “the public bath is operating” are different facts. A functioning source can coexist with a closed bath because of staffing, pipe, access, maintenance or water-quality review. A bath can also receive water from more than one source or supply line if canon later establishes it.

Do not import:

- Lavaridge’s geography, characters, Gym, customs or businesses;
- claims about specific mineral benefits as truth;
- any assumption that all Ouros thermal settlements use the same bathing etiquette or infrastructure.

## Source 2 — Pokémon Journeys, “Absol Absolved!”

Sources:
- Bulbapedia, `JN064 - Absol Absolved!`: https://bulbapedia.bulbagarden.net/wiki/JN064
- Apple TV episode synopsis: https://tv.apple.com/fi/episode/absol-absolved/umc.cmc.34l2ct5e2pfuxysv515umbpj2

Useful high-level structures:

- an economic/service symptom begins in town: the hot water cools and then stops;
- a visible Pokémon is blamed through an existing superstition before anyone verifies the source;
- investigation follows the physical supply relationship uphill rather than treating the bath itself as the cause;
- the real issue involves ecological occupancy and a geothermal blockage;
- the same event creates several simultaneous consequences: service loss, empty/closed visitor-facing businesses, fear, misattribution, ecological displacement and a dangerous source condition;
- restoring service and correcting the public story are separate consequences.

Transformation for Ouros:

Use a causal chain such as:

`source observation -> delivery/supply observation -> service condition -> public claim/rumor -> investigation -> cause hypothesis -> verified intervention -> reopening review -> public correction`

The design should permit a town to be wrong about why its spring changed without making residents irrational. Their belief can arise from precedent, incomplete observation or a historical story. The investigation should narrow the cause using physical evidence and provenance.

Do not import:

- Absol as the blamed species;
- Glalie/Snorunt, the exact blockage, capture scene or episode resolution;
- the premise that breaking a blockage with attacks is a universal or safe geothermal procedure.

## Source 3 — Pokémon Adventures: Lavaridge spring failure and restoration

Source: Bulbapedia, “Lavaridge Town”, Pokémon Adventures section.
https://bulbapedia.bulbagarden.net/wiki/Lavaridge_Town

Useful high-level structure:

When Mt. Chimney is made dormant, Lavaridge’s hot springs cool and the town reacts immediately. Later, the restored springs again become a social/public destination.

Transformation for Ouros:

A thermal attraction can be a downstream indicator of a larger geological/infrastructure state. Restoration can therefore have visible settlement consequences beyond the technical source: visitors return, routines resume, venues reopen, public memory updates and a previously quiet district changes again.

This supports a persistent callback loop rather than a one-time “repair the spring” quest.

## Source 4 — Pokémon Mystery Dungeon: Explorers Hot Spring

Sources:
- Bulbapedia, “Hot Spring”: https://bulbapedia.bulbagarden.net/wiki/Hot_Spring
- Bulbapedia, “Torkoal (Mystery Dungeon 2 character)”: https://bulbapedia.bulbagarden.net/wiki/Torkoal_(Mystery_Dungeon_2_character)
- GameFAQs Explorers of Sky walkthrough by mossyman27: https://gamefaqs.gamespot.com/ds/955859-pokemon-mystery-dungeon-explorers-of-sky/faqs/60790

Useful high-level structures:

- the place is first discovered through exploration and an unexpected water connection;
- it functions as a rest/social pause after a difficult route;
- it later becomes a recurring information location because a knowledgeable elder can be found there;
- access changes over time: an initially indirect discovery becomes a normal revisitable location;
- the spring is a place with routine occupants rather than an anonymous “healing tile”.

Transformation for Ouros:

A thermal site can change function across visits without changing identity. First visit: exploration/discovery. Later visits: leisure, local conversation, recurring NPC schedule, knowledge lookup, observation or another service. That pattern is valuable for location reuse and avoids consuming the place after one quest.

Do not import:

- Torkoal, Hidden Land information, Waterfall Cave plot, fatigue removal or any PMD-specific mechanic;
- the assumption that every hot spring has an elder or provides reliable healing.

## Source 5 — PTU 1.05 rest and healing boundary

Sources:
- PTU 1.05+ community rules reference, “Health”: https://ptu-unofficial.wikidot.com/rules:health
- PTU 1.05 Core mirror, resting/Pokémon Center section: https://anyflip.com/qloz/xgfq/basic/251-300

Relevant governing distinction:

PTU already defines Rest, Extended Rest, Injury recovery limits and Pokémon Center healing. The available rules text defines Rest broadly as low-exertion downtime such as sleep or sitting quietly, with exact qualification left to GM judgment. It does not establish a universal “hot spring” healing multiplier, Injury cure or status cleanse.

Ouros consequence:

A bath/soak event may count as ordinary rest only through the existing authoritative PTU rest rules and scenario timing. The thermal-place layer must never add HP, remove Injuries, cure status, refresh Moves, restore AP, grant Combat Stages or create a bespoke recovery multiplier because the water is described as therapeutic.

Cultural, commercial or personal statements such as “good for sore muscles” remain claims unless governing mechanics say otherwise.

## PTU campaign search result

This pass searched public PTU material for focused hot-spring/bathhouse campaign logs and actual-play examples. No source with sufficiently clear provenance and enough scene detail was found to justify extracting a distinct PTU-specific thermal-site pattern.

That absence is recorded rather than filled with weak attribution or homebrew rules.

## Low-authority community spatial inspiration

Pokémon Pokopia players publicly share bathhouse builds and report Pokémon visually congregating around spring amenities. These examples are useful only as evidence that a thermal amenity can read clearly as a social/public-space build in a Pokémon-flavored voxel world.

Examples:
- https://www.reddit.com/r/Pokopia/comments/1s60g50/hot_spring_bathhouse/
- https://www.reddit.com/r/Pokopia/comments/1s4wopy/i_was_inspired_by_the_idea_of_making_a_hot_spring/

Do not infer Ouros AI routines, attraction values, buffs or Pokémon preferences from Pokopia behavior.

## Reusable design lessons

1. Store thermal source state separately from bath/facility operation.
2. Let multiple downstream services depend on one source without forcing a single global “town broken” flag.
3. A visible Pokémon near a service failure is evidence of presence, not causation.
4. A long-running local belief can shape investigation and public response without becoming canonical truth.
5. Reopening requires verification; restoring source flow alone does not prove every pool, pipe or service is ready.
6. Thermal spaces can support recurring NPC schedules, leisure, conversations and information exchange.
7. Discovery access and routine access can differ over time.
8. A thermal site can overlap wildlife habitat, especially around outflow, warm ground or quiet-hours use, without making those Pokémon staff, owners or battle participants.
9. Therapeutic language belongs to claims and culture unless PTU/Caelo rules explicitly support a mechanical effect.
10. A successful intervention should leave history: repaired pipework, revised notices, changed access, new ecological observations, altered visitor pressure or a corrected local story.

## Canon questions raised, not answered

- Which Ouros regions have geothermal springs or other thermal waters?
- Are any bathhouses public, private, communal, institutional or hospitality-operated?
- What bathing customs, privacy rules or access practices exist by culture?
- Which sources are naturally geothermal versus artificially heated?
- Who owns/stewards a spring source, delivery infrastructure or bath facility?
- What testing/inspection practices exist before reopening?
- Are therapeutic claims culturally important anywhere, and how are they framed?
- Which thermal outflows or warm-ground areas have persistent Pokémon ecology?
- Which locations are visitor destinations versus ordinary neighborhood amenities?

No answer is established by this research pass.
