# Rest, Sleep & Duty-Cycle Continuity Research — Pass 196

Status: RESEARCH / NON-CANON
Date: 2026-09-01
Narrative base inspected: `7187978b17553da62bfc39b5aae99cad7da11049`

## Scope

This pass researches sleep, ordinary rest, extended rest, overnight rhythm, watches, shift handoffs, camp downtime and time-of-day availability as narrative continuity problems.

The intended use is not a fatigue simulator. The goal is to let Ouros remember that people and Pokémon have hours when they work, stop, sleep, wake, hand responsibilities over, miss events, resume interrupted plans or choose to wait for a better time, while leaving PTU mechanical recovery under PTU/AutoPTU authority.

## Repository duplication audit

The complete current repository path inventory was inspected before selecting this seam. All files in `canon/` were then read directly, together with the root README and the implementation packet for Marea Interior.

Existing layers already cover nearby concerns:

- `travel-transport-expedition-layer.md` models journeys and staging sites, but explicitly does not create camping/rest mechanics;
- hospitality/lodging work covers guest stays and rooms;
- care/recovery covers treatment and medical continuity;
- community education and supervised-practice layers cover learning and competency;
- weather, ecology, schedules, expeditions and public services can all create time-specific activity;
- `maritime-coasts-depths-layer.md` already owns tide/current/sea-state and tidal-access-window structure, so this pass deliberately did not create a second tide system;
- the Marea implementation packet already gives several NPCs meaningful morning, afternoon and evening schedule anchors.

Searches for `sleep`, `rest sleep fatigue overnight`, and related dedicated layer terminology did not return a current Narrative subsystem dedicated to sleep/rest continuity.

The useful gap is therefore narrow: represent periods of rest and duty coverage without inventing healing, fatigue, exhaustion or sleep-condition mechanics.

## Canon anchors already available in Marea

Current canon provides enough ordinary-world structure to use this seam without adding a new institution.

Puerto Bruma has boarding rooms and a clinic/care station. Mara has morning Field Office responsibilities and variable afternoon work. Ivo begins purchasing before dawn. Nerea has observation, archive and field-work days. Taro has archive hours and interview evenings. Sela has morning maintenance and afternoon/evening public sessions. Lia and Mina operate around ferry activity. Ema works at Mirador and on transects. Jace helps with Battle Yard sessions and maintenance.

These facts make changes of shift, early observation windows, delayed departures and overnight staging plausible consequences of established work. They do not establish 24-hour staffing, labor law, mandatory rest periods or any specific sleep schedule.

## Public-source findings

### Pokémon Tabletop United 1.05 Core — Resting

Public source: Pokémon Tabletop United 1.05 Core, Combat / Resting section.

Source URL:
`https://peda.net/p/josajoki/fista/ohjeet/ptu/pokemon-tabletop-united-1.05-core%3Afile/download/c109e0ecc0ac41065575a4a324183b80189a2c70/Pokemon%20Tabletop%20United%201.05%20Core.pdf`

Relevant structure, paraphrased:

- PTU defines Rest by the absence of rigorous physical or mental activity; sleep is a common example, but rest is broader than sleep.
- Rest can restore HP in timed increments under explicit daily and Injury constraints.
- PTU separately defines an Extended Rest by a continuous-duration threshold.
- Extended Rest has additional mechanical consequences involving Persistent Status Conditions, Drained AP and Daily-Frequency Moves.
- Pokémon Centers are a distinct recovery path with their own timing and Injury interaction.

Design lesson: Narrative must never use `slept`, `used a bed`, `player skipped time`, `NPC was off-stage`, or `camp scene completed` as a shortcut for applying PTU recovery. A recorded period can be submitted to the authoritative rules layer for adjudication when the implementation supports it.

The supplied AutoPTU source set also contains PTU rest-related material and content that can modify resting behavior. That reinforces the need to avoid a hard-coded narrative healing rule. Current AutoPTU-Java search did not locate an end-to-end Rest/Extended Rest resolver by those terms during this pass.

### Pokémon Legends: Arceus — Base camps and chosen time advance

Sources:

