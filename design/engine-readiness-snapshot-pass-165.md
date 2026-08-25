# Engine Readiness Snapshot — Pass 165

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-25
Narrative topic: wildlife telemetry, tagging, and movement monitoring

## Read-only engine evidence inspected

### AutoPTU-Java

Inspected `main` head: `4148255b038f85902feb781413f163c7b7cf3799`.

Latest visible slice at inspection time: `Add package-private move-special target result transport (#195)`. The change keeps per-target Move Special result transport inside the runtime and generalizes action-finalization transport. Its parent `10fd20bfd513898a6f8f157a9b469db993444974` finalizes `END_ACTION` Move Specials once per declaration.

This is meaningful evidence for runtime ownership and move-specific execution ordering. It does not prove full Move coverage, complete damage, a general reaction system, forced movement, environmental mechanics, tactical objective AI, or Minecraft integration.

The live README still states that Python AutoPTU remains authoritative while the Java port is incomplete. It marks targeting and base shift/jump legality as implemented, while still listing full combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, remaining hook registries, full transcript parity, AI scoring/policy, and Craftics/Cobblemon integration as unfinished.

### AutoPTU Python oracle

Inspected `main` head: `c9b9b372b6a86546679188df97aa5bde27ab066c`.

The newest visible change is Career-facing recurring-rival identity stabilization. It explicitly preserves combat mechanics and does not justify any tactical capability promotion.

### PTU / Caelo evidence

The project continues to use PTU 1.05 / Python AutoPTU as the accessible mechanics baseline. No primary PTU/Caelo contract for electronic wildlife telemetry, GPS collars, acoustic arrays, receiver ranges, tag attachment, or automated tracking infrastructure was recovered during this run.

No result is attributed to Super PTU Online Helper because it was not available as an invocable capability.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Evidence remains strong for tactical range, areas, footprints, target anchors, and line of sight. This verification is battle-specific and must not be reused as radio/telemetry coverage.

`base movement legality`

Shift/jump legality has parity-backed coverage for the implemented movement boundary. This does not include the full movement family below.

`core calculations`

Core PTU tables and calculation primitives remain covered at the project’s verified boundary.

`action economy/initiative`

Typed action flow, budgets, and deterministic initiative/declaration ordering remain covered.

`AI legal-action infrastructure`

The engine can construct/filter legal battle choices. Legal-action generation is not tactical objective selection.

### PARTIAL

`full turn/round lifecycle`

Multiple lifecycle slices exist, including delayed effects and Move Special phase/finalization work, but the whole lifecycle is not promoted.

`full stateful damage pipeline`

Damage primitives and multiple ordering contracts exist, while README still explicitly lists full damage resolution as incomplete.

`status lifecycle`

Several status/prevention/application slices exist, but the complete status controller is still listed as unfinished.

`move-specific behavior`

Recent PRE_DAMAGE, POST_DAMAGE, END_ACTION, Status Move, multi-target, and per-target-result contracts materially strengthen this family. The complete registry/catalogue is not demonstrated.

`abilities`

Representative Ability contracts exist. They do not prove full catalogue parity.

`items`

Representative item behavior exists, but the full item family is not demonstrated.

`Trainer Features/perks`

Generic prerequisite/context/frequency/resource/target/effect infrastructure and representative contracts exist, while complete Feature execution/catalogue coverage remains unproven.

### BLOCKING

`complete movement including push/pull/knockback/interception/forced movement`

Specific reaction movement and narrow push/redirect contracts exist, but README still explicitly lists forced movement as unfinished. Full movement cannot be inferred from representative cases.

`terrain/weather/hazards/zones/reactions`

This family remains BLOCKING as a complete category. Specific reaction contracts and field-state/lifecycle slices do not demonstrate complete terrain, Weather, hazards, zones, entry/exit triggers, or reactions.

`AI tactical policy`

Legal choices exist, but goal-aware scoring/policy for objectives such as `WITHDRAW`, `CROSS`, `PROTECT`, `REACH_DEVICE`, `CLEAR_ROUTE`, and non-hostile actors remains unfinished.

`Minecraft/Cobblemon/Craftics adapter/playback`

README still states the adapter comes after a parity-safe vertical slice. Minecraft must not own PTU rules.

## Pass 165 telemetry-specific readiness

Telemetry itself is an overworld/science protocol and does not require AutoPTU for ordinary operation. Current project blockers are world-state/integration contracts, not battle formulas.

Required new overworld contracts before implementation:

