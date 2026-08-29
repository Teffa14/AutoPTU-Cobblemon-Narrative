# Ouros Narrative Research — Building Safety, Occupancy & Reentry Assessment — Pass 122

Status: RESEARCH ONLY. This file records provenance and reusable design lessons. It does not establish Ouros canon, building law, structural-engineering rules or PTU mechanics.
Date: 2026-08-29

## Why this gap was selected

The repository was inspected recursively before writing. Existing layers already cover facility faults/repair/verification, residential habitability/relocation, crisis response, civic public works, seismic events, wildfire, slope instability, workplaces and route access.

A narrower continuity gap remains between acute danger and later repair: after a building or structure has been affected, who has observed which area, what use is currently allowed, which portions remain restricted, what evidence caused a restriction to change, and whether a later review superseded an earlier one.

This pass therefore researches building-safety assessment and reentry continuity without creating a universal building-code simulator.

## Public Pokémon sources

### Old clock tower — damage, hidden condition and changed disposition

Source: https://bulbapedia.bulbagarden.net/wiki/Clock_tower
Source: https://bulbapedia.bulbagarden.net/wiki/BW008

The animated-series clock tower is an old landmark whose apparent decline leads toward demolition. Investigation reveals a specific hidden physical problem involving the bell support and a resident Darmanitan. After the immediate problem is resolved, the town changes the building's future from demolition toward restoration and continued use.

Reusable high-level lessons:
- visible disrepair and actual failure mechanism can be different facts;
- a building can have cultural/ecological occupants whose presence matters to later decisions;
- emergency stabilization, repair, restoration and future-use decisions are separate transitions;
- discovery can change a planned disposition without erasing the earlier record.

Ouros transformation:
A damaged landmark can retain an assessment history, temporary restrictions, a stabilization event and a later reuse/restoration decision. Pokémon observations remain evidence about individual actors and occupancy, not proof of structural condition or technical competence.

No characters, dialogue, episode resolution, bell mechanism or town are copied into canon.

### Prism Tower ruins — cleanup, persistent damage and public reuse

Source: https://bulbapedia.bulbagarden.net/wiki/Prism_Tower

Recent Pokémon material depicts a heavily damaged major structure whose surrounding plaza can be cleaned up and reopened while the ruined tower remains physically present. Later material treats restoration of the landmark as a separate future concern.

Reusable high-level lessons:
- cleanup of a surrounding area can finish before restoration of the principal structure;
- public access can return to one spatial scope while another remains damaged;
- ruins can become a persistent part of a living city's current identity instead of disappearing after a crisis;
- reopening should be recorded per area/use rather than as one building-wide boolean.

Ouros transformation:
A site may contain multiple assessment scopes: plaza, exterior setback, entrance, floor, room, roof, adjacent structure or service area. Each scope can carry its own restriction and review history.

No plot, named factions, characters, hyperspace mechanics or exact redevelopment outcome are imported.

### Pyrite Building — renovation and changed use across time

Source: https://bulbapedia.bulbagarden.net/wiki/Pyrite_Bldg

The Pyrite Building appears first as a run-down storage building and is later renovated and repurposed as an organization headquarters.

Reusable high-level lessons:
- a persistent structure can change condition, operator and function while retaining historical identity;
- renovation can close one narrative era without deleting evidence from the previous use;
- later stories can gain meaning from the contrast between former and current use.

Ouros transformation:
Building identity survives repair, restriction changes and adaptive reuse unless canon explicitly retires the structure. Assessment records remain historical provenance after reopening.

### Withered Wasteland Pokémon Center — rubble to rebuilt service

Source: https://bulbapedia.bulbagarden.net/wiki/Withered_Wasteland

A Pokémon Center in this setting begins as rubble after extreme weather and is later rebuilt by local actors.

Reusable high-level lesson:
A service's history can include destruction, absence, rebuilding and resumed use. Physical reconstruction and service restoration should have explicit milestones rather than an instant reset.

Ouros transformation:
Facility Maintenance continues to own repair work and service owners continue to own operational restoration. The new continuity layer only preserves safety-assessment/reentry decisions and their evidence.

## PTU community source

### Environment matters, but homebrew terrain is not governing evidence

Source: https://www.tapatalk.com/groups/pokemon_tabletop/need-help-with-gming-t5365.html
Source: https://www.tapatalk.com/groups/pokemon_tabletop/special-terrain-ptu-t3434.html

Public PTU discussion reinforces that spatial environment is important to tactical play. Separate homebrew discussion proposes detailed collapsing-terrain effects.

Reusable lesson:
Built environments can make encounters more legible and memorable when geometry and objectives matter.

Mechanical guardrail:
Community homebrew is provenance, not PTU/Caelo authority. A suggested collapse, falling-object, forced-movement, damage or difficult-terrain rule must never be promoted into Ouros merely because a public GM used or proposed it.

## Operational reference sources

### FEMA P-2055 — post-disaster evaluation and revision

