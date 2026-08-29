# Air-Quality Monitoring & Airborne-Condition Seeds — Pass 119

Status: PROPOSED / NON-CANON. These are narrative candidates. They do not establish regional canon, PTU mechanics or environmental health rules.
Date: 2026-08-29

## Design intent

These seeds use air monitoring as persistent world state rather than as a generic poison cloud mechanic. Most can run without any tactical airborne effect.

Every seed preserves the distinction between observation, spatial interpretation, source attribution, health interpretation and downstream operational decisions.

## Situation seed — The Ridge Is Clear, the Valley Is Not

A ridge monitoring site reports its ordinary condition while a lower settlement records a meaningful change during the same afternoon.

The public initially treats the two reports as contradictory. The actual question is whether the sites sampled the same air mass, the same observation class and the same time window.

Useful actors:

- monitoring technician;
- valley shopkeeper who trusts the local reading;
- traveler who only saw the regional bulletin;
- event organizer deciding whether to move an activity;
- Pokémon observer with a long personal baseline for one location.

Possible consequences:

- a temporary valley monitor is deployed;
- the public map gains a clearer coverage annotation;
- an event relocates even though the ridge remains unaffected;
- the discrepancy becomes a future training example rather than a scandal.

No sabotage is required.

## Situation seed — The Smoke Is Visible, the Ground Reading Is Ordinary

A distant plume is plainly visible from a settlement. A local monitoring site does not show the same condition residents expected from the view.

The situation can generate pressure without deciding that the monitor is broken or that the plume is harmless.

Questions:

- what exactly was observed visually?
- what does the monitor measure?
- when was the reading taken?
- does the plume observation establish ground impact at this location?
- did a source-specific incident authority issue a separate assessment?

This is especially useful after a wildfire or volcanic episode because it forces the story to preserve source-event evidence and local-air evidence separately.

## Situation seed — Nothing Was Recorded From 14:20 to 15:05

A key monitoring site has a bounded data gap during the most disputed part of an episode.

The gap can result from maintenance, communications delay, access loss, quality review or an unknown cause.

The story should resist two easy mistakes:

- treating the missing interval as clean air;
- treating the gap as proof that someone concealed an adverse reading.

Other observers, photographs, neighboring sites or later technical review may narrow uncertainty without fabricating the missing measurement.

## Situation seed — The Temporary Monitor Became a Landmark

A temporary observation site is installed near a market or school during an episode. Months later the technical need ends, but the location has acquired social meaning.

Possible continuities:

- residents keep using the shelter beside it as a meeting point;
- a teacher starts an environmental-history club there;
- a Pokémon begins visiting the platform at the same time each morning;
- a replacement monitor is installed elsewhere but locals still call the old corner “the station”;
- archived notices posted there become evidence in a later investigation.

The technical deployment can end while the place remains narratively persistent.

## Situation seed — The Festival Went Indoors, the Market Stayed Open

Two institutions receive the same air-condition product and make different decisions because their activities, authority and risk assumptions differ.

The outcome should not imply that one institution ignored scientific truth. The event organizer, market operator, workplace, school and travel service each own their own operational decision.

Future consequences can include:

- complaints about inconsistent messaging;
- a later policy review;
- new indoor venue relationships;
- changed annual scheduling;
- public memory that simplifies several separate decisions into one story.

## Situation seed — The Pokémon Returned Before the Bulletin Changed

A group of Pokémon begins using a familiar rooftop or grove again before the current public assessment is revised.

Their behavior is a valid ecological observation. It does not automatically prove improved air quality, biological sensing, immunity or that officials are wrong.

The observation can trigger:

- a Conservation review;
- another monitoring round;
- comparison with prior seasonal behavior;
- renewed interest in old photographs;
- a local belief that later becomes either supported, weakened or unresolved.

## Situation seed — The Sky Looks Better Than Yesterday

Residents perceive a visibly clearer morning while the formal product remains unchanged or still carries uncertainty.

This seed examines the difference between appearance and bounded measurement.

Potential explanations should remain open until supported:

- actual improvement in one part of the area;
- a change in visibility with the relevant measured subject unchanged;
- delayed publication;
- different time windows;
- a product covering a wider region than the observers can see.

The story works even if nobody made an error.

## Situation seed — The Factory Closed, the Investigation Stayed Open

A facility stops operating during an air-condition episode, but the source investigation remains unresolved and monitoring continues.

