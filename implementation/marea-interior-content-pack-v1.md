# Marea Interior Content Pack v1

Status: IMPLEMENTATION CONTRACT
Depends on: `canon/ouros-playable-foundation-v1.md`

This file converts the first canon slice into concrete programming work.

## Content IDs

Locations:
- `ouros.marea.puerto_bruma`
- `ouros.marea.loma_clara`
- `ouros.marea.sendero_vidrio`
- `ouros.marea.estacion_mirador`

Factions:
- `ouros.faction.marea_field_office`
- `ouros.faction.loma_cooperative`
- `ouros.faction.tideglass_archive`
- `ouros.faction.bruma_battle_yard`

NPCs:
- `ouros.npc.mara_veyra`
- `ouros.npc.ivo_serrat`
- `ouros.npc.nerea_sol`
- `ouros.npc.taro_min`
- `ouros.npc.sela_orrin`

Named Pokémon:
- `ouros.pokemon.kite`
- `ouros.pokemon.pepa`
- `ouros.pokemon.lumen`
- `ouros.pokemon.margin`
- `ouros.pokemon.rook`

## Event state machine

`UNSEEN -> NOTICED -> INVESTIGATING -> EVIDENCE_ACCUMULATING -> CONVERGENCE_ELIGIBLE`

No automatic transition beyond `NOTICED` occurs because time passed.

### market_shortfall_notice
Prerequisites:
- arc state `UNSEEN`;
- player enters Market Hall activation volume during open service state.

Actions:
1. instantiate ordinary market presentation;
2. place Ivo in purchasing/service schedule slot;
3. expose observable shortfall through world-safe dialogue/environmental presentation;
4. write observation fact;
5. set arc state `NOTICED`.

Must not:
- pick a cause;
- spawn an antagonist;
- mark Loma Clara as failing;
- alter inventory mechanically without an economy owner.

### competing_explanations
Prerequisites:
- arc >= `NOTICED`;
- conversation with Ivo, Mara or Nerea.

Actions:
- retrieve speaker knowledge state;
- choose only hypotheses the speaker currently knows/believes;
- attach speaker provenance to every claim;
- unlock relevant evidence lane references;
- set arc state `INVESTIGATING` after first lane becomes available.

### evidence lanes
Each lane is independently completable and records evidence, not a universal quest-complete bit.

`lane.route_field_check`
Owner: Mara.
Primary locations: Field Office -> Sendero del Vidrio.
Class affinity: Survivalist, Backpacker, Rider, Capture Specialist, Commander.

`lane.archive_comparison`
Owner: Taro.
Primary location: Tideglass Archive.
Class affinity: Chronicler, Researcher, Sage, Hobbyist.

`lane.cooperative_visit`
Owner: cooperative contact; named contact not yet frozen.
Primary location: Loma Clara.
Class affinity: Chef, Commander, Mentor, Researcher.

`lane.mirador_records`
Owner: Nerea.
Primary location: Estación Mirador.
Class affinity: Researcher, Chronicler, Oracle where exact class mechanics permit.

`lane.market_substitution_log`
Owner: Ivo.
Primary location: Bruma Market Hall.
Class affinity: Chef, Hobbyist, Researcher.

## Multiclass/respec implementation

Quest eligibility is computed from:
- world prerequisites;
- current location/access;
- prior quest history;
- actor relationships;
- current authoritative class/Skill/Feature state only where a mechanic actually requires it.

Persist separately:
- `current_class_refs[]` from authoritative character build;
- `class_history_refs[]` narrative history;
- `class_arc_progress[class_id]`;
- `quest_episode_history[]`;
- `knowledge_refs[]`;
- `relationship_refs[]`.

A respec updates `current_class_refs[]`. It must not delete the other collections.

## NPC runtime schedules v1

These schedules are canon presentation defaults, not hard simulation requirements when an active authored event moves an NPC.

Mara Veyra:
- morning: Marea Field Office;
- afternoon: Field Office, docks or Sendero field assignment according to event state;
- night: off-stage unless an explicit incident requires presence.

