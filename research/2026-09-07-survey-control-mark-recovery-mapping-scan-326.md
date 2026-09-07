# Survey control, mark recovery & persistent mapping scan — Pass 326

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-07
Canon effect: NONE. External material below is inspiration/evidence, not Ouros canon or PTU rules authority.

## Why this slice

The repository already has archaeology, archives, mapping, travel, infrastructure, communication, environmental observation and institutional-decision systems. A dedicated scan for geodetic control, survey-mark recovery, disturbed reference points and map revision was not found in the recursive tree or repository searches before authoring this pass.

This slice focuses on a narrower reusable problem: a physical reference point can persist, move, be misidentified, become unreliable or remain correctly described while the surrounding landmarks change. That creates investigation and institutional consequences without requiring a villain or a battle mechanic.

## Source 1 — NOAA National Geodetic Survey: Survey Mark Recovery

URL: https://www.ngs.noaa.gov/surveys/mark-recovery/index.shtml

NGS describes survey marks as permanent marks or disks with known positional/elevation information and explicitly separates recovery from reliability. Damage, destruction or removal can compromise usefulness, and recovery reports record current condition.

Reusable Ouros structures:
- durable reference-object identity;
- recovery/inspection events with semantic time;
- condition history distinct from recorded coordinate history;
- public or institutional reports that may await approval;
- a mark can be found without being fit for authoritative use.

Do not copy real agency names, identifiers or administrative workflow into canon.

## Source 2 — NOAA NGS: Mark Descriptions Help

URL: https://www.ngs.noaa.gov/surveys/mark-recovery/mark-descriptions-help.shtml

NGS emphasizes detailed descriptions because similar marks can be misidentified. Condition categories also distinguish an apparently undisturbed mark from one whose damage or movement makes its stability doubtful.

Reusable Ouros structures:
- `OBJECT_FOUND != OBJECT_IDENTIFIED`;
- `OBJECT_IDENTIFIED != CONTROL_RELIABLE`;
- descriptions, markings, nearby references and photographs can corroborate identity;
- later field evidence may downgrade confidence without deleting historical records.

## Source 3 — USGS: reference benchmarks and reconstruction

URL: https://www.usgs.gov/media/images/cast-bronze-benchmark

USGS explains that reference marks can preserve azimuth/distance relationships to a triangulation station so the station can be re-established if lost.

Reusable Ouros structures:
- a missing primary reference need not make a site unsolvable;
- several surviving secondary references can reconstruct a prior control point;
- reconstruction is an inference backed by multiple measurements, not a magical restoration of the original object;
- environmental storytelling can place several mundane reference objects whose relationship matters more than any one object.

## Source 4 — NOAA NGS geodetic benchmark manual

URL: https://www.ngs.noaa.gov/PUBS_LIB/GeodeticBMs/

The manual describes how erosion, frost heave, soil movement and material deterioration can compromise benchmarks. It also stresses durable descriptions because vegetation grows, reference objects move and old marks may not be recovered for years.

Reusable Ouros structures:
- historical coordinates can remain valid records even when present physical control is no longer reliable;
- site change can be natural and cumulative;
- a field description can become stale because its reference landscape changed;
- maintenance, re-observation and replacement can produce lineage rather than overwrite.

## Source 5 — USGS: Benchmarking benchmarks

URL: https://www.usgs.gov/observatories/yvo/news/benchmarking-benchmarks

USGS describes benchmarks as durable reference points tied to a wider reference frame through surveying. This reinforces that a marker has meaning through relationships to other observations, not because a metal disk is intrinsically authoritative.

Reusable Ouros structure:

`PHYSICAL_MARK != REFERENCE_FRAME`

## Source 6 — NPS: Boundary Oak Tree

URL: https://www.nps.gov/places/the-boundary-oak-tree.htm

NPS documents a historical boundary that used a living tree as a survey point and property marker. The tree later died and disappeared, while the historical boundary evidence persisted through records.

Reusable Ouros structures:
- important spatial claims can outlive the original landmark;
- natural landmarks can be legitimate historical references without being permanent;
- later actors can disagree because they inherited different subsets of physical and documentary evidence.

No real property law, historical family or US metes-and-bounds system should be imported into Ouros.

## Source 7 — Pokémon Legends: Arceus official story material

URL: https://legends.arceus.pokemon.com/en-au/story/

The official site frames Survey Corps work as repeated excursions from a settlement base to study how Pokémon live, followed by return, reporting and preparation for later assignments.

Reusable Ouros structures:
- survey work can be a recurring adventure loop rather than a one-off fetch task;
- field evidence returns to an institution where it becomes records and future assignments;
- revisiting the same area with a better question can advance world knowledge;
- survey teams can have institutional duties without automatically knowing everything other teams observed.

Do not copy Hisui, Jubilife, the Galaxy Team, Survey Corps characters, requests or story beats.

## Source 8 — The Reckless Rollers PTU actual play

URL: https://podcasts.apple.com/us/podcast/the-reckless-rollers/id1505329084

Public listing identifies the main campaign as Pokémon Tabletop United and shows a long-running actual play plus shorter episodes from Pokémon-side perspectives.

Reusable Ouros lesson:
- a PTU campaign can sustain a long-running main continuity while occasionally changing viewpoint or encounter scale;
- a mapping/survey mystery can recur through different witnesses instead of demanding one exhaustive exposition scene;
- perspective changes are useful only when each actor receives evidence explicitly.

No characters, dialogue, plots or episode content are imported.

## Original Ouros design lessons

1. Stable ID and stable position are separate.
2. Historical position record and current reliable control are separate.
3. Finding a marker does not prove it is the correct marker.
4. Correct identification does not prove the object has not moved.
5. Missing primary control can sometimes be reconstructed from independent surviving references.
6. A changed landscape can make an old description stale without making the old observer dishonest.
7. Boundary, route and construction decisions should cite the evidence set used at decision time.
8. Later corrections append lineage. They do not erase the decision history produced from earlier evidence.
9. NPCs know only recovery reports, maps, field notes or direct observations they actually receive.
10. Minecraft marker geometry is presentation. It cannot author coordinates, property authority or PTU legality.

## PTU / Caelo cross-check boundary

The narrative repository currently exposes `sources/kairos` and no adopted `sources/caelo` directory was visible during this pass. The project README explicitly requires exact source validation before inventing navigation checks, movement capabilities, Trainer Feature effects, communication ranges or tactical environmental behavior.

This research therefore does not define:
- Survival or Education DCs;
- navigation bonuses;
- Topographer/Researcher/Survivalist Feature effects;
- Pokémon sensing ranges;
- special compass/GPS-equivalent mechanics;
- climbing, jumping or traversal costs;
- legal property/boundary authority;
- battle effects from survey equipment.

Any such mechanic remains UNVERIFIED until checked against the project-authoritative PTU/Caelo material and current AutoPTU contracts.

## Candidate implementation direction

Use survey-control mysteries as world-state investigations:

`reference feature -> historical record -> recovery observation -> identification assessment -> stability assessment -> actor receipt -> interpretation -> institutional spatial decision -> later verification/revision`

This is compatible with the global NPC AI because reports can travel through ordinary explicit recipients, archives can provide external evidence without rewriting memory, and changed spatial decisions can trigger route/work obligations without requiring tactical AI.