Source: https://www.fema.gov/sites/default/files/2020-07/fema_p-2055_post-disaster_buildingsafety_evaluation_2019.pdf

FEMA's post-disaster building-safety guidance distinguishes evaluation categories, permits restricted use, and explicitly allows an earlier posting to change after reevaluation or a subsequent event. It also distinguishes technical evaluation from the governing authority that controls official posting decisions.

Reusable architecture lessons only:
- an assessment result has a timestamp, scope, evaluator and authority basis;
- restrictions can be partial rather than binary;
- a later assessment may supersede an earlier one while preserving history;
- changed conditions can trigger reevaluation;
- technical advice and official authorization can be separate records.

Not imported:
- FEMA/ATC placard colors or labels;
- US legal authority;
- evaluator qualifications;
- inspection procedure;
- occupancy criteria;
- engineering thresholds;
- disaster-program requirements.

### FEMA P-2055-1 — advisory versus authorized evaluation

Source: https://www.fema.gov/sites/default/files/documents/fema_rm-p-2055-1-guidance-accelerated-building-reoccupancy_012023.pdf

This guidance provides a useful conceptual distinction between an evaluator who supplies technical advice and an authority that makes the final official reoccupancy decision.

Ouros use:
Store `technical_assessment` and `occupancy_authorization` as separable objects. Canon decides whether a region combines those roles or assigns them to different institutions.

### USGS structural monitoring — evidence can supplement visible inspection

Source: https://earthquake.usgs.gov/monitoring/nsmp/buildings/
Source: https://earthquake.usgs.gov/monitoring/nsmp/buildings/evolution.php

USGS material describes post-earthquake assessment needs and the value of instrumented structural observations. It also highlights that visible inspection may not reveal every relevant condition.

Reusable architecture lessons:
- observation source matters;
- visible condition, instrument reading, technical interpretation and occupancy decision are distinct evidence layers;
- `NO_VISIBLE_DAMAGE_OBSERVED` must not become `STRUCTURE_PROVEN_SAFE`;
- missing or unavailable monitoring should remain an evidence gap rather than a reassuring default.

No seismic thresholds, engineering models or code provisions are imported.

## Cross-check against internal PTU/Caelo evidence

The internal source scan confirms that Caelo can give a location explicit mechanical identity when a governing source defines the effect. It does not establish universal structural collapse, falling debris, unstable floor, crushing, falling, rescue/carrying, rubble movement or building-reentry mechanics.

The PTU/Caelo material currently available to the project therefore supports narrative location identity and ordinary legal battle mechanics only where exact source rules exist. Architectural safety state must remain world-state logic unless a specific governed mechanic is later verified.

## Reusable Ouros design principles

1. Assessment scope must be explicit. One room, floor, wing, plaza or adjacent route can differ from the rest of the site.
2. Observation, technical interpretation, restriction and authorization remain separate records.
3. A restriction can tighten or loosen after later evidence without deleting the earlier decision.
4. Repair completion does not automatically authorize reentry.
5. Reentry does not prove every service is operational.
6. A public area can reopen while an adjacent damaged structure remains restricted.
7. A building can preserve historical identity through damage, restoration and adaptive reuse.
8. Pokémon presence can be an ecological/social fact without becoming a structural diagnostic.
9. Missing evidence must remain unknown.
10. Minecraft appearance never becomes safety authority.

## Candidate narrative structures

### Layered reopening

A familiar civic building is affected by a prior incident. Exterior access returns first, then one service area, then a second floor. Another wing remains restricted for weeks. NPC routines and businesses adapt around the partial reopening.

### Conflicting but valid signs

Two public records seem contradictory because one applies to an exterior plaza and one to an interior floor. A mystery resolves through scope and revision history rather than exposing a liar.

### The building that changed jobs

A damaged warehouse is repaired for a different public use. Former workers, current occupants, nearby Pokémon and old route names all preserve different pieces of its history.

### Reinspection after a second event

A building already reviewed after one incident experiences an aftershock, storm, fire, nearby excavation or other authored trigger. The previous assessment remains historically valid for its time but no longer answers the current question.

## Mechanical dependency warning

A narrative about assessment and reentry needs no battle implementation by itself. Tactical scenes inside actively unstable structures are different.

If an encounter uses falling debris, changing cells, collapse, unstable floors, moving machinery, smoke, fire, flooding, aftershocks, dynamic exclusion zones, rescue carrying, forced displacement or reaction windows, the exact relevant capability families must be declared. Visual rubble or a damaged Minecraft build never proves those rules exist.

## Provenance and canon boundary

Everything in this scan is RESEARCH/PROPOSED inspiration unless an existing Ouros file explicitly establishes a fact.

This pass does not establish:
- any Ouros building code;
- any government inspection authority;
- engineer or inspector professions;
- universal placards;
- structural formulas;
- mandatory evacuation/reentry rules;
- repair standards;
- liability;
- property ownership;
- Pokémon construction abilities;
- automatic building damage from Moves;
- any new PTU terrain or status rule.

Those remain canon/rules questions for later approval.