Ivo Serrat:
- pre-dawn: Market Hall purchasing zone;
- morning/lunch: communal kitchen;
- afternoon: supplier desk/kitchen prep;
- evening: off-stage or authored market event.

Nerea Sol:
- observation day: Estación Mirador;
- archive-review day: Tideglass Archive during scheduled block;
- field event: authored transect position.

Taro Min:
- archive open hours: Tideglass Archive;
- interview evenings: archive interview room;
- otherwise off-stage/home state not yet spatially authored.

Sela Orrin:
- morning: Battle Yard maintenance/training;
- afternoon/evening: Battle Yard public session;
- can leave only through authored event state.

## NPC interaction minimums

Each named NPC requires implementation of:
- neutral greeting;
- first arc conversation;
- post-lane acknowledgment where relevant;
- unavailable/busy state;
- one relationship-memory callback;
- one class-sensitive dialogue hook where supported;
- one response after a player respec that does not pretend prior history vanished.

Exact dialogue prose is not frozen by this packet.

## Pokémon presentation minimums

Named companions require:
- stable UUID/identity mapping;
- species and nickname;
- owner/relationship link without reducing Pokémon to inventory;
- default presentation location near their partner where appropriate;
- explicit battle-eligible flag;
- authoritative PTU battle sheet reference before any BattleSpec inclusion.

Until audited, set `battle_eligible=false` for Kite, Pepa, Lumen, Margin and Rook in implementation content. This prevents presentation species from silently inventing mechanics.

## Battle handoff: Sendero Incident reduced contract

Preconditions:
- route lane active;
- encounter source selected from an audited future encounter table;
- explicit combatants resolved by Ouros;
- all combatant battle sheets validated.

Pre-battle:
- remove semantic cargo, civilians and investigation truth from BattleSpec;
- freeze positions/footprints and legal tactical state;
- create ordinary battle objective only.

Allowed result mapping:
- battle resolved with route opposition removed/withdrawn -> `IMMEDIATE_SENDERO_SEGMENT_CLEAR=true`;
- no other world inference.

Forbidden inference:
- `delivery_crisis_cause_known`;
- `wild_population_hostile`;
- `route_permanently_safe`;
- `cooperative_at_fault`;
- `weather_caused_shortfall`.

## Minecraft/Cobblemon implementation boundary

Minecraft/Cobblemon should implement presentation for:
- buildings;
- roads;
- schedules/visible NPC placement;
- named Pokémon models/entities;
- market and archive props;
- event indicators;
- battle playback.

Ouros owns:
- canonical NPC identity;
- schedule state;
- quest/event state;
- knowledge;
- relationships;
- faction state;
- named Pokémon identity;
- BattleSpec participants;
- aftermath.

AutoPTU owns tactical legality and battle outcomes.

Minecraft entity death/despawn, block destruction, inventory movement or proximity cannot independently mutate those facts.

## Immediate implementation backlog

P0:
1. persistent world-arc state keys;
2. stable NPC and Pokémon IDs;
3. event trigger/transition service;
4. quest evidence-lane records;
5. current-class vs class-history separation;
6. NPC schedule resolver;
7. reduced BattleSpec handoff contract.

P1:
1. map/chunk placement for four locations;
2. NPC models/skins;
3. named Pokémon battle-sheet audits;
4. Sendero encounter table;
5. Loma Clara cooperative contact roster;
6. dialogue content;
7. relationship callback rules.

P2:
1. richer escort/objective encounters after engine readiness;
2. dynamic weather/route hazards after capability promotion;
3. objective-aware tactical AI;
4. semantic adapter feedback from battle playback without authority leakage.

## Acceptance tests

- Starting a new world and entering Market Hall produces the notice exactly once.
- Speaking to different NPCs can expose contradictory attributed hypotheses without changing canonical truth.
- Completing one evidence lane does not complete the others.
- Changing Trainer classes does not delete completed lane history.
- Losing access to a class removes only current mechanics/class-gated options.
- A reduced Sendero battle can clear immediate access but cannot set the arc's cause.
- Despawning a named Minecraft NPC or Pokémon does not delete canonical identity/state.
- Re-entering a location reconstructs presentation from Ouros state rather than treating rendered entities as authority.
