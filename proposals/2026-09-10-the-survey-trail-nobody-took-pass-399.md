# The Survey Trail Nobody Took — Pass 399

Status: PROPOSED / NON-CANON
Canon approval: REQUIRED before naming a region, route, institution, NPC, species, item, disaster or historical incident.

## Premise

A low-priority field notice asks for one baseline reading from a side trail that most travelers skip.

The player may accept it, ignore it, postpone it or never see it. The world does not wait for that choice forever.

If the request remains open, a named survey team can later reserve and check out the shared instrument, travel to the trail and attempt the work off-screen under the ordinary global NPC planner. Their success, failure, partial completion and communications depend on what those actors actually know and can do.

Later, the trail changes. Heavy weather, erosion, a landslip, seasonal water or another still-undecided cause alters access to part of the route. A larger problem then makes the old baseline unexpectedly valuable.

The resulting investigation is about chronology and evidence rather than destiny. What was measured before the change? Who physically held the instrument at that time? Who received the report? Which parts of the route were accessible then? What has changed since?

The original side quest becomes consequential without being retroactively mandatory.

## Persistent-world structure

The request can create several independent facts:

- one optional obligation with a real time window;
- one shared WorldResource required for the preferred survey method;
- reservation and checkout history;
- holder transitions if the instrument changes hands;
- travel and schedule consequences for the NPC team;
- one or more site observations with semantic time and revision context;
- explicit communication recipients;
- private knowledge that may differ between surveyors, dispatchers and later investigators.

No single record owns the whole story.

A current holder does not prove who held the instrument during the old reading. A custody transfer does not prove that every later holder mutation is known. A present-day route map does not overwrite the earlier site revision. A report being published does not mean every NPC received it.

## Player outcomes

If the player performs the first survey, later NPCs can refer to evidence the player actually created.

If another team performs it, the player can encounter their records, testimony, equipment history or incomplete communications later.

If nobody completes it, the larger problem begins without a baseline. The later investigation must use weaker comparison methods, nearby observations, witness recollection or a fresh survey.

If the first expedition fails, failure still creates consequences: a missed obligation, a route warning, a resource left in an uncertain state, an incomplete observation, or a rescue/recovery need if justified by actual world state.

None of these branches requires a hidden canonical answer that says the player should have accepted the original notice.

## Reduced implementation

The complete narrative premise can run without AutoPTU.

Represent route change between scenes as a new site/travel revision rather than a dynamic battle hazard. Use semantic time, persistent NPC schedules, world travel, resource reservations, `ResourceHolderTransitionLedger`, the V3 recovery manifest, Pass 399 post-restore reconciliation, persistent observations, explicit communication and replanning.

Wild Pokémon contact can remain non-tactical or be omitted. The investigation can resolve through records, interviews, comparison of old/new observations and a repeat measurement.

This version does not require the Minecraft adapter to simulate missing PTU hazard or objective rules.

## Full mechanically rich version

A later expedition can revisit the altered trail while conditions continue to deteriorate. The scene may combine navigation, measurement, protection of survey equipment, assistance to another team and optional wild-Pokémon pressure.

Narrative success can be any justified combination of obtaining the reading, recovering evidence, reaching a stranded person, preserving the instrument, transmitting a result or withdrawing safely. KO is not the default objective.

## Engine dependency classification

Targeting/footprints/range/LoS: VERIFIED only in previously audited scopes. Needed only if the rich version uses ranged protection, spatial targeting or line-of-sight constraints.

Base movement legality: VERIFIED in audited scopes. Sufficient for ordinary tactical relocation when no richer movement interaction is required.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required for slides, forced displacement, interception, dragging or rescue reposition. The reduced version avoids all of them.

Core calculations: VERIFIED only in audited scopes. Relevant if ordinary combat calculations are invoked.

Action economy/initiative: PARTIAL as a family; audited primitives are verified. Required if measurement, rescue and combat actions compete inside structured turns.

Full turn/round lifecycle: PARTIAL. Required for timed survey windows, delayed collapse, multi-round weather phases or countdown extraction.

Full stateful damage pipeline: PARTIAL. Required if damage must persistently alter a carrier, protected objective or later world outcome.

Status lifecycle: PARTIAL. Required for any complex persistent tactical condition.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Required for dynamic landslip, flooding, visibility reduction, unstable ground, wind zones, triggered hazards or reactions. The reduced version moves the environmental change between scenes instead.

Move-specific behavior: individually gated. No Move is assumed available merely because the narrative suggests traversal, protection or clearing debris.

Abilities: individually gated. No Ability-triggered weather, terrain, rescue or sensing effect is assumed.

Items: individually gated. The survey instrument is a world resource unless a verified PTU Item effect is explicitly bound to it.

Trainer Features/perks: individually gated. No Researcher, Topographer, Climatologist or other Feature effect is invented by this proposal.

AI legal-action infrastructure: VERIFIED only in ordinary audited scopes. It can support legal tactical choices already covered by engine contracts.

AI tactical policy: BLOCKING for survey-first priorities, protect-equipment behavior, rescue-first behavior, objective-aware withdrawal, abandoning a measurement to save a person, or disengaging after a non-KO objective.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for stable survey-object projection, dynamic route/hazard state, acknowledgement of pickup/handoff, persistent environmental objectives and authoritative non-KO completion.

## Provenance and canon boundary

Research inspiration is recorded separately in `research/2026-09-10-holder-journal-optional-route-continuity-scan-399.md`.

The sources contribute only high-level structures: optional hooks can become persistent story threads; revisited exploration spaces can change; side content can coexist with long-form narrative. No protected prose, characters, plots, maps or distinctive encounters are copied.

No location, institution, survey technology, environmental event, NPC identity or species assignment becomes Ouros canon in this pass.

## Open canon questions

The project still needs an approved location and reason the side trail matters, an institution or person able to issue the survey request, the physical nature of the measurement, the cause and permanence of the route change, and the later problem that makes the baseline valuable.

Any named Pokémon ecology must be checked against established regional/ecological canon before binding species to the scene.

## Open mechanical questions

The survey action itself has no invented PTU DC or Feature bonus yet. Any Skill, Edge, Trainer Feature or Item interaction must be checked against the underlying PTU/Caelo/Kairos material.

The rich encounter also remains gated until the exact environmental mechanics and objective-aware AI behavior it needs are verified.

The holder journal cannot yet be declared universally complete because at least one current rescheduled-handoff execution path can bypass the journal. Pass 399 therefore treats completeness as explicit audited evidence rather than a global assumption.