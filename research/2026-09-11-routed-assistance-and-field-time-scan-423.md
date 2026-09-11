# Routed assistance and field-time research — Pass 423

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Retrieval date: 2026-09-11

Repository inspection basis

The recursive repository tree at narrative head `c39cd4676c4102503a811f23b2ae5c6af954c57e` was inventoried before research. `CURRENT_FOCUS.md`, the complete `canon/` inventory, canon governance, Pass 418–422 consequence/observation/delivery/replanning/action-intent chain, the information queue, private knowledge ledger, Marea resident network, recent research/proposals and `sources/kairos/KAIROS_SOURCE_INDEX.md` were checked before writing.

Repository-wide searches found no prior research entries under the titles `Pentiment`, `Roadwarden` or `PTU Night Rangers: Hollow Underdeep`. The pass does not reopen previously processed source anchors such as Unavowed, Invisible Inc., Outer Wilds, Pokémon Starwish, Pokémon Unchosen, Pokémon Hollow Woods, Pokémon Lithic Veil, Pokémon Memories, Pokémon Space Pog Jam or Aipom's Great Pirate Adventure.

## Source 1 — PTU Night Rangers: Hollow Underdeep

Public source: StartPlaying Games campaign listing, `PTU Night Rangers... "Hollow Underdeep" - Underdark Poké-Fantasy`.

URL: https://startplaying.games/adventure/cmtrrpyqw00d7jl04r0mm82kx

The public campaign pitch describes a PTU expedition whose Rangers cross an old underground route, deliver four eggs and help a separated community. Its historical setup frames the Rangers as a connection point between communities that once traded and traveled together before old routes disappeared.

Reusable high-level lessons for Ouros:

- a field role can be valuable because it connects people and institutions, not because it wins battles;
- carrying a request, observation, specimen or protected delivery can be a full adventure objective;
- old or difficult routes create communication latency and local uncertainty without requiring magical isolation;
- reconnecting two groups can begin with one bounded delivery rather than an immediate faction merger or global state rewrite;
- a courier or field liaison needs an explicit sender, destination, route and arrival event.

Do not copy the Hollow Underdeep, Night Rangers identity, Bellow, the four eggs, history, geography, NPCs, encounters, dialogue or campaign plot.

## Source 2 — Pentiment design interview

Public source: MMORPG.com, `The RPG Files: Building Obsidian's Pentiment: Interview With Game Director Josh Sawyer`.

URL: https://www.mmorpg.com/interviews/the-rpg-files-building-obsidians-pentiment-interview-with-game-director-josh-sawyer-2000126821

The interview explains that investigation opportunities deliberately exceed the time available. Meals and other activities consume time, leads have availability windows, and the player must act under another person's timetable while accepting incomplete information and consequences.

Reusable high-level lessons for Ouros:

- a request reaching someone does not create unlimited time to act on it;
- receiving new information should compete with existing commitments instead of overriding them automatically;
- some opportunities can remain valid yet become impractical because travel, work or another duty consumed the available window;
- uncertainty can remain legitimate at decision time; the system should preserve what each actor actually knew when choosing.

Do not copy Pentiment characters, murder cases, accusations, setting, dialogue, clues, scenes or plot outcomes.

## Source 3 — Roadwarden design analysis

Public source: Jay McGavren, `Game Design Analysis - Roadwarden`.

URL: https://jay.mcgavren.com/2023/02/22/roadwarden-game-design-analysis.html

The analysis notes that travel between longer-distance locations consumes meaningful game time, while some local interactions do not, and that the overall journey operates under a finite day budget. It also calls out the importance of keeping the player oriented through map and journal access.

Reusable high-level lessons for Ouros:

- communication and assistance requests can have a world route/time cost distinct from the eventual task;
- long-distance response should be represented by travel or message latency rather than teleporting an NPC because a quest needs them;
- request history should stay inspectable so later scenes can explain whether a person never knew, knew too late, or knew and chose another priority.

Do not copy Roadwarden's world, characters, monsters, locations, quest content, prose or specific progression rules.

## Combined Ouros design candidate

The strongest shared structure is a three-stage field-coordination loop:

1. one actor decides that another person's assistance would be useful;
2. that request travels as an ordinary information event with a real channel, latency and provenance;
3. only after receipt may the requested person weigh the request against their own schedule, duties, travel and knowledge.

This preserves independent NPC agency. `REQUEST_SENT`, `REQUEST_RECEIVED`, `REQUEST_ACCEPTED` and `ASSISTANCE_STARTED` are separate world facts.

The structure is useful for Marea only as a regression site. Mara may request Teo, Oren, Nerea, Lia or another resident when their established responsibilities make them relevant, but the request itself cannot silently assign them. The same architecture must work globally for future regions and institutions.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes world-running questions to the Kairos living-world material and PTU campaign/session guidance while routing mechanical actions to their actual rule chapters. Kairos evidence supports persistent off-session activity and one-shot quest structure, but it does not grant Ouros a new communication, travel or battle rule.

Any future request that becomes a structured PTU action must revalidate current character state and use the explicit AutoPTU handoff. Narrative role labels such as repairer, Medic, Researcher or Ranger never grant Features, moves, Items or tactical permissions by themselves.

## Capability impact

The reduced coordination form requires no battle implementation. It uses durable world-action intent, private knowledge, information delivery, semantic time, schedules, obligations, permissions, travel and event-driven replanning.

A mechanically rich version may begin or end inside an escort, rescue, retrieval or extraction encounter. In that form the permanent engine categories must be evaluated individually: targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

No representative implementation is treated as proof that an entire category exists.
