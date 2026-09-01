# Marea Phenology & Migration Seeds — Pass 178

Status: PROPOSED / NON-CANON
Date: 2026-09-01
Depends on: `design/ecological-phenology-migration-continuity-layer.md`

These candidates use canonized Marea sites/residents while leaving species, exact ecological calendars and migration routes uncanonized unless explicitly stated otherwise.

## 1. Three Mornings at Mirador

Anchor: Estación Mirador + transect trailhead
Residents: Dr. Nerea Sol, Ema Rey, Jo Venn
Status: LOW-RISK / RECOMMENDED FIRST IMPLEMENTATION

Premise:
Two existing field sheets appear to disagree about whether a recurring wild-Pokémon presence is common near the transect trailhead. Nerea suspects the comparison is poor because one record came from a short late-morning visit and the other from a complete early transect.

Player work:
- perform comparable observations on three separate mornings;
- record start band, duration, route completion and disturbance notes;
- submit `DETECTED`, `NOT_DETECTED` or `OBSERVATION_BLOCKED` rather than guessing abundance;
- compare the new series with older Tideglass copies.

Possible outputs:
- `PHENOLOGY_WINDOW_CANDIDATE_CREATED`
- `OLDER_RECORD_NOT_COMPARABLE`
- `NO_PATTERN_YET`

Mechanical dependency:
world/quest/observation state only. No battle required.

Design value:
This teaches the player that repeated comparable observation is useful gameplay and that absence cannot be inferred from one empty visit.

## 2. The Crossing Window

Anchor: Sendero del Vidrio seasonal crossing
Residents: Mara Veyra, Nerea Sol, Ema Rey
Status: PROPOSED; species intentionally unspecified

Premise:
Historical reports suggest a recurring group may pass through or near the seasonal crossing during a narrow part of the district calendar. The current year has only weak preliminary signs.

Player work:
- inspect current route state;
- compare prior Field Office and Mirador records;
- place observation points without blocking the crossing;
- update Mara's operational guidance only after direct evidence.

Possible outcomes:
- `POSSIBLE_ARRIVAL`
- `ACTIVE_PASSAGE_CONFIRMED`
- `EXPECTED_WINDOW_NO_DETECTION`
- `ROUTE_SHIFT_SUSPECTED`

Guardrail:
No species, destination, breeding purpose or exact trigger is canonized by this seed.

Mechanical dependency:
reduced form requires no battle.

## 3. The Missing Stopover

Anchor: a canon site adjacent to the Sendero; exact ecological use remains proposed
Residents: Nerea Sol, Mara Veyra, Taro Min

Premise:
A place used in several older observation records has no current detections during the expected window.

The story is about a missing pattern, not a missing Pokémon count.

Investigation branches:
- observation effort changed;
- access/noise changed;
- resource condition changed;
- the expected window is wrong this year;
- the group is using another site;
- evidence is insufficient.

Player work:
- repeat a comparable observation;
- inspect current site condition;
- retrieve older source records;
- avoid escalating to `population collapse` without evidence.

Mechanical dependency:
none unless a later authored encounter is separately approved.

## 4. Ferry Noise, Fewer Sightings

Anchor: Puerto Bruma ferry landing
Residents: Lia Morn, Mina Cors, Nerea Sol, Ema Rey

Premise:
After a ferry schedule change or maintenance period, residents report fewer sightings of an ordinarily observed wild presence near the landing.

Competing hypotheses:
- actual route shift;
- timing shift;
- observation became harder because of noise/traffic;
- the original comparison used different effort;
- ordinary stochastic variation.

Player work:
- compare sightings at matched time bands;
- correlate ferry operating windows without claiming causation;
- optionally recommend a low-cost observation window away from active unloading.

Possible output:
`DETECTABILITY_CHANGE_CANDIDATE` rather than `WILDLIFE_DECLINE`.

Mechanical dependency:
world/service/observation state only.

## 5. One Pokémon Behind the Window

Anchor: Sendero del Vidrio or Mirador branch
Residents: Mara Veyra, Oren Vale, Nerea Sol
Status: INDIVIDUAL WELFARE + ECOLOGY

Premise:
During a recurring movement window, one wild Pokémon is observed repeatedly behind the main visible group.

Safe questions:
- is this the same individual across observations?
- is it delayed, resting, injured, or simply using the route differently?
- is the main group still nearby?

Possible persistent-individual promotion:
Only if repeated evidence or care interaction makes identity matter.

Player options:
- observe from distance;
- report to Mara/Nerea;
- request Oren's involvement if an actual care case is evidenced;
- help maintain an unobstructed route without touching/capturing the Pokémon.

Guardrails:
No parent/child relation, herd leadership, ownership or PTU status is inferred.

Mechanical dependency:
non-combat version needs observation/care workflow only.

## 6. The False Outbreak

Anchor: Loma Clara edge or another existing Marea observation site
Residents: Alba Ríos, Jo Venn, Nerea Sol, Mara Veyra
Status: TEMPORARY AGGREGATION STUDY

Premise:
Many wild Pokémon are visible in one small area over a short period. Public language starts calling it an invasion or outbreak.

Player work:
- register a temporary aggregation record;
- document species actually observed;
- compare nearby resource/site conditions;
- correct public wording if evidence does not support the stronger claim;
- check whether the concentration persists after the temporary condition changes.

