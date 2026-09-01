# Ouros Playable Foundation v1

Status: CANON-APPROVED FOUNDATION
Date: 2026-09-01

This file freezes the first connected implementation slice of Ouros. Names and facts below are canonical unless later revised through an explicit canon migration.

## 1. Regional premise

Ouros is a lived-in Pokémon region whose settlements depend on each other through food, research, transport, archives, field services and Trainer institutions. Pokémon are integrated into daily work and ecology as individual actors, companions and wild populations rather than generic utilities.

The first playable district is the **Marea Interior District**, where a sheltered bay, agricultural uplands and an old survey road meet. The district is intentionally dense enough that early class questlines can repeatedly cross the same people and institutions.

## 2. Canon locations

### Puerto Bruma
`location_id: ouros.marea.puerto_bruma`

A working bay town and the initial service hub. It contains:
- Bruma Market Hall;
- Marea Field Office;
- Tideglass Archive branch;
- public battle yard;
- ferry landing;
- clinic and Pokémon care station;
- kitchens, repair stalls and boarding rooms around the market street.

Puerto Bruma is not a capital. Its importance comes from being the transfer point between coastal traffic and inland producers.

### Loma Clara
`location_id: ouros.marea.loma_clara`

An agricultural settlement above the bay. Mixed small producers supply berries, grains, vegetables, preserved foods and specialist ingredients to Puerto Bruma. The settlement has a cooperative storehouse, communal kitchen and field school.

### Sendero del Vidrio
`location_id: ouros.marea.sendero_vidrio`

The old survey road connecting Puerto Bruma and Loma Clara. It crosses scrub, seasonal watercourses and exposed stone shelves. It remains usable but requires maintenance after heavy weather. Several class arcs use it for observation, supply and fieldwork.

### Estación Mirador
`location_id: ouros.marea.estacion_mirador`

A small research and weather-observation station on the upper road. It maintains ecological observations, route reports and specimen records. It does not own regional truth: its records are claims with provenance and revision history.

## 3. Canon institutions and factions

### Marea Field Office
`faction_id: ouros.faction.marea_field_office`

A public-facing field-service institution coordinating route observations, wildlife incidents, missing-person searches and practical assistance between settlements. It is not a police force and does not automatically own captured or rescued Pokémon.

Natural class intersections: Capture Specialist, Survivalist, Researcher, Medic, Commander, Rider, Backpacker, Chronicler.

### Loma Clara Producers Cooperative
`faction_id: ouros.faction.loma_cooperative`

A cooperative that coordinates storage, shared deliveries and market representation while individual producers retain their own holdings and decisions.

Natural class intersections: Chef, Researcher, Survivalist, Commander, Mentor, Hobbyist.

### Tideglass Archive
`faction_id: ouros.faction.tideglass_archive`

A small regional archive and circulating library network. The Puerto Bruma branch preserves route surveys, oral-history deposits, old market records and copies of ecological observations.

Natural class intersections: Chronicler, Researcher, Sage, Rune Master, Oracle, Hobbyist.

### Bruma Battle Yard
`faction_id: ouros.faction.bruma_battle_yard`

A local battle and training institution. It supports ordinary audited Trainer battles, practice and community exhibitions. It is not yet canonically a Gym and grants no invented badge or progression reward.

Natural class intersections: Ace Trainer, Duelist, Commander, Stat Aces, Style Expert, Cheerleader and combat-oriented classes.

## 4. First regional pressure: The Thin Delivery Season

`world_arc_id: ouros.arc.thin_delivery_season`

CANON FACTS at campaign start:
- several Loma Clara deliveries have arrived smaller and less predictably than the previous local season;
- Puerto Bruma vendors disagree about whether the cause is production, route reliability, purchasing behavior or simple coincidence;
- Estación Mirador has incomplete but relevant weather and field observations;
- the cooperative has not declared a crop failure;
- no canonical cause has yet been established;
- ordinary residents continue daily life.

This is deliberately a question with several owners, not a scripted disaster.

