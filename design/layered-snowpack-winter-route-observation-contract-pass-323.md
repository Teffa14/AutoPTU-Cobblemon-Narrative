# Layered snowpack and winter-route observation contract — Pass 323

Status: DESIGN CONTRACT / NON-CANON
Date: 2026-09-07

## Purpose

Provide a reusable boundary for winter route state, layered environmental history, observations, access decisions, and later consequences without allowing snow rendering, footprints, old traffic, a cleared road, or franchise flavor to become hidden tactical authority.

This contract is for Ouros world-state design. It is not real-world avalanche guidance and must not implement real hazard prediction from simplified inputs.

## Authority chain

Authoritative narrative state should preserve:

`persistent feature identity -> authored event/history -> authored current feature state -> observation -> observer/receiver -> interpretation -> institutional/actor decision -> feature-scoped consequence -> later evidence`

When a tactical encounter exists, append rather than collapse:

`... -> explicit AutoPTU handoff -> authoritative tactical state -> semantic events -> Minecraft/Cobblemon/Craftics presentation`

## Required separations

### Event history versus current state

A storm, wind event, maintenance pass, thaw, previous closure, or older debris event is historical provenance. It may help explain current state but does not automatically determine it.

A new surface appearance must not delete earlier event history.

### Surface observation versus full feature state

Tracks, cleared snow, exposed markers, drift shape, debris, cracking, a field note, or a maintenance record are bounded observations. They do not expose the entire hidden state of a slope, road, gully, bridge approach, shelter, or upper traverse.

`TRACKS_OBSERVED` must never be promoted automatically to `ROUTE_SAFE`.

`ROAD_CLEARED` must never be promoted automatically to `CONNECTED_TERRAIN_SAFE`.

### Feature state versus regional state

Nearby winter features can differ. A maintained lower approach, sheltered bench, cross-loaded gully, upper traverse, road cut, bridge approach, and refuge keep independent IDs and histories.

Do not use one global mountain `SAFE/UNSAFE` bit when the decision concerns specific features.

### Observation versus interpretation

An observation can remain true while its interpretation changes.

Example: a set of tracks existed at observation time. Later evidence may show they belonged to maintenance access, were older than assumed, or used a route unavailable to the public. The observation remains in history.

### Knowledge versus world truth

NPCs know only observations, reports, publications, decisions, consequences, or direct perceptions that entered their explicit knowledge path.

Shared faction membership does not confer route knowledge. A maintenance crew's local inspection does not automatically wake every administrator. A public reopening notice does not imply every traveler received the revision.

### Decision versus consequence

An access decision and its consequences are separately persistent.

Reopening one feature can leave another closed. Revising a closure does not erase a delayed convoy, missed appointment, shelter supply drawdown, public complaint, ecological observation gap, or earlier publication history already produced by the old decision.

## Semantic-time contract

Every operational observation that can become stale should retain either a semantic timestamp or a bounded time window plus enough provenance to compare it with later world events.

A later authored weather/world event may make an earlier observation stale for a decision without making the historical observation false.

The same feature may therefore support:

`OBSERVATION_VALID_AT_T1`

followed later by:

`OBSERVATION_STALE_FOR_T2_DECISION`

without mutating the first record.

## Persistent route-state contract

Reduced winter content should use ordinary route states already compatible with global travel/world-agent reasoning, for example:

`OPEN`
`RESTRICTED`
`MAINTENANCE_ONLY`
`CLOSED`
`MONITORING`

Any richer environmental descriptor remains separate from route permission unless an explicit decision connects them.

A route closure is an institutional/operational fact, not a PTU status.

## Evidence schema guidance

A winter observation should carry at least:
- observation ID;
- feature ID;
- semantic time or interval;
- source/observer;
- observation kind;
- provenance root;
- confidence or uncertainty when the existing evidence system requires it;
- optional related event ID;
- optional instrument/record ID;
- no hidden-world-state fields exposed merely for UI convenience.

Useful narrative observation kinds may include:
- lower route cleared;
- route marker exposed/covered;
- old debris boundary observed;
- tracks observed with source unresolved;
- field restriction recommendation received;
- public notice received;
- later event occurred after observation;
- local state unresolved.

These are evidence/world-state records, not battle conditions.

## PTU / Caelo / Kairos boundary

The repository currently exposes `sources/kairos` as a comparative source registry and no adopted `sources/caelo` directory. `sources/kairos/KAIROS_SOURCE_INDEX.md` points to movement/terrain, status, hazards, terrain/weather, encounter design, and utility classes in the supplied Kairos PDF, but explicitly states that the index is not source authority and Kairos rules are not automatically accepted by Ouros.

Before numeric or legal winter mechanics are authored, verify the actual project-authoritative PTU/Caelo material and current engine implementation.

Do not infer from this contract:
- snow movement costs;
- Ice terrain behavior;
- cold exposure damage;
- avalanche damage;
- burial or suffocation rules;
- falling damage or fall triggers;
- climbing DCs;
- visibility penalties;
- weather penalties;
- rescue actions or interrupts;
- Survival/Perception/Topographer/Climatologist modifiers;
- Ice Body behavior;
- Move-created snow/ice/wind effects;
- item bonuses;
- species traversal privileges.

