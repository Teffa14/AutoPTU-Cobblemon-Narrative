# The Quarry That Grew Back Differently

Status: PROPOSED / NON-CANON

Pass: 319

## Premise

A former extraction site was stabilized and partially reclaimed years ago. A lower bench now carries young habitat, a former haul road serves as an occasional route, and drainage works were intended to keep the old cut stable. Recent reports disagree: one crew says a closed sector is failing again, another says Pokémon are using that same sector as shelter, and an old map marks a drainage connection that nobody can find on the current ground.

The central question is not whether the quarry is simply safe or dangerous. The player must reconstruct which parts of the landscape belong to which historical phase, which features actually changed, and what should happen next when safety, access, habitat, and local use overlap.

## Spatial structure

The location is built as a persistent, readable industrial landscape rather than a sequence of generic cave rooms.

The upper rim provides broad sightlines and old survey markers. The main haul road links the outside world to the lower floor. A reclaimed bench contains young vegetation and signs of Pokémon use. A spoil slope carries erosion and rockfall evidence of different ages. A drainage cut or culvert crosses beneath part of the old road. A sealed service opening or adit exists as a historical feature whose current condition must be established rather than assumed. A monitoring point records one part of the site but does not make the whole location observable.

Several routes should expose different evidence. A quick road approach is legible but reveals little of the upper slope. A slower bench route passes ecological evidence. A maintenance path reaches drainage infrastructure. The player can understand the site without being forced through one exact corridor.

## Investigation loop

The player compares evidence from different historical layers.

Old extraction evidence can include cut faces, bolt patterns, abandoned foundations, rails, retaining structures, numbered survey marks, or a map showing a former service connection.

Reclamation evidence can include reshaped slopes, planted vegetation, drainage works, trail surfacing, barriers, monitoring stakes, or repaired channels.

Recent evidence can include fresh sediment, displaced stones, recent tire/tool traces, new cracks, blocked drainage, fresh tracks, feeding signs, nesting material, or a changed barrier.

The player should be able to conclude that a feature is recent without knowing who caused it, or that a habitat is real without proving the sector mechanically safe.

## Alternate authored explanations

These remain proposals, not simultaneous canon facts.

A drainage route may have become blocked, redirecting water into a slope that was previously stable. A historic map may describe a service opening that was filled during reclamation, making the modern team search for infrastructure that no longer exists. A legitimate emergency access may have compacted or damaged a restored section. Natural erosion may have exposed old spoil without any human action. Pokémon may have enlarged or reused a void that already existed. A second-order habitat may depend on seepage that a proposed repair would alter. Two of these causes may coexist.

The final version should select causes only after regional geology, institution history, species ecology, and rule authority are approved.

## NPC and faction dynamics

A reclamation steward wants evidence strong enough to justify intervention and funding. A habitat researcher wants the secondary ecosystem documented before machinery changes it. A route/logistics operator wants to know whether the old haul road can reopen. Nearby residents or workers remember how the site was used but may have incomplete information about later remediation. A local authority wants a defensible decision about access. A former contractor or legacy institution may possess records without being responsible for current conditions.

No faction needs to be secretly evil. Their disagreement can come from different responsibilities, time horizons, and datasets.

## Environmental storytelling

The quarry should communicate chronology through physical relationships.

Vegetation growing through a repaired retaining structure establishes that the repair predates the current growth. Fresh sediment over an older paved drain establishes a newer flow event. A rusted anchor beside a recent monitoring stake shows two management eras. A newly used Pokémon shelter inside an old industrial recess shows ecological reuse without implying that the original excavation was environmentally beneficial.

The player should be able to revisit the same viewpoints later and see remediation, closure, habitat change, or renewed access in the world itself.

## Decision point

The first resolution does not need to choose one global state for the entire quarry.

Possible feature-level outcomes include:
- keep the haul road open while closing the upper spoil path;
- stabilize one slope while preserving a lower wetland or shelter;
- reroute a trail around a monitoring zone;
- investigate drainage before deciding whether to alter a seep;
- reopen a reclaimed bench but keep the service opening sealed;
- defer work until an ecological or structural question is answered.

This fits the existing Ouros consequence model: decisions and repairs should affect the specific world features that depend on them rather than reset every consequence of the site.

## Reduced implementation version

The reduced version preserves the entire premise with scene-authored world states and ordinary verified route traversal.

Useful world descriptors can include:
- ROUTE_OPEN;
- ROUTE_RESTRICTED;
- FEATURE_STABLE_OBSERVED;
- FEATURE_UNSTABLE_SUSPECTED;
- DRAINAGE_BLOCKED_OBSERVED;
- HABITAT_USE_OBSERVED;
- HISTORICAL_FEATURE_UNRESOLVED;
- MONITORING_REQUIRED;
- RECLAMATION_WORK_AUTHORIZED.