Class entry lanes include:
- Chef: ingredient availability, substitution, producer relationships and food tradition;
- Researcher: evidence quality, ecological observations and competing hypotheses;
- Survivalist/Backpacker: route condition and field verification;
- Chronicler: historical delivery records and conflicting memories;
- Commander: coordination between actors without inventing authority;
- Capture Specialist: changes in wild Pokémon presence only when observations support them;
- Medic: care implications only if an actual care case emerges;
- Ace Trainer/Duelist: battle-yard relationships and field assistance, not automatic ownership of the investigation.

## 5. Canon NPC foundation

### Mara Veyra
`npc_id: ouros.npc.mara_veyra`

Role: coordinator at Marea Field Office.
Age band: adult.
Current PTU class concept: Commander / Survivalist.
Class implementation status: narrative identity is canon; exact mechanical sheet requires authoritative PTU build validation before battle use.
Personality: concise, practical, dislikes reports that erase uncertainty.
Motivation: keep the district functioning without turning every irregularity into an emergency.
Routine: mornings at the Field Office; afternoons vary between route review, dock meetings and field visits.
Relationships: professional working relationship with Ivo Serrat and Nerea Sol; frequent disagreement with vendors who want immediate categorical explanations.
Pokémon companion: **Kite**, a Corviknight used for travel and observation support. Exact level, Ability, Moves and combat loadout remain UNRESOLVED until PTU/Caelo/engine audit. Kite is not generic transport infrastructure.
Quest roles: initial field-service contact; Commander and Survivalist class-thread anchor; recurring convergence NPC.

### Ivo Serrat
`npc_id: ouros.npc.ivo_serrat`

Role: cook and purchasing lead at Bruma Market Hall communal kitchen.
Age band: adult.
Current PTU class concept: Chef / Hobbyist.
Personality: observant, social, stubborn about distinguishing scarcity from poor planning.
Motivation: keep ordinary meals affordable and preserve local dishes without pretending substitutions are identical.
Routine: pre-dawn purchasing; kitchen through lunch; supplier calls and recipe testing later in day.
Pokémon companion: **Pepa**, a Greedent that assists with ingredient sorting and storage observation. No mechanical harvesting/storage bonus is canon without audit.
Quest roles: Chef anchor; market-side witness for Thin Delivery Season; later bridge into food, hospitality and festival arcs.

### Dr. Nerea Sol
`npc_id: ouros.npc.nerea_sol`

Role: lead field researcher at Estación Mirador.
Age band: adult.
Current PTU class concept: Researcher / Chronicler.
Personality: methodical, willing to revise published conclusions, impatient with unsupported certainty.
Motivation: maintain a useful longitudinal record of the district.
Routine: station work on observation days; scheduled archive visits; field transects when conditions permit.
Pokémon companion: **Lumen**, a Heliolisk used as an individual field partner. No weather-prediction or electrical infrastructure power is inferred from species alone.
Quest roles: Researcher anchor; evidence/provenance tutorial; recurring source of hypotheses rather than omniscient exposition.

### Taro Min
`npc_id: ouros.npc.taro_min`

Role: Tideglass Archive branch custodian and local-history interviewer.
Age band: older adult.
Current PTU class concept: Chronicler / Mentor.
Personality: patient, exacting about dates and editions, comfortable preserving contradictory testimony.
Motivation: keep local memory usable without turning recollection into fact.
Routine: archive opening hours; two evenings per week reserved for recorded community interviews.
Pokémon companion: **Margin**, a Noctowl. Margin is a companion and observation partner; presence does not confer truth detection.
Quest roles: Chronicler anchor; Mentor crossover; archive access and historical-record threads.

### Sela Orrin
`npc_id: ouros.npc.sela_orrin`

