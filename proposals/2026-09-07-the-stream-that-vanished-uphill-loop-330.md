# The Stream That Vanished Uphill — Pass 330

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

A small surface stream disappears into a sink feature near a maintained route. Days later, a spring used by a settlement shows a change in flow or quality. The intuitive explanation is that the stream feeds the spring because the spring is nearby and downhill.

A field team runs a trace expecting recovery at that spring. The expected receptor remains negative during the first observation window. A different receptor at a more distant resurgence later returns a positive result.

The investigation becomes a persistent-world problem about hidden connectivity rather than a cave maze with a single secret passage.

## Persistent features

Use stable feature IDs:

- `SINK_STREAM_ENTRY` — the surface stream segment where water disappears underground.
- `EXPECTED_SPRING` — the outlet most actors initially suspect.
- `DISTANT_RESURGENCE` — a farther outlet that can receive a later positive trace.
- `COMMUNITY_WELL` — an optional dependent water source whose relation remains uncertain until evidence exists.
- `CAVE_RECEPTOR_SITE_A` and `CAVE_RECEPTOR_SITE_B` — sampling points inside mapped or partially mapped subterranean reaches.
- `SURFACE_ROUTE_CROSSING` — infrastructure whose drainage or incident history can introduce material into the system.
- `ARCHIVE_MAP_NODE` — an institutional record source containing old survey, cave, water, or maintenance observations.

Region, settlement, geology, ownership, hydrologic regime, and species remain unresolved until canon promotion.

## Actors and bounded knowledge

A hydrology or cave-research team knows the traces it performed, receptor placement, observations, and uncertainty in its own interpretation. It does not automatically know every maintenance incident or household report.

A water operator knows well/spring condition, service interruptions, samples, and reports actually delivered to it. It does not know unseen cave connectivity by default.

A route-maintenance crew knows culverts, runoff, spills, repairs, and drainage work along its corridor. It may have the earliest evidence that material entered a sink feature while lacking downstream hydrology knowledge.

A cave guide or local explorer knows mapped passages, access conditions, and remembered water behavior. Personal experience can suggest hypotheses but is not authoritative connection proof.

Residents can provide dated observations about flow, turbidity, odor, water use, animal presence, or unusual surface behavior. Those observations remain local and require interpretation.

An administrator or emergency coordinator acts only on reports received into its process. A revised connection map must be delivered before it changes that actor's knowledge.

## Investigation loop

The first stage establishes an intuitive causal story. Water disappeared at `SINK_STREAM_ENTRY`; `EXPECTED_SPRING` changed; surface maps make the relationship look plausible.

The player can inspect surface drainage, historic reports, cave access, receptor placement, maintenance records, and timing. The investigation should make clear that a plausible hypothesis is useful but remains a hypothesis.

A tracer test produces multiple evidence records rather than one global answer. Possible results:

- `EXPECTED_SPRING`: negative in the initial window;
- `DISTANT_RESURGENCE`: positive after a delay;
- `COMMUNITY_WELL`: no sample, inconclusive sample, or later result;
- one cave receptor: positive;
- another cave receptor: negative or not recovered.

The second stage asks what the positive result establishes. It confirms a hydrologic connection for that test context. It does not reveal the exact underground geometry, guarantee identical flow in every season, or prove that the original change at `EXPECTED_SPRING` had the same cause.

The decision stage is operational. The player can help determine which outlets require monitoring, which maps/notices need revision, whether a route incident now creates a downstream obligation, whether a cave area becomes a protected monitoring site, and which actors need the updated connection evidence.

A later revisit can expose new evidence: a second trace under different conditions, a previously unknown seep, a delayed receptor result, a route-repair consequence, changed NPC beliefs, or an institutional procedure updated because the first investigation revealed an unexpected connection.

## Open causal hypotheses

Keep these unresolved:

- the disappearing stream connects primarily to the distant resurgence;
- the expected spring has a different recharge source and changed for an unrelated reason;
- both outlets share part of a recharge area but respond differently by condition;
- one tracer was retained or delayed, making the first observation window incomplete;
- a maintenance incident introduced material into a sink point that affects a different dependent feature than expected;
- a previously unknown conduit or resurgence exists;
- verified Pokémon activity altered a local flow path or obstruction, if later evidence specifically supports it;
- several independent processes happened during the same period.

Sabotage is not required.

## Consequence model

