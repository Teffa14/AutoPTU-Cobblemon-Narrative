# Ouros inland waterways, canals, locks & navigation candidates — Pass 154

Status: NON-CANON PROPOSALS. Requires continuity, originality, PTU/Caelo and implementation review before promotion.
Date: 2026-08-24

These candidates assume the proposed architecture in `design/inland-waterways-canals-locks-navigation-layer.md`. Names are placeholders unless separately approved.

## Thirty worldbuilding and adventure candidates

### 1. The Lock That Works but Cannot Be Used

A recently serviced lock passes every mechanical inspection. The upstream navigation reach remains too restricted for the loaded vessel waiting below it. Public rumor calls the repair a failure; the actual problem is elsewhere in the network.

### 2. Two Boats, One Chamber

A passenger ferry and a time-sensitive research craft reach the same lock window. The interesting decision is operational priority and downstream consequence, not a battle for first place.

### 3. The Ferry Is Running, Freight Is Not

A shallow passenger service continues while deeper cargo traffic is held. Shops still look normal for several days before the supply consequence becomes visible.

### 4. Low Water, Full Reservoir

A public reservoir looks healthy, yet a shoal farther downstream limits navigation. The apparent contradiction triggers a survey rather than an accusation.

### 5. Tomorrow’s Water

Operators can improve one navigation window by changing a managed release, but other water-use claims also exist. The decision becomes a transparent institutional trade-off with follow-up monitoring.

### 6. The Rescue Boat Is First in Queue

A routine lock queue reorganizes when an Emergency Services craft arrives. Later, several delayed passengers tell different stories about why their service was late.

### 7. Debris Boom Full

A floating-debris control asset reaches capacity after storms upstream. Removing material is Public Works/Navigation work; identifying where unusual material came from becomes a separate investigation.

### 8. The Canal That Became Habitat

A low-traffic branch canal gradually acquires wetlands, nesting areas and a walking route. A proposal to restore regular navigation must account for the new ecological history rather than assume the old use automatically overrides it.

### 9. Night Lockages

A maintenance period shifts traffic toward nighttime. Nearby residents notice noise, workers change schedules and different Pokémon activity is observed. None of those consequences automatically makes the schedule wrong.

### 10. The Portage Market

A historical transfer point around an unnavigable reach developed into a small market. Even after a modern lock opens, the market survives because it acquired its own social function.

### 11. The Blocked Passage

A large wild Pokémon rests in a narrow approach where vessels cannot safely pass. Conservation and operators suspend traffic while observers determine whether the event is temporary. Removal/capture is not the default objective.

### 12. The Lockkeeper’s Notebook

Old handwritten operating notes reveal repeated seasonal constraints that never entered the digital archive. The notes are evidence of practice, not proof that every old interpretation was correct.

### 13. Gate Sensor Disagreement

The control display reports a gate secured while a second observation source disagrees. The lock is held pending verification. The mystery can end as a sensor fault without sabotage.

### 14. The Chamber With Two Names

A lock chamber was expanded and renamed, but older maps, workers and local residents still use the previous designation. Identity resolution prevents two maintenance records from being mistaken for two structures.

### 15. Emergency Bypass

A temporary passenger shuttle around an out-of-service lock becomes unexpectedly popular. When the lock reopens, the settlement must decide whether the temporary connection should remain.

### 16. Migration Week Hold

A documented migration crosses an approach reach during a short seasonal window. Operators institute a temporary hold that was once informal and later becomes a recurring public notice.

### 17. Cargo Arrived by Road Instead

A navigation closure does not make a consignment disappear. Supply Chains reroutes it by road at higher logistical cost and with a different arrival time.

### 18. The Canal Town After Commerce

Freight traffic gradually shifts to rail. The canal town keeps its locks, waterfront, former warehouses and institutional memory while reinventing its economy around research, tourism, local ferries or habitat restoration.

### 19. The Dredged Reach Refilled

A maintained channel returns to restricted condition sooner than expected. Competing hypotheses include sediment input, survey differences and an outdated model. No one is blamed before evidence exists.