- Bulbapedia, `Base camp`: `https://bulbapedia.bulbagarden.net/wiki/Fieldlands_Camp`
- Bulbapedia, `Time`: `https://bulbapedia.bulbagarden.net/wiki/Morning`

Legends: Arceus lets a player use quarters or a base-camp tent to rest and choose whether to advance to a later time-of-day boundary. It also couples the action to game-specific party healing.

Reusable structure:

- a rest location can be a persistent world node;
- a player may choose a target time rather than waiting through every minute;
- time advancement and recovery are separate design concerns even when one game presents them in the same interaction;
- returning to a camp can alter which time-sensitive observations or encounters are available.

Ouros transformation: a bed, room, field shelter or camp may expose a `wait/rest until` interaction, but Narrative records the requested interval and resulting world clock only after validation. PTU recovery remains a separate authoritative adjudication. Legends: Arceus full healing is not imported.

### Pokémon Mystery Dungeon: Explorers — daily institutional rhythm

Sources:

- Bulbapedia, `Wigglytuff's Guild`: `https://bulbapedia.bulbagarden.net/wiki/Wigglytuff%27s_Guild`
- Bulbapedia, Explorers of Sky Chapter 2 walkthrough: `https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Mystery_Dungeon:_Explorers_of_Sky/Chapter_2`

The guild places sleeping rooms, evening meals, morning assembly/announcements and daily job selection inside one recurring institutional rhythm.

Reusable structure:

- day boundaries can create handoff points rather than simply reset a quest board;
- sleeping space can establish where an actor plausibly begins the next period;
- morning information can differ from what was known the previous evening;
- a job, report or board can change while the protagonist is asleep because other actors continue to work.

Ouros transformation: a new day can surface changed schedules, delivered correspondence, updated route information, revised records or tasks completed by other residents. It should not respawn an identical universe or force a ceremonial morning scene every day.

No distinctive dialogue, character, guild plot or wording is imported.

### Fan-game day/night implementation — selective temporal significance

Source: PokeXGames Wiki, `Day and Night System`:
`https://wiki.pokexgames.com/Day_and_Night_System`

Its documented design explicitly concentrates the virtual-clock system in selected missions, areas, NPC rotations and spawn-time cases instead of using time to obstruct broad progress.

Reusable lesson: time-of-day gains value when it changes a specific opportunity or observation. It becomes friction when every service or quest exists only during narrow windows without alternatives.

Ouros transformation: schedule state should create different people, evidence or routes through an episode. Routine access can compress or offer a wait option when no meaningful decision is lost.

### PTU community search

Public searches for PTU camping, overnight watches and sleep procedures returned scattered equipment/build discussions rather than a consistent campaign-level subsystem that could safely be treated as PTU authority.

No homebrew watch initiative, fatigue meter, sleep-deprivation penalty, camp ambush table or sleeping-gear bonus is imported from community posts.

## High-level reusable structures

### 1. Narrative rest interval and mechanical rest adjudication must be separate

A useful world record can say that an actor stopped work at a place for a period. A separate authoritative operation decides whether that period satisfies PTU Rest or Extended Rest and what mechanical recovery follows.

This preserves both world continuity and rules parity.

### 2. Duty coverage can change while a character rests

Institutions do not require every named NPC to remain available at all times. A handoff can preserve:

- active task;
- latest known facts;
- pending response;
- equipment or key custody;
- who currently has operational responsibility;
- who should be contacted if conditions change.

This lets NPC absence produce believable world motion without inventing a staffing bureaucracy.

### 3. Interruption should preserve history

If a planned rest interval is interrupted, the world should remember:

- when it began;
- why it ended;
- whether the actor returned to rest later;
- which responsibility caused the interruption;
- whether the governing PTU engine credited any mechanical rest.

Narrative should not silently concatenate separated intervals into a continuous Extended Rest.

### 4. Waking and readiness are different facts

An actor can be awake while unavailable, busy, traveling, treating a case or preparing equipment. Conversely, an authored emergency may wake someone who was off duty.

`AWAKE` is therefore not a universal availability flag.

### 5. Overnight world progression should be bounded

Other actors may perform already-authorized ordinary activity while the player sleeps or waits. The simulation should resolve traceable scheduled work and existing clocks, not generate arbitrary crises merely because time advanced.

