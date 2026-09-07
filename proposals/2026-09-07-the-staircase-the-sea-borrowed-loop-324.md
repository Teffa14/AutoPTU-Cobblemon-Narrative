# The Staircase the Sea Borrowed — Pass 324

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

A coastal settlement uses an old stepped route cut into a rocky shoreline to reach a lower survey shelf, service niche and small landing. One report says the route is open. Another says the lower access is underwater and should remain closed. A third actor insists they used the stairs recently and found fresh evidence below.

All three statements may be accurate.

The player must establish which persistent coastal features are usable during which tidal window, which observations remain current, and what decision should govern the next scheduled movement of people, supplies or Pokémon.

No region, settlement, institution, species population, economic dependency, final explanation or PTU mechanic in this proposal is canon-approved.

## Why this belongs in Ouros

The site changes without becoming a different map. Tide phase modifies access and what can be observed while feature identity, history and prior decisions persist.

The loop also exercises the global NPC architecture. Different actors may receive observations from different tide windows and make reasonable but incompatible decisions without hidden-state leakage.

## Persistent site features

### Upper marker terrace

A permanently accessible reference point above ordinary tide reach. It contains route markers, notices, an observation post or old survey marks.

Narrative purpose: establishes a stable comparison point and prevents the entire location from becoming temporally ambiguous.

### Borrowed staircase

A stepped route that descends through multiple exposure bands. Upper steps may remain dry while lower steps are submerged.

Narrative purpose: access is feature-scoped. `STAIRCASE_EXISTS` never means `ALL_STEPS_CURRENTLY_PASSABLE`.

### Lower survey shelf

A rocky or hard-surface platform exposed only during a suitable low-water phase.

Possible evidence:
- maintenance marks;
- recently moved debris;
- ecological observations;
- a damaged marker;
- a service cache;
- an old repair seam;
- a deposited object whose source remains unresolved.

### Tidal channel

A narrow water-filled separation between the shelf and another feature. Its width/depth may change by authored world phase, but Pass 324 does not invent current vectors, Swim costs or jumping rules.

### Service niche or landing

A small persistent feature used by workers, fishers, researchers, couriers or another institution. Its use can produce records, custody traces and scheduled obligations.

## Investigation loop

The player begins with several bounded claims.

A route worker can truthfully report that the upper stairs and marker terrace were inspected and opened.

A field observer can truthfully report that the lower shelf was inaccessible during their visit.

A courier can truthfully say they reached the service niche during an earlier low-water window.

The player can compare timestamps, route-feature IDs, authored tide phase, local marks, logs, communications and later observations.

The intended deduction is narrow:

`this observation supports this claim about this feature during this tide window`

The player is never required to infer a real-world tide table from astronomical data.

## Open explanations

Keep several explanations viable until canon review selects one or leaves uncertainty durable.

- The upper route was correctly reopened while the lower shelf remained phase-limited.
- Two actors visited during different valid tide windows.
- A public notice referred to the staircase generally even though only the upper section was continuously usable.
- A service team used a maintenance-only low-water window that ordinary travelers could not rely on.
- A marker was moved by water between observations, making an older report look inaccurate.
- A deposited object was interpreted as evidence of recent human passage but originated elsewhere.
- Ecological activity altered the appearance of a surface without altering route legality.
- A later weather or swell event invalidated an earlier observation without falsifying it.
- Several causes coexist.

Sabotage or supernatural causation is unnecessary.

## Actors and pressures

### Coastal route authority

Goal: maintain access without publishing a dangerously broad statement.

Knowledge boundary: receives only explicit reports and publications. It does not know the current state of every lower feature by default.

### Survey or ecology team

Goal: access the lower shelf during a useful observation window and preserve data provenance.

Knowledge boundary: knows its own visit, instruments and observations, not every subsequent tide phase.

### Service worker, courier or harbor operator

Goal: reach the landing or niche before a scheduled obligation is missed.

Narrative pressure: timing has economic or logistical consequence without turning the actor into an antagonist.

### Local resident or fisher

Goal: preserve practical access based on lived experience.

Narrative use: may possess strong local timing knowledge while still lacking formal authority or the latest institutional notice.

### Resident Pokémon

Species remain unresolved. Future coastal species can provide bounded observations only after ecological and mechanical validation. They are never automatic tide gauges, route-authority substitutes or omniscient hazard detectors.

## Decisions and persistent consequences

Possible decisions include:
- keep upper terrace permanently open;
- mark lower stairs as tide-window access only;
- reserve the service niche for maintenance during one phase;
- delay a delivery;
- publish a narrower correction to an earlier broad reopening notice;
- move a monitoring point higher;
- retain a lower ecological observation zone while restricting casual access;
- schedule a later revisit rather than force immediate resolution.

