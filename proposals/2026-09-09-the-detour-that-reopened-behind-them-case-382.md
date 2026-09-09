# The Detour That Reopened Behind Them — case 382

Status: PROPOSED / NON-CANON
Canon effect: NONE

## Premise

A field team begins a legitimate trip toward a persistent work site. After departure, the next route segment becomes unavailable. The semantic travel runtime produces `TRAVEL_REPLAN_REQUIRED`, and V19 can preserve that interruption coherently with the action start.

The team takes a slower alternate route after replanning.

Later, the original segment becomes usable again before the team reaches the destination. A second observer sees the route open and concludes that the first team should never have detoured.

Both observations can be correct because they refer to different semantic times.

## Narrative value

The mystery is not whether the route was ever blocked. The world can preserve that fact.

The interesting questions are:
- what changed the route state;
- who knew about the change and when;
- whether the closure was correctly communicated;
- whether the reopening was expected;
- whether the detour exposed the team to a second problem;
- whether somebody benefits from later witnesses seeing an apparently normal route.

The structure supports misunderstanding and investigation without requiring any NPC to lie.

## Reduced implementation

The reduced version requires no AutoPTU handoff.

1. A persistent NPC selects a travel intent.
2. `TRAVEL_EDGE_STARTED` is recorded.
3. The next edge becomes unavailable through explicit world state.
4. `TRAVEL_REPLAN_REQUIRED` is recorded.
5. V19 persists the start and interruption together.
6. The planner chooses a detour, waits, seeks information or abandons the objective.
7. The original edge may later become available again as a new world-state transition.

The narrative premise survives even if the reason for the closure remains unresolved.

## Mechanically rich version

A later authored site may explain the interruption through environmental damage, unstable terrain, work crews, authority restriction, Pokémon activity or deliberate interference. The exact cause requires canon review and a separate evidence owner.

Possible non-KO objectives:
- inspect several route markers;
- escort a surveyor or maintenance worker;
- recover monitoring equipment;
- document the condition before it changes again;
- keep a temporary bypass usable while others cross;
- withdraw safely after obtaining enough evidence.

## Permanent engine dependency classification

Targeting/footprints/range/LoS: VERIFIED only for audited ordinary tactical contracts if the rich version uses ordinary targeting.

Base movement legality: VERIFIED within audited ordinary contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL; required only if the rich version adds displacement, interception or forced-movement hazards.

Core calculations: VERIFIED within audited deterministic contracts.

Action economy/initiative: VERIFIED for audited primitives; no blanket lifecycle inference.

Full turn/round lifecycle: PARTIAL; required if the rich version depends on multi-round phase timing.

Full stateful damage pipeline: PARTIAL; required for authoritative tactical damage consequences.

Status lifecycle: PARTIAL; required for persistent or complex status consequences.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism. A dynamic weather closure, hazard zone or reaction-triggered crossing requires exact evidence before admission.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED. Existing Intimidate rollover evidence proves only that specific seam.

Items: INDIVIDUALLY GATED.

Trainer Features/perks: INDIVIDUALLY GATED.

AI legal-action infrastructure: VERIFIED for ordinary audited actions.

AI tactical policy: BLOCKING for route-clearing, escort, protect-equipment/noncombatant, search, rescue-first, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING for persistent route/closure/objective identity, visible non-KO objective acknowledgement and authoritative end-to-end tactical result playback.

## Canon questions

No location, institution, species, cause or communication technology is canonized here.

Before promotion, choose an established Ouros/Caelo route network and institution that can support this event, then verify local species/habitat and communications against project authority.

## Provenance boundary

`TRAVEL_REPLAN_REQUIRED` proves only that the recorded travel could not continue on its planned route under the preserved conditions.

A later open route does not erase that interruption. It is a later fact.

`ROUTE_REOPENED_LATER != INTERRUPTION_NEVER_HAPPENED`
