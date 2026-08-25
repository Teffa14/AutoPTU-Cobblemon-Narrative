# Engine Readiness Snapshot — Pass 166

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-25
Narrative topic: community science and participatory monitoring

## Read-only engine evidence inspected

### AutoPTU-Java

Inspected `main` head: `ebdbcdc58c41bae72e9264e8f508338be95e2295`.

Latest visible slice: `Freeze END_ACTION target aggregation semantics (#196)`. The contract freezes that per-target results replace `last_result` and target damage accumulates before the declaration-level `END_ACTION` dispatch, preserving Python-oracle ordering.

This materially strengthens runtime-owned Move Special aggregation and `move-specific behavior`. It does not prove full Move coverage, complete damage, complete Status, generic forced movement, complete reactions, environmental mechanics, tactical-objective AI, or Minecraft integration.

The live README continues to state that Python AutoPTU is authoritative while Java is incomplete. It marks targeting, shift/jump legality, core calculations, typed action flow, initiative, and legal action-space infrastructure as implemented, while listing core combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, remaining hook registries, full transcript parity, AI scoring/policy, and Craftics/Cobblemon integration as unfinished.

### AutoPTU Python oracle

Inspected `main` head: `0bff7521ecb8b1163cbd5f366dea4651de83c353`.

The newest visible change is Career-facing draw-outcome presentation. Its commit message explicitly preserves combat rules, AI, RNG, transcript, and season resolution. It does not justify a tactical capability promotion.

### PTU / Caelo evidence

The read-only AutoPTU repository contains structured Trainer Class material including Researcher-related data. This confirms that formal Trainer progression remains a separate PTU mechanic. Public participation in monitoring cannot grant Researcher, Pokémon Education, Chronicler, Perception, or another mechanical competency by narrative inference.

No primary PTU/Caelo contract for community science, crowdsourced biodiversity monitoring, volunteer-review networks, BioBlitz procedures, or public observation platforms was recovered.

No result is attributed to Super PTU Online Helper because it was not available as an invocable capability.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Battle-specific range, target anchors, area geometry, footprints, and LoS remain parity-backed. This must not be reused for survey coverage or observation opportunity.

`base movement legality`

Implemented shift/jump legality remains verified at the existing boundary. It does not include the full movement family.

`core calculations`

Core PTU tables and calculation primitives remain covered at the established verified boundary.

`action economy/initiative`

Typed action flow, budgets, and deterministic ordering remain covered.

`AI legal-action infrastructure`

The engine can generate/filter legal battle choices. It does not choose ecological, evacuation, protection, or non-hostile objectives intelligently.

### PARTIAL

`full turn/round lifecycle`

Many lifecycle and Move Special phase contracts exist, but the whole lifecycle is not demonstrated.

`full stateful damage pipeline`

Damage primitives and ordering slices exist; README still explicitly lists full damage resolution as incomplete.

`status lifecycle`

Representative Status application/prevention contracts exist, while the complete status controller remains unfinished.

`move-specific behavior`

PRE_DAMAGE, POST_DAMAGE, END_ACTION, Status Move, multi-target, per-target transport, and target-aggregation contracts materially strengthen this family. Full catalogue coverage is not demonstrated.

`abilities`

Representative Ability contracts exist. Full catalogue parity is unproven.

`items`

Representative item behavior exists. Full item coverage is unproven.

`Trainer Features/perks`

Generic prerequisite/context/frequency/resource/target/effect infrastructure and representative effects exist. Full Feature/perk execution and catalogue coverage remain unproven.

### BLOCKING

`complete movement including push/pull/knockback/interception/forced movement`

Narrow reaction movement and push/redirect cases exist, but README still explicitly lists forced movement as unfinished.

`terrain/weather/hazards/zones/reactions`

The complete family remains BLOCKING. Specific field/reaction slices do not demonstrate terrain, Weather, hazards, zones, entry/exit triggers, or reactions as a full system.

`AI tactical policy`

Legal choices exist, but goal-aware scoring/policy for `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_PARTICIPANT`, `REACH_DEVICE`, and non-hostile wildlife movement remains unfinished.

`Minecraft/Cobblemon/Craftics adapter/playback`

The live README still places the adapter after a parity-safe vertical slice. Minecraft must remain presentation/integration, never PTU or science authority.

## Pass 166 overworld readiness

Community science itself is an overworld/science protocol. Ordinary operation does not require AutoPTU.

Required world-state contracts before implementation include:

- persistent `COMMUNITY_MONITORING_PROGRAM` identity;
- participation campaign/version history;
- observation effort with method, time, route/station, duration, and completeness;
- immutable observation submissions;
- source-dependency and duplicate links;
- validation/review history;
- scoped quality assessments;
- coverage and observation-opportunity revisions;
- sensitive-location privacy/publication transforms;
- aggregate-product provenance;
- correction events that preserve originals;
- Community Science -> Research Ethics handoff;
- Community Science -> Visual Records handoff;
- Community Science -> Taxonomy handoff;
- Community Science -> Identity handoff;
- Community Science -> domain Science/Ecology handoff;
- Community Science -> Minecraft presentation boundary.

## Encounter dependency matrix

### BioBlitz Trail Closure — FULL

- targeting/footprints/range/LoS: VERIFIED for ordinary battle targeting.
- base movement legality: VERIFIED.
- complete movement: BLOCKING for participant/wildlife crossing, withdrawal, interception, or forced repositioning.
- core calculations: VERIFIED.
- action economy/initiative: VERIFIED.
- full turn/round lifecycle: PARTIAL.
- full stateful damage: PARTIAL.
- status lifecycle: PARTIAL if exact statuses are used.
- terrain/weather/hazards/zones/reactions: BLOCKING if closure conditions, dynamic terrain, weather, or protected corridors affect tactics.
- move-specific behavior: PARTIAL where exact Moves are required.
- abilities: PARTIAL.
- items: PARTIAL if tactical equipment enters the battle.
- Trainer Features/perks: PARTIAL when exact Features are used.
- AI legal-action infrastructure: VERIFIED.
- AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_PARTICIPANT`, and non-hostile movement goals.
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED: suspend the survey in world state, evacuate participants, advance wildlife outside the grid, preserve survey coverage as incomplete, then use only a static conventional battle if an independent confrontation remains.

### Rare Sighting Crowd Surge — FULL

- complete movement: BLOCKING for crowd routing and wildlife withdrawal.
- AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, and protection objectives.
- adapter/playback: BLOCKING.
- environmental family: BLOCKING only if a real tactical environmental effect is present.
- ordinary targeting/calculations/action economy remain VERIFIED; lifecycle/damage/status/move/ability/item/Feature families remain PARTIAL where invoked.

REDUCED: Community Science reduces public location precision; Public Space reroutes visitors; wildlife moves outside battle; any independent conflict uses a static arena.

### Community Sensor Retrieval — FULL

- complete movement: BLOCKING for technician traversal/withdrawal.
- terrain/weather/hazards/zones/reactions: BLOCKING if storm debris, water, unstable ground, or equipment-protection zones matter tactically.
- AI tactical policy: BLOCKING for `REACH_DEVICE`, `PROTECT_TECHNICIAN`, `WITHDRAW`.
- adapter/playback: BLOCKING.
- ordinary combat categories retain the permanent map above.

REDUCED: device custody, retrieval, technician movement, and data validation occur in world state. A nearby static battle can occur independently.

### Observation Review Night

Non-combat. No battle capability is required. Scientific review can end `VALID_FOR_SCOPE`, `DUPLICATE_SOURCE`, `IDENTIFICATION_REVISED`, `INSUFFICIENT_FOR_PRODUCT`, or `UNRESOLVED`.

## What current evidence does not prove

Recent Java Move Special aggregation work does not prove:

- survey protocols;
- observation effort;
- automatic species identification;
- community-review workflows;
- public scientific credentials;
- population inference;
- duplicate-source detection;
- geoprivacy;
- participant reputation as a PTU stat;
- crowdsourced spawn control;
- Minecraft observation authority.

Battle `targeting/footprints/range/LoS` must never be reused as survey coverage. Legal battle range and an observer’s opportunity to detect wildlife are different semantic systems.

## Prohibited shortcuts

- loaded entity count -> abundance;
- visible entity -> validated observation automatically;
- no loaded entity -> non-detection;
- player proximity -> survey effort;
- screenshot -> reviewed scientific record without provenance;
- repeated reposts -> repeated independent detections;
- public map pin -> exact sensitive location;
- accepted observation -> Researcher/Pokémon Education/Chronicler;
- rare sighting -> capture eligibility;
- observation leaderboard -> XP or Trainer advancement;
- many reports -> population increase;
- Minecraft waypoint -> authoritative field location;
- battle LoS -> observation coverage.

## Promotion decision

No permanent engine category is promoted in Pass 166.

Java head `ebdbcdc58c41bae72e9264e8f508338be95e2295` adds meaningful evidence for declaration-level Move Special target aggregation, but the live README continues to identify the large unfinished systems directly. The conservative capability map remains appropriate.