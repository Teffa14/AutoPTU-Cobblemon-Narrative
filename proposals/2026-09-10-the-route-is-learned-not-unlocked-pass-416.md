# The Route Is Learned, Not Unlocked — Pass 416

Status: PROPOSED / NON-CANON

Research provenance: `research/2026-09-10-knowledge-route-changing-world-scan-416.md`

## Premise

A practical route through an already-existing area is difficult to use because the useful path depends on recognizing current conditions and understanding evidence that most travelers would overlook. The route does not appear when a quest starts. Learning about it changes what an informed actor can attempt.

Sendero del Vidrio and Estación Mirador are suitable existing canon anchors for a future implementation, but this proposal does not add a new route, structure, hazard or historical event to either location.

## World-state structure

The physical route has a revisioned state independent of who knows about it. Rain, maintenance, erosion, temporary closure, wildlife pressure, repairs or ordinary obstruction may make one description obsolete while leaving its historical observation valid.

Knowledge remains actor-specific. One resident may know an older route description. Another may have a recent observation but not understand its significance. A traveler can combine communicated evidence only after receiving it. Shared institution membership never grants the information automatically.

An archive note, field observation or repeated environmental marker can teach an actor what to look for. The learned information can alter route planning without creating a global `ROUTE_UNLOCKED` flag.

## Possible scene loop

A traveler encounters an apparent dead end or an unattractive public route. Existing evidence suggests another way may be usable under particular conditions. The actor decides whether to investigate, ask someone, consult a record, wait for a better window, use the slower known route or abandon the trip.

If the alternate route is attempted later, the system evaluates the current site revision rather than assuming the earlier clue still guarantees passage. A correct old report can therefore remain correct for its own time while no longer describing the present.

NPCs can use the route off-screen only when their own knowledge, permissions, schedule, travel state and current accessible conditions support that decision.

## Reduced implementation

This version can run without new AutoPTU mechanics.

Use existing semantic time, world-route planning, private knowledge, explicit communication, schedules, obligations, permissions, persistent observations, site revisions and event-driven replanning. Route availability is authored world state. Environmental changes occur through the persistent-world layer rather than through invented tactical simulation.

Minecraft/Cobblemon may display authored signs, repairs, water level, debris, worn markers or route geometry. Those visuals do not independently decide hidden history, PTU checks or tactical consequences.

## Mechanically rich implementation

A later version may place the traversal under active pressure. Examples include reaching a safe tile, protecting an observer during a crossing, withdrawing after collecting evidence, crossing while an environmental phase changes, or moving another participant out of danger.

The full version must use exact capability gates:

- targeting/footprints/range/LoS: VERIFIED only for audited scopes; required if tactical observation, attacks or interactions use spatial targeting;
- base movement legality: VERIFIED only for audited ordinary movement scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL; required for forced slides, dragging, rescue reposition, interception or knockback-dependent traversal;
- core calculations: VERIFIED only for audited calculation paths;
- action economy/initiative: PARTIAL; required when traversal competes with combat actions or initiative timing matters;
- full turn/round lifecycle: PARTIAL; required for timed crossings, multi-round protection, delayed collapse or phase changes;
- full stateful damage pipeline: PARTIAL; required if injury/damage consequences must persist authoritatively after the encounter;
- status lifecycle: PARTIAL; required for persistent or timed status consequences;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact behavior; required for live flooding, unstable ground, weather phases, reactive debris, triggered zones or reaction windows;
- move-specific behavior: individually gated; a Move cannot create a traversal affordance merely because a similar Move works elsewhere;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: VERIFIED only for ordinary audited scopes; specialized inspect, rescue, brace, interact or extraction actions require explicit legal admission;
- AI tactical policy: BLOCKING for route-aware rescue, protect-observer, evidence-first withdrawal and objective-aware disengagement unless separately implemented;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative hazard state, specialized tactical interactables, non-KO objective completion and tactical recovery.

## Consequences

Success can improve later travel because a particular actor now possesses defensible route knowledge, because they communicated it, or because someone performed a real repair. Failure can consume time, create a new observation, force replanning or reveal that an old record describes an obsolete revision.

No universal reputation score or quest flag is required. The durable consequences are world state, knowledge, provenance, schedules, access and relationships.

## Canon questions before promotion

A future canon pass must decide whether any alternate route actually exists, which existing location owns it, what authored condition changes it, which NPCs initially know what, whether any institution maintains it, and which evidence is observable without PTU adjudication.

Any tactical version must remain optional until every mechanic it relies on has direct implementation evidence. The reduced version preserves the narrative premise meanwhile.
