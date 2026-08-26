# Weather Forecast, Observation & Preparedness Scan — Pass 63

Status: RESEARCH / PROVENANCE. Not Ouros canon.
Date: 2026-08-26

## Research question

How can Ouros make weather feel like a persistent part of ordinary life, travel, research, ecology, public services and adventure preparation without treating every forecast as truth or inventing unsupported PTU weather mechanics?

This pass deliberately extends, rather than replaces, the existing Seasonality, Calendar & Phenology layer. That layer already separates calendar, climate expectation, observed weather, overworld presentation and optional tactical Weather. Pass 63 focuses on the operational chain that was still missing:

observation -> forecast -> dissemination -> preparation -> actual conditions -> verification -> revised local knowledge.

The narrative goal is to make weather matter before combat begins and after it ends.

## Internal overlap review

The repository tree and existing research/design files were inspected before writing.

Existing systems already own these domains:

- Seasonality / Calendar / Phenology: world date, climate expectations, actual weather observations and recurring environmental timing.
- Travel: physical routes, services, incidents and route availability.
- Crisis / Rescue / Recovery: emergency lifecycle.
- Conservation: protected-area policy, migration corridors and stewardship.
- Science / Observation / Photography / Soundscapes: evidence and research provenance.
- Temporary Public Events: edition readiness, temporary services, cancellation or altered operation.
- Facility Maintenance: physical condition, inspection, work orders and reopening.
- Courier / Storefront / Staffing: downstream logistical and service consequences.
- Communications: information packets and dissemination.
- Rumor / Testimony / Local Knowledge: informal claims and local expertise.

Therefore Pass 63 does not create a second climate simulator, another travel graph, another emergency system or a generic weather-combat ruleset.

## Public source 1 — Weather Institute, Hoenn

Source: Bulbapedia, Weather Institute.
https://bulbapedia.bulbagarden.net/wiki/Weather_Institute

Observed reusable structure:

- a dedicated institution tracks weather across a region;
- the facility is integrated into a route rather than existing as detached lore;
- meteorological information can point toward unusual conditions in specific places;
- forecasts or reports can change where the player chooses to travel next;
- weather knowledge can become a reason to revisit the institution later.

In Pokémon Emerald, the Weather Institute meteorologist reports unusual drought or downpour conditions tied to particular routes. The useful design lesson is not the Legendary-specific plot. The useful structure is a persistent information service that converts observed regional anomalies into actionable location-specific leads.

Transformation for Ouros:

A weather or field-observation network can issue scoped products with location, validity window, confidence and revision history. A forecast should be a claim about future conditions, not a hidden trigger that rewrites the world to make itself correct.

Do not import:

- Hoenn institution names;
- Groudon/Kyogre plot structure;
- Castform ownership/reward structure;
- weather-control technology;
- exact route geography.

## Public source 2 — Unfair-Weather Friends / Weather Institute animation material

Sources:

- The Pokémon Company episode material for “Unfair-Weather Friends”.
- Bulbapedia episode summary AG083.

Reusable structure:

- travelers first experience abnormal weather as an immediate route problem;
- shelter and local expertise become relevant before the underlying cause is known;
- weather data, institutional records and equipment are story objects;
- rapid weather changes can motivate investigation without immediately proving a supernatural cause.

Transformation for Ouros:

Anomalous conditions should first appear as observations: sudden rain, visibility loss, wind, temperature shift, route closure, changed wildlife behavior or altered service. Investigators then compare station records, local reports and current observations.

A critical guardrail follows from the source: prediction, measurement and control are separate capabilities. The existence of weather research does not authorize Ouros to invent regional weather-control infrastructure.

## Public source 3 — Pokémon Legends: Arceus, Daybreak / massive mass outbreaks

Source: Bulbapedia, Daybreak and task documentation.
https://bulbapedia.bulbagarden.net/wiki/Daybreak

The Daybreak chain asks the player to investigate repeated phenomena across multiple regions. Rainstorms become an observed correlate of massive mass outbreaks only after field investigation.

Reusable structure:

- a recurring environmental condition can be correlated with a recurring ecological event;
- one region is not enough to prove the relationship;
- investigation moves across several locations;
- later observations can strengthen or revise a hypothesis;
- a weather-linked ecological pattern can become a persistent research program rather than a one-off quest.

Transformation for Ouros:

Forecast products may include ecological implications only when there is explicit evidence linking a condition to a local pattern. For example, a forecast of rain cannot generically produce “more Water-types”. A specific population may alter location or activity if Ouros observations establish that relationship.

Do not import the massive-mass-outbreak mechanic as a universal weather rule.

## Public source 4 — Castform and Forecast

Sources:

- Bulbapedia, Castform.
- Bulbapedia, Forecast Ability.

The important mechanical lesson is negative. Castform’s form response is governed by a specific Ability and specific weather states. It is not evidence that every weather-associated Pokémon predicts weather or that narrative weather can directly change species behavior in combat.

Transformation for Ouros:

A Pokémon may participate in weather observation only through authored evidence. A species association, Pokédex statement, known Move, Ability or observed behavior can support a role. Type alone cannot.

If a battle concept relies on Forecast or another weather-sensitive Ability, that exact Ability must be verified in AutoPTU rather than inferred from the narrative concept.

## Public source 5 — weather across Pokémon games and spin-offs

Source: Bulbapedia general weather documentation and Mystery Dungeon weather documentation.