Consequences can persist as missed deliveries, delayed fieldwork, altered staffing, stale public notices, damaged trust, changed schedules, relocated equipment, ecological observation gaps or later review.

A corrected notice does not erase the earlier publication or the consequences it already caused.

## Revisit structure

The same location should support returns:
- at a different tide phase;
- after a storm or swell event;
- after repair work;
- during another season;
- when a previous route decision affects an NPC obligation;
- when a species observation is expected during a specific exposure window;
- when an old object or marker reappears after being submerged.

## Reduced implementation version

The reduced version uses authored semantic tide states rather than physical tide simulation.

Example world descriptors:
- `TIDE_HIGH`;
- `TIDE_FALLING`;
- `TIDE_LOW_WINDOW`;
- `TIDE_RISING`;
- `UPPER_ROUTE_OPEN`;
- `LOWER_ROUTE_WINDOWED`;
- `LOWER_ROUTE_SUBMERGED`;
- `SERVICE_ACCESS_MAINTENANCE_ONLY`;
- `OBSERVATION_STALE_AFTER_PHASE_CHANGE`.

These are narrative/world-state descriptors, not PTU statuses.

Unsupported tactical spaces become blocked route edges or authored scene boundaries. Tide transitions occur between structured encounters or through explicit world events outside AutoPTU.

The full investigation, NPC knowledge boundaries, publication corrections, scheduling pressure and durable consequences remain intact.

## Intended mechanically rich version

A future rich encounter may include changing water coverage during a tactical scene, exposed and submerged footing, moving water hazards, rescue/interception, forced displacement, underwater or partially obscured LoS, dynamic access to objectives, environmental reactions or Pokémon-assisted traversal.

Those mechanics are optional. They may only activate when their exact capability families and PTU/Caelo rules are verified.

Minecraft/Cobblemon/Craftics may render the waterline and route state after receiving authoritative state. It must not create missing PTU rules to make the scene appear dynamic.

## Dependency classification

Targeting / footprints / range / LoS: ordinary verified contracts are enough for the reduced version. Underwater vision, surface distortion, spray/fog concealment or changing water occlusion require dedicated evidence beyond ordinary LoS.

Base movement legality: ordinary movement works on authored open surfaces. Slippery footing, wading, swimming, climbing, jumping gaps or species-specific aquatic traversal require source-backed contracts.

Complete movement including push/pull/knockback/interception/forced movement: required for currents, wave displacement, rescue pulls, interception or knockback near water. Current evidence remains partial.

Core calculations: ordinary deterministic calculations remain usable. No tide equation, buoyancy formula, drowning meter or water-pressure arithmetic is introduced.

Action economy / initiative: ordinary ordering is available. Custom rescue actions, environmental interrupts or tide-control actions require exact legal contracts.

Full turn/round lifecycle: required for waterline changes, timed exposure windows, repeated environmental pulses or within-battle phase transitions. Current evidence remains partial.

Full stateful damage pipeline: required for any impact, fall, crushing, drowning-like or environmental damage. Current evidence remains partial.

Status lifecycle: required for any persistent mechanical condition. The reduced version creates none.

Terrain / weather / hazards / zones / reactions: required for dynamic water coverage, wave/current sectors, changing safe zones, slippery terrain or rescue reactions. Current evidence remains mixed/partial/blocking by subfamily.

Move-specific behavior: every Move used for water manipulation, terrain change, movement, rescue, concealment or environmental damage must be verified individually.

Abilities: every Ability used for aquatic movement, water interaction, weather, detection, protection or environmental response must be verified individually.

Items: ropes, markers, survey instruments or coastal gear remain narrative objects until exact mechanics are source-backed.

Trainer Features / perks: Survivalist, Topographer, Climatologist, Researcher or comparable specializations require project-authoritative verification before granting modifiers, access or interrupts.

AI legal-action infrastructure: may enumerate only already supported legal actions.

AI tactical policy: general autonomous reasoning about changing water coverage, evacuation, rescue, timing windows or dynamic coastal hazards remains blocking.

Minecraft / Cobblemon / Craftics adapter/playback: may present waterline, exposed geometry, route markers and authoritative events. It must not decide route truth, legal movement, damage, statuses, NPC knowledge or outcomes.

## Canon questions deliberately unresolved

Region; coast type; settlement; route name; responsible institution; tidal regime; economic use; service niche purpose; resident species; ecological significance; exact history of the stair; final explanation for conflicting reports; whether the route stays public; exact PTU/Caelo mechanics; and whether a rich tactical version is desirable all remain unresolved.