The shutdown can be operational, precautionary, unrelated or part of another system's decision. The air-quality layer must not record `SOURCE_CONFIRMED` simply because the facility is visually plausible or temporarily closed.

Long-term hooks:

- another source hypothesis survives;
- measurements improve but causality remains uncertain;
- the facility reopens under a different operating arrangement;
- public belief remains fixed after the formal investigation changes direction.

## Situation seed — Two Maps, Two Audiences

A scientific operations map and a public bulletin show different geographic detail. Screenshots circulate without their timestamps or legends.

The mystery is solved through provenance:

- source product ID;
- intended audience;
- issue time;
- input sites;
- known gaps;
- revision chain.

The maps need not be contradictory.

## Situation seed — The Old Sampling Roof

A former municipal or research rooftop still contains mounting brackets, painted alignment marks, an obsolete cable route and a locked archive cabinet.

A new building blocks part of the old view. The monitoring equipment moved years ago, but old records still refer to the rooftop name.

This can support:

- environmental-history research;
- a missing-record mystery;
- a former technician NPC;
- photographs showing neighborhood change;
- Pokémon occupancy that changed as adjacent buildings changed use.

The roof itself can be fully safe and mechanically ordinary.

## Provenance mystery — Five Maps, One Afternoon

The player finds five depictions of the same episode:

- a raw point-monitor map;
- a temporary-sensor map;
- a spatially interpreted public product;
- a smoke/plume overlay;
- a later archived reconstruction.

They appear incompatible when compared as if every pixel were the same type of evidence.

Resolution structure:

1. identify each product;
2. establish its issue time;
3. identify direct observations versus derived areas;
4. recover monitor/network coverage;
5. identify revisions and backfilled evidence;
6. reconstruct what each institution knew at that time.

No map must be fraudulent for the mystery to be satisfying.

## Provenance mystery — Three Smells, Two Sources, Zero Proof

Three witnesses report different odors at different times. A visible industrial site and a distant fire both become popular explanations.

The player can establish chronology, wind observations from the Weather owner, source-incident timing, monitoring coverage and witness locations.

Possible outcomes:

- one hypothesis becomes better supported;
- the observations probably describe different events;
- evidence remains insufficient;
- a source case is handed to Pollution/Case Authority.

The story must not invent toxicity or health damage from odor alone.

## Exploration concept — The Station Above the Old Market

A monitoring station once occupied the roof of a market building that later changed use several times.

Exploration layers:

- current safe roof access;
- old maintenance route;
- former instrument mounts;
- archived photographs from several years;
- weatherproof record box or legitimate archive reference;
- neighboring buildings that altered the station's observation context;
- current Pokémon residents using parts of the roof.

The player reconstructs why a famous historical map had a coverage gap near the district edge.

Current executable version:

The site is static and safe. Investigation uses maps, provenance, NPC testimony and persistent IDs. No gas, smoke, dynamic visibility or exposure mechanic appears in BattleSpec.

Future rich version, only if governing rules and runtime support exist:

A live episode may make certain outdoor sections temporarily restricted or change visibility. That future variant depends on `terrain/weather/hazards/zones/reactions`, any exact LoS modifier, lifecycle ordering and semantic playback. It must not be implemented by Minecraft fog alone.

## Long arc — A Town Learns to Read the Air

Phase 1 establishes ordinary life before any crisis. Players see a monitoring roof, industrial district, schoolyard, market, ferry/road links, local wildlife and ordinary weather variation without treating every atmospheric change as danger.

Phase 2 introduces small disagreements between perception and records. A smell report, a visual haze report and a monitor observation refer to different scopes. The player learns how the information system works while stakes are still low.

Phase 3 begins a bounded episode. Temporary monitoring expands coverage. Different institutions respond differently. One popular source explanation weakens under later evidence. Public screenshots and revised maps create a provenance puzzle.

Phase 4 resolves the operational episode without requiring perfect causal certainty. Some restrictions end quickly; others require their owner systems to review separately. An old public belief may survive the formal closure.

Phase 5 preserves legacy. A temporary location becomes socially important, an annual event changes practice, archived products become teaching material and Pokémon occupancy changes become a research topic.

A later season can reactivate those records when a new haze/plume/odor event occurs. The system must compare the new evidence rather than declaring that “the old problem returned.”