Weather effects vary substantially across Pokémon games and spin-offs. Some systems change accuracy, damage, status, movement or other tactical properties; others use weather mainly as presentation or encounter context.

Reusable lesson:

“weather” is not one portable mechanic. Ouros must preserve the distinction between:

- observed atmospheric condition;
- forecast information;
- route or service response;
- ecology response;
- Minecraft presentation;
- PTU battlefield Weather.

The narrative repository must never select mechanics from a different Pokémon game merely because the same weather label appears.

## Public PTU campaign scan

A currently advertised Pokémon Tabletop United campaign, “Hoenn: Awakened”, uses strange regional weather as long-running campaign pressure while characters pursue ordinary institutional goals. This source is a campaign pitch rather than an actual-play transcript, so evidence weight is limited.

Reusable high-level structure only:

- persistent environmental instability can coexist with everyday progression;
- weather can remain a background question across many sessions;
- every appearance of bad weather does not need to become a boss fight.

No characters, plot reveals, supernatural causes or regional specifics are imported.

## Design findings

### 1. Forecasts need provenance

A forecast should record who or what issued it, what observations informed it, the geographic scope, issue time, valid window and confidence band.

A forecast without scope invites false omniscience.

### 2. Forecast and observation are different records

Observed rain is evidence about the present or past.

A prediction of rain is a claim about the future.

The world can contradict a forecast without retconning either record.

### 3. Revision is content

A new forecast can replace an earlier operational recommendation while retaining the earlier issued product in history.

Players can later inspect:

- what was predicted;
- what changed;
- which new observations caused the revision;
- who received the update;
- which organizations changed plans.

This creates fair investigative content without requiring a conspiracy.

### 4. Warning and authority are separate

An actor can publish a warning or recommendation without having legal authority to close a road, cancel an event or evacuate a settlement.

The relevant owner system must make that decision.

### 5. End of weather does not equal reopening

A storm ending does not prove that a road, bridge, ferry, trail, event venue or power system is safe.

Facility Maintenance, Travel, Public Works or the relevant service layer owns inspection and reopening.

### 6. Forecast error is not negligence

A forecast miss may result from:

- ordinary uncertainty;
- spatial scope mismatch;
- timing error;
- missing observations;
- sensor outage;
- local microclimate;
- changed conditions after issue;
- unusual but natural conditions;
- a real anomalous event.

Negligence, sabotage or deception require separate evidence.

### 7. Microclimates can create local stories

Two nearby sites can observe different conditions. That divergence should be documented before a cause is assigned.

The resulting investigation can connect geography, elevation, coastlines, vegetation, built environment or other authored factors, but should avoid fake scientific precision.

### 8. Preparedness is a world-state action

A forecast can justify decisions such as:

- moving an event indoors;
- delaying a ferry;
- staging repair crews;
- securing temporary structures;
- changing a research window;
- pre-positioning supplies;
- closing one trail;
- moving visitors away from a vulnerable area;
- adjusting a courier route;
- warning residents of a service interruption.

The forecast itself does not execute those changes. Each owner system records its own response.

### 9. Forecast verification creates institutional memory

After the valid window ends, the issuer can compare prediction and observation.

Persisted verification supports:

- better local expectations;
- recognition of blind spots;
- equipment maintenance;
- future staffing or station proposals;
- player trust based on visible history rather than a hidden reputation score.

### 10. Weather can create a quest without combat

Useful weather-centered tasks include:

- restoring a missing observation feed;
- checking a remote gauge or station;
- comparing two inconsistent reports;
- delivering a revised warning;
- documenting storm effects after conditions pass;
- verifying whether a closed route is physically safe;
- identifying which service never received an update;
- investigating why an ecological pattern differed from its expected weather linkage.

## PTU/Caelo and engine boundary

Pass 63 treats all meteorological operations as narrative/world-state unless an exact PTU/Caelo mechanic is validated.

Current AutoPTU-Java evidence is especially easy to overread. Java now contains a weather Damage Base calculation primitive, but the README still explicitly lists terrain, hazards, forced movement and reactions as unfinished and does not claim a complete battlefield-weather controller. One calculation helper cannot promote the permanent `terrain/weather/hazards/zones/reactions` category.

Current permanent classification remains:

VERIFIED:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## Transformation rules for Ouros

- Never make a forecast automatically come true.
- Never infer exact atmospheric science that canon has not established.
- Never infer a meteorological institution’s authority from its expertise.
- Never turn a weather warning into a combat debuff.
- Never infer Pokémon work capability from type or species association.
- Never import weather mechanics from another Pokémon game into PTU.
- Never make forecast confidence a hidden player-success modifier.
- Never use one unusual storm to prove climate change, supernatural intervention or sabotage.
- Never make a station outage prove that the station was attacked.
- Preserve prior forecast issues and revisions instead of overwriting them.
- Preserve actual observations even when they contradict expectations.
- Let downstream systems own closures, cancellations, reroutes, inspections and resource changes.

## Candidate Ouros value

The strongest contribution of this pass is a weather-information lifecycle that can run almost entirely before advanced combat support exists.

It creates persistent reasons to revisit weather stations, route offices, ports, research posts, farms, event sites and neighborhoods. It also gives previous layers a shared information input without forcing those layers to agree or respond identically.

Nothing in this research note establishes a specific Ouros weather service, climate, region, technology level, station network, warning vocabulary or institutional mandate. Those remain canon decisions.