- persistent `TELEMETRY_DEVICE` identity;
- device-to-`pokemon_entity_id` deployment history;
- receiver/station identity and configuration history;
- receiver observation-opportunity / coverage revisions;
- immutable raw detection storage;
- time correction and metrology provenance;
- derived location-fix provenance and uncertainty;
- movement-segment derivation with unknown intermediate path;
- tag-loss / detachment / recovery cases;
- monitoring-series ownership;
- sensitive-location privacy/redaction policy;
- Telemetry -> Migration handoff;
- Telemetry -> Rehabilitation/Conservation handoff;
- Telemetry -> Pokémon Agency identity handoff;
- Telemetry -> Research Ethics authorization/welfare handoff;
- Telemetry -> Minecraft presentation boundary.

## Encounter dependency matrix

### Telemetry Receiver Ridge Recovery — FULL

- targeting/footprints/range/LoS: VERIFIED for any ordinary battle portion.
- base movement legality: VERIFIED.
- complete movement: BLOCKING when technician/wildlife traversal, interception, or withdrawal occurs inside the battle space.
- core calculations: VERIFIED.
- action economy/initiative: VERIFIED.
- full turn/round lifecycle: PARTIAL.
- full stateful damage: PARTIAL.
- status lifecycle: PARTIAL if exact statuses are invoked.
- terrain/weather/hazards/zones/reactions: BLOCKING if storm damage, unstable ground, protected equipment zones, or dynamic environmental effects matter tactically.
- move-specific behavior: PARTIAL when specific Moves beyond verified contracts are required.
- abilities: PARTIAL.
- items: PARTIAL if tactical equipment is introduced.
- Trainer Features/perks: PARTIAL if exact Features are used.
- AI legal-action infrastructure: VERIFIED.
- AI tactical policy: BLOCKING for `REACH_DEVICE`, `PROTECT_TECHNICIAN`, `WITHDRAW`, `CLEAR_ROUTE`.
- adapter/playback: BLOCKING.

REDUCED: world state resolves technicians, receiver diagnosis, wildlife movement, and equipment. Any remaining battle uses a static conventional arena.

### Released Pokémon Signal Goes Silent

Primary form is non-combat. No battle capability is required for the core investigation. Telemetry, Rehabilitation, Radio/Technology, Timekeeping, Research Ethics, and Conservation must support an unresolved outcome.

If a separate field confrontation occurs, it inherits only the capabilities actually used by that confrontation.

### Tag Recovery at River Crossing — FULL

- complete movement: BLOCKING for crossing, withdrawal, or interception.
- terrain/weather/hazards/zones/reactions: BLOCKING if current, changing water, debris, or bank state affects tactics.
- AI tactical policy: BLOCKING for `RETRIEVE_DEVICE`, `PROTECT_RESEARCHER`, `WITHDRAW`.
- adapter/playback: BLOCKING.
- ordinary targeting/calculations/action economy remain VERIFIED; lifecycle/damage/status/move/ability/item/Feature families remain PARTIAL where invoked.

REDUCED: Freshwater/Travel freeze a safe world-state geometry; tag recovery happens outside battle; a separate static battle is allowed if needed.

### Migration Receiver Array Interruption — FULL

- complete movement: BLOCKING for group crossing and withdrawal.
- AI tactical policy: BLOCKING for non-hostile movement objectives.
- adapter/playback: BLOCKING for persistent group/device projection.
- environmental family: BLOCKING only if a tactical corridor, weather effect, or hazard is part of the arena.

REDUCED: Migration advances outside the grid. Technicians and moving groups are removed before a static confrontation.

## What current evidence does not prove

Recent Move Special transport/finalization work does not prove:

- electronic telemetry;
- tracking-device Items;
- overworld target locking;
- radio or acoustic propagation;
- receiver coverage;
- device-to-Pokémon identity association;
- scientific location uncertainty;
- animal-movement AI;
- migration simulation;
- capture/release telemetry;
- Minecraft locator authority.

Battle `targeting/footprints/range/LoS` must never be reused for receiver coverage. A receiver detection and a battle target lock are different semantic systems.

## Prohibited shortcuts

- loaded Cobblemon entity position -> telemetry fix;
- entity despawn -> signal loss;
- death event -> telemetry mortality conclusion;
- compass/waypoint -> scientific location;
- redstone/signal bars -> receiver signal strength;
- tag visible on model -> valid deployment record;
- tag deployed -> ownership/custody;
- no signal -> absent/dead/release failure;
- one tagged animal -> population corridor;
- stationary signal -> stationary Pokémon;
- battle LoS -> receiver LoS/coverage;
- Electric/Psychic Type -> telemetry capability;
- Tracker capability -> electronic-tracking subsystem.

## Promotion decision

No permanent engine category is promoted in Pass 165.

The latest Java evidence materially improves runtime-owned Move Special state transport and finalization, but the repository README continues to mark the large missing systems directly. The conservative map above remains the correct dependency model for narrative design.