### 6. Time-specific ecology requires evidence

Night-active or dawn-active Pokémon activity can exist when species data, current ecology state or observations support it. The clock alone does not invent a species, migration or encounter.

## Strong boundaries for Ouros

The following separations should remain explicit:

- `NARRATIVE_SLEEP_RECORD != ENGINE_APPLIED_EXTENDED_REST`
- `BED_USED != HP_RESTORED`
- `TIME_SKIPPED != PTU_REST_CREDITED`
- `OFF_STAGE != ASLEEP`
- `AWAKE != AVAILABLE`
- `REST_INTERRUPTED != PTU_STATUS_CONDITION`
- `ORDINARY_SLEEP != PTU_SLEEP_STATUS`
- `NIGHT_SHIFT != FATIGUED`
- `MISSED_WAKE_EVENT != NEGLIGENCE`
- `NOCTURNAL_POKEMON != HOSTILE_POKEMON`
- `PLAYER_OFFLINE != CHARACTER_SLEEP`
- `MINECRAFT_BED_ANIMATION != CANONICAL_REST_COMPLETION`
- `SERVER_RESTART != WORLD_NIGHT_PASSED`

## PTU/Caelo mechanical boundary

The rest rules themselves are mechanical source material, not design freedom.

Before executable PTU recovery is added, validate at minimum:

- the exact Rest and Extended Rest definitions in the project's pinned ruleset;
- HP-restoration timing and Injury constraints;
- Persistent Status removal;
- Drained AP restoration;
- Daily-Frequency Move restoration;
- any content that changes normal resting behavior;
- Pokémon Center/equivalent treatment interactions;
- whether Caelo changes any of these rules;
- whether the current Java engine owns these transitions end-to-end.

Do not add:

- fatigue or exhaustion meters;
- sleep-deprivation penalties;
- generic night perception penalties;
- watch-order initiative bonuses;
- camp-quality healing multipliers;
- sleeping-bag bonuses;
- mandatory sleep quotas;
- invented wake-up checks;
- automatic PTU Sleep status when someone is narratively asleep.

## Current engine cross-check

AutoPTU-Java head inspected during this pass: `09fc8bcf22c18d3106718a9d98005aae501a41d4`.

Its newest change freezes the pinned Python semantic-event obligation around Insectoid Utility + Wallclimber forced-movement prevention. The change explicitly states that Java can preserve prevention provenance internally without yet exposing the Python event. This is useful evidence about one Trainer Feature interaction and one forced-movement path, not proof of complete movement or complete Trainer Feature support.

Search for an `Extended Rest` / `Resting` resolver in AutoPTU-Java returned no matching implementation in this pass. Absence of a search hit is not proof that no related recovery code exists under other names. It is sufficient reason not to claim rest support without a direct contract/test.

AutoPTU remains pinned at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its head change is presentation-only viewport synchronization and explicitly does not alter battle rules or outcomes.

## Caelo uncertainty

A literal `Caelo` search across the three current repositories returned no indexed result in this run. The root Narrative README nevertheless identifies Caelo Player's Guide, rulebook/errata, character-creation material and the Caelo Region Location & Encounter List as authoritative project sources.

Until those materials are directly available through an indexed source path, do not invent:

- mandatory sleep or watch procedures;
- regional curfews or quiet hours;
- labor/rest law;
- standard camp services;
- official lodging categories;
- Caelo-specific recovery changes;
- night travel restrictions;
- cultural rules around waking or hospitality.

## Originality note

This pass imports only high-level structures: continuous rest versus interruption, day-boundary handoffs, selectable time advancement, institutional daily rhythm and selective temporal significance. It does not copy protected dialogue, maps, distinctive characters, guild plots, healing presentation or fan-game schedules into Ouros.

## Recommended first implementation candidate

`Mirador First-Light Handoff` should be the first narrative slice.

It can reuse Nerea and Ema, existing Mirador geography and existing schedule/evidence systems. It requires no new species, no battle, no fatigue rule and no PTU recovery implementation. The point is to prove that an observation window, an actor's availability and a subsequent handoff can cross a day boundary while preserving who personally observed what.