Possible outcomes:
- `TEMPORARY_AGGREGATION_CONFIRMED`
- `MULTIPLE_GROUPS_PRESENT`
- `PERSISTENCE_UNKNOWN`
- `PUBLIC_INVASION_CLAIM_UNSUPPORTED`

Mechanical dependency:
none. The presence of many visible Pokémon does not require tactical instantiation.

## 7. First Arrival Board

Anchor: Estación Mirador / field school / Tideglass
Residents: Nerea Sol, Ema Rey, Jo Venn, Pia Min
Status: INSTITUTIONAL CANDIDATE

Premise:
Mirador maintains a public-facing seasonal board showing first detections, last detections and confidence notes for selected non-sensitive ecological events.

Important design rule:
The board publishes observations and forecasts, not hidden world truth or rare nest locations.

Player contribution:
- submit a field report;
- attach comparable observation metadata;
- see an entry revised later if better evidence arrives.

Long-term value:
A simple board can make the changing ecological year visible in Minecraft without requiring hundreds of active entities.

Mechanical dependency:
world object + quest/communications state only.

## 8. Old Year, New Route

Anchor: Tideglass Archive -> Sendero -> Mirador
Residents: Taro Min, Pia Min, Nerea Sol, Mara Veyra

Premise:
An archived route sketch records a recurring movement path from years ago. Current observations no longer line up with it.

Player work:
- preserve the old route as historical evidence;
- gather current observations;
- produce a new route-shift hypothesis;
- avoid silently moving the old record's coordinates.

Possible outcomes:
- `HISTORICAL_ROUTE_RETAINED`
- `CURRENT_ROUTE_SHIFT_SUPPORTED`
- `INSUFFICIENT_CURRENT_EVIDENCE`

Mechanical dependency:
no battle.

## 9. Corridor Under Pressure

Anchor: future authored Sendero encounter space
Status: MECHANICALLY RICH / FULL VERSION BLOCKED

Narrative premise:
A recurring wild movement corridor intersects an active route problem. The player needs to keep the corridor and a human work path from collapsing into the same dangerous space while a small subset of wild Pokémon is physically present.

### Full intended version

Possible tactical elements:
- exact grid lanes representing a narrow crossing;
- wild participants attempting to move through rather than simply defeat opponents;
- interception or forced movement near a bottleneck;
- dynamic route/hazard zones;
- weather or surface phases if supported by the authored incident;
- Trainer Features/perks that affect positioning or intervention;
- tactical AI choosing legal movement toward exit objectives;
- Minecraft/Cobblemon playback showing the same authoritative movement/results.

Required permanent capability families:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected content needs it;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current status: BLOCKED for full version.

### Reduced executable version

The migration/corridor remains world state outside BattleSpec.

Flow:
1. Mara closes or restricts the human work path based on server-owned route state.
2. The player observes the visible subgroup from a safe point.
3. The player clears ordinary debris or coordinates work only through already-supported world verbs.
4. If a separate hostile encounter is authored, it occurs on stable terrain away from the moving group and only after exact parity audit.
5. The authoritative battle may emit a narrow consequence such as `IMMEDIATE_OBSERVATION_ROUTE_CLEAR`.
6. World logic, not battle victory, decides whether passage continues.

Combat cannot establish:
- why the migration exists;
- the total population size;
- future route safety;
- environmental causation;
- whether the whole group passed successfully;
- whether the corridor is permanently restored.

## 10. Marea Phenology Ledger

Anchor: Estación Mirador with Tideglass copies
Residents: Nerea Sol, Ema Rey, Taro Min, Pia Min
Status: LONG-TERM SYSTEM CANDIDATE / HIGH VALUE

Premise:
Mirador maintains a durable year-to-year ledger of selected ecological timing observations.

Candidate record types:
- first detection;
- last detection;
- repeated route use;
- stopover use;
- temporary aggregation start/end;
- day/night activity shift;
- unusual missing detection;
- forecast revision.

The ledger stores:
- observation IDs;
- sampling protocol;
- confidence;
- environmental context;
- contradiction/correction history.

It does not store omniscient true population counts.

World payoff:
After enough cycles, players can notice that an event is early, late, shifted or poorly sampled. This produces future research and operational hooks from accumulated world history rather than from random quest generation.

Mechanical dependency:
no battle.

## Recommended implementation sequence

First: `Three Mornings at Mirador`.

Reason:
- uses existing canon residents and fixed sites;
- requires no new species canon;
- exercises repeated observation, time, evidence quality and physical field-note surfaces;
- can use the RPG adapter's proven persistent quest-object and normal-world provisioning patterns;
- produces durable state that later migration content can consume.

Second: `First Arrival Board`.

Reason:
- makes ecological change visible to players without spawning a crowd of Pokémon;
- reuses communications/public-information systems;
- allows corrections and forecast uncertainty.

Third: `The Crossing Window` after a specific Marea species/collective is approved through ecology/canon review.

## Canon boundary

None of these proposals establish:
- a specific migratory species in Marea;
- exact migration dates;
- fixed population counts;
- breeding seasons;
- a migration festival;
- a new settlement/site;
- a new faction;
- weather causation;
- new PTU mechanics;
- automatic hostility from wild groups;
- ecological authority from Cobblemon spawns.

Promotion requires explicit canon and source review.