These are world/evidence descriptors, not PTU statuses.

Rockfall and water changes occur only between authored scenes. Unstable edges are blocked route edges rather than dynamic forced movement. Rescue, if needed, resolves through deterministic world events rather than reaction timing. No fall damage, collapse timer, current, slippery status, environmental DoT, or Pokémon traversal immunity is invented.

The same NPC conflict, historical reconstruction, faction choices, feature-level consequence repair, and later revisit all remain available.

## Full mechanically rich version

A future full version can make the extraction geometry tactically active after the required contracts exist.

Potential additions include loose scree with movement consequences, elevation-sensitive LoS, falling debris, a timed slope failure, unstable platforms, water crossing from drainage changes, rescue/interception, knockback near edges, environmental damage, hazard zones that change after rainfall or machinery operation, and Pokémon-specific terrain interactions that have been individually verified.

A combat encounter is optional. If one occurs, it should emerge from the place and current conflict rather than exist solely to turn the quarry into an arena.

## Permanent engine capability dependencies

Targeting/footprints/range/LoS: VERIFIED within audited geometric contracts. Useful for elevation and occlusion only when the actual quarry geometry is represented. This status does not verify darkness, unstable-edge detection, sound, dust, or environmental sensing.

Base movement legality: VERIFIED within audited contracts. Sufficient for the reduced version's ordinary open/blocked route traversal. Exact climbing, jumping, water traversal, or rough-terrain exceptions still require rule-specific verification.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required for slides, falling displacement, knockback near drops, debris push, rescue/interception, or current-driven movement.

Core calculations: VERIFIED within audited deterministic arithmetic. This does not authorize geology, slope-stability, fall, water-flow, or contamination formulas.

Action economy/initiative: VERIFIED within audited primitives. Can sequence already-valid tactical actions but does not define inspection, stabilization, climbing, or rescue actions by itself.

Full turn/round lifecycle: PARTIAL. AutoPTU-Java PR #387 verifies a new generic round-start-effects seam before the first initiative actor, in addition to earlier round-window lifecycle work. That does not establish complete lifecycle coverage. Timed collapse, delayed debris, rainfall phase changes, or multi-phase hazard evolution remain dependent on this family.

Full stateful damage pipeline: PARTIAL. Required for falling rock, fall, impact, crushing, water, or other environmental damage when authored mechanically.

Status lifecycle: PARTIAL. Required only for persistent mechanical conditions. The reduced version defines no quarry-specific status.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by subfamily. Dynamic scree, unsafe ledges, rockfall zones, changing drainage, weather-triggered hazards, rescue reactions, and hazard boundaries require exact verified subfamilies.

Move-specific behavior: PARTIAL. Any Move used for excavation, stabilization, traversal, rescue, terrain alteration, or combat must be individually verified.

Abilities: PARTIAL. No Ability gains quarry traversal, hazard immunity, mining, or stability effects from flavor alone.

Items: PARTIAL. Survey gear, ropes, helmets, pumps, detectors, held items, or tools require their own contracts if they affect rules.

Trainer Features/perks: PARTIAL. Engineering, survival, climbing, geological interpretation, rescue, or interruption Features must be sourced and verified individually.

AI legal-action infrastructure: VERIFIED within audited contracts once underlying actions exist. It does not invent quarry-specific actions.

AI tactical policy: BLOCKING for generalized autonomous navigation, rescue, hazard anticipation, route selection, or terrain exploitation in a dynamically changing quarry.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end. Block collapse, particles, water flow, falling entities, pathfinding, or client animation must represent authoritative world/battle state rather than decide PTU outcomes.

## Longer-term arc potential

The quarry can become a revisitable regional landmark. The first visit establishes what actually exists. A later pass can show remediation. Another can show Pokémon changing how they use the restored site. Economic pressure may make the haul road valuable again. A new storm can test a repaired drainage system. Historical records can later reveal why a seemingly irrational old design choice made sense at the time.

This lets the landscape accumulate history instead of resetting after the quest.

## PTU / Caelo and species boundary

Rolycoly is only a candidate because official franchise material explicitly associates it with mines, caves, darkness, and rough terrain. It is not assigned to the region and receives no PTU travel privilege from this proposal.

No adopted Caelo quarry/reclamation overlay was found in the current narrative source tree. PTU/Caelo numeric rules for climbing, rough terrain, falls, environmental hazards, water crossing, rescue, excavation, and species-specific traversal remain UNVERIFIED until checked against the project's authoritative source material.

## Canon questions left open

Region, geology, extracted material, quarry age, former operator, present steward, reclamation history, drainage state, exact hazards, species population, economic role, ownership, final causes, and final feature-level decisions remain unset. Nothing in this proposal silently attaches the quarry to an established settlement or faction.