### 20. Research Vessel Locked Out

A research crew reaches a site but cannot pass a scheduled maintenance closure. Their sampling program changes, creating a future gap in a long-term dataset.

### 21. The Towpath Outlived Towing

An old towpath becomes a public trail, emergency access route and wildlife corridor. Navigation heritage remains visible even though its original operational role disappeared.

### 22. One Closure, Three Consequences

The same lock outage delays a postal transfer, changes a market delivery and prevents a mobile clinic from following its normal route. Each downstream layer records its own consequence.

### 23. The Waterway Map Is Correct for Last Year

A published chart correctly represents the last surveyed navigation channel but no longer matches the newest river geometry. Cartography and navigation revisions diverge without either record being fraudulent.

### 24. Floating Habitat at the Approach

A mass of floating vegetation or debris becomes temporary habitat near a lock approach. The operational problem and ecological value coexist.

### 25. Repair Parts Downstream

The component needed to reopen an upstream lock is itself delayed by the closure. A road/rail transfer solves the logistics problem without creating a contrived combat objective.

### 26. The Retired Lock

A lock is decommissioned but its chamber remains as heritage infrastructure, pedestrian crossing and public landmark. Minecraft preserves the structure while navigation state records retirement.

### 27. The Canal Is Open but Nothing Moves

Water level, lock and channel are all normal. The scheduled operator/service is unavailable. The world correctly shows an open canal with no passenger movement.

### 28. The Same Ferry, Different Route

Over several years one persistent vessel changes landing pattern as settlements grow and bridges open. Its asset identity and maintenance history remain continuous.

### 29. Former Working Pokémon at the Landing

A Pokémon formerly associated with a navigation service is repeatedly observed near its old landing after retirement. The observation creates continuity, not an assumption that it wants to resume work.

### 30. Nothing Happened at Lock Four

A complete season of ordinary lockages, inspections and routine delays produces no adventure. Years later those records become the baseline that makes an unusual pattern visible.

## Longer-term arcs

### Five Seasons on Meridian Canal

Year 1 establishes ordinary passenger/freight service and a reliable lock sequence.

Year 2 brings a short low-water restriction. Cargo shifts temporarily to road while passenger ferries continue.

Year 3 adds a migration hold near one approach and creates a recurring ecological monitoring program.

Year 4 a major control-system modernization changes operator practice without changing the canal’s identity.

Year 5 an unrelated downstream geometry change causes restrictions despite the upgraded locks. Characters who remember the previous years understand immediately that “the lock is broken again” is the wrong simplification.

The arc can continue with increasingly capable institutions and fewer mandatory quests.

### The Lockkeeper Generations

An old lock passes through several generations of workers, controls, public notices and transport patterns. One family may be involved, but office/employment and kinship remain separate.

Useful callbacks include an old handwritten ledger, a retired operator correcting an institutional memory error, a successor declining to follow an obsolete custom, and modernization preserving rather than erasing earlier revisions.

### River Becomes Network

A natural river crossing begins with informal boats and portage. A landing is formalized, then a canal/lock link appears, then rail and road transfers connect to it. Decades later the waterway is only one component of a multimodal network.

This arc lets infrastructure grow without presenting technological change as automatically good or bad. Each revision produces new trade-offs, memories and alternate routes.

## Encounter contracts

### Lock Chamber Evacuation

Premise: An operational incident causes lockage to stop while a hostile or panicked combat-capable threat remains after workers/passengers are moved toward safety.

FULL version:

The encounter can include moving noncombatants, protected routes, chamber edges, changing access, interrupted lock state and possibly a dynamic water-level or gate constraint.

Permanent capability dependencies:

- targeting/footprints/range/LoS — required;
- base movement legality — required;
- complete movement including push/pull/knockback/interception/forced movement — required if actors can be displaced near restricted areas or routes change dynamically;
- core calculations — required;
- action economy/initiative — required;
- full turn/round lifecycle — required for full parity;
- full stateful damage pipeline — required;
- status lifecycle — as invoked by combatants;
- terrain/weather/hazards/zones/reactions — required if water/gates/chamber edges have tactical effects or generic reactions are expected;
- move-specific behavior — as invoked;
- abilities — as invoked;
- items — as invoked;
- Trainer Features/perks — as invoked;
- AI legal-action infrastructure — required;
- AI tactical policy — required for `EVACUATE`, `PROTECT_ROUTE`, `WITHDRAW`, `CLEAR_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback — required for full presentation and world-state handoff.

REDUCED version:

Navigation halts the lock, secures gates/water state and evacuates workers/passengers before battle. AutoPTU receives a static safe chamber-side or control-house arena with actual combatants only. No dynamic water, crushing gates, moving vessels or civilian HP exists. After the battle, world state decides whether the lock can resume.

### Debris Boom Recovery at Navigation Reach

Premise: A control/maintenance asset is overwhelmed after an upstream event. A combat encounter occurs independently while a crew needs access to inspect or secure the site.

FULL version:

Moving debris, changing water route, protected technicians and retrieval objectives can coexist.

Dependencies:

- complete movement — BLOCKING for moving objective/withdrawal/interception;
- terrain/weather/hazards/zones/reactions — BLOCKING if currents, debris or water state affect tactics;
- AI tactical policy — BLOCKING for `PROTECT_TECHNICIAN`, `RETRIEVE`, `WITHDRAW`, `CLEAR_ROUTE`;
- adapter/playback — BLOCKING;
- ordinary combat categories follow the permanent status map.

REDUCED version:

Freshwater/Navigation isolates the work area first. Technicians and debris operations remain outside the grid. The battle occurs on a static bank/platform arena. Recovery work resumes afterward and its success is not inferred from combat victory.

### Wildlife Crossing During Lockage

Premise: A migration or recurring wildlife movement intersects a navigation approach while a scheduled lockage is pending.

FULL version:

Wild Pokémon should be able to `CROSS`, `WITHDRAW`, `REACH_GROUP` or avoid the battlefield rather than behave as ordinary hostile AI. Operators may need to hold traffic while conditions change.

Dependencies:

- complete movement — BLOCKING for route crossing/withdrawal/interception;
- terrain/weather/hazards/zones/reactions — BLOCKING if water/approach state changes tactically;
- AI legal-action infrastructure — VERIFIED as a foundation only;
- AI tactical policy — BLOCKING for ecological objectives;
- adapter/playback — BLOCKING;
- exact Move/Ability/Item/Feature behavior remains PARTIAL as invoked.

REDUCED version:

Navigation suspends lockage. Migration resolves in world state first. Only if an independent hostile conflict remains does AutoPTU receive a conventional static arena. The wildlife crossing itself does not require combat and successful passage does not alter capture eligibility.

### Lock Queue Dispute

Primarily non-combat.

Operators, Travel, Public Information and Institutional Review reconcile queue state, emergency priority, stale estimates and service consequences. If participants voluntarily initiate a separately legal battle, its result has no authority over queue priority unless an authored institution explicitly defines such a rule.

## Dependency design rule

The narrative premise must survive the reduced version.

A lock incident remains a lock incident even when AutoPTU cannot yet simulate changing water. A wildlife crossing remains an ecological/navigation conflict even when CROSS/WITHDRAW AI is not yet available. The Minecraft adapter must never duplicate missing PTU mechanics to make the full version appear complete.

## Canon questions raised by these proposals

- Does Ouros contain engineered inland canals and locks at campaign start?
- Which rivers or lakes support regular passenger/cargo navigation?
- Which institutions operate locks and public information?
- Which waterways have strong ecological passage constraints?
- Are any historical towpaths, portage towns or retired canals established lore?
- Can player organizations operate ferries, barges or lock-linked businesses?
- What technologies exist for controls, sensors and vessel propulsion?
- Which Pokémon roles in navigation are authored and voluntary?
- Which PTU/Caelo rules govern Swim, vessels, currents, falls, drowning, carrying and environmental water?