Consequences remain feature-scoped:

- `DISTANT_RESURGENCE` gains `MONITORING` and a new institutional responsibility.
- `EXPECTED_SPRING` remains under investigation instead of being declared resolved by the tracer result.
- `SURFACE_ROUTE_CROSSING` gains a spill/runoff reporting obligation because hidden downstream connectivity is now documented.
- `ARCHIVE_MAP_NODE` receives a revision lineage rather than overwriting the older map.
- `COMMUNITY_WELL` can remain `UNRESOLVED_CONNECTION` until sampled or traced.
- named NPCs update belief only after receiving the relevant observation or revised map.

The world should remember the old hypothesis, the test that challenged it, and the decision made with each evidence set.

## Reduced implementation — current-capability version

The core loop needs no live fluid simulation.

World state can author semantic trace events such as `TRACE_INJECTED`, `RECEPTOR_NEGATIVE_WINDOW`, `TRACE_RECOVERED`, `CONNECTION_HYPOTHESIS_REVISED`, and `MAP_REVISION_PUBLISHED`. These are narrative/world facts, not PTU statuses.

The underground connection graph can remain hidden authoritative world state while actors possess only evidence-backed beliefs. Travel through caves can use static route segments and ordinary authored access restrictions. Unsupported flooded, collapsed, or high-flow reaches remain inaccessible rather than being approximated by Minecraft physics.

If combat occurs, use static legal geometry and the ordinary verified families: targeting/range/LoS where no darkness-specific or water-specific modifier is needed, base movement, core calculations, action economy/initiative, and legal-action infrastructure.

The reduced version does not require currents, drowning, live water-level changes, cave collapse, falling debris, darkness penalties, rescue interrupts, environmental damage, contamination statuses, or special Pokémon navigation.

## Intended full version and exact engine dependencies

A richer cave encounter could eventually include dark or obscured chambers, moving water, unstable ledges, collapses, rescue objectives, narrow passages, environmental timing, and species-specific behavior.

Dependency classification:

- targeting/footprints/range/LoS — VERIFIED only for ordinary audited contracts; darkness, spray, mist, underwater visibility, narrow-portal occlusion, or changing cave visibility require separate evidence.
- base movement legality — VERIFIED for ordinary audited movement; climbing, swimming, squeezing, slippery rock, cave-specific costs, or submerged traversal require separate support.
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL; required for currents, falls, rescue/interception, collapse displacement, or forced movement through channels.
- core calculations — VERIFIED for ordinary audited deterministic combat calculations.
- action economy/initiative — VERIFIED for ordinary audited primitives.
- full turn/round lifecycle — PARTIAL; required for timed flooding, delayed collapse, recurring environmental pulses, changing access, or scheduled cave events during combat.
- full stateful damage pipeline — PARTIAL; required for fall, collapse, impact, crushing, drowning-like damage, or other environmental HP changes.
- status lifecycle — PARTIAL; required for any persistent exposure or condition represented tactically.
- terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by subfamily; required for water zones, unstable terrain, collapse zones, shelter, reactive hazards, or environmental triggers.
- move-specific behavior — PARTIAL and individually gated.
- abilities — PARTIAL and individually gated.
- items — PARTIAL and individually gated.
- Trainer Features/perks — PARTIAL and individually gated.
- AI legal-action infrastructure — VERIFIED for ordinary audited legal actions.
- AI tactical policy — BLOCKING for general rescue, escort, retreat, investigation-under-threat, dynamic hazard avoidance, and non-defeat objectives.
- Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING end-to-end for authoritative dynamic cave/environment playback.

One verified mechanic cannot promote a whole family.

## Minecraft / Cobblemon presentation boundary

Minecraft may render sinkholes, disappearing streams, caves, springs, dye-color visualization after an authoritative observation, monitoring gear, route closures, and changed maps. Those visuals do not calculate hydrologic truth.

A water block path cannot decide that two features are connected. Minecraft pathfinding cannot reveal an underground connection graph. Particle color cannot create a PTU status. A cave mob path cannot define legal movement. NPCs learn connection evidence through explicit observation, reports, archives, and delivery events.

## Canon questions intentionally unresolved

Region, geology, settlement, water authority, cave institution, route identity, hydrologic seasonality, exact connection graph, spring/well dependencies, species populations, cultural importance, true cause of the original spring change, final management decision, and whether any combat occurs remain open.