## Capability dependency contract

### Targeting / footprints / range / LoS

Ordinary audited targeting and LoS may be used where the scene does not add concealment. Active snowfall, whiteout, snow walls, elevation-specific occlusion, or visibility-changing weather need dedicated evidence beyond ordinary LoS.

Current category status: VERIFIED within audited ordinary contracts; winter visibility extensions unverified.

### Base movement legality

Ordinary verified traversal can support authored open ground. Deep snow, ice, climbing, sliding, species-specific winter movement, or special footing require exact source and engine evidence.

Current category status: VERIFIED within audited ordinary contracts only.

### Complete movement

Required for push/pull, knockback, interception, rescue pulls, forced slides, moving debris, displacement caused by snow, or movement near ledges when forced movement matters.

Current category status: PARTIAL.

### Core calculations

Use verified deterministic arithmetic only. No snow-load, stability, temperature, exposure, or avalanche-probability formula is introduced.

Current category status: VERIFIED within audited deterministic contracts.

### Action economy / initiative

Ordinary verified action ordering may be used. Any environmental interrupt, rescue action, or special winter interaction requires its exact legal contract.

Current category status: VERIFIED within audited ordinary contracts.

### Full turn / round lifecycle

Required for scheduled within-battle snowfall changes, delayed environmental events, timed refuge windows, repeated pulses, or other transitions outside specifically verified lifecycle seams.

Current category status: PARTIAL.

### Full stateful damage pipeline

Required for any environmental damage, fall, collision, crushing, cold, debris, or Move/environment interaction that changes authoritative health state.

Current category status: PARTIAL.

### Status lifecycle

Required for any persistent mechanical condition. Pass 323 introduces no new PTU status.

Current category status: PARTIAL.

### Terrain / weather / hazards / zones / reactions

Required for dynamic snow/ice terrain, weather-dependent areas, hazard boundaries, refuge zones, environmental reactions, or rescue windows.

Current category status: MIXED / PARTIAL / BLOCKING by subfamily.

### Move-specific behavior

Each Move affecting weather, ice, snow, wind, terrain, visibility, movement, rescue, or environmental damage must be verified independently.

Current category status: PARTIAL.

### Abilities

Each Ability must be verified independently. Official Pokédex or videogame text cannot establish AutoPTU Ice Body, weather interaction, snow traversal, detection, or protection behavior.

Current category status: PARTIAL.

### Items

Narrative equipment may exist as world objects. Mechanical bonuses or legal rescue/survey effects require source-backed item implementation.

Current category status: PARTIAL.

### Trainer Features / perks

Any Survivalist, Topographer, Climatologist, Researcher, ranger-like, rescue, or navigation privilege must be verified from project-authoritative rules and current implementation.

Current category status: PARTIAL.

### AI legal-action infrastructure

May enumerate only verified legal actions. It cannot legalize an unsupported rescue, environmental interaction, or traversal shortcut.

Current category status: VERIFIED within audited contracts.

### AI tactical policy

General autonomous winter-hazard reasoning, dynamic evacuation, refuge selection, rescue prioritization, or risk-aware traversal remains outside verified policy.

Current category status: BLOCKING for general autonomous behavior.

### Minecraft / Cobblemon / Craftics adapter/playback

The adapter may render snowfall, tracks, snow depth appearance, route barriers, debris, refuge geometry, NPC movement, and authoritative semantic events. It must not decide tactical legality, terrain cost, damage, status, route truth, hidden ecological state, or NPC knowledge.

Current category status: PARTIAL / BLOCKING end-to-end.

## Reduced-version rule

When rich mechanics are unavailable, preserve the complete narrative premise through:
- persistent feature IDs;
- authored route states;
- semantic-time world events;
- explicit evidence with provenance;
- NPC receipt and belief boundaries;
- feature-scoped decisions;
- durable consequences;
- between-scene environmental transitions;
- blocked route edges instead of simulated moving hazards.

Do not recreate missing PTU rules inside the Minecraft adapter.

## Rich-version gate

A rich winter encounter may be enabled only after every mechanic it uses has named source and implementation evidence. Representative support in one terrain, weather, reaction, Move, Ability, item, Feature, or lifecycle seam does not prove the family complete.

If a scene uses knockback, rescue interception, snowfall phases, delayed debris, persistent conditions, Ability-triggered weather, or Trainer Feature interrupts, record those exact dependencies in the encounter contract.

## Acceptance tests for later implementation

A conforming implementation should demonstrate that:
- clearing the lower road does not silently open the upper traverse;
- observed tracks do not create a global safety fact;
- two observations from different times can disagree without corrupting history;
- a later weather event can make a report stale without deleting it;
- an NPC cannot cite a field report it never received;
- a revised access decision changes only targeted consequences;
- Minecraft rendering cannot create authoritative winter state;
- a rich encounter can fall back to the reduced route/evidence version when tactical dependencies are unavailable.