Role: manager and senior trainer at Bruma Battle Yard.
Age band: adult.
Current PTU class concept: Ace Trainer / Duelist.
Personality: competitive but not theatrical; treats rematches as evidence of change rather than repetition.
Motivation: build a respected local training culture without pretending every strong Trainer needs a formal League title.
Routine: morning maintenance/training; public sessions afternoon/evening.
Pokémon companion: **Rook**, a Falinks. Exact battle sheet remains UNRESOLVED pending authoritative build audit.
Quest roles: Ace Trainer and Duelist anchor; audited ordinary-battle onboarding; connection between class identity and regional problems without making battle solve every problem.

## 6. Canon opening event chain

### Event 1: Market Shortfall Notice
`event_id: ouros.event.market_shortfall_notice`

Trigger: first campaign-day visit to Bruma Market Hall after world initialization.
Writes:
- `world_fact.thin_delivery_season.player_noticed = true`
- observation that selected deliveries are smaller/less predictable;
- no cause.

NPCs: Ivo Serrat, ordinary vendors.
Battle: none.

### Event 2: Competing Explanations
`event_id: ouros.event.competing_explanations`

Trigger: player has noticed shortfall and speaks with either Ivo, Mara or Nerea.
Behavior: exposes at least two attributed hypotheses. Hypotheses remain claims.
Class-aware presentation may surface different follow-up questions, but event truth is shared.

### Event 3: Choose an Evidence Lane
`event_id: ouros.event.choose_evidence_lane`

Available lanes depend on world access and player choices, not permanent class locks:
- inspect route condition with Field Office;
- inspect historical delivery records at Tideglass;
- visit cooperative contacts in Loma Clara;
- review Mirador observations;
- help Ivo document substitutions and missing lots.

Current classes may expose shortcuts, dialogue or mechanically governed options. A later respec does not erase completed lane history.

### Event 4: Sendero Incident
`event_id: ouros.event.sendero_incident_01`

This is the first optional battle handoff candidate.
Narrative premise: while a field lane is active, a localized Pokémon confrontation may obstruct immediate safe passage if current ecology state supports an encounter.

FULL version dependencies: complete movement if escort/interception is included; lifecycle for sustained route objectives; exact Moves/Abilities/Items/Features; AI tactical policy for objective-aware behavior; adapter/playback.

REDUCED version: noncombatants and semantic route objects remain outside BattleSpec. AutoPTU resolves an ordinary audited battle. Allowed world output is only `IMMEDIATE_SENDERO_SEGMENT_CLEAR`. It cannot establish the cause of the delivery irregularity or ecological truth.

## 7. Implementation variables v1

Required persistent keys:
- `ouros.arc.thin_delivery_season.state`
- `ouros.arc.thin_delivery_season.player_noticed`
- `ouros.arc.thin_delivery_season.hypotheses_seen[]`
- `ouros.arc.thin_delivery_season.evidence_refs[]`
- `ouros.arc.thin_delivery_season.lanes_completed[]`
- `ouros.route.sendero_vidrio.current_access_state`
- `ouros.faction.marea_field_office.relationship_state`
- `ouros.faction.loma_cooperative.relationship_state`
- `ouros.faction.tideglass_archive.relationship_state`
- per-NPC encounter/knowledge refs rather than one global friendship score.

## 8. Explicit non-canon / unresolved implementation fields

Do not invent yet:
- exact regional map coordinates and Minecraft chunk positions;
- exact NPC skins/models;
- exact Trainer levels/stats/Edges/Features;
- exact Pokémon levels/Natures/Abilities/Moves/Items;
- encounter tables for Sendero del Vidrio;
- exact economy/prices;
- final cause or resolution of Thin Delivery Season;
- formal League/Gym hierarchy;
- global government structure;
- whether every proposed class is available at campaign start.

These are implementation tasks to resolve against source material and engine readiness, not permission to silently improvise in runtime.

## 9. Design intent

This foundation creates a small world where the same five NPCs and four institutions can support multiple class identities. It follows PTU guidance that character-centric interests, ordinary Trainer activity and central plot should weave into each other rather than compete for play time. It also follows the PTU expectation that Trainers commonly combine several narrow classes, so no NPC or quest assumes a single permanent class identity.