## Encounter concept — Hilltop Monitoring Site Withdrawal

Narrative premise:

A temporary monitoring team must leave a hilltop site because a separate hostile encounter threatens the location. The scientific record and the immediate tactical conflict remain separate.

Full intended version:

Staff and equipment may withdraw while combat continues. Exact Intercept, forced movement and protection reactions may matter. If a validated airborne condition changes cells or visibility during rounds, the battle also uses dynamic environmental state.

Permanent capability dependencies:

- targeting/footprints/range/LoS: VERIFIED baseline; any dynamic visibility modifier requires exact governing evidence and the environmental family;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL if withdrawal or airborne state changes at lifecycle seams;
- full stateful damage pipeline: PARTIAL if a validated airborne effect causes damage;
- status lifecycle: PARTIAL if a validated effect applies status;
- terrain/weather/hazards/zones/reactions: BLOCKING for dynamic airborne zones/protection reactions;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for WITHDRAW/PROTECT;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING.

Current reduced version:

The team powers down or secures authored equipment and exits before BattleSpec. The monitored condition remains world-state information only. Ouros creates a static hilltop arena with explicit combatants. Victory may record `IMMEDIATE_MONITORING_SITE_PERIMETER_SECURED`; it does not validate readings, restore coverage, identify a source or clear any downstream restriction.

## Encounter concept — Community Hall Access Perimeter

Narrative premise:

A community hall has become an information/coordination point during an air-condition episode. A separate conflict threatens its exterior access.

Full intended version:

A rich implementation could include civilians withdrawing, protected access lanes and possibly an environmental zone if an exact PTU/Caelo effect exists.

Permanent capability dependencies:

- targeting/footprints/range/LoS: VERIFIED baseline;
- base movement legality: VERIFIED;
- complete movement: PARTIAL for escort/Intercept/forced movement;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL for timed withdrawal or changing boundaries;
- full stateful damage pipeline: PARTIAL for exact validated effects only;
- status lifecycle: PARTIAL for exact validated statuses only;
- terrain/weather/hazards/zones/reactions: BLOCKING for protection lanes or airborne zones;
- move-specific behavior / abilities / items / Trainer Features: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for PROTECT/WITHDRAW/HOLD_ACCESS;
- adapter/playback: BLOCKING.

Current reduced version:

All civilians and information staff move behind an authored secure boundary before combat. Any outdoor-condition effect is excluded from BattleSpec. The fight occurs in a static exterior approach. Victory can secure the immediate access area; it cannot declare the building healthy, end an episode or complete message receipt.

## Encounter concept — Sampling Roof Diversion

Narrative premise:

A rooftop team has already secured its samples/records when a conflict forces the party to clear an alternate exit route.

Full intended version:

A future implementation may combine rooftop hazards, changing visibility, reactions and route-clearing objectives.

Permanent capability dependencies:

- targeting/footprints/range/LoS: VERIFIED baseline;
- base movement legality: VERIFIED;
- complete movement: PARTIAL if displacement/Intercept matters;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL if route or condition changes by phase;
- full stateful damage pipeline/status lifecycle: PARTIAL if exact environmental mechanics exist;
- terrain/weather/hazards/zones/reactions: BLOCKING for roof/environment zones;
- move-specific behavior / abilities / items / Trainer Features: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for CLEAR_ROUTE/ESCAPE;
- adapter/playback: BLOCKING.

Current reduced version:

The sample/record handoff completes in world state before combat. Staff leave the roof. The remaining battle uses a reviewed static roof/access geometry with no active air-quality modifier. Victory establishes only immediate route security.

## Minecraft/Cobblemon presentation opportunities

Minecraft/Cobblemon can show monitoring huts, roof mounts, temporary instruments, notice boards, distant smoke/haze particles, changed sky presentation, NPC crews and authored Pokémon routines.

None of those visuals execute PTU rules.

A smoke particle does not create a hazard zone. Render fog does not impose a targeting penalty. A Koffing, Grimer, Torkoal or other visually relevant species does not establish the source or severity of an episode. Cobblemon BattleState remains outside combat authority.

## Canon questions intentionally unresolved

These proposals do not decide which regions monitor air, which technologies exist, what is measured, what public classifications exist, whether indoor-air systems are modeled, who can order operational restrictions, or whether any species has a verified monitoring role.

All such details require later canon approval or